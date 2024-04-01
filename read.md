1. En cmd colocar sls
2. Seleccionar la opción HTTP python
3. colocar nombre
4. Para crear el entrono: virtualenv -p python3 env


* __en el .yml colocar:__

plugins:
  - serverless-offline

useDotenv: true #para tomar variables del entorno virtual