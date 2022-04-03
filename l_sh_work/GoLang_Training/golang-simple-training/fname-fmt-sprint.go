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
	name := fmt.Sprint(fi.Name())
	isdir := fmt.Sprint(fi.IsDir())
	modes := fmt.Sprint(mode)
	fmt.Printf("%s\n", name) // fmt.Printf("%v\n", fi.Name())
	fmt.Printf("%s\n", isdir)
	fmt.Printf("%s\n", modes)
}
