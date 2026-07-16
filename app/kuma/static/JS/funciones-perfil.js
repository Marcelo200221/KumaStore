document.getElementById("boton-editar").addEventListener("click", function(){
    const nameInput = document.getElementById("name-input")
    const emailInput = document.getElementById("email-input")
    const btnGuardar = document.getElementById("boton-guardar")

    if(!nameInput.disabled && !emailInput.disabled){
        nameInput.disabled = true;
        emailInput.disabled = true;
        this.innerText = "Editar"

        btnGuardar.classList.add("d-none")
        return;
    }
    nameInput.disabled = false;
    emailInput.disabled = false;
    this.innerText = "Cancelar"

    btnGuardar.classList.remove("d-none")

    btnGuardar.addEventListener("click", function() {
        btnEditar = document.getElementById("boton-editar")
        document.getElementById("editar-form").submit()

        this.classList.add("d-none")
        nameInput.disabled = true;
        emailInput.disabled = true;
        btnEditar.innerText = "Editar"

    })
});