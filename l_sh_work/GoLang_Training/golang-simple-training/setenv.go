package main

import (
    "fmt"
    "os"
)

func main() {

    fmt.Println("editor:", os.Getenv("MYEDITOR"))

    os.Setenv("MYEDITOR", "leafpad")

    fmt.Println("editor:", os.Getenv("MYEDITOR"))
}
