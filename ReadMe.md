# Como utilizar este programa

## Transformação linear: Rotação

Para alterar a matriz a ser rotacionada, troque o valor no arquivo Example.txt, cada vetor entre quebra de linhas, e cada valor dentro do vetor entre virgulas, assim como no exemplo:

```
1,1
2,2
```

 e para alterar os graus, troque no main.py o valor, nesta chamada de método:

```python
rotatedMatrix = vectorRotation.rotate(matrix, 45)
```

note que para a rotação linear foi implementado para matrizes 2x2

## Resolução de sistema linear por Cramer

Para alterar a matriz, é necessário trocar os valores no Example2.txt, e para trocar os valores que estas matrizes resultam, é no ExampleVectorResult.txt, no mesmo formato anteriormente descrito. Segue os exemplos, respectivamente.

Example2.txt:
```
1,2,1
2,-1,1
-1,3,1
```

ExampleVectorResult.txt:
```
0,1,-2
```

Neste exemplo, temos o seguinte sistema linear:

```
x + 2y + z = 0
2x - y + z = 1
-x + 3y + z = -2
```