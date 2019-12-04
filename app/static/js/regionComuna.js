
                // Consigue el elemento provincias/poblaciones por su identificador id. Es un método del DOM de HTML
                var id1 = document.getElementById("id_region");
                var id2 = document.getElementById("id_comuna");

                // Añade un evento change al elemento id1, asociado a la función cambiar()
                if (id1.addEventListener) {     // Para la mayoría de los navegadores, excepto IE 8 y anteriores
                    id1.addEventListener("change", cambiar);
                } else if (id1.attachEvent) {   // Para IE 8 y anteriores
                    id1.attachEvent("change", cambiar); // attachEvent() es el método equivalente a addEventListener()
                }

                // Definición de la función cambiar()
                function cambiar() {
                    for (var i = 0; i < id2.options.length; i++)

                        // -- Inicio del comentario -- 
                        // Muestra solamente los id2 que sean iguales a los id1 seleccionados, según la propiedad display
                        if (id2.options[i].getAttribute("codigo") == id1.options[id1.selectedIndex].getAttribute("codigo")) {
                            id2.options[i].style.display = "block";
                        } else {
                            id2.options[i].style.display = "none";
                        }
                    // -- Fin del comentario --

                    id2.value = "";
                }

                // Llamada a la función cambiar()
                cambiar();
            
