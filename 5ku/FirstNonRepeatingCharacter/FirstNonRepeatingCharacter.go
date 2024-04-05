package main

import "strings"

func FirstNonRepeating(str string) string {
	//your code here
	low := strings.ToLower(str)
	for k, _ := range low {
		if strings.Count(low, low[k:k+1]) == 1 {
			return str[k : k+1]
		}

	}
	return ""
}

/*	best
package kata
import (
	"strings"
)
func FirstNonRepeating(str string) string {
    for _, c := range str {
        if strings.Count(strings.ToLower(str), strings.ToLower(string(c))) < 2 {
	          return string(c)
	      }
    }
    return ""
}
*/
