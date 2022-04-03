package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"os"
	"strconv"
)

type Users struct {
	Users []User `json:"users"`
}

type User struct {
	Name   string `json:"name"`
	Type   string `json:"type"`
	Age    int    `json:"Age"`
	Social Social `json:"social"`
}

type Social struct {
	Facebook string `json:"facebook"`
	Twitter  string `json:"twitter"`
}

func main() {
	jsonEdit := "edit.json"
	
	jsonFile := "users.json"
	if _, err := os.Stat(jsonFile); err != nil {
		//fmt.Printf("File does not exist\n"); 
		panic(err) 
	}
	byteValue, _ := ioutil.ReadFile(jsonFile)
	var users Users
	json.Unmarshal(byteValue, &users)
	for i := 0; i < len(users.Users); i++ {
		fmt.Println("User Type: " + users.Users[i].Type)
		fmt.Println("User Age: " + strconv.Itoa(users.Users[i].Age))
		fmt.Println("User Name: " + users.Users[i].Name)
		fmt.Println("Facebook Url: " + users.Users[i].Social.Facebook + " " + users.Users[i].Social.Twitter)
	}
	
	users.Users[0].Age = 25
	var newUser User
	newUser.Type = "Editor"
	newUser.Age = 33
	newUser.Name = "Zmey Gorinich"
	newUser.Social.Twitter = "https://twitter.com/"
	newUser.Social.Facebook = "https://facebook.com"
	users.Users = append(users.Users, newUser)
	bytes, _ := json.MarshalIndent(users, "", "\t")
	ioutil.WriteFile(jsonEdit, bytes, 0777)
	fmt.Println("\n")
	
	users.Users = nil

	valueBytes, _ := ioutil.ReadFile(jsonEdit)
	json.Unmarshal(valueBytes, &users)
	for i := 0; i < len(users.Users); i++ {
		fmt.Println("User Type: " + users.Users[i].Type)
		fmt.Println("User Age: " + strconv.Itoa(users.Users[i].Age))
		fmt.Println("User Name: " + users.Users[i].Name)
		fmt.Println("Facebook Url: " + users.Users[i].Social.Facebook + " " + users.Users[i].Social.Twitter)
	}
}
