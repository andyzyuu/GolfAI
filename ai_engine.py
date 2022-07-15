from storage_manager import StorageManager
import os
import important
import glob
import shutil
from pathlib import Path


sm = StorageManager()

def send_images_example(v1, v2):
    important.kmeans(v1,v2) # 1. calls the kmeans clustering code in important.py and picks up the key frames of the video 2. Creates coach and student folders of all of the frames of the correspondent videos 3. Fills vid1 and vid2 with key frames
    
    public_urls = []
    #get the list of file store in the vid1 and vid2 directories

    
    vid1 = os.listdir(r'C:\Users\bobby\Downloads\finafina\images\vid1') # Finds the directory of the filtered frames folder
    vid2 = os.listdir(r'C:\Users\bobby\Downloads\finafina\images\vid2') 
    vid3 = os.listdir(r'C:\Users\bobby\Downloads\finafina\images\highlighted_differences')



    # Get list of all files in a given directory sorted by name
    dir1_name = r'C:\Users\bobby\Downloads\finafina\images\vid1*.jpg'
    list_of_files1 = filter(os.path.isfile, glob.glob(dir1_name + '*')) # sorts vid1 frames by time
    list_of_files1 = sorted(list_of_files1, key = os.path.getmtime)
    dir2_name = r'C:\Users\bobby\Downloads\finafina\images\vid2*.jpg'
    # Get list of all files in a given directory sorted by name
    list_of_files2 = filter(os.path.isfile, glob.glob(dir2_name + '*')) # sorts vid2 frames by time 
    list_of_files2 = sorted(list_of_files2, key = os.path.getmtime)


    dir3_name = r'C:\Users\bobby\Downloads\finafina\images\highlighted_differences*.jpg'
    list_of_files3 = filter(os.path.isfile, glob.glob(dir3_name + '*'))
    list_of_files3 = sorted(list_of_files3, key = os.path.getmtime)


    counter1 = 1
    counter2 = 5
    counter3 = 9
    for i in range(len(vid1)):
        public_url1 = sm.upload_file(file_name=f'tennis/{vid1[i]}', local_path=f'images/vid1/{vid1[i]}')
        public_url2 = sm.upload_file(file_name=f'tennis/{vid2[i]}', local_path=f'images/vid2/{vid2[i]}')
        public_urls.append((public_url1,public_url2))
        
    
    for (file_path1, file_path2, file_path3) in zip(list_of_files1, list_of_files2, list_of_files3): # combined loop
        public_url1 = sm.upload_file(file_name = f'tennis/{counter1}' , local_path= file_path1) # uploads file to cloud with 2 parameters, name of new file (where it's going to go), and local path of the file (where we are getting it from on our computer)
        public_url2 = sm.upload_file(file_name = f'tennis/{counter2}' , local_path= file_path2) # uploads file to cloud with 2 parameters, name of new file (where it's going to go), and local path of the file (where we are getting it from on our computer)
        # public_url3 = sm.upload_file(file_name = f'tennis/{counter3}' , local_path= file_path3)
        counter1+=1
        counter2+=1
        counter3+=1
        public_urls.append((public_url1,public_url2)) # stores the two images (links to the cloud files), and stores in pairs 
    
    shutil.rmtree('coach') # deletes the coach folder
    shutil.rmtree('student') # deletes the student folder
    # #deletes all the files in vid1
    folder = 'images/vid1'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
    

    # #deletes all the files in vid2
    folder = 'images/vid2'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
    
    folder = 'images/highlighted_differences'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

            
    return public_urls

