package main

import (
	"fmt"
	"strings"
)

func FirstNonRepeating(str string) string {
	//your code here
	low := strings.ToLower(str)
	for k, _ := range low {
		// fmt.Println(str[k : k+1])
		if strings.Count(low, low[k:k+1]) == 1 {
			fmt.Println(strings.Count(low, str[k:k+1]))
			return str[k : k+1]
		}

	}
	return ""
}
func main() {
	fmt.Println(FirstNonRepeating("stress"))
	fmt.Println(FirstNonRepeating("sTreSS"))
}
