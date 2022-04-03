// pki/pki package
package pki

import (
	"crypto/rand"
	"crypto/rsa"
	"crypto/sha512"
	"crypto/x509"
	"encoding/pem"
	"io/ioutil"
)

type Key struct {
	publicKey  *rsa.PublicKey
	privateKey *rsa.PrivateKey
}

func New() (Key, error) {
	var k Key
 
	privateKey, err := rsa.GenerateKey(rand.Reader, 4096)
	if err != nil {
		return k, err
	}
 
	k.publicKey = &privateKey.PublicKey
	k.privateKey = privateKey
 
	return k, nil
}

func (k Key) PublicKeyToPemString() string {
	return string(
		pem.EncodeToMemory(
			&pem.Block{
				Type: "RSA PUBLIC KEY",
				Bytes: x509.MarshalPKCS1PublicKey(k.publicKey),
			},
		),
	)
}

func (k Key) PrivateKeyToPemString() string {
	return string(
		pem.EncodeToMemory(
			&pem.Block{
				Type: "RSA PRIVATE KEY",
				Bytes: x509.MarshalPKCS1PrivateKey(k.privateKey),
			},
		),
	)
}

func Encrypt(publicKeyPath, plainText string) (string, error) {
	bytes, err := ioutil.ReadFile(publicKeyPath)
	if err != nil {
		return "", err
	}
 
	publicKey, err := convertBytesToPublicKey(bytes)
	if err != nil {
		return "", err
	}
 
	cipher, err := rsa.EncryptOAEP(sha512.New(), rand.Reader, publicKey, []byte(plainText), nil)
	if err != nil {
		return "", err
	}
 
	return cipherToPemString(cipher), nil
}

func convertBytesToPublicKey(keyBytes []byte) (*rsa.PublicKey, error) {
	var err error
 
	block, _ := pem.Decode(keyBytes)
	blockBytes := block.Bytes
	ok := x509.IsEncryptedPEMBlock(block)
 
	if ok {
		blockBytes, err = x509.DecryptPEMBlock(block, nil)
		if err != nil {
			return nil, err
		}
	}

	publicKey, err := x509.ParsePKCS1PublicKey(blockBytes)
	if err != nil {
		return nil, err
	}
 
	return publicKey, nil
}

func cipherToPemString(cipher []byte) string {
	return string(
		pem.EncodeToMemory(
			&pem.Block{
				Type: "MESSAGE",
				Bytes: cipher,
			},
		),
	)
}

func Decrypt(privateKeyPath, encryptedMessage string) (string, error) {
	bytes, err := ioutil.ReadFile(privateKeyPath)
	if err != nil {
		return "", err
	}
 
	privateKey, err := convertBytesToPrivateKey(bytes)
	if err != nil {
		return "", err
	}
 
	plainMessage, err := rsa.DecryptOAEP(
		sha512.New(),
		rand.Reader,
		privateKey,
		pemStringToCipher(encryptedMessage),
		nil,
	)
 
	return string(plainMessage), err
}

func convertBytesToPrivateKey(keyBytes []byte) (*rsa.PrivateKey, error) {
	var err error
 
	block, _ := pem.Decode(keyBytes)
	blockBytes := block.Bytes
	ok := x509.IsEncryptedPEMBlock(block)
 
	if ok {
		blockBytes, err = x509.DecryptPEMBlock(block, nil)
		if err != nil {
			return nil, err
		}
	}
 
	privateKey, err := x509.ParsePKCS1PrivateKey(blockBytes)
	if err != nil {
		return nil, err
	}
 
	return privateKey, nil
}

func pemStringToCipher(encryptedMessage string) []byte {
	b, _ := pem.Decode([]byte(encryptedMessage))
 
	return b.Bytes
}
