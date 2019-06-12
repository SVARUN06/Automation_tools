import difflib,filecmp
golden_folder = "C:\\Users\\svaru\\OneDrive\\Desktop\\Goldenconfig\\Golden\\"
config_folder = "C:\\Users\\svaru\\OneDrive\\Desktop\\Goldenconfig\\Version\\"
report_folder = "C:\\Users\\svaru\\OneDrive\\Desktop\\Goldenconfig\\report\\"

fname1 = golden_folder + "baseconfig.txt"
fname2 = config_folder + "new template_copy.txt"

print fname1
print fname2

f1 = open(fname1)
f2 = open(fname2)

lines1 = f1.readlines()
lines2 = f2.readlines()

if not filecmp.cmp(fname1, fname2):
        print("Golden Template Vs New Template are not equal")
        difference = difflib.HtmlDiff().make_file(lines1,lines2,f1,f2)
        difference_report = open('C:\\Users\\svaru\\OneDrive\\Desktop\\Goldenconfig\\report\\Audit_diff_template_1.html','w')
        difference_report.write(difference)
        difference_report.close()
        diff2 = difflib.context_diff(lines1,lines2)
        print("Cisco:Base_template Vs new_template Difference_HTML generated successfully")
        diff2_report = open('C:\\Users\\svaru\\OneDrive\\Desktop\\Goldenconfig\\report\\Audit_diff_template_1.csv','w')
        diff2_report.writelines(diff2)
        diff2_report.close()
        f1.close()
        f2.close()
        print("Cisco:Base_template Vs new_template Difference_CSV generated successfully")


#Run if templates are equal       
else:
    print("Golden Template Vs new template are equal: Device config are compared here")
    entry_file = golden_folder + "S1CW-E-709_A.txt"
    exit_file = config_folder + "S1CW-E-709_B.txt"
    print entry_file
    print exit_file
    print("Audit file HTML Generating.....0%")
    entry_file_lines = open(entry_file,'r').readlines()
    exit_file_lines = open(exit_file,'r').readlines()
    audit_diff = difflib.HtmlDiff().make_file(entry_file_lines,exit_file_lines,entry_file,exit_file)
    print("Audit file HTML Generating.....80%")
    difference_audit = open('C:\\Users\\svaru\\OneDrive\\Desktop\\Goldenconfig\\report\\audit_diff_device_1.html','w')
    difference_audit.write(audit_diff)
    print("Config Audit file HTML Generated 100%")
    difference_audit.close()
    diff3 = difflib.context_diff(entry_file_lines,exit_file_lines)
    print("Cisco:Golden_device_config Vs running_config Difference_HTML generated successfully")
    print("Audit difference CSV Generating.....0%")
    diff3_report = open('C:\\Users\\svaru\\OneDrive\\Desktop\\Goldenconfig\\report\\Audit_diff_device_1.csv','w')
    diff3_report.writelines(diff3)
    print("Audit difference CSV Generated.....100%")
    diff3_report.close()
    print("ASR:Entry_Config Vs Exit_config Diff_Report CSV generated successfully")
    

    

    


