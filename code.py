import json

if __name__ == '__main__':
    try:
        with open('myInput.json', 'r') as f:
            data = json.loads(f.read())

        output = ','.join([*data[0]])
        for obj in data:
            output += f'\n{obj["Name"]},{obj["BirthYear"]},{obj["Team"]}'

        with open('myOutput.csv', 'w') as f:
            f.write(output)
    except Exception as ex:
        print(f'Error: {str(ex)}')