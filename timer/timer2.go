package main

// https://studygolang.com/articles/25634
import (
	"fmt"
	"time"
)

func AsyncService(service func() string) chan string {
	retCh := make(chan string, 1)
	go func() {
		ret := service()
		fmt.Println("service()执行结束.")
		retCh <- ret
		fmt.Println("service()返回值塞进通道.")
	}()
	return retCh
}

func AsyncServiceOut(service func() string, duration time.Duration) {
	select {
	case ret := <-AsyncService(service):
		fmt.Println("====", ret)
	case <-time.After(duration):
		fmt.Println("time out")
	}
}

func main() {
	service := func() string {
		time.Sleep(3e9)
		return "service()的返回值"
	}
	AsyncServiceOut(service, 2e9)

	time.Sleep(7e9)
}
