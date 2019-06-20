from .cp import SemanticError, visitor, Context, SelfType, AutoType
from .parser import ProgramNode, ClassDeclarationNode
from .semantic_errors import ERROR_ON_LN_COL

class TypeCollector:
    def __init__(self, errors = []):
        self.context = Context()
        self.errors = errors

        #Tipos especiales
        self.context.add_type(SelfType())
        self.context.add_type(AutoType())

        #Tipos Buit-In
        self.context.create_type('Object')
        self.context.create_type('Bool')
        self.context.create_type('Int')
        self.context.create_type('IO')
        self.context.create_type('String')
    
    @visitor.on('node')
    def visit(self, node):
        pass

    @visitor.when(ProgramNode)
    def visit(self, node):
        for class_def in node.declarations:
            self.visit(class_def)

    @visitor.when(ClassDeclarationNode):
    def visit(self, node):
        try:
            self.context.create_type(node.id.lex)
        except SemanticError as se:
            self.errors.append(ERROR_ON_LN_COL % (node.line, node.column) + se.text)