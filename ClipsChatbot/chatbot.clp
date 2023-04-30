;;chatbot que adivina una figura geométrica dado su número de lados y sus ángulos internos 

(defrule triangulo
    (numero-lados 3)
    (angulos-internos 180)
    => 
    (printout t "La figura es un triangulo" crlf)
    (assert (done))
    )

(defrule cuadrado
    (numero-lados 4)
    (angulos-internos 360)
    => 
    (printout t "La figura es un cuadrado" crlf)
    (assert (done))
    )

(defrule pentagono
    (numero-lados 5)
    (angulos-internos 540)
    => 
    (printout t "La figura es un pentagono" crlf)
    (assert (done))
    )

(defrule hexagono
    (numero-lados 6)
    (angulos-internos 720)
    => 
    (printout t "La figura es un hexagono" crlf)
    (assert (done))
)

(defrule heptagono
    (numero-lados 7)
    (angulos-internos 900)
    => 
    (printout t "La figura es un heptagono" crlf)
    (assert (done))
)

(defrule octagono
    (numero-lados 8)
    (angulos-internos 1080)
    => 
    (printout t "La figura es un octagono" crlf)
    (assert (done))
)

(defrule nonagono
    (numero-lados 9)
    (angulos-internos 1260)
    => 
    (printout t "La figura es un nonagono" crlf)
    (assert (done))
)

(defrule decagono
    (numero-lados 10)
    (angulos-internos 1440)
    => 
    (printout t "La figura es un decagono" crlf)
    (assert (done))
)



;;pregunta al usuario
(defrule pregunta
    (inicio)
    =>
    (printout t "¿Cuantos lados tiene la figura?" crlf)
    (assert (numero-lados (read)))
    (printout t "¿Cuantos grados tiene la figura?" crlf)
    (assert (angulos-internos (read)))
)

(defrule inicio
    (declare (salience 10))
    =>
    (printout t "Bienvenido al chatbot de figuras geometricas" crlf)
    (printout t "Por favor ingrese los datos de la figura" crlf)
    (assert (inicio))
)

;;caso en que no se conoce la figura
(defrule default 
    (declare (salience -10))
    (not (done))
    =>
    (printout t "No se que figura es, o es una figura irregular" crlf)
    (assert (done))
)





