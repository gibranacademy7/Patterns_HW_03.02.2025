from abc import ABC, abstractmethod

# Component
class PackableItem(ABC):
    @abstractmethod
    def get_weight(self):
        pass