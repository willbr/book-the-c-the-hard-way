include_lib('stdio.h')


def main(argc: int, argv: tuple[str]) -> int:
    nul_byte:char = char('\0')
    distance: int = 100
    power: float = 2.345
    super_power: double = 56789.4532
    initial: char = char('A')
    first_name: tuple[char] = "Zed"
    last_name: tuple[char] = "Shaw"

    printf("You are %d miles away.\n", distance)
    printf("You have %f levels of power.\n", power)
    printf("You have %f awesome super powers.\n", super_power)

    printf("I have an inital %c.\n", initial)
    printf("I have a first name %s.\n", first_name)
    printf("I have a last name s.\n", last_name)
    printf("My whole name is %s %c. %s.\n",
            first_name,
            initial,
            last_name);


    bugs: int = 100
    bug_rate: double = 1.2

    printf("You have %d bugs at the imaginary rate of %f.\n",
            bugs,
            bug_rate)

    universe_of_defects: long = 1 * 1024 * 1024 * 1024
    printf("The entire universe has %ld bugs.\n",
            universe_of_defects)

    expected_bugs: double = bugs * bug_rate
    printf("You are expected to have %f bugs.\n",
            expected_bugs)


    part_of_universe: double = expected_bugs / universe_of_defects
    printf("This is only a %e portion of the universe.\n",
            part_of_universe)


    nul_byte:char = char('\0')
    care_percentage: int = bugs * nul_byte
    printf("Which means you should care %d%%.\n",
            care_percentage)
    return 0
