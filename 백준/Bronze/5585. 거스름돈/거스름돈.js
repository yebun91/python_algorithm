const fs = require('fs');
const input = fs.readFileSync("/dev/stdin").toString().trim();

const solution = (s) => {
    let answer = 0;
    let num = 1000 - Number(s);
    let change = [500, 100, 50, 10, 5, 1];
    for(let x of change){
        answer += parseInt(num/x);
        num = num%x;
    }
    return answer
}

console.log(solution(input));