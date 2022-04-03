package main

import (
	"os"
	"fmt"
	"log"
)

func main() {
	dirname, err := os.UserHomeDir()
	if err != nil {
		log.Fatal( err )
	}
	home_env := dirname + "/.env"
	fmt.Println( home_env )
}
