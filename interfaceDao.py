from abc import ABC, abstractmethod
from modelo import aparelho

class AparelhoDAOInterface(ABC):
    @abstractmethod
    def create(self, aparelho: aparelho):
        pass

    @abstractmethod
    def read(self, aparelho_id: int):
        pass

    @abstractmethod
    def update(self, aparelho: aparelho):
        pass

    @abstractmethod
    def delete(self, aparelho_id: int):
        pass

    @abstractmethod
    def list_all(self):
        pass
    
    @abstractmethod
    def sum_quantity(self):
        pass

    @abstractmethod
    def select_min_max_price(self):
        pass