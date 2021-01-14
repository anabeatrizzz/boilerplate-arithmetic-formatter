### [README original](https://github.com/freeCodeCamp/boilerplate-arithmetic-formatter/blob/master/README.md)

### Tarefa

Os estudantes do ensino fundamental frequentemente escrevem problemas aritméticos verticalmente para ficar fácil de resolver. Por exemplo, "235 + 52" fica:

```
  235
+  52
-----
```

Crie uma função que recebe uma lista de strings que são problemas aritméticos e retorna os problemas organizados verticalmente e lado a lado. A função deve ter um segundo argumento opcional. Quando este for `True`, as respostas devem ser mostradas.

### Por exemplo

Chamando a função:

```py
arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
```

Resultado:

```
   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
```

Chamando a função:
```py
arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
```

Resultado:
```
  32         1      9999      523
+  8    - 3801    + 9999    -  49
----    ------    ------    -----
  40     -3800     19998      474
```

### Regras

A função retornará a conversão correta se os problemas fornecidos estiverem formatados corretamente, se não, ela **retornará** uma **string** que descreve um erro descritivo para o usuário.

* Situações em que um erro é retornado:
  * Se **muitos problemas** forem fornecidos. O limite é **cinco**, mais do que isso a função retornará:
    `Error: Too many problems.`
  * Os operadores que a função aceitará são **adição** e **subtração**. Multiplicação e divisão retornarão um erro. Outros operadores não mencionados aqui não precisarão ser testados. O erro retornado será:
    `Error: Operator must be '+' or '-'.`
  * Cada numero (operando) deve conter apenas dígitos. Se não, a função retornará:
    `Error: Numbers must only contain digits.`
  * Cada operando (vulgo numero em cada lado do operador) precisa ter quatro dígitos. Se não, a string de erro retornada será:
    `Error: Numbers cannot be more than four digits.`
*  Se o usuário escreveu os problemas corretamente, a conversão retornada será:
    * Deverá ter um único espaço entre o operador e o maior dos operandos, o operador estará na mesma linha que o segundo operando, os dois operandos estarão na mesma ordem fornecida (o primeiro no topo e o segundo embaixo).
    * Números devem estar alinhados na direita.
    * Deverá ter quatro espaços entre cada problema.
    * Deverá ter hifens embaixo de cada problema. Os hifens devem preencher todo o problema individualmente. (O exemplo acima mostra como deve ser feito.)

### Desenvolvimento

Escreva seu código em `arithmetic_arranger.py`. Para desenvolver, você pode usar `main.py` para testar sua função `arithmetic_arranger()`. Clique no botão "run" e `main.py` executará.

### Testando

A unidade de testes para este projeto está em `test_module.py`. Importamos os testes de `test_module.py` para `main.py` para sua conveniência. Os testes executarão automaticamente toda vez que você apertar o botão "run".

### Enviando

Copie a URL do seu projeto e envie para freeCodeCamp.
