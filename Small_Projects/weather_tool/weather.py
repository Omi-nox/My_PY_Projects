import requests
from datetime import datetime
import time

api_code='4ac2ce3ec03d3e3a21248ff663f08bbe'
url='https://api.openweathermap.org/data/2.5/weather'


class MyCustomError(Exception): # for exception handling
    pass

def get_weather(city): # weather data get karne ke liye function
    params={'q':city,'appid':api_code,'units':'metric'}
    response=requests.get(url,params=params)
    data=response.json()
    return data

def tm(tm):
    val=tm
    time = datetime.fromtimestamp(tm).strftime('%H:%M')
    return time

def spd(spp): # speed ko km/h me convert karne ke liye function
    val=spp
    speed=val*3600/1000
    return speed

def country(tzone):
    val=tzone
    ctime=tzone/3600
    if ctime > 0:
        print(f"this city is forward than LONDON. (Offset: +{ctime} hours)")
    elif ctime < 0:
        print(f"this city is backward than LONDON. (Offset: {ctime} hours)")
    else:
        print("this city is in the same timezone as LONDON. (Offset: 0 hours)")
    

def show_detail(d):
    data=d
    print('-----------------------------------------')
    print(f"  -------------Weather detail-----------      \n")
    print(f"City: {data['name'] }\ncountry: {data['sys']['country']}\n")
    print('description of weather:',data['weather'][0]['description'],'\n')
    print(f"Temperature: {data['main']['temp']}°C\n")
    print(f"Weather: {data['weather'][0]['description']}\n")
    print(f"Humidity: {data['main']['humidity']}%\n")
    print(f'feels like: {data["main"]["feels_like"]}°C\n')
    print(f'Current time : {tm(data["dt"])}\n')
    print(f'wind speed: {spd(data["wind"]["speed"])} km/h\n')
    print(f'sunrise: {tm(data["sys"]["sunrise"])}\n')
    print(f'sunset: {tm(data["sys"]["sunset"])}\n')
    print(f'timezone: {data['timezone']} \n')
    country(data["timezone"])
    print('------------------------------')



def inputr():
    try:
        city=input('Enter the city name: ')
        print("DATA FETCHING.. Please Wait!!!!")
        time.sleep(2)
        d=get_weather(city)
        if d['cod'] != 200:
            raise MyCustomError("Something went wrong, you put INVALID CITY NAME _ WRITE PROPER CITY NAME")
        else:
            show_detail(d)
    except MyCustomError as e:
        print(f'from programmer: {e}') # Ab 'e' define ho chuka hai

    
    return city

print('loading...')
for i in range(40):
    print('-',end='')
    time.sleep(0.05)
print()

# inputr()
print('welcome to the weather tool!!!\n')
val=int(input('Enter 1 to check weather of another city or 2 to exit: '))
t=True
t1=False
while True: 
    if(val==1 and t):
        # print('if part')
        inputr()
        t=False
        # t1=True   
    elif (val==1 and not t):
        choice=input('Do you want to check another city weather? (yes/no): ')
        if choice.lower() == 'yes':
            inputr()
        elif choice.lower() == 'no':
            print('good to see you , Bye!!!')
            break
        else:
            print('Invalid input, please enter "yes" or "no".')
        # print('we are good')
       
    elif val==2:
        print('good to see you , Bye!!!')
        break
    else:
        print('Invalid input, please enter "yes" or "no".') 