class demandEntity:
    def __init__(self,markets,releaseDate,project,key,sku,description,brand,subcategory,category,status,country,countryAnswer,similarKey,similarDescription,similarBrand,similarSubcategory,similarCategory,premiseBrazil,projectType):
        self.markets = markets
        self.releaseDate = releaseDate
        self.project = project
        self.key = key
        self.sku = sku
        self.description = description
        self.brand = brand
        self.subcategory = subcategory
        self.category = category
        self.status = status
        self.country = country
        self.countryAnswer = countryAnswer
        self.similarKey = similarKey
        self.similarDescription = similarDescription
        self.similarBrand = similarBrand
        self.similarSubcategory = similarSubcategory
        self.similarCategory = similarCategory
        self.premiseBrazil = premiseBrazil
        self.projectType = projectType

    def __str__(self) -> str:
        return f'Markets: {self.markets}, ReleaseDate: {self.releaseDate}, Project: {self.project}, Key: {self.key}, Sku: {self.sku}'

    def __repr__(self) -> str:
        return str(self)