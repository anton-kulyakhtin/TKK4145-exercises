// Go 1.2
// go run helloworld_go.go

package main

import (
	. "fmt"
	"runtime"
	"time"
)

var i int

func increase_i(total_steps int) {
	for k := 0; k < total_steps; k++ {
		//println(i)
		i++
	}
}

func decrease_i(total_steps int) {
	for k := 0; k < total_steps; k++ {
		//println(i)
		i--
	}
}

func main() {
	total_steps := 1000000
	runtime.GOMAXPROCS(runtime.NumCPU()) // I guess this is a hint to what GOMAXPROCS does...
	// Try doing the exercise both with and without it!
	//go someGoroutine() // This spawns someGoroutine() as a goroutine
	go increase_i(total_steps) // This spawns someGoroutine() as a goroutine
	go decrease_i(total_steps) // We have no way to wait for the completion of a goroutine (without additional syncronization of some sort)
	// We'll come back to using channels in Exercise 2. For now: Sleep.
	time.Sleep(1000 * time.Millisecond)
	Println(i)
	Println("Hello from main!")
}
