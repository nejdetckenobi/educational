from abc import ABC, abstractmethod


# This class is a contract and a template for developers.
# Any method under @abstractmethod decorator must be implemented.
# The adapters will be a subclass of BaseAdapter and BaseAdapter will not be used directly.
class BaseAdapter(ABC):
    @abstractmethod
    def action(self, context):
        raise NotImplementedError("This method must be implemented first.")
