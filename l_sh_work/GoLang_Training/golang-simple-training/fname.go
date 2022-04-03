package main

import (
	"fmt"
	"os"
)

func main() {
	
	root := "config.json"
	fi, err := os.Stat(root)
	if err != nil {
		panic(err)
	}
	mode := fi.Mode()
	fmt.Printf("%s\n", fi.Name()) // fmt.Printf("%v\n", fi.Name())
	fmt.Printf("%t\n", fi.IsDir())
	fmt.Printf("%s\n", mode)
}
