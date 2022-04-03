package main
import (
    "fmt"
    "encoding/json"
)
type Seller struct {
    Id int `json:"id"`
    Name string `json:"name"`
    CountryCode string `json:"country_code,omitempty"`
}
type Product struct {
    Id int `json:"-"`
    Name string `json:"name"`
    Seller Seller `json:"seller"`
    Price int `json:"price"`
}
func main() {
    products := []Product{
        Product {
            Id: 50,
            Name: "Writing Book",
            Seller: Seller {Id: 1, Name: "ABC Company", CountryCode: "US"},
            Price: 100,
        },
        Product {
            Id: 51,
            Name: "Kettle",
            Seller: Seller {Id: 20, Name: "John Store"},
            Price: 500,
        },
    }
    bytes, _ := json.MarshalIndent(products, "", "\t")
    fmt.Println(string(bytes))
}
