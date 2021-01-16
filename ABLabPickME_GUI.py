# -*- coding: utf-8 -*-
"""
Created on Sat Jan 17 11:52:08 2021

@author: peachrl
"""

#pyinstaller -D -w -i ablab.ico ABLabPickME_GUI.py

import PySimpleGUI as sg
import pickwho as pw
import os
#import codecs

if not os.path.exists(os.getcwd()+r'\data'):
    os.makedirs(os.getcwd()+r'\data')

sg.theme('GreenMono')

layout = [
    [sg.Frame(layout=[
    [sg.Text('若从上次储存开始则不需要选择文件夹', size=(40, 1), key="-MEMORY-")],
    [sg.Radio('从上次储存开始', "RADIO1", default=True, size=(20,1)), sg.Radio('重新开始', "RADIO1")],
    [
        sg.Text("重新开始，请选择namelist.txt文档所在文件夹："),
        sg.In(size=(10, 1), enable_events=True, key="-FOLDER-"),
        sg.FolderBrowse('浏览'),
    ],
    [sg.Radio('自动储存结果', "RADIO2", default=True, size=(20,1)), sg.Radio('不自动储存结果', "RADIO2")],
    [sg.Text('选择抽取范围：', size=(40, 1), key="-LIST-")],
    [sg.Checkbox('老师组', default=False)],
    [sg.Checkbox('2021组', default=False), sg.Checkbox('2020组', default=True), sg.Checkbox('2019组', default=True), sg.Checkbox('2018组', default=True)],
    [sg.Checkbox('2017组', default=True), sg.Checkbox('2016组', default=True), sg.Checkbox('2015组', default=True)],      
    ], 
    title='Options',title_color='black', relief=sg.RELIEF_SUNKEN, tooltip='May you be lucky! <(*￣▽￣*)/')],
    
    [
        sg.Button('储存结果', enable_events=True, key="-SAVE-"),
        sg.Text(size=(15, 1), key="-TOUT2-"),
        sg.Button('开始抽取', enable_events=True, key="-PICK-"),
        sg.Text(size=(0, 1), key="-TOUT1-")],
    [
        sg.Button('清空储存', enable_events=True, key="-FORGET-"),
        sg.Text(size=(15, 1), key="-TOUT3-"),
        sg.Button('退出程序', enable_events=True, key="-EXIT-"),
        sg.Text(size=(0, 1), key="-TOUT4-")]
    ]
window = sg.Window('这是ABLab专用抽奖小程序。祝你好运！', layout)
while True:
    event, values = window.read()
    if event == "-EXIT-" or event == None:
        if os.path.exists(os.getcwd()+r'\data\tmp.txt'):
            os.remove(os.getcwd()+r"\data\tmp.txt")
        break

    elif event == "-PICK-":
        if values[0]:
            if not os.path.exists(os.getcwd()+r'\data\data.txt'):
                sg.popup("NO Memory..")
            elif os.path.getsize(os.getcwd()+r'\data\data.txt')==0:
                sg.popup("EVERYONE has been \n picked out for once!")
            else:
                with open(os.getcwd()+r'\data\data.txt',mode="r",encoding='utf-8') as fdata:
                    with open(os.getcwd()+r'\data\tmp.txt',mode="w+",encoding='utf-8') as ftmp:
                        ftmp.seek(0)
                        ftmp.truncate()
                        for line in fdata:
                            ftmp.write(line.encode('utf-8').decode('utf-8-sig'))
                    # fdata=codecs.open(os.getcwd()+r'\data\data.txt','w+','utf-8')
                    # ftmp=codecs.open(os.getcwd()+r'\data\tmp.txt','r','utf-8')
                    # ftmp.seek(0)
                    # for line in fdata:
                    #     ftmp.truncate()
                    #     ftmp.write(line)
                    # fdata.close()
                    # ftmp.close()
                window["-TOUT1-"].update("Picking...")
                name_list_cut = pw.savedlist(pw.dict_saved)
                name = pw.luckyone(name_list_cut)
                rest_list = pw.restlist(name_list_cut, name)
                pw.autosave(pw.dict_saved, rest_list)
                window["-TOUT1-"].update("Ending~~~")
                sg.popup('    '+name+'    ')
                pw.save(values[2], pw.dict_saved, rest_list)
                    # if event == "-SAVE-":
                    #     pw.save(1, pw.dict_saved, rest_list)
                    #     window["-TOUT2-"].update("Saving...")
                    #     window["-TOUT2-"].update("Saved Already")
        elif values["-FOLDER-"]:
            list_dict = pw.list_dict(values['-FOLDER-'])
            window["-TOUT1-"].update("Picking...")
            name_list_cut = pw.picklist(values['-FOLDER-'], values[4], values[5], values[6], values[7], values[8], values[9], values[10], values[11])
            name = pw.luckyone(name_list_cut)
            rest_list = pw.restlist(name_list_cut, name)
            pw.autosave(list_dict, rest_list)
            window["-TOUT1-"].update("Ending~~~")
            sg.popup('    '+name+'    ')
            pw.save(values[2], list_dict, rest_list)
            if values[2]==1:
                window[0].update(True)
            # if event == "-SAVE-":
            #     pw.save(1, list_dict, rest_list)
            #     window["-TOUT2-"].update("Saving...")
            #     window["-TOUT2-"].update("Saved Already")
        
            name = 'name'
            rest_list = []
            name_list_cut = []
        
    elif event == "-SAVE-":
        # pw.save(1, pw.dict_saved, rest_list)
        if not os.path.exists(os.getcwd()+r'\data\tmp.txt'):
            sg.popup("NO Memory..")
        else:
            with open(os.getcwd()+r'\data\tmp.txt',mode="r",encoding='utf-8') as ftmp:
                with open(os.getcwd()+r'\data\data.txt',mode="w+",encoding='utf-8') as fdata:
                    fdata.seek(0)
                    fdata.truncate()
                    for line in ftmp:
                        fdata.write(line)
        window["-TOUT2-"].update("Saving...")
        window["-TOUT2-"].update("Saved Already")
        
    elif event == "-FORGET-":
        if os.path.exists(os.getcwd()+r'\data\data.txt')!=0:
            os.remove(os.getcwd()+r"\data\data.txt")
        if os.path.exists(os.getcwd()+r'\data\tmp.txt')!=0:
            os.remove(os.getcwd()+r"\data\tmp.txt")
        window["-TOUT3-"].update("Deleting...")
        window["-TOUT3-"].update("Deleted Already")
        
    
    else:
        window["-TOUT1-"].update("Wrong...")

    if event == "-EXIT-" or event == None:
        if os.path.exists(os.getcwd()+r'\data\tmp.txt'):
            os.remove(os.getcwd()+r"\data\tmp.txt")
        break
    print(event, values)
window.close()
