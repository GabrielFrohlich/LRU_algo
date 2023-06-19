import random

cache_size = 4
cache = []

def savePage(name, value, time):
    page =     {
        "page": name,
        "last_used": time,
        "value": value
    }

    if(len(cache) >= cache_size):
        least_used_min = 1000
        least_used_page_index = 0
        i = 0
        for pages in cache:
            if(pages['last_used'] < least_used_min):
                least_used_min = pages['last_used']
                least_used_page_index = i
            
            i+=1
        
        del cache[least_used_page_index]
        cache.append(page)
    else:
        cache.append(page)
    
    return page

missed = 0
hit = 0

def getPage(name, time):
    i = 0
    for page in cache:
        if(page['page'] == name):
            #update on cache last used of this page
            cache[i]['last_used'] = time
            global hit
            hit += 1
            return cache[i]

        
        i+=1
    global missed
    missed +=1
    return savePage(name, random.randrange(0,100), time)

#clock cycle
for i in range(0,100):
    #randomly generate page name between A and F
    page_name = chr(random.randrange(65,70))

    #get page from cache
    page = getPage(page_name, i)
    
    if(i == 3 or i==7):
        print(cache)

# getPage("A", 0)
# getPage("B", 1)
# getPage("C", 2)
# getPage("D", 3)
# print("Instante de tempo 3: ")
# print(cache)

# getPage("A", 4)
# print("\nInstante de tempo 4: ")
# print(cache)

# getPage("C", 5)
# print("\nInstante de tempo 5: ")
# print(cache)

# getPage("E", 6)
# print("\nInstante de tempo 6: ")
# print(cache)

# getPage("F", 7)
# print("\nInstante de tempo 7: ")
# print(cache)

print("Missed: {}\nHits: {}".format(missed, hit))
