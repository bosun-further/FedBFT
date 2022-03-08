// Copyright 2015 gRPC authors.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.26.0
// 	protoc        v3.6.1
// source: p4p/p4p/user/p4p/users.proto

package p4p

import (
	protoreflect "google.golang.org/protobuf/reflect/protoreflect"
	protoimpl "google.golang.org/protobuf/runtime/protoimpl"
	reflect "reflect"
	sync "sync"
)

const (
	// Verify that this generated code is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(20 - protoimpl.MinVersion)
	// Verify that runtime/protoimpl is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(protoimpl.MaxVersion - 20)
)

// The request message containing the user's name.
type UserSRequest struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Name string `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
}

func (x *UserSRequest) Reset() {
	*x = UserSRequest{}
	if protoimpl.UnsafeEnabled {
		mi := &file_p4p_p4p_user_p4p_users_proto_msgTypes[0]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *UserSRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*UserSRequest) ProtoMessage() {}

func (x *UserSRequest) ProtoReflect() protoreflect.Message {
	mi := &file_p4p_p4p_user_p4p_users_proto_msgTypes[0]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use UserSRequest.ProtoReflect.Descriptor instead.
func (*UserSRequest) Descriptor() ([]byte, []int) {
	return file_p4p_p4p_user_p4p_users_proto_rawDescGZIP(), []int{0}
}

func (x *UserSRequest) GetName() string {
	if x != nil {
		return x.Name
	}
	return ""
}

type BytesDataSRequest struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Data string `protobuf:"bytes,1,opt,name=data,proto3" json:"data,omitempty"`
}

func (x *BytesDataSRequest) Reset() {
	*x = BytesDataSRequest{}
	if protoimpl.UnsafeEnabled {
		mi := &file_p4p_p4p_user_p4p_users_proto_msgTypes[1]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *BytesDataSRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*BytesDataSRequest) ProtoMessage() {}

func (x *BytesDataSRequest) ProtoReflect() protoreflect.Message {
	mi := &file_p4p_p4p_user_p4p_users_proto_msgTypes[1]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use BytesDataSRequest.ProtoReflect.Descriptor instead.
func (*BytesDataSRequest) Descriptor() ([]byte, []int) {
	return file_p4p_p4p_user_p4p_users_proto_rawDescGZIP(), []int{1}
}

func (x *BytesDataSRequest) GetData() string {
	if x != nil {
		return x.Data
	}
	return ""
}

// The response message containing the greetings
type UserSReply struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Message string `protobuf:"bytes,1,opt,name=message,proto3" json:"message,omitempty"`
}

func (x *UserSReply) Reset() {
	*x = UserSReply{}
	if protoimpl.UnsafeEnabled {
		mi := &file_p4p_p4p_user_p4p_users_proto_msgTypes[2]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *UserSReply) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*UserSReply) ProtoMessage() {}

func (x *UserSReply) ProtoReflect() protoreflect.Message {
	mi := &file_p4p_p4p_user_p4p_users_proto_msgTypes[2]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use UserSReply.ProtoReflect.Descriptor instead.
func (*UserSReply) Descriptor() ([]byte, []int) {
	return file_p4p_p4p_user_p4p_users_proto_rawDescGZIP(), []int{2}
}

func (x *UserSReply) GetMessage() string {
	if x != nil {
		return x.Message
	}
	return ""
}

var File_p4p_p4p_user_p4p_users_proto protoreflect.FileDescriptor

var file_p4p_p4p_user_p4p_users_proto_rawDesc = []byte{
	0x0a, 0x1c, 0x70, 0x34, 0x70, 0x2f, 0x70, 0x34, 0x70, 0x2f, 0x75, 0x73, 0x65, 0x72, 0x2f, 0x70,
	0x34, 0x70, 0x2f, 0x75, 0x73, 0x65, 0x72, 0x73, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x12, 0x10,
	0x70, 0x34, 0x70, 0x2e, 0x70, 0x34, 0x70, 0x2e, 0x75, 0x73, 0x65, 0x72, 0x2e, 0x70, 0x34, 0x70,
	0x22, 0x22, 0x0a, 0x0c, 0x55, 0x73, 0x65, 0x72, 0x53, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74,
	0x12, 0x12, 0x0a, 0x04, 0x6e, 0x61, 0x6d, 0x65, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x04,
	0x6e, 0x61, 0x6d, 0x65, 0x22, 0x27, 0x0a, 0x11, 0x42, 0x79, 0x74, 0x65, 0x73, 0x44, 0x61, 0x74,
	0x61, 0x53, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x12, 0x12, 0x0a, 0x04, 0x64, 0x61, 0x74,
	0x61, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x04, 0x64, 0x61, 0x74, 0x61, 0x22, 0x26, 0x0a,
	0x0a, 0x55, 0x73, 0x65, 0x72, 0x53, 0x52, 0x65, 0x70, 0x6c, 0x79, 0x12, 0x18, 0x0a, 0x07, 0x6d,
	0x65, 0x73, 0x73, 0x61, 0x67, 0x65, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x07, 0x6d, 0x65,
	0x73, 0x73, 0x61, 0x67, 0x65, 0x32, 0xf4, 0x01, 0x0a, 0x05, 0x55, 0x73, 0x65, 0x72, 0x53, 0x12,
	0x4a, 0x0a, 0x08, 0x53, 0x61, 0x79, 0x48, 0x65, 0x6c, 0x6c, 0x6f, 0x12, 0x1e, 0x2e, 0x70, 0x34,
	0x70, 0x2e, 0x70, 0x34, 0x70, 0x2e, 0x75, 0x73, 0x65, 0x72, 0x2e, 0x70, 0x34, 0x70, 0x2e, 0x55,
	0x73, 0x65, 0x72, 0x53, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x1a, 0x1c, 0x2e, 0x70, 0x34,
	0x70, 0x2e, 0x70, 0x34, 0x70, 0x2e, 0x75, 0x73, 0x65, 0x72, 0x2e, 0x70, 0x34, 0x70, 0x2e, 0x55,
	0x73, 0x65, 0x72, 0x53, 0x52, 0x65, 0x70, 0x6c, 0x79, 0x22, 0x00, 0x12, 0x4e, 0x0a, 0x07, 0x53,
	0x61, 0x79, 0x44, 0x61, 0x74, 0x61, 0x12, 0x23, 0x2e, 0x70, 0x34, 0x70, 0x2e, 0x70, 0x34, 0x70,
	0x2e, 0x75, 0x73, 0x65, 0x72, 0x2e, 0x70, 0x34, 0x70, 0x2e, 0x42, 0x79, 0x74, 0x65, 0x73, 0x44,
	0x61, 0x74, 0x61, 0x53, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x1a, 0x1c, 0x2e, 0x70, 0x34,
	0x70, 0x2e, 0x70, 0x34, 0x70, 0x2e, 0x75, 0x73, 0x65, 0x72, 0x2e, 0x70, 0x34, 0x70, 0x2e, 0x55,
	0x73, 0x65, 0x72, 0x53, 0x52, 0x65, 0x70, 0x6c, 0x79, 0x22, 0x00, 0x12, 0x4f, 0x0a, 0x0d, 0x53,
	0x61, 0x79, 0x48, 0x65, 0x6c, 0x6c, 0x6f, 0x41, 0x67, 0x61, 0x69, 0x6e, 0x12, 0x1e, 0x2e, 0x70,
	0x34, 0x70, 0x2e, 0x70, 0x34, 0x70, 0x2e, 0x75, 0x73, 0x65, 0x72, 0x2e, 0x70, 0x34, 0x70, 0x2e,
	0x55, 0x73, 0x65, 0x72, 0x53, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x1a, 0x1c, 0x2e, 0x70,
	0x34, 0x70, 0x2e, 0x70, 0x34, 0x70, 0x2e, 0x75, 0x73, 0x65, 0x72, 0x2e, 0x70, 0x34, 0x70, 0x2e,
	0x55, 0x73, 0x65, 0x72, 0x53, 0x52, 0x65, 0x70, 0x6c, 0x79, 0x22, 0x00, 0x42, 0x5f, 0x0a, 0x1d,
	0x69, 0x6f, 0x2e, 0x67, 0x72, 0x70, 0x63, 0x2e, 0x65, 0x78, 0x61, 0x6d, 0x70, 0x6c, 0x65, 0x73,
	0x2e, 0x70, 0x34, 0x70, 0x2e, 0x70, 0x34, 0x70, 0x2e, 0x75, 0x73, 0x65, 0x72, 0x42, 0x0a, 0x55,
	0x73, 0x65, 0x72, 0x53, 0x50, 0x72, 0x6f, 0x74, 0x6f, 0x50, 0x01, 0x5a, 0x30, 0x67, 0x6f, 0x6f,
	0x67, 0x6c, 0x65, 0x2e, 0x67, 0x6f, 0x6c, 0x61, 0x6e, 0x67, 0x2e, 0x6f, 0x72, 0x67, 0x2f, 0x67,
	0x72, 0x70, 0x63, 0x2f, 0x65, 0x78, 0x61, 0x6d, 0x70, 0x6c, 0x65, 0x73, 0x2f, 0x70, 0x34, 0x70,
	0x2f, 0x70, 0x34, 0x70, 0x2f, 0x75, 0x73, 0x65, 0x72, 0x2f, 0x70, 0x34, 0x70, 0x62, 0x06, 0x70,
	0x72, 0x6f, 0x74, 0x6f, 0x33,
}

var (
	file_p4p_p4p_user_p4p_users_proto_rawDescOnce sync.Once
	file_p4p_p4p_user_p4p_users_proto_rawDescData = file_p4p_p4p_user_p4p_users_proto_rawDesc
)

func file_p4p_p4p_user_p4p_users_proto_rawDescGZIP() []byte {
	file_p4p_p4p_user_p4p_users_proto_rawDescOnce.Do(func() {
		file_p4p_p4p_user_p4p_users_proto_rawDescData = protoimpl.X.CompressGZIP(file_p4p_p4p_user_p4p_users_proto_rawDescData)
	})
	return file_p4p_p4p_user_p4p_users_proto_rawDescData
}

var file_p4p_p4p_user_p4p_users_proto_msgTypes = make([]protoimpl.MessageInfo, 3)
var file_p4p_p4p_user_p4p_users_proto_goTypes = []interface{}{
	(*UserSRequest)(nil),      // 0: p4p.p4p.user.p4p.UserSRequest
	(*BytesDataSRequest)(nil), // 1: p4p.p4p.user.p4p.BytesDataSRequest
	(*UserSReply)(nil),        // 2: p4p.p4p.user.p4p.UserSReply
}
var file_p4p_p4p_user_p4p_users_proto_depIdxs = []int32{
	0, // 0: p4p.p4p.user.p4p.UserS.SayHello:input_type -> p4p.p4p.user.p4p.UserSRequest
	1, // 1: p4p.p4p.user.p4p.UserS.SayData:input_type -> p4p.p4p.user.p4p.BytesDataSRequest
	0, // 2: p4p.p4p.user.p4p.UserS.SayHelloAgain:input_type -> p4p.p4p.user.p4p.UserSRequest
	2, // 3: p4p.p4p.user.p4p.UserS.SayHello:output_type -> p4p.p4p.user.p4p.UserSReply
	2, // 4: p4p.p4p.user.p4p.UserS.SayData:output_type -> p4p.p4p.user.p4p.UserSReply
	2, // 5: p4p.p4p.user.p4p.UserS.SayHelloAgain:output_type -> p4p.p4p.user.p4p.UserSReply
	3, // [3:6] is the sub-list for method output_type
	0, // [0:3] is the sub-list for method input_type
	0, // [0:0] is the sub-list for extension type_name
	0, // [0:0] is the sub-list for extension extendee
	0, // [0:0] is the sub-list for field type_name
}

func init() { file_p4p_p4p_user_p4p_users_proto_init() }
func file_p4p_p4p_user_p4p_users_proto_init() {
	if File_p4p_p4p_user_p4p_users_proto != nil {
		return
	}
	if !protoimpl.UnsafeEnabled {
		file_p4p_p4p_user_p4p_users_proto_msgTypes[0].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*UserSRequest); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_p4p_p4p_user_p4p_users_proto_msgTypes[1].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*BytesDataSRequest); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_p4p_p4p_user_p4p_users_proto_msgTypes[2].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*UserSReply); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_p4p_p4p_user_p4p_users_proto_rawDesc,
			NumEnums:      0,
			NumMessages:   3,
			NumExtensions: 0,
			NumServices:   1,
		},
		GoTypes:           file_p4p_p4p_user_p4p_users_proto_goTypes,
		DependencyIndexes: file_p4p_p4p_user_p4p_users_proto_depIdxs,
		MessageInfos:      file_p4p_p4p_user_p4p_users_proto_msgTypes,
	}.Build()
	File_p4p_p4p_user_p4p_users_proto = out.File
	file_p4p_p4p_user_p4p_users_proto_rawDesc = nil
	file_p4p_p4p_user_p4p_users_proto_goTypes = nil
	file_p4p_p4p_user_p4p_users_proto_depIdxs = nil
}