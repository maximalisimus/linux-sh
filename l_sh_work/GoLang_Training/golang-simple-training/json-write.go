package main
import (
    "io/ioutil"
    "encoding/json"
)
type Window struct {
    Width int `json:"width"`
    Height int `json:"height"`
    X int `json:"x"`
    Y int `json:"y"`
}
type Config struct {
    Timeout float32 `json:"timeout"`
    PluginsPath string `json:"pluginsPath"`
    Window Window `json:"window"`
}
func main() {
    config := Config {
        Timeout: 40.420,
        PluginsPath: "~/plugins/etc",
        Window: Window {500, 200, 20, 20},
    }
    bytes, _ := json.MarshalIndent(config, "", "  ")
    ioutil.WriteFile("config.json", bytes, 0644)
}
