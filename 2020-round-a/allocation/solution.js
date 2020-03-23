
// variable to parse cases
const lineForEachCase = 2
function parseCases(lines) {
    const [ houseNo, budget ] = lines[0].split(' ').map(v => Number(v))
    const houses = lines[1].split(' ').map(v => Number(v))
    return {
        houseNo,
        budget,
        houses
    }
}

// Actual solution
function solveCases(cases) {
    cases.forEach((c, i) => {
        const sorted = c.houses.sort(function(a, b){return a-b})
        let totalNo = 0
        let balance = c.budget
        for(let i = 0; i < c.houseNo; ++i) {
            balance -= sorted[i]
            if(balance < 0) {
                break;
            }
            totalNo += 1
        }
        console.log(`Case #${i+1}: ${totalNo}`)
    })
}

const readline = require('readline')
const rl = readline.createInterface({
    input: process.stdin,
})
let totalCase = 0
let caseLines = []
let cases = []
rl.on('line', (line) => {
    if(totalCase === 0) {
        totalCase = Number.parseInt(line)
        return;
    }
    caseLines.push(line)
    if(caseLines.length >= lineForEachCase) {
        cases.push(parseCases(caseLines))
        caseLines = []
    }
}).on('close', () => {
    solveCases(cases)
    process.exit(0)
})
