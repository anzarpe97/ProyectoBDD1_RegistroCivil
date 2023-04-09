-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 09-04-2023 a las 04:12:25
-- Versión del servidor: 10.1.38-MariaDB
-- Versión de PHP: 7.3.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `RegistroCivilBDD`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `acta_defuncion`
--

CREATE TABLE `acta_defuncion` (
  `id_acta_defuncion` int(11) NOT NULL,
  `a_nacimiento_fallecido` int(11) NOT NULL COMMENT 'cedula fallecido',
  `edad_fallecido` int(11) NOT NULL COMMENT 'edad del fallecido',
  `sexo_fallecido` varchar(10) NOT NULL COMMENT 'sexo del fallecido',
  `estado_civil_f` varchar(20) NOT NULL COMMENT 'estado civil del fallecido',
  `fecha_defuncion` date NOT NULL,
  `hora_defuncion` time NOT NULL,
  `lugar_defuncion` varchar(50) NOT NULL,
  `causa_muerte` varchar(100) NOT NULL,
  `c_informante` int(11) NOT NULL COMMENT 'cedula del informante',
  `relacion_informante` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `acta_defuncion`
--

INSERT INTO `acta_defuncion` (`id_acta_defuncion`, `a_nacimiento_fallecido`, `edad_fallecido`, `sexo_fallecido`, `estado_civil_f`, `fecha_defuncion`, `hora_defuncion`, `lugar_defuncion`, `causa_muerte`, `c_informante`, `relacion_informante`) VALUES
(1, 1, 33, 'f', 'soltero', '2023-05-06', '12:00:00', 'sambil', 'gente', 2, 'amigo'),
(2, 2, 15, 'm', 'd', '2023-04-10', '10:00:00', 'dfg', 'fdg', 2, 'fdgd'),
(5, 2, 30, 'femenino', 'soltero', '2007-02-06', '12:00:00', 'casa venezuela no se', 'hambre', 3, 'amigo');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `acta_divorcio`
--

CREATE TABLE `acta_divorcio` (
  `n_acta` int(11) NOT NULL COMMENT 'Primary Key',
  `c_conyuge1` int(11) NOT NULL,
  `c_conyuge2` int(11) NOT NULL,
  `id_ab_conyuge1` int(11) NOT NULL,
  `id_ab_conyuge2` int(11) NOT NULL,
  `id_hijo1` int(11) DEFAULT NULL COMMENT 'acta de nacimiento hijo 1',
  `id_hijo2` int(11) DEFAULT NULL COMMENT 'acta de nacimiento hijo 2',
  `id_prefectura` int(11) NOT NULL COMMENT 'id de la prefectura/registro'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `acta_divorcio`
--

INSERT INTO `acta_divorcio` (`n_acta`, `c_conyuge1`, `c_conyuge2`, `id_ab_conyuge1`, `id_ab_conyuge2`, `id_hijo1`, `id_hijo2`, `id_prefectura`) VALUES
(1, 1, 2, 3, 4, 5, 6, 2),
(5, 1, 2, 3, 4, 5, 6, 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `acta_matrimonio`
--

CREATE TABLE `acta_matrimonio` (
  `nro_acta` int(11) NOT NULL,
  `fecha_acta` date NOT NULL,
  `id_contrayente1` int(11) NOT NULL,
  `ocupacion_contrayente1` varchar(50) NOT NULL,
  `direccion_contrayente1` varchar(50) NOT NULL,
  `id_contrayente2` int(11) NOT NULL,
  `ocupacion_contrayente2` varchar(50) NOT NULL,
  `direccion_contrayente2` varchar(50) NOT NULL,
  `id_registrador_civil` int(11) NOT NULL,
  `id_testigo1` int(11) NOT NULL,
  `id_testigo2` int(11) NOT NULL,
  `id_prefectura` int(11) NOT NULL COMMENT 'id de la prefectura'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `acta_matrimonio`
--

INSERT INTO `acta_matrimonio` (`nro_acta`, `fecha_acta`, `id_contrayente1`, `ocupacion_contrayente1`, `direccion_contrayente1`, `id_contrayente2`, `ocupacion_contrayente2`, `direccion_contrayente2`, `id_registrador_civil`, `id_testigo1`, `id_testigo2`, `id_prefectura`) VALUES
(1, '2023-04-08', 1, 'colector', 'la limpia', 2, 'peluquera', 'san francisco', 3, 4, 5, 3);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `acta_nacimiento`
--

CREATE TABLE `acta_nacimiento` (
  `nro_acta` int(11) NOT NULL,
  `nombres` varchar(50) NOT NULL,
  `apellidos` varchar(50) NOT NULL,
  `fecha_nacimiento` date NOT NULL,
  `hora_nacimiento` time NOT NULL,
  `lugar_nacimiento` varchar(50) NOT NULL,
  `sexo` varchar(10) NOT NULL,
  `cedula_padre` int(11) NOT NULL,
  `nombre_padre` varchar(50) NOT NULL,
  `apellido_padre` varchar(50) NOT NULL,
  `cedula_madre` int(11) NOT NULL,
  `nombre_madre` varchar(50) NOT NULL,
  `apellido_madre` varchar(50) NOT NULL,
  `id_prefectura` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='Acta de nacimiento';

--
-- Volcado de datos para la tabla `acta_nacimiento`
--

INSERT INTO `acta_nacimiento` (`nro_acta`, `nombres`, `apellidos`, `fecha_nacimiento`, `hora_nacimiento`, `lugar_nacimiento`, `sexo`, `cedula_padre`, `nombre_padre`, `apellido_padre`, `cedula_madre`, `nombre_madre`, `apellido_madre`, `id_prefectura`) VALUES
(1, 'alicia', 'lopez', '2003-06-01', '12:00:00', 'venezuela', 'femenino', 2, 'javier', 'lopez', 1, 'maria', 'gonzalez', 3),
(2, 'maria', 'lopez', '2003-06-01', '12:00:00', 'venezuela', 'femenino', 2, 'javier', 'lopez', 1, 'maria', 'gonzalez', 3),
(3, 'maria', 'lopez', '2003-06-01', '12:00:00', 'venezuela', 'femenino', 2, 'javier', 'lopez', 1, 'maria', 'gonzalez', 3),
(4, 'maria', 'lopez', '2003-06-01', '12:00:00', 'venezuela', 'femenino', 2, 'javier', 'lopez', 1, 'maria', 'gonzalez', 3),
(5, 'maria', 'lopez', '2003-06-01', '12:00:00', 'venezuela', 'femenino', 2, 'javier', 'lopez', 1, 'maria', 'gonzalez', 3),
(6, 'maria', 'lopez', '2003-06-01', '12:00:00', 'venezuela', 'femenino', 2, 'javier', 'lopez', 1, 'maria', 'gonzalez', 3);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cedula`
--

CREATE TABLE `cedula` (
  `n_cedula` int(11) NOT NULL COMMENT 'Numero de cedula ',
  `acta_nacimiento` int(11) NOT NULL,
  `nombres` varchar(50) NOT NULL,
  `apellidos` varchar(50) NOT NULL,
  `estado_civil` varchar(20) NOT NULL,
  `sexo` varchar(10) NOT NULL,
  `fecha_emision` date NOT NULL,
  `fecha_vencimiento` date NOT NULL,
  `nacionalidad` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `cedula`
--

INSERT INTO `cedula` (`n_cedula`, `acta_nacimiento`, `nombres`, `apellidos`, `estado_civil`, `sexo`, `fecha_emision`, `fecha_vencimiento`, `nacionalidad`) VALUES
(1, 1, 'hola', 'adios', 'soltero', 'm', '2023-10-11', '2033-10-11', 'Venezolano'),
(2, 2, '', '', 'Soltero', 'M', '2023-04-11', '2023-04-11', 'Venezolano'),
(3, 3, '', '', 'Soltero', 'M', '2023-04-11', '2023-04-11', 'Venezolano'),
(4, 4, '', '', 'Soltero', 'Femenino', '2023-04-11', '2023-04-26', 'Venezolano'),
(5, 5, '', '', 'Soltero', 'M', '2023-04-11', '2023-04-16', 'Venezolano'),
(6, 6, '', '', 'gdfg', 'dgdf', '2023-04-11', '2023-04-26', 'Venezolano');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `prefecturas`
--

CREATE TABLE `prefecturas` (
  `id_prefectura` int(11) NOT NULL COMMENT 'Primary Key',
  `nombre_registro` varchar(100) NOT NULL COMMENT 'nombre de la prefectura o oficina de registro',
  `estado` varchar(50) NOT NULL,
  `municipio` varchar(50) NOT NULL,
  `parroquia` varchar(50) NOT NULL,
  `direccion` varchar(100) NOT NULL,
  `director_nombre` varchar(50) NOT NULL,
  `director_apellido` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `prefecturas`
--

INSERT INTO `prefecturas` (`id_prefectura`, `nombre_registro`, `estado`, `municipio`, `parroquia`, `direccion`, `director_nombre`, `director_apellido`) VALUES
(1, 'Registro Civil Parroquial Coquivacoa ', 'Zulia', 'Maracaibo', 'Coquivacoa', 'Av. 6 entre calles 54B y 55 urbanización zapara, entre los edificios zapara y el CDI', 'Jose', 'Perez'),
(2, 'Registro Civil Parroquial Chiquinquirá', 'Zulia', 'Maracaibo', 'Chiquinquirá', 'Calle 95 del saladillo detrás de panorama.', 'Carlos', 'Rodriguez'),
(3, 'Registro Civil Parroquial Cacique Mara', 'Zulia', 'Maracaibo', 'Cacique Mara', 'Av. 41 entre calles 92A y 93, sector cañada honda, diagonal al colegio consuelo nava', 'Antonio', 'Banderas'),
(4, 'Registro Civil Olegario Villalobos', 'Zulia', 'Maracaibo', 'Olegario Villalobos', 'Plaza de la República, av. 78 Dr. Portillo, calle 77 (detrás de la concha acústica)', 'Andres', 'Gonzalez');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `acta_defuncion`
--
ALTER TABLE `acta_defuncion`
  ADD PRIMARY KEY (`id_acta_defuncion`),
  ADD KEY `a_nacimiento_fallecido` (`a_nacimiento_fallecido`),
  ADD KEY `c_informante` (`c_informante`);

--
-- Indices de la tabla `acta_divorcio`
--
ALTER TABLE `acta_divorcio`
  ADD PRIMARY KEY (`n_acta`),
  ADD KEY `esposo` (`c_conyuge1`),
  ADD KEY `esposa` (`c_conyuge2`),
  ADD KEY `id_hijo1` (`id_hijo1`),
  ADD KEY `id_hijo2` (`id_hijo2`),
  ADD KEY `id_prefectura` (`id_prefectura`),
  ADD KEY `n_acta` (`n_acta`,`c_conyuge1`,`c_conyuge2`,`id_ab_conyuge1`,`id_ab_conyuge2`,`id_hijo1`,`id_hijo2`,`id_prefectura`);

--
-- Indices de la tabla `acta_matrimonio`
--
ALTER TABLE `acta_matrimonio`
  ADD PRIMARY KEY (`nro_acta`),
  ADD KEY `prefectura` (`id_prefectura`);

--
-- Indices de la tabla `acta_nacimiento`
--
ALTER TABLE `acta_nacimiento`
  ADD PRIMARY KEY (`nro_acta`),
  ADD KEY `id_prefectura` (`id_prefectura`) USING BTREE;

--
-- Indices de la tabla `cedula`
--
ALTER TABLE `cedula`
  ADD PRIMARY KEY (`n_cedula`),
  ADD KEY `n_cedula` (`n_cedula`),
  ADD KEY `acta_nacimiento` (`acta_nacimiento`);

--
-- Indices de la tabla `prefecturas`
--
ALTER TABLE `prefecturas`
  ADD PRIMARY KEY (`id_prefectura`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `acta_defuncion`
--
ALTER TABLE `acta_defuncion`
  MODIFY `id_acta_defuncion` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `acta_divorcio`
--
ALTER TABLE `acta_divorcio`
  MODIFY `n_acta` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Primary Key', AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `acta_nacimiento`
--
ALTER TABLE `acta_nacimiento`
  MODIFY `nro_acta` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `prefecturas`
--
ALTER TABLE `prefecturas`
  MODIFY `id_prefectura` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Primary Key', AUTO_INCREMENT=5;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `acta_defuncion`
--
ALTER TABLE `acta_defuncion`
  ADD CONSTRAINT `acta_defuncion_ibfk_1` FOREIGN KEY (`a_nacimiento_fallecido`) REFERENCES `acta_nacimiento` (`nro_acta`);

--
-- Filtros para la tabla `acta_divorcio`
--
ALTER TABLE `acta_divorcio`
  ADD CONSTRAINT `acta_divorcio_ibfk_10` FOREIGN KEY (`id_prefectura`) REFERENCES `prefecturas` (`id_prefectura`),
  ADD CONSTRAINT `acta_divorcio_ibfk_2` FOREIGN KEY (`c_conyuge1`) REFERENCES `cedula` (`n_cedula`),
  ADD CONSTRAINT `acta_divorcio_ibfk_3` FOREIGN KEY (`c_conyuge2`) REFERENCES `cedula` (`n_cedula`),
  ADD CONSTRAINT `acta_divorcio_ibfk_8` FOREIGN KEY (`id_hijo1`) REFERENCES `acta_nacimiento` (`nro_acta`),
  ADD CONSTRAINT `acta_divorcio_ibfk_9` FOREIGN KEY (`id_hijo2`) REFERENCES `acta_nacimiento` (`nro_acta`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
