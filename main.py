from engine import *


f = open("./grammar.txt","r")

t = f.read()

#print("conteido", t)

tokens = tokenizer(t)

parse, operations = CoolParser(tokens)

if not operations:
    print(f'Unexpected token: {parse.lex} at Ln: {parse.line}, Col {parse.column}\n')


ast = evaluate_reverse_parse(parse, operations, tokens)
formatter = Format()

# en tree se encuentra guardado el ast de cool, esto hay que imprimirlo en un nuevo tab
tree = formatter.visit(ast,0)
#print(tree)

#aca se encuentran los errores de cada fase de la construccion de los tipos
#es muy importante que si una lista de estas no es vacía se pare el proceso y no continue hasta que se resuelva,
#es decir, por ejemplo si type_collector_errors no es vacía no se ejecuta mas nada

type_collector_errors = []
type_builder_errors = []
type_checker_errors = []
type_inferer_errors = []

collector = Collector(type_collector_errors)

collector.visit(ast)

context = collector.context

# context del type collector (solo es imprimirlo)
print(context)

for error in type_collector_errors:
    print("typecollectorerror", error, "\n")

builder = Builder(context, type_builder_errors)
builder.visit(ast)

for error in type_builder_errors:
    print("typebuildererror", error, "\n")

#context actualizado con el type builder (solo imprimirlo)
print(context)

checker = Checker(context, type_checker_errors)
scope = checker.visit(ast)

for error in type_checker_errors:
    print("typecheckererror", error, "\n")

#print(scope)

inferences = []
inferer = Inferer(context, type_inferer_errors, inferences)
while inferer.visit(ast, scope): pass

print("inferences")
for inference in inferences:
    print(inference)

print("errors")
for error in type_inferer_errors:
    print(error)