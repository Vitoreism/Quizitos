class Player:
    def __init__(self,  name: str, limit: int) -> None:
        self.name=name  
        self.hits: int = 0
        self.time_played: float = 0.0
        self.limit = limit


    def get_info(self) -> None:
        print(f'Name: {self.name}')
        print(f'Anserws: {self.hits}')
        print(f'Time played: {self.time_played}')
        print(f'Limit of answers: {self.limit}')
        print('-='*20)
    

    def increment_hits(self) -> None:
        self.hits += 1
    
    def get_hits(self) -> int:
        return self.hits

    def add_time_played(self, time_to_answer:float) -> None:
        self.time_played += time_to_answer