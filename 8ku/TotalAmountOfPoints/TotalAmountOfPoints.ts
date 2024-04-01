export function points(games : string[]): number {
    let result = 0
    games.forEach(element => {
        if(element[0]>element[2]){
            result += 3
        }else if(element[0]==element[2]){
            result += 1
        }
    });
    return result
  }