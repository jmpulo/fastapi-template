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
