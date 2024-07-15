@echo off
echo.
echo      **               **            *******                   
echo     ****             /**           /**////**                  
echo    **//**   **   ** ******  ****** /**    /**  ******  **   **
echo   **  //** /**  /**///**/  **////**/**    /** **////**//** ** 
echo  **********/**  /**  /**  /**   /**/**    /**/**   /** //***  
echo /**//////**/**  /**  /**  /**   /**/**    ** /**   /**  **/** 
echo /**     /**//******  //** //****** /*******  //******  ** //**
echo //      //  //////    //   //////  ///////    //////  //   // 
echo.
                                                            
set /p ip_address=Enter an IP address: 

cd /d "C:\Users\Admin\Desktop\D0xAuto\Source"

python whois_lookup.py %ip_address%
pause
