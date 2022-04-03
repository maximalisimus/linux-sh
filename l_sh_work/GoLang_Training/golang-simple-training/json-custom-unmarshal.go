package main
import (
    "fmt"
    "encoding/json"
)
type Config struct {
    FunctionName string 
    Temperature float32
}
func main() {
    jsonInput := `{
        "functionName": "triggerModule",
        "temperature": 4560.32
    }`
    var config Config
    err := json.Unmarshal([]byte(jsonInput), &config)

    if err != nil {
        fmt.Println("JSON decode error!")
        return
    }

    fmt.Println(config) // {triggerModule 4287.17}
}
func (c *Config) UnmarshalJSON(data []byte) error {
    type ConfigAlias Config
    tmp := struct {
        Temperature float32
        *ConfigAlias
    }{
        ConfigAlias: (*ConfigAlias)(c),
    }
    if err := json.Unmarshal(data, &tmp); err != nil {
        return err
    }
    c.Temperature = tmp.Temperature - 273.15
    return nil
}
