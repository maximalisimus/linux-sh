package main
import (
    "fmt"
    "encoding/json"
    "strings"
)
type Person struct {
    Name string `json:"name"`
    Age int `json:"age"`
    Email string `json:"-"`
}
func main() {
    persons := []Person {
            Person {"James Henrick", 25, "james.h@gmail.com"},
            Person {"David Rick", 30, "rick.dvd@yahoo.com"},
    }
    bytes, _ := json.MarshalIndent(persons, "", "  ")
    fmt.Println(string(bytes))
}
func (p *Person) MarshalJSON() ([]byte, error) {
    type PersonAlias Person
    return json.Marshal(&struct{
        *PersonAlias
        Email string `json:"email"`
    }{
        PersonAlias: (*PersonAlias)(p),
        Email: strings.Repeat("*", 4) + "@mail.com", // alter email
    })
}
