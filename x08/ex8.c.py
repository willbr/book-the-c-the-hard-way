include_lib('stdio.h')


def main(argc: int, argv: tuple[str]) -> int:
    i: int = 0

    if argc == 1:
        printf("You only have one argument. You suck.\n")
    elif 1 < argc and argc < 4:
        print("Here's your arguments:\n")

        for i in range(argc):
            printf("%s ", argv[i])

        printf("\n")
    else:
        printf("You have too many arguments. You suck.\n")

        return 0

