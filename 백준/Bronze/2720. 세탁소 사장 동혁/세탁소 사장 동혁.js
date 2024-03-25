const input = require('fs')
  .readFileSync('dev/stdin')
  .toString()
  .trim()
  .split('\n')
  .map(Number);

const solution = (s) => {
    let answer = "";
    let money = s;
    const change = [25, 10, 5, 1];
    
    for(let i = 0; i < change.length; i++){
        answer += parseInt(money/change[i])+" ";
        money = money%change[i];
    }
    
    return answer;
};

for(let i=0; i<input[0]; i++){
    console.log(solution(input[i+1]));
}
