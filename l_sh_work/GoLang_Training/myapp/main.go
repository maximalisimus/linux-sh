package main
 
import (
	"fmt"
	"log"
	//"os"
	"myapp/pki"
)

func main() {
	/*
	key, err := pki.New()
	if err != nil {
		log.Fatalln(err)
	}
	//fmt.Println(key.PublicKeyToPemString())
	//fmt.Println(key.PrivateKeyToPemString())
	
	publicfile, err := os.Create("./certs/public.key")
	if err != nil{
		fmt.Println("Unable to create file:", err) 
		os.Exit(1) 
	}
	defer publicfile.Close() 
	publicfile.WriteString(key.PublicKeyToPemString())
	
	privatefile, err := os.Create("./certs/private.key")
	if err != nil{
		fmt.Println("Unable to create file:", err) 
		os.Exit(1) 
	}
	defer privatefile.Close() 
	privatefile.WriteString(key.PrivateKeyToPemString())
	*/
	
	plainText := "This is a very secret message :)"
 
	encryptedMessage, err := pki.Encrypt("./certs/public.key", plainText)
	if err != nil {
		log.Fatalln(err)
	}
	fmt.Println(encryptedMessage)
	
	//encryptedMessage = ""
	// This is the incoming encrypted text as shown above.
 
	decryptedMessage, err := pki.Decrypt("./certs/private.key", encryptedMessage)
	if err != nil {
		log.Fatalln(err)
	}
	fmt.Println(decryptedMessage)
}
