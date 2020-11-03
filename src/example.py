import fire
from conditional_sample import interact_model


def test(text=''):
    output = interact_model(text)
    print("=" * 40 + " OUTPUT " + "=" * 40)
    print(output)
    print("=" * 80)


fire.Fire(interact_model)
