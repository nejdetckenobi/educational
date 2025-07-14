from custom_signal import my_custom_signal


@my_custom_signal.register
def sample_callback_1(context):
    print("AHOY! This is the first callback")


@my_custom_signal.register
def sample_callback_2(context):
    print("AHOY! This is the second callback")


if __name__ == "__main__":
    my_custom_signal.trigger({"my": "context"})

