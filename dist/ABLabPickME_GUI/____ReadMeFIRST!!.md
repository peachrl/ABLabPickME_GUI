# ReadMe File

[![standard-readme compliant](https://img.shields.io/badge/ABLabPickME-v2021.01.16-brightgreen.svg?style=flat-square)](https://github.com/peachRL/ABLabPickME)

- [ReadMe File](#readme-file)
  - [背景](#背景)
  - [安装](#安装)
  - [使用说明](#使用说明)
    - [储存](#储存)
    - [抽取范围](#抽取范围)
    - [界面和ico](#界面和ico)
  - [维护者](#维护者)
  - [使用许可](#使用许可)

## 背景

ABLabPickME小程序基于ABLab实验室年会随机报告的需求，对实验室成员进行随机抽奖。

## 安装

该项目使用Python编写，使用Pyinstaller打包成exe，在**gist**文件夹中。仅在windows系统使用。

本小程序不需要安装啦！直接双击ABLabPickME_GUI.exe使用。

## 使用说明

### 储存

ABLabPickME的数据储存在./data文件夹中。若从上次储存的结果开始，则不需要输入文件；若选择重新开始，需输入一个命名为namelist.txt的文件，示例在./data文件夹中有。

ABLabPickME使用自动储存，可用于每次抽取一人排除一人；使用不自动储存，则每次都会从同意名单抽取。

默认选项为“从上次储存开始”、“自动保存结果”。

### 抽取范围

包括老师组以及各年级组。默认选项为2015-2020年级组。

### 界面和ico

界面由PySimpleGUI生成，ico为随手打的。

<img src="https://img.imgdb.cn/item/6002e98b3ffa7d37b303e1e6.png" alt="界面" style="zoom:50%;" />

<img src="https://img.imgdb.cn/item/6002e9bf3ffa7d37b303fafb.png" alt="ico" style="zoom:25%;" />

## 维护者

[@peachRL](https://github.com/peachrl)


## 使用许可

[MIT](LICENSE) © peachRL

