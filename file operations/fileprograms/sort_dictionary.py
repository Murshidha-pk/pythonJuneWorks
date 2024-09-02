placements={"django":32,"python":42,"teseter":38,"mearn":45}

def get_value(key):

    return placements.get(key)

srt=sorted(placements,key=get_value,reverse=True)
print(srt)