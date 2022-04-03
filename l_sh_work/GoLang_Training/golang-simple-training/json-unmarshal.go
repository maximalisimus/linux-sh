package main
import (
    "fmt"
    "encoding/json"
)
type Window struct {
    Width int `json:"width"`
    Height int `json:"height"`
    Title string `json:"title"`
}
func main() {
    jsonInput := `{
        "width": 500,
        "height": 200,
        "title": "Hello Go!"
    }`
    var window Window
    err := json.Unmarshal([]byte(jsonInput), &window)

    if err != nil {
        fmt.Println("JSON decode error!")
        return
    }

    fmt.Println(window) // {500 200 Hello Go!}
}
