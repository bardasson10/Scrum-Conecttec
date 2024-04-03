// Arquivo: botascript.js (na pasta static)

function addClickListenerToExpandButtons() {
    const expandButtons = document.querySelectorAll(".btn-expand");

    expandButtons.forEach(button => {
        button.addEventListener("click", function () {
            const apontamento = button.closest(".apontamento");
            const descricao = apontamento.querySelector(".apontamento-descricao")
            const descrizinha = apontamento.querySelector(".apontamento-info");
            
            // Inverte a visibilidade da descrição ao clicar no botão
            descricao.classList.toggle("truncated");

            // Alterna o texto do botão entre "+" e "-"
            button.textContent = descricao.classList.contains("truncated") ? "+" : "-";
            
            descrizinha.classList.toggle("truncated");

            // Alterna o texto do botão entre "+" e "-"
            button.textContent = descrizinha.classList.contains("truncated") ? "+" : "-";
        });
    }); 
}

// Chama a função após o carregamento do DOM
document.addEventListener('DOMContentLoaded', function() {
    addClickListenerToExpandButtons();
});
