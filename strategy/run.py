from custom_adapter import CustomAdapter1, CustomNotWorkingAdapter

context = {"my": "context"}

# this will work
custom_adapter = CustomAdapter1()

custom_adapter.action(context=context)

# this will not work
not_working_adapter = CustomNotWorkingAdapter()
