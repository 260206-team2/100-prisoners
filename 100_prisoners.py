import random

def play_random(n):
    pardoned = 0
    in_drawer = list(range(100))
    sampler = list(range(100))    

    for _round in range(n):
        random.shuffle(in_drawer) 
        all_found = True 

        for prisoner in range(100):
            found = False
            for reveal in random.sample(sampler, 50):
                if in_drawer[reveal] == prisoner:
                    found = True
                    break

            if not found:
                all_found = False
                break

        
        if all_found:
            pardoned += 1

    return pardoned / n * 100
