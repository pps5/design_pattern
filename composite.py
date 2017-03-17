# coding: utf-8

class Task(object):
    """A process for making cake."""

    def __init__(self, name):
        self.name = name
        self.parent = None

    def get_time_required(self):
        return .0


class CompositeTask(Task):
    """A process contains sub processes."""

    def __init__(self, name):
        Task.__init__(self, name)
        self.sub_tasks = []

    def get_time_required(self):
        return sum(t.get_time_required() for t in self.sub_tasks)

    def add_sub_task(self, task):
        self.sub_tasks.append(task)
        task.parent = self

    def remove_sub_task(self, task):
        self.sub_tasks.remove(task)

    def __getitem__(self, i):
        return self.sub_tasks[i]


class MakeBatterTask(CompositeTask):
    """A task to make batter."""

    def __init__(self):
        CompositeTask.__init__(self, 'make a dough')
        self.add_sub_task(AddDryIngredientsTask())
        # self.add_sub_task(AddLiquidesTask())
        # self.add_sub_task(MixTask())


class AddDryIngredientsTask(CompositeTask):
    """A task to add dry ingredients."""

    def __init__(self):
        CompositeTask.__init__(self, 'add dry ingredients')

    def get_time_required(self):
        return 1


class MakeCakeTask(CompositeTask):
    """A task to make cake."""

    def __init__(self):
        CompositeTask.__init__(self, 'make a cake')
        self.add_sub_task(MakeBatterTask())
        # self.add_sub_task(FillPanTask())
        # self.add_sub_task(BakeTask())
        # self.add_sub_task(FrostTask())
        # self.add_sub_task(LickSpoonTask())

if __name__ == '__main__':
    make_cake = MakeCakeTask()
    print(make_cake.get_time_required())  # output: 1
