const canvas = document.getElementById("gameCanvas");
const ctx = canvas.getContext("2d");
const scoreElement = document.getElementById("pontuacao");

const grid = 20; // tamanho da célula
let snake = [{ x: 160, y: 200 }];
let dx = grid; // direção inicial (direita)
let dy = 0;
let comida = gerarComida();
let pontuacao = 0;
let jogoAtivo = true;

function voltarMenu() {
    window.location.href = "../index.html";
}

function desenharCobra() {
    ctx.fillStyle = "#f1faee";
    snake.forEach(parte => {
        ctx.fillRect(parte.x, parte.y, grid - 2, grid - 2);
    });
}

function desenharComida() {
    ctx.fillStyle = "#e63946";
    ctx.fillRect(comida.x, comida.y, grid - 2, grid - 2);
}

function moverCobra() {
    const cabeca = { x: snake[0].x + dx, y: snake[0].y + dy };
    snake.unshift(cabeca);

    // comer comida
    if (cabeca.x === comida.x && cabeca.y === comida.y) {
        pontuacao++;
        scoreElement.textContent = pontuacao;
        comida = gerarComida();
    } else {
        snake.pop();
    }
}

function verificarColisoes() {
    const cabeca = snake[0];

    // bordas
    if (cabeca.x < 0 || cabeca.y < 0 || cabeca.x >= canvas.width || cabeca.y >= canvas.height) {
        jogoAtivo = false;
    }

    // corpo
    for (let i = 1; i < snake.length; i++) {
        if (cabeca.x === snake[i].x && cabeca.y === snake[i].y) {
            jogoAtivo = false;
        }
    }
}

function gerarComida() {
    return {
        x: Math.floor(Math.random() * (canvas.width / grid)) * grid,
        y: Math.floor(Math.random() * (canvas.height / grid)) * grid
    };
}

function desenhar() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    desenharCobra();
    desenharComida();
}

function loop() {
    if (!jogoAtivo) {
        ctx.fillStyle = "#a9bcd0";
        ctx.font = "20px Segoe UI";
        ctx.fillText("💀 Fim de jogo! Pressiona Reiniciar.", 40, canvas.height / 2);
        return;
    }

    moverCobra();
    verificarColisoes();
    desenhar();

    setTimeout(loop, 100);
}

function mudarDirecao(event) {
    if (event.key === "ArrowUp" && dy === 0) {
        dx = 0; dy = -grid;
    } else if (event.key === "ArrowDown" && dy === 0) {
        dx = 0; dy = grid;
    } else if (event.key === "ArrowLeft" && dx === 0) {
        dx = -grid; dy = 0;
    } else if (event.key === "ArrowRight" && dx === 0) {
        dx = grid; dy = 0;
    }
}

function reiniciarJogo() {
    snake = [{ x: 160, y: 200 }];
    dx = grid;
    dy = 0;
    comida = gerarComida();
    pontuacao = 0;
    scoreElement.textContent = pontuacao;
    jogoAtivo = true;
    loop();
}

document.addEventListener("keydown", mudarDirecao);

reiniciarJogo();