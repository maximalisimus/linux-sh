package main

import (
	"fmt"
	ps "github.com/mitchellh/go-ps"
	"strings"
	"os"
)

func main(){
	processList, err := ps.Processes()
	if err != nil {
		fmt.Println("ps.Processes() Failed, are you using windows?")
		return
	}
	//fmt.Println(len(os.Args), os.Args)
	var refString = "thunar"
	if (len(os.Args)>1) {
		//fmt.Println(len(os.Args), os.Args[1])
		refString = os.Args[1]
	}
	//const refString = "thunar"
	// map ages
	for x := range processList {
		var process ps.Process
		process = processList[x]
		contain := strings.Contains(strings.ToLower(process.Executable()),strings.ToLower(refString))
		if (contain) {
			fmt.Printf("%d ",process.Pid())
		}
		//fmt.Printf("%d\t%s\n",process.Pid(),process.Executable())
		// do os.* stuff on the pid
	}
	fmt.Printf("\n")
}
