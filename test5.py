def clear_text(text, excepts):
    d = ""
    for i in text:
        i = i.replace("1", "")
        i = i.replace("2", "")
        i = i.replace("3", "")
        i = i.replace("4", "")
        i = i.replace("5", "")
        i = i.replace("6", "")
        i = i.replace("7", "")
        i = i.replace("8", "")
        i = i.replace("9", "")
        i = i.replace("0", "")
        i = i.replace("'", "")
        i = i.replace(";", "")
        i = i.replace("-", "")
        i = i.replace("!", "")
        i = i.replace("@", "")
        i = i.replace("#", "")
        i = i.replace("%", "")
        i = i.replace("^", "")
        i = i.replace("&", "")
        i = i.replace("(", "")
        i = i.replace(")", "")
        i = i.replace("*", "")
        i = i.replace("_", "")
        i = i.replace("}", "")
        i = i.replace("{", "")
        i = i.replace("[", "")
        i = i.replace("]", "")
        i = i.replace("/", "")
        i = i.replace("?", "")
        i = i.replace("©", "")
        if excepts!=" ":
            i = i.replace(" ", "")
        i = i.replace("|", "")
        i = i.replace(".", "")
        i = i.replace(",", "")
        i = i.replace("»", "")
        i = i.replace("«", "")
        i = i.replace("\n", "")
        i = i.replace("\t", "")
        i = i.replace("~", "")
        i = i.replace("—", "")
        i = i.replace("”", "")
        i = i.replace("=", "")
        i = i.replace("<", "")
        i = i.replace(">", "")
        i = i.replace('"', "")
        i = i.replace('+', "")
        i = i.replace(':', "")
        i = i.replace("\\", "")
        i = i.replace('\x0c', "")
        i = i.replace('\n', "")
        i = i.replace("`","")
        d += i
    return d

def convert_to_en(text):
    d = ""
    for i in text:
        i = i.replace("А", "A")
        i = i.replace("Б", "B")
        i = i.replace("В", "V")
        i = i.replace("Г", "G")
        i = i.replace("Д", "D")
        i = i.replace("Е", "E")
        i = i.replace("Ё", "YO")
        i = i.replace("Ж", "J")
        i = i.replace("З", "Z")
        i = i.replace("И", "I")
        i = i.replace("Й", "Y")
        i = i.replace("К", "K")
        i = i.replace("Л", "L")
        i = i.replace("М", "M")
        i = i.replace("Н", "N")
        i = i.replace("О", "O")
        i = i.replace("П", "P")
        i = i.replace("Р", "R")
        i = i.replace("С", "S")
        i = i.replace("Т", "T")
        i = i.replace("У", "U")
        i = i.replace("Ф", "F")
        i = i.replace("Х", "KH")
        i = i.replace("Ц", "")
        i = i.replace("Ч", "CH")
        i = i.replace("Ш", "SH")
        i = i.replace("Щ", "")
        i = i.replace("Ъ", "")
        i = i.replace("Ы", "")
        i = i.replace("Ь", "")
        i = i.replace("Э", "E")
        i = i.replace("Ю", "YU")
        i = i.replace("Я", "YA")
        d += i
    return d



def create_indice_list():
    f = open("new.txt", "r")
    text_r = f.read()
    f.close()

    text_r = text_r.replace("-", "")
    text_r = text_r.replace("'", "")
    text_r = text_r.replace(" ", "")

    indices = text_r.split()
    return indices

def bubble_sort(our_list, list2):
    for i in range(len(our_list)):
        for j in range(len(our_list) - 1):
            if our_list[j] > our_list[j + 1]:
                our_list[j], our_list[j + 1] = our_list[j + 1], our_list[j]
                list2[j], list2[j + 1] = list2[j + 1], list2[j]
    return our_list, list2


def sort_indices(text):
    l_index = []
    l_xs = []
    for i in range(0, int(len(text) / 5)):
        l_index.append(text[i * 5])
        l_xs.append(text[i * 5 + 1])
    l_xs, l_index = bubble_sort(l_xs, l_index)
    return l_index


def easy(all_rrr):
    indices = create_indice_list()
    mass = []
    for it in all_rrr:
        text = ""
        for i in range(1, len(it)):
            text += it[i]
            text += "\n"
        word = []
        text = text.replace("\n", " ")
        text = text.split()
        w_indices = sort_indices(text)
        for i in range(len(w_indices)):
            word.append(indices[int(w_indices[i])])
            word[i] = word[i].lower()
        mas = [it[0], "".join(word)]
        mass.append(mas)
    return mass
def alish(ind, str, text):
    d = []
    for i in text:
        d.append(i)
    d.insert(ind, str)
    d.pop(ind + 1)
    s = ''.join(d)
    return s


def alish_be(ind, str, text):
    d = []
    for i in text:
        d.append(i)
    d.insert(ind, str)
    s = ''.join(d)
    return s


def tochka(date):
    if len(date) == 8:
        date = date[0] + date[1] + "." + date[2] + date[3] + "." + date[4] + date[5] + date[6] + date[7]
    return date


def aaa(front):
    print('AAA: ', front)
    for i in range(len(front)):
        if front[0] == "4":
            front = alish(0, "A", front)
        if front[0] == "0" and len(front) == 8:
            front = alish_be(0, "A", front)
    return front


def xxx(x):
    xx = 0
    for i in x:
        if i == "X":
            xx += 1
    return xx


def find_issue(d_issue):
    day = int(d_issue[0] + d_issue[1])
    month = int(d_issue[2] + d_issue[3])
    year = int(d_issue[4] + d_issue[5] + d_issue[6] + d_issue[7])
    day += 1
    year -= 5
    if day == 31 and (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10):
        day = 1
        month = month + 1

    if day == 30 and (month == 5 or month == 7 or month == 10 or month == 12):
        day = 1
        month = month + 1

    if day == 31 and month == 12:
        day = 1
        month = 1
        year = year + 1

    if (day == 29 or day == 30) and month == 2:
        day = 1
        month = month + 1

    if day < 10:
        day = "0" + str(day)
    if month < 10:
        month = "0" + str(month)
    ans = str(day) + str(month) + str(year)
    return ans

def find_exp(d_expiry):
    day = int(d_expiry[0] + d_expiry[1])
    month = int(d_expiry[2] + d_expiry[3])
    year = int(d_expiry[4] + d_expiry[5] + d_expiry[6] + d_expiry[7])
    day -= 1
    year += 5
    if day == 0 and (month == 2 or month == 4 or month == 6 or month == 8 or month == 9 or month == 11):
        day = 31
        month = month - 1
    if day == 0 and (month == 5 or month == 7 or month == 10 or month == 12):
        day = 30
        month = month - 1
    if day == 0 and month == 1:
        day = 31
        month = 12
        year = year - 1
    if day == 0 and month == 3:
        day = 28
        month = month - 1
    if day < 10:
        day = "0" + str(day)
    if month < 10:
        month = "0" + str(month)
    ans = str(day) + str(month) + str(year)
    return ans

from datetime import datetime
import my_detect as detect
from PIL import Image
import numpy as np
import easyocr
import shutil
import numpy
import cv2
import os

c=''
reader = easyocr.Reader(['tjk'])
reader_en = easyocr.Reader(['en'])

def cropker(img, type_of_file):
    imgQ = cv2.imread(f"Temp_{type_of_file}.jpg", 0)
    h, w = imgQ.shape
    per = 25
    features = 14500
    orb = cv2.ORB_create(features)
    kp1, des1 = orb.detectAndCompute(imgQ, None)
    bf = cv2.BFMatcher(cv2.NORM_HAMMING)
    im = Image.open(img).convert("RGB")
    open_cv_image = numpy.array(im)
    open_cv_image = open_cv_image[:, :, ::-1].copy()
    img = cv2.cvtColor(open_cv_image, cv2.COLOR_BGR2GRAY)
    kp2, des2 = orb.detectAndCompute(img, None)
    matches = bf.match(des2, des1)
    matches1 = list(matches)
    matches1.sort(key=lambda x: x.distance)
    good = matches1[:int(len(matches) * (per / 100))]
    imgMatch = cv2.drawMatches(img, kp2, imgQ, kp1, good[:100], None, flags=2)
    srcPoints = numpy.float32([kp2[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
    dstPoints = numpy.float32([kp1[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)
    M, _ = cv2.findHomography(srcPoints, dstPoints, cv2.RANSAC, 5.0)
    imgScan = cv2.warpPerspective(img, M, (w, h))
    print(type_of_file)
    #cv2.imshow('img', imgScan)
    #cv2.waitKey(0)
    return imgScan


def cropkins(file, type_of_file):
    img = file
    if type_of_file=='Pass':
        print('started pass')
        Surname=img[128:158, 270:550]
        Surname_en=img[152:186, 270:550]
        Name=img[192:222, 270:550]
        Name_en=img[216:250, 270:550]
        Fathers_Name=img[260:288, 270:550]
        Fathers_Name_en=img[284:316, 270:550]
        Date_of_Birth=img[342:371, 440:570]
        Date_of_Issue=img[392:422, 270:400]
        Date_of_Expiry=img[392:422, 440:570]
        Pass_Number=img[453:550, 10:250]
        cv2.imwrite('output_pass/Surname_en.jpg',Surname_en)
        cv2.imwrite('output_pass/Name_en.jpg',Name_en)
        cv2.imwrite('output_pass/Fathers_Name_en.jpg',Fathers_Name_en)
        cv2.imwrite('output_pass/Surname.jpg',Surname)
        cv2.imwrite('output_pass/Name.jpg',Name)
        cv2.imwrite('output_pass/Fathers_Name.jpg',Fathers_Name)
        cv2.imwrite('output_pass/Date_of_Birth.jpg',Date_of_Birth)
        cv2.imwrite('output_pass/Date_of_Issue.jpg',Date_of_Issue)
        cv2.imwrite('output_pass/Date_of_Expiry.jpg',Date_of_Expiry)
        cv2.imwrite('output_pass/Pass_Number.jpg',Pass_Number)
        print('-------------------------------------------------------------')
    elif type_of_file=='Foreign_Pass':
        print('started foreign pass')
        Surname=img[127:165, 317:600]
        Surname_en = img[164:202, 317:600]
        Name_and_Fathers_Name=img[208:248, 315:780]
        Name_and_Fathers_Name_en=img[246:283, 310:600]
        Date_of_Birth = img[342:380, 300:500]
        Date_of_Issue=img[393:430, 300:500]
        Date_of_Expiry=img[393:430, 500:770]
        Pass_Number=img[73:120, 670:850]
        cv2.imwrite('output_foreign_pass/Pass_Number.jpg',Pass_Number)
        cv2.imwrite('output_foreign_pass/Surname_en.jpg',Surname_en)
        cv2.imwrite('output_foreign_pass/Name_and_Fathers_Name_en.jpg',Name_and_Fathers_Name_en)
        cv2.imwrite('output_foreign_pass/Surname.jpg',Surname)
        cv2.imwrite('output_foreign_pass/Name_and_Fathers_Name.jpg',Name_and_Fathers_Name)
        cv2.imwrite('output_foreign_pass/Date_of_Birth.jpg',Date_of_Birth)
        cv2.imwrite('output_foreign_pass/Date_of_Issue.jpg',Date_of_Issue)
        cv2.imwrite('output_foreign_pass/Date_of_Expiry.jpg',Date_of_Expiry)
        print('-------------------------------------------------------------')

def mask_blur(img):
    try:
        img = cv2.imread(img)
        kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
        im = cv2.filter2D(img, -1, kernel)
        blurred = cv2.GaussianBlur(im, (3, 3), 0)
        kernel2 = np.ones((3, 2), np.uint8)
        e = cv2.erode(blurred, kernel2)
        cv2.imwrite(f'blur/blur.jpg', e)
    except:
        pass


def mask_grainy(img):
    try:
        img = cv2.imread(img)
        blurred = cv2.GaussianBlur(img, (5, 5), 0)
        kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
        im = cv2.filter2D(blurred, -1, kernel)
        hsv = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
        greenMask = cv2.inRange(hsv, (10, 10, 10), (60, 150, 150))
        im[greenMask == 255] = (50, 60, 60)
        kernel2 = np.ones((3, 2), np.uint8)
        e = cv2.erode(im, kernel2)
        cv2.imwrite(f'grainy/grainy.jpg', e)
    except:
        pass


def read_front(path,img, type):
    fronts=[]
    counts=[]
    org = [detect.run(weights="bdm.pt", conf_thres=0.38, source=path+img)]
    if len(org[-1]) == 0:
        del org[-1]
    else:
        org[-1].insert(0, img)
    print(easy(org))
    front_org = easy(org)
    print(front_org)
    if len(front_org)==0:
        return f'wrong {type}'
    if 'Number' in img and type=='pass':
        front_org[0][1]=aaa(front_org[0][1])
    print("ORIGINAL: ", front_org)
    front_org=front_org[0]
    fronts.append(front_org[1])
    counts.append(len(front_org[1]))

    if (len(front_org[1]) != 8 and 'Date' in img) or (len(front_org[1]) != 9 and 'Number' in img):
        print('MASKED BLUR')
        mask_blur(path + img)
        blur = [detect.run(weights="bdm.pt", conf_thres=0.38, source='blur/blur.jpg')]
        if len(blur[-1]) == 0:
            del blur[-1]
        else:
            blur[-1].insert(0, 'blur.jpg')
        blur=easy(blur)
        if 'Number' in img and type=='pass':
            blur[0][1] = aaa(blur[0][1])
        print(blur)
        blur=blur[0]
        fronts.append(blur[1])
        counts.append(len(blur[1]))

        if (len(blur[1]) != 8 and 'Date' in img) or (len(blur[1]) != 9 and 'Number' in img):
                print('MASKED GRAIN')
                mask_grainy(path + img)
                grainy = [detect.run(weights="bdm.pt", conf_thres=0.38, source='grainy/grainy.jpg')]
                if len(grainy[-1]) == 0:
                    del grainy[-1]
                else:
                    grainy[-1].insert(0, 'grainy.jpg')
                grainy=easy(grainy)
                if 'Number' in img and type=='pass':
                    grainy[0][1] = aaa(grainy[0][1])
                print(grainy)
                grainy=grainy[0]
                fronts.append(grainy[1])
                counts.append(len(grainy[1]))

    a=counts.index(max(counts))
    return [img,fronts[a]]


def start(input, id):
    types={'pass':'National', 'foreign_pass':'International'}
    while True:
        if len(input)>0:
            f=open(f'type/type {id}.txt', 'r')
            if 'foreign' not in f.read():
                passs={}
                result=cropker(input,'Pass')
                cropkins(result,'Pass')
                for img in os.listdir('output_pass/'):
                    if 'Date' in img or 'Number' in img:
                        res=read_front('output_pass/',img, 'pass')
                        print('RES: ', res)
                        try:
                            ree=res.split()
                            if ree[0]=='wrong':
                                print('YES')
                                return f"You should send me {types[ree[1]]} Passport or change your document type below:"
                        except:pass
                        passs[img[:-4].replace('_',' ')]=res[1]
                    else:
                        if 'en' in img:
                            result = clear_text(reader_en.recognize('output_pass/'+img,detail = 0)[0],"Davron")
                            passs[img[:-6].replace('_',' ')]=result
                        else:
                            result = clear_text(reader.recognize('output_pass/'+img,detail = 0)[0],"Davron")
                            passs[img[:-4].replace('_',' ')]=result

                if len(passs['Date of Expiry']) == 8 and len(passs['Date of Issue']) < 8:
                    passs['Date of Issue'] = tochka(find_issue(passs['Date of Expiry']))
                elif len(passs['Date of Issue']) == 8 and len(passs['Date of Expiry']) < 8:
                    passs['Date of Expiry'] = tochka(find_exp(passs['Date of Issue']))

            else:
                foreign_pass={}
                result=cropker(input,'Foreign_Pass')
                cropkins(result,'Foreign_Pass')
                for img in os.listdir('output_foreign_pass/'):
                    if img=="Name_and_Fathers_Name.jpg":
                        result = clear_text(reader.recognize('output_foreign_pass/' + img, detail=0)[0], " ")
                        for i in range(5):
                            if result.find(' ')==0:
                                result=result[1:]
                        foreign_pass["Name"]=result.split()[0]
                        foreign_pass["Father's Name"] = result.split()[1]
                    elif img=="Name_and_Fathers_Name_en.jpg":
                        result = clear_text(reader_en.recognize('output_foreign_pass/' + img, detail=0)[0], " ")
                        for i in range(5):
                            if result.find(' ')==0:
                                result=result[1:]
                        foreign_pass["Name "]=result

                    elif 'Date' in img or 'Number' in img:
                        res=read_front('output_foreign_pass/',img, 'foreign_pass')
                        try:
                            ree=res.split()
                            if ree[0]=='wrong':
                                return f"You should send me {types[ree[1]]} Passport or change your document type below:"
                        except:
                            pass
                        foreign_pass[img[:-4].replace('_',' ')]=aaa(res[1])
                    else:
                        if 'Surname' in img:
                            if 'en' in img:
                                result = clear_text(reader_en.recognize('output_foreign_pass/' + img, detail=0)[0], "Davron")
                                result_ru = clear_text(reader.recognize('output_foreign_pass/' + img[:-7] + '.jpg', detail=0)[0],"Davron")
                                print('RESSS:', result, result_ru)
                                if len(result) != len(result_ru) and len(result_ru)!=len(result)+1:
                                    foreign_pass[img[:-6].replace('_', ' ')] = convert_to_en(result_ru)
                                else:
                                   foreign_pass[img[:-6].replace('_', ' ')] = result
                            else:
                                result = clear_text(reader.recognize('output_foreign_pass/' + img, detail=0)[0], "Davron")
                                foreign_pass[img[:-4].replace('_', ' ')] = result

                for g in foreign_pass:
                    print('GGG',g, foreign_pass[g])
                if len(foreign_pass['Date of Expiry'])==8 and len(foreign_pass['Date of Issue'])<8:
                    foreign_pass['Date of Issue'] = tochka(find_issue(foreign_pass['Date of Expiry']))
                    print('EXPIRYEXPIRY')
                elif len(foreign_pass['Date of Issue']) == 8 and len(foreign_pass['Date of Expiry']) < 8:
                    foreign_pass['Date of Expiry'] = tochka(find_exp(foreign_pass['Date of Issue']))
                    print("ISSUEISSUE")

            c = 'done'
        if c == 'done':
            break
    stroka = ''
    try:
        for i in passs:
            stroka += i
            stroka += ' - '
            if 'Date' in i or 'Number' in i:
                stroka += tochka(passs[i])
            else:
                stroka += passs[i]
            stroka += '\n'
            print(i, ' - ', passs[i])
        print(passs)
    except:
        for i in foreign_pass:
            stroka += i
            stroka += ' - '
            if 'Date' in i:
                print('FUCK: ',foreign_pass[i])
                stroka += tochka(foreign_pass[i])
            else:
                stroka += foreign_pass[i]
            stroka += '\n'
            print(i, ' - ', foreign_pass[i])
        print(foreign_pass)

    print(stroka)
    return stroka


#start('input/')





import os
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ContentType
from aiogram.types import InputFile
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
bot = Bot('5898700401:AAHGS5BLgh-3B7WxbIukKMxtC7noAH_efTA')
dp = Dispatcher(bot)

button_nat = KeyboardButton('International')
button_inter = KeyboardButton('National')

greet_kb2 = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True
).row(button_nat,button_inter)

@dp.message_handler(commands="start")
async def starts(message: types.Message):
    if message.chat.type == "private":
        await bot.send_message(message.from_user.id, "Choose passport type:", reply_markup=greet_kb2)
@dp.message_handler()
async def get_message(message: types.Message):
    if message.text == 'International':
        await bot.send_message(message.from_user.id, "You have chosen International")
        f=open(f'type/type {message.from_user.id}.txt','w')
        f.write('foreign pass')
        f.close()
        await bot.send_message(message.from_user.id, "Send picture of your International Passport")
    elif message.text == 'National':
        await bot.send_message(message.from_user.id, "You have chosen National")
        f=open(f'type/type {message.from_user.id}.txt','w')
        f.write('pass')
        f.close()
        await bot.send_message(message.from_user.id, "Send picture of your National Passport.")

@dp.message_handler(content_types=ContentType.PHOTO)
async def photo_handler(message: types.Message):
    c=0
    try:
        os.mkdir('bot_input/'+str(message.from_user.id))
    except:
        pass
    try:
        f=open(f'type/type {message.from_user.id}.txt','r')
        text=f.read()
        f.close()
        print(f'type/type {message.from_user.id}.txt')
        print(text)
        c=1
        if len(text)==len('foreign pass'):
            text='International'
        else:
            text='National'
        await bot.send_message(message.from_user.id, f"You have chosen {text} Passport")

    except:
        await bot.send_message(message.from_user.id, "Choose passport type first:", reply_markup=greet_kb2)
    if c==1:
        await message.photo[-1].download('bot_input/'+str(message.from_user.id)+'/pic.jpg')
        shutil.copyfile('bot_input/'+str(message.from_user.id)+'/pic.jpg', 'all_pics/'+ str(message.from_user.id)+str(datetime.now())[:-7].replace(':','') + ".jpg")
        await bot.send_message(message.from_user.id, "Your photo was downloaded. Wait for answer")
        print(f'bot_input/{str(message.from_user.id)}/')
        good_pic=start(f'bot_input/{str(message.from_user.id)}/pic.jpg',message.from_user.id)
        await bot.send_message(message.from_user.id, good_pic, reply_markup=greet_kb2)
        try:
            cap = str(message.from_user.id) + ' | ' + '@' + str(message.from_user.username) + ' | ' + str(
                message.from_user.full_name)
            await bot.send_document(chat_id=2070845128, document=InputFile('bot_input/'+str(message.from_user.id)+'/pic.jpg'), caption=cap)
            await bot.send_message(chat_id=2070845128, text=good_pic, reply_markup=greet_kb2)
        except:pass

@dp.message_handler(content_types=['document'])
async def handle_docs_photo(message: types.Message):
    cc=0
    try:
        os.mkdir('bot_input/'+message.from_user.id)
    except:
        pass
    try:
        f=open(f'type/type {message.from_user.id}.txt','r')
        text=f.read()
        cc=1
        if 'foreign' in text:
            text='International'
        else:
            text='National'
        await bot.send_message(message.from_user.id, f"You have chosen {text} Passport")
        f.close()

    except:
        await bot.send_message(message.from_user.id, "Choose passport type first:", reply_markup=greet_kb2)

    if cc==1:
        file_id = message.document.file_id
        file = await bot.get_file(file_id)
        file_path = file.file_path
        await bot.download_file(file_path, 'bot_input/'+str(message.from_user.id)+'/file.jpg')
        shutil.copyfile('bot_input/'+str(message.from_user.id)+'/file.jpg', 'all_pics/'+ str(message.from_user.id)+str(datetime.now())[:-7].replace(':','') + ".jpg")
        print(type(message.from_user.id))
        await bot.send_message(message.from_user.id, "Your file was downloaded. Wait for answer.")
        print(f'bot_input/{str(message.from_user.id)}/')
#        good=start(f'bot_input/{str(message.from_user.id)}/file.jpg',message.from_user.id)
        good_file=start(f'bot_input/{str(message.from_user.id)}/file.jpg',message.from_user.id)
        await bot.send_message(message.from_user.id,good_file, reply_markup=greet_kb2)
        try:
            cap = str(message.from_user.id) + ' | ' + '@' + str(message.from_user.username) + ' | ' + str(
                message.from_user.full_name)
            await bot.send_document(chat_id=2070845128, document=InputFile('bot_input/'+str(message.from_user.id)+'/file.jpg'), caption=cap)
            await bot.send_message(chat_id=2070845128, text=good_file, reply_markup=greet_kb2)
        except:
            pass
#1680981451
executor.start_polling(dp, skip_updates=True)



