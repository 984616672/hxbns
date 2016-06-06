#!/bin/env python2.7
#coding:utf-8
# aixuancheng
#

from argparse import ArgumentParser
import sys

# help
def func_help():
    """
        1, 设置python main.py -h 帮助信息；
        2, 对传入的值获取[字典],并赋给全局变量option；
    """
    global options
    parser = ArgumentParser()
    parser.add_argument('-r', '--region', action='store', default='0', help="android", required=True)
    parser.add_argument('-a', '--action', action='store', default='0', help="hotupdate", required=True)
    parser.add_argument('-v', '--version', action='store', type=int, default='0', help="74747")
    parser.add_argument('-f', '--sqlfile', action='store', type=file, help="account.sql")
    parser.add_argument('-d', '--database', action='store', default='0', help="3dgamedata")
    options = vars(parser.parse_args())

# parameter_rule
def func_parameter_rule():
    """
        判断参数的合理性；
    """
    region_List = ['android', 'app', 'thailand', 'taiwan', 'malaysia', 'vietnam', 'korea', 'japan', 'abroad']
    if options.get('region') not in region_List:
        print('--region parameter err.')
        sys.exit()

    action_List = ['start', 'stop', 'update', 'hotupdate', 'importsql', 'backupsql']
    if options.get('action') not in action_List:
        print('--action parameter err.')
        sys.exit()

    dbs_List = ['3dgamedata', '3dgamedatalog', '3dactivecode', '3dgameaccount']
    if options.get('database') != '0' and options.get('database') not in dbs_List:
        print('--database parameter err.')
        sys.exit()

# action_start
def func_action_start():
    if options.get('action') == 'start':
        print('You are '+options.get('action')+' '+options.get('region')+' server !!')

    if options.get('action') == 'stop':
        print('You are '+options.get('action')+' '+options.get('region')+' server !!')

    if options.get('action') == 'update' and options.get('version') != 0:
        print('You are '+options.get('action')+' '+options.get('region')+' server, version: '+str(options.get('version'))+' !!')
    else:
        print('parameter err !!')

    if options.get('action') == 'hotupdate' and options.get('version') != 0:
        print('You are '+options.get('action')+' '+options.get('region')+' server, version: '+str(options.get('version'))+' !!')

    if options.get('action') == 'backupsql':
        print('You are '+options.get('action')+' '+options.get('region')+' server !!')

    if options.get('action') == 'importsql' and options.get('database') != '0' and options.get('sqlfile') != None:
        print('You are '+options.get('action')+' '+options.get('region')+' server, database: '+options.get('database')+' sqlfile: '+options.get('sqlfile')+' !')

# run
if __name__ == '__main__':
    func_help()
    func_parameter_rule()
    func_action_start()
#    print(options)
