function firstNonRepeatingLetter(s) {
    small = s.toLocaleLowerCase()
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
function firstNonRepeatingLetter(s) {
  for(var i in s) {
    if(s.match(new RegExp(s[i],"gi")).length === 1) {
      return s[i];
    }
  }
  return '';
}
*/
