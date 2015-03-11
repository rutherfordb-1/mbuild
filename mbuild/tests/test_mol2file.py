import mbuild as mb
from mbuild.components.small_groups.ch3 import CH3
from mbuild.testing.tools import get_fn
from mbuild.tests.base_test import BaseTest


class TestMol2(BaseTest):

    def test_load_and_create(self):
        methyl = mb.load(get_fn('methyl.mol2'))

    def test_load_into(self):
        methyl = CH3()
        methyl.update_coordinates(get_fn('methyl.mol2'))

    def test_save(self):
        methyl = mb.load(get_fn('methyl.mol2'))
        methyl.save(filename='methyl_out.mol2')
