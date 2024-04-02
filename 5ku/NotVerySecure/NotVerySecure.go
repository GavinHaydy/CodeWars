package kata

import "unicode"

func alphanumeric(str string) bool {
	if str == "" {
		return false
	}
	for _, s := range str {
		if !unicode.IsLetter(s) && !unicode.IsNumber(s) {
			return false
		}
	}
	return true
}

/*
package kata

import "regexp"

func alphanumeric(s string) bool {
	r := regexp.MustCompile("^[a-zA-Z0-9]+$")
	return r.MatchString(s)
}

*/
