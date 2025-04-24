const scissorsButton = document.getElementById("scissors-button");
const rockButton = document.getElementById("rock-button");
const paperButton = document.getElementById("paper-button");

const result = document.createElement("div");
result.style.backgroundColor = "rgb(30, 144, 255, 0.7)";
result.style.position = "fixed";
result.style.top = "50%";
result.style.left = "50%";
result.style.width = "100%";
result.style.height = "50%";
result.style.transform = "translate(-50%, -50%)";
result.style.zIndex = "99";
result.textContent = "";
result.style.color = "white";
result.style.fontSize = "3rem";
result.style.textAlign = "center";
result.style.alignContent = "center";
result.style.fontWeight = "bold";
result.style.pointerEvents = "none"; // 클릭 안되게함!!! 이거 안해주니까 result가 버튼을 덮어버려서 안눌려

let player1Score = document.querySelector(".countA");
let player2Score = document.querySelector(".countB");

let player1 = {
  name: "player1",
  score: 0,
  choice: "",
};
let player2 = {
  name: "player2",
  score: 0,
  choice: "",
};

player1Score.textContent = player1.score;
player2Score.textContent = player2.score;

const choices = ["scissors", "rock", "paper"];

function playGame(player1, player2) {
  if (player1.choice === player2.choice) {
    result.textContent = "It's a tie!";
  } else if (player1.choice === "scissors") {
    if (player2.choice === "rock") {
      player2.score++;
      player2Score.textContent = player2.score;
      result.textContent = "Player 2 wins!";
    } else if (player2.choice === "paper") {
      player1.score++;
      player1Score.textContent = player1.score;
      result.textContent = "Player 1 wins!";
    }
  } else if (player1.choice === "rock") {
    if (player2.choice === "scissors") {
      player1.score++;
      player1Score.textContent = player1.score;
      result.textContent = "Player 1 wins!";
    } else if (player2.choice === "paper") {
      player2.score++;
      player2Score.textContent = player2.score;
      result.textContent = "Player 2 wins!";
    }
  } else if (player1.choice === "paper") {
    if (player2.choice === "rock") {
      player1.score++;
      player1Score.textContent = player1.score;
      result.textContent = "Player 1 wins!";
    } else if (player2.choice === "scissors") {
      player2.score++;
      player2Score.textContent = player2.score;
      result.textContent = "Player 2 wins!";
    }
  }
  document.body.appendChild(result);
}

const player1Img = document.getElementById("player1-img");
const player2Img = document.getElementById("player2-img");

function buttonClickHandler(choice) {
  // 게임 재시작 했을때 result 사라지게.
  if (document.body.contains(result)) {
    document.body.removeChild(result);
  }

  player1.choice = choice;
  player1Img.src = `img/${player1.choice}.png`;
  // player1가 이미 선택한 상태면 player2의 choice로 넣어준다

  // setInterval : 80초마다 안에있는 코드를 반복해서 실행한다.
  let interval = setInterval(() => {
    const idx = Math.floor(Math.random() * 3);
    player2.choice = choices[idx];
    player2Img.src = `img/${player2.choice}.png`;
  }, 80);

  // 버튼 비활성화 : 이미 buttonClickHandler가 동작했으면 다시 못누르게 일단 막아준다.
  scissorsButton.disabled = true;
  rockButton.disabled = true;
  paperButton.disabled = true;

  // setTimeout : 3000초후 안에있는 코드를 1번 실행한다.
  setTimeout(() => {
    clearInterval(interval); // player2 무작위이미지 멈춤

    playGame(player1, player2); // 게임 결과 계산

    // 버튼 비활성화 했던거 다시 ㅜ어준다
    scissorsButton.disabled = false;
    rockButton.disabled = false;
    paperButton.disabled = false;
  }, 3000);
}

scissorsButton.addEventListener("click", function () {
  buttonClickHandler("scissors");
});
rockButton.addEventListener("click", function () {
  buttonClickHandler("rock");
});
paperButton.addEventListener("click", function () {
  buttonClickHandler("paper");
});
