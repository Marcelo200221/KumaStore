//Función reloj

const $tiempo=document.querySelector('.tiempo');

function relojDigital(){
    if ($tiempo) {
        let f= new Date();
        let timeString= f.toLocaleTimeString();
        $tiempo.innerHTML=timeString;
    }
}
if ($tiempo) {
    setInterval(() => {
        relojDigital();
    }, 1000);
}

const btnSwitch = document.querySelector('#switch');

const flick = localStorage.getItem("switch");

if (flick === "activo"){
    document.body.classList.add('dark');
    document.documentElement.classList.add('dark');
    if (btnSwitch) btnSwitch.classList.add('active');
} else {
    document.body.classList.remove('dark');
    document.documentElement.classList.remove('dark');
    if (btnSwitch) btnSwitch.classList.remove('active');
}

if (btnSwitch) {
    btnSwitch.addEventListener('click', () => {
        document.body.classList.toggle('dark');
        document.documentElement.classList.toggle('dark');
        btnSwitch.classList.toggle('active');

        if(document.body.classList.contains('dark') || document.documentElement.classList.contains('dark')){
            localStorage.setItem("switch", "activo");
        } else {
            localStorage.setItem("switch", "inactivo");
        }
    });
}