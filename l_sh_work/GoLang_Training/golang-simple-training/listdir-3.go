package main

import (
	"fmt"
	"log"
	"os"
	"path/filepath"
)

func main() {

	fmt.Println("List by ReadDir")
	fmt.Println()
	err := filepath.Walk(".",
		func(path string, info os.FileInfo, err error) error {
			if err != nil {
				return err
			}
		fmt.Println(path, info.Size())
		return nil
	})
	if err != nil {
		log.Println(err)
	}
}

