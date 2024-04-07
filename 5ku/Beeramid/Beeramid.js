var beeramid = function(bonus, price) {
    if (bonus < price) {
      return 0 
    }else if (bonus == price) {
      return 1
    }else{
      result = 0
      for (let index = 0; index < bonus/price; index++) {
          result += index * index
          if (bonus/price < result) {
              return index - 1
          }else if (result == bonus/price) {
              return index 
          }
      }
    }
  }
/*	best
var beeramid = function(bonus, price) {
  var beers = Math.floor(bonus / price), levels = 0;
  while(beers >= ++levels * levels) {
    beers -= levels * levels;
  }
  return levels - 1;
}
*/
