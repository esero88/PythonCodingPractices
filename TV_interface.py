import random
import time

class Remote():

    def __init__(self, tv_status = "Off", tv_volume = 0, channel_list =None, channel ="TRT"):
        if channel_list is None:
            channel_list = ["TRT"]
        print("Remote control is creating...")

        self.tv_volume =  tv_volume

        self.tv_status = tv_status

        self.channel_list = channel_list

        self.channel = channel
    def volume_down_up(self):

        while True:
            character = input("For decrease volume '<' increase volume '>' If it is ok press 'q' ")

            if (character == "<"):
                if (self.tv_volume != 0):
                    self.tv_volume -= 1
                    print("Volume:",self.tv_volume)
            elif (character == ">"):
                if (self.tv_volume != 32):
                    self.tv_volume += 1
                    print("Volume:",self.tv_volume)
            else:
                print("Volume is updated:",self.tv_volume)
                break
    def tv_off(self):
        if (self.tv_status == "Off"):
            print("TV is already off.")
        else:
            print("TV is turning off...")
            self.tv_status = "Off"
    def tv_on(self):
        if (self.tv_status == "On"):
            print("TV is already on.")
        else:
            print("TV is turning on...")
            self.tv_status = "On"
    def __str__(self):
        return "Tv Status : {}\nVolume: {}\nChannels: {}\nCurrent Channel: {}\n".format(self.tv_status,self.tv_volume,self.channel_list,self.channel)
    def __len__(self):
        return  len(self.channel_list)

    def random_channel(self):
        randomly = random.randint(0,len(self.channel_list)-1)

        self.channel = self.channel_list[randomly]

        print("Current Channel:", self.channel)
    def add_channel(self,channel):
        print("Channel is adding...")
        time.sleep(1)
        self.channel_list.append(channel)
        print("Channel is added ",channel)
    def change_channel(self):
        new_channel = input("Please write that channel you want to watch: ")
        if new_channel in channels:
            print("Channel is changing...")
            self.channel = new_channel
        else:
            print("Channel that you entered is not in channel list.")
        time.sleep(1)


remote = Remote()
print("""*******************

TV Application

Operations ;

1. TV On

2. TV Off

3. Informations About TV

4. Amount of Channels

5. Add Channel

6. Random Channel

7. Volume Down or Volume Up

8. Change Channel

Press 'q' for exit.
*******************""")

while True:

    operation = input("Select operation:")
    if (operation == "q"):
        print("Exiting from TV application...")
        break
    if (operation == "1"):
        remote.tv_on()
    elif (operation == "2"):
        remote.tv_off()
    elif (operation == "3"):
        print(remote)
    elif (operation == "4"):
        print("Amount of Channels: ",len(remote))
    elif (operation == "5"):
        channels = input("Please enter the channels that you want add by seperating them with  ',': ")
        channels_will_be_added = channels.split(",")
        for i in channels_will_be_added:
            remote.add_channel(i)
        print("Channel list is updated successfully.")
    elif (operation == "6"):
        remote.random_channel()
    elif (operation == "7"):
        remote.volume_down_up()
    elif (operation == "8"):
        remote.change_channel()
    else:
        print("Invalid Action...")
