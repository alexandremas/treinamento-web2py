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

- Try, catch, finally

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
```