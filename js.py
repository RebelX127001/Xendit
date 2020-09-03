"""
!/usr/bin/env python3
__AUTHOR = "JIMOH IDRIS OLANSHILE"
__DATE = "MAR 2019 - till date."
__TECHNOLOGIES = "PY, adb, Batch Programming"
"""
import os as gd, time, subprocess as sp, jswelcome
def js():
	#create jspage
	def jspage():
		def jsgroupsend():
			def jsdouble():
				def doubledo():
					gd.system("cls")
					print ("Drag and Drop the file or Folder to send to all selected devices.")
					print ("+" * 8)
					fpath = input("File: ")
					print ("+" * 8)
					gd.system("""start cmd.exe /k "adb -s " + serial0 + "push " fpath /sdcard && Timeout 3 && exit" """)
					gd.system("""adb -s " + serial2 + "push " fpath "/sdcard" """)
					print (" ")
					print ("+" * 62)
					print ("""Check directory "J-share/J-share Group" on both devices.|""")
					print ("+" * 62)
					gd.system("echo.")
					print ("""Put in ".." to go back.""")
					print ("""Or "O" to open the folder.""")
					print (" ")
					print ("+" * 10)
					numbb = input ("Put it in: ") 
					if (numbb == ".."):
						jsgroupsend()
					elif (intta == "O") or (intte == "o"):
						gd.system("""start. "C:/J-share-Downloads/Images" """)
						jsgroupsend()
					else:
						jsgroupsend()
						
				gd.system("cls")
				print ("+" * 30)
				sp.call("adb devices")
				print ("+" * 41)
				print ("Copy and Paste first device serial number.")
				serial0 = input("Serial 1: ") 
				print ("+" * 41)
				print ("Copy and Paste Second device serial number.")
				serial2 = input("Serial 2: ") 
				doubledo()
				
			def jstriple():
				def tripledo():
					gd.system("cls")
					print ("Drag and Drop the file or Folder to send to all selected devices.")
					print ("+" * 8)
					fpath2 = input("File: ")
					print ("+" * 8)
					sp.call("""start cmd.exe /k "adb -s serial0 push fpath "/sdcard" && Timeout 3 && exit """)
					sp.call("""start cmd.exe /k "adb -s serial2 push fpath "/sdcard" && Timeout 3 && exit """)
					sp.call("""adb -s serial3 push fpath "/sdcard" """)
					print (" ")
					print ("+" * 60)
					print ("""Check directory "J-share/J-share Group" on the device.|""")
					print ("+" * 60)
					gd.system("echo.")
					print ("""Put in ".." to go back.""")
					print ("""Or "O" to open the folder.""")
					print (" ")
					print ("+" * 10)
					numbb2 = input("Put it in: ")
					if (numbb2 == ".."):
						jsgroupsend()
					elif (intta == "O") or (intte == "o"):
						gd.system("""start. "C:/J-share-Downloads/Images" """)
						jsgroupsend()
					else:
						jsgroupsend()
						
				gd.system("cls")
				print ("+" * 41)
				sp.call("adb devices")
				print ("+" * 41)
				print ("Copy and Paste First device serial number.")
				serial0 = input("Serial 1: ") 
				print ("+" * 41)
				print ("Copy and Paste Second device serial number.")
				serial2 = input("Serial 2: ")
				print ("+" * 41)
				print ("Copy and Paste Third device serial number.")
				serial3 = input("Serial 3: ")
				tripledo()
			
			
			gd.system("cls")
			gd.system("Title J-share Group Send")
			print ("+" * 26)
			gd.system("echo Hi  %username%, welcome..")
			print ("+" * 26)
			sp.call("""adb devices""")
			print ("+" * 38)
			print ("How many devices are you connected to?")
			print ("+" * 7)
			howmany = input("Put it in: ") 
			if (howmany == "2"):
				jsdouble()
			if (howmany == "3"):
				jstriple()
				
		##########J-share MULTI##########
		#create J-share-MULTI
		def jsmulti():
			#create function to log serial number to enable multiple devices
			def jsserialpage():
				#create jspagemulti
				def jspagemulti():
					#create jspull page
					def jspull():
						#create function to pull an image
						def jspullimg():
							gd.system("cls")
							print ("""Put in the Image-Path plus Image-Name to pull i.e "sdcard/J-share/imagename.png" """)
							print ("""Or ".." to go back.""")
							print ("")
							print ("+" * 10)
							imagepath2 = input ("Put it in: ")
							if (imagepath2 == ".."):
								jspull()
							gd.system("cls")
							sp.call("adb -s " + serialno + " pull " + imagepath2 + " C:/J-share-Downloads/Images")
							print ("")
							print ("+" * 69)
							print ("""Check directory "C:/J-share-Downloads/Images" on the PC.^|""")
							print ("+" * 69)
							gd.system("echo.")
							print ("""Put in ".." to go back.""")
							print ("""Or "O" to open the folder.""")
							print ("")
							print ("+" * 10)
							intta = input ("Put it in: ")
							if (intta == ".."):
								jspullimg()
							elif (intta == "O") or (intte == "o"):
								gd.system("""start. "C:/J-share-Downloads/Images" """)
								jspullimg()
							else:
								jspullimg()

						#create function to pull an video
						def jspullvideo():
							gd.system("cls")
							print ("""Put in the Video-Path plus Video-Name to pull i.e "sdcard/J-share/videoname.mp4 " """)
							print ("""Or ".." to go back.""")
							print ("")
							print ("+" * 10)
							videopath2 = input ("Put it in: ")
							if (videopath2 == ".."):
								jspull()
							gd.system("cls")
							sp.call("adb -s " + serialno + " pull " + videopath2 + " C:/J-share-Downloads/Videos")
							print ("")
							print ("+" * 69)
							print ("""Check directory "C:/J-share-Downloads/Videos" on the PC.^|""")
							print ("+" * 69)
							gd.system("echo.")
							print ("""Put in ".." to go back.""")
							print ("""Or "O" to open the folder.""")
							print ("")
							print ("+" * 10)
							inttb = input ("Put it in: ")
							if (inttb == ".."):
								jspullvideo()
							elif (intta == "O") or (intte == "o"):
								gd.system("""start. "C:/J-share-Downloads/Videos" """)
								jspullvideo()
							else:
								jspullvideo()

						#create function to pull a music
						def jspullmusic():
							gd.system("cls")
							print ("""Put in the Music-Path plus Music-Name to pull i.e "sdcard/J-share/musicname.mp3" """)
							print ("""Or ".." to go back.""")
							print ("")
							print ("+" * 10)
							musicpath2 = input ("Put it in: ")
							if (musicpath2 == ".."):
								jspull()
							gd.system("cls")
							sp.call("adb -s " + serialno + " pull " + musicpath2 + " C:/J-share-Downloads/Musics")
							print ("")
							print ("+" * 69)
							print ("""Check directory "C:/J-share-Downloads/Musics" on the PC.^|""")
							print ("+" * 69)
							gd.system("echo.")
							print ("""Put in ".." to go back.""")
							print ("""Or "O" to open the folder.""")
							print ("")
							print ("+" * 10)
							inttc = input ("Put it in: ")
							if (inttc == ".."):
								jspullmusic()
							elif (intta == "O") or (intte == "o"):
								gd.system("""start. "C:/J-share-Downloads/Music" """)
								jspullmusic()
							else:
								jspullmusic()
								


						#create function to pull a folder
						def jspullfolder():
							gd.system("cls")
							print ("""Put in the Folder-Path to pull i.e "sdcard/J-share" """)
							print ("""Or ".." to go back.""")
							print ("")
							print ("+" * 10)
							fldrpath2 = input ("Put it in: ")
							if (fldrpath2 == ".."):
								jspull()
							gd.system("cls")
							sp.call("adb -s " + serialno + " pull " + fldrpath2 + " C:/J-share-Downloads/Folders")
							print ("")
							print ("+" * 70)
							print ("""Check directory "C:/J-share-Downloads/Folders" on the PC.^|""")
							print ("+" * 70)
							gd.system("echo.")
							print ("""Put in ".." to go back.""")
							print ("""Or "O" to open the folder.""")
							print ("")
							print ("+" * 10)
							inttd = input ("Put it in: ")
							if (inttd == ".."):
								jspullfolder()
							elif (intta == "O") or (intte == "o"):
								gd.system("""start. "C:/J-share-Downloads/Images" """)
								jspullfolder()
							else:
								jspullfolder()

						#create function to pull document
						def jspulldocument():
							gd.system("cls")
							print ("""Put in the Document-Path plus Document-Name to pull i.e "sdcard/J-share/doc.txt" """)
							print ("""Or ".." to go back.""")
							print ("")
							print ("+" * 10)
							docpath2 = input ("Put it in: ")
							if (docpath2 == ".."):
								jspull()
							gd.system("cls")
							sp.call("adb -s " + serialno + " pull " + docpath2 + " C:/J-share-Downloads/Documents")
							print ("")
							print ("+" * 72)
							print ("""Check directory "C:/J-share-Downloads/Documents" on the PC.^|""")
							print ("+" * 72)
							gd.system("echo.")
							print ("""Put in ".." to go back.""")
							print ("""Or "O" to open the folder.""")
							print ("")
							print ("+" * 10)
							intte = input ("Put it in: ")
							if (intte == ".."):
								jspulldocument()
							elif (intta == "O") or (intte == "o"):
								gd.system("""start. "C:/J-share-Downloads/Images" """)
								jspulldocument()
							else:
								jspulldocument()
								
								
						gd.system("cls")
						gd.system("Title J-share Pull")
						jswelcome.welcome()
						print ("+" * 65)
						print ("""Select an Option or ".." to go back.""")
						print ("+" * 65)
						print ("1) Pull an Image")
						print ("2) Pull a Video")
						print ("3) Pull a Music")
						print ("4) Pull a Folder")
						print ("5) Pull a Document")
						print ("")
						print ("+" * 7)
						option3 = input ("Option: ")
						if (option3 == "1"):
							jspullimg()
						elif (option3 == "2"):
							jspullvideo()
						elif (option3 == "3"):
							jspullmusic()
						elif (option3 == "4"):
							jspullfolder()
						elif (option3 == "5"):
							jspulldocument()
						elif (option3 == ".."):
							jspagemulti()
						else:
							jspull()
							
					#create jssend page
					def jssend():
						#create function to send an image
						def jssendimg():
							gd.system("cls")
							print ("Drag and Drop the Image-file here")
							print ("")
							print ("+" * 10)
							pictpath = input ("Put it in: ")
							gd.system("cls")
							sp.call("adb -s " + serialno + " push " + pictpath + " /sdcard/J-share/Images")
							print ("")
							print ("+" * 60)
							print ("""Check directory "J-share/Images" on the device.	   ^|""")
							print ("+" * 60)
							print ("""Put in ".." to go back.""")
							print ("")
							print ("+" * 10)
							intaa = input ("Put it in: ")
							if (intaa == ".."):
								jssend()
								

						#create function to send a video
						def jssendvideo():
							gd.system("cls")
							print ("Drag and Drop the Video-File here")
							print ("")
							print ("+" * 10)
							videopath = input ("Put it in: ")
							gd.system("cls")
							sp.call("adb -s " + serialno + " push " + videopath + " /sdcard/J-share/Videos")
							print ("")
							print ("+" * 60)
							print ("""Check directory "J-share/Videos" on the device.	   ^|""")
							print ("+" * 60)
							print ("""Put in ".." to go back.""")
							print ("")
							print ("+" * 10)
							intbb = input ("Put it in: ")
							if (intbb == ".."):
								jssend()
								

						#create function to send a music
						def jssendmusic():
							gd.system("cls")
							print ("Drag and Drop the Music-File here.")
							print ("")
							print ("+" * 10)
							musicpath = input  ("Put it in: ")
							gd.system("cls")
							sp.call("adb -s " + serialno + " push " + musicpath + " /sdcard/J-share/Musics")
							print ("")
							print ("+" * 60)
							print ("""Check directory "J-share/Musics" on the device.	   ^|""")
							print ("+" * 60)
							print ("""Put in ".." to go back.""")
							print ("")
							print ("+" * 10)
							intcc = input ("Put it in: ")
							if (intcc == ".."):
								jssend()
								

						#create function to a send a folder
						def jssendfolder():
							gd.system("cls")
							print ("Drop and Drop the Folder here.")
							print ("""Or ".." to go back""")
							print ("")
							print ("+" * 10)
							fldrpath = input ("Put it in: ")
							if (fldrpath == ".."):
								jssend()
							gd.system("cls")
							sp.call("adb -s " + serialno + " push " + fldrpath + " /sdcard/J-share/Folders")
							print ("")
							print ("+" * 61)
							print ("""Check directory "J-share/Folders" on the device.    ^|""")
							print ("+" * 61)
							print ("""Put in ".." to go back.""")
							print ("")
							print ("+" * 10)
							intdd = input ("Put it in: ")
							if (intdd == ".."):
								jssend()
								

						#create function to a send a document
						def jssenddocument():
							gd.system("cls")
							print (" Drag and Drop the Document-File here.")
							print ("""Or ".." to go back""")
							print ("")
							print ("+" * 10)
							docpath = input ("Put it in: ")
							if (docpath == ".."):
								jssend()
							gd.system("cls")
							sp.call("adb -s "+ serialno + " push " + docpath + " /sdcard/J-share/Documents")
							print ("")
							print ("+" * 63)
							print ("""Check directory "J-share/Documents" on the device.    ^|""")
							print ("+" * 63)
							print ("""Put in ".." to go back.""")
							print ("")
							print ("+" * 10)
							intee = input ("Put it in: ")
							if (intee == ".."):
								jssend()
								

						gd.system("cls")
						gd.system("Title J-share Send")
						jswelcome.welcome
						print ("+" * 65)
						print ("""Select an Option or ".." to go back.""")
						print ("+" * 65)
						print ("1) Send an Image")
						print ("2) Send a Video")
						print ("3) Send a Music")
						print ("4) Send a Folder")
						print ("5) Send a Document")
						print ("")
						print ("+" * 7)
						option2 = input ("Option: ")
						if (option2 == "1"):
							jssendimg()
						elif (option2 == "2"):
							jssendvideo()
						elif (option2 == "3"):
							jssendmusic()
						elif (option2 == "4"):
							jssendfolder()
						elif (option2 == "5"):
						
							jssenddocument()
						elif (option2 == ".."):
							jspagemulti()
							
							
					#create function to setup folder structure on a new Android
					def jssetup():
						gd.system("cls")
						print ("Please wait...")
						#create needed folder for android device
						sp.call("adb -s " + serialno + " shell mkdir sdcard/J-share")
						sp.call("adb -s " + serialno + " shell mkdir sdcard/J-share/Images")
						sp.call("adb -s " + serialno + " shell mkdir sdcard/J-share/Videos")
						sp.call("adb -s " + serialno + " shell mkdir sdcard/J-share/Musics")
						sp.call("adb -s " + serialno + " shell mkdir sdcard/J-share/Folders")
						sp.call("adb -s " + serialno + " shell mkdir sdcard/J-share/Documents")
						#create needed folders for pc
						gd.mkdir("C:\J-share-Downloads")
						gd.mkdir("C:\J-share-Downloads\Images")
						gd.mkdir("C:\J-share-Downloads\Videos")
						gd.mkdir("C:\J-share-Downloads\Musics")
						gd.mkdir("C:\J-share-Downloads\Folders")
						gd.mkdir("C:\J-share-Downloads\Documents")
						gd.system("cls")
						print ("Done.")
						time.sleep(3)
						gd.system("cls")
						jspagemulti()
						
						
					gd.system("cls")
					gd.system("mode con: cols=71 lines=20")
					jswelcome.welcome()
					print ("+" * 64)
					jswelcome.helloMulti()
					print ("""Select an Option OR "?" for a new user folder setup.""")
					print ("+" * 64)
					print ("1) To Send Files")
					print ("2) To Pull Files")
					print ("..) To go back")
					print ("")
					print ("+" * 7)
					intopt = input ("Option: ")
					if (intopt == "1"):
						jssend()
					elif (intopt == "2"):
						jspull()
					elif (intopt == ".."):
						jsserialpage()
					elif (intopt == "?"):
						jssetup()
					else:
						jspagemulti()
						
				gd.system("cls")
				print ("+" * 39)
				sp.call("adb devices")
				print ("+" * 39)
				print ("Copy and paste the serial number of the device you would like to use.")
				print ("""Or ".." to go back to J-share SINGLE""")
				print ("")
				print ("+" * 7)
				serialno = input ("Option: ")
				if (serialno == ".."):
					js()
				else:
					print ("")
					print ("+" * 65)
					print ("Done! You will now be directed to the multiple devices platform.^|")
					print ("+" * 65)
					time.sleep(2)
					jspagemulti()
				
			gd.system("color 8")
			gd.system("Title J-share-MULTI")
			gd.chdir("c:/J-share")
			gd.system("cls")
			#call jsserialpage pagee
			jsserialpage()
		##########J-share MULTI##########
		#create jspull page
		def jspull():
			#create function to pull an image
			def jspullimg():
				gd.system("cls")
				print ("""Put in the Image-Path plus Image-Name to pull i.e "sdcard/J-share/imagename.png" """)
				print ("""Or ".." to go back.""")
				print ("")
				print ("+" * 10)
				imagepath2 = input ("Put it in: ")
				if (imagepath2 == ".."):
					jspull()
				gd.system("cls")
				sp.call("adb pull " + imagepath2 + " C:/J-share-Downloads/Images")
				print ("")
				print ("+" * 65)
				print ("""Check directory "C:/J-share-Downloads/Images" on the PC.^|""")
				print ("+" * 65)
				gd.system("echo.")
				print ("""Put in ".." to go back.""")
				print ("""Or "O" to open the folder.""")
				print ("")
				print ("+" * 10)
				intta = input ("Put it in: ")
				if (intta == ".."):
					jspullimg()
				elif (intta == "O") or (intte == "o"):
					gd.system("""start. "C:/J-share-Downloads/Images" """)
					jspullimg()
				else:
					jspullimg()
					

			#create function to pull an video
			def jspullvideo():
				gd.system("cls")
				print ("""Put in the Video-Path plus Video-Name to pull i.e "sdcard/J-share/videoname.mp4" """)
				print ("""Or ".." to go back.""")
				print ("")
				print ("+" * 10)
				videopath2 = input ("Put it in: ")
				if (videopath2 == ".."):
					jspull()
				gd.system("cls")
				sp.call("adb pull " + videopath2 + " C:/J-share-Downloads/Videos")
				print ("")
				print ("+" * 69)
				print ("""Check directory "C:/J-share-Downloads/Videos" on the PC.^|""")
				print ("+" * 69)
				print ("""Put in ".." to go back.""")
				print ("""Or "O" to open the folder.""")
				print ("")
				print ("+" * 10)
				inttb = input ("Put it in: ")
				if (inttb == ".."):
					jspullvideo()
				elif (inttb == "O") or (inttb == "o"):
					gd.system("""start. "C:/J-share-Downloads/Videos" """)
					jspullvideo()
				else:
					jspullvideo()

			#create functiono to pull a music
			def jspullmusic():
				gd.system("cls")
				print ("""Put in the Music-Path plus Music-Name to pull i.e "sdcard/J-share/musicname.mp3" """)
				print ("""Or ".." to go back.""")
				print ("")
				print ("+" * 10)
				musicpath2 = input ("Put it in: ")
				if (musicpath2 == ".."):
					jspull()
					
				gd.system("cls")
				sp.call("adb pull " + musicpath2 + " C:/J-share-Downloads/Musics")
				print ("")
				print ("+" * 69)
				print ("""Check directory "C:/J-share-Downloads/Musics" on the PC.^|""")
				print ("+" * 69)
				gd.system("echo.")
				print ("""Put in ".." to go back.""")
				print ("""Or "O" to open the folder.""")
				print ("")
				print ("+" * 10)
				inttc = input ("Put it in: ")
				if (inttc == ".."):
					jspullmusic()
				elif (inttb == "O") or (intte == "o"):
					gd.system("""start. "C:/J-share-Downloads/Musics" """)
					jspullmusic()
				else:
					jspullmusic()
			#create function to pull a folder
			def jspullfolder():
				gd.system("cls")
				print ("""Put in the Folder-Path to pull i.e "sdcard/J-share" """)
				print ("""Or ".." to go back.""")
				print ("")
				print ("+" * 10)
				fldrpath2 = input ("Put it in: ")
				if (fldrpath2 == ".."):
					jspull()
					
				gd.system("cls")
				sp.call("adb pull " + fldrpath2 + " C:/J-share-Downloads/Folders")
				print ("")
				print ("+" * 70)
				print ("""Check directory "C:/J-share-Downloads/Folders" on the PC.^|""")
				print ("+" * 70)
				gd.system("echo.")
				print ("""Put in ".." to go back.""")
				print ("""Or "O" to open the folder.""")
				print ("")
				print ("+" * 10)
				inttd = input ("Put it in: ")
				if (inttd == ".."):
					jspullfolder()
				elif (inttd == "O") or (intte == "o"):
					gd.system("""start. "C:/J-share-Downloads/Folders" """)
					jspullfolder()
				else:
					jspullfolder()

			#create function to pull document
			def jspulldocument():
				gd.system("cls")
				print ("""Put in the Document-Path plus Document-Name to pull i.e "sdcard/J-share/doc.txt" """)
				print ("""Or ".." to go back.""")
				print ("")
				print ("+" * 10)
				docpath2 = input ("Put it in: ")
				if (docpath2 == ".."):
					jspull()
					
				gd.system("cls")
				sp.call("adb pull " + docpath2 + " C:/J-share-Downloads/Documents")
				print ("")
				print ("+" * 66)
				print ("""Check directory "C:/J-share-Downloads/Documents" on the PC.^|" """)
				print ("+" * 66)
				gd.system("echo.")
				print ("""Put in ".." to go back.""")
				print ("""Or "O" to open the folder.""")
				print ("")
				print ("+" * 10)
				intte = input ("Put it in: ")
				if (intte == ".."):
					jspulldocument()
				elif (intte == "O") or (intte == "o"):
					gd.chdir("C:\J-share-Downloads\Documents")
					gd.system("start.")
					jspulldocument()
				else:
					jspulldocument()
					
			gd.system("cls")
			gd.system("Title J-share Pull")
			jswelcome.welcome()
			print ("+" * 65)
			print ("""Select an Option or ".." to go back.""")
			print ("+" * 65)
			print ("1) Pull an Image")
			print ("2) Pull a Video")
			print ("3) Pull a Music")
			print ("4) Pull a Folder")
			print ("5) Pull a Document")
			print ("")
			print ("+" * 7)
			option3 = input ("Option: ")
			if (option3 == "1"):
				jspullimg()
			elif (option3 =="2"):
				jspullvideo()
			elif (option3 == "3"):
				jspullmusic()
			elif (option3 == "4"):
				jspullfolder()
			elif (option3 == "5"):
				jspulldocument()
			elif (option3 == ".."):
				jspage()
			else:
				jspull()
				
		#create jssend page
		def jssend():
			#create function to send an image
			def jssendimg():
				gd.system("cls")
				print ("Drag and Drop the Image-file here")
				print ("""Or ".." to go back""")
				print ("")
				print ("+" * 10)
				pictpath = input ("Put it in: ")
				if (pictpath == ".."):
					jssend()
				gd.system("cls")
				sp.call("adb push " + pictpath + " /sdcard/J-share/Images")
				print ("")
				print ("+" * 60)
				print ("""Check directory "J-share/Images" on the device.	   ^|""")
				print ("+" * 60)
				print ("""Put in ".." to go back.""")
				print ("")
				print ("+" * 10)
				intaa = input ("Put it in: ")
				if (intaa == ".."):
					jssendimg()
					
			#create function to send a video
			def jssendvideo():
				gd.system("cls")
				print ("Drag and Drop the Video-File here")
				print ("""Or ".." to go back """)
				print ("")
				print ("+" * 10)
				videopath = input ("Put it in: ")
				if (videopath == ".."):
					jssend()
				gd.system("cls")
				sp.call("adb push " + videopath + " /sdcard/J-share/Videos")
				print ("")
				print ("+" * 60)
				print ("""Check directory "J-share/Videos" on the device.	        ^|""")
				print ("+" * 60)
				print ("""Put in ".." to go back.""")
				print ("")
				print ("+" * 10)
				intbb = input ("Put it in: ")
				if (intbb == ".."):
					jssendvideo()

			#create function to send a music
			def jssendmusic():
				gd.system("cls")
				print ("Drag and Drop the Music-File here.")
				print ("""Or ".." to go back""")
				print ("")
				print ("+" * 10)
				musicpath = input ("Put it in: ")
				if (musicpath == ".."):
					jssend()
				gd.system("cls")
				sp.call("adb push " + musicpath + " /sdcard/J-share/Musics")
				print ("")
				print ("+" * 60)
				print ("""Check directory "J-share/Musics" on the device.         ^|""")
				print ("+" * 60)
				print ("""Put in ".." to go back.""")
				print ("")
				print ("+" * 10)
				intcc = input ("Put it in: ")
				if (intcc == ".."):
					jssendmusic()

			#create function to a send a folder
			def jssendfolder():
				gd.system("cls")
				print ("Drop and Drop the Folder here.")
				print ("""Or ".." to go back""")
				print ("")
				print ("+" * 10)
				fldrpath = input ("Put it in: ")
				if (fldrpath == ".."):
					jssend()
				gd.system("cls")
				sp.call("adb push " + fldrpath + " /sdcard/J-share/Folders")
				print ("")
				print ("+" * 61)
				print ("""Check directory "J-share/Folders" on the device.    ^|""")
				print ("+" * 61)
				print ("""Put in ".." to go back.""")
				print ("")
				print ("+" * 10)
				intdd = input ("Put it in: ")
				if (intdd == ".."):
					jssendfolder()
					

			#create function to a send a document
			def jssenddocument():
				gd.system("cls")
				print ("Drag and Drop the Document-File here.")
				print ("""Or ".." to go back""")
				print ("")
				print ("+" * 10)
				docpath = input ("Put it in: ")
				if (docpath == ".."):
					jssend()
				gd.system("cls")
				sp.call("adb push " + docpath + " /sdcard/J-share/Documents")
				print ("")
				print ("+" * 63)
				print ("""Check directory "J-share/Documents" on the device.	     ^|""")
				print ("+" * 63)
				print ("""Put in ".." to go back.""")
				print ("")
				print ("+" * 10)
				intee = input ("Put it in: ")
				if (intee == ".."):
					jssenddocument()

			gd.system("cls")
			gd.system("Title J-share Send")
			jswelcome.welcome()
			print ("+" * 65)
			print ("""Select an Option or ".." to go back.""")
			print ("+" * 65)
			print ("1) Send an Image")
			print ("2) Send a Video")
			print ("3) Send a Music")
			print ("4) Send a Folder")
			print ("5) Send a Document")
			print ("")
			print ("+" * 7)
			option2 = input ("Option: ")
			if (option2 == "1"):
				jssendimg()
				
			if (option2 == "2"):
				jssendvideo()
				
			if (option2 == "3"):
				jssendmusic()
				
			if (option2 == "4"):
				jssendfolder()
				
			if (option2 == "5"):
				jssenddocument()
				
			if (option2 == ".."):
				jspage()
			else:
				js()

		#create function to setup folder structure on a new Android
		def jssetup():
			gd.system("cls")
			print ("Please wait...")
			#create needed folder for android device
			sp.call("adb shell mkdir sdcard/J-share")
			sp.call("adb shell mkdir sdcard/J-share/Images")
			sp.call("adb shell mkdir sdcard/J-share/Videos")
			sp.call("adb shell mkdir sdcard/J-share/Musics")
			sp.call("adb shell mkdir sdcard/J-share/Folders")
			sp.call("adb shell mkdir sdcard/J-share/Documents")
			sp.call("adb shell mkdir sdcard/J-share/Group")
			#create needed folders for pc
			gd.mkdir("C:\J-share-Downloads")
			gd.mkdir("C:\J-share-Downloads\Images")
			gd.mkdir("C:\J-share-Downloads\Videos")
			gd.mkdir("C:\J-share-Downloads\Musics")
			gd.mkdir("C:\J-share-Downloads\Folders")
			gd.mkdir("C:\J-share-Downloads\Documents")
			gd.system("cls")
			print ("Done.")
			time.sleep(3)
			gd.system("cls")
			jspage()
			
		gd.system("cls")
		jswelcome.welcome()
		print ("+" * 64)
		print ("""Select an Option OR "?" for a new user folder setup.""")
		print ("+" * 64)
		print ("1) To Send Files")
		print ("2) To Pull Files")
		print ("3) Group Share")
		print ("4) To pick a specific device (if connected to multiple devices).")
		print ("..) To go back")
		print ("")
		print ("+" * 7)
		intopt = input ("Option: ")
		if (intopt == "1"):
			jssend()
		elif (intopt == "2"):
			jspull()
		elif (intopt == "3"):
			jsgroupsend()
		elif (intopt == ".."):
			jsconnectwirelessly()
		elif (intopt == "?"):
			jssetup()
		elif(intopt == "4"):
			jsmulti()
		else:
			jspage()
			
	#create function to connect wirelessly
	def jsconnectwirelessly():	
		#create function to check IPAddress for wireless connection
		def jsgetip():
			gd.system("cls")
			gd.system("mode con: cols=70 lines=20")
			gd.system("Title Get IPAddress")
			print ("To get the IPAddress, the device has to be connected via a USB cable.")
			time.sleep(2)
			print ("+" * 68)
			sp.call("adb shell ip route")
			print ("+" * 68)
			print (" ")
			print ("""Copy your IPAddress (Next to "src") and place it down below""") 
			print ("""Or ".." to go back.""")
			print ("+" * 10)
			ip2 = input ("Put it in: ")
			print (" ")
			if (ip2 == ".."):
				jsconnectwirelessly()
			else:
				jsconnect(ip2)
		
		#create function to connect device with the provided IPAddress		
		def jsconnect(ip):
			#create function to disconnect device
			def jsdisconnect():
				gd.system("cls")
				sp.call("adb disconnect " + ip + ":5555")
				print (" ")
				time.sleep(2)
				jsconnectwirelessly()
				
			sp.call("adb tcpip 5555")
			gd.system("cls")
			print ("+" * 30)
			sp.call("adb connect " + ip + ":5555")
			print ("+" * 30)
			print ("""Input 1 to proceed or "d" to disconnect the device.""")
			print (" ")
			print ("+" * 10)
			varb = input("Put it in: ") 
			if (varb == "1"):
				jspage()
			elif (varb == "d"):
				jsdisconnect()
			else:
				jsconnect()
				
		#create fucntion to connect my personal device
		def jsconnectjay():
			#create function to disconnect device
			def jsdisconnectjay():
				gd.system("cls")
				sp.call("adb disconnect 192.168.43.1:5555")
				print (" ")
				time.sleep(2)
				jsconnectwirelessly()
				
			gd.system("cls")
			sp.call("adb tcpip 5555")
			gd.system("cls")
			print ("+" * 30)
			sp.call("adb connect 192.168.43.1:5555")
			print ("+" * 30)
			print ("""Input 1 to proceed or "d" to disconnect the device.""")
			print (" ")
			print ("+" * 10)
			varb = input("Put it in: ") 
			#if input is 1 goto hackpage
			if (varb == "1"):
				jspage()
			elif (varb == "d") or (varb == "D"):
				jsdisconnectjay()
			else:
				jsconnectjay()
			
		def jscheckdevices():
			#create function to disconnect device
			def jsdisconnect():
				gd.system("cls")
				sp.call("adb disconnect " + chkdev)
				time.sleep(2)
				jsconnectwirelessly()
				
			gd.system("Title Check Connected Devices")
			gd.system("cls")
			print ("+" * 26)
			gd.system("echo Hi %username%, welcome..")
			print ("+" * 26)
			sp.call("adb devices")
			print ("""Put in "1" to proceed to the jspage or ".." to go back...""")
			print ("Or copy and paste the device ID down below to disconnect.")
			print (" ")
			print ("+" * 10)
			chkdev = input("Put it in: ")
			if (chkdev == "1"):
				jspage()
			elif (chkdev == ".."):
				jsconnectwirelessly()
			else:
				jsdisconnect()
			
		#js connect wirelessly interface
		gd.system("mode con: cols=66 lines=22")
		gd.system("cls")
		jswelcome.welcome()
		print ("+" * 63)
		print("Provide phone's IPAddress or .. to exit.")
		print(" ")
		print("?) To get the IPAddress")
		print("1) If youre already connected")
		print("c) To check other connected devices")
		print ("+" * 13)
		print("J) For JAY |")
		print ("+" * 13) 
		print("PS: Some IPAddresses change(Dynamic IPAddresses)")
		print("    So you need to check for the IPAddress again if the data")
		print("    connection was ressetted or the phone was restarted.")
		print ("+" * 63)
		print(" ")
		ip = input("IPAddress: ")
		if (ip == "1") :
			jspage()
		elif (ip== "c") or (ip == "C"):
			jscheckdevices()
		elif (ip == "?"):
			jsgetip()
		elif (ip == "J") or (ip == "j"):
			jsconnectjay()
		elif (ip == ".."):
			gd.system("exit")
			gd.system("cls")
		else: 
			jsconnect(ip)

	gd.system("mode con: cols=65 lines=15")
	gd.system("color 8")
	gd.system("Title J-share.PY")
	ptH = gd.path.join ("C:\\", "virtualenvironment\\", "J_Hack_Share\\", "J-share 2.0\\")
	gd.chdir(ptH)
	gd.system("cls")
	jsconnectwirelessly()
js()
