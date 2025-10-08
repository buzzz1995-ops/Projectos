const choices = ["pedra", "papel", "tesoura"];
const buttons = document.querySelectorAll(".ppt-btn");
const playerChoiceText = document.getElementById("player-choice");
const computerChoiceText = document.getElementById("computer-choice");
const winnerText = document.getElementById("winner");

buttons.forEach(button => {
    button.addEventListener("click", () => {
        const playerChoice = button.dataset.choice;
        const computerChoice = choices[Math.floor(Math.random() * 3)];

        playerChoiceText.textContent = `Tu escolheste: ${playerChoice}`;
        computerChoiceText.textContent = `Computador escolheu: ${computerChoice}`;

        if (playerChoice === computerChoice) {
            winnerText.textContent = "Resultado: Empate! 🤝";
        } else if (
            (playerChoice === "pedra" && computerChoice === "tesoura") ||
            (playerChoice === "papel" && computerChoice === "pedra") ||
            (playerChoice === "tesoura" && computerChoice === "papel")
        ) {
            winnerText.textContent = "Resultado: Ganhaste! 🎉";
        } else {
            winnerText.textContent = "Resultado: Perdeste 😢";
        }
    });
});
