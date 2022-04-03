package main

import (
	"fmt"
	"math/rand"
	"time"
)

func main() {
	rand.Seed(time.Now().UnixNano())
	fmt.Printf("%d\n", rand.Int63())
	//generator := rand.New(rand.NewSource(time.Now().UnixNano()))
	//fmt.Printf("%d\n", generator.Int63())
	a:=0
	b:=100
	n := a + rand.Intn(b-a+1) // a ≤ n ≤ b
	fmt.Printf("%d\n", n)
	c := 'a' + rune(rand.Intn('z'-'a'+1)) // 'a' ≤ c ≤ 'z'
	fmt.Printf("%c\n", c)
	chars := []rune("AB⌘")
	c = chars[rand.Intn(len(chars))]
	fmt.Printf("%c\n", c)
}
