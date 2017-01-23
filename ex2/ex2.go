// Go 1.2
// go run helloworld_go.go

package main

import (
	. "fmt"
	//"runtime"
	//"time"
)

var i int


func increase_i(total_steps int,channel chan int, incr_done chan int) {
	for k := 0; k < total_steps; k++ {
		//println(i)
		a:=<-channel
		a++
		channel<-a
		
	}
	incr_done<-1
}

func decrease_i(total_steps int, channel chan int, decr_done chan int) {
	for k := 0; k < total_steps+2; k++ {
		//println(i)
		b:=<-channel
		b--
		channel<-b
	}
	decr_done<-1
}

func main() {
	total_steps := 1000000
	channel:=make(chan int,1)
	incr_done:= make(chan int,1)
	decr_done:= make(chan int,1)

	go increase_i(total_steps,channel, incr_done) // This spawns someGoroutine() as a goroutine
	go decrease_i(total_steps,channel,decr_done) // We have no way to wait for the completion of a goroutine (without additional syncronization of some sort)
	channel<-i
	
	<-incr_done
	<-decr_done
	i:=<-channel
	Println(i)
	Println("Hello from main!")
}
