import random, string, itertools, time, pyzipper
from tqdm import tqdm

alphabet = string.printable[:95]
charlength = 3
passw = 'slm'
startTime = int(time.time())
numpw = 0

def test_zip_password(zip_path, password):
    try:
        with pyzipper.AESZipFile(zip_path) as zf:
            # Attempt to read the first file in the archive
            zf.pwd = password.encode()
            zf.read(zf.namelist()[0])
            print("Password is correct!")
            return password
    except RuntimeError as e:
        if 'encrypted' in str(e):
            print("The file is password protected.")
    except Exception as e:
        print("An error occurred:", e)



def bruteforce():
    
    global numpw
    charList = [[x for x in alphabet]] * charlength
    args = [char for char in charList]
    for combination in itertools.product(*args):
        numpw += 1
        test = test_zip_password('ziptest.zip',''.join(combination))
        if test == ''.join(combination):
            return combination

    
if __name__=="__main__":
    result = bruteforce()
    endTime = int(time.time())
    print(f"bruteforced password {''.jon(result)} in {endTime - startTime} seconds, with a total of {numpw} attempts" )