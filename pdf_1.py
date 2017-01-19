# this program is created to extract from "pdf_2.pdf"
import re
#import csv
#import BeautifulSoup
from lxml import html
from lxml import etree
#import requests
import pdfquery
#------------------------------------------------------------------------------#

#------------------------------------------------------------------------------#

REPEATER = re.compile(r"(.+?)\1+$")
#the function repeated is used to cut out any repeatation of the result
#it is implemented as there were some results with repeatation problem
#------------------------------------------------------------------------------#

#------------------------------------------------------------------------------#
def repeated(s):
    s = s + " "
    match = REPEATER.match(s)
    return match.group(1) if match else s
#------------------------------------------------------------------------------#

#------------------------------------------------------------------------------#
def pdf_extract(path):
    pdf1 = pdfquery.PDFQuery(path)
    pdf1.load()
    name_element = pdf1.pq('LTPage[pageid=\'1\'] LTTextLineHorizontal:contains("Mon")')[0]
    print name_element.text
    x1 = float(name_element.get('x0'))
    y1 = float(name_element.get('y0'))
    #the pdf1.tree.write("name",) creates an xml file of the namspecified
    pdf1.tree.write("scrping_scraper", pretty_print=True)
    Task = []

    j = 0
    for i in range(21):
        #the pdf1.pq() works like a jquery query it extracts the text inside the specified box
        #text1 = repeated((pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("52.0, %s, 195.85, %s ")'%(1,385.6 - j,398.93 - j)).text()))
        text1 = repeated((pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("%s, %s, %s, %s ")'
                                  %(1,52.0 - 250.0 + x1 ,385.6 -413.6 + y1- j,195.85 - 250.0 + x1,398.93 -413.6 + y1- j)).text())).encode('utf8')
        Task.append(text1)
        j = j + 14
        #print text1

    #print text2
    j = 0
    Tue = []
    for k in range(21):
        #text5 = repeated(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("303.0, %s, 338.666, %s ")'%(1,385.6 - j,398.93 - j)).text()))
        text5 = repeated((pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("%s, %s, %s, %s ")'
                                  %(1,303.0 - 250.0 + x1 ,385.6 -413.6 + y1- j,338.666 - 250.0 + x1,398.93 -413.6 + y1- j)).text())).encode('utf8')
        Tue.append(text5)
        j = j + 14
        #print text5

    j = 0
    Wed = []
    for k in range(21):
        #text6 = repeated(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("361.0,%s , 398.666,%s ")'%(1,385.6 - j,398.93 - j)).text()))
        text6 = repeated((pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("%s, %s, %s, %s ")'
                                  %(1,361.0 - 250.0 + x1 ,385.6 -413.6 + y1- j,398.666 - 250.0 + x1,398.93 -413.6 + y1- j)).text())).encode('utf8')
        Wed.append(text6)
        j = j + 14
        #print text6



    j = 0
    Mon = []
    for k in range(21):
        #text8 = repeated(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("238.0, %s, 278.666, %s")'%(1,385.6 - j,398.93 - j)).text()))
        text8 = repeated((pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("%s, %s, %s, %s ")'
                                  %(1,238.0 - 250.0 + x1 ,385.6 -413.6 + y1- j,278.666 - 250.0 + x1,398.93 -413.6 + y1- j)).text())).encode('utf8')
        Mon.append(text8)
        j = j + 14
        #print text8

    j = 0
    Fri = []
    for k in range(21):
        #text9 =repeated(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("487.0, %s, 515.666, %s")'%(1,385.6 - j,398.93 - j)).text()))
        text9 = repeated((pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("%s, %s, %s, %s ")'
                                  %(1,487.0 - 250.0 + x1 ,385.6 -413.6 + y1- j,515.666 - 250.0 + x1,398.93 -413.6 + y1- j)).text())).encode('utf8')
        Fri.append(text9)
        j = j + 14
        #print text9

    j = 0
    Thu = []
    for k in range(21):
        #text9 = repeated(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("425.0, %s, 455.666, %s")'%(1,385.6 - j,398.93 - j)).text()))
        text9 = repeated((pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("%s, %s, %s, %s ")'
                                  %(1,425.0 - 250.0 + x1 ,385.6 -413.6 + y1- j,455.666 - 250.0 + x1,398.93 -413.6 + y1- j)).text())).encode('utf8')
        Thu.append(text9)
        j = j + 14
        #print text9
    j = 0
    Sat = []
    for k in range(21):
        #text10 = repeated(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("545.0, %s, 580.516, %s")'%(1,385.6 - j,398.93 - j)).text()))
        text10 = repeated((pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("%s, %s, %s, %s ")'
                                  %(1,545.0 - 250.0 + x1 ,385.6 -413.6 + y1- j,580.516 - 250.0 + x1,398.93 -413.6 + y1- j)).text())).encode('utf8')
        Sat.append(text10)
        j = j + 14
        #print text10
    j = 0
    Sun = []
    for k in range(21):
        #text11 = repeated(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("600.0, %s, 650.516, %s")'%(1,385.6 - j,398.93 - j)).text()))
        text11 = repeated((pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("%s, %s, %s, %s ")'
                                  %(1,600.0 - 250.0 + x1 ,385.6 -413.6 + y1- j,650.516 - 250.0 + x1,398.93 -413.6 + y1- j)).text())).encode('utf8')
        Sun.append(text11)
        j = j + 14
        #print text11
    Total = []
    j = 0
    for k in range(21):
        #text12 = repeated(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("677.0, %s, 694.874, %s")'%(1,385.6 - j,398.93 - j)).text()))
        text12 = repeated((pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("%s, %s, %s, %s ")'
                                  %(1,677.0 - 250.0 + x1 ,385.6 -413.6 + y1- j,694.874 - 250.0 + x1,398.93 -413.6 + y1- j)).text())).encode('utf8')
        Total.append(text12)
        j = j + 14
        #print text12

    j = 0
    ThuD = []
    for k in range(21):
        #text9 = repeated(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("415.0, %s, 470.556, %s")'%(1,399.6 - j,412.93 - j)).text()))
        text9 = repeated((pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("%s, %s, %s, %s ")'
                                  %(1,415.0 - 250.0 + x1 ,399.6 -413.6 + y1- j,470.556 - 250.0 + x1,412.93 -413.6 + y1- j)).text())).encode('utf8')
        ThuD.append(text9)
        j = j + 70
        #print text9
    '''
    text4 = pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("83.9,%s, 124.676,%s")'%(1,442.817, 454.577)).text()
    print text4
    '''
    j = 0
    SatD = []
    for k in range(4):
        #text11 = repeated(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("535.0, %s, 598.624, %s")'%(1,399.6 - j,412.93 - j)).text()))
        text11 = repeated((pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("%s, %s, %s, %s ")'
                                  %(1,535.0 - 250.0 + x1 ,399.6 -413.6 + y1- j,598.624 - 250.0 + x1,412.93 -413.6 + y1- j)).text())).encode('utf8')
        SatD.append(text11)
        j = j + 70
        #print text11

    j = 0
    TueD = []
    for k in range(31):
        #text11 = repeated(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("290.0, %s, 350.624, %s")'%(1,399.6 - j,412.93 - j)).text()))
        text11 = repeated((pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("%s, %s, %s, %s ")'
                                  %(1,290.0 - 250.0 + x1 ,399.6 -413.6 + y1- j,350.624 - 250.0 + x1,412.93 -413.6 + y1- j)).text())).encode('utf8')
        TueD.append(text11)
        j = j + 70
        #print text11

    j = 0
    FriD = []
    for k in range(21):
        #text11 = repeated(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("470.0, %s, 535.624, %s")'%(1,399.6 - j,412.93 - j)).text()))
        text11 = repeated((pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("%s, %s, %s, %s ")'
                                  %(1,470.0 - 250.0 + x1 ,399.6 -413.6 + y1- j,535.624 - 250.0 + x1,412.93 -413.6 + y1- j)).text())).encode('utf8')
        FriD.append(text11)
        j = j + 70
        #print text11
    j = 0
    WedD = []
    for k in range(21):
        #text11 = repeated(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("350.0, %s, 411.666, %s")'%(1,399.6 - j,412.93 - j)).text()))
        text11 = repeated((pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("%s, %s, %s, %s ")'
                                  %(1,350.0 - 250.0 + x1 ,399.6 -413.6 + y1- j,411.666 - 250.0 + x1,412.93 -413.6 + y1- j)).text())).encode('utf8')
        WedD.append(text11)
        j = j + 70
        #print text11
    j = 0
    MonD = []
    for k in range(21):
        #text11 = repeated(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("221.0, %s, 296.666, %s")'%(1,399.6 - j,412.93 - j)).text()))
        text11 = repeated((pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("%s, %s, %s, %s ")'
                                  %(1,221.0 - 250.0 + x1 ,399.6 -413.6 + y1- j,296.666 - 250.0 + x1,412.93 -413.6 + y1- j)).text())).encode('utf8')
        MonD.append(text11)
        j = j + 70
        #print text11
    '''
    Early = []
    for k in range(size):
        text13 = pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("225.55,%s , 260.938,%s ")'%(1,694.817 - j,706.577 - j)).text()
        Early.append(text13)
        j = j + 12
        print text13
    Absent = []
    for k in range(size):
        text14 = pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("260.55,%s , 290.938,%s ")'%(1,694.817 - j,706.577 - j)).text()
        Absent.append(text14)
        j = j + 12
        print text14
    Leave = []
    for k in range(size):
        text15 = pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("290.55,%s , 330.938,%s ")'%(1,694.817 - j,706.577 - j)).text()
        Leave.append(text15)
        j = j + 12
        print text15

    text4 = pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("83.9,%s, 124.676,%s")'%(1,442.817, 454.577)).text()
    print text4
    #print date
    '''
    #all the attributes of the table are zipped in the m_file
    m_file = zip(Task,Mon,Tue,Wed,Thu,Fri,Sat,Sun,Total)
    #print m_file[1][0]
    #print m_file
    dict_list = []
    i = 0
    '''
    
    for y in m_file:
        
        dict1 = {str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("68.0, 407.6, 86.124, 420.93")'%(1,)).text()):m_file[i][0],
                 repeated(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("225.0, 413.6, 278.073, 426.93")'%(1,)).text())):m_file[i][1],
                 repeated(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("302.0, 413.6, 345.106, 426.93")'%(1,)).text())):m_file[i][2],
                 repeated(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("360.0, 413.6, 401.122, 426.93")'%(1,)).text())):m_file[i][3],
                 repeated(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("420.0, 413.6, 465.376, 426.93")'%(1,)).text())):m_file[i][4],
                 repeated(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("482.0, 413.6, 523.37, 426.93")'%(1,)).text())):m_file[i][5],
                 repeated(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("540.0, 413.6, 585.735, 426.93")'%(1,)).text())):m_file[i][6],
                 repeated(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("600.0, 413.6, 650.1, 426.93")'%(1,)).text())):m_file[i][7],
                 repeated(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("393.3, 706.049, 419.439, 717.78")'%(1,)).text())):m_file[i][8]
              }
        dict_list.append(dict1)
        i = i + 1
    '''
    for y in m_file:
        
        dict1 = {str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("%s,%s,%s,%s")'
                             %(1,68.0 - 250.0 + x1 ,407.6 -413.6 + y1,86.124 - 250.0 + x1,420.93 -413.6 + y1)).text()).encode('utf8'):m_file[i][0],
                 repeated(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("%s,%s,%s,%s")'
                                      %(1,68.0 - 250.0 + x1 , y1,86.124 - 250.0 + x1,426.93 -413.6 + y1)).text())).encode('utf8'):m_file[i][1],
                 repeated(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("%s,%s,%s,%s")'
                                      %(1,302.0 - 250.0 + x1 , y1,345.106 - 250.0 + x1,426.93 -413.6 + y1)).text())).encode('utf8'):m_file[i][2],
                 repeated(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("%s,%s,%s,%s")'
                                      %(1,360.0 - 250.0 + x1 , y1,401.122 - 250.0 + x1,426.93 -413.6 + y1)).text())).encode('utf8'):m_file[i][3],
                 repeated(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("%s,%s,%s,%s")'
                                      %(1,420.0 - 250.0 + x1 , y1,465.376 - 250.0 + x1,426.93 -413.6 + y1)).text())).encode('utf8'):m_file[i][4],
                 repeated(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("%s,%s,%s,%s")'
                                      %(1,482.0 - 250.0 + x1 , y1,523.37 - 250.0 + x1,426.93 -413.6 + y1)).text())).encode('utf8'):m_file[i][5],
                 repeated(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("%s,%s,%s,%s")'
                                      %(1,540.0 - 250.0 + x1 , y1,585.735 - 250.0 + x1,426.93 -413.6 + y1)).text())).encode('utf8'):m_file[i][6],
                 repeated(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("%s,%s,%s,%s")'
                                      %(1,600.0 - 250.0 + x1 , y1,650.1 - 250.0 + x1,426.93 -413.6 + y1)).text())).encode('utf8'):m_file[i][7],
                 repeated(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("%s,%s,%s,%s")'
                                      %(1,393.3 - 250.0 + x1 ,706.049 - 413.6 + y1,419.439 - 250.0 + x1,717.78 -413.6 + y1)).text())).encode('utf8'):m_file[i][8]
              }
        dict_list.append(dict1)
        i = i + 1    
    #dict_list is the dictionary list having dictionaries where the key is the table column heading
    #print dict_list
    
    '''
    def double_single(string):
        count = 0
        d = str(string).index(' ')
        
        string1 = list(string)
        length = len(string1)
        j = 0
        for i in range(length/2 - 1):
            j = j + 1
            
            if string1[j] == ' ':
                
                if string1[j] == string1[j +length/2 +1]:
                    count = count + 1
                i = i + 1
            
            else :
                
                if string1[j] == string1[j + length/2]:
                    count = count + 1
            if count == (length/2 - 1):
                return string1[:count]
            else:
                return string
        
    print double_single("dbz dbz")
    '''
    '''
    dict2 = {
             repeated(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("62.0, 463.6, 165.231, 476.93")'%(1,)).text())):
             repeated(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("225.0, 463.6, 320.1, 477.05")'%(1,)).text())),
             repeated(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("405.0, 463.6, 520.644, 476.93")'%(1,)).text())):
             repeated(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("520.0, 463.6, 620.889, 477.05")'%(1,)).text())),
             repeated(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("65.0, 495.6, 128.282, 508.93")'%(1,)).text())):
             repeated(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("220.0, 495.6, 285.156, 508.93")'%(1,)).text())),
             repeated(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("65.0, 481.6, 128.114, 494.93")'%(1,)).text())):
             repeated(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("220.0, 481.6, 280.224, 494.93")'%(1,)).text())),
             repeated(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("405.0, 495.6, 505.048, 508.62")'%(1,)).text())):
             repeated(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("525.0, 495.6, 595.224, 508.93")'%(1,)).text())),
             repeated(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("409.0, 481.6, 485.435, 494.62")'%(1,)).text())):
             repeated(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("530.0, 481.6, 628.439, 494.93")'%(1,)).text())),
             repeated(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("404.0, 449.6, 525.034, 462.93")'%(1,)).text())):
             repeated(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("520.0, 477.6, 620.889, 491.053")'%(1,)).text())),
             repeated(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("65.0, 431.6, 140.347, 444.93")'%(1,)).text())):
             repeated(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("225.0, 431.6, 400.483, 445.05")'%(1,)).text())),
             repeated(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("65.0, 449.6, 140.347, 462.93")'%(1,)).text())):
             repeated(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("225.0, 449.6, 345.283, 462.62")'%(1,)).text())),
            
             
             
             }
    '''
    dict2 = {
             repeated(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("%s, %s, %s, %s")'
                                  %(1,68.0 - 250.0 + x1 ,463.6 -413.6 + y1,165.231 - 250.0 + x1,476.93 -413.6 + y1)).text())).encode('utf8'):
             repeated(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("%s, %s, %s, %s")'
                                  %(1,225.0 - 250.0 + x1 ,463.6 -413.6 + y1,320.1 - 250.0 + x1,477.05 -413.6 + y1)).text())).encode('utf8'),
             repeated(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("%s, %s, %s, %s")'
                                  %(1,405.0 - 250.0 + x1 ,463.6 -413.6 + y1,520.644 - 250.0 + x1,476.93 -413.6 + y1)).text())).encode('utf8'):
             repeated(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("%s, %s, %s, %s")'
                                  %(1,520.0 - 250.0 + x1 ,463.6 -413.6 + y1,620.889 - 250.0 + x1,477.05 -413.6 + y1)).text())).encode('utf8'),
             repeated(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("%s, %s, %s, %s")'
                                  %(1,65.0 - 250.0 + x1 ,495.6 -413.6 + y1,128.282 - 250.0 + x1,508.93 -413.6 + y1)).text())).encode('utf8'):
             repeated(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("%s, %s, %s, %s")'
                                  %(1,220.0 - 250.0 + x1 ,495.6 -413.6 + y1,285.156 - 250.0 + x1,508.93 -413.6 + y1)).text())).encode('utf8'),
             repeated(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("%s, %s, %s, %s")'
                                  %(1,65.0 - 250.0 + x1 ,481.6 -413.6 + y1,128.114 - 250.0 + x1,494.93 -413.6 + y1)).text())).encode('utf8'):
             repeated(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("%s, %s, %s, %s")'
                                  %(1,220.0 - 250.0 + x1 ,481.6 -413.6 + y1,280.224 - 250.0 + x1,494.93 -413.6 + y1)).text())).encode('utf8'),
             repeated(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("%s, %s, %s, %s")'
                                  %(1,405.0 - 250.0 + x1 ,495.6 -413.6 + y1,505.048 - 250.0 + x1,508.62 -413.6 + y1)).text())).encode('utf8'):
             repeated(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("%s, %s, %s, %s")'
                                  %(1,525.0 - 250.0 + x1 ,495.6 -413.6 + y1,595.224 - 250.0 + x1,508.93 -413.6 + y1)).text())).encode('utf8'),
             repeated(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("%s, %s, %s, %s")'
                                  %(1,409.0 - 250.0 + x1 ,481.6 -413.6 + y1,485.435 - 250.0 + x1,494.62 -413.6 + y1)).text())).encode('utf8'):
             repeated(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("%s, %s, %s, %s")'
                                  %(1,530.0 - 250.0 + x1 ,481.6 -413.6 + y1,628.439 - 250.0 + x1,494.93 -413.6 + y1)).text())).encode('utf8'),
             repeated(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("%s, %s, %s, %s")'
                                  %(1,404.0 - 250.0 + x1 ,449.6 -413.6 + y1,525.034 - 250.0 + x1,462.93 -413.6 + y1)).text())).encode('utf8'):
             repeated(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("%s, %s, %s, %s")'
                                  %(1,520.0 - 250.0 + x1 ,477.6 -413.6 + y1,620.889 - 250.0 + x1,491.053 -413.6 + y1)).text())).encode('utf8'),
             repeated(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("%s, %s, %s, %s")'
                                  %(1,65.0 - 250.0 + x1 ,431.6 -413.6 + y1,140.347 - 250.0 + x1,444.93 -413.6 + y1)).text())).encode('utf8'):
             repeated(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("%s, %s, %s, %s")'
                                  %(1,225.0 - 250.0 + x1 ,431.6 -413.6 + y1,400.483 - 250.0 + x1,445.05 -413.6 + y1)).text())).encode('utf8'),
             repeated(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("%s, %s, %s, %s")'
                                  %(1,65.0 - 250.0 + x1 ,449.6 -413.6 + y1,140.347 - 250.0 + x1,462.93 -413.6 + y1)).text())).encode('utf8'):
             repeated(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("%s, %s, %s, %s")'
                                  %(1,225.0 - 250.0 + x1 ,449.6 -413.6 + y1,345.283 - 250.0 + x1,462.62 -413.6 + y1)).text())).encode('utf8'),
            
             
             
             }
    #dict2 is used to retrieve some datas outside the table
    #print dict2
    print dict_list,dict2
    file1 = open("pdf_1.txt",'w')
    for dictionary in dict_list:
        for key,value in dictionary.iteritems():
            print key,value
            file1.write(key + ":"  +  value)
            file1.write("\t")
            file1.write("\t")
        file1.write("\t")
        file1.write("\n")
    for key,value in dict2.iteritems():
        print key,value
        file1.write(key + ":"  +  value)
        file1.write("\t")
    file1.close()
    return dict_list,dict2

                       
