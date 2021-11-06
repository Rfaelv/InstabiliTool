class Path:
    def __init__(self, path):
        self.rootPath = path + '/data'
        self.runLocale = self.rootPath + '/ansys'
        self.model =  self.rootPath + '/model.json'
        self.settings = self.rootPath + '/settings.json'
        self.images = self.rootPath + '/images'