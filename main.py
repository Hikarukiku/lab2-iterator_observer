from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List

class AbstractSubject(ABC):

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass


class Subject(AbstractSubject):

    _state: int = None
  
    _observers: List[Observer] = []

    def attach(self, observer: Observer):
        print("Subject: Attached an observer.")
        self._observers.append(observer)

    def detach(self, observer: Observer):
        self._observers.remove(observer)

    def notify(self):
        print("Subject: Notifying observers...")
        for observer in self._observers:
            observer.update(self)

    def some_business_logic(self, x):
        print("\nSubject: I'm doing something important.")
        self._state = x
        print(f"Subject: My state has just changed to: {self._state}")
        self.notify()


class Observer(ABC):
    @abstractmethod
    def update(self, subject: Subject) -> None:
        pass

class ObserverA(Observer):
    def update(self, subject: Subject):
        if subject._state < 30:
            print("ObserverA: Reacted to the event")

class ObserverB(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state == 33 or subject._state >= 35:
            print("ObserverB: Reacted to the event")

class TreeNode:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = TreeNode(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = TreeNode(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()

class Iterator:
    
    def __init__(self, root: TreeNode):
        self.nodes_sorted = []
        self.index = -1
        self._inorder(root)
        
    def _inorder(self, root):
        if not root:
            return
        self.nodes_sorted.append(root.data)
        self._inorder(root.left)
        self._inorder(root.right)

    def curr(self) -> int:
        return self.nodes_sorted[self.index]

    def next(self) -> int:
        self.index += 1
        return self.nodes_sorted[self.index]

    def hasNext(self) -> bool:
        return self.index + 1 < len(self.nodes_sorted)

    def print_order(self):
        print(self.nodes_sorted)

root = TreeNode(30)
root.insert(10)
root.insert(35)
root.insert(5)
root.insert(27)
root.insert(33)
root.insert(80)

root.PrintTree()

new_iterator = Iterator(root)

    
subject = Subject()

observer_a = ObserverA()
subject.attach(observer_a)

observer_b = ObserverB()
subject.attach(observer_b)

while (new_iterator.hasNext()):
    subject.some_business_logic(new_iterator.next())

subject.detach(observer_a)
new_iterator.print_order()



