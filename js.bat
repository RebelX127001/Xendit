:jayshare
	@echo off
	mode con: cols=65 lines=15
	color 8     
	Title JAY-share
	cd c:/jay-share
	cls
	::::call jayshareconnectwirelessly pagee
	goto jayshareconnectwirelessly
	::::create jayshareconnectwirelessly page
	:jayshareconnectwirelessly
		cls
		mode con: cols=66 lines=22
		call jaysharewelcome.bat
		echo ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
		echo Provide phone's IPAddress or put in;
		echo.
		echo ?) To get the IPAddress.
		echo 1) If you're already connected.
		echo c) To check connected devices.
		echo +++++++++++++
		echo J) For JAY^|
		echo +++++++++++++
		echo PS: Some IPAddresses change(Dynamic IPAddresses)
		echo     So you need to check for the IPAddress again if the data
		echo     connection was ressetted or the phone was restarted.
		echo ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
		echo.
		::::create a variable "ip" to save the IPAddress
		set /p ip="IPAddress: "
		if "%ip%"=="?" (
			goto jaysharegetip
			)
		if "%ip%"=="1" (
			goto jaysharepage
			)
		if "%ip%"=="J" (
			goto jayshareconnectjay
				)
			)
		if "%ip%"=="c" (
			goto jaysharecheckdevices
			)
		::::create connect function - to connect IPAddress
		:connect
			cls
			adb tcpip 5555
			cls
			echo ++++++++++++++++++++++++++++++
			adb connect %ip%:5555
			echo ++++++++++++++++++++++++++++++
			echo.
			echo Input 1 to proceed or "d" to disconnect the device.
			::::end connect function
			::::create a variable "web" to take input for navigation
			echo.
			set /p web=Put it in: 
			::::if input is 1 goto jaysharepage
			if "%web%"=="1" (
				goto jaysharepage
				)
			if "%web%"=="d" (
				goto jaysharedisconnect
				)
		::::create function to disconnect device
		:jaysharedisconnect
			cls
			adb disconnect %ip%:5555
			echo.
			Timeout 2
			goto jayshareconnectwirelessly
			
			::::create function to connect my personal phone using my static ipaddress
			:jayshareconnectjay
				cls
				adb tcpip 5555
				cls
				echo ++++++++++++++++++++++++++++++
				adb connect 192.168.43.1:5555
				echo ++++++++++++++++++++++++++++++
				echo Input 1 to proceed or "d" to disconnect the device.
				echo.
				echo ++++++++++
				set /p varb=Put it in: 
				::if input is 1 goto hackpage
				if "%varb%"=="1" goto jaysharepage
				if "%varb%"=="d" goto jaysharedisconnect
				::create function to disconnect device
				:jaysharedisconnect
					cls
					adb disconnect 192.168.43.1:5555
					echo.
					Timeout 2
					goto jayshareconnectwirelessly
		::::create function to get ip address
		:jaysharegetip
			cls
			mode con: cols=75 lines=20
			echo To get the IPAddress, the device has to be connected via a USB cable.
			Timeout 2
			echo +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
			adb shell ip route
			echo +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
			echo.
			echo Find and copy your IPAddress (Next to "src") and Put in "b" to go back.
			echo ++++++++++
			set /p chkip="Put it in: "
			echo.
			if "%chkip%"=="b" (
				goto jayshareconnectwirelessly
				)
		
		:jaysharecheckdevices
			Title Check Connected Devices
			cls
			@echo off
			echo ++++++++++++++++++++++++++
			echo Hi  %username%, welcome..
			echo ++++++++++++++++++++++++++
			adb devices
			echo Put in "1" to proceed to the jaysharepage or "b" to go back...
			echo Or copy and paste the device ID down below to disconnect.
			echo.
			echo ++++++++++
			set /p chkdev=Put it in: 
			if "%chkdev%"=="1" (
				goto jaysharepage
				)
			if "%chkdev%"=="b" (
				goto jayshareconnectwirelessly
				)
			:jaysharedisconnect
				cls
				adb disconnect %chkdev%
				echo.
				Timeout 2
				goto jayshareconnectwirelessly

	::::create JAYsharepage
	:jaysharepage
		cls
		Title JAY-share Page
		call jaysharewelcome.bat
		echo ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
		echo Select an Option OR "?" for a new user folder setup.
		echo ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
		echo 1) To Send Files
		echo 2) To Pull Files
		echo 3) To pick a specific device (if connected to multiple devices).
		echo ..) To go back
		echo.
		echo +++++++
		set /p intopt=Option: 
		if "%intopt%"=="1" (
			goto jaysharesend
			)
		if "%intopt%"=="2" (
			goto jaysharepull
			)
		if "%intopt%"=="3" (
			call jaysharepagemulti.bat
			)
		if "%intopt%"==".." (
			goto jayshareconnectwirelessly
			)
		if "%intopt%"=="?" (
			goto jaysharesetup
			)
			
		::::create function to setup folder structure on a new Android
		:jaysharesetup
			cls
			echo Please wait...
			::::create needed folder for android device
			adb shell mkdir sdcard/JAY-share
			adb shell mkdir sdcard/JAY-share/Images
			adb shell mkdir sdcard/JAY-share/Videos
			adb shell mkdir sdcard/JAY-share/Musics
			adb shell mkdir sdcard/JAY-share/Folders
			adb shell mkdir sdcard/JAY-share/Documents
			adb shell mkdir sdcard/JAY-share/Group
			pause
			::::create needed folders for pc
			mkdir "C:\JAY-share Downloads"
			mkdir "C:\JAY-share Downloads\Images"
			mkdir "C:\JAY-share Downloads\Videos"
			mkdir "C:\JAY-share Downloads\Musics"
			mkdir "C:\JAY-share Downloads\Folders"
			mkdir "C:\JAY-share Downloads\Documents"
			cls
			echo Done.
			Timeout 3
			cls
			goto jaysharepage
			
		::::create JAYsharesend page
		:jaysharesend
			cls
			Title JAY-share Send
			call jaysharewelcome.bat
			echo +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
			echo Select an Option or ".." to go back.
			echo +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
			echo 1) Send an Image
			echo 2) Send a Video
			echo 3) Send a Music
			echo 4) Send a Folder
			echo 5) Send a Document
			echo.
			echo +++++++
			set /p option2=Option: 
			if "%option2%"=="1" (
				goto jaysharesendimg
				)
			if "%option2%"=="2" (
				goto jaysharesendvideo
				)
			if "%option2%"=="3" (
				goto jaysharesendmusic
				)
			if "%option2%"=="4" (
				goto jaysharesendfolder
				)
			if "%option2%"=="5" (
				goto jaysharesenddocument
				)
			if "%option2%"==".." (
				goto jaysharepage
				)
			Timeout 2

			::::create function to send an image
			:jaysharesendimg
				cls
				echo Drag and Drop the Image-file here
				echo.
				echo ++++++++++
				set /p pictpath=Put it in: 
				cls
				adb push %pictpath% "/sdcard/JAY-share/Images"
				echo.
				echo ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
				echo Check directory "JAY-share/Images" on the device.			^|
				echo ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
				echo Put in ".." to go back.
				echo.
				echo ++++++++++
				set /p intaa=Put it in: 
				if "%intaa%"==".." (
					goto jaysharesend
					)

			::::create function to send a video
			:jaysharesendvideo
				cls
				echo Drag and Drop the Video-File here
				echo.
				echo ++++++++++
				set /p videopath=Put it in: 
				cls
				adb push %videopath% "/sdcard/JAY-share/Videos"
				echo.
				echo ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
				echo Check directory "JAY-share/Videos" on the device.			^|
				echo ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
				echo Put in ".." to go back.
				echo.
				echo ++++++++++
				set /p intbb=Put it in: 
				if "%intbb%"==".." (
					goto jaysharesend
					)

			::::create function to send a music
			:jaysharesendmusic
				cls
				echo Drag and Drop the Music-File here.
				echo.
				echo ++++++++++
				set /p musicpath=Put it in: 
				cls
				adb push %musicpath% "/sdcard/JAY-share/Musics"
				echo.
				echo ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
				echo Check directory "JAY-share/Musics" on the device.			^|
				echo ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
				echo Put in ".." to go back.
				echo.
				echo ++++++++++
				set /p intcc=Put it in: 
				if "%intcc%"==".." (
					goto jaysharesend
					)

			::::create function to a send a folder
			:jaysharesendfolder
				cls
				echo Drop and Drop the Folder here.
				echo.
				echo ++++++++++
				set /p fldrpath=Put it in: 
				cls
				adb push %fldrpath% "/sdcard/JAY-share/Folders"
				echo.
				echo +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
				echo Check directory "JAY-share/Folders" on the device.			 ^|
				echo +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
				echo Put in ".." to go back.
				echo.
				echo ++++++++++
				set /p intdd=Put it in: 
				if "%intdd%"==".." (
					goto jaysharesend
					)

			::::create function to a send a document
			:jaysharesenddocument
				cls
				echo Drag and Drop the Document-File here.
				echo.
				echo ++++++++++
				set /p docpath=Put it in: 
				cls
				adb push %docpath% "/sdcard/JAY-share/Documents"
				echo.
				echo +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
				echo Check directory "JAY-share/Documents" on the device.		   ^|
				echo +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
				echo Put in ".." to go back.
				echo.
				echo ++++++++++
				set /p intee=Put it in: 
				if "%intee%"==".." (
					goto jaysharesend
					)


		::::create JAYsharepull page
		:jaysharepull
			cls
			Title JAY-share Pull
			call jaysharewelcome.bat
			echo +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
			echo Select an Option or ".." to go back.
			echo +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
			echo 1) Pull an Image
			echo 2) Pull a Video
			echo 3) Pull a Music
			echo 4) Pull a Folder
			echo 5) Pull a Document
			echo.
			echo +++++++
			set /p option3=Option: 
			if "%option3%"=="1" (
				goto jaysharepullimg
				)
			if "%option3%"=="2" (
				goto jaysharepullvideo
				)
			if "%option3%"=="3" (
				goto jaysharepullmusic
				)
			if "%option3%"=="4" (
				goto jaysharepullfolder
				)
			if "%option3%"=="5" (
				goto jaysharepulldocument
				)
			if "%option3%"==".." (
				goto jaysharepage
				)


			::::create function to pull an image
			:jaysharepullimg
				cls
				echo Put in the Image-Path plus Image-Name to pull i.e "sdcard/JAY-share/imagename.png"
				echo Or ".." to go back.
				echo.
				echo ++++++++++
				set /p imagepath2=Put it in: 
				if "%imagepath2%"==".." (
					goto jaysharepull
					)
				cls
				adb pull "%imagepath2%" "C:/JAY-share Downloads/Images"
				echo.
				echo +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
				echo Check directory "C:/JAY-share Downloads/Images" on the PC.  ^|
				echo +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
				echo Put in ".." to go back.
				echo.
				echo ++++++++++
				set /p intta=Put it in: 
				if "%intta%"==".." (
					goto jaysharepullimg
					)

			::::create function to pull an video
			:jaysharepullvideo
				cls
				echo Put in the Video-Path plus Video-Name to pull i.e "sdcard/JAY-share/videoname.mp4"
				echo Or ".." to go back.
				echo.
				echo ++++++++++
				set /p videopath2=Put it in: 
				if "%videopath2%"==".." (
					goto jaysharepull
					)
				cls
				adb pull "%videopath2%" "C:/JAY-share Downloads/Videos"
				echo.
				echo +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
				echo Check directory "C:/JAY-share Downloads/Videos" on the PC.^|
				echo +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
				echo Put in ".." to go back.
				echo.
				echo ++++++++++
				set /p inttb=Put it in: 
				if "%inttb%"==".." (
					goto jaysharepullvideo
					)

			::::create functiono to pull a music
			:jaysharepullmusic
				cls
				echo Put in the Music-Path plus Music-Name to pull i.e "sdcard/JAY-share/musicname.mp3"
				echo Or ".." to go back.
				echo.
				echo ++++++++++
				set /p musicpath2=Put it in: 
				if "%musicpath2%"==".." (
					goto jaysharepull
					)
				cls
				adb pull "%musicpath2%" "C:/JAY-share Downloads/Musics"
				echo.
				echo +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
				echo Check directory "C:/JAY-share Downloads/Musics" on the PC.^|
				echo +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
				echo Put in ".." to go back.
				echo.
				echo ++++++++++
				set /p inttc=Put it in: 
				if "%inttc%"==".." (
					goto jaysharepullmusic
					)


			::::create function to pull a folder
			:jaysharepullfolder
				cls
				echo Put in the Folder-Path to pull i.e "sdcard/JAY-share"
				echo Or ".." to go back.
				echo.
				echo ++++++++++
				set /p fldrpath2=Put it in: 
				if "%fldrpath2%"==".." (
					goto jaysharepull
					)
				cls
				adb pull "%fldrpath2%" "C:/JAY-share Downloads/Folders"
				echo.
				echo ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
				echo Check directory "C:/JAY-share Downloads/Folders" on the PC.^|
				echo ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
				echo Put in ".." to go back.
				echo.
				echo ++++++++++
				set /p inttd=Put it in: 
				if "%inttd%"==".." (
					goto jaysharepullfolder
					)

			::::create function to pull document
			:jaysharepulldocument
				cls
				echo Put in the Document-Path plus Document-Name to pull i.e "sdcard/JAY-share/doc.txt"
				echo Or ".." to go back.
				echo.
				echo ++++++++++
				set /p docpath2=Put it in: 
				if "%docpath2%"==".." (
					goto jaysharepull
					)
				cls
				adb pull "%docpath2%" "C:/JAY-share Downloads/Documents"
				echo.
				echo ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
				echo Check directory "C:/JAY-share Downloads/Documents" on the PC.^|
				echo ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
				echo Put in ".." to go back.
				echo.
				echo ++++++++++
				set /p intte=Put it in: 
				if "%intte%"==".." (
					goto jaysharepulldocument
					)


	:exit
		echo.
		echo Bye...
		echo Do you really wanna leave tho? (y/n) Case sensitive
		echo.
		echo ++++++++++
		set /p web2=Put it in: 
		if "%web2%"=="n" (
			goto jaysharepage
			)
		if "%web2%"=="y" (
			goto leave
			)
	:leave
		@echo off
		exit
		::end exit function for other created functions
