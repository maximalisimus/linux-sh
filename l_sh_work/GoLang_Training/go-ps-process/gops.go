package main

import (
	"fmt"
	ps "github.com/mitchellh/go-ps"
)

func main(){
	processList, err := ps.Processes()
	if err != nil {
		fmt.Println("ps.Processes() Failed, are you using windows?")
		return
	}

	// map ages
	for x := range processList {
		var process ps.Process
		process = processList[x]
		fmt.Printf("%d\t%s\n",process.Pid(),process.Executable())
		// do os.* stuff on the pid
	}
}
