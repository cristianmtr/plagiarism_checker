import os
import subprocess
# from glob import glob

samples_dir = "D:\\thesis_code\\model_fulldata1\\samples\\sessiontune45846_transposed"

training_set_dir = "D:\\data\\folkdataset\\3_transposed"

command_melodyshape = "java.exe -jar D:\\data\\thesis_model2\\plagiarism_checker\\melodyshape-1.4.jar -q %s -c %s -t 2 -a 2015-shapeh"

monophonize_cmd = "C:\\Anaconda3\\envs\\python2\\python.exe D:\\data\\thesis_model2\\plagiarism_checker\\monophonize\\p2m.py -i %s"

backup_dir = "D:\\data\\folkdataset\\3_transposed\\not mono\\"

# samples_files = glob(os.path.join(samples_dir, "*.mid"))

# training_set_files = glob(os.path.join)

done = False

while not done:
    # run, extract filename, monophonize, remove
    command = (command_melodyshape %
               (samples_dir, training_set_dir))
    p1 = subprocess.Popen(command.split(" "), stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    results = p1.communicate()
    if len(results) == 2:
        text = results[1]
        text = text.decode()
        if "Error" in text:
            # get filepath
            path = text.split("file")[1].split(": ")[0].strip().strip("'")
            print("found file %s" %path)
            # monophonize
            monophonize_cmd_path = monophonize_cmd %path
            p2 = subprocess.Popen(
                monophonize_cmd_path.split(" "), 
                stderr=subprocess.PIPE, 
                stdout=subprocess.PIPE
            )
            results_2 = p2.communicate()
            print(results_2)
            # rm
            fileid = path.split("\\")[-1]
            os.rename(path, os.path.join(backup_dir, fileid))
        else:
            done = True
            print('done!')



