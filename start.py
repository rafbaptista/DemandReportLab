from services.reportService import reportService

class start:
    def __init__(self):
        print('Iniciando...')
        self.reportService = reportService()
        self.reportService.run()

start()