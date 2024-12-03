import Controller from "./controller.js";
import Client from "./client.js";


// script.js

// Obtener el canvas y su contexto
const canvas = document.getElementById('drawingCanvas');
const submitButton = document.getElementById('submitButton');
const resultText = document.getElementById('resultText');
const ctx = canvas.getContext('2d');

// Ajustar el tamaño del canvas al de la caja contenedora
canvas.width = canvas.offsetWidth;
canvas.height = canvas.offsetHeight;

// Variables para manejar el estado del dibujo
let isDrawing = false;
let lastX = 0;
let lastY = 0;

// Configuración del dibujo (color y grosor de línea)
ctx.strokeStyle = '#000'; // Color negro
ctx.lineWidth = 6;
ctx.lineJoin = 'round';
ctx.lineCap = 'round';

// Funciones para manejar eventos de dibujo
function startDrawing(e) {
    isDrawing = true;
    [lastX, lastY] = [e.offsetX, e.offsetY];
}

function draw(e) {
    if (!isDrawing) return; // No dibujar si no está activo
    ctx.beginPath();
    ctx.moveTo(lastX, lastY); // Punto inicial
    ctx.lineTo(e.offsetX, e.offsetY); // Punto final
    ctx.stroke();
    [lastX, lastY] = [e.offsetX, e.offsetY]; // Actualizar las coordenadas
}

function stopDrawing() {
    isDrawing = false;
    ctx.beginPath(); // Termina el trazado actual
}

// Eventos del mouse
canvas.addEventListener('mousedown', startDrawing);
canvas.addEventListener('mousemove', draw);
canvas.addEventListener('mouseup', stopDrawing);
canvas.addEventListener('mouseout', stopDrawing);

// Eventos táctiles (para pantallas táctiles)
canvas.addEventListener('touchstart', (e) => {
    const touch = e.touches[0];
    const rect = canvas.getBoundingClientRect();
    lastX = touch.clientX - rect.left;
    lastY = touch.clientY - rect.top;
    isDrawing = true;
});
canvas.addEventListener('touchmove', (e) => {
    if (!isDrawing) return;
    const touch = e.touches[0];
    const rect = canvas.getBoundingClientRect();
    const x = touch.clientX - rect.left;
    const y = touch.clientY - rect.top;
    ctx.beginPath();
    ctx.moveTo(lastX, lastY);
    ctx.lineTo(x, y);
    ctx.stroke();
    lastX = x;
    lastY = y;
});
canvas.addEventListener('touchend', stopDrawing);
canvas.addEventListener('touchcancel', stopDrawing);


const client = new Client()
const controller = new Controller(client)

export function updateResultText(newText){
	resultText.textContent = newText
}


submitButton.addEventListener('click', () =>{
	const dataURL = canvas.toDataURL('image/png');
	fetch(dataURL).then((result) => {
		result.blob().then((image) => {
			controller.sendImage(image)
		})
	})
});

