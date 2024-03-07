DIRECTORY_SIZE_LIMIT = 100_000
TOTAL_DISK_SPACE = 70_000_000
REQUIRED_UNUSED_DISK_SPACE = 30_000_000


class Directory:
    _total_allowed_size = 0
    _min_space = None

    def __init__(self, directory_name, parent=None):
        self.name = directory_name
        self.parent = parent
        self.files = {}
        self.subdirectories = {}
        self.total_size = 0

    @classmethod
    def reset_class(cls):
        cls._total_allowed_size = 0
        cls._min_space = None

    @classmethod
    def add_to_total_allowed_size(cls, value):
        cls._total_allowed_size += value

    @classmethod
    def get_total_allowed_size(cls):
        return cls._total_allowed_size

    @classmethod
    def update_min_space(cls, space):
        if cls._min_space is None or space < cls._min_space:
            cls._min_space = space

    @classmethod
    def get_min_space(cls):
        return cls._min_space

    def compute_size(self):
        self.total_size = 0
        for file_size in self.files.values():
            self.total_size += file_size
        for subdirectory in self.subdirectories.values():
            self.total_size += subdirectory.compute_size()

        return self.total_size
    
    def compute_total_allowed_size(self):
        if self.total_size <= DIRECTORY_SIZE_LIMIT:
            self.add_to_total_allowed_size(self.total_size)

        for subdirectory in self.subdirectories.values():
            subdirectory.compute_total_allowed_size()
    
    def find_min_space_to_delete(self, min_space_to_delete):
        if self.total_size >= min_space_to_delete:
            self.update_min_space(self.total_size)

        for subdirectory in self.subdirectories.values():
            subdirectory.find_min_space_to_delete(min_space_to_delete)


def main(filename):
    root = Directory("/")
    current_dir = None

    with open(filename) as input_file:
        for line in input_file:
            line = line.strip()

            if line.startswith("$ cd "):
                if line == "$ cd /":
                    current_dir = root
                elif line == "$ cd ..":
                    current_dir = current_dir.parent
                else:
                    subdirectory_name = line[len("$ cd "):]
                    if subdirectory_name in current_dir.subdirectories:
                        current_dir = current_dir.subdirectories[subdirectory_name]
                    else:
                        subdirectory = Directory(subdirectory_name, parent=current_dir)
                        current_dir.subdirectories[subdirectory_name] = subdirectory
                        current_dir = subdirectory
            elif line != "$ ls":
                description, element_name = line.split()
                if description == "dir":
                    if element_name not in current_dir.subdirectories:
                        subdirectory = Directory(element_name, parent=current_dir)
                        current_dir.subdirectories[element_name] = subdirectory
                else:
                    file_size = int(description)
                    current_dir.files[element_name] = file_size

    Directory.reset_class()
    total_size = root.compute_size()

    # part 1
    root.compute_total_allowed_size()
    result_part_1 = Directory.get_total_allowed_size()

    # part 2
    available_space = TOTAL_DISK_SPACE - total_size
    min_space_to_delete = REQUIRED_UNUSED_DISK_SPACE - available_space
    root.find_min_space_to_delete(min_space_to_delete)
    result_part_2 = Directory.get_min_space()

    print(f"part 1: {result_part_1}")
    print(f"part 2: {result_part_2}")


if __name__ == "__main__":
    for name in [
        "sample.txt",
        "input.txt"
    ]:
        print(f"-- {name} --")
        main(name)
