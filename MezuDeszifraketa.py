#name = input("Inscribe tu nombre: ")
#print("Hey, que tal ", name)
import string
from collections import Counter
def deszifratuAutomatiko():
    print("================Automatikoki egindako deszifraketa=================")
    #mezua sartu dut
    mezua="RIJ AZKKZHC PIKCE XT ACKCUXJHX SZX, E NZ PEJXKE, PXGIK XFDKXNEQE RIPI RIPQEHCK ET OENRCNPI AXNAX ZJ RKCHXKCI AX CJAXDXJAXJRCE AX RTENX, E ACOXKXJRCE AXT RITEQIKERCIJCNPI OKXJHXDIDZTCNHE AX TE ACKXRRCIJ EJEKSZCNHE. AZKKZHC OZX ZJ OERHIK AX DKCPXK IKAXJ XJ XT DEDXT AX TE RTENX IQKXKE XJ REHETZJVE XJ GZTCI AX 1936. DXKI AZKKZHC, RIPI IRZKKX RIJ TEN DXKNIJETCAEAXN XJ TE MCNHIKCE, JI REVI AXT RCXTI. DXKNIJCOCREQE TE HKEACRCIJ KXvITZRCIJEKCE AX TE RTENX IQKXKE. NZ XJIKPX DIDZTEKCAEA XJHKX TE RTENX HKEQEGEAIKE, KXOTXGEAE XJ XT XJHCXKKI PZTHCHZACJEKCI XJ QEKRXTIJE XT 22 AX JIvCXPQKX AX 1936, PZXNHKE XNE CAXJHCOCRERCIJ. NZ PZXKHX OZX NCJ AZAE ZJ UITDX IQGXHCvI ET DKIRXNI KXvITZRCIJEKCI XJ PEKRME. NCJ AZKKZHC SZXAI PEN TCQKX XT REPCJI DEKE SZX XT XNHETCJCNPI, RIJ TE RIPDTCRCAEA AXT UIQCXKJI AXT OKXJHX DIDZTEK V AX TE ACKXRRCIJ EJEKSZCNHE, HXKPCJEKE XJ PEVI AX 1937 TE HEKXE AX TCSZCAEK TE KXvITZRCIJ, AXNPIKETCLEJAI E TE RTENX IQKXKE V OERCTCHEJAI RIJ XTTI XT DINHXKCIK HKCZJOI OKEJSZCNHE."
    print("Mezu zifratua:")
    print(mezua)

    #puntuazioak(. ,) hutsune batengatik aldatu ditut
    punct = string.punctuation
    for a in punct:
        mezua=mezua.replace(a," ")

    #mezua ordezkatuko duten letren lista sortu dut
    # frekuentziak = ['e', 'a', 'o', 'l', 's', 'n', 'd', 'r', 'u', 'i', 't', 'c', 'p', 'm', 'y', 'q', 'b', 'h', 'g', 'f','v', 'j', 'ñ', 'z', 'x', 'k', 'w']
    frekuentziak = ['e', 'a', 'r', 'o', 'i', 'n', 'l', 'd', 'c', 'u', 't', 's', 'm', 'p', 'b', 'f', 'q', 'j', 'y', 'v','g', 'h', 'x', 'z', 'x', 'k', 'w']
    #eta letrak zenbatu ditut Counter erabiliz
    letrak=Counter(mezua)
    print("\nMezuaren karaktereen frekuentziak handienetik txikienera:")
    print(letrak)

    #mezuko letrak ordenatu ditut bere frekuentziaren arabera, handienetik txikira
    letra_ord=letrak.most_common()

    i = 0
    #mezuko karaktere bakoitzeko while bat
    for e in letra_ord:

        #karakterea zenbaki bat ez bada
        if not e[0].isdigit():
            #karakterea hutsune bat ez bada
            if not e[0] == " ":
                #karakterea frekuentzien listako i. elementuarengatik ordezkatu
                mezua = mezua.replace(e[0], frekuentziak.__getitem__(i))
                i = i + 1

    #mezu deszifratua printeatu
    print("\nMezu deszifratua: ")
    print(mezua+"\n")



def deszifratuEskuz():
    print("========================Eskuz egindako deszifraketa==========================")
    # mezua jarri eta letrak zenbatu ditut Counter erabiliz
    mezua = "RIJ AZKKZHC PIKCE XT ACKCUXJHX SZX, E NZ PEJXKE, PXGIK XFDKXNEQE RIPI RIPQEHCK ET OENRCNPI AXNAX ZJ RKCHXKCI AX CJAXDXJAXJRCE AX RTENX, E ACOXKXJRCE AXT RITEQIKERCIJCNPI OKXJHXDIDZTCNHE AX TE ACKXRRCIJ EJEKSZCNHE. AZKKZHC OZX ZJ OERHIK AX DKCPXK IKAXJ XJ XT DEDXT AX TE RTENX IQKXKE XJ REHETZJVE XJ GZTCI AX 1936. DXKI AZKKZHC, RIPI IRZKKX RIJ TEN DXKNIJETCAEAXN XJ TE MCNHIKCE, JI REVI AXT RCXTI. DXKNIJCOCREQE TE HKEACRCIJ KXvITZRCIJEKCE AX TE RTENX IQKXKE. NZ XJIKPX DIDZTEKCAEA XJHKX TE RTENX HKEQEGEAIKE, KXOTXGEAE XJ XT XJHCXKKI PZTHCHZACJEKCI XJ QEKRXTIJE XT 22 AX JIvCXPQKX AX 1936, PZXNHKE XNE CAXJHCOCRERCIJ. NZ PZXKHX OZX NCJ AZAE ZJ UITDX IQGXHCvI ET DKIRXNI KXvITZRCIJEKCI XJ PEKRME. NCJ AZKKZHC SZXAI PEN TCQKX XT REPCJI DEKE SZX XT XNHETCJCNPI, RIJ TE RIPDTCRCAEA AXT UIQCXKJI AXT OKXJHX DIDZTEK V AX TE ACKXRRCIJ EJEKSZCNHE, HXKPCJEKE XJ PEVI AX 1937 TE HEKXE AX TCSZCAEK TE KXvITZRCIJ, AXNPIKETCLEJAI E TE RTENX IQKXKE V OERCTCHEJAI RIJ XTTI XT DINHXKCIK HKCZJOI OKEJSZCNHE.\n"
    letrak = Counter(mezua)
    print("Mezu zifratua:")
    print(mezua)
    print("Mezuaren karaktereen frekuentziak handienetik txikienera:")
    print(letrak)

    # letrak banan banan aldatu
    mezua=mezua.replace('X', 'e')
    mezua=mezua.replace('E', 'a')
    mezua = mezua.replace('T', 'l')
    mezua = mezua.replace('A', 'd')
    mezua = mezua.replace('R', 'c')
    mezua = mezua.replace('N', 's')
    mezua = mezua.replace('C', 'i')
    mezua = mezua.replace('J', 'n')
    mezua = mezua.replace('D', 'p')
    mezua = mezua.replace('Z', 'u')
    mezua = mezua.replace('P', 'm')
    mezua = mezua.replace('K', 'r')
    mezua = mezua.replace('I', 'o')
    mezua = mezua.replace('H', 't')
    mezua = mezua.replace('U', 'g')
    mezua = mezua.replace('S', 'q')
    mezua = mezua.replace('G', 'j')
    mezua = mezua.replace('F', 'x')
    mezua = mezua.replace('Q', 'b')
    mezua = mezua.replace('O', 'f')
    mezua = mezua.replace('M', 'h')
    mezua = mezua.replace('V', 'y')

    #mezu deszifratua printeatu
    print("\nMezu deszifratua: ")
    print(mezua)



deszifratuAutomatiko()
deszifratuEskuz()