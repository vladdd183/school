from time import sleep as wait

def get():
    a = int(input('How many tasks: '))
    tasks = []
    for x in range(0, a):
        tasks.append([])
        print('=========Task=Number=#' + str(x+1) + '=========')
        print('Commands:')
        tasks[x].insert(x, input('1. '))
        tasks[x].insert(x+1, input('2. '))
        tasks[x].insert(x+2, input('Need transfer: '))
        tasks[x].insert(x+3, input('Transfer to: '))
    return tasks
    pass

def main():
    a = get()
    for x in range(0, len(a)): \\Дальше старый код
        debug = 1
        need = [0 , 0]
        need_tmp = [0, 0]
        path = []
        tmp_fcom = 0
        tmp_scom = 0
        stop = 0
        stop_suka = 0
        fcom = a[x][0] 
        scom = a[x][1]
        fcom = fcom.split(' ')
        scom = scom.split(' ')
        fcom[1] = int(fcom[1])
        scom[1] = int(scom[1])
        if debug == 1:
            print(fcom)
            print(scom)

        need[0] = int(a[x][2])
        need[1] = int(a[x][3])
        need_tmp[0] = need[0]
        need_tmp[1] = need[1]
        if debug == 1:
            print(need)
        inver = 0

        if fcom[0] == '-':
            if scom[0] == '-':
                while need_tmp[0] > need[1]:
                    if scom[1] > fcom[1] and need_tmp[0] - scom[1] >= need[1]:
                        print(str(need_tmp[0]) + ' - ' + str(scom[1]))
                        need_tmp[0] = need_tmp[0] -  scom[1]
                        print('=' + str(need_tmp[0]))
                        if inver == 1:
                            path.append('1')
                            inver = 0
                        else:
                            path.append('2')
                    elif need_tmp[0] - fcom[1] >= need[1]:
                        print(str(need_tmp[0]) + ' - ' + str(fcom[1]))
                        need_tmp[0] = need_tmp[0] -  fcom[1]
                        print('=' + str(need_tmp[0]))
                        if inver == 1:
                            path.append('2')
                            inver = 0
                        else:
                            path.append('1')
                    else:
                        inver = 1
                        tmp_fcom = fcom[1]
                        tmp_scom = scom[1]
                        fcom[1] = tmp_scom
                        scom[1] = tmp_fcom
                print(str(list(path)) + '<== Ответ')

            elif scom[0] == '+':
                while need_tmp[0] != need[1]:
                    if need_tmp[0] > need[1]:
                        print(str(need_tmp[0]) + ' - ' + str(fcom[1]))
                        need_tmp[0] = need_tmp[0] -  fcom[1]
                        print('=' + str(need_tmp[0]))
                        path.append('1')
                    elif need_tmp[0] < need[1]:
                        print(str(need_tmp[0]) + ' + ' + str(scom[1]))
                        need_tmp[0] = need_tmp[0] +  scom[1]
                        print('=' + str(need_tmp[0]))
                        path.append('2')
                print(str(list(path)) + '<== Ответ')

            elif scom[0] == '*':
                while need_tmp[1] != need[0]:
                    if need_tmp[1] > need[0]:
                        if need_tmp[1] % scom[1] == 0:
                            print(str(need_tmp[1]) + ' / ' + str(scom[1]))
                            need_tmp[1] = need_tmp[1] / scom[1]
                            path.append('2')
                            need_tmp[1] = int(need_tmp[1])
                        else:
                            print(str(need_tmp[1]) + ' + ' + str(fcom[1]))
                            need_tmp[1] = need_tmp[1] + fcom[1]
                            path.append('1')
                            need_tmp[1] = int(need_tmp[1])
                    else:
                        print(str(need_tmp[1]) + ' + ' + str(fcom[1]))
                        need_tmp[1] = need_tmp[1] + fcom[1]
                        path.append('1')
                        need_tmp[1] = int(need_tmp[1])
                print(str(list(reversed(path))) + '<== Ответ')

            elif scom[0] == '/':
                while need_tmp[0] != need[1]:
                    if need_tmp[0] % scom[1] == 0:
                        print(str(need_tmp[0]) + ' / ' + str(scom[1]))
                        need_tmp[0] = need_tmp[0] / scom[1]
                        path.append('2')
                        need_tmp[0] = int(need_tmp[0])
                    else:
                        print(str(need_tmp[0]) + ' - ' + str(fcom[1]))
                        need_tmp[0] = need_tmp[0] - fcom[1]
                        path.append('1')
                        need_tmp[0] = int(need_tmp[0])
                print(str(list(path)) + '<== Ответ')
        #===============================================================================
        elif fcom[0] == '+':
            if scom[0] == '-':
                while need_tmp[0] != need[1]:
                    if need_tmp[0] - scom[1] >= need[1]:
                        print(str(need_tmp[0]) + ' - ' + str(scom[1]))
                        need_tmp[0] = need_tmp[0] -  scom[1]
                        print('=' + str(need_tmp[0]))
                        path.append('2')
                    else:
                        print(str(need_tmp[0]) + ' + ' + str(fcom[1]))
                        need_tmp[0] = need_tmp[0] +  fcom[1]
                        print('=' + str(need_tmp[0]))
                        path.append('1')
                print(path)

            elif scom[0] == '+':
                while need_tmp[0] != need[1]:
                    if need_tmp[0] + fcom[1] <= need[1]:
                        print(str(need_tmp[0]) + ' + ' + str(fcom[1]))
                        need_tmp[0] = need_tmp[0] +  fcom[1]
                        print('=' + str(need_tmp[0]))
                        path.append('1')
                    else:
                        print(str(need_tmp[0]) + ' + ' + str(scom[1]))
                        need_tmp[0] = need_tmp[0] +  scom[1]
                        print('=' + str(need_tmp[0]))
                        path.append('2')
                print(str(list(path)) + '<== Ответ')

            elif scom[0] == '*':
                while need_tmp[1] != need[0]:
                    if need_tmp[1] - fcom[1] == need[0]:
                        print(str(need_tmp[1]) + ' - ' + str(fcom[1]))
                        need_tmp[1] = need_tmp[1] - fcom[1]
                        path.append('1')
                        need_tmp[1] = int(need_tmp[1])
                    elif need_tmp[1] % scom[1] == 0 and need_tmp[1] / fcom[1] >= need[0]:
                        print(str(need_tmp[1]) + ' / ' + str(scom[1]))
                        need_tmp[1] = need_tmp[1] / scom[1]
                        path.append('2')
                        need_tmp[1] = int(need_tmp[1])
                    else:
                        print(str(need_tmp[1]) + ' - ' + str(fcom[1]))
                        need_tmp[1] = need_tmp[1] - fcom[1]
                        path.append('1')
                        need_tmp[1] = int(need_tmp[1])
                print(str(list(reversed(path))) + '<== Ответ')

            elif scom[0] == '/':
                while need_tmp[0] != need[1]:
                    if need_tmp[0] % scom[1] == 0:
                        print(str(need_tmp[0]) + ' / ' + str(scom[1]))
                        need_tmp[0] = need_tmp[0] / scom[1]
                        path.append('2')
                        need_tmp[0] = int(need_tmp[0])
                    else:
                        print(str(need_tmp[0]) + ' + ' + str(fcom[1]))
                        need_tmp[0] = need_tmp[0] + fcom[1]
                        path.append('1')
                        need_tmp[0] = int(need_tmp[0])
                print(str(list(path)) + '<== Ответ')
        #===============================================================================
        elif fcom[0] == '*':
            if scom[0] == '-':
                while need_tmp[1] != need[0]:
                    if need_tmp[1] % fcom[1] == 0 and need_tmp[1] / fcom[1] >= need[0] - (3 * scom[1]):
                        print(str(need_tmp[1]) + ' / ' + str(fcom[1]))
                        need_tmp[1] = need_tmp[1] / fcom[1]
                        path.append('1')
                        need_tmp[1] = int(need_tmp[1])
                    else:
                        print(str(need_tmp[1]) + ' + ' + str(scom[1]))
                        need_tmp[1] = need_tmp[1] + scom[1]
                        path.append('2')
                        need_tmp[1] = int(need_tmp[1])
                print(str(list(reversed(path))) + '<== Ответ')

            elif scom[0] == '+':
                while need_tmp[1] != need[0]:
                    if need_tmp[1] - scom[1] == need[0]:
                        print(str(need_tmp[1]) + ' - ' + str(scom[1]))
                        need_tmp[1] = need_tmp[1] - scom[1]
                        path.append('2')
                        need_tmp[1] = int(need_tmp[1])
                    elif need_tmp[1] % fcom[1] == 0 and need_tmp[1] / fcom[1] >= need[0]:
                        print(str(need_tmp[1]) + ' / ' + str(fcom[1]))
                        need_tmp[1] = need_tmp[1] / fcom[1]
                        path.append('1')
                        need_tmp[1] = int(need_tmp[1])
                    else:
                        print(str(need_tmp[1]) + ' - ' + str(scom[1]))
                        need_tmp[1] = need_tmp[1] - scom[1]
                        path.append('2')
                        need_tmp[1] = int(need_tmp[1])
                print(str(list(reversed(path))) + '<== Ответ')

            elif scom[0] == '*':
                while need_tmp[1] != need[0]:
                    if fcom[1] > scom[1]:
                        if need_tmp[1] % fcom[1] == 0 and need_tmp[1] / fcom[1] >= need[0]:
                            print(str(need_tmp[1]) + ' / ' + str(fcom[1]))
                            need_tmp[1] = need_tmp[1] / fcom[1]
                            path.append('1')
                            need_tmp[1] = int(need_tmp[1])
                        else:
                            print(str(need_tmp[1]) + ' / ' + str(scom[1]))
                            need_tmp[1] = need_tmp[1] / scom[1]
                            path.append('2')
                            need_tmp[1] = int(need_tmp[1])
                    else:
                        if need_tmp[1] % scom[1] == 0 and need_tmp[1] / scom[1] >= need[0]:
                            print(str(need_tmp[1]) + ' / ' + str(scom[1]))
                            need_tmp[1] = need_tmp[1] / scom[1]
                            path.append('2')
                            need_tmp[1] = int(need_tmp[1])
                        else:
                            print(str(need_tmp[1]) + ' / ' + str(fcom[1]))
                            need_tmp[1] = need_tmp[1] / fcom[1]
                            path.append('1')
                            need_tmp[1] = int(need_tmp[1])
                print(str(list(reversed(path))) + '<== Ответ')

            elif scom[0] == '/':
                while need_tmp[0] != need[1]:
                    if need_tmp[0] % scom[1] == 0:
                        print(str(need_tmp[0]) + ' / ' + str(scom[1]))
                        need_tmp[0] = need_tmp[0] / scom[1]
                        path.append('2')
                        need_tmp[0] = int(need_tmp[0])
                    else:
                        print(str(need_tmp[0]) + ' * ' + str(fcom[1]))
                        need_tmp[0] = need_tmp[0] * fcom[1]
                        path.append('1')
                        need_tmp[0] = int(need_tmp[0])
                print(str(list(path)) + '<== Ответ')
        #===============================================================================
        elif fcom[0] == '/':
            if scom[0] == '-':
                while need_tmp[0] != need[1]:
                    if need_tmp[0] % fcom[1] == 0 and need_tmp[0] / fcom[1] >= need[1]:
                        print(str(need_tmp[0]) + ' / ' + str(fcom[1]))
                        need_tmp[0] = need_tmp[0] /  fcom[1]
                        print('=' + str(need_tmp[0]))
                        path.append('1')
                        time.sleep(1)
                    else:
                        print(str(need_tmp[0]) + ' - ' + str(scom[1]))
                        need_tmp[0] = need_tmp[0] -  scom[1]
                        print('=' + str(need_tmp[0]))
                        path.append('2')
                        time.sleep(1)
                print(path)

            elif scom[0] == '*':
                while need_tmp[0] != need[1]:
                    while need_tmp[0] * scom[1] != need[1]:
                        print(str(need_tmp[0]) + ' / ' + str(fcom[1]))
                        need_tmp[0] = need_tmp[0] / fcom[1]
                        print('=' + str(need_tmp[0]))
                        path.append('1')
                    print(str(need_tmp[0]) + ' * ' + str(scom[1]))
                    need_tmp[0] = need_tmp[0] * scom[1]
                    print('=' + str(need_tmp[0]))
                    path.append('2')
                print(str(list(reversed(path))) + '<== Ответ')

            elif scom[0] == '+':
                while need_tmp[0] != need[1]:
                    if (need_tmp[0] % fcom[1] == 0) and (need_tmp[0] / fcom[1] >= need[1] - 2 * scom[1]):
                        print(str(need_tmp[0]) + ' / ' + str(fcom[1]))
                        need_tmp[0] = need_tmp[0] /  fcom[1]
                        print('=' + str(need_tmp[0]))
                        path.append('1')
                        time.sleep(1)
                    else:
                        print(str(need_tmp[0]) + ' + ' + str(scom[1]))
                        need_tmp[0] = need_tmp[0] +  scom[1]
                        print('=' + str(need_tmp[0]))
                        path.append('2')
                        time.sleep(1)
                print(str(path) + '<== Ответ')

            elif scom[0] == '^':
                while need_tmp[1] != need[0]:
                    if sqrt(need_tmp[1]).is_integer():
                        print(str(sqrt(need_tmp[1])))
                        need_tmp[1] = sqrt(need_tmp[1])
                        print('=' + str(need_tmp[1]))
                        path.append('2')
                    else:
                        print(str(need_tmp[1]) + ' * ' + str(fcom[1]))
                        need_tmp[1] = need_tmp[1] *  fcom[1]
                        print('=' + str(need_tmp[1]))
                        path.append('1')
                print(str(list(reversed(path))) + '<== Ответ')
    pass


main()
