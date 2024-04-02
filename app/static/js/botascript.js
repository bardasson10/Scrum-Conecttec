// Arquivo: botascript.js (na pasta static)

function addClickListenerToExpandButtons() {
    const expandButtons = document.querySelectorAll(".btn-expand");

    expandButtons.forEach(button => {
        button.addEventListener("click", function () {
            const apontamento = button.closest(".apontamento");
            const descricao = apontamento.querySelector(".apontamento-descricao");
            
            // Inverte a visibilidade da descrição ao clicar no botão
            descricao.classList.toggle("hidden");

            // Alterna o texto do botão entre "+" e "-"
            button.textContent = descricao.classList.contains("hidden") ? "+" : "-";
        });
    });
}

// Chama a função após o carregamento do DOM
document.addEventListener('DOMContentLoaded', function() {
    addClickListenerToExpandButtons();
});
