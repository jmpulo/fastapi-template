from typing import Any

from faker.providers import DynamicProvider

body_part_provider = DynamicProvider(
    provider_name="body_part",
    elements=[
        "ear",
        "eye",
        "nose",
        "paw",
        "tail",
        "whisker",
        "foot",
        "leg",
        "back",
        "belly",
        "arm",
        "shoulder",
        "neck",
        "head",
        "chest",
    ],
)


def generate_unique(existing_value: Any, generator: callable, *args) -> Any:
    """
    Generate a unique value using the provided generator function.
    """
    new_value = generator(*args)
    while new_value == existing_value:
        new_value = generator(*args)
    return new_value
