import os

from dotenv import load_dotenv

load_dotenv()

## todas as variaveis de ambiente do SO
# print(os.environ)

usuario = os.environ['USERNAME']
sistema = os.environ['OS']

print(usuario + ' ' + sistema)


print(os.environ['nome'])

print(os.environ.get('sobrenome', 'Cesar'))

print(os.getenv('nome'))

print(os.getenv('sobrenome', 'Cesar'))


