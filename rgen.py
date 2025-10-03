import string

import click
from nanoid import generate


@click.command("Generate random string with nanoid")
@click.option("--size", "-s", default=10, help="Size of the string", show_default=True)
@click.option(
    "--alphabet",
    "-a",
    default=string.ascii_lowercase + string.digits,
    help="Alphabet to use",
    show_default=True,
)
@click.option(
    "--use-punctuation",
    "-p",
    default=False,
    is_flag=True,
    help="Use punctuation in alphabet",
)
@click.option(
    "--use-uppercase",
    "-u",
    default=False,
    is_flag=True,
    help="Use uppercase in alphabet",
)
def main(size: int, alphabet: str, use_uppercase: bool, use_punctuation: bool):
    if use_uppercase:
        alphabet += string.ascii_uppercase

    if use_punctuation:
        alphabet += string.punctuation

    print(generate(alphabet, size))


if __name__ == "__main__":
    main()
