function alphanumeric(string){
    let pat = /[0-9a-zA-Z]+/
    if(pat.exec(string) == string){
        return true
    }
    return false
  }

/* best
let alphanumeric = s => /^[a-z\d]+$/i.test(s);
*/