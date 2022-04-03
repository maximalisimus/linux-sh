package main

import (
	"encoding/base64"
	"fmt"
	"log"
	"strings"
	"bytes"
)

func main() {	
	var mess string = "Success"
	str := base64.StdEncoding.EncodeToString([]byte(mess))
	
	var codes string = strings.Replace(str,"=","",-1)
	// strings.TrimSuffix(str, "=")
	fmt.Println(codes)
	
	fmt.Println(str)
	
	var buffer bytes.Buffer
	buffer.WriteString(codes)
	// buffer.WriteString("=")
	
	var isstr bool = true
	
	for isstr == true {
		buffer.WriteString("=")
		data, err := base64.StdEncoding.DecodeString(buffer.String())
		if err != nil {
			//log.Fatal("error:", err)
			isstr = true
		} else {
			isstr = false
			fmt.Printf("%q\n", data)
		}
		
	}
	
	data, err := base64.StdEncoding.DecodeString(str)
	if err != nil {
		log.Fatal("error:", err)
		
	}
	fmt.Printf("%q\n", data)
}
