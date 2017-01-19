import re
from lxml import html
from lxml import etree
import pdfquery
#------------------------------------------------------------------------------#

#------------------------------------------------------------------------------#
def split_on_space(string,i):
    if(string != None):
        li = string.split(' ')
        return li[i]
    else:
        return [None,None,None]
#------------------------------------------------------------------------------#

#------------------------------------------------------------------------------#        
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
#------------------------------------------------------------------------------#

#------------------------------------------------------------------------------#            
def pdf_extract(path):
    pdf1 = pdfquery.PDFQuery(path)
    pdf1.load()
    pdf1.tree.write("scrpfl2", pretty_print=True)
    #date = extract_cells(1,"Out",198.538 - 176.15)
    j = 0
    text_file1 = str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("24.0, 763.5, 706.049, 779.925")'%(1,)).text())
    print text_file1
    text_file2 = str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("24.0, 748.8, 706.049, 762.794")'%(1,)).text())
    print text_file2
    text_file0 = str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("23.85, 779.925, 706.049, 803.642")'%(1,)).text())
    print text_file0
    def size(text_file1):
        size = re.findall('\d{1,2}',text_file1)
        print size
        i = size[0].split('\\')
        print i
        j = size[1].split('\\')
        print j
        return (int(size[4]) - int(size[0]) + 1)
    size = size(text_file1)
    print size

    text = pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("83.9, 622.817, 124.676, 634.577")'%(1,)).text()
    text2 = pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("83.9, 430.817, 124.676, 442.577")'%(1,)).text()
    text3 = pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("83.9, 418.817, 124.676, 430.577")'%(1,)).text()
    a = []
    for i in range(size):
        text1 = pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("83.9, %s, 124.676,%s ")'%(1,694.817 - j,706.577 - j)).text()
        a.append(text1)
        j = j + 12
        print text1
    print text2
    j = 0
    b = []
    for k in range(size):
        text5 = pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("176.15,%s , 196.538,%s ")'%(1,694.817 - j,706.577 - j)).text()
        b.append(text5)
        j = j + 12
        print text5
    j = 0
    c = []
    for k in range(size):
        text6 = pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("144.55,%s , 164.938,%s ")'%(1,694.817 - j,706.577 - j)).text()
        c.append(text6)
        j = j + 12
        print text6
    j = 0
    d = []
    for k in range(size):
        text7 = pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("208.55,%s , 229.938,%s ")'%(1,694.817 - j,706.577 - j)).text()
        d.append(text7)
        j = j + 12
        print text7
    j = 0
    i = []
    for k in range(size):
        text8 = split_on_space(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("334.3,%s , 385.507,%s ")'%(1,694.817 - j,706.577 - j)).text()),0)
        i.append(text8)
        j = j + 12
        print text8
    j = 0
    e = []
    for k in range(size):
        text9 = pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("517.95, %s, 563.093,%s ")'%(1,694.817 - j,706.577 - j)).text()
        e.append(text9)
        j = j + 12
        print text9
    j = 0
    f = []
    for k in range(size):
        text9 = pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("458.55, %s, 478.938,%s ")'%(1,694.817 - j,706.577 - j)).text()
        f.append(text9)
        j = j + 12
        print text9
    j = 0
    g = []
    for k in range(size):
        text10 = pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("545.2, %s, 565.588,%s ")'%(1,694.817 - j,706.577 - j)).text()
        g.append(text10)
        j = j + 12
        print text10
    text4 = pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("83.9,%s, 124.676,%s")'%(1,442.817, 454.577)).text()
    print text4
    j = 0
    Late = []
    for k in range(31):
        text11 = pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("208.65, %s, 225.757,%s ")'%(1,694.817 - j,706.577 - j)).text()
        Late.append(text11)
        j = j + 12
        print text11
    j = 0
    Tour = []
    for k in range(31):
        text11 = str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("334.05, %s, 350.507,%s ")'%(1,694.817 - j,706.577 - j)).text())
        Tour.append(text11)
        j = j + 12
        print text11
    j = 0
    Holi = []
    for k in range(31):
        text12 = pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("398.3, %s, 414.439,%s ")'%(1,694.817 - j,706.577 - j)).text()
        Holi.append(text12)
        j = j + 12
        print text12
    j = 0
    Early = []
    for k in range(size):
        text13 = pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("225.55,%s , 260.938,%s ")'%(1,694.817 - j,706.577 - j)).text()
        Early.append(text13)
        j = j + 12
        print text13
    j = 0
    Absent = []
    for k in range(size):
        text14 = pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("260.55,%s , 290.938,%s ")'%(1,694.817 - j,706.577 - j)).text()
        Absent.append(text14)
        j = j + 12
        print text14
    j = 0
    Leave = []
    for k in range(size):
        text15 = pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("290.55,%s , 330.938,%s ")'%(1,694.817 - j,706.577 - j)).text()
        Leave.append(text15)
        j = j + 12
        print text15
    j = 0
    Pwh = []
    for k in range(size):
        text16 = pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("475.25,%s , 520.32,%s ")'%(1,694.817 - j,706.577 - j)).text()
        Pwh.append(text16)
        j = j + 12
        print text16
    j = 0
    Uwh = []
    for k in range(size):
        text17 = pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("505.25,%s , 545.32,%s ")'%(1,694.817 - j,706.577 - j)).text()
        Uwh.append(text17)
        j = j + 12
        print text17
    j = 0
    O_T = []
    for k in range(size):
        text18 = pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("415.25,%s , 450.32,%s ")'%(1,694.817 - j,706.577 - j)).text()
        O_T.append(text18)
        j = j + 12
        print text18

    text4 = pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("83.9,%s, 124.676,%s")'%(1,442.817, 454.577)).text()
    print text4
    #print date
    m_file = zip(a,b,c,d,f,g,i,Late,Tour,Holi,Early,Absent,Leave,Pwh,Uwh,O_T)
    print m_file[1][0]
    print m_file
    dict_list = []
    i = 0

    for y in m_file:
        
        dict1 = {str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("85.0, 706.049, 132.354, 717.78")'%(1,)).text()):m_file[i][0],
                 split_on_space(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("173.55, 706.049, 200.42, 717.78")'%(1,)).text()),1):m_file[i][1],
                 split_on_space(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("143.55, 706.049, 165.066, 717.78")'%(1,)).text()),1):m_file[i][2],
                 split_on_space(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("334.05, 706.049, 385.507, 717.78")'%(1,)).text()),1):m_file[i][6],
                 split_on_space(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("429.05, 706.049, 479.157, 717.78")'%(1,)).text()),1):m_file[i][4],
                 split_on_space(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("517.95, 706.049, 563.093, 717.78")'%(1,)).text()),1):m_file[i][5],
                 split_on_space(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("208.65, 706.049, 225.757, 717.78")'%(1,)).text()),0):m_file[i][7],
                 split_on_space(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("334.05, 706.049, 385.507, 717.78")'%(1,)).text()),0):m_file[i][8],
                 split_on_space(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("393.3, 706.049, 419.439, 717.78")'%(1,)).text()),1):m_file[i][9],
                 split_on_space(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("237.9, 706.049, 322.434, 717.78")'%(1,)).text()),0):m_file[i][10],
                 split_on_space(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("237.9, 706.049, 322.434, 717.78")'%(1,)).text()),1):m_file[i][11],
                 split_on_space(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("237.9, 706.049, 322.434, 717.78")'%(1,)).text()),2):m_file[i][12],
                 split_on_space(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("475.25, 706.049, 515.32, 717.78")'%(1,)).text()),0):m_file[i][13],
                 split_on_space(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("517.95, 706.049, 563.093, 717.78")'%(1,)).text()),0):m_file[i][14],
                 split_on_space(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("429.05, 706.049, 479.157, 717.78")'%(1,)).text()),0):m_file[i][15]
                 }
        dict_list.append(dict1)
        i = i + 1
    print dict_list

        
    print double_single("dbz dbz")

    dict2 = {split_on_space(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("143.55, 706.049, 165.066, 717.78")'%(1,)).text()),1):
             str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("154.65, 321.217, 170.313, 332.977")'%(1,)).text()),
             split_on_space(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("517.95, 706.049, 563.093, 717.78")'%(1,)).text()),1):
             split_on_space(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("545.2, 308.417, 573.463, 358.577")'%(1,)).text()),0),
             split_on_space(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("334.05, 706.049, 385.507, 717.78")'%(1,)).text()),1):
             split_on_space(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("383.65, 321.217, 390.363, 332.977")'%(1,)).text()),1),
             split_on_space(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("208.65, 706.049, 225.757, 717.78")'%(1,)).text()),0):
             split_on_space(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("258.05, 278.017, 264.763, 289.777")'%(1,)).text()),0),
             split_on_space(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("393.3, 706.049, 419.439, 717.78")'%(1,)).text()),0):
             split_on_space(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("415.65, 321.217, 422.363, 332.977")'%(1,)).text()),0),
             split_on_space(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("429.05, 706.049, 479.157, 717.78")'%(1,)).text()),1):
             split_on_space(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("545.2, 308.417, 573.463, 358.577")'%(1,)).text()),0),
             split_on_space(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("237.9, 706.049, 322.434, 717.78")'%(1,)).text()),2):
             split_on_space(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("282.5, 321.217, 295.925, 332.977")'%(1,)).text()),0),
             split_on_space(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("237.9, 706.049, 322.434, 717.78")'%(1,)).text()),1):
             split_on_space(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("282.5, 321.217, 295.925, 332.977")'%(1,)).text()),1),
             split_on_space(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("334.05, 706.049, 385.507, 717.78")'%(1,)).text()),0):
             split_on_space(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("281.7, 278.017, 295.125, 289.777")'%(1,)).text()),0),
             split_on_space(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("237.9, 706.049, 322.434, 717.78")'%(1,)).text()),0):
             split_on_space(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("258.05, 278.017, 264.763, 289.777")'%(1,)).text()),1),
             split_on_space(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("489.25, 706.049, 508.32, 717.78")'%(1,)).text()),0):
             split_on_space(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("506.85, 321.217, 513.563, 332.977")'%(1,)).text()),0),
             split_on_space(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("517.95, 706.049, 563.093, 717.78")'%(1,)).text()),0):
             split_on_space(str(pdf1.pq('LTPage[pageid =\'%s\' ] :in_bbox("534.85, 321.217, 541.563, 332.977")'%(1,)).text()),0)
             
             
             }
    file1 = open("pdf_2.txt",'w')
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
    print dict_list,dict2
    return dict_list, dict2
#------------------------------------------------------------------------------#                  
