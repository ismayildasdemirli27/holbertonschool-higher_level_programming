#!/usr/bin/env python3
from abc import ABC, abstractmethod

class Animal(ABC):
    """Abstract Animal class"""
    
    @abstractmethod
    def sound(self):
        """Abstract method that must be implemented by subclasses"""
        pass

class Dog(Animal):
    """Dog subclass inheriting from Animal"""
    
    def sound(self):
        """Returns the Dog's sound"""
        return "Bark"

class Cat(Animal):
    """Cat subclass inheriting from Animal"""
    
    def sound(self):
        """Returns the Cat's sound"""
        return "Meow"
