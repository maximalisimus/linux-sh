package main

import (
	"fmt"
	"runtime"
)

func main() {
	// Variant-1
	os := runtime.GOOS
	switch os {
	case "windows":
		fmt.Println("Windows")
	case "darwin":
		fmt.Println("MAC operating system")
	case "linux":
		fmt.Println("Linux")
	default:
		fmt.Printf("%s.\n", os)
	}

	// Variant-2
	myos := fmt.Sprint(runtime.GOOS)
	// Detect Windows
	if myos == "windows" {
		fmt.Println("Windows OS detected")
	}
	// Detect Linux
	if myos == "linux" {    // also can be specified to FreeBSD
		fmt.Println("Unix/Linux type OS detected")
	}
	// Detect Mac OS/X
	if myos == "darwin" {
		fmt.Println("Mac OS detected")
	}
}
