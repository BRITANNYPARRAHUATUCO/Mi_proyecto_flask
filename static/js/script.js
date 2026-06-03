document.addEventListener("DOMContentLoaded", () => {
    const preloader = document.getElementById("preloader");

    const ocultarPreloader = () => {
        if (preloader) {
            // El setTimeout de 2000ms hace que el usuario vea tu diseño por 2 segundos
            setTimeout(() => {
                preloader.style.opacity = "0";
                preloader.style.visibility = "hidden";
                
                // Luego esperamos los 0.5s de la transición CSS antes de quitarlo del DOM
                setTimeout(() => {
                    preloader.style.display = "none";
                }, 500);
            }, 2000); 
        }
    };

    // Ejecutamos cuando todo carga
    window.addEventListener("load", ocultarPreloader);
});

// Carrusel de marcas infinito
const slider = document.querySelector(".marcas-slider");
if (slider) {
    const copy = slider.cloneNode(true);
    slider.parentElement.appendChild(copy);
}