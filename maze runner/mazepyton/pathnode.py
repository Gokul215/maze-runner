class pathnode:
    def __init__(self,row,col,steps,previous) -> None:
        self.row=row
        self.col=col 
        self.steps=steps
        self.previous=previous