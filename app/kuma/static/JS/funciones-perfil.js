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

document.getElementById("editar-contraseña").addEventListener("click", function(){
    let campos = document.getElementById("campos-contraseña")
    let otrosCampos = document.getElementById("campos-usuario")
    let botonesUsuario = document.getElementById("botones-usuario")
    let botonCambiar = document.getElementById("editar-contraseña")
    let botonConfirmar = document.getElementById("btn-confirmar")

    if(!campos.classList.contains("d-none")){
        campos.classList.add("d-none")
        botonConfirmar.classList.add("d-none")
        otrosCampos.classList.remove("d-none")
        botonesUsuario.classList.remove("d-none")
        botonCambiar.innerHTML = "Cambiar contraseña"
        return;
    }


    campos.classList.remove("d-none")
    botonConfirmar.classList.remove("d-none")
    otrosCampos.classList.add("d-none")
    botonesUsuario.classList.add("d-none")

    botonCambiar.innerHTML = "Cancelar"

    botonConfirmar.addEventListener("click", function(){
        document.getElementById("form-contraseña").submit()
    })

})

document.addEventListener("DOMContentLoaded", () => {
    const loader = document.getElementById("loader-overlay");

    document.querySelectorAll("form").forEach(form => {
        form.addEventListener("submit", () => {
            if(loader) {
                loader.classList.remove("d-none")
            }
        })
    })

    
})

