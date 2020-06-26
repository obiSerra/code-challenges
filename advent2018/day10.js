const cv = document.querySelector("canvas")
const ctx = cv.getContext("2d")
const data = document
  .querySelector("#data2")
  .innerText.split("|")
  .map(v => v.match(/\-?[0-9]+/gi))
  .filter(v => v)
  .map(v => v && v.map(vv => parseInt(vv, 10)))

const pxW = 2
const middleX = cv.width / 2 - 220 * pxW
const middleY = cv.height / 2 - 150 * pxW
let cnt = 0
let running = false
let reverse = false
const sp = 1000 / 5
let cPts = data
const cntEl = document.querySelector("#cnt")
const avgXEl = document.querySelector("#avgX")
const avgYEl = document.querySelector("#avgY")

let avgX = 0
let avgY = 0

ctx.fillStyle = "white"

const drawPoints = pts => {
  avgX = 0
  avgY = 0
  pts.forEach(p => {
    const x = p[0] * pxW + middleX
    const y = p[1] * pxW + middleY

    avgX += Math.abs(p[0] * pxW)
    avgY += Math.abs(p[1] * pxW)

    ctx.fillRect(x, y, pxW, pxW)
  })

  avgXEl.innerText = Math.round(avgX / pts.length)
  avgYEl.innerText = Math.round(avgY / pts.length)
}

const movePts = pts => pts.map(p => [p[0] + p[2], p[1] + p[3], p[2], p[3]])
const moveBack = pts => pts.map(p => [p[0] - p[2], p[1] - p[3], p[2], p[3]])

const logCnt = () => {
  cntEl.innerText = cnt
}

drawPoints(data)

// Btns animations
document.querySelector("#stop-animation").addEventListener("click", e => {
  running = !running
  if (running) {
    document.querySelector("#stop-animation").innerText = "STOP"
    gameLoop(cPts)
  } else {
    document.querySelector("#stop-animation").innerText = "PLAY"
  }
})

document.querySelector("#back").addEventListener("mousedown", e => {
  running = true
  reverse = true
})

document.querySelector("#back").addEventListener("mouseup", e => {
  running = false
  reverse = false
})

document.querySelector("#fwd").addEventListener("mousedown", e => {
  running = true
  reverse = false
})

document.querySelector("#fwd").addEventListener("mouseup", e => {
  running = false
  reverse = false
})

const gameLoop = () => {
  if (running && reverse) {
    cPts = moveBack(cPts)
    ctx.clearRect(0, 0, cv.width, cv.height)
    drawPoints(cPts)
    logCnt()
    cnt--
  } else if (running) {
    cPts = movePts(cPts)
    ctx.clearRect(0, 0, cv.width, cv.height)
    drawPoints(cPts)
    logCnt()
    cnt++
  }

  setTimeout(gameLoop, sp)
}

for (let i = 0; i < 10355; i++) {
  cPts = movePts(cPts)
  cnt++
}

ctx.clearRect(0, 0, cv.width, cv.height)
drawPoints(cPts)
logCnt()
gameLoop()
