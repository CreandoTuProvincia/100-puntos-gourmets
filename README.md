# Selección aleatoria de vinos con 100 puntos (JCR-ready)

Este repositorio documenta la selección aleatoria de 8 vinos entre una lista de 9 candidatos con puntuaciones de 100 puntos por críticos internacionales.

## Metodología

- Lenguaje: Python 3.x  
- Método: `random.sample()` (selección sin reemplazo)  
- Semilla fija: `20250610` para asegurar replicabilidad  
- Verificación: Hash SHA-256 del resultado final

## Resultado

Lista seleccionada:
1. Sorte O Soro 2023  
2. L'Ermita 2022  
3. Pazo Señorans Selección de Añada 2014  
4. Vega Sicilia Único 2015  
5. Cirsion 2021  
6. Tradición Oloroso VORS  
7. Recaredo Homenatge a Josep Mata Capellades 2004  
8. Poley Amontillado Convento Selección 1952

Hash SHA-256 del resultado:  
`8e14e669326bbde9e4a33052c84fb03801299d73da88a87443de911ee2308bdf`

## Reproducibilidad

Ejecuta el script `seleccion_aleatoria.py` en cualquier entorno Python 3.x para comprobar la selección y validar el hash.
