def tulosta_inventaario(esineet):
    if not esineet:
        print ('Sinulla ei ole mukana mitään.')
    else :
        print('Sinulla on mukana:')
        for i in esineet:
            print('- ' + i.capitalize())