-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 03-04-2023 a las 03:51:52
-- Versión del servidor: 10.4.27-MariaDB
-- Versión de PHP: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `registrocivilbdd`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `abogados`
--

CREATE TABLE `abogados` (
  `id_abogado` int(11) NOT NULL COMMENT 'Primary Key',
  `nombres_abogado` varchar(50) NOT NULL,
  `apellido_abogado` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `abogados`
--

INSERT INTO `abogados` (`id_abogado`, `nombres_abogado`, `apellido_abogado`) VALUES
(30237967, 'Miguel Alfonso', 'Quiroz Manga');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `acta_defuncion`
--

CREATE TABLE `acta_defuncion` (
  `id_acta_defuncion` int(11) NOT NULL,
  `a_nacimiento_fallecido` int(11) NOT NULL COMMENT 'cedula fallecido',
  `fallecido_nombres` varchar(50) NOT NULL COMMENT 'nombres del fallecido',
  `fallecido_apellidos` varchar(50) NOT NULL COMMENT 'apellidos del fallecido',
  `edad_fallecido` int(11) NOT NULL COMMENT 'edad del fallecido',
  `sexo_fallecido` varchar(10) NOT NULL COMMENT 'sexo del fallecido',
  `estado_civil_f` varchar(20) NOT NULL COMMENT 'estado civil del fallecido',
  `fecha_defuncion` date NOT NULL,
  `hora_defuncion` time NOT NULL,
  `lugar_defuncion` varchar(50) NOT NULL,
  `causa_muerte` varchar(100) NOT NULL,
  `c_informante` int(11) NOT NULL COMMENT 'cedula del informante',
  `informante_nombre` varchar(50) NOT NULL,
  `informante_apellido` varchar(50) NOT NULL,
  `relacion_informante` varchar(50) NOT NULL,
  `madre_nombres` varchar(50) DEFAULT NULL COMMENT 'nombres de la madre',
  `madre_apellidos` varchar(50) DEFAULT NULL COMMENT 'apellidos de la madre',
  `padre_nombres` varchar(50) DEFAULT NULL,
  `padre_apellidos` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `acta_divorcio`
--

CREATE TABLE `acta_divorcio` (
  `n_acta` int(11) NOT NULL COMMENT 'Primary Key',
  `c_conyuge1` int(11) NOT NULL,
  `conyuge1_nombres` varchar(50) NOT NULL COMMENT 'nombres del primero conyuge',
  `conyuge1_apellidos` varchar(50) NOT NULL COMMENT 'apellidos del primer conyuge',
  `c_conyuge2` int(11) NOT NULL,
  `conyuge2_nombres` varchar(50) NOT NULL COMMENT 'nombres del segundo conyuge',
  `conyuge2_apellidos` varchar(50) NOT NULL COMMENT 'apellidos del segundo conyuge',
  `id_ab_conyuge1` int(11) NOT NULL,
  `nombres_ab_conyuge1` varchar(50) NOT NULL COMMENT 'nombres abogado conyuge 1',
  `apellidos_ab_conyuge1` varchar(50) NOT NULL COMMENT 'apellidos abogado conyuge 1',
  `id_ab_conyuge2` int(11) NOT NULL,
  `nombres_ab_conyuge2` varchar(50) NOT NULL COMMENT 'nombres abogado conyuge 2',
  `apellidos_ab_conyuge2` varchar(50) NOT NULL COMMENT 'apellidos abogado conyuge 2',
  `id_hijo1` int(11) DEFAULT NULL COMMENT 'acta de nacimiento hijo 1',
  `nombres_hijo1` varchar(50) DEFAULT NULL COMMENT 'nombres hijo 1',
  `apellidos_hijo1` varchar(50) DEFAULT NULL COMMENT 'apellidos hijo 1',
  `id_hijo2` int(11) DEFAULT NULL COMMENT 'acta de nacimiento hijo 2',
  `nombres_hijo2` varchar(50) DEFAULT NULL COMMENT 'nombres hijo 2',
  `apellidos_hijo2` varchar(50) DEFAULT NULL COMMENT 'apellidos hijo 2',
  `id_prefectura` int(11) NOT NULL COMMENT 'id de la prefectura/registro',
  `nombre_registro_civil` varchar(100) NOT NULL COMMENT 'nombre de la prefectura/registro',
  `dir_registro_nmbr` varchar(50) NOT NULL,
  `dir_registro_aplld` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `acta_matrimonio`
--

CREATE TABLE `acta_matrimonio` (
  `nro_acta` int(11) NOT NULL,
  `fecha_acta` date NOT NULL,
  `id_contrayente1` int(11) NOT NULL,
  `nmbr_contrayente1` varchar(50) NOT NULL COMMENT 'nombre de contrayente 1',
  `aplldo_contrayente1` varchar(50) NOT NULL COMMENT 'apellidos del contrayente 1',
  `id_contrayente2` int(11) NOT NULL,
  `nmbr_contrayente2` varchar(50) NOT NULL COMMENT 'nombre de contrayente 2',
  `aplldo_contrayente2` varchar(50) NOT NULL COMMENT 'apellidos contrayente 2',
  `id_registrador_civil` int(11) NOT NULL,
  `nmbr_registrador` varchar(50) NOT NULL COMMENT 'nombres registrador civil',
  `aplldo_registrador` varchar(50) NOT NULL COMMENT 'apellidos registrador civil',
  `id_testigo1` int(11) NOT NULL,
  `nmbr_testigo1` varchar(50) NOT NULL COMMENT 'nombres testigo 1',
  `apllido_testigo1` varchar(50) NOT NULL COMMENT 'apellidos testigo 1',
  `id_testigo2` int(11) NOT NULL,
  `nmbr_testigo2` varchar(50) NOT NULL COMMENT 'nombres testigo 2',
  `apllido_testigo2` varchar(50) NOT NULL COMMENT 'apellidos testigo 2',
  `id_prefectura` int(11) NOT NULL COMMENT 'id de la prefectura',
  `nombre_registro_civil` varchar(100) NOT NULL,
  `dir_registro_nmbr` varchar(50) NOT NULL,
  `dir_registro_aplld` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

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
  `sexo` varchar(10) NOT NULL,
  `cedula_padre` int(11) NOT NULL,
  `nombre_padre` varchar(50) NOT NULL,
  `apellido_padre` varchar(50) NOT NULL,
  `cedula_madre` int(11) NOT NULL,
  `nombre_madre` varchar(50) NOT NULL,
  `apellido_madre` varchar(50) NOT NULL,
  `id_prefectura` int(11) NOT NULL,
  `nombre_registro_civil` varchar(100) NOT NULL,
  `dir_registro_nmbr` varchar(50) NOT NULL,
  `dir_registro_aplld` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='Acta de nacimiento';

--
-- Volcado de datos para la tabla `acta_nacimiento`
--

INSERT INTO `acta_nacimiento` (`nro_acta`, `nombres`, `apellidos`, `fecha_nacimiento`, `hora_nacimiento`, `sexo`, `cedula_padre`, `nombre_padre`, `apellido_padre`, `cedula_madre`, `nombre_madre`, `apellido_madre`, `id_prefectura`, `nombre_registro_civil`, `dir_registro_nmbr`, `dir_registro_aplld`) VALUES
(2, 'Miguel Alfonso', 'Quiroz Manga', '2002-09-25', '09:15:00', 'Masculino', 0, 'Jhonnys Alfonso', 'Quiroz Cardozo', 0, 'Belkys Maribel', 'Manga Vanegas', 2, 'Registro Civil Parroquial Chiquinquirá', 'NULL', 'NULL');

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `cedula`
--

INSERT INTO `cedula` (`n_cedula`, `acta_nacimiento`, `nombres`, `apellidos`, `estado_civil`, `sexo`, `fecha_emision`, `fecha_vencimiento`, `nacionalidad`) VALUES
(30237967, 2, 'Miguel Alfonso', 'Quiroz Manga', 'Soltero', 'Masculino', '2013-04-23', '2023-04-23', 'Venezolano');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `prefecturas`
--

CREATE TABLE `prefecturas` (
  `id_prefecturas` int(11) NOT NULL COMMENT 'Primary Key',
  `nombre_registro` varchar(100) NOT NULL COMMENT 'nombre de la prefectura o oficina de registro',
  `estado` varchar(50) NOT NULL,
  `municipio` varchar(50) NOT NULL,
  `parroquia` varchar(50) NOT NULL,
  `direccion` varchar(100) NOT NULL,
  `director_nombre` varchar(50) NOT NULL,
  `director_apellido` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `prefecturas`
--

INSERT INTO `prefecturas` (`id_prefecturas`, `nombre_registro`, `estado`, `municipio`, `parroquia`, `direccion`, `director_nombre`, `director_apellido`) VALUES
(1, 'Registro Civil Parroquial Coquivacoa ', 'Zulia', 'Maracaibo', 'Coquivacoa', 'Av. 6 entre calles 54B y 55 urbanización zapara, entre los edificios zapara y el CDI', 'Jose', 'Perez'),
(2, 'Registro Civil Parroquial Chiquinquirá', 'Zulia', 'Maracaibo', 'Chiquinquirá', 'Calle 95 del saladillo detrás de panorama.', 'Carlos', 'Rodriguez'),
(3, 'Registro Civil Parroquial Cacique Mara', 'Zulia', 'Maracaibo', 'Cacique Mara', 'Av. 41 entre calles 92A y 93, sector cañada honda, diagonal al colegio consuelo nava', 'Antonio', 'Banderas'),
(4, 'Registro Civil Olegario Villalobos', 'Zulia', 'Maracaibo', 'Olegario Villalobos', 'Plaza de la República, av. 78 Dr. Portillo, calle 77 (detrás de la concha acústica)', 'Andres', 'Gonzalez');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `abogados`
--
ALTER TABLE `abogados`
  ADD PRIMARY KEY (`id_abogado`);

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
  ADD KEY `id_ab_conyuge1` (`id_ab_conyuge1`),
  ADD KEY `id_ab_conyuge2` (`id_ab_conyuge2`),
  ADD KEY `id_hijo1` (`id_hijo1`),
  ADD KEY `id_hijo2` (`id_hijo2`),
  ADD KEY `id_prefectura` (`id_prefectura`);

--
-- Indices de la tabla `acta_matrimonio`
--
ALTER TABLE `acta_matrimonio`
  ADD PRIMARY KEY (`nro_acta`),
  ADD KEY `id_contrayente1` (`id_contrayente1`),
  ADD KEY `id_contrayente2` (`id_contrayente2`),
  ADD KEY `abogado_contrayente1` (`id_registrador_civil`),
  ADD KEY `abogado_contrayente2` (`id_testigo2`),
  ADD KEY `id_testigo1` (`id_testigo1`),
  ADD KEY `prefectura` (`id_prefectura`);

--
-- Indices de la tabla `acta_nacimiento`
--
ALTER TABLE `acta_nacimiento`
  ADD PRIMARY KEY (`nro_acta`),
  ADD KEY `id_prefectura` (`id_prefectura`);

--
-- Indices de la tabla `cedula`
--
ALTER TABLE `cedula`
  ADD PRIMARY KEY (`n_cedula`),
  ADD KEY `n_cedula` (`n_cedula`),
  ADD KEY `apellido` (`apellidos`),
  ADD KEY `acta_nacimiento` (`acta_nacimiento`);

--
-- Indices de la tabla `prefecturas`
--
ALTER TABLE `prefecturas`
  ADD PRIMARY KEY (`id_prefecturas`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `acta_defuncion`
--
ALTER TABLE `acta_defuncion`
  MODIFY `id_acta_defuncion` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `acta_divorcio`
--
ALTER TABLE `acta_divorcio`
  MODIFY `n_acta` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Primary Key';

--
-- AUTO_INCREMENT de la tabla `acta_nacimiento`
--
ALTER TABLE `acta_nacimiento`
  MODIFY `nro_acta` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `prefecturas`
--
ALTER TABLE `prefecturas`
  MODIFY `id_prefecturas` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Primary Key', AUTO_INCREMENT=5;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `abogados`
--
ALTER TABLE `abogados`
  ADD CONSTRAINT `abogados_ibfk_1` FOREIGN KEY (`id_abogado`) REFERENCES `cedula` (`n_cedula`);

--
-- Filtros para la tabla `acta_defuncion`
--
ALTER TABLE `acta_defuncion`
  ADD CONSTRAINT `acta_defuncion_ibfk_1` FOREIGN KEY (`a_nacimiento_fallecido`) REFERENCES `acta_nacimiento` (`nro_acta`);

--
-- Filtros para la tabla `acta_divorcio`
--
ALTER TABLE `acta_divorcio`
  ADD CONSTRAINT `acta_divorcio_ibfk_10` FOREIGN KEY (`id_prefectura`) REFERENCES `prefecturas` (`id_prefecturas`),
  ADD CONSTRAINT `acta_divorcio_ibfk_2` FOREIGN KEY (`c_conyuge1`) REFERENCES `cedula` (`n_cedula`),
  ADD CONSTRAINT `acta_divorcio_ibfk_3` FOREIGN KEY (`c_conyuge2`) REFERENCES `cedula` (`n_cedula`),
  ADD CONSTRAINT `acta_divorcio_ibfk_6` FOREIGN KEY (`id_ab_conyuge1`) REFERENCES `abogados` (`id_abogado`),
  ADD CONSTRAINT `acta_divorcio_ibfk_7` FOREIGN KEY (`id_ab_conyuge2`) REFERENCES `abogados` (`id_abogado`),
  ADD CONSTRAINT `acta_divorcio_ibfk_8` FOREIGN KEY (`id_hijo1`) REFERENCES `acta_nacimiento` (`nro_acta`),
  ADD CONSTRAINT `acta_divorcio_ibfk_9` FOREIGN KEY (`id_hijo2`) REFERENCES `acta_nacimiento` (`nro_acta`);

--
-- Filtros para la tabla `acta_matrimonio`
--
ALTER TABLE `acta_matrimonio`
  ADD CONSTRAINT `acta_matrimonio_ibfk_1` FOREIGN KEY (`id_contrayente1`) REFERENCES `cedula` (`n_cedula`),
  ADD CONSTRAINT `acta_matrimonio_ibfk_2` FOREIGN KEY (`id_contrayente2`) REFERENCES `cedula` (`n_cedula`),
  ADD CONSTRAINT `acta_matrimonio_ibfk_6` FOREIGN KEY (`id_registrador_civil`) REFERENCES `abogados` (`id_abogado`),
  ADD CONSTRAINT `acta_matrimonio_ibfk_7` FOREIGN KEY (`id_testigo2`) REFERENCES `abogados` (`id_abogado`),
  ADD CONSTRAINT `acta_matrimonio_ibfk_8` FOREIGN KEY (`id_testigo1`) REFERENCES `cedula` (`n_cedula`),
  ADD CONSTRAINT `acta_matrimonio_ibfk_9` FOREIGN KEY (`id_prefectura`) REFERENCES `prefecturas` (`id_prefecturas`);

--
-- Filtros para la tabla `acta_nacimiento`
--
ALTER TABLE `acta_nacimiento`
  ADD CONSTRAINT `acta_nacimiento_ibfk_1` FOREIGN KEY (`id_prefectura`) REFERENCES `prefecturas` (`id_prefecturas`);

--
-- Filtros para la tabla `cedula`
--
ALTER TABLE `cedula`
  ADD CONSTRAINT `cedula_ibfk_1` FOREIGN KEY (`acta_nacimiento`) REFERENCES `acta_nacimiento` (`nro_acta`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
