package main
import (
    "fmt"
    "encoding/json"
)
type Seller struct {
    Id int `json:"id"`
    Name string `json:"name"`
    CountryCode string `json:"country_code"`
}
type Product struct {
    Id int `json:"id"`
    Name string `json:"name"`
    Seller Seller `json:"seller"`
    Price int `json:"price"`
}
func main() {
    book := Product{
        Id: 50,
        Name: "Writing Book",
        Seller: Seller {1, "ABC Company", "US"},
        Price: 100,
    }
    bytes, _ := json.MarshalIndent(book, "", "\t")
    fmt.Println(string(bytes))
}
