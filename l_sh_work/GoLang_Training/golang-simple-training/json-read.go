package main
import (
    "fmt"
    "io/ioutil"
    "encoding/json"
)
type Config struct {
    Timeout float32
    PluginsPath string
    Window struct {
        Width int
        Height int
        X int
        Y int
    }
}
func main() {

    bytes, err := ioutil.ReadFile("config.json")

    if err != nil {
        fmt.Println("Unable to load config file!")
        return
    }

    var config Config
    err = json.Unmarshal(bytes, &config)

    if err != nil {
        fmt.Println("JSON decode error!")
        return
    }

    fmt.Println(config) // {50.3 ~/plugins/ {500 200 500 500}}
}
