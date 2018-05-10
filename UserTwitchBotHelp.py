from ChatBotCommands import *
from Asynctesting import *
import asynctwitch

if __name__ == '__main__':
    @command(name='hi')
    def test(user):
        send_message(f'hello @{user}! How are you?')

    @command(name='pgame')
    def test1(user, *args):
        send_message(f'@{user} are you ready to play?')
        time.sleep(1)
        send_message(f'@{user}')
        global answerq
        answerq = 'a'
        question1 = [
            {'question': 'Who has more followers? Answer either A,B,C or D.', 'a': 'A.) Ninja', 'b': 'B.) Lirik',
             'c': 'C.) Lirikk', 'd': 'D.) summit1g', 'answer': 'Your answer:'}]
        question(**question1[0])
        global youranswer
    @command(name='a')
    def answercorrect(user):
        send_message(f'@{user} Correct!')

    @command(name='b')
    def answerwrong(user):
        send_message(f'@{user} Incorrect!')

    @command(name='b')
    def answerwrong(user):
        send_message(f'@{user} Incorrect!')

    @command(name='c')
    def answerwrong(user):
        send_message(f'@{user} Incorrect!')

    @command(name='d')
    def answerwrong(user):
        send_message(f'@{user} Incorrect!')

    @command(name='help')
    def help(user):
        send_message(f'@{user} I have many commands:')
        time.sleep(0.5)
        send_message(f'@{user} To get a list of my commands say "commands" at the start of your text')

    @command(name='mods')
    def mods(user):
        send_message(f'@{user} The mods I have are:')
        time.sleep(0.3)
        send_message(f'andrewgamer1937, comsciprogramming, gabelover23, gconnor911, hexploitation, malvious_mh, nex_infinite, nezamizero, nightbot, streamelements, sudokid, userman2, wizebot, yojimbozz')

    @command(name='commands')
    def rewards(user):
        send_message(f'My commands are:')
        time.sleep(0.3)
        send_message(f'These: !mlg !points !leroy !shots !tadah !challenge !hiest !boss !ffa !yii !help !mods !pgame !hi !stats !uptime !emote !userman !add !credits !follow !math !water !whoisthat !schedule !mouse 1keyboard !monitor !webcam !specs !sup !bye !cya !mistake !distracted')

    @command(name='emote')
    def emote(user):
        send_message(f'@{user} My emote is:')
        time.sleep(0.5)
        send_message(f'nexinf1niteCTRLZ')

    @command(name='userman')
    def userman(user):
        send_message(f'Userman? More like HelperMan. <3 🐍 🐍 🐍 🐍 🐍')

    @command(name='add')
    def addcommand(user):
        send_message(f'@{user} Tell me what to add and we will add it <3')

    @command(name='credits')
    def credits(user):
        send_message(f'@{user} The people who built this bot are:')
        time.sleep(0.3)
        send_message(f'@Userman2 and @nex_infinite, also The chat helped a lot; thanks @everyone')

    @command(name='follow')
    def follow(user):
        send_message(f'@{user} to follow my follow this link:')
        time.sleep(0.3)
        send_message(f'https://www.twitch.tv/nex_infinite and click follow above the screen')

    @command(name='math')
    def maths(user):
        send_message(f'@{user} Here we call math maths #bestcommandever')

    @command(name='water')
    def drinkwater(user):
        send_message(f'@{user} remind nex to drink water! Even though I probably have squash or coffee')

    @command(name='whoisthat')
    def whoisthat(user):
        send_message(f'@{user} The person you can here in the background is probably my twin, ignore him if u can <3')

    @command(name='schedule')
    def schedule(user):
        send_message(f'@{user} my schedule is not very good, on the weekends i try to stream everyday and on the weekdays i stream from about 5 till 8 gmt.')

    @command(name='mouse')
    def mymouse(user):
        send_message(f'@{user} The mouse I use is Coolmaster masterkeys Lite L (Mouse)')

    @command(name='keyboard')
    def mykeyboard(user):
        send_message(f'@{user} The keyboard I use is Coolmaster masterkeys lite l (keybaord)')

    @command(name='monitor')
    def mymonitor(user):
        send_message(f'@{user} I have two monitors:')
        time.sleep(0.3)
        send_message(f'My main monitor is a Logik monitor (https://www.currys.co.uk/gbuk/tv-and-home-entertainment/televisions/televisions/logik-l22fe14-22-led-tv-21940504-pdt.html)')
        time.sleep(0.3)
        send_message(f'My second monitor is a viewsonic square monitor (I do not have a link too it)')

    @command(name='webcam')
    def mywebcam(user):
        send_message(f'@{user} The webcam I use is a logitech webcam (couldnt find the label for it)')

    @command(name='specs')
    def mypcspecs(user):
        send_message(f'@{user} My pc specs are as follows:')
        time.sleep(0.3)
        send_message(f'Gpu: Geforce GTX 1050 TI, Cpu: AMD fx 8300 black edition, Motherboard: Gigabyte d3ysp, Hard drive: 250gb ssd and 250gb hdd, Ram: 8gb Baliistic ram')

    @command(name='sup')
    def sup(user):
        send_message(f'@{user} sup')

    @command(name='bye')
    def bye(user):
        send_message(f'@{user} Goodbye, have a good day/night nexinf1niteCTRLZ')

    @command(name='cya')
    def cya(user):
        send_message(f'@{user} Goodbye, have a good day/night nexinf1niteCTRLZ')

    @command(name='mistake')
    def mistake(user):
        send_message(f'@{user} What mistake? nexinf1niteCTRLZ')

    @command(name='distracted')
    def distracted(user):
        send_message(f'@{user} Ok, I may get distracted but it happens <3 Kappa')



    print("What channel would you like to connect to?")
    channel_login_input = input()
    if channel_login_input == '1':
        channel_login_input_login = 'nex_infinite'
    else:
        channel_login_input_login = channel_login_input
    login(channel_login=channel_login_input_login)
    print('logged into chat....')

    for msg in iter_message_loop():
        # see if it is a command
        if is_cmd(msg):
            handle_command(msg)
            continue
        else:
            print(format_message(msg))