from tkinter import *
import PIL
import cv2
import os
from PIL import ImageTk, Image
from tkinter import ttk
from Recognition import RecoWindow
from TrainingModel import TrainingModel
from os import listdir
import pymysql

class MainWindow:
    
    count = 0

    def __init__(self,root):
        self.root = root
        self.root.geometry("1200x650+0+0")
        self.root.resizable(False,False)
        self.root.title("Criminal Face Detection System")
        Windowicon = ImageTk.PhotoImage(file="Assests/icon.png")
        self.root.iconphoto(False,Windowicon)
        # camdriver = "http://192.168.137.57:8080/video"

    #=================================== UI Implementation ====================================================

    #============= All Variables ==================
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 690)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 450)
        self.txt_noti = StringVar()
        self.id_var = StringVar()
        self.name_var = StringVar()
        self.fname_var = StringVar()
        self.mname_var = StringVar()
        self.gender_var = StringVar()
        self.dob_var = StringVar()
        self.nation_var = StringVar()
        self.crimesdone_var = StringVar()
        self.txt_countface_var = StringVar()

    #=======================================
        self.parent_Frame = Frame(self.root)
        self.parent_Frame.pack(fill=BOTH,expand=1)
    #==== Left Side Frames ===============

        #==== Details Frame ==================
        detail_Frame = Frame(self.parent_Frame, bd=4, relief=GROOVE)
        detail_Frame.place(x=3,y=0,width=500,height=400)

        lb_title = Label(detail_Frame, text="Criminal Details",font=("Montserrat",15))
        lb_title.grid(row=0,column=0,pady=7,padx=20,sticky="w")

        lb_required = Label(detail_Frame, text="* Required",font=("Montserrat",15))
        lb_required.grid(row=0,column=1,pady=7,padx=20,sticky="w")

        lb_id = Label(detail_Frame, text="Identification No. *",font=("Montserrat",13))
        lb_id.grid(row=1,column=0,pady=7,padx=20,sticky="w")
        id_txt = Entry(detail_Frame,font=("Montserrat",11),width=30,textvariable = self.id_var)
        id_txt.grid(row=1,column=1,pady=7,padx=20,sticky="w")

        lb_name = Label(detail_Frame, text="Name *",font=("Montserrat",13))
        lb_name.grid(row=2,column=0,pady=7,padx=20,sticky="w")
        name_txt = Entry(detail_Frame,textvariable=self.name_var,font=("Montserrat",11),width=30)
        name_txt.grid(row=2,column=1,pady=7,padx=20,sticky="w")
        
        lb_fname = Label(detail_Frame, text="Father name",font=("Montserrat",13))
        lb_fname.grid(row=3,column=0,pady=7,padx=20,sticky="w")
        fname_txt = Entry(detail_Frame,textvariable=self.fname_var,font=("Montserrat",11),width=30)
        fname_txt.grid(row=3,column=1,pady=7,padx=20,sticky="w")

        lb_mname = Label(detail_Frame, text="Mother name",font=("Montserrat",13))
        lb_mname.grid(row=4,column=0,pady=7,padx=20,sticky="w")
        mname_txt = Entry(detail_Frame,textvariable=self.mname_var,font=("Montserrat",11),width=30)
        mname_txt.grid(row=4,column=1,pady=7,padx=20,sticky="w")

        lb_gender = Label(detail_Frame, text="Gender",font=("Montserrat",13))
        lb_gender.grid(row=5,column=0,pady=7,padx=20,sticky="w")
        gender_txt = Entry(detail_Frame,textvariable=self.gender_var,font=("Montserrat",11),width=30)
        gender_txt.grid(row=5,column=1,pady=7,padx=20,sticky="w")

        lb_dob = Label(detail_Frame, text="DOB(yyyy-mm-dd)",font=("Montserrat",13))
        lb_dob.grid(row=6,column=0,pady=7,padx=20,sticky="w")
        dob_txt = Entry(detail_Frame,textvariable=self.dob_var,font=("Montserrat",11),width=30)
        dob_txt.grid(row=6,column=1,pady=7,padx=20,sticky="w")

        lb_nationality = Label(detail_Frame, text="Nationality *",font=("Montserrat",13))
        lb_nationality.grid(row=7,column=0,pady=7,padx=20,sticky="w")
        nationality_txt = Entry(detail_Frame,textvariable=self.nation_var,font=("Montserrat",11),width=30)
        nationality_txt.grid(row=7,column=1,pady=7,padx=20,sticky="w")

        lb_crime = Label(detail_Frame, text="Crimes Done *",font=("Montserrat",13))
        lb_crime.grid(row=8,column=0,pady=7,padx=20,sticky="w")
        crime_txt = Entry(detail_Frame,textvariable=self.crimesdone_var,font=("Montserrat",11),width=30)
        crime_txt.grid(row=8,column=1,pady=7,padx=20,sticky="w")

        #==== Profile Image Frame ===============
        profile_Frame = Frame(self.parent_Frame, bd=4, relief=GROOVE)
        profile_Frame.place(x=3,y=400,width=500,height=250)

        frame_pp = Frame(profile_Frame,bd=4,relief=GROOVE)
        frame_pp.place(x=5,y=15,width=150,height=200)
        self.lb_pp = Label(frame_pp)
        self.lb_pp.pack(fill = BOTH, expand = 1)

        btn_capture = Button(profile_Frame,text="Capture",font=("Montserrat",10,"bold"),bg="#f2f2f2",cursor="hand2",command = self.faceExtractor)
        btn_capture.place(x=200,y=20,width=100,height=40)

        btn_cancel = Button(profile_Frame,text="Cancel/Delete",font=("Montserrat",10,"bold"),bg="#f2f2f2",cursor="hand2",command=self.cancelCollect)
        btn_cancel.place(x=350,y=20,width=100,height=40)

        btn_training = Button(profile_Frame,text="Start Training",font=("Montserrat",10,"bold"),bg="#f2f2f2",cursor="hand2",command=self.traingingModel)
        btn_training.place(x=200,y=100,width=250,height=40)

        btn_recognition= Button(profile_Frame,text="Start Recognition",font=("Montserrat",10,"bold"),bg="#f2f2f2",cursor="hand2",command=self.recognitionWin)
        btn_recognition.place(x=200,y=170,width=250,height=40)

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

        # Progress bar widget 
        lb_progress = Label(self.noti_Frame, text="Progress:",font=("Montserrat",13,"bold"))
        lb_progress.place(x=0,y=10)
        self.progress = ttk.Progressbar(self.noti_Frame, orient = HORIZONTAL,length = 500, mode = 'determinate') 
        self.progress.place(x=100,y=10)

        # Notification
        lb_notification = Label(self.noti_Frame, text="Notification:",font=("Montserrat",13,"bold"))
        lb_notification.place(x=0,y=65)
        text_notification = Label(self.noti_Frame, textvariable=self.txt_noti,font=("Montserrat",10,"bold"),fg="green")
        text_notification.place(x=100,y=67)
        text_countFace = Label(self.noti_Frame, textvariable=self.txt_countface_var,font=("Montserrat",25,"bold"),fg="#262626")
        text_countFace.place(x=600,y=67)

    #=====================================BackEnd Implementation===============================================
    #Face_Extractor======================
    def faceExtractor(self):
        MainWindow.count +=1
        self.txt_countface_var.set("")
        self.txt_countface_var.set(str(MainWindow.count))
        self.data_path = str("datasets/"+str(self.id_var.get()))
        for (x, y, w, h) in self.faces:
            roi_image = self.imgGray[y:y+h, x:x+w]
            profilePic = self.extractImage[y-100:y+h+200, x-100:x+w+100]
            profilePic = cv2.resize(profilePic,(200,200))

        if not os.path.exists(self.data_path):
            os.mkdir(self.data_path)
        else:
            cv2.imwrite(self.data_path + "/" + "pp" + ".jpg", profilePic)
            cv2.imwrite(self.data_path + "/" +str(self.id_var.get())+" "+str(MainWindow.count)+ ".jpg", roi_image)

    #Face Detection======================
    def faceDetection(self,image):
        
        # Create the haar cascade
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        try:
            self.imgGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            # Detect faces in the image
            self.faces = faceCascade.detectMultiScale(
                self.imgGray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(5, 5)
               )
            self.extractImage = self.imgGray
            # try:
            #     self.faceExtractor(faces,imgGray,image)
            # except Exception as e:
            #     print("Exception",e)

            # Draw a rectangle around the faces
            for (x, y, w, h) in self.faces:
                cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
            self.txt_noti.set("Face Found")
            return image
        except Exception as e:
            print("Exception Inside FD ", e)
            self.txt_noti.set("Face Not Found")
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
        self.cap.release()
        self.lb_webcam.destroy()
        profilePic= ImageTk.PhotoImage(Image.open(str(self.data_path+"/"+"pp.jpg")))
        self.lb_pp.config(image=profilePic)
        self.lb_pp.image = profilePic
        # print(bool(self.lb_webcam.winfo_exists()))
        # print(self.lb_webcam.destroy() == None)
# ==========================================

    # Function responsible for the updation 
        # of the progress bar value 
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
# ====================================================
    def recognitionWin(self):
        RecoWindow(self.root)
        self.parent_Frame.destroy()

# Training Model=======================================
    def traingingModel(self):
        train = TrainingModel()
        train.model_train()
        print(train.operationCompleted)
        if train.operationCompleted:
            self.addCriminal()
            self.bar()
            self.txt_noti.set("Training Data Completed")

        else:
            self.txt_noti.set("Something Went Wrong")
#======================================================
    def cancelCollect(self):
        try:
            conn = pymysql.connect(host="localhost",user="root",password="",database="criminaldb")
            cur = conn.cursor()
            cur.execute("delete from criminals where id=%s",self.id_var.get())
        except Exception as deletedbError:
            print(f"DB Delete Error {deletedbError}")
        finally:
            conn.commit()
            conn.close()
            
        try:
            import shutil
            data_path = listdir("datasets/")
            for dir in data_path:
                print(f"{dir} ---> {type(dir)}")
                if  dir == str(self.id_var.get()):
                    shutil.rmtree(str("datasets/"+dir))
        except Exception as fileError:
            self.txt_noti.set(str(fileError))
        self.clearFeild()
#======================================================
    def clearFeild(self):
        self.id_var.set("")
        self.name_var.set("")
        self.fname_var.set("")
        self.mname_var.set("")
        self.dob_var.set("")
        self.gender_var.set("")
        self.nation_var.set("")
        self.crimesdone_var.set("")
# Add Criminal To Database=========================================   
    def addCriminal(self):
        # print(type(img_path_var),"-->",img_path_var)
        if self.id_var == "" and self.name == "" and len(str(self.id_var)) !=6: 
                self.txt_noti.set("Error Occured: Atleast Id and Name Feild are Required!!")
        else:
            try:
                conn = pymysql.connect(host="localhost",user="root",password="",database="criminaldb")
                curr = conn.cursor()
                curr.execute("insert into criminals values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.id_var.get(),
                                                                                    self.name_var.get(),
                                                                                    self.fname_var.get(),
                                                                                    self.mname_var.get(),
                                                                                    self.gender_var.get(),
                                                                                    self.dob_var.get(),
                                                                                    self.nation_var.get(),
                                                                                    self.crimesdone_var.get(),
                                                                                    str("datasets/"+str(self.id_var.get())) ))
                self.txt_noti.set("Success!! Record is inserted")                                                                       
            except Exception as dbError:
                print(f"Database Error(addCriminal):  {dbError}")
            finally:
                conn.commit()
                self.clearFeild()
                conn.close()
            


        


    
        




# if __name__ == "__main__":
#     root = Tk()
#     MainWindow(root)
#     root.mainloop()