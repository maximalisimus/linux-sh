package main

import (
	"fmt"
	"log"
	"os"
	"path/filepath"
	"strings"
)

func main() {

	var files []string
	
	root := "."
	
	fmt.Println("List by ReadDir")
	fmt.Println()
	err := filepath.Walk(root,
		func(path string, info os.FileInfo, err error) error {
			if err != nil {
				return err
			}
		//fmt.Println(path, info.Size())
		files = append(files, path)
		return nil
	})
	if err != nil {
		log.Println(err)
	}
	sep := fmt.Sprint(os.PathSeparator)
	for _, file := range files {
        fi, err := os.Stat(file)
		if err != nil {
			panic(err)
		}
		mode := fi.Mode()
		if mode.IsDir() {
			outdir := strings.Split(string(file), sep)
			fmt.Printf("[%s: %s]\n", outdir[len(outdir)-1], file)
		} else {
			fmt.Println(filepath.Base(file))
		}
    }
}

