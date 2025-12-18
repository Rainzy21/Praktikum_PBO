class Character:
    def __init__(self, name, health, attack_power):
        self._name = name
        self._health = health
        self._attack_power = attack_power
        print(f"{self._name} bergabung ke dalam pertarungan!")

    def show_info(self):
        print(f"\n--- Character Info ---")
        print(f"Name: {self._name}")
        print(f"Health: {self._health}")
        print(f"Attack Power: {self._attack_power}")

    def attack(self, target):
        print(f"{self._name} menyerang {target.get_name()}!")
        target.take_damage(self._attack_power)

    def take_damage(self, damage):
        self._health -= damage
        if self._health <= 0:
            print(f"{self._name} Telah dikalahkan!")
            self._health = 0
        else:
            print(f"Health {self._name} tersisa {self._health}")

    def get_name(self):
        return self._name


class Warrior(Character):
    def __init__(self, name, health, attack_power, armor):
        super().__init__(name, health, attack_power)
        self._armor = armor
        print(f"Armor set to: {self._armor}")

    def show_info(self):
        super().show_info()
        print(f"Armor: {self._armor}")

    def take_damage(self, damage):
        # damage dikurangi armor
        reduced_damage = max(0, damage - self._armor)
        self._health -= reduced_damage
        if self._health <= 0:
            print(f"{self._name} Telah dikalahkan!")
            self._health = 0
        else:
            print(f"Health {self._name} tersisa {self._health}")


# -- bagian utama program
print("--- Membuat Objek dari Parent Class ---")
aragorn = Character("Aragorn", 100, 15)
aragorn.show_info()

print("\n--- Membuat Objek dari Child Class ---")
gimli = Warrior("Gimli", 120, 20, 5)
gimli.show_info()

print("\n--- Pertarungan Dimulai ---")
aragorn.attack(gimli)
gimli.attack(aragorn)
