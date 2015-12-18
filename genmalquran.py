#!/usr/bin/python
# -*- coding: utf-8 -*- 
target=open('qu.tex','w')
trans=open('ml.abdulhameed.txt','r')
surasize=[7,286,200,176,120,165,206,75,129,109,123,111,43,52,99,128,111,110,98,135,112,78,118,64,77,227,93,88,69,60,34,30,73,54,45,83,182,88,75,85,54,53,89,59,37,35,38,29,18,45,60,49,62,55,78,96,29,22,24,13,14,11,11,18,12,12,30,52,52,44,28,28,20,56,40,31,50,40,46,42,29,19,36,25,22,17,19,26,30,20,15,21,11,8,8,19,5,8,8,11,11,8,3,9,5,4,7,3,6,3,5,4,5,6]
suraname= ["അല്‍ ഫാത്തിഹ ( പ്രാരംഭം )","അല്‍ ബഖറ ( പശു )","ആലു ഇംറാന്‍ ( ഇംറാന്‍ കുടുംബം )","നിസാഅ് ( സ്ത്രീകള്‍ )","മാഇദ ( ഭക്ഷണ തളിക )","അന്‍ആം ( കാലികള്‍ )","അഅ്റാഫ് ( ഉന്നതസ്ഥലങ്ങള്‍‍ )","അന്‍ഫാല്‍ ( യുദ്ധമുതല്‍‍ )","തൌബ ( പശ്ചാത്താപം )","യൂനുസ്","ഹൂദ്","യൂസുഫ്","‍റഅദ് ( ഇടിനാദം )","ഇബ്രാഹീം","ഹിജ്റ്","നഹ്ല്‍ ( തേനീച്ച )","ഇസ്റാഅ് ( നിശായാത്ര )","അല്‍ കഹഫ് ( ഗുഹ‍ )","മര്‍യം","ത്വാഹാ","അന്‍ബിയാഅ് ( പ്രവാചകന്മാര്‍ )","ഹജ്ജ് ( തീര്‍ത്ഥാടനം )","അല്‍ മുഅ്മിനൂന്‍ ( സത്യവിശ്വാസികള്‍ )","നൂര്‍ ( പ്രകാശം )","ഫുര്‍ഖാന്‍ ( സത്യാസത്യ വിവേചനം )","ശുഅറാ ( കവികള്‍ )","നംല്‍ ( ഉറുമ്പ് )","ഖസസ് ( കഥാകഥനം‍ )","അങ്കബൂത് ( എട്ടുകാലി )","റൂം ( റോമാക്കാര്‍ )","ലുഖ്മാന്‍","സജദ ( സാഷ്ടാംഗം )","അഹ്സാബ് (സംഘടിത കക്ഷികള്‍ )","സബഅ്","ഫാത്വിര്‍ ( സ്രഷ്ടാവ് )","യാസീന്‍","സ്വാഫ്ഫാത്ത് ( അണിനിരന്നവ‍ )","സ്വാദ്","സുമര്‍ ( കൂട്ടങ്ങള്‍ )","മുഅ്മിന്‍‍ ( വിശ്വാസി )","ഫുസ്സിലത്ത്","ശൂറാ ( കൂടിയാലോചന )","സുഖ്റുഫ് ( സുവര്‍ണ്ണാലങ്കാരം )","ദുഖാന്‍ ( പുക )","ജാഥിയ ( മുട്ടുകുത്തുന്നവര്‍ )","അഹ്ഖാഫ്","മുഹമ്മദ്","ഫതഹ് ( വിജയം )","ഹുജുറാത് ( അറകള്‍ )","ഖാഫ്","ദാരിയാത് ( വിതറുന്നവ )","ത്വൂര്‍ ( ത്വൂര്‍ പര്‍വ്വതം)","നജ്മ് ( നക്ഷത്രം )","ഖമര്‍ ( ചന്ദ്രന്‍ )","റഹ് മാന്‍‍ ( പരമകാരുണികന്‍ )","അല്‍ വാഖിഅ ( സംഭവം )","ഹദീദ്  ( ഇരുമ്പ് )","  മുജാദില ( തര്‍ക്കിക്കുന്നവള്‍ )","ഹഷ്ര്‍ ( തുരത്തിയോടിക്കല്‍ )","മുംതഹന (. പരീക്ഷിക്കപ്പെടേണ്ടവള്‍ )","സ്വഫ്ഫ് ( അണി )","ജുമുഅ","മുനാഫിഖൂന്‍ ( കപടവിശ്വാസികള്‍ )","തഗാബൂന്‍ ( നഷ്ടം വെളിപ്പെടല്‍ )","ത്വലാഖ് ( വിവാഹ മോചനം )","തഹ് രീം ( നിഷിദ്ധമാക്കല്‍ )","മുല്‍ക്ക് ( അധിപത്യം )","ഖലം ( പേന )","ഹാഖ ( യഥാര്‍ത്ഥ സംഭവം )","മആരിജ് ( കയറുന്ന വഴികള്‍ )","നൂഹ്","ജിന്ന് ( ജിന്ന് വര്‍ഗ്ഗം )","മുസമ്മില്‍ ( വസ്ത്രത്താല്‍ മൂടിയവന്‍ )","മുദ്ദഥിര്‍ ( പുതച്ച് മൂടിയവന്‍ )","ഖിയാമ ( ഉയിര്‍ത്തെഴുന്നേല്‍പ്പ് )","ഇന്‍സാന്‍ ( മനുഷ്യന്‍ )","മുര്‍സലാത്ത് ( അയക്കപ്പെടുന്നവര്‍ )","നബഅ് ( വൃത്താന്തം )","നാസിയാത്ത് ( ഊരിയെടുക്കുന്നവ )","അബസ ( മുഖം ചുളിച്ചു )","തക് വീര്‍  ( ചുറ്റിപ്പൊതിയല്‍ )","ഇന്‍ഫിത്വാര്‍ ( പൊട്ടിക്കീറല്‍ )","മുതഫ്ഫിഫീന്‍ ( അളവില്‍ കുറയ്ക്കുന്നവന്‍ )","ഇന്ഷിഖാഖ് ( പൊട്ടിപിളരല്‍ )","ബുറൂജ് ( നക്ഷത്രമണ്ഡലങ്ങള്‍ )","ത്വാരിഖ് ( രാത്രിയില്‍ വരുന്നത് )","അഅ്അലാ ( അത്യുന്നതന്‍ )","ഗാശിയ ( മൂടുന്ന സംഭവം )","ഫജ്ര്‍ ( പ്രഭാതം )","ബലദ് ( രാജ്യം )","ശംസ് ( സൂര്യന്‍ )","ലൈല്‍ ( രാത്രി )","ളുഹാ ( പൂര്‍വ്വാഹ്നം )","ശര്‍ഹ് ( വിശാലമാക്കല്‍ )","തീന്‍ ( അത്തി )","അലഖ് ( ഭ്രൂണം )","ഖദ്ര്‍ ( നിര്‍ണയം )","ബയ്യിന ( വ്യക്തമായ തെളിവ് )","സല്‍സല ( പ്രകമ്പനം )","ആദിയാത് ( ഓടുന്നവ )","അല്‍ ഖാരിഅ ( ഭയങ്കര സംഭവം )","തകാഥുര്‍ (പെരുമ നടിക്കല്‍ )","അസ്വര്‍ ( കാലം )","ഹുമസ (കുത്തിപ്പറയുന്നവര്‍ )","ഫീല്‍ ( ആന )","ഖുറൈഷ്","മാഊന്‍ (  പരോപകാര വസ്തുക്കള്‍ )","കൌഥര്‍‍ ( ധാരാളം )","കാഫിറൂന്‍ ( സത്യനിഷേധികള്‍ )","നസ്ര്‍ ( സഹായം )","മസദ് (  ഈന്തപ്പനനാര് )","ഇഖ് ലാസ് ( നിഷ്കളങ്കത )","ഫലഖ് ( പുലരി )","നാസ് ( ജനങ്ങള്‍ )"]
for x in range(114):
    target.write("\\chapter{\\textmalayalam{%s}}\n" % (suraname[x]) )
    target.write("\\begin{Arabic}\n\\Huge{\\centerline{\\basmalah}}\\end{Arabic}\n")
    count=0
    while(count<surasize[x]):
        target.write("\\flushright{\\begin{Arabic}\n")
        target.write("\\quranayah[%d][%d]\n" %(x+1,count+1))
        target.write("\\end{Arabic}}\n")
        count=count+1
        ab=trans.readline()
        target.write("\\flushleft{\\begin{malayalam}\n")
        target.write(ab)
        target.write("\\end{malayalam}}\n")


target.close()


