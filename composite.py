from __future__ import annotations
from abc import ABC
from typing import List

class Component(ABC):

    def parent(self) -> Component:
        return self._parent

    def parent(self, parent: Component):
        self._parent = parent

class Folha(Component):

    def operation(self) -> str:
        return "Folha"

class Composite(Component):

    def __init__(self) -> None:
        self._children: List[Component] = []

    def add(self, component: Component) -> None:
        self._children.append(component)
        component.parent = self

    def remove(self, component: Component) -> None:
        self._children.remove(component)
        component.parent = None

    def is_composite(self) -> bool:
        return True

    def operation(self) -> str:

        results = []
        for child in self._children:
            results.append(child.operation())
        return f"Galho({'+'.join(results)})"

def code(component: Component) -> None:

    print(f"{component.operation()}", end="")

def code2(component1: Component, component2: Component) -> None:

    if component1.is_composite():
        component1.add(component2)

    print(f"{component1.operation()}", end="")

if __name__ == "__main__":
    
    simple = Folha()
    print("Componente simples: ")
    code(simple)
    print("\n")
    
    tree = Composite()

    branch1 = Composite()
    branch1.add(Folha())
    branch1.add(Folha())

    branch2 = Composite()
    branch2.add(Folha())

    tree.add(branch1)
    tree.add(branch2)

    print("Árvore composta: ")
    code(tree)
    print("\n")

    print("Componente simples adicionado na árvore: ")
    code2(tree, simple)