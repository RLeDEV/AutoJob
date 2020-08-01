import pymongo
import yaml

class Driver:
    instance = None

    def __init__(self):
        if not self.instance:
            try:
                with open("./Driver/config.yml", "r") as yml:
                    cfg = yaml.load(yml, Loader=yaml.FullLoader)
                self.instance = pymongo.MongoClient("mongodb://"+cfg["mongodb"]["username"]+":"+cfg["mongodb"]["password"]+"@jobs-information-shard-00-00-akfpv.mongodb.net:27017,jobs-information-shard-00-01-akfpv.mongodb.net:27017,jobs-information-shard-00-02-akfpv.mongodb.net:27017/test?ssl=true&replicaSet=jobs-information-shard-0&authSource=admin&retryWrites=true&w=majority")
            except Exception as e:
                print("An error occured while tried to connect MongoDB")
                print(e)