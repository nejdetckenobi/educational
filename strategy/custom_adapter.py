from base import BaseAdapter


class CustomAdapter1(BaseAdapter):
    def action(self, context):
        # The implementation is mandatory
        print(f"AHOY! action() method is triggered by {self.__class__.__name__}")
        return None


class CustomNotWorkingAdapter(BaseAdapter):
    pass
