import requests
import time
def test_connectivity(url , start_time):
    """
    Test connectivity to the URL
    """
    response = requests.get(url)
    if response.status_code == 200:
        end_time = time.time()
        times = end_time - start_time
        print(f"Connectivity to " + url + " is OK" + " time to live" , int(times) , "seconds" )
        return True
    else:
        return False


if __name__ == '__main__':
    start_time = time.time()
    url = input("write your url to test: ")
    print(test_connectivity(url , start_time))