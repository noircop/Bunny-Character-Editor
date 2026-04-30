class FlowController(object):

    def __init__(self, steps_list):
        self.steps_list = steps_list
        self.current_step = 0

        self.started = False

    # Жизненый Цикл
    def start(self):
        self.started = True
        self.exited = False
        self.current_step = 0

    def reset(self):
        self.current_step = 0
        self.started = False

    # Состояние
    @property
    def step_count(self):
        return len(self.steps_list)

    @property
    def current(self):
        if self.step_count == 0:
            return None
        return self.steps_list[self.current_step]

    @property
    def is_first(self):
        return self.current_step <= 0

    @property
    def is_last(self):
        return self.current_step >= self.step_count - 1

    # Навигация
    def next(self):
        if not self.is_last:
            self.current_step += 1

    def prev(self):
        if not self.is_first:
            self.current_step -= 1

    def go_to(self, index):
        if 0 <= index < self.step_count:
            self.current_step = index

    # Хэлперы для UI
    def can_next(self):
        return not self.is_last

    def can_prev(self):
        return not self.is_first
