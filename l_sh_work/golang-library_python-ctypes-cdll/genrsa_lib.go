package main


import (
	"crypto/rand"
	"crypto/rsa"
	"crypto/x509"
	"encoding/pem"
	"fmt"
	"os"
)

import "C"

func New(size int) (*rsa.PrivateKey, error) {

	privateKey, err := rsa.GenerateKey(rand.Reader, size)
	if err != nil {
		return privateKey, err
	}
 
	return privateKey, nil
}

func PrivateKeyToPemString(k *rsa.PrivateKey) string {
	return string(
		pem.EncodeToMemory(
			&pem.Block{
				Type: "RSA PRIVATE KEY",
				Bytes: x509.MarshalPKCS1PrivateKey(k),
			},
		),
	)
}

func PublicKeyToPemString(k *rsa.PublicKey) string {
	return string(
		pem.EncodeToMemory(
			&pem.Block{
				Type: "RSA PUBLIC KEY",
				Bytes: x509.MarshalPKCS1PublicKey(k),
			},
		),
	)
}

//export GenRsa
func GenRsa(length int) {
	key, err := New(length)
	if err != nil {
		//panic(err)
		fmt.Println(err.Error())
	}
	filekey, err := os.Create("private-key.gpg")
	if err != nil{
		fmt.Println("Unable to create file:", err) 
		fmt.Println(err.Error())
	}
	defer filekey.Close() 
	filekey.WriteString(PrivateKeyToPemString(key))
	filekey, err = os.Create("public-key.gpg")
	if err != nil{
		fmt.Println("Unable to create file:", err) 
		fmt.Println(err.Error())
	}
	defer filekey.Close() 
	filekey.WriteString(PublicKeyToPemString(&key.PublicKey))
}

func main() {
	//GenRsa(4096)
	// fmt.Println(GenRsa(4096))
}

// go build -o genrsa_lib.so -buildmode=c-shared genrsa_lib.go
