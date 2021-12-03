from Fetch_Data import Fetch_Data
from sklearn import tree , preprocessing

def learning_price(data):
    cars_data = Fetch_Data()

    names = []
    model = []
    karkard = []

    for item in cars_data:
        names.append((item[0]).lower())
        model.append(item[1])
        karkard.append(item[2])

    le = preprocessing.LabelEncoder()
    le.fit(names)
    s = le.fit_transform(names)

    new_data = []
    for i in range(len(cars_data)):
        new_data.append([s[i], int(model[i]), int(karkard[i])])
  
    
    x = new_data
    y =[]

    for item in cars_data:
        y.append(item[3])
    

    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(x,y)

    data_user = [data[0].lower(),data[1] , data[2]]
    for name in names:
        if data_user[0] == name:
            ind = names.index(name)
            data_user[0] = s[ind]
        
    prediction = clf.predict([data_user])

    return int(prediction)

