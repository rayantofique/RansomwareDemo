from flask import json


#key is email
def saveKey(request):
	jsonDict = convertToDict(request)
	f = open("privatekey-" + jsonDict['email'] + ".txt", "w")
	f.write(jsonDict['privatekey'])
	f.close()


def fetchKey(request):
	jsonDict = convertToDict(request)
	f = open("privatekey-" + jsonDict['email'] + ".txt", "r")
	privateKey = f.read().replace('\n', '')
	f.close()
	return privateKey


def convertToDict(request):
	return json.loads(json.dumps(request))

def main():
	print("runs")

if __name__ == '__main__':
	main()