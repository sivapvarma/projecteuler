package main

import "fmt"

func main() {
	res := 0
	for n := 1; n < 1000; n++ {
		if n%3==0 || n%5==0 {
			res += n
		}
	} 
	fmt.Println("p100: ", res)
}