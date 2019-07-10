import smtplib 
import os
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 
import base64
import cv2

# HTML based testing report
def imageTag(pathToImage):
    datauri = base64.b64encode(open(pathToImage, 'rb').read()).decode('utf-8')
    imgtag = "<td width='37.5%'><img src='data:image/png;base64,{0}'></td>".format(datauri)
    return imgtag

def totalDevices(mainDir):
    deviceCount = 0
    file = open(os.path.join(mainDir,r'deviceId.txt'),'r')
    for line in file:
        deviceCount+=1
    deviceCount-=2
    return deviceCount
    
def totalTestCase(resultsDir,deviceId):
    testCases = 0
    testPassed = 0
    resultFilePath = os.path.join(r"C:\Users\MAQUser\Desktop\scripts\start_execution\onebillion\results",deviceId,deviceId+'.txt')
    file = open(resultFilePath,'r')
    for line in file :
        val =line.split('\n') 
        if val[0] == "Pass" or val[0] == "Fail":
            testCases+=1
            if val[0] == "Pass":
                testPassed+=1
    return (testCases,testPassed)


if __name__ == "__main__":
    path = os.getcwd()
    print(path)
    mainDir = os.path.abspath(os.path.join(path, '..'))
    print(mainDir)
    totalTestCases = 94
    fromaddr = "ayushm@maqsoftware.com"
    toaddr = "ayushm@maqsoftware.com"
    deviceCount = totalDevices(mainDir)
    # instance of MIMEMultipart 
    msg = MIMEMultipart() 
    msg['From'] = fromaddr 
    msg['To'] = toaddr 
    msg['Subject'] = "[Automated Validation]: Testing Report"
    
    body = """
            <!DOCTYPE html>
            <html>
            <head>
            <meta http-equiv='Content-Type' content='text/html; charset=iso-8859-1'>
            <style TYPE='text/css'>
            table {
            border:0.25px solid #000000;
            border-left:0px;
            border-collapse:collapse;
            }
            #report-status
            {
            background-color:#008000;
            font-size:30px;
            }
            #dailyVerification
            {
            background-color:#4472C4;
            color:#FFFFFF;
            font-size :30px;
            }
            td {
            font-family: 'Segoe UI';
            font-size: 13px;
            border-top: 1px solid #000000;
            border-left: 1px solid #000000;
            padding-left: 5px;
            padding-bottom: 5px;
            padding-top: 5px;
            padding-right: 3px;
            }
            th {
            font-family: 'Segoe UI';
            font-size: 15px;
            border-top: 1px solid #000000;
            border-left: 1px solid #000000;
            padding-left: 5px;
            padding-bottom: 5px;
            padding-top: 5px;
            padding-right: 3px;
            }
            p {
            font-family: 'Segoe UI';
            font-size: 13px;
            }
          
            </style>
            </head>
            <body>
            <table width='100%' cellpadding='0' cellspacing='0' align='center'> <tbody>
            <tr>
            <td colspan="3" width='25%' style='color:white;' id='report-status' >Testing Report</td>
            <td colspan="2" width='75%'style='color:white;' id='report-status'>Local Automated Testing System</td></tr>
            <tr>
            <td colspan="3" width='25%' >Application</td>
            <td colspan="2" width='75%'>Onecourse</td></tr>
            <tr>
            <td colspan="3" width='25%' >No. of devices</td>
            <td colspan="2" width='75%'>"""+str(deviceCount)+"""</td></tr>
            <tr>
            <td colspan="3" width='25%' >Total Test cases</td>
            <td colspan="2" width='75%'>"""+str(totalTestCases)+"""</td></tr>
            </tbody></table>
            """
    resultsDir = os.path.join(r"C:\Users\MAQUser\Desktop\scripts\start_execution",r"\onebillion\results")
    expectedResultsDir = os.path.join(r"C:\Users\MAQUser\Desktop\scripts\start_execution",r"\onebillion\expected_result")
    print(resultsDir)
    print(expectedResultsDir)
    deviceNumber = 0
    file = open(os.path.join(mainDir,'devices.txt'),'r')
    iterater = iter(file)
    next(iterater)    
    prev = next(iterater)
    for line in iterater:
        deviceNumber+=1
        details = prev.split(':')
        id = details[0].split(" ")[0]
        testResult = totalTestCase(r"C:\Users\MAQUser\Desktop\scripts\start_execution\onebillion\results",id)
        accuracy = 100*testResult[1]/testResult[0]
        body +="""
            <table width='100%' cellpadding='1' cellspacing='1' align='center'> <tbody>
            <tr>
            <td colspan="3" width='25%' id='report-status'>Device """+str(deviceNumber)+"""</td>
            <td colspan="2" width='75%'></td></tr>
            <tr>
            <td colspan="3" width='25%' >Device id</td>
            <td colspan="2" width='75%'>"""+id+"""</td></tr>
             <tr>
            <td colspan="3" width='25%'>Device Details</td>
            <td colspan="2" width='75%'>"""+details[1]+" "+details[2]+"""</td></tr>
             <tr>
            <td colspan="3" width='25%'>Test passed/total</td>
            <td colspan="1" width='37.5%'>"""+str(testResult[1])+"""</td>
            <td colspan="1" width='37.5%'>"""+str(testResult[0])+"""</td></tr>
            <tr>
            <td colspan="3" width='25%'>Testing accuracy</td>
            <td colspan="2" width='75%'>"""+ str(accuracy) +"""%</td></tr>
            </tbody></table>
            <table border="1" width='100%' cellpadding='0' cellspacing='0' align='center' border=1> <tbody>
             <tr>
            <th width='3%' align ='center'><strong> # </strong></th>
            <th width='15%' align='center'><strong>Test Scenarios</strong></th>
            <th width='7%' align='center'><strong>Test Result</strong></th>
            <th width='37.5%' align='center'><strong>Actual Result</strong></th>
            <th width='37.5%' align='center'><strong>Expected Result</strong></th></tr>"""

        outputImages = os.path.join( r"C:\Users\MAQUser\Desktop\scripts\start_execution\onebillion\results",id,'outputs')
        imageCount = 0
        resultfile = open(os.path.join(r"C:\Users\MAQUser\Desktop\scripts\start_execution\onebillion\results",id,id+'.txt'),'r')
        iterater1 = iter(resultfile)
        flag = 0
        for value in iterater1:
            val = value.split('\n')[0]
            if val == 'Pass' or val == 'Fail' or val == 'Extraction':
                if val == 'Extraction':
                    flag = 1
                if flag == 1 and (val == 'Pass' or val == 'Fail'):
                    imageCount+=1
                    body +=""" 
                        <tr>
                        <td  width='3%' align ='center'> """+str(imageCount)+""" </td>
                        <td  width='15%' align='center'>-</td>"""
                    if val == "Pass":
                        body+="""
                            <td width='7%' align='center' style='background-color:#008000;'>   Pass  </td>"""
                    else:
                        body+="""
                            <td width='7%' align='center' style='background-color:#800000;'>   Fail  </td>"""
                    img = cv2.imread(outputImages+'\output_t'+str(imageCount)+'.png')
                    img = cv2.resize(img,( 350,300))
                    cv2.imwrite(outputImages+'\output_t'+str(imageCount)+'.png',img)
                    
                    img = cv2.imread(r"C:\Users\MAQUser\Desktop\scripts\start_execution\onebillion\expected_result"+'\output_t'+str(imageCount)+'.png')
                    img = cv2.resize(img,( 350,300))
                    cv2.imwrite(r"C:\Users\MAQUser\Desktop\scripts\start_execution\onebillion\expected_result"+'\output_t'+str(imageCount)+'.png',img)
                    
                    body+=imageTag(outputImages+'\output_t'+str(imageCount)+'.png')
                    body+=imageTag(r"C:\Users\MAQUser\Desktop\scripts\start_execution\onebillion\expected_result"+'\output_t'+str(imageCount)+'.png')+"</tr>"
            
        body+="""
            </tbody></table>
            </body>"""
        resultfile = open(os.path.join(r"C:\Users\MAQUser\Desktop\scripts\start_execution\onebillion\results",id,id+'.txt'),'r')
        iterater1 = iter(resultfile)
        for value in iterater1:
            val = value.split('\n')[0]
            if val == 'Pass' or val == 'Fail':
                imageCount+=1
                body +=""" 
                    <tr>
                    <td  width='3%' align ='center'> """+str(imageCount)+""" </td>
                    <td  width='15%' align='center'>-</td>"""
                if val == "Pass":
                    body+="""
                        <td width='7%' align='center' style='background-color:#008000;'>   Pass  </td>"""
                else:
                    body+="""
                        <td width='7%' align='center' style='background-color:#800000;'>   Fail  </td>"""
                img = cv2.imread(outputImages+'\output_t'+str(imageCount)+'.png')
                img = cv2.resize(img,( 500,349))
                cv2.imwrite(outputImages+'\output_t'+str(imageCount)+'.png',img)
                
                img = cv2.imread(r"C:\Users\MAQUser\Desktop\scripts\start_execution\onebillion\expected_result"+'\output_t'+str(imageCount)+'.png')
                img = cv2.resize(img,( 500,349))
                cv2.imwrite(r"C:\Users\MAQUser\Desktop\scripts\start_execution\onebillion\expected_result"+'\output_t'+str(imageCount)+'.png',img)
                
                body+=imageTag(outputImages+'\output_t'+str(imageCount)+'.png')
                body+=imageTag(r"C:\Users\MAQUser\Desktop\scripts\start_execution\onebillion\expected_result"+'\output_t'+str(imageCount)+'.png')+"</tr>"
            if val == 'Extraction':
                break
            
            body+="""
                </tbody></table>
                </body>"""
        prev = line


    msg.attach(MIMEText(body, 'html')) 
    # creates SMTP session 
    s = smtplib.SMTP('smtp.office365.com', 587) 
    print("loggedin") 
    # start TLS for security 
    s.starttls()
    s.ehlo() 
    print("loggedin") 
    # Authentication 
    s.login(fromaddr, "szskykzrmndgxpqx") 
    print("loggedin")
    # Converts the Multipart msg into a string 
    text = msg.as_string()
    s.sendmail(fromaddr, toaddr, text) 
    s.quit() 