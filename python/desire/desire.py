import yaml
f = open('desire.yaml')
desire_dictionary = yaml.load(f)
f.close()
with open("desire.yaml", 'r') as stream:
    print(yaml.load(stream))

print(desire_dictionary['infrastructure']['host'][1])
