from tkinter import *
from tkinter import messagebox

#전체 창 생성 및 크기 제목 설정
pro = Tk()
pro.geometry("730x700")
pro.title("직장생활 백서")
pro.configure(background='LemonChiffon2')

#직장인 생활 백서 라벨생성
la=Label(pro, text="<직장인 생활 백서>", font=("궁서", 17, "bold"), fg="olive drab", bg="LemonChiffon2")
la.place(x=270, y=10)

#프로그램 설명 버튼 클릭 요청  라벨생성
la=Label(pro, text="1장. 아래의 버튼을 클릭하여 사용법을 익혀보세요.", font=("맑은 고딕", 12), fg="olive drab", bg="LemonChiffon2")
la.place(x=180, y=50)


#설명버튼 클릭 후 프로그램 설명 라벨리스트박스 띄우기 함수 정의
def explain():

    nexplain = Toplevel(pro)
    nexplain.title("프로그램 설명")
    nexplain.geometry("500x300")
    nexplain.configure(background='Lavender')
    
    exp=Label(nexplain,text="프로그램 설명",font=("맑은 고딕",11), fg="purple4", bg="Lavender")
    exp.pack()

    expbox=Listbox(nexplain, selectmode="extended",width=0, height=0,font=("맑은 고딕",10), fg="purple4", bg="white")
    expbox.insert(0," 1. 혼동하기 쉬운 맞춤법 교정과 실무용어 설명")
    expbox.insert(1," : 실생활에서 자주 혼동하는 어휘 교정과 실무 용어 정리 ")
    expbox.insert(2," : 직장인 맞춤 어휘 교정 및 실무 용어 테스트 ")
    expbox.insert(3,"")
    expbox.insert(4," 2. 단축키 사용 설명 ")
    expbox.insert(5," : 직장에서 유용하게 사용하는 컴퓨터 단축키 사용 설명 ")
    expbox.insert(6," : 직장에서 유용하게 사용하는 컴퓨터 단축키 테스트 ")
    expbox.insert(7," ")
    expbox.insert(8," 3. 점심메뉴 랜덤 추첨기 ")
    expbox.insert(9," : 점심메뉴 결정이 어려울 때 랜덤으로 메뉴를 추천 ")
    expbox.insert(10,"  - 한식, 양식, 중식, 일식, 랜덤 중 선택 ")
    expbox.pack()


#설명버튼 생성
b=Button(pro, text="1. 프로그램 설명",command=explain, activebackground="orange",font=("맑은 고딕",11),fg="olive drab", bg="ivory2")
b.place(x=320, y=90)

#직장인 단어 라벨생성
la=Label(pro, text="2장. 자주 혼동하는 맞춤법과 직장에서 자주 사용하는 단어를 알아봅시다.",font=("맑은 고딕", 12), fg="olive drab", bg="LemonChiffon2")
la.place(x=105, y=160)

#직장인 단어 설명 클릭 후 단어 설명 라벨,리스트박스 띄우기 함수 정의
def word():
    
    nword = Toplevel(pro)
    nword.title("맞춤법 및 직장인 단어 설명")
    nword.geometry("900x700")
    nword.configure(background='misty rose')
    
    exp=Label(nword,text="맞춤법 및 직장인 단어 설명", font=("맑은 고딕",11), fg="Palevioletred4", bg="misty rose")
    exp.pack()

    expbox=Listbox(nword, selectmode="extended",width=0, height=0, font=("맑은 고딕",10), fg="Palevioletred4", bg="white")
    expbox.insert(0,"< 맞춤법의 올바른 사용과 직장인이 자주 사용하는 단어 설명>")
    expbox.insert(1,"- 맞춤법 -")
    expbox.insert(2," 1. 되 VS 돼")
    expbox.insert(3,"   '돼'는 '되어요'의 준말입니다. '되'와 '돼'가 들어갈 자리에 '하'와 '해'를 넣어 구분해보세요! (하=되/해=돼)")
    expbox.insert(4," 2. 안 VS 않")
    expbox.insert(5,"    '안'을 '아니', '않'을 '아니하'로 바꿔보세요! 말이 되면 '안' 말이 안 되면 '않'을 사용합니다.")
    expbox.insert(6," 3. 왠만하면X / 웬만하면 O")
    expbox.insert(7,"    '왠'은 '왠지'에서만 사용합니다. 그 외는 모두 '웬'이 맞습니다! '웬'을 '어찌 된'으로 놓고 말이 되는지 확인해보세요. 말이 되면 맞는 것입니다.")
    expbox.insert(8," 4. 뵈요 X / 봬요 O")
    expbox.insert(9,"     '봬요'는 '뵈어요'의 준말입니다. '봬'가 들어갈 자리에 '뵈어'를 대입했을 때 자연스럽다면 '봬'를 사용하고, 그렇지 않다면 '뵈'를 사용하세요!")
    expbox.insert(11," 5. 몇일 X / 며칠 O")
    expbox.insert(12,"    '몇 일'이라고 적는 경우는 없고, '며칠'을 사용하는 것이 옳습니다.")
    expbox.insert(13," ")
    expbox.insert(14,"- 직장인 단어 -")
    expbox.insert(15," 1. 업무편")
    expbox.insert(16,"   ⓛ TFT(Task Force Team): 특별 프로젝트를 수행하기 위해 만든 팀을 말합니다.")
    expbox.insert(17,"   ② R&R(Role & Responsibility): 구성원들이 수행해야 하는 역할과 업무 책임범위를 말합니다.")
    expbox.insert(18,"   ③ PM(Project Manager): 프로젝트를 책임지는 수장을 말합니다.")
    expbox.insert(19,"   ④ ASAP(As Soon As Possible): '가능한 빠른 시일 내'를 의미합니다.")
    expbox.insert(20," 2. 메일편")
    expbox.insert(21,"   ① CC(Carbon Copy): 참조")
    expbox.insert(22,"   ② BCC(Blind Carbon Copy): 숨은 참조")
    expbox.insert(23,"   ③ FW(Forward): 메일 재전달")
    expbox.insert(24,"   ④ RE(Reply): 답장")
    expbox.insert(25," 3. 문서편")
    expbox.insert(26,"   ⓛ 품의: 어떤 일을 진행하기에 앞서 결재권자에게 특정 사안에 대해 승인을 요청하는 문서")
    expbox.insert(27,"   ② 기안: 어떤 일을 진행하기 전 포괄적인 내용을 보고하는 문서")
    expbox.insert(28,"   ③ 지출결의: 회사 내 지출이 예상되는 비용을 사전에 승인 요청하는 문서")
    expbox.insert(29," 4. 날짜편")
    expbox.insert(30,"   ① 금일: 오늘")
    expbox.insert(31,"   ② 작일: 어제")
    expbox.insert(32,"   ③ 명일: 내일")
    expbox.insert(33," 5. 직위체계편")
    expbox.insert(34,"   ① 일반직: 사원 > 주임(계장) > 대리 > 과장 > 차장 > 부장")
    expbox.insert(35,"   ② 중간 관리직: 과장 > 차장 > 부장")
    expbox.insert(36,"   ③ 임원직: 이사 > 상무 > 전무 > 부사장 > 사장 > 부회장 > 회장")
    expbox.pack()


#직장인 단어 설명 버튼 생성
b=Button(pro, text="2-1. 직장인 단어 설명",command=word, activebackground="orange",font=("맑은 고딕",11),fg="olive drab", bg="ivory2")
b.place(x=300, y=200)


#직장인 단어 테스트 클릭 후 테스트 창 실행
def wordtest():
    
    nwordtest = Toplevel(pro)
    nwordtest.title("직장인 단어 테스트")
    nwordtest.geometry("500x450")    
    nwordtest.configure(background='misty rose')

    def qwordtest1():

        fir = Tk()
        fir.geometry("200x150")
        fir.title("직장인 단어 테스트 1번")
        fir.configure(background='misty rose')

        def yes():
            messagebox.showinfo("결과","오답입니다.")
        def no():
            messagebox.showinfo("결과","정답입니다!")

        label=Label(fir,text='1. 다음 문장은 올바른 문장인가? ',fg="Palevioletred4",bg="misty rose")
        label.pack()

        label=Label(fir,text='<나는 회계사가 됬다.>',fg="Palevioletred4",bg="misty rose")
        label.pack()

        btn1 = Button(fir, text="O",command=yes,fg="Palevioletred4",bg="white")
        btn2 = Button(fir, text="X",command=no,fg="Palevioletred4",bg="white")

        btn1.pack()
        btn2.pack()

        fir.mainloop()

    def qwordtest2():

        fir = Tk()
        fir.geometry("200x150")
        fir.title("직장인 단어 테스트 2번")
        fir.configure(background='misty rose')

        def yes():
            messagebox.showinfo("결과","오답입니다.")
        def no():
            messagebox.showinfo("결과","정답입니다!")

        label=Label(fir,text='2. 다음 문장은 올바른 문장인가? ',fg="Palevioletred4",bg="misty rose")
        label.pack()

        label=Label(fir,text='<왠만하면 그러지 말자.>',fg="Palevioletred4",bg="misty rose")
        label.pack()

        btn1 = Button(fir, text="O",command=yes,fg="Palevioletred4",bg="white")
        btn2 = Button(fir, text="X",command=no,fg="Palevioletred4",bg="white")

        btn1.pack()
        btn2.pack()

        fir.mainloop()
        
    def qwordtest3():

        fir = Tk()
        fir.geometry("200x150")
        fir.title("직장인 단어 테스트 3번")
        fir.configure(background='misty rose')

        def yes():
            messagebox.showinfo("결과","정답입니다!")
        def no():
            messagebox.showinfo("결과","오답입니다.")

        label=Label(fir,text='3. 다음 문장은 올바른 문장인가? ',fg="Palevioletred4",bg="misty rose")
        label.pack()

        label=Label(fir,text='<오늘이 며칠이지?>',fg="Palevioletred4",bg="misty rose")
        label.pack()

        btn1 = Button(fir, text="O",command=yes,fg="Palevioletred4",bg="white")
        btn2 = Button(fir, text="X",command=no,fg="Palevioletred4",bg="white")

        btn1.pack()
        btn2.pack()

        fir.mainloop()
        
        
    def qwordtest4():

        fir = Tk()
        fir.geometry("200x150")
        fir.title("직장인 단어 테스트 4번")
        fir.configure(background='misty rose')

        def yes():
            messagebox.showinfo("결과","오답입니다.")
        def no():
            messagebox.showinfo("결과","정답입니다!")

        label=Label(fir,text='4. 다음 단어의 뜻이 올바른가? ',fg="Palevioletred4",bg="misty rose")
        label.pack()

        label=Label(fir,text='<R&RD은 후속 조치라는 뜻이다.> ',fg="Palevioletred4",bg="misty rose")
        label.pack()

        btn1 = Button(fir, text="O",command=yes,fg="Palevioletred4",bg="white")
        btn2 = Button(fir, text="X",command=no,fg="Palevioletred4",bg="white")

        btn1.pack()
        btn2.pack()

        fir.mainloop()
        
    def qwordtest5():

        fir = Tk()
        fir.geometry("200x150")
        fir.title("직장인 단어 테스트 5번")
        fir.configure(background='misty rose')

        def yes():
            messagebox.showinfo("결과","정답입니다!")
        def no():
            messagebox.showinfo("결과","오답입니다.")

        label=Label(fir,text='5. 다음 단어의 뜻이 올바른가? ',fg="Palevioletred4",bg="misty rose")
        label.pack()

        label=Label(fir,text='<CC는 참조라는 뜻이다.> ',fg="Palevioletred4",bg="misty rose")
        label.pack()

        btn1 = Button(fir, text="O",command=yes,fg="Palevioletred4",bg="white")
        btn2 = Button(fir, text="X",command=no,fg="Palevioletred4",bg="white")

        btn1.pack()
        btn2.pack()

        fir.mainloop()
        
        


    labelf=Label(nwordtest, text="<직장인 단어 테스트>",font=("맑은 고딕",11),fg="Palevioletred4", bg="misty rose")
    labelf.pack()

    labelf=Label(nwordtest, text="  문제를 읽고 알맞은 답을 선택하시오.",font=("맑은 고딕",11),fg="Palevioletred4",bg="misty rose")
    labelf.pack()

    labelf=Label(nwordtest, text="  ",font=("맑은 고딕",11),fg="Palevioletred4",bg="misty rose")
    labelf.pack()


    labels=Label(nwordtest, text="1. 다음 문장은 올바른 문장인가? ",font=("맑은 고딕",11),fg="Palevioletred4",bg="misty rose")
    labels.pack()

    b=Button(nwordtest, text="직장인 단어 테스트 1번", command=qwordtest1, activebackground="orange",font=("맑은 고딕",11),fg="Palevioletred4",bg="white")
    b.pack()
    
    labels=Label(nwordtest, text="2. 다음 문장은 올바른 문장인가? ",font=("맑은 고딕",11),fg="Palevioletred4",bg="misty rose")
    labels.pack()

    b=Button(nwordtest, text="직장인 단어 테스트 2번", command=qwordtest2, activebackground="orange",font=("맑은 고딕",11),fg="Palevioletred4",bg="white")
    b.pack()

    labels=Label(nwordtest, text="3. 다음 문장은 올바른 문장인가? ",font=("맑은 고딕",11),fg="Palevioletred4",bg="misty rose")
    labels.pack()

    b=Button(nwordtest, text="직장인 단어 테스트 3번", command=qwordtest3, activebackground="orange",font=("맑은 고딕",11),fg="Palevioletred4",bg="white")
    b.pack()
    
    labels=Label(nwordtest, text="4. 다음 단어의 뜻이 올바른가? ",font=("맑은 고딕",11),fg="Palevioletred4",bg="misty rose")
    labels.pack()

    b=Button(nwordtest, text="직장인 단어 테스트 4번", command=qwordtest4, activebackground="orange",font=("맑은 고딕",11),fg="Palevioletred4",bg="white")
    b.pack()

    labels=Label(nwordtest, text="5. 다음 단어의 뜻이 올바른가? ",font=("맑은 고딕",11),fg="Palevioletred4",bg="misty rose")
    labels.pack()

    b=Button(nwordtest, text="직장인 단어 테스트 5번", command=qwordtest5, activebackground="orange",font=("맑은 고딕",11),fg="Palevioletred4",bg="white")
    b.pack()
    
    labels=Label(nwordtest, text=" ",font=("맑은 고딕",11),fg="Palevioletred4",bg="misty rose")
    labels.pack()

    labels=Label(nwordtest, text=" 수고하셨습니다 ^^  ",font=("맑은 고딕",11),fg="Palevioletred4",bg="misty rose")
    labels.pack()
    

    

#직장인 단어 테스트 버튼 생성
b=Button(pro, text="2-2. 직장인 단어 테스트",command=wordtest, activebackground="orange",font=("맑은 고딕",11),fg="olive drab", bg="ivory2")
b.place(x=290, y=255)


#단축키 설명 라벨생성
la=Label(pro, text="3장. 업무 시 자주 사용하는 단축키를 알아봅시다.",font=("맑은 고딕", 12), fg="olive drab", bg="LemonChiffon2")
la.place(x=180, y=325)

#단축키 설명 클릭 후 단어 설명 라벨,리스트박스 띄우기 함수 정의
def key():

    nkey = Toplevel(pro)
    nkey.title("단축키 설명")
    nkey.geometry("500x450")
    nkey.configure(background='LightSkyBlue1')
     
    exp=Label(nkey,text="단축키 설명", font=("맑은 고딕",11), fg="RoyalBlue4", bg="LightSkyBlue1")
    exp.pack()

    expbox=Listbox(nkey, selectmode="extended",width=0, height=0,font=("맑은 고딕",10), fg="RoyalBlue4", bg="white")
    expbox.insert(0,"< 단축키 사용 설명>")
    expbox.insert(1," - 엑셀(실무에서 가장 많이 사용하는 MS프로그램 입니다.) -")
    expbox.insert(2,"   1. F2: 현재 셀 편집")
    expbox.insert(3,"   2. F7 맞춤법 검사")
    expbox.insert(4,"   3. F12: 다른 이름으로 저장")
    expbox.insert(5,"   4. Ctrl + F2: 인쇄 미리보기")
    expbox.insert(6,"   5. Ctrl + A: 모두 선택")
    expbox.insert(7,"   6. Ctrl + F: 찾기")
    expbox.insert(8,"   7. Ctrl + D: 위쪽 셀 복사 (아래쪽 셀에) 붙여넣기")
    expbox.insert(9,"   8. Ctrl + S: 저장")
    expbox.insert(10,"  9. Ctrl + W: 닫기")
    expbox.insert(11,"  10. Ctrl + Z: 실행취소")
    expbox.insert(12,"  11. Ctrl + Tab: 다른 작업 파일로 이동")
    expbox.insert(13,"  12. Ctrl + PageUp/Down: 작업파일의 다른 시트로 이동")
    expbox.insert(14,"  13. Ctrl + N + I: 이미지 삽입")
    expbox.insert(15,"   ")
    expbox.insert(16," - 윈도우 -")
    expbox.insert(17,"   1. Window + 방향키: 현재 띄워진 창을 방향키의 방향으로 옮길 때")
    expbox.insert(18,"   2. Window + ,(쉼표): 창을 내리지 않고 바탕화면을 볼 때")
    expbox.insert(19,"   3. Window + D: 현재 띄워진 창을 모두 내릴 때")
    expbox.insert(20,"   9. Window + L: 화면을 잠굴 때")
    expbox.insert(21,"   9. Ctrl + Shift + Esc: 작업관리자를 띄울 때")
    expbox.pack()


#단축키 설명 버튼 생성
b=Button(pro, text="3-1. 단축키 설명",command=key, activebackground="orange",font=("맑은 고딕",11),fg="olive drab", bg="ivory2")
b.place(x=320, y=365)


#단축키 테스트 클릭 후 테스트 창 실행
def keytest():
    
    nwordtest = Toplevel(pro)
    nwordtest.title("단축키 테스트")
    nwordtest.geometry("500x450")
    nwordtest.configure(background='LightSkyBlue1')


    def qkeytest1():

        fir = Tk()
        fir.geometry("350x200")
        fir.title("단축키 테스트 1번")
        fir.configure(background='LightSkyBlue1')

        def V():
            messagebox.showinfo("결과","오답입니다.")
        def A():
            messagebox.showinfo("결과","오답입니다.")
        def C():
            messagebox.showinfo("결과","오답입니다.")
        def B():
            messagebox.showinfo("결과","정답입니다!")

        label=Label(fir,text='1. 엑셀에서 현재 셀을 편집할 때 사용하는 단축키는? ',fg="RoyalBlue4", bg="LightSkyBlue1")
        label.pack()

        btn1 = Button(fir, text=" ① F7",command=V,fg="RoyalBlue4",bg="white")
        btn2 = Button(fir, text=" ② Ctrl + F2",command=A,fg="RoyalBlue4",bg="white")
        btn3 = Button(fir, text=" ③ F12",command=C,fg="RoyalBlue4",bg="white")
        btn4 = Button(fir, text=" ④ F2",command=B,fg="RoyalBlue4",bg="white")

        btn1.pack()
        btn2.pack()
        btn3.pack()
        btn4.pack()

        fir.mainloop()

    def qkeytest2():

        fir = Tk()
        fir.geometry("300x200")
        fir.title("단축키 테스트 2번")
        fir.configure(background='LightSkyBlue1')
        
        def Q():
            messagebox.showinfo("결과","오답입니다.")
        def W():
            messagebox.showinfo("결과","정답입니다!")
        def E():
            messagebox.showinfo("결과","오답입니다.")
        def R():
            messagebox.showinfo("결과","오답입니다.")

        label=Label(fir,text='2. 엑셀에서 맞춤법 검사할 때 사용하는 단축키는? ',fg="RoyalBlue4", bg="LightSkyBlue1")
        label.pack()

        btn1 = Button(fir, text="① Ctrl + Z",command=Q,fg="RoyalBlue4",bg="white")
        btn2 = Button(fir, text="② F7",command=W,fg="RoyalBlue4",bg="white")
        btn3 = Button(fir, text="③ Ctrl + S",command=E,fg="RoyalBlue4",bg="white")
        btn4 = Button(fir, text="④ Ctrl+ W",command=R,fg="RoyalBlue4",bg="white")

        btn1.pack()
        btn2.pack()
        btn3.pack()
        btn4.pack()

        fir.mainloop()

    def qkeytest3():

        fir = Tk()
        fir.geometry("300x200")
        fir.title("단축키 테스트 3번")
        fir.configure(background='LightSkyBlue1')

        def Q():
            messagebox.showinfo("결과","오답입니다.")
        def W():
            messagebox.showinfo("결과","오답입니다.")
        def E():
            messagebox.showinfo("결과","오답입니다.")
        def R():
            messagebox.showinfo("결과","정답입니다!")

        label=Label(fir,text='3. 엑셀에서 실행취소할 때 사용하는 단축키는? ',fg="RoyalBlue4", bg="LightSkyBlue1")
        label.pack()

        btn1 = Button(fir, text="① Ctrl + F",command=Q,fg="RoyalBlue4",bg="white")
        btn2 = Button(fir, text="② Ctrl + A",command=W,fg="RoyalBlue4",bg="white")
        btn3 = Button(fir, text="③ F2",command=E,fg="RoyalBlue4",bg="white")
        btn4 = Button(fir, text="④ Ctrl + Z",command=R,fg="RoyalBlue4",bg="white")

        btn1.pack()
        btn2.pack()
        btn3.pack()
        btn4.pack()

        fir.mainloop()

    def qkeytest4():

        fir = Tk()
        fir.geometry("450x200")
        fir.title("단축키 테스트 4번")
        fir.configure(background='LightSkyBlue1')

        def Q():
            messagebox.showinfo("결과","정답입니다!")
        def W():
            messagebox.showinfo("결과","오답입니다.")
        def E():
            messagebox.showinfo("결과","오답입니다.")
        def R():
            messagebox.showinfo("결과","오답입니다.")

        label=Label(fir,text='4. 엑셀에서 위쪽 셀을 아래쪽에 붙여넣기할 때 사용하는 단축키는? ',fg="RoyalBlue4", bg="LightSkyBlue1")
        label.pack()

        btn1 = Button(fir, text="① Ctrl + D",command=Q,fg="RoyalBlue4",bg="white")
        btn2 = Button(fir, text="② F6",command=W,fg="RoyalBlue4",bg="white")
        btn3 = Button(fir, text="③ Ctrl + T",command=E,fg="RoyalBlue4",bg="white")
        btn4 = Button(fir, text="④ Ctr l+ W",command=R,fg="RoyalBlue4",bg="white")

        btn1.pack()
        btn2.pack()
        btn3.pack()
        btn4.pack()

        fir.mainloop()

    def qkeytest5():

        fir = Tk()
        fir.geometry("300x200")
        fir.title("단축키 테스트 5번")
        fir.configure(background='LightSkyBlue1')

        def Q():
            messagebox.showinfo("결과","오답입니다.")
        def W():
            messagebox.showinfo("결과","오답입니다.")
        def E():
            messagebox.showinfo("결과","정답입니다!")
        def R():
            messagebox.showinfo("결과","오답입니다.")

        label=Label(fir,text='5. 윈도우 화면잠금할 때 사용하는 단축키는? ',fg="RoyalBlue4", bg="LightSkyBlue1")
        label.pack()

        btn1 = Button(fir, text="① Window + ,",command=Q,fg="RoyalBlue4",bg="white")
        btn2 = Button(fir, text="② Window + D",command=W,fg="RoyalBlue4",bg="white")
        btn3 = Button(fir, text="③ Window + L",command=E,fg="RoyalBlue4",bg="white")
        btn4 = Button(fir, text="④ Window + Z",command=R,fg="RoyalBlue4",bg="white")

        btn1.pack()
        btn2.pack()
        btn3.pack()
        btn4.pack()

        fir.mainloop()


    labelf=Label(nwordtest, text="<단축키 테스트>",font=("맑은 고딕",11),fg="RoyalBlue4", bg="LightSkyBlue1")
    labelf.pack()

    labelf=Label(nwordtest, text="  문제 속 문장을 실행하려면 눌러야 하는 단축키를 고르시오.",font=("맑은 고딕",11),fg="RoyalBlue4", bg="LightSkyBlue1")
    labelf.pack()

    labelf=Label(nwordtest, text="  ",font=("맑은 고딕",11),fg="RoyalBlue4", bg="LightSkyBlue1")
    labelf.pack()

    labels=Label(nwordtest, text="1. 엑셀에서 현재 셀을 편집할 때 사용하는 단축키는? ",font=("맑은 고딕",11),fg="RoyalBlue4", bg="LightSkyBlue1")
    labels.pack()

    b=Button(nwordtest, text="단축키 테스트 1번", command=qkeytest1, activebackground="orange",font=("맑은 고딕",11),fg="RoyalBlue4",bg="white")
    b.pack()
        
    labels=Label(nwordtest, text="2. 엑셀에서 맞춤법 검사할 때 사용하는 단축키는? ",font=("맑은 고딕",11),fg="RoyalBlue4", bg="LightSkyBlue1")
    labels.pack()

    b=Button(nwordtest, text="단축키 테스트 2번", command=qkeytest2, activebackground="orange",font=("맑은 고딕",11),fg="RoyalBlue4",bg="white")
    b.pack()

    labels=Label(nwordtest, text="3. 엑셀에서 실행취소할 때 사용하는 단축키는? ",font=("맑은 고딕",11),fg="RoyalBlue4", bg="LightSkyBlue1")
    labels.pack()

    b=Button(nwordtest, text="단축키 테스트 3번", command=qkeytest3, activebackground="orange",font=("맑은 고딕",11),fg="RoyalBlue4",bg="white")
    b.pack()
    
    labels=Label(nwordtest, text="4. 엑셀에서 위쪽 셀을 아래쪽에 붙여넣기할 때 사용하는 단축키는? ",font=("맑은 고딕",11),fg="RoyalBlue4", bg="LightSkyBlue1")
    labels.pack()

    b=Button(nwordtest, text="단축키 테스트 4번", command=qkeytest4, activebackground="orange",font=("맑은 고딕",11),fg="RoyalBlue4",bg="white")
    b.pack()

    labels=Label(nwordtest, text="5. 윈도우 화면잠금할 때 사용하는 단축키는?  ",font=("맑은 고딕",11),fg="RoyalBlue4", bg="LightSkyBlue1")
    labels.pack()

    b=Button(nwordtest, text="단축키 테스트 5번", command=qkeytest5, activebackground="orange",font=("맑은 고딕",11),fg="RoyalBlue4",bg="white")
    b.pack()

    labels=Label(nwordtest, text=" ",font=("맑은 고딕",11),fg="RoyalBlue4", bg="LightSkyBlue1")
    labels.pack()

    labels=Label(nwordtest, text=" 수고하셨습니다 ^^  ",font=("맑은 고딕",11),fg="RoyalBlue4",bg="LightSkyBlue1")
    labels.pack()
    


    

#단축키 테스트 버튼 생성
b=Button(pro, text="3-2. 단축키 테스트",command=keytest, activebackground="orange",font=("맑은 고딕",11),fg="olive drab", bg="ivory2")
b.place(x=310, y=420)


#점심메뉴 랜덤 
import random

#점심메뉴 추천 라벨생성
la=Label(pro, text="4장. 선택하기 어려운 점심메뉴를 추천해드립니다.",font=("맑은 고딕", 12), fg="olive drab", bg="LemonChiffon2")
la.place(x=180, y=490)

#점심 추천 메뉴
korea = ["떡볶이","비빔밥","김치찌개","불고기","쌈밥"]
usa = ["파스타","리조또","햄버거","뇨끼","피자"]
china = ["짜장면","마라탕","짬뽕","마파두부","고추잡채"]
japan = ["초밥","오니기리","가츠동","라멘","규동"]
all = ["카레","케밥","쌀국수","팟타이","부대찌개","감자탕","뼈해장국","김밥","죽","삼겹살","족발"]

#점심메뉴 추천  클릭 후 점심메뉴 확인 실행
def lunch():
    
    nlunch = Toplevel(pro)
    nlunch.title("점심메뉴 추천 실행")
    nlunch.geometry("250x250")
    nlunch.configure(background="DarkSeaGreen1")

    def check():
        random_korea = random.randint(0,4)
        random_usa = random.randint(0,4)
        random_china = random.randint(0,4)
        random_japan = random.randint(0,4)
        random_all = random.randint(0,10)
        str = ' '
        if ch1.get() == 1:
            str = str+korea[random_korea]
        if ch2.get() == 1:
            str = str+usa[random_usa]
        if ch3.get() == 1:
            str = str+china[random_china]
        if ch4.get() == 1:
            str = str+japan[random_japan]
        if ch5.get() == 1:
            str = str+all[random_all]
        if str == ' ':
            str = "점심메뉴 종류를 선택하세요."
        messagebox.showinfo("점심메뉴 선택 결과: ",str)

    ch1 = IntVar()
    ch2 = IntVar()
    ch3 = IntVar()
    ch4 = IntVar()
    ch5 = IntVar()
    
    c_btn1=Checkbutton(nlunch, text="한식",variable=ch1,font=("맑은 고딕",11),fg="dark olive green", bg="white")
    c_btn2=Checkbutton(nlunch, text="양식",variable=ch2,font=("맑은 고딕",11),fg="dark olive green", bg="white")
    c_btn3=Checkbutton(nlunch, text="중식",variable=ch3,font=("맑은 고딕",11),fg="dark olive green", bg="white")
    c_btn4=Checkbutton(nlunch, text="일식",variable=ch4,font=("맑은 고딕",11),fg="dark olive green", bg="white")
    c_btn5=Checkbutton(nlunch, text="랜덤",variable=ch5,font=("맑은 고딕",11),fg="dark olive green", bg="white")

    c_btn1.pack()
    c_btn2.pack()
    c_btn3.pack()
    c_btn4.pack()
    c_btn5.pack()
    
    b=Button(nlunch, text="추천 메뉴 확인",command=check,font=("맑은 고딕",11),fg="dark olive green", bg="white")
    b.pack()

 
#점심메뉴 추천 버튼 생성
b=Button(pro, text="4. 점심메뉴 추천",command=lunch, activebackground="orange",font=("맑은 고딕",11),fg="olive drab", bg="ivory2")
b.place(x=320, y=530)



#전체 창 설정
pro.mainloop()
