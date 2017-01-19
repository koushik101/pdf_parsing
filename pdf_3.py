#import csv
#import BeautifulSoup
from lxml import html
from lxml import etree
#import requests
import pdfquery
import re
#the function repeated is used to cut out any repeatation of the result
#it is implemented as there were some results with repeatation problem
#------------------------------------------------------------------------------#

#------------------------------------------------------------------------------#
def repeated(s):
    REPEATER = re.compile(r"(.+?)\1+$")
    s = s + " "
    match = REPEATER.match(s)
    return match.group(1) if match else s
#------------------------------------------------------------------------------#

#------------------------------------------------------------------------------#
def pdf_extract(filename):
    pdf1 = pdfquery.PDFQuery(filename)
    pdf1.load()
    #the pdf1.tree.write("name",) creates an xml file of the namspecified
    pdf1.tree.write("scrpf2", pretty_print=True)
    
    name_element = pdf1.pq('LTPage[pageid=\'1\'] LTTextLineHorizontal:contains("Month")')[0]
    #print name_element.text
    x0 = float(name_element.get('x0'))
    y0 = float(name_element.get('y0'))

    pn = 1
    #the pdf1.pq() works like a jquery query it extracts the text inside the specified box
    #c_data1 = repeated(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("570.744, 510.837, 605.631, 523.366 ")'%(1,)).text())
    c_data1 = repeated(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("%s, %s, %s, %s ")'
                               %(1,570.744  - 634.536 + x0,510.837 - 484.479 + y0,605.631 - 634.536 + x0,523.366 - 484.479 + y0)).text())
    #print c_data1
    size = re.findall("\d*",str(c_data1))
    #print size
    size = int(size[0])
    #print size
    x1 = 250.92  - 634.536 + x0
    x2 = 349.099 - 634.536 + x0
    y1 = 511.911 - 484.479 + y0
    y2 = 523.187 - 484.479 + y0
    c_data2 = repeated(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("%s, %s, %s, %s")'%(1,x1,y1,x2,y2)).text())
    #print c_data2
    
    #r_data2 = pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("707.976, 460.503, 806.254, 471.779")'%(2,)).text()
    r_data2 = pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("%s, %s, %s, %s")'
                      %(2,707.976  - 634.536 + x0,460.503 - 484.479 + y0,806.254 - 634.536 + x0,471.779 - 484.479 + y0)).text()
    #print r_data2
    #total =  repeated(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("711.192, 492.609, 776.66, 502.632")'%(2,)).text())
    total =  repeated(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("%s, %s, %s, %s")'
                              %(2,711.192  - 634.536 + x0,492.609 - 484.479 + y0,776.66 - 634.536 + x0,502.632 - 484.479 + y0)).text())
    #print total
    Atime =  repeated(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("%s, %s, %s, %s")'
                              %(2,697.976  - 634.536 + x0,460.503 - 484.479 + y0,796.254 - 634.536 + x0,471.779 - 484.479 + y0)).text())
    #print Atime
    j = 0
    Pname = []
    
    for k in range(size):
        x1 = 306.08  - 634.536 + x0
        x2 = 350.398 - 634.536 + x0
        y1 = 469.785 - 484.479 + y0
        y2 = 479.808 - 484.479 + y0
        text5 = repeated(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("%s, %s,%s,%s ")'%(pn,x1,y1  - j,x2,y2 - j)).text())
        #text5 = repeated(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("306.08,%s , 350.398,%s  ")'%(pn,469.785  - j,479.808 - j)).text())
        Pname.append(text5)
        if k == 26:
            j = -98.424
            pn = pn + 1
        j = j + 15.12
        #print text5
    j = 0

    Dentry = []
    AA_type = []
    pn = 1
    for k in range(size):
        x1 = 350.336  - 634.536 + x0
        x2 = 470.243 - 634.536 + x0
        y1 = 469.785 - 484.479 + y0
        y2 = 479.808 - 484.479 + y0
        text6 = repeated(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("%s, %s,%s,%s ")'%(pn,x1,y1  - j,x2,y2 - j)).text())
        #text6 = repeated(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("350.336, %s, 470.243, %s")'%(pn,469.785  - j,479.808 - j)).text())
        #print text6
        text8 = re.findall('[A-Za-z]*\s[A-Za-z]*',text6)
        text7 = " "
        for itr in text8:
            text7 = text7 + str(itr)
        
        text6 = re.findall('\d+/\d+/\d+',text6)
        #print text7
        AA_type.append(text7)
        
        
        Dentry.append(text6)
        if k == 26:
        #if y1 == 469.785 - 26*15.12:
            j = -98.424
            pn = pn + 1
        j= j + 15.12
        #print text6
    j = 0
    Status = []
    pn = 1
    for k in range(size):
        x1 = 555.024  - 634.536 + x0
        x2 = 614.252 - 634.536 + x0
        y1 = 469.785 - 484.479 + y0
        y2 = 479.808 - 484.479 + y0
        text7 = repeated(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("%s, %s,%s,%s ")'%(pn,x1,y1  - j,x2,y2 - j)).text())
        #text7 = repeated(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("555.024, %s, 614.252,%s ")'%(pn,469.785  - j,479.808 - j)).text())
        Status.append(text7)
        if k == 26:
        #if y1 == 469.785 - 26*15.12:
            j = -98.424
            pn = pn + 1
            #pn = 2
        j = j + 15.12
        #print text7
    j = 0
    Month = []
    pn = 1
    for k in range(size):
        x1 = 623.816  - 634.536 + x0
        x2 = 672.252 - 634.536 + x0
        y1 = 469.785 - 484.479 + y0
        y2 = 479.808 - 484.479 + y0
        text8 = repeated(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("%s, %s,%s,%s ")'%(pn,x1,y1  - j,x2,y2 - j)).text())
        #text8 = repeated(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("623.816, %s, 672.252, %s ")'%(pn,469.785  - j,479.808 - j)).text())
        if k == 26:
        #if y1 == 469.785 - 26*15.12:
            j = -98.424
            pn = pn + 1
            #pn = 2
        j = j + 15.12
        Month.append(text8)
        #print text8
    j = 0
    Year_ID = []
    pn = 1
    for k in range(size):
        x1 = 678.68 - 634.536 + x0
        x2 = 716.47 - 634.536 + x0
        y1 = 469.785 - 484.479 + y0
        y2 = 479.808 - 484.479 + y0
        text9 = repeated(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("%s, %s,%s,%s ")'%(pn,x1,y1  - j,x2,y2 - j)).text())
        #text9 = repeated(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("678.68, %s, 716.47, %s ")'%(pn,469.785  - j,479.808 - j)).text())
        Year_ID.append(text9)
        if k == 26:
        #if y1 == 469.785 - 26*15.12:
            j = -98.424
            pn = pn + 1
        j = j + 15.12
        #print text9
    j = 0
    Description = []
    pn = 1
    for k in range(size):
        x1 = 476.216 - 634.536 + x0
        x2 = 557.729 - 634.536 + x0
        y1 = 469.785 - 484.479 + y0
        y2 = 479.808 - 484.479 + y0
        text10 = repeated(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("%s, %s,%s,%s ")'%(pn,x1,y1  - j,x2,y2 - j)).text())
        #text10 = repeated(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("476.216, %s, 557.729, %s ")'%(pn,469.785  - j,479.808 - j)).text())
        Description.append(text10)
        if k == 26:
        #if y1 == 469.785 - 26*15.12:
            j = -98.424
            pn = pn + 1
        j = j + 15.12
        #print text10
    j = 0
    Emgr = []
    pn = 1
    for k in range(size):
        x1 = 221.48 - 634.536 + x0
        x2 = 293.306 - 634.536 + x0
        y1 = 469.785 - 484.479 + y0
        y2 = 479.808 - 484.479 + y0
        text11 = repeated(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("%s, %s,%s,%s ")'%(pn,x1,y1  - j,x2,y2 - j)).text())
        #text11 = repeated(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("221.48, %s, 293.306, %s ")'%(pn,469.785  - j,479.808 - j)).text())
        Emgr.append(text11)
        if k == 26:
        #if y1 == 469.785 - 26*15.12:
            j = -98.424
            pn = pn + 1
        j = j + 15.12
        #print text11
    j = 0
    EID = []
    pn = 1
    for k in range(size):
        x1 = 85.616 - 634.536 + x0
        x2 = 141.196 - 634.536 + x0
        y1 = 469.785 - 484.479 + y0
        y2 = 479.808 - 484.479 + y0
        text12 = repeated(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("%s, %s,%s,%s ")'%(pn,x1,y1  - j,x2,y2 - j)).text())
        #text12 = repeated(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("85.616, %s, 141.196, %s ")'%(pn,469.785  - j,479.808 - j)).text())
        EID.append(text12)
        if k == 26:
        #if y1 == 469.785 - 26*15.12:
            j = -98.424
            pn = pn + 1
        j = j + 15.12
        #print text12

    j = 0
    NSA = []
    pn = 1
    for k in range(size):
        x1 = 776.816 - 634.536 + x0
        x2 = 831.5 - 634.536 + x0
        y1 = 469.785 - 484.479 + y0
        y2 = 479.808 - 484.479 + y0
        text1 = repeated(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("%s, %s,%s,%s ")'%(pn,x1,y1  - j,x2,y2 - j)).text())
        #text1 = repeated(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("776.816, %s,831.5, %s ")'%(pn,469.785  - j,479.808 - j)).text())
        NSA.append(text1)
        if k == 26:
        #if y1 == 469.785 - 26*15.12:
            j = -98.424
            pn = pn + 1
            #pn = 2
        j = j + 15.12
        #print text1
    j = 0
    Ename = []
    pn = 1
    for k in range(size):
        x1 = 151.416 - 634.536 + x0
        x2 = 217.632 - 634.536 + x0
        y1 = 469.785 - 484.479 + y0
        y2 = 479.808 - 484.479 + y0
        text2 = repeated(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("%s, %s,%s,%s ")'%(pn,x1,y1  - j,x2,y2 - j)).text())
        #text2 = repeated(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("151.416, %s,217.632, %s ")'%(pn,469.785  - j,479.808 - j)).text())
        Ename.append(text2)
        if k == 26:
        #if y1 == 469.785 - 26*15.12:
            j = -98.424
            pn = pn + 1
            #pn = 2
        j = j + 15.12
        #print text2
    j = 0
    Hours = []
    pn = 1
    for k in range(size):
        x1 = 722.168 - 634.536 + x0
        x2 = 765.7 - 634.536 + x0
        y1 = 469.785 - 484.479 + y0
        y2 = 479.808 - 484.479 + y0
        text2 = repeated(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("%s, %s,%s,%s ")'%(pn,x1,y1  - j,x2,y2 - j)).text())
        #text2 = repeated(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("722.168, %s,765.7, %s ")'%(pn,469.785  - j,479.808 - j)).text())
        Hours.append(text2)
        if k == 26:
        #if y1 - j == 76.665:
            print "yes"
            j = -98.424
            pn = pn + 1
            #pn = 2
        j = j + 15.12
        #print text2
    #all the attributes of the table are zipped in the m_file
    m_file  = zip(Pname,Dentry,Status,Month,Year_ID,Description,Emgr,EID,NSA,Ename,Hours,AA_type)
    #print m_file
    dict_list = []
    i = 0

    for y in m_file:
        
        dict1 = {'Project Name':m_file[i][0],
                 'Date Entry':(m_file[i][1])[0],
                 repeated(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("564.632, 567.783, 609.631, 579.059")'%(1,)).text())):m_file[i][2],
                 repeated(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("624.536, 567.783, 671.389, 579.059")'%(1,)).text())):m_file[i][3],
                 #repeated(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("672.632, 567.783, 752.428, 579.059")'%(1,)).text())):m_file[i][4],
                 'Year':m_file[i][4],
                 repeated(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("486.8, 484.479, 551.03, 495.755")'%(1,)).text())):m_file[i][5],
                 #repeated(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("218.816, 567.783, 295.636, 579.059")'%(1,)).text())):m_file[i][6],
                 'Employee Mgr':m_file[i][6],
                 #repeated(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("56.0, 438.6, 129.102, 472.93")'%(1,)).text())):m_file[i][7],
                 'Employee ID':m_file[i][7],
                 repeated(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("793.944, 484.479, 814.426, 495.755")'%(1,)).text())):m_file[i][8],
                 repeated(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("76.544, 528.765, 168.937, 541.294")'%(1,)).text())):m_file[i][9],
                 repeated(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("722.168, 484.479, 765.7, 495.755")'%(1,)).text())):m_file[i][10],
                 repeated(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("421.352, 484.479, 475.071, 495.755")'%(1,)).text())):m_file[i][11]
              }
        #dict_list is the dictionary list having dictionaries where the key is the table column heading
        dict_list.append(dict1)
        i = i + 1
    #print dict_list
    #dict2 is used to retrieve some datas outside the table
        '''
    dict2 = {
            repeated(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("247.048, 528.765, 352.971, 541.294")'%(1,)).text())):c_data2,
            repeated(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("563.984, 528.837, 612.381, 541.366")'%(1,)).text())):c_data1,
            repeated(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("402.92, 528.837, 498.203, 541.366")'%(1,)).text())):
            repeated(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("402.92, 510.837, 498.203, 523.366 ")'%(1,)).text()),
            repeated(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("497.976, 460.503, 697.976, 471.779 ")'%(2,)).text()):
            Atime,
            repeated(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("511.192, 492.609, 711.192, 502.632")'%(2,)).text()):
            total,
            repeated(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("69.416, 461.295, 178.247, 472.571")'%(2,)).text()):
            repeated(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("188.247, 461.295, 378.247, 472.571")'%(2,)).text())
            
            
            }
            '''
    dict2 = {
            repeated(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("%s,%s,%s,%s")'
                                 %(1,247.048- 634.536 + x0,528.765- 484.479 + y0,352.971- 634.536 + x0,541.294- 484.479 + y0)).text())):c_data2,
            repeated(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("%s,%s,%s,%s")'
                                 %(1,563.984- 634.536 + x0,528.837- 484.479 + y0,612.381- 634.536 + x0,541.366- 484.479 + y0)).text())):c_data1,
            repeated(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("%s,%s,%s,%s")'
                                 %(1,402.92- 634.536 + x0,528.837- 484.479 + y0,498.203- 634.536 + x0,541.366- 484.479 + y0)).text())):
            repeated(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("%s,%s,%s,%s")'
                             %(1,402.92- 634.536 + x0,510.837- 484.479 + y0,498.203- 634.536 + x0,523.366- 484.479 + y0)).text()),
            repeated(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("%s,%s,%s,%s")'
                             %(2,497.976- 634.536 + x0,460.503- 484.479 + y0,697.976- 634.536 + x0,471.779- 484.479 + y0)).text()):
            Atime,
            repeated(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("%s,%s,%s,%s")'
                             %(2,511.192- 634.536 + x0,492.609- 484.479 + y0,711.192- 634.536 + x0,502.632- 484.479 + y0)).text()):
            total,
            repeated(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("%s,%s,%s,%s")'
                             %(2,69.416- 634.536 + x0,461.295- 484.479 + y0,178.247- 634.536 + x0,472.571- 484.479 + y0)).text()):
            repeated(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("%s,%s,%s,%s")'
                             %(2,188.247- 634.536 + x0,461.295- 484.479 + y0,378.247- 634.536 + x0,472.571- 484.479 + y0)).text())
            
            
            }
    text6 = repeated(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("%s,%s,%s,%s")'
                             %(2,364.104- 634.536 + x0,553.089- 484.479 + y0,447.884- 634.536 + x0,563.112- 484.479 + y0)).text())
    #print text6
    text6 = re.findall('\d+/\d+/\d+',text6)
    #print text7
    print dict2,dict_list
    file1 = open("pdf_3.txt",'w')
    for dictionary in dict_list:
        for key,value in dictionary.iteritems():
            print key,value
            file1.write(key + ":"  +  value)
            file1.write("\t")
        file1.write("\n")
    for key,value in dict2.iteritems():
        print key,value
        file1.write(key + ":"  +  value)
        file1.write("\t")
    file1.close()
    return dict_list,dict2
