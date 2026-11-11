from homework8.task2.Bachelor import Bachelor
from homework8.task2.Undergraduate import Undergraduate


class TestUndergraduate:
    def test_is_bachelor_subclass(self) -> None:
        assert issubclass(Undergraduate, Bachelor)

    def test_constructor_stores_inherited_fields(self) -> None:
        undergrad = Undergraduate("Petr", "Petrov", "FMI-2", 4.5, "research topic")
        assert undergrad._first_name == "Petr"
        assert undergrad._last_name == "Petrov"
        assert undergrad._group == "FMI-2"
        assert undergrad._average_mark == 4.5

    def test_constructor_stores_research_work(self) -> None:
        undergrad = Undergraduate("Petr", "Petrov", "FMI-2", 4.5, "research topic")
        assert undergrad._Undergraduate__research_work == "research topic"

    def test_perfect_mark_gets_highest_scholarship(self) -> None:
        undergrad = Undergraduate("Petr", "Petrov", "FMI-2", 5, "research topic")
        assert undergrad.get_scholarship() == 15000

    def test_mark_above_three_gets_base_scholarship(self) -> None:
        undergrad = Undergraduate("Petr", "Petrov", "FMI-2", 4, "research topic")
        assert undergrad.get_scholarship() == 7500

    def test_mark_three_gets_no_scholarship(self) -> None:
        undergrad = Undergraduate("Petr", "Petrov", "FMI-2", 3, "research topic")
        assert undergrad.get_scholarship() == 0

    def test_low_mark_gets_no_scholarship(self) -> None:
        undergrad = Undergraduate("Petr", "Petrov", "FMI-2", 2, "research topic")
        assert undergrad.get_scholarship() == 0
