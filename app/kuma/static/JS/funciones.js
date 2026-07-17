document.getElementById('opciones').addEventListener('change', function(){
    const valorSeleccionado = this.value;

    if(valorSeleccionado == 'logout') {
        document.getElementById('form-logout').submit();
    } else if(valorSeleccionado == 'perfil') {
        window.location.href = '/perfil'
    }
})