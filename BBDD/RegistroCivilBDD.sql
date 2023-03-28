-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost
-- Tiempo de generación: 28-03-2023 a las 20:48:50
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
-- Base de datos: `RegistroCivilBDD`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `abogados`
--

CREATE TABLE `abogados` (
  `id_abogado` int(11) NOT NULL COMMENT 'Primary Key',
  `email_abogado` varchar(100) DEFAULT NULL,
  `tlf_abogado` varchar(30) NOT NULL,
  `nombres_abogado` varchar(50) NOT NULL,
  `apellido_abogado` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

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
  `c_padre` int(11) NOT NULL COMMENT 'cedula del padre',
  `padre_nombres` varchar(50) NOT NULL COMMENT 'nombres del padre',
  `padre_apellidos` varchar(50) NOT NULL COMMENT 'apellidos del padre',
  `c_madre` int(11) NOT NULL COMMENT 'cedula de la madre',
  `madre_nombres` varchar(50) NOT NULL COMMENT 'nombres de la madre',
  `madre_apellidos` varchar(50) NOT NULL COMMENT 'apellidos de la madre'
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
  `email_esposo` varchar(70) DEFAULT NULL,
  `tlf_esposo` varchar(30) NOT NULL,
  `dir_esposo` int(11) NOT NULL,
  `c_conyuge2` int(11) NOT NULL,
  `conyuge2_nombres` varchar(50) NOT NULL COMMENT 'nombres del segundo conyuge',
  `conyuge2_apellidos` varchar(50) NOT NULL COMMENT 'apellidos del segundo conyuge',
  `email_esposa` varchar(70) DEFAULT NULL,
  `tlf_esposa` varchar(30) NOT NULL,
  `dir_esposa` int(11) NOT NULL,
  `id_ab_conyuge1` int(11) NOT NULL,
  `id_ab_conyuge2` int(11) NOT NULL,
  `nombres_ab_conyuge1` varchar(50) NOT NULL COMMENT 'nombres abogado conyuge 1',
  `apellidos_ab_conyuge1` varchar(50) NOT NULL COMMENT 'apellidos abogado conyuge 1',
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
  `nombre_estado` varchar(50) NOT NULL,
  `nombre_municipio` varchar(50) NOT NULL,
  `nombre_parroquia` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `acta_matrimonio`
--

CREATE TABLE `acta_matrimonio` (
  `nro_acta` int(11) NOT NULL,
  `prefectura` int(11) NOT NULL COMMENT 'id de la prefectura',
  `nombre_estado` varchar(100) NOT NULL,
  `nombre_municipio` varchar(100) NOT NULL,
  `nombre_parroquia` varchar(100) NOT NULL,
  `nombre_registro_civil` varchar(100) NOT NULL,
  `direccion_prefectura` varchar(100) NOT NULL,
  `fecha_acta` date NOT NULL,
  `id_contrayente1` int(11) NOT NULL,
  `nmbr_contrayente1` varchar(50) NOT NULL COMMENT 'nombre de contrayente 1',
  `aplldo_contrayente1` varchar(50) NOT NULL COMMENT 'apellidos del contrayente 1',
  `ocup_contrayente1` varchar(50) DEFAULT 'NULL',
  `residencia_contrayente1` varchar(100) NOT NULL,
  `id_contrayente2` int(11) NOT NULL,
  `nmbr_contrayente2` varchar(50) NOT NULL COMMENT 'nombre de contrayente 2',
  `aplldo_contrayente2` varchar(50) NOT NULL COMMENT 'apellidos contrayente 2',
  `ocup_contrayente2` varchar(50) DEFAULT NULL,
  `residencia_contrayente2` varchar(100) NOT NULL,
  `id_testigo1` int(11) NOT NULL,
  `nmbr_testigo` varchar(50) NOT NULL COMMENT 'nombre de testigo',
  `apllido_testigo1` varchar(50) NOT NULL COMMENT 'apellidos testigo 1',
  `ocup_testigo1` varchar(50) DEFAULT NULL,
  `abogado_contrayente2` int(11) NOT NULL,
  `abogado_contrayente1` int(11) NOT NULL,
  `nmbr_abogado_con1` varchar(50) NOT NULL COMMENT 'nombres abogado contrayente 1',
  `aplldo_abogado_con1` varchar(50) NOT NULL COMMENT 'apellidos abogado contrayente 1',
  `nmbr_abogado_con2` varchar(50) NOT NULL COMMENT 'nombres abogado contrayente 2',
  `aplldo_abogado_con2` varchar(50) NOT NULL COMMENT 'apellidos abogado contrayente 2'
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
  `nombre_padre` varchar(50) NOT NULL,
  `apellido_padre` varchar(50) NOT NULL,
  `nombre_madre` varchar(50) NOT NULL,
  `apellido_madre` varchar(50) NOT NULL,
  `id_prefectura` int(11) NOT NULL,
  `nombre_registro_civil` varchar(100) NOT NULL,
  `nombre_estado` varchar(50) NOT NULL,
  `nombre_municipio` varchar(50) NOT NULL,
  `nombre_parroquia` varchar(50) NOT NULL,
  `direccio_prefectura` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='Acta de nacimiento';

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
  `direccion` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

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
  ADD KEY `c_padre` (`c_padre`),
  ADD KEY `c_madre` (`c_madre`),
  ADD KEY `c_informante` (`c_informante`);

--
-- Indices de la tabla `acta_divorcio`
--
ALTER TABLE `acta_divorcio`
  ADD PRIMARY KEY (`n_acta`),
  ADD KEY `esposo` (`c_conyuge1`),
  ADD KEY `esposa` (`c_conyuge2`),
  ADD KEY `dir_esposo` (`dir_esposo`),
  ADD KEY `dir_esposa` (`dir_esposa`),
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
  ADD KEY `residencia_contrayente1` (`residencia_contrayente1`),
  ADD KEY `abogado_contrayente1` (`abogado_contrayente1`),
  ADD KEY `abogado_contrayente2` (`abogado_contrayente2`),
  ADD KEY `id_testigo1` (`id_testigo1`),
  ADD KEY `prefectura` (`prefectura`);

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
  MODIFY `nro_acta` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `prefecturas`
--
ALTER TABLE `prefecturas`
  MODIFY `id_prefecturas` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Primary Key';

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
  ADD CONSTRAINT `acta_defuncion_ibfk_1` FOREIGN KEY (`a_nacimiento_fallecido`) REFERENCES `acta_nacimiento` (`nro_acta`),
  ADD CONSTRAINT `acta_defuncion_ibfk_2` FOREIGN KEY (`c_padre`) REFERENCES `cedula` (`n_cedula`),
  ADD CONSTRAINT `acta_defuncion_ibfk_3` FOREIGN KEY (`c_madre`) REFERENCES `cedula` (`n_cedula`),
  ADD CONSTRAINT `acta_defuncion_ibfk_4` FOREIGN KEY (`c_informante`) REFERENCES `cedula` (`n_cedula`);

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
  ADD CONSTRAINT `acta_matrimonio_ibfk_6` FOREIGN KEY (`abogado_contrayente1`) REFERENCES `abogados` (`id_abogado`),
  ADD CONSTRAINT `acta_matrimonio_ibfk_7` FOREIGN KEY (`abogado_contrayente2`) REFERENCES `abogados` (`id_abogado`),
  ADD CONSTRAINT `acta_matrimonio_ibfk_8` FOREIGN KEY (`id_testigo1`) REFERENCES `cedula` (`n_cedula`),
  ADD CONSTRAINT `acta_matrimonio_ibfk_9` FOREIGN KEY (`prefectura`) REFERENCES `prefecturas` (`id_prefecturas`);

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
