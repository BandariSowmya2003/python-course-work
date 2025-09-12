#Encapsulation:
class Profile:
    def __init__(self,username,password):
        self._followers=set()
        self._following=set()
        self.post=[]
        self.username=username
        self.__password=password
        self.bio=''
        print(f'\n{self.username},Your account is created. Have fun with Instagram')


    def getPassword(self):
        return self.__password

    def setPassword(self,new_password):
        self.__password=new_password
        
    @property
    def NRfollowers(self):
        return self._followers

    @NRfollowers.setter
    def NRfollowers(self,req_uname):
        self._followers.add(req_uname)

    @property
    def NRfollowing(self):
        return self._following

    @NRfollowing.setter
    def NRfollowing(self,rai_uname):
        self._following.add(rai_uname)
    
Jyothsna= Profile('Jyothsna','Jyo@123')

print('Jyothsna Details'.center(40,'-'))

print('\nBefore Changing')
print(f'Before Username : {Jyothsna.username}')
print(f'Before Password : {Jyothsna.getPassword()}')
print(f'Before Bio : {Jyothsna.bio}')
print(f'Before Post : {Jyothsna.post}')
print(f'Before Followers : {Jyothsna.NRfollowers}')
print(f'Before Following : {Jyothsna.NRfollowing}')

print('\nAfter Changing')
Jyothsna.username='Jyosh'
print(f'After Username : {Jyothsna.username}')

Jyothsna.setPassword('Jyosh@123')
print(f'After Password : {Jyothsna.getPassword()}')

Jyothsna.bio='Celebrity'
print(f'After Bio : {Jyothsna.bio}')

Jyothsna.post.extend(['Post Graduate.png','Traveler.mp4','Foodie.jpg'])
print(f'After Post : {Jyothsna.post}')

Jyothsna.NRfollowers='Madhavi'
Jyothsna.NRfollowers='Kavitha'
Jyothsna.NRfollowers='Swathi'
Jyothsna.NRfollowers='Akhila'
Jyothsna.NRfollowers='Akshaya'

print(f'After Followers : {Jyothsna.NRfollowers}')

Jyothsna.NRfollowing='Sowmya'
Jyothsna.NRfollowing='Bharani'
Jyothsna.NRfollowing='Chandana'
Jyothsna.NRfollowing='Nagashilpa'
Jyothsna.NRfollowing='Yashwanthi'

print(f'After Following : {Jyothsna.NRfollowing}')

Kusuma= Profile('Kusuma','Kusuma@123')
print('Kusuma Details'.center(40,'-'))

print('\nBefore Changing')
print(f'Before Username : {Kusuma.username}')
print(f'Before Password : {Kusuma.getPassword()}')
print(f'Before Bio : {Kusuma.bio}')
print(f'Before Post : {Kusuma.post}')
print(f'Before Followers : {Kusuma.NRfollowers}')
print(f'Before Following : {Kusuma.NRfollowing}')

print('\nAfter Changing')
Kusuma.username='SakeKusuma'
print(f'After Username : {Kusuma.username}')

Kusuma.setPassword('Sake@123')
print(f'After Password : {Kusuma.getPassword()}')

Kusuma.bio='Software Engineer'
print(f'After Bio : {Kusuma.bio}')

Kusuma.post.extend(['Post Graduate.png','Traveler.mp4','Foodie.jpg'])
print(f'After Post : {Kusuma.post}')

Kusuma.NRfollowers='Nagashilpa'
Kusuma.NRfollowers='Bharani'
Kusuma.NRfollowers='Sowmya'
Kusuma.NRfollowers='Yashwanthi'
Kusuma.NRfollowers='Chandana'

print(f'After Followers : {Kusuma.NRfollowers}')

Kusuma.NRfollowing='Swathi' 
Kusuma.NRfollowing='Akshaya'  
Kusuma.NRfollowing='Madhavi'   
Kusuma.NRfollowing='Akhila'  
Kusuma.NRfollowing='Kavitha'  

print(f'After Following : {Kusuma.NRfollowing}')

#Output:

'''
Jyothsna,Your account is created. Have fun with Instagram
------------Jyothsna Details------------

Before Changing
Before Username : Jyothsna
Before Password : Jyo@123
Before Bio : 
Before Post : []
Before Followers : set()
Before Following : set()

After Changing
After Username : Jyosh
After Password : Jyosh@123
After Bio : Celebrity
After Post : ['Post Graduate.png', 'Traveler.mp4', 'Foodie.jpg']
After Followers : {'Akhila', 'Akshaya', 'Madhavi', 'Kavitha', 'Swathi'}
After Following : {'Nagashilpa', 'Sowmya', 'Bharani', 'Chandana', 'Yashwanthi'}

Kusuma,Your account is created. Have fun with Instagram
-------------Kusuma Details-------------

Before Changing
Before Username : Kusuma
Before Password : Kusuma@123
Before Bio : 
Before Post : []
Before Followers : set()
Before Following : set()

After Changing
After Username : SakeKusuma
After Password : Sake@123
After Bio : Software Engineer
After Post : ['Post Graduate.png', 'Traveler.mp4', 'Foodie.jpg']
After Followers : {'Nagashilpa', 'Sowmya', 'Bharani', 'Chandana', 'Yashwanthi'}
After Following : {'Akhila', 'Akshaya', 'Madhavi', 'Kavitha', 'Swathi'}

'''
