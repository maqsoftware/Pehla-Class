import xlsxwriter
import cv2
import os
import datetime
import sys

# Excel report for testing
class reportGeneration:
    def __init__(self):
        # extract VBA function's bin file from functionsVBA.xlsm so that it can be used in generated report  
        os.system("python extractVBA.py functionsVBA.xlsm")
        self.totalTests = 93
        self.workbook = xlsxwriter.Workbook('testingReport.xlsm')
        self.workbook.add_vba_project('./vbaProject.bin')
        self.workbook.set_vba_name('THisWorkbook')
        self.mainHeadingFormat = self.workbook.add_format({
            'bold': 1,
            'font': 'Calibri',
            'size': 18})
        self.subHeadingFormat = self.workbook.add_format({
            'bold': 0.5,
            'font': 'Calibri',
            'size': 13})
        self.normalFormat = self.workbook.add_format({
            'font': 'Calibri',
            'size': 11})
        self.normalFormatMiddle = self.workbook.add_format({
            'font': 'Calibri',
            'size': 11})
        self.normalFormatMiddle.set_align('center')
        self.normalFormatMiddle.set_align('vcenter')
        self.normalcenterFormat = self.workbook.add_format({
            'font': 'Calibri',
            'size': 11,
            'align':'center'})
        self.normalcenterFormatHead = self.workbook.add_format({
            'font': 'Calibri',
            'border':1,
            'size': 11,
            'align':'center'})
        self.path = os.getcwd()
        self.mainDir = os.path.abspath(os.path.join(self.path, '..'))
        self.arg1 = sys.argv[1]
    def indexPagelabel(self):
        worksheet=self.workbook.add_worksheet('Index')
        worksheet.set_vba_name('first')
        worksheet.set_column(0,3, 18)
        worksheet.set_column(4,7, 7)
        worksheet.set_column(8,9, 15)
        worksheet.set_row(0,24)
        count = 10
        constant = 10
        worksheet.merge_range('A1:G1','Local Automated Testing System - Testing Report',self.mainHeadingFormat)
        worksheet.write('A2', 'Date and Time',self.normalFormat)
        worksheet.write('A3', 'Application',self.normalFormat)
        worksheet.write('A4', 'No. of devices',self.normalFormat)
        worksheet.write('A5', 'Total Test cases',self.normalFormat)
        worksheet.write('C2', 'Avg test pass',self.normalFormat)
        worksheet.write('C3', 'Avg testing accuracy',self.normalFormat)
        worksheet.write('C4', 'Avg manual accuracy',self.normalFormat)

        worksheet.write('A7', 'Summary:',self.subHeadingFormat)
        worksheet.write('A8', 'Sr no.',self.normalcenterFormatHead)
        worksheet.write('B8', 'Device name',self.normalcenterFormatHead)
        worksheet.write('C8', 'Passed tests',self.normalcenterFormatHead)
        worksheet.write('D8', 'Testing accuracy',self.normalcenterFormatHead)
        worksheet.merge_range('E8:H8','Manual analysis result',self.normalcenterFormatHead)
        worksheet.write('E9', 'T P',self.normalcenterFormatHead)
        worksheet.write('F9', 'T N',self.normalcenterFormatHead)
        worksheet.write('G9', 'F P',self.normalcenterFormatHead)
        worksheet.write('H9', 'F N',self.normalcenterFormatHead)
        worksheet.write('I8', 'Actual accuracy',self.normalcenterFormatHead)
        worksheet.write('J8', 'Comments',self.normalcenterFormatHead)
        # summary table   
        results = os.path.join(self.mainDir,self.arg1,'results')
        file = open(os.path.join(self.mainDir,'deviceId.txt'),'r')
        iterater = iter(file)
        next(iterater)
        next(iterater)
        
        for raw in iterater:
            countPass = 0
            countFail = 0
            id = raw.split('!')
            worksheet.write('A'+str(count),count-9,self.normalcenterFormat)
            worksheet.write('B'+str(count),'Device '+str(count-9),self.normalcenterFormat)
            resultfile = open(os.path.join(results,id[0],id[0]+'.txt'),'r')
            iterater1 = iter(resultfile)
            for value in iterater1:
                val = value.split('\n')
                if val[0] == 'Pass':
                    countPass+=1
                if val[0] == 'Fail':
                    countFail+=1
            
            worksheet.write('C'+str(count),countPass,self.normalcenterFormat)
            worksheet.write_formula('E'+str(count),'=\'Device '+ str(count-9)+'\'!C5',self.normalcenterFormat)
            worksheet.write_formula('F'+str(count),'=\'Device '+ str(count-9)+'\'!D5',self.normalcenterFormat)
            worksheet.write_formula('G'+str(count),'=\'Device '+ str(count-9)+'\'!C6',self.normalcenterFormat)
            worksheet.write_formula('H'+str(count),'=\'Device '+ str(count-9)+'\'!D6',self.normalcenterFormat)
            worksheet.write_formula('D'+str(count), '=100.00*C'+str(count)+'/'+str(self.totalTests),self.normalcenterFormat)
            count+=1
        # Header values 
        worksheet.write('B2',str(datetime.datetime.now().strftime("%Y-%m-%d, %H:%M:%S")),self.normalcenterFormat)
        worksheet.write('B5',93,self.normalcenterFormat)
        worksheet.write('B4',count-10,self.normalcenterFormat)
        worksheet.write_formula('D2','=if(B4>0,AVERAGE(C10:C'+str(count)+'),"NA")')
        worksheet.write_formula('D3','=if(B4>0,AVERAGE(D10:D'+str(count)+'),"NA")')
        # worksheet.write_formula('C6',)
     



    # create device sheets
    def device(self): 
        worksheet ={}
        results = os.path.join(self.mainDir,self.arg1,'results')
        file = open(os.path.join(self.mainDir,'devices.txt'),'r')
        iterater = iter(file)
        next(iterater)
        deviceCount = 0
        
        # Device sheets
        prev = next(iterater)
        # total  = 0
        # count = 10
        # worksheet[deviceCount].write_formula('C5','= For Count 1 To C3 if(D'+str(count)+' == "-",total,if(D'+str(count)+' == C'+str(count)+',total= total+1,total)) Next Count')

        for raw in iterater:
            resultTableIndex = 10
            worksheet[deviceCount] = self.workbook.add_worksheet('Device '+str(deviceCount+1))
            worksheet[deviceCount].set_column(0,1,25)
            worksheet[deviceCount].set_column(2,3,15)
            worksheet[deviceCount].set_column(6,6,25)
            details = prev.split(':')[0:3]
            id = details[0].split(' ')
            worksheet[deviceCount].write('A1','Device id')
            worksheet[deviceCount].write('B1',id[0])
            worksheet[deviceCount].write('A2','Device Details')
            worksheet[deviceCount].merge_range('B2:C2',details[1]+' '+details[2],self.normalFormat)
            worksheet[deviceCount].write('B2',details[1]+' '+details[2])
            worksheet[deviceCount].write('A3','Test passed/total')
            ######################### values ############### bottom next for loop
            worksheet[deviceCount].merge_range('A4:A6','Testing results analysis',self.normalFormatMiddle)
            worksheet[deviceCount].write('B4','Cases',self.normalcenterFormatHead)
            worksheet[deviceCount].write('B5','True',self.normalcenterFormatHead)
            worksheet[deviceCount].write('B6','False',self.normalcenterFormatHead)
            worksheet[deviceCount].write('C4','Positive',self.normalcenterFormatHead)
            worksheet[deviceCount].write('D4','Negative',self.normalcenterFormatHead)
            worksheet[deviceCount].write('A8','Testing results :',self.subHeadingFormat)

            # result table header
            worksheet[deviceCount].write('A9','Sr no.',self.normalcenterFormatHead)
            worksheet[deviceCount].write('B9','Test cases details',self.normalcenterFormatHead)
            worksheet[deviceCount].write('C9','Testing result',self.normalcenterFormatHead)
            worksheet[deviceCount].write('D9','Actual result',self.normalcenterFormatHead)
            worksheet[deviceCount].write('E9','Expected screen',self.normalcenterFormatHead)
            worksheet[deviceCount].write('F9','Actual screen',self.normalcenterFormatHead)
            worksheet[deviceCount].write('G9','Comments',self.normalcenterFormatHead)

            outputImages = os.path.join(results,id[0],'outputs')
            countPass = 0
            worksheet[deviceCount].set_column(4,5, 80)
            resultfile = open(os.path.join(results,id[0],id[0]+'.txt'),'r')
            iterater1 = iter(resultfile)
            flag = 0
            for value in iterater1:
                
                val = value.split('\n')[0]
                if val == 'Pass' or val == 'Fail' or val == 'Extraction':
                    if val == 'Extraction':
                        flag = 1
                    elif flag == 1:
                        if val == 'Pass':
                            countPass+=1 
                        worksheet[deviceCount].set_row(resultTableIndex-1,300)
                
                        # print(outputImages+'\output_t'+str(resultTableIndex-9)+'.png')
                        worksheet[deviceCount].write('A'+str(resultTableIndex),resultTableIndex-9,self.normalFormatMiddle)
                        worksheet[deviceCount].write('C'+str(resultTableIndex),val,self.normalFormatMiddle)
                        worksheet[deviceCount].write('D'+str(resultTableIndex),'-',self.normalFormatMiddle)
                        worksheet[deviceCount].data_validation('D'+str(resultTableIndex), {'validate': 'list',
                                  'source': ['-','Pass','Fail']})
                        
                        # expected result
                        img = cv2.imread(self.path+'\expected_result\output_t'+str(resultTableIndex-9)+'.png')
                        img = cv2.resize(img,( 564,399))
                        cv2.imwrite('expected_result\output_t'+str(resultTableIndex-9)+'.png',img)
                        
                        worksheet[deviceCount].insert_image('E'+str(resultTableIndex), 'expected_result\output_t'+str(resultTableIndex-9)+'.png',{'object_position': 1,'border':1,'x_offset': 1, 'y_offset': 1})
                        # actual result
                        img = cv2.imread(outputImages+'\output_t'+str(resultTableIndex-9)+'.png')
                        img = cv2.resize(img,( 564,399))
                        cv2.imwrite('base_images\Routput_'+str(deviceCount)+'t'+str(resultTableIndex-9)+'.png',img)
                        worksheet[deviceCount].insert_image('F'+str(resultTableIndex), 'base_images\Routput_'+str(deviceCount)+'t'+str(resultTableIndex-9)+'.png',{'object_position': 1,'border':1,'x_offset': 1, 'y_offset': 1})
                        resultTableIndex+=1

            resultfile = open(os.path.join(results,id[0],id[0]+'.txt'),'r')
            iterater1 = iter(resultfile) 
            for value in iterater1:
                val = value.split('\n')[0]
                if val == 'Pass' or val == 'Fail':
                    if val == 'Pass':
                        countPass+=1
                    worksheet[deviceCount].set_row(resultTableIndex-1,300)
                    
                    # print(outputImages+'\output_t'+str(resultTableIndex-9)+'.png')
                    worksheet[deviceCount].write('A'+str(resultTableIndex),resultTableIndex-9,self.normalFormatMiddle)
                    worksheet[deviceCount].write('C'+str(resultTableIndex),val,self.normalFormatMiddle)
                    worksheet[deviceCount].write('D'+str(resultTableIndex),'-',self.normalFormatMiddle)
                    worksheet[deviceCount].data_validation('D'+str(resultTableIndex), {'validate': 'list','source': ['-','Pass','Fail']})
                    # expected result
                    img = cv2.imread(self.path+'\expected_result\output_t'+str(resultTableIndex-9)+'.png')
                    img = cv2.resize(img,( 564,399))
                    cv2.imwrite('expected_result\output_t'+str(resultTableIndex-9)+'.png',img)
                    
                    worksheet[deviceCount].insert_image('E'+str(resultTableIndex), 'expected_result\output_t'+str(resultTableIndex-9)+'.png',{'object_position': 1,'border':1,'x_offset': 1, 'y_offset': 1})
                    # actual result
                    img = cv2.imread(outputImages+'\output_t'+str(resultTableIndex-9)+'.png')
                    img = cv2.resize(img,( 564,399))
                    cv2.imwrite('base_images\Routput_'+str(deviceCount)+'t'+str(resultTableIndex-9)+'.png',img)
                    worksheet[deviceCount].insert_image('F'+str(resultTableIndex), 'base_images\Routput_'+str(deviceCount)+'t'+str(resultTableIndex-9)+'.png',{'object_position': 1,'border':1,'x_offset': 1, 'y_offset': 1})
                    resultTableIndex+=1
                elif val == 'Extraction':
                    break
            worksheet[deviceCount].write('B3',countPass,self.normalcenterFormat)
            worksheet[deviceCount].write('C3',93,self.normalcenterFormat)
            # worksheet[deviceCount].write_formula('C5','=module1.truePositive()')
            # worksheet[deviceCount].write_formula('C6','=module1.falsePositive()')
            # worksheet[deviceCount].write_formula('D5','=module1.trueNegative()')
            # worksheet[deviceCount].write_formula('D6','=module1.falseNegative()')
            deviceCount+=1
            prev = raw
            count = 10
            
            




    


if __name__ == "__main__":
    generationInstance = reportGeneration()
    # Add VBA Functions
    generationInstance.indexPagelabel()
    generationInstance.device()
    # closing sheet
    generationInstance.workbook.close()




