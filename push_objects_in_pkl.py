import csv
import pickle
station={}
added_station=[]
train={}
added_train=[]
route=[]
train_list=[]
with open('Train_details_22122017.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    line_count = 0
    ind = 0
    im = 0
    i=0
    for row in csv_reader:
        if i == 0:
            i = i + 1
            continue
        print(row)
        t = row[0]
        bg = 0
        if t not in added_train:
            bg = 1
            train[t] = {'index': im, 'tname': row[1], 'scode': row[8], 'dcode': row[10]}
            im = im + 1
            added_train.append(t)
            route.append([(row[3], row[7], row[5], row[6])])
        else:
            route[train.get(t).get('index')].append((row[3], row[7], row[5], row[6]))
        s = row[3]
        if s not in added_station:
            station[s] = {'index': ind, 'station_name': row[4], 'imp_station': bg}
            added_station.append(s)
            ind = ind + 1
            train_list.append([t])
        else:
            train_list[station.get(s).get('index')].append(t)
        if bg == 1:
            station[s]['imp_station'] = 1
print(train)
print(station)
print(train_list)
print(route)

p1 = open('train.pkl', 'wb')
pickle.dump(train, p1, pickle.HIGHEST_PROTOCOL)
p2 = open('station.pkl', 'wb')
pickle.dump(station, p2, pickle.HIGHEST_PROTOCOL)
p3 = open('route.pkl', 'wb')
pickle.dump(route, p3, pickle.HIGHEST_PROTOCOL)
p4 = open('trainlist.pkl', 'wb')
pickle.dump(train_list, p4, pickle.HIGHEST_PROTOCOL)

p1.close()
p2.close()
p3.close()
p4.close()


