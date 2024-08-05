document.addEventListener('DOMContentLoaded', function() {
    const continueButton = document.getElementById('continue-button');

    continueButton.addEventListener('click', function() {
        const player1Name = document.getElementById('player1-name').value;
        const player1Alias = document.getElementById('player1-alias').value;

        // Aquí podrías almacenar el nombre y alias en algún lugar si es necesario.
        // Por ejemplo, usando localStorage.
        localStorage.setItem('player1Name', player1Name);
        localStorage.setItem('player1Alias', player1Alias);

        // Redirigir a la página del jugador 2
        window.location.href = 'page2.html';
    });
});


function goToPage2() {
    window.location.href = 'player2.html';
}

function goToWarriorSelection() {
    window.location.href = 'warrior_selection.html';
}

function goToWarriorDetails(warriorName) {
    // Lógica para cargar detalles del guerrero
    window.location.href = 'warrior_details.html';
}

function selectWarrior() {
    // Lógica para seleccionar guerrero
}

function goBackToSelection() {
    window.location.href = 'warrior_selection.html';
}

function startGame() {
    // Lógica para iniciar el juego
    window.location.href = 'index.html';
}

// Funciones adicionales para manejar la generación y selección de guerreros
