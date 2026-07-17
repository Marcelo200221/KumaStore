document.getElementById('opciones').addEventListener('change', function(){
    const valorSeleccionado = this.value;

    if(valorSeleccionado == 'logout') {
        let modal = document.getElementById("modal-logout");
        let botonAceptar = document.getElementById("aceptar-logout")
        let botonCancelar = document.getElementById("cancelar-logout")

        modal.classList.remove("d-none")

        botonAceptar.addEventListener("click", () => {
            document.getElementById('form-logout').submit();
        })

        botonCancelar.addEventListener("click", () => {
            modal.classList.add("d-none")
        })

        this.value = 'default'
    } else if(valorSeleccionado == 'perfil') {
        window.location.href = '/perfil'
        this.value = 'default'
    }
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

document.querySelectorAll(".btn-loader").forEach(boton => {
        boton.addEventListener("click", () => {
            const loader = document.getElementById("loader-overlay");
            if(loader){
                loader.classList.remove("d-none");
            }
        })
    })
