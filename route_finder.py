import pickle
#getting all train details saved in pickle file

p1=open('train.pkl','rb')
train=pickle.load(p1)
p2=open('station.pkl','rb')
station=pickle.load(p2)
p3=open('route.pkl','rb')
route=pickle.load(p3)
p4=open('trainlist.pkl','rb')
train_list=pickle.load(p4)


k=list(station.keys())
sn=[]
for i in k:
    sn.append(station[i].get('station_name'))

def find_all_trains():
    print("Enter the station")
    s = input()
    i = station.get(s).get('index')
    for k in range(len(train_list[i])):
        print(train.get(train_list[i][k]).get('tname'))



def directroute(source,dest):
    selected=[]
    sind = station.get(source).get('index')
    trains_passes = train_list[sind]
    for eachtrain in trains_passes:
        dist1=0
        dist2=0
        tind = train.get(eachtrain).get('index')
        gotroute = route[tind]
        i=0
        while i<len(gotroute):
            if gotroute[i][0]==source:
               dist1=int(gotroute[i][1])
               break
            else:
                i=i+1
            i=i+1
        while i<len(gotroute):
             if gotroute[i][0] == dest:
                 dist2=int(gotroute[i][1])
                 selected.append((train.get(eachtrain).get('tname'), gotroute[i][2], dist2 - dist1))
                 break
             else:
                 i=i+1
    return selected

def altroute(source,dest):
        sourceset = set()
        destset = set()
        source_end_station = set()
        dest_end_station = set()
        trains_from_source= train_list[station.get(source).get('index')]
        trains_from_destination=train_list[station.get(dest).get('index')]
        for eachtrain in trains_from_source:
            station_covered=route[train.get(eachtrain).get('index')]
            source_end_station.add(station_covered[-1][0])
            for stn in station_covered:
                if station.get(stn[0]).get('imp_station')==1:
                    sourceset.add(stn[0])



        for eachtrain in trains_from_destination:
            station_covered=route[train.get(eachtrain).get('index')]
            dest_end_station.add(station_covered[-1][0])
            for stn in station_covered:
                if station.get(stn[0]).get('imp_station')==1:
                    destset.add(stn[0])


        intermediate=source_end_station.intersection(destset).intersection(dest_end_station.intersection(sourceset))
        routes=[]
        accepted_route=[]
        dst = []
        for inm in intermediate:
            first_half=directroute(source,inm)
            second_half=directroute(inm,dest)
            dst1=[]
            dst2=[]
            for tr in first_half:
                dst1.append(tr[2])
            for tr in second_half:
                dst2.append(tr[2])
            try:
                distancebws=min(dst1)+min(dst2)
                routes.append((source,inm,dest,distancebws))
                dst.append(distancebws)
            except:
                continue
        mindist=min(dst)
        for rte in routes:
            if rte[3]<=mindist+500:
                accepted_route.append(rte)
        return accepted_route

if __name__=="__main__":

print("Enter source station")
source = input()
print("Enter destination station")
dest = input()
print('Direct route:')
k=directroute(source,dest)
print(k)
print('\n\n')
print('Alternate route:')
accepted=altroute(source,dest)
for r in accepted:
    print(r[0],'->',r[1],'->',r[2],'distance is',r[3])
