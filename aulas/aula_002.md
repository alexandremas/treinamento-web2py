# Treinamento web2py

## Aula 2 (20/03/14)

### 1. Sobre o Python

- Linguagem de programação interpretada
- Fracamente tipada
- Linguagem de programação de alto nível

###	2. Estruturas de dados do Python

-	Caracteres (string)

``` python
texto = 'String'
```

-	Inteiro longo (long int)

``` python
valor = 3
```

-	Ponto flutuante (float)

``` python
valor = 3.14
```

-	Lista (list)

``` python
lista = [9, 'Pedone', 3.14]
```

-	Tupla (tuples)

``` python
tupla = (9, 'Pedone', 3.14)
```

-	Dicionários (dictionaries)

``` python
dicionario = {'banana':3.99, 'maca':2.99}
```

### 3. Estruturas de controles

- If, elif, else

``` python
valor = 3
quantidade = 2
if valor > 3:
	print "maior que 3"
elif valor == 2:
	print "valor é 2"
else:
	print "menor que 2"
```

- For

```python
for x in range(0, 3):
    print x
```

- While

```python
x = 0
while x < 10:
	print x
	x = x+1
```

- Try, except, finally

``` python
try:
	print "Rotina."
except:
	print "Caso algo na rotina acima exiba um erro, roda isto aqui."
finally:
	print "Independente do que aconteça nos dois casos acima, isto é executado."
```

- Funções/Métodos

```python
def soma(a, b):
	return a+b

print soma(3,4) # retorna 7
print "A soma de %s + %s é %s " % (3, 4, soma(3, 4)) # retorna "A soma de 3 + 4 é 7"
```

### 4. Classes

```python
# Implementação da classe pessoa
class Pessoa(object):
	name = ""
	age = 0
	def __init__(self, name, age):
		self.name = name
		self.age  = age
	def isAdult(self):
		if self.age > 18:
			return True
		else:
			return False

# Uso da classe pessoa
pessoa = Pessoa("Luiz Felipe Pedone", 26)
print pessoa.name # retorna "Luiz Felipe Pedone"
print pessoa.isAdult() # retorna True
```

### 5. Consultas com o web2py

Continuando a aplicação da aula anterior, temos o objeto produto. Este objeto possui os campos:

- Nome
- Preço
- Quantidade

Este objeto é definido pelo schema:

``` python
db.define_table('produto',
    Field('nome', label="Produto"),
    Field('preco', 'double', label="Preço"),
    Field('quantidade', 'double')
)
```

Para gerar uma consulta que retorna todos os produtos:

``` python
rows = db(db.produto.id>0).select()
```

Para filtrar por produtos que tenham preço superior a R$150:

``` python
rows = db(db.produto.preco > 150.00).select()
```

Para filtrar por produtos que tenham preço superior a R$150 e a quantidade maior que 10:
``` python
rows = db((db.produto.preco > 150.00) & (db.produto.quantidade > 10.00)).select()
```

### 6. HTML, CSS e Javascript

O resultado da programação com o Web2py é uma página HTML que inclui CSS e javascript.

O HTML é uma notação para organizar a apresentação de conteúdo, enquanto o CSS é uma notação para definir atributos de apresentação deste conteúdo.
O Javascript é uma linguagem para alterar e operar dinâmicamente o conteúdo HTML.

Enquanto os templates HTML estão na pasta 'views', os conteúdos estáticos css, javascript e imagens devem ficar na pasta 'static'.

