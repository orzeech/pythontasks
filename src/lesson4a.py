if __name__ == '__main__':
    names = ["Marcin", "Adam", "Agata", "Anna", "Mateusz", "Wojtek", "Kasia", "Tomek", "Kamil",
            "Maria", "Arkadiusz", "Przemysław", "Horacy", "Zofia", "Genowefa", "Serafin"]
    # names.stream().map(s -> s + " Kowalski").collect(Collectors.toList());
    names_and_surnames = list(map(lambda s: s + " Kowalski", names))
    print(names_and_surnames)
    # names_and_surnames.stream().filter(s -> !s.contains("e")).collect(Collectors.toList())
    names_and_surnames_filtered = list(filter(lambda s: "e" not in s, names_and_surnames))
    print(names_and_surnames_filtered)

