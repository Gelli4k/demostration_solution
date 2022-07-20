import pytest

from service.director import DirectorService


class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_service = DirectorService(dao=director_dao)

    def test_get_one(self):
        director = self.director_service.get_one(1)
        assert director is not None

    def test_get_all(self):
        directors = self.director_service.get_all()
        assert len(directors) > 0

    def test_create(self):
        director_d = {'name': "New Name"}
        new_director = self.director_service.create(director_d)
        assert new_director.id is not None

    def test_update(self):
        director = self.director_service.update(1)

    def test_delete(self):
        res = self.director_service.delete(2)
        assert res is None
