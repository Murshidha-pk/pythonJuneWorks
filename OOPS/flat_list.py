

def flat_list(*args):  #10,20,[100,200],[1000,[2000,3000]])(

    flat=[]

    for arg in args:

        if isinstance(arg,list):

            flat.extend(flat_list(*args))

        else:

            flat.append(arg)

    return flat

print(flat_list((10,20,[100,200],[1000,[2000,3000]])))