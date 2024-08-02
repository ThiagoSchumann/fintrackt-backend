#!/bin/sh

# Subir os contêineres de teste em segundo plano
docker-compose -f docker-compose.yml -f docker-compose.test.yml up -d

# Esperar alguns segundos para garantir que os contêineres estão totalmente inicializados
sleep 10

# Executar os testes
docker-compose -f docker-compose.yml -f docker-compose.test.yml exec web pytest

# Derrubar os contêineres após a execução dos testes
docker-compose -f docker-compose.yml -f docker-compose.test.yml down
