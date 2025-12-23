CREATE TABLE IF NOT EXISTS usuarios(
    id_usuario INTEGER NOT NULL AUTO_INCREMENT, 
    nombre_usuario VARCHAR(25) NOT NULL, 
    contrasena VARCHAR(255) NOT NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,

    CONSTRAINT pk_usuarios PRIMARY KEY (id_usuario)
);