from services.demandService import demandService

class reportService:
    def __init__(self):
        self.demandService = demandService()

    def run(self):
        print('coletando dados das planilhas')
        demands = self.demandService.getData()