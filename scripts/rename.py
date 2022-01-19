import os
import xlrd


data = xlrd.open_workbook('Sample_ID.xls') 

 
 
sheet = data.sheet_by_name("sheet_1")

mobile = sheet.col_values(0)
filelist = sheet.col_values(1)

n = 0
s = 0
for i in filelist:
		
    mulu = '/cluster/projects/nn9845k/transcriptomics/2_HeVRF02_He028/Filtered_Raw_Data/filtered_file/'
 
    if n== 0:
        filepath = ''
    else:
        filepath = mulu + i

        if os.path.exists(filepath):
   
            s+=1
            os.rename(filepath,  mulu + str(mobile[n]) + '.fastq.gz')
        else:
            print(filepath + ' no exists')
        
    n+=1

print('success'+ str(s))
