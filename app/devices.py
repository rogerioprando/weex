def getevent():
    event = '>RUS00,090118221546-3016404-04850266999000,2064;ID=3958;#5E41;*01<'
    return event


def request_xvm(id,cmd):
    #>QGV;ID=4116;#8046;*5E<
    msg_cmd = '>'+cmd+';ID='+id+';#804C;*{crc}<'
    crc = hex(calcula_crc(msg_cmd))[2:].upper()
    msg_cmd = msg_cmd.format(crc=str(crc))
    return msg_cmd

##############################################
# colocar ou não thread nesse arquivo #
##############################################


def calcula_crc(data):
    crc = 0
    for ch in data:
        if ch == '*':
            break
        else:
            ch = ord(ch)
            crc = crc ^ ch
    return crc

