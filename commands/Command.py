import abc


class Command(abc.ABC):

    @classmethod
    def action(self):
        pass
