export function beeramid(bonus: number, price: number): number {
    let beers = Math.floor(bonus/ price), levels = 0
    while(beers >= ++levels ** 2){
        beers -= levels ** 2
    }
    return levels -1
  }

/*	best
export function beeramid(bonus: number, price: number): number {
  let level: number = 0;
  let n: number = 1;
  let i: number = 1
  while(n <= Math.floor(bonus / price)){
    i++;
    n += i ** 2;
    level++
  }
  return level
}
*/
