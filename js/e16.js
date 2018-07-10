/** Akachukwu Obi, 2018

Project Euler #16 - Power of 2 digits sum

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?

Retrieved 28 June 2018 from https://projecteuler.net/problem=16

**/
// brute force code to get sum
var i, j, sum, str;
for (i = 0; i <= 20; i++) {
    sum = 0;
	str = String(Math.pow(2, i));
    for (j in str) {
        sum += Number(str[j]);
    }
    console.log(Math.pow(2, i), sum);
}

// to begin, Math.pow(2, 1000) gives 1.0715086071862673e+301; not precise enough to sum all of its digits

var getDigits = function(power) {
    var digits = [];
    digits[0] = 1;
    while (power > 0) {
        for (var i = digits.length-1; i >= 0; i--) {
            digits[i] *= 2;
            if (digits[i] > 9) {
                digits[i] -= 10;
                digits[i+1] = digits[i+1] || 0;
                digits[i+1] += 1;
            }
        }
        power--;
    }

    return digits;
};

var getSum = function(power){
    var digits = getDigits(power);
    var sum = 0;
    for(var i = digits.length - 1; i >= 0; i--){
        sum += digits[i];
    }
    return sum;
};

console.log(getSum(15));
console.log(getSum(1000));


var number = [1],
    sum = 0;

for(var i = 0; i < 1000; i++)
{
    var overflow = 0,
        count = number.length + 1

    for(var j = 0; j < count; j++)
    {
        var digit = number[j] || 0;

        digit = 2 * digit + overflow;

        if(digit > 9)
        {
            digit -= 10;
            overflow = 1;
        }
        else
        {
            overflow = 0;
        }

        number[j] = digit;
    }
}

for(var i = 0; i < 1000; i++)
{
    sum += number[i];
}

console.log(sum);
