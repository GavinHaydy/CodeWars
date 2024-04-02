export function alphanumeric(string: string): boolean {
    //your code here
    if(/[A-Za-z0-9]+$/.exec(string) != null && /^[A-Za-z0-9]+$/.exec(string)){
        return true;
    }
    return false;
  }

/* best
export function alphanumeric(string: string): boolean {
  return /^[a-z\d]+$/i.test(string)
}
*/