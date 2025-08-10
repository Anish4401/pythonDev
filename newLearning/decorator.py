#Decorator  so it is basically work as toll-plaza where we need to pass through it if called 
import time
# def func(func2):
#     def func1(*args,**kwargs): #here we are passing the argument more than one of type
#         start_time=time.time()
#         res=func2(*args,**kwargs)
#         end_time=time.time()
#         print(f"  {func2.__name__}{start_time} and the {end_time} is perfect")    #formatting string
#         return res
#     return func1
# @func    #it is a decorator that the below method need to pass to it
# def time_func(n):
#     time.sleep(n)
#     return f"slept for {n} sec"
# print(time_func(2))
    
        
# def debug(func):
#     def func2(*args,**kwargs):
#         args_val=(",".join(str(arg)for (arg) in args))
#         kwargs_val=(",".join(f"{k}={v}" for k ,v in kwargs.items()))
#         print(f"{args_val} is the value is going and with {kwargs_val} also")
#         return func(*args,**kwargs)
#     return func2
# @debug
# def hii(name,place):
#     print(f"{name} welcome {place}")
# hii("Anish","asansol")
# hii(name="Baap" ,place="Of HIT")


#Cacheing the values which are called just before 
def cache(func):
    cache_val={}
    print(cache_val)
    def func3(*args):
        if args in cache_val:   #here we are checking whether the value exist if their can show the cache val or if not then after sleep over generate the new one
            return cache_val[args]
        res= func(*args)
        cache_val[args]=res
        return res
        
    return func3
@cache
def sleep(a,b):
    time.sleep(4)
    return a+b
print(sleep(4,3))
print(sleep(4,1))


        
