import random
import time

class Environment:
    def __init__(self):
        self.rooms = {
            'Sol': random.choice(['Clean', 'Dirty']),
            'Sağ': random.choice(['Clean', 'Dirty'])
        }
        print(f"Ev hazır! Başlangıç durumu: {self.rooms}")

    def get_room_status(self, room_name):
        return self.rooms[room_name]

    def set_room_status(self, room_name, status):
        self.rooms[room_name] = status

    def randomly_dirty_rooms(self):
        for room in self.rooms:
            if self.rooms[room] == 'Clean' and random.random() < 0.3:
                self.rooms[room] = 'Dirty'
                print(f">> Dış etken: '{room}' odası yeniden kirlendi!")


class SimpleReflexAgent:
    def __init__(self, start_location='Sol'):
        self.location = start_location
        print(f"Robot süpürge '{self.location}' odasında işe başladı. \n")

    def perceive(self, environment):
        return environment.get_room_status(self.location)

    def act(self, environment):
        current_room_status = self.perceive(environment)
        print(f"\nRobot şu anda '{self.location}' odasında. Durum: {current_room_status}")

        if current_room_status == 'Dirty':
            print("→ Oda kirli görünüyor, hemen temizleniyor...")
            environment.set_room_status(self.location, 'Clean')
            print(f"'{self.location}' odası temizlendi.")
        else:
            if self.location == 'Sol':
                print("Bu oda temiz. Sağ odaya geçiliyor...")
                self.location = 'Sağ'
            else:
                print("Bu oda temiz. Sola geçiliyor...")
                self.location = 'Sol'
       


def run_simulation(simulation_steps, delay_seconds):
    print("\nRobot Süpürge Simülasyonu Başlatılıyor...")
    env = Environment()
    robot = SimpleReflexAgent('Sol')

    time.sleep(1.5)

    for step in range(simulation_steps):
        print(f"[ Adım {step + 1} / {simulation_steps} ]")
        robot.act(env)
        env.randomly_dirty_rooms()

        print(f"Anlık oda durumu: {env.rooms}")
        print("=" * 50)

        time.sleep(delay_seconds)

    print("\nTüm adımlar tamamlandı.")
    print(f"Son oda durumu: {env.rooms}")
    print(f"Robotun son konumu: {robot.location}\n")


if __name__ == "__main__":
    SIMULATION_LIMIT = 25
    STEP_DELAY = 1.8
    run_simulation(SIMULATION_LIMIT, STEP_DELAY)
