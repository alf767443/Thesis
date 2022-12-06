
import requests
import pandas
import json
import ast

class readURL:
    def __init__(self, url: str):
        self.url = url
        
    def read(self) -> requests:
        payload = ""
        headers = {}
        response = requests.request("GET", self.url, headers=headers, data=payload)
        return response
    
    def json(self) -> json:
        return self.read().text

    def only_dict(d):
        return ast.literal_eval(d)

    def list_of_dicts(ld):
        return dict([(list(d.values())[1], list(d.values())[0]) for d in ast.literal_eval(ld)])

    def expand(self, data:pandas.DataFrame, withId:bool = True) -> pandas.DataFrame:
        for x in data.columns:
            if data[x].dtypes == object and data[x].name != '_id' :
                if withId:
                    newColumn = pandas.json_normalize(data[x].apply(ast.literal_eval).tolist()).add_prefix(str(data[x].name) + '.')
                else:
                    newColumn = pandas.json_normalize(data[x].apply(ast.literal_eval).tolist()).drop(columns=['_id']).add_prefix(str(data[x].name) + '.')
                data = data.drop(columns=data[x].name)
                data = data.join([newColumn])
        return data

    def dataFrame(self, withId:bool = True, columnExpand:bool = True) -> pandas.DataFrame:
        data = pandas.read_json(self.json())
        if not withId:
            data = data.drop(columns=['_id'])
        if columnExpand:
            data = self.expand(data=data, withId=withId)
            return data
        else:
            return data
    

class readJSON:
    def __init__(self, json: json):
        self.json = json

    def only_dict(d):
        return ast.literal_eval(d)

    def list_of_dicts(ld):
        return dict([(list(d.values())[1], list(d.values())[0]) for d in ast.literal_eval(ld)])

    def expand(self, data:pandas.DataFrame, withId:bool = True) -> pandas.DataFrame:
        for x in data.columns:
            if data[x].dtypes == object and data[x].name != '_id' :
                if withId:
                    newColumn = pandas.json_normalize(data[x].apply(ast.literal_eval).tolist()).add_prefix(str(data[x].name) + '.')
                else:
                    newColumn = pandas.json_normalize(data[x].apply(ast.literal_eval).tolist()).drop(columns=['_id']).add_prefix(str(data[x].name) + '.')
                data = data.drop(columns=data[x].name)
                data = data.join([newColumn])
        return data

    def dataFrame(self, withId:bool = True, columnExpand:bool = True) -> pandas.DataFrame:
        data = pandas.read_json(self.json)
        if not withId:
            data = data.drop(columns=['_id'])
        if columnExpand:
            data = self.expand(data=data, withId=withId)
        self.json = data.to_json()
        return data
    
    
        #full = readJSON(json=json.dumps(battery_serializer.data)).dataFrame().to_json()
        #print(json.loads(full))        
        #print(BatterySerializer(json.loads(full),many=True))
        #battery_serializer=BatterySerializer(json.loads(full),many=True))
        #print(json.load(readJSON(json=json.dumps(battery_serializer.data)).dataFrame().to_json()))
        #print(JSONParser().parse(battery_serializer.data))
        #return JsonResponse(readJSON(JSONParser().parse(battery_serializer.data)).dataFrame().to_json(), safe=False)