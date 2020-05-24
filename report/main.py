from .generator import *
import os
import sys

os.path.dirname(sys.executable)


def main():
    create_report(
        "C:/Alex/ReabilitationSystem/Report/simple_table.pdf",
        _rollleft=90,
        _rollright=89,
        _yawleft=89,
        _yawright=88,
        _pitchdown=75,
        _pitchup=90,
        _name="Богусевич Олексій",
        _age="20",
        _card="748394",
        _height="178",
        _weight="66",
        _number="0951360156",
        _room="1",
    )


if __name__ == "__main__":
    main()
