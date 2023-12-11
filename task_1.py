import doctest


class Dota2Hero:
    def __init__(self, hero_name: str, ability_name: str):
        """
        Initialize a Dota 2 Hero with name and abylity.
        :param hero_name: Name of the hero.
        :param ability_name: Name of his ability.
        Example:
        >>> weapon = Dota2Hero("Razor", "Plasma Field")
        """
        if not isinstance(hero_name, str):
            raise TypeError("Name should be of type str.")
        if not hero_name:
            raise ValueError("Name should not be an empty string.")
        self.hero_name: str = hero_name

        if not isinstance(ability_name, str):
            raise TypeError("Name should be of type str.")
        if not ability_name:
            raise ValueError("Name should not be an empty string.")
        self.ability_name: str = ability_name

    def use_ability(self, ability_name: str) -> str:
        """
        Use a hero's ability.
        Return value: Message about ability use.
        :param ability_name: Название способности.
        Example:
        >>> hero = Dota2Hero("Invoker", "Sun Strike")
        >>> hero.use_ability(f"{hero.hero_name} casts {hero.ability_name} and summons a meteor from the heavens!")
        """
        ...

    def respawn(self, hero_name: str) -> str:
        """
        Resurrect the hero.
        Return value: Message about the resurrection of the hero.
        Example:
        >>> hero = Dota2Hero("Pudge", "Meat Hook")
        >>> hero.respawn(f"{hero.hero_name} is resurrected and ready to feast on the battlefield!")
        """
        ...


class ValorantAgent:
    def __init__(self, agent_name: str, ability_name: str):
        """
        Initialize a Valorant agent with name and ability.
        :param agent_name: Name of the agent.
        :param ability_name: Name of his ability.
        Example:
        >>> agent = ValorantAgent("ISO", "Contingency")
        """
        if not isinstance(agent_name, str):
            raise TypeError("Name should be of type str.")
        if not agent_name:
            raise ValueError("Name should not be an empty string.")
        self.agent_name: str = agent_name

        if not isinstance(ability_name, str):
            raise TypeError("Name should be of type str.")
        if not ability_name:
            raise ValueError("Name should not be an empty string.")
        self.ability_name: str = ability_name

    def use_ability(self, agent_name: str) -> str:
        """
        Use an agent's ability.
        Return value: Message about the use of the ability.
        :param agent_name: Agent name.
        Example:
        >>> agent = ValorantAgent("Jett", "Tailwind")
        >>> agent.use_ability(f"{agent.agent_name} activates {agent.ability_name} and dashes through the battlefield!")
        """
        ...

    def ultimate_ability(self, agent_name: str) -> str:
        """
        Use an agent's special ability (Ultimate).
        Return value: Message about using a special ability.
        Example:
        >>> agent = ValorantAgent("Phoenix", "Hot Hands")
        >>> agent.ultimate_ability(f"{agent.agent_name} unleashes the fire and rises from the ashes!")
        """
        ...


class CSGOWeapon:
    def __init__(self, weapon_name: str, number_of_bullets: int):
        """
        Initialize a CS:GO weapon.
        :param weapon_name: Name of the weapon.
        :param number_of_bullets: Number of bullets in weapon.
        Example:
        >>> weapon = CSGOWeapon("USP", 36)
        """
        if not isinstance(weapon_name, str):
            raise TypeError("Name should be of type str.")
        if not weapon_name:
            raise ValueError("Name should not be an empty string.")
        self.weapon_name: str = weapon_name

        if not isinstance(number_of_bullets, int):
            raise TypeError("Number of bullets should be of type int.")
        if number_of_bullets < 0:
            raise ValueError("Number of bullets should should be a non-negative number.")
        self.number_of_bullets: int = number_of_bullets

    def shoot(self, weapon_name: str) -> str:
        """
        Fire a weapon.
        Return value: Shot message.
        Example:
        >>> weapon = CSGOWeapon("AK-47", 90)
        >>> weapon.shoot(f"{weapon.weapon_name} fires and hits the target!")
        """
        ...

    def reload(self, weapon_name: str) -> str:
        """
        Reload your weapon.
        Return value: Recharge message.
        Example:
        >>> weapon = CSGOWeapon("AWP", 30)
        >>> weapon.reload(f"{weapon.weapon_name} reloads and is ready for action!")
        """
        ...


if __name__ == "__main__":
    doctest.testmod()  # Testing examples
