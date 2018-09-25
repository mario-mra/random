import svgwrite
import os
import random

def rand_array(min_num, max_num, size):
    return [random.randint(min_num, max_num) for _ in range(size)]

def make_svg_texts(text, sep=' ', out_dir='./text_out', rand_rotate=[0, 0], font='Z003'):
    ctrl = 0
    while(os.path.exists(out_dir+str(ctrl))):
        ctrl += 1
    out_dir = out_dir+str(ctrl)+'/'
    os.makedirs(out_dir)
    
    text_array = text.split(sep)
    
    for i,j in enumerate(text_array):
        dwg = svgwrite.Drawing(out_dir+'out'+str(i)+'.svg')
        dwg.add(dwg.text(j, fill='black', rotate=rand_array(rand_rotate[0], rand_rotate[1], len(j))))
        dwg.save()

    return (out_dir, i)



if __name__ == '__main__':
    make_svg_texts("#PapaPitufo #Amadeame #Maravilla #ITI #ITIANOS #Python #C #C++ #Java #html #php #MeExplicó #Aranzazu #Sampersan #Moya #Polaski #PDF'S #Tirado #Cruasán #Franco #Nazi #BlackAcademy #Paquito #PayoJr #Chuwi #Chatarramovil #Copito #Gilperez #Rosendo #RasberryPi #Pisapapeles #Cubatas #Potenciómetro #Aguilucho #MeCageEnDios #TFG #Novelista #9,9 #Erasmus2018 #Jubilados #Gálvez #Surfero #SeñoritaReyes #Luisiño #QueTePeines #VivaFranco #CadaPerroSeLameSuCipote #ArrozGuineano #Nyquist #Coriolis #HastaLuegoMariCarmen #NedFlanders #Cabañas #Novato #Becario #Zenio #Matlab #Arduino")
