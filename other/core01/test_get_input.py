import os  
import sys   
# import nlp_tools as nt  
  
urlstr = 'curl localhost:%d/brand/%s'  
  
if __name__=='__main__':  
      
    n_args = len(sys.argv)  
      
    line = sys.argv[2]  
      
    ecd_data = ''  
    for word in line.decode('utf-8'):  
        ecd_data += '%d_'%( ord(word) )  
      
    url_request = ''  
    if n_args == 2:  
        url_request = urlstr % ( 8080, ecd_data )  
    else:  
        url_request = urlstr % ( int(sys.argv[1]), ecd_data )  
          
    print line   
    print url_request   
  
    os.system( url_request )