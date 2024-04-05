function firstNonRepeatingLetter(s) {
    let small = s.toLocaleLowerCase();
    for (const key in s) {
        var regexWithFlags = new RegExp(s[key].toLocaleLowerCase(), 'gi');
        if (small.match(regexWithFlags).length==1) {
            return s[key];
        }
    }
    return ""
    // Add your code here
  }

/*	best
*/
