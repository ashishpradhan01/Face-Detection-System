from tkinter import *
import PIL
import cv2
from PIL import ImageTk, Image
from tkinter import ttk
import pymysql

class RecoWindow:

    def __init__(self,root):
        self.root = root
        self.root.geometry("1200x650+0+0")
        self.root.resizable(False,False)
        self.root.title("Criminal Face Detection System")
        Windowicon = ImageTk.PhotoImage(file="Assests/icon.png")
        self.root.iconphoto(False,Windowicon)
        # camdriver = "http://192.168.137.57:8080/video"

    #=================================== UI Implementation =====================================================

    # ============= All Variables ==================
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 690)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 450)
        # ============================================
        self.id_var = StringVar()
        self.name_var = StringVar()
        self.fname_var = StringVar()
        self.mname_var = StringVar()
        self.gender_var = StringVar()
        self.dob_var = StringVar()
        self.nationality_var = StringVar()
        self.crime_var = StringVar()
        self.txt_notification = StringVar()
        self.data_path = 'datasets/' 
        

    #================================================
        self.parent_Frame = Frame(self.root)
        self.parent_Frame.pack(fill=BOTH,expand=1)
    #==== Left Side Frames ===============

        #==== Profile Image Frame ===============
        profile_Frame = Frame(self.parent_Frame, bd=4, relief=GROOVE)
        profile_Frame.place(x=3,y=0,width=500,height=250)

        frame_pp = Frame(profile_Frame,bd=4,relief=GROOVE)
        frame_pp.place(x=5,y=15,width=150,height=200)
        self.lb_pp = Label(frame_pp)
        self.lb_pp.pack(fill = BOTH, expand = 1)

        btn_recognition= Button(profile_Frame,text="Recognition",font=("Montserrat",10,"bold"),bg="#f2f2f2",cursor="hand2",command=self.recognitionFace)
        btn_recognition.place(x=200,y=20,width=250,height=40)

        lb_Search = Label(profile_Frame, text="Search By:",font=("Montserrat",13,"bold"))
        lb_Search.place(x=200,y=80)
        lb_id = Label(profile_Frame, text="Identification no.",font=("Montserrat",13))
        lb_id.place(x=200,y=110)
        txt_Search = Entry(profile_Frame,font=("Montserrat",11),width=30,textvariable=self.id_var)
        txt_Search.place(x=200,y=140)

        btn_Search = Button(profile_Frame,text="Search",font=("Montserrat",10,"bold"),bg="#f2f2f2",cursor="hand2",command=self.searchDb)
        btn_Search.place(x=270,y=174,width=100,height=40)

        #==== Details Frame ==================
        detail_Frame = Frame(self.parent_Frame, bd=4, relief=GROOVE)
        detail_Frame.place(x=3,y=250,width=500,height=400)

        lb_title = Label(detail_Frame, text="Criminal Details",font=("Montserrat",15))
        lb_title.grid(row=0,column=0,pady=7,padx=20,sticky="w")

        lb_required = Label(detail_Frame, text="* Required",font=("Montserrat",15))
        lb_required.grid(row=0,column=1,pady=7,padx=20,sticky="w")

        # lb_id = Label(detail_Frame, text="Identification No. *",font=("Montserrat",13))
        # lb_id.grid(row=1,column=0,pady=7,padx=20,sticky="w")
        # id_txt = Entry(detail_Frame,font=("Montserrat",11),width=30)
        # id_txt.grid(row=1,column=1,pady=7,padx=20,sticky="w")

        lb_name = Label(detail_Frame, text="Name *",font=("Montserrat",13))
        lb_name.grid(row=1,column=0,pady=7,padx=20,sticky="w")
        name_txt = Entry(detail_Frame,textvariable=self.name_var,font=("Montserrat",11),width=30)
        name_txt.grid(row=1,column=1,pady=7,padx=20,sticky="w")
        
        lb_fname = Label(detail_Frame, text="Father name",font=("Montserrat",13))
        lb_fname.grid(row=2,column=0,pady=7,padx=20,sticky="w")
        fname_txt = Entry(detail_Frame,textvariable=self.fname_var,font=("Montserrat",11),width=30)
        fname_txt.grid(row=2,column=1,pady=7,padx=20,sticky="w")

        lb_mname = Label(detail_Frame, text="Mother name",font=("Montserrat",13))
        lb_mname.grid(row=3,column=0,pady=7,padx=20,sticky="w")
        mname_txt = Entry(detail_Frame,textvariable=self.mname_var,font=("Montserrat",11),width=30)
        mname_txt.grid(row=3,column=1,pady=7,padx=20,sticky="w")

        lb_gender = Label(detail_Frame, text="Gender",font=("Montserrat",13))
        lb_gender.grid(row=4,column=0,pady=7,padx=20,sticky="w")
        gender_txt = Entry(detail_Frame,textvariable=self.gender_var,font=("Montserrat",11),width=30)
        gender_txt.grid(row=4,column=1,pady=7,padx=20,sticky="w")

        lb_dob = Label(detail_Frame, text="DOB(yyyy-mm-dd)",font=("Montserrat",13))
        lb_dob.grid(row=5,column=0,pady=7,padx=20,sticky="w")
        dob_txt = Entry(detail_Frame,textvariable=self.dob_var,font=("Montserrat",11),width=30)
        dob_txt.grid(row=5,column=1,pady=7,padx=20,sticky="w")

        lb_nationality = Label(detail_Frame, text="Nationality *",font=("Montserrat",13))
        lb_nationality.grid(row=6,column=0,pady=7,padx=20,sticky="w")
        nationality_txt = Entry(detail_Frame,textvariable=self.nationality_var,font=("Montserrat",11),width=30)
        nationality_txt.grid(row=6,column=1,pady=7,padx=20,sticky="w")

        lb_crime = Label(detail_Frame, text="Crimes Done *",font=("Montserrat",13))
        lb_crime.grid(row=7,column=0,pady=7,padx=20,sticky="w")
        crime_txt = Entry(detail_Frame,textvariable=self.crime_var,font=("Montserrat",11),width=30)
        crime_txt.grid(row=7,column=1,pady=7,padx=20,sticky="w")

        btn_frame = Frame(detail_Frame)
        btn_frame.place(x=50,y=330,width=400,height=50)

        update_btn = Button(btn_frame,text="Update",font=("Montserrat",10,"bold"),bg="#f2f2f2",cursor="hand2",command=self.update_data)
        update_btn.place(x=10,width=150,height=40)
        clear_btn = Button(btn_frame,text="Clear All",font=("Montserrat",10,"bold"),bg="#f2f2f2",cursor="hand2",command=self.clearAllData)
        clear_btn.place(x=200,width=150,height=40)

        
    #==== Right Side Frames ===============

        #===== Webcam Frame ===================
        self.webcam_Frame = Frame(self.parent_Frame, bd=4, relief=GROOVE)
        self.webcam_Frame.place(x=507,y=0,width=690,height=450)

        self.lb_webcam_title = Label(self.webcam_Frame,text = "Camera Input",font=("Montserrat",15,"bold"))
        self.lb_webcam_title.place(x=278,y=245)

        self.lb_webcam = Label(self.webcam_Frame)
        self.lb_webcam.pack()

        #===== Button Frame ===================
        btn_Frame = Frame(self.parent_Frame, bd=4,relief=GROOVE)
        btn_Frame.place(x=507,y=450,width=690,height=50)

        self.startcam_btn = Button(btn_Frame,text="Start Cam",font=("Montserrat",10,"bold"),bg="#f2f2f2",cursor="hand2",command=self.show_cam)
        self.startcam_btn.place(x=270,width=150,height=40)
        self.stopcam_btn = Button(btn_Frame,text="Stop Cam",font=("Montserrat",10,"bold"),bg="#f2f2f2",cursor="hand2",command = self.stop_cam)

        #===== Notification Frame =============
        self.noti_Frame = Frame(self.parent_Frame, bd=4, relief=GROOVE)
        self.noti_Frame.place(x=507,y=500,width=690,height=150)

        # Notification
        lb_notification = Label(self.noti_Frame, text="Notification:",font=("Montserrat",13,"bold"))
        lb_notification.place(x=0,y=15)
        text_notification = Label(self.noti_Frame, font=("Montserrat",10,"bold"),fg="green",textvariable=self.txt_notification)
        text_notification.place(x=100,y=17)
    
    #Face Detection======================
    def faceDetection(self,image):
        # Create the haar cascade
        self.faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        try:
            self.imgGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            # Detect faces in the image
            self.faces = self.faceCascade.detectMultiScale(
                self.imgGray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30,30)
                # flags = cv2.cv.CV_HAAR_SCALE_IMAGE
            )
            # Draw a rectangle around the faces
            for (x, y, w, h) in self.faces:
                cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
            return image
        except:
            print("No Face Found ") 
            return image

    #Webcam Functionalty=================
    def show_cam(self):
        camAvaiable, frame = self.cap.read()
        self.stopcam_btn.place(x=270,width=150,height=40)
        self.startcam_btn.place_forget()
        # self.lb_webcam_title.config(text="")
        if(camAvaiable == True):
            frame = cv2.flip(frame, 1)
            image = self.faceDetection(frame)
            cv2image = cv2.cvtColor(image, cv2.COLOR_BGR2RGBA)
            # cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
            img = PIL.Image.fromarray(cv2image)
            imgtk = ImageTk.PhotoImage(image=img)
            self.lb_webcam.imgtk = imgtk
            self.lb_webcam.configure(image=imgtk)
            self.lb_webcam.after(10, self.show_cam)
        else:
            print("Turning On Camera")
            self.cap = cv2.VideoCapture(0)
            self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 690)
            self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 450)
            self.lb_webcam = Label(self.webcam_Frame)
            self.lb_webcam.pack()
            self.lb_webcam.after(10, self.show_cam)


    def stop_cam(self):
        self.startcam_btn.place(x=270,width=150,height=40)
        self.stopcam_btn.place_forget()
        # self.lb_webcam_title.config(text="Camera Input")
        self.cap.release()
        self.lb_webcam.destroy()
        # print(self.lb_webcam.destroy() == None)
# ==========================================

    def parent_dest(self):
        MainWindow(self.root)
        self.parent_Frame.destory()

    # Function responsible for the updation of the progress bar value.
    def bar(self): 
        import time
        self.progress['value'] = 20
        self.noti_Frame.update_idletasks() 
        time.sleep(1) 
    
        self.progress['value'] = 40
        self.noti_Frame.update_idletasks() 
        time.sleep(1) 
    
        self.progress['value'] = 45
        self.noti_Frame.update_idletasks() 
        time.sleep(1) 
    
        self.progress['value'] = 58
        self.noti_Frame.update_idletasks() 
        time.sleep(1) 
    
        self.progress['value'] = 85
        self.noti_Frame.update_idletasks() 
        time.sleep(1) 
        self.progress['value'] = 100

#====================================================
    def parent_destroy(self):
        self.parent_Frame.destroy()

    #ClearAllData=====================
    def clearAllData(self):
        self.txt_notification.set("")
        self.name_var.set("")
        self.fname_var.set("")
        self.mname_var.set("")
        self.gender_var.set("")
        self.dob_var.set("")
        self.nationality_var.set("")
        self.crime_var.set("")
    
    #Search Database by Id
    def searchDb(self):
        try:
            conn = pymysql.connect(host="localhost",user="root",password="",database="criminaldb")
            curr = conn.cursor()
            curr.execute("select * from criminals where id LIKE '%"+str(self.id_var.get())+"%'")
            rows = curr.fetchall()
            for criminalData in rows:
                self.name_var.set(str(criminalData[1]))
                self.fname_var.set(str(criminalData[2]))
                self.mname_var.set(str(criminalData[3]))
                self.gender_var.set(str(criminalData[4]))
                self.dob_var.set(str(criminalData[5]))
                self.nationality_var.set(str(criminalData[6]))
                self.crime_var.set(str(criminalData[7]))
                self.imgPath = str(criminalData[8])
            profilePic= ImageTk.PhotoImage(Image.open(str(self.imgPath+"/"+"pp.jpg")))
            self.lb_pp.config(image=profilePic)
            self.lb_pp.image = profilePic
            self.txt_notification.set("")
        except Exception as searchError:
            self.txt_notification.set("No Criminal with this id")
            print(f"Search Database Error: {searchError}")
        finally:
            conn.close() 

    #Update Criminal DB
    def update_data(self):  
        try:
            conn = pymysql.connect(host="localhost",user="root",password="",database="criminaldb")
            cur = conn.cursor()
            cur.execute("update criminals set name=%s,father_name=%s,mother_name=%s,gender=%s,dob=%s,nationality=%s,crimesdone=%s where id=%s",(self.name_var.get(),
                                                                                                                                            self.fname_var.get(),
                                                                                                                                            self.mname_var.get(),
                                                                                                                                            self.gender_var.get(),
                                                                                                                                            self.dob_var.get(),
                                                                                                                                            self.nationality_var.get(),
                                                                                                                                            self.crime_var.get(),
                                                                                                                                            self.id_var.get()))
            self.txt_notification.set("Update Successfully")
        except Exception as updateError:
            self.txt_notification.set("Error Occured While Updating")
            print(f"Updata Data Error: {updateError}")
        finally:                                                                                                                                    
            conn.commit()
            conn.close()
    
    def recognitionFace(self):
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read('trainer/trainedModel.yml')
        id =  0
        confidence=0
        for (x, y, w, h) in self.faces:
            id, confidence = recognizer.predict(self.imgGray[y:y + h, x:x + w])

        if id ==0 and confidence ==0:
            self.id_var.set("")
            self.txt_notification.set("Face Not Found")
        else:
            self.txt_notification.set(f'id: {id} confidence: {confidence}')
            self.id_var.set(str(id))    


    

        




# if __name__ == "__main__":
#     root = Tk()
#     RecoWindow(root)
#     root.mainloop()