package main
 
import (
	//"os"
	//"bufio"
	"bytes"
	"fmt"
	"io/ioutil"
	//"log"
	"strings"
	"encoding/base64"
)
 
func main() {
	
	var hash_env string
	
	home_env := "env.txt"
	
	fContent, err := ioutil.ReadFile(home_env)
	if err != nil {
		panic(err)
	}
	hash_env = strings.TrimSpace(string(fContent))
	fmt.Println(hash_env)
	var buffer bytes.Buffer
	buffer.WriteString(hash_env)
	var codes string
	var isstr bool = true
	for isstr == true {
		buffer.WriteString("=")
		data, err := base64.StdEncoding.DecodeString(buffer.String())
		if err != nil {
			//log.Fatal("error:", err)
			isstr = true
		} else {
			isstr = false
			codes = string(data)
		}
	}
	fmt.Printf("%q\n", codes)
}
