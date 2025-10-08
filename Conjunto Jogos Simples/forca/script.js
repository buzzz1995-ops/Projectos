const palavras = ["javascript", "computador", "programa", "desenvolvedor", "teclado"];
let palavra, palavraCorreta, erros;
const maxErros = 6;

const palavraDisplay = document.getElementById("palavraDisplay");
const letrasDiv = document.querySelector(".letras");
const mensagem = document.getElementById("mensagem");
const canvas = document.getElementById("forcaCanvas");
const ctx = canvas.getContext("2d");
const reiniciarBtn = document.getElementById("reiniciar");

iniciarJogo();

function iniciarJogo() {
    palavra = palavras[Math.floor(Math.random() * palavras.length)].toLowerCase();
    palavraCorreta = Array(palavra.length).fill("_");
    erros = 0;
    mensagem.textContent = "";
    reiniciarBtn.style.display = "none";

    palavraDisplay.textContent = palavraCorreta.join(" ");

    letrasDiv.innerHTML = "";
    for (let i = 65; i <= 90; i++) {
        const button = document.createElement("button");
        button.textContent = String.fromCharCode(i);
        button.addEventListener("click", letraEscolhida);
        letrasDiv.appendChild(button);
    }

    desenharBase();
}

reiniciarBtn.addEventListener("click", iniciarJogo);

function letraEscolhida(event) {
    const button = event.target;
    const letra = button.textContent.toLowerCase();
    button.disabled = true;

    if (palavra.includes(letra)) {
        palavra.split("").forEach((l, i) => {
            if (l === letra) palavraCorreta[i] = letra;
        });
        palavraDisplay.textContent = palavraCorreta.join(" ");
        button.classList.add("certo");

        if (!palavraCorreta.includes("_")) {
            mensagem.textContent = "🎉 Parabéns! Ganhou!";
            terminarJogo();
        }
    } else {
        erros++;
        desenharForca(erros);
        button.classList.add("errado");
        if (erros >= maxErros) {
            mensagem.textContent = `💀 Perdeu! A palavra era: ${palavra}`;
            terminarJogo();
        }
    }
}

function terminarJogo() {
    letrasDiv.querySelectorAll("button").forEach(b => b.disabled = true);
    reiniciarBtn.style.display = "inline-block";
}

function desenharBase() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.strokeStyle = "#f1faee";
    ctx.lineWidth = 2;

    // Base inicial da forca
    ctx.beginPath();
    ctx.moveTo(10, 240);
    ctx.lineTo(190, 240);
    ctx.moveTo(50, 240);
    ctx.lineTo(50, 20);
    ctx.lineTo(150, 20);
    ctx.lineTo(150, 40);
    ctx.stroke();
}

function desenharForca(erros) {
    desenharBase();

    if (erros > 0) { // cabeça
        ctx.beginPath();
        ctx.arc(150, 60, 20, 0, Math.PI * 2);
        ctx.stroke();
    }
    if (erros > 1) { // corpo
        ctx.beginPath();
        ctx.moveTo(150, 80);
        ctx.lineTo(150, 150);
        ctx.stroke();
    }
    if (erros > 2) { // braço esquerdo
        ctx.beginPath();
        ctx.moveTo(150, 100);
        ctx.lineTo(120, 130);
        ctx.stroke();
    }
    if (erros > 3) { // braço direito
        ctx.beginPath();
        ctx.moveTo(150, 100);
        ctx.lineTo(180, 130);
        ctx.stroke();
    }
    if (erros > 4) { // perna esquerda
        ctx.beginPath();
        ctx.moveTo(150, 150);
        ctx.lineTo(120, 190);
        ctx.stroke();
    }
    if (erros > 5) { // perna direita
        ctx.beginPath();
        ctx.moveTo(150, 150);
        ctx.lineTo(180, 190);
        ctx.stroke();
    }
}
