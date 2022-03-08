/*
 *
 * Copyright 2015 gRPC authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 *
 */

// Package main implements a simple gRPC client that demonstrates how to use gRPC-Go libraries
// to perform unary, client streaming, server streaming and full duplex RPCs.
//
// It interacts with the route guide service whose definition can be found in routeguide/route_guide.proto.
package client

import (
	"context"
	"encoding/json"
	"flag"
	"fmt"
	"io"
	"io/ioutil"
	"log"
	"math/rand"
	"os"
	"time"

	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials"
	"google.golang.org/grpc/examples/data"
	pb "google.golang.org/grpc/examples/p4p/p4p/sim/p4p"
)

var (
	tls                = flag.Bool("tls", false, "Connection uses TLS if true, else plain TCP")
	caFile             = flag.String("ca_file", "", "The file containing the CA root cert file")
	p4pCoordinate_Addr = flag.String("addr", "localhost:8980", "The server address in the format of host:port")
	serverHostOverride = flag.String("server_host_override", "x.test.example.com", "The server name used to verify the hostname returned by the TLS handshake")
)

type AutoGenerated struct {
	Feature []Feature `json:"feature"`
}
type Location struct {
	Latitude  int `json:"latitude"`
	Longitude int `json:"longitude"`
}
type Feature struct {
	Location Location `json:"location"`
	Name     string   `json:"name"`
}

// printFeature gets the feature for the given point.
func printFeature(client pb.P4PCoordianteClient, point *pb.Point) {
	log.Printf("Getting feature for point (%d, %d)", point.Latitude, point.Longitude)
	ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
	defer cancel()
	feature, err := client.GetFeature(ctx, point)
	if err != nil {
		log.Println("%v.GetFeatures(_) = _, %v: ", client, err)
	}
	log.Println(feature)
}

func printWrap(client pb.P4PCoordianteClient, mtype string) {
	var point *pb.Point
	point = machineType(mtype)
	printFeature(client, point)
}

func machineType(mtype string) *pb.Point {
	fmt.Println("mtype:", mtype)
	jsonFile, err1 := os.Open("/root/FedBFT/voting/testdata/route_guide_db.json")
	// 最好要处理以下错误
	if err1 != nil {
		fmt.Println(err1)
	}
	// 要记得关闭
	defer jsonFile.Close()

	byteValue, _ := ioutil.ReadAll(jsonFile)
	var mapResult map[string]interface{}
	err2 := json.Unmarshal([]byte(string(byteValue)), &mapResult)
	if err2 != nil {
		fmt.Println("JsonToMapDemo err2: ", err2)
	}
	fmt.Println(mapResult["feature"])

	var ag AutoGenerated
	json.Unmarshal(byteValue, &ag)
	fmt.Println(ag)

	// var mapResult2 map[string]interface{}
	// makeRe

	// map[string] innerMap := mapResult["feature"]
	// print map
	for i, s := range ag.Feature {
		fmt.Println(i, s.Location.Latitude)
		fmt.Print("s.Name: ", s.Name)
		if mtype == s.Name {
			return &pb.Point{Latitude: int32(s.Location.Latitude), Longitude: int32(s.Location.Longitude)}
		}
	}

	return &pb.Point{Latitude: 0, Longitude: 0}
	// fmt.Println(string(byteValue.feature))
}

// printFeatures lists all the features within the given bounding Rectangle.
func printFeatures(client pb.P4PCoordianteClient, rect *pb.Rectangle) {
	log.Printf("Looking for features within %v", rect)
	ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
	defer cancel()
	stream, err := client.ListFeatures(ctx, rect)
	if err != nil {
		log.Fatalf("%v.ListFeatures(_) = _, %v", client, err)
	}
	for {
		feature, err := stream.Recv()
		if err == io.EOF {
			break
		}
		if err != nil {
			log.Fatalf("%v.ListFeatures(_) = _, %v", client, err)
		}
		log.Printf("Feature: name: %q, point:(%v, %v)", feature.GetName(),
			feature.GetLocation().GetLatitude(), feature.GetLocation().GetLongitude())
	}
}

// runRecordRoute sends a sequence of points to server and expects to get a RouteSummary from server.
func runRecordRoute(client pb.P4PCoordianteClient) {
	// Create a random number of random points
	r := rand.New(rand.NewSource(time.Now().UnixNano()))
	// pointCount := int(r.Int31n(100)) + 2 // Traverse at least two points
	pointCount := 1 // Traverse at least two points
	var points []*pb.Point
	for i := 0; i < pointCount; i++ {
		points = append(points, randomPoint(r))
	}
	log.Printf("Traversing %d points.", len(points))
	ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
	defer cancel()
	stream, err := client.RecordRoute(ctx)
	if err != nil {
		log.Fatalf("%v.RecordRoute(_) = _, %v", client, err)
	}
	for _, point := range points {
		if err := stream.Send(point); err != nil {
			log.Fatalf("%v.Send(%v) = %v", stream, point, err)
		}
	}
	reply, err := stream.CloseAndRecv()
	if err != nil {
		log.Fatalf("%v.CloseAndRecv() got error %v, want %v", stream, err, nil)
	}
	log.Printf("Route summary: %v", reply)
}

// runRouteChat receives a sequence of route notes, while sending notes for various locations.
func runRouteChat(client pb.P4PCoordianteClient) {
	notes := []*pb.RouteNote{
		{Location: &pb.Point{Latitude: 0, Longitude: 1}, Message: "First message"},
		// {Location: &pb.Point{Latitude: 0, Longitude: 2}, Message: "Second message"},
		// {Location: &pb.Point{Latitude: 0, Longitude: 3}, Message: "Third message"},
		// {Location: &pb.Point{Latitude: 0, Longitude: 1}, Message: "Fourth message"},
		// {Location: &pb.Point{Latitude: 0, Longitude: 2}, Message: "Fifth message"},
		// {Location: &pb.Point{Latitude: 0, Longitude: 3}, Message: "Sixth message"},
	}

	ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
	defer cancel()
	stream, err := client.RouteChat(ctx)
	if err != nil {
		log.Fatalf("%v.RouteChat(_) = _, %v", client, err)
	}
	waitc := make(chan struct{})
	go func() {
		for {
			in, err := stream.Recv()
			if err == io.EOF {
				// read done.
				close(waitc)
				return
			}
			if err != nil {
				log.Fatalf("Failed to receive a note : %v", err)
			}
			log.Printf("Got message %s at point(%d, %d)", in.Message, in.Location.Latitude, in.Location.Longitude)
		}
	}()
	for _, note := range notes {
		if err := stream.Send(note); err != nil {
			log.Fatalf("Failed to send a note: %v", err)
		}
	}
	stream.CloseSend()
	<-waitc
}

func randomPoint(r *rand.Rand) *pb.Point {
	lat := (r.Int31n(180) - 90) * 1e7
	long := (r.Int31n(360) - 180) * 1e7
	return &pb.Point{Latitude: lat, Longitude: long}
}

func Main_c(x string) string {
	flag.Parse()
	var opts []grpc.DialOption
	if *tls {
		if *caFile == "" {
			*caFile = data.Path("x509/ca_cert.pem")
		}
		creds, err := credentials.NewClientTLSFromFile(*caFile, *serverHostOverride)
		if err != nil {
			log.Fatalf("Failed to create TLS credentials %v", err)
		}
		opts = append(opts, grpc.WithTransportCredentials(creds))
	} else {
		opts = append(opts, grpc.WithInsecure())
	}

	conn, err := grpc.Dial(*p4pCoordinate_Addr, opts...)
	if err != nil {
		log.Fatalf("fail to dial: %v", err)
	}
	defer conn.Close()
	client := pb.NewP4PCoordianteClient(conn)

	// Looking for a valid feature
	printWrap(client, x)
	// printFeature(client, &pb.Point{Latitude: 1, Longitude: 1})
	// printFeature(client, &pb.Point{Latitude: 2, Longitude: 2})

	// printFeature(client, &pb.Point{Latitude: 2, Longitude: 2})
	// printFeature(client, &pb.Point{Latitude: 9999, Longitude: -8888})
	// // Feature missing.
	// printFeature(client, &pb.Point{Latitude: 0, Longitude: 0})

	// Looking for features between 40, -75 and 42, -73.
	// printFeatures(client, &pb.Rectangle{
	// 	Lo: &pb.Point{Latitude: 400000000, Longitude: -750000000},
	// 	// Hi: &pb.Point{Latitude: 420000000, Longitude: -730000000},

	// 	Hi: &pb.Point{Latitude: 987000000, Longitude: 876000000},
	// })

	// RecordRoute
	runRecordRoute(client)
	return "x"

	// RouteChat
	// runRouteChat(client)
}