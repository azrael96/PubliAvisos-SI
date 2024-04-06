-- --------------------------------------------------------

--
-- Base de datos: `publiavisos`
--

-- --------------------------------------------------------
DROP DATABASE publiavisos;
COMMIT;

CREATE DATABASE publiavisos;
COMMIT;

USE publiavisos;
COMMIT;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `empleado`
--

CREATE TABLE empleado (
    `emp_cedula` varchar(20) NOT NULL,
    `emp_nombre1` varchar(50) NOT NULL,
    `emp_nombre2` varchar(50) NOT NULL,
    `emp_apellido1` varchar(50) NOT NULL,
    `emp_apellido2` varchar(50) NOT NULL,
    `emp_direccion` varchar(50) NOT NULL,
    `emp_activo` boolean NOT NULL,
    `emp_telefono` varchar(32) NOT NULL,
    `emp_correo` varchar(50) NOT NULL,
    `emp_ubicacion` varchar(50) NOT NULL
);
ALTER TABLE `empleado` ADD PRIMARY KEY (`emp_cedula`);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cliente`
--

CREATE TABLE cliente (
    `cli_cedula` varchar(20) NOT NULL,
    `cli_nombre1` varchar(50) NOT NULL,
    `cli_nombre2` varchar(50) NOT NULL,
    `cli_apellido1` varchar(50) NOT NULL,
    `cli_apellido2` varchar(50) NOT NULL,
    `cli_direccion` varchar(50) NOT NULL,
    `cli_telefono` varchar(32) NOT NULL,
    `cli_correo` varchar(50) NOT NULL,
    `cli_ubicacion` varchar(50) NOT NULL
);
ALTER TABLE `cliente` ADD PRIMARY KEY (`cli_cedula`);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `orden`
--

CREATE TABLE orden (
    `ord_ID` int NOT NULL,
    `ord_estado` varchar(50) NOT NULL,
    `ord_descripcion` varchar(100) NOT NULL,
    `ord_valor` int NOT NULL,
    `ord_fechaEntrega` date NOT NULL,
    `ord_fechaRecepcion` date NOT NULL,
    `cli_cedula_fk` varchar(20) NOT NULL,
    `emp_cedula_fk` varchar(20) NOT NULL
);
ALTER TABLE `orden` ADD PRIMARY KEY (`ord_ID`);
ALTER TABLE `orden` ADD FOREIGN KEY (`cli_cedula_fk`) REFERENCES cliente(cli_cedula);
ALTER TABLE `orden` ADD FOREIGN KEY (`emp_cedula_fk`) REFERENCES empleado(emp_cedula);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `registro`
--

CREATE TABLE registro (
    `reg_ID` int NOT NULL,
    `reg_fechaCambio` date NOT NULL,
    `reg_descripcion` varchar(100) NOT NULL,
    `ord_ID_fk` int NOT NULL
);
ALTER TABLE `registro` ADD PRIMARY KEY (`reg_ID`);
ALTER TABLE `registro` ADD FOREIGN KEY (`ord_ID_fk`) REFERENCES orden(`ord_ID`);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cotizacion`
--

CREATE TABLE cotizacion (
    `cot_ID` int NOT NULL,
    `cot_descripcion` varchar(100) NOT NULL,
    `cot_valor` int NOT NULL,
    `cli_cedula_fk` varchar(20) NOT NULL
);
ALTER TABLE `cotizacion` ADD PRIMARY KEY (`cot_ID`);
ALTER TABLE `cotizacion` ADD FOREIGN KEY (`cli_cedula_fk`) REFERENCES cliente(cli_cedula);

-- --------------------------------------------------------

--
-- Usuarios iniciales de la base de datos
--

