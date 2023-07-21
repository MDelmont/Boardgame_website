from data.database.tables.table import Tables

def test_make_condition():

    test1 = {

        'Test1':['AND','=','Test1',"TEXT"],
        'Test2':['AND','=',2,'INT'],
        'Test3':['OR','=','Test3','TEXT'],
        'Test4':['OR','=',4,'INT'],
        
        }
    print(test1)
    print(Tables('app','app',[]).make_condition_columns(test1))
    test2 = {

        'Test1':['AND','IN',['1','2','3','4','5'],"TEXT"],
        'Test2':['AND','IN',[1,2,3,4,5],"INT"],
    
        
        }
    print(test2)
    print(Tables('app','app',[]).make_condition_columns(test2))
    test3 = {

        'Test1':['AND','><',[1,2],"INT"],

        'Test2':['OR','<>',[3,2],'INT'],
   
        
        }
    print(test3)
    print(Tables('app','app',[]).make_condition_columns(test3))
test_make_condition()