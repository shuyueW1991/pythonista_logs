import os
import shutil


path_result = 'Result_renaming'
try:
    shutil.rmtree(path_result)
except:
    print('there is no path_result.')
    
os.mkdir(path_result)

path = "templates_b1_graphics_standards[169]"
dir_list = os.listdir(path)
dir_list_needed  = [i for i in dir_list if (not i.startswith('.DS'))]

# begins with number 0 or other number
idx = 0


for subdirectory in dir_list_needed:
    print('subdirectory ', subdirectory)
    ppt_list =  os.listdir(os.path.join(path, subdirectory))
    print('ppt_list', ppt_list)
    ppt_list_needed = [i for i in ppt_list if i.startswith('WS_')]
    print('ppt_list_needed', ppt_list_needed)

    for shit in ppt_list_needed:
        idx += 1
        dest = 'templates_part' + str(idx) + '.pptx'
        shutil.copy(os.path.join(path, subdirectory, shit), os.path.join(path_result, dest))



