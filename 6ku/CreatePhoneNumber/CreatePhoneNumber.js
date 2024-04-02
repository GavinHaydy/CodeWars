function createPhoneNumber(numbers){
    return `(${numbers.slice(0, 3).join('')}) ${numbers.slice(3, 6).join('')} - ${numbers.slice(6).join('')}`;
}

// best 
function createPhoneNumber(numbers){
    return numbers.join('').replace(/(...)(...)(.*)/, '($1) $2-$3');
  }