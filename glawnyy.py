import cv2
import mediapipe as mp
import numpy as np
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

def prisedaniye(l_shoulder, l_hip, l_knee, r_shoulder, r_hip, r_knee, l_ankle, r_ankle, counter, stage):
    # Calculate angle (wycisleniye ugla)
    l_hip_angle = calculate_angle(l_shoulder, l_hip, l_knee)

    # # Visualize (Wizualizirowat)
    # cv2.putText(image, str(l_hip_angle),
    #             tuple(np.multiply(l_hip, [640, 480]).astype(int)),
    #                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
    #             )
    r_hip_angle = calculate_angle(r_shoulder, r_hip, r_knee)

    # # Visualize (Wizualizirowat)
    # cv2.putText(image, str(r_hip_angle),
    #             tuple(np.multiply(r_hip, [640, 480]).astype(int)),
    #             cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
    #             )
    l_knee_angle = calculate_angle(l_hip, l_knee, l_ankle)

    # # Visualize (Wizualizirowat)
    # cv2.putText(image, str(l_knee_angle),
    #             tuple(np.multiply(l_knee, [640, 480]).astype(int)),
    #             cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
    #             )
    r_knee_angle = calculate_angle(r_hip, r_knee, r_ankle)

    # # Visualize (Wizualizirowat)
    # cv2.putText(image, str(r_knee_angle),
    #             tuple(np.multiply(r_knee, [640, 480]).astype(int)),
    #             cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
    #             )

    # Curl counter logic (Логика счетчика завитков)
    if l_hip_angle < 130 and r_hip_angle < 130 and l_knee_angle < 140 and r_knee_angle < 140:
        stage = 'down'
    elif l_hip_angle > 160 and r_hip_angle > 160 and l_knee_angle > 160 and r_knee_angle > 160 and stage == 'down':
        stage = 'up'
        counter += 1
        print('def_counter: ', counter)
    return counter, stage


def jump(l_shoulder, r_shoulder, l_hip, r_hip, l_knee, r_knee, l_elbow, r_elbow, counter, stage):

    l_shoulder_angle = calculate_angle(l_elbow, l_shoulder, l_hip)

    r_shoulder_angle = calculate_angle(r_elbow, r_shoulder, r_hip)

    l_hip_angle = calculate_angle(r_hip, l_hip, l_knee)

    r_hip_angle = calculate_angle(l_hip, r_hip, r_knee)

    if l_shoulder_angle > 110 and r_shoulder_angle > 110 and l_hip_angle > 100 and r_hip_angle > 100:
        stage = 'jump'
    elif l_shoulder_angle < 50 and r_shoulder_angle < 50 and l_hip_angle < 96 and r_hip_angle < 96 and stage == 'jump':
        stage = 'down'
        counter += 1
    return counter, stage


def pres(l_shoulder, r_shoulder, l_hip, r_hip, l_knee, r_knee, counter, stage, landmarks):

    l_hip_angle = calculate_angle(l_shoulder, l_hip, l_knee)

    r_hip_angle = calculate_angle(r_shoulder, r_hip, r_knee)

    l_ankle_y = landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y
    l_hip_y = landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y

    r_ankle_y = landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].y
    r_hip_y = landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y

    # l_hip_per = np.interp(l_hip_angle, (125, 160), (0, 100))
    # l_hip_bar = np.interp(l_hip_angle, (135, 160), (400, 70))
    if (l_hip_angle < 125 or r_hip_angle < 125) and (l_ankle_y - l_hip_y < 0.2 or r_ankle_y - l_hip_y < 0.2):
        stage = 'nagnulsya'
    elif (l_hip_angle > 160 or r_hip_angle > 160) and stage == 'nagnulsya':
        stage = 'lyog'
        counter += 1
    # return counter, stage, l_hip_per, l_hip_bar
    return counter, stage

def otjimaniye(l_elbow, r_elbow, l_shoulder, r_shoulder, l_hip, r_hip, counter, stage):

    l_shoulder_angle = calculate_angle(l_elbow, l_shoulder, l_hip)

    r_shoulder_angle = calculate_angle(r_elbow, r_shoulder, r_hip)

    if (l_shoulder_angle < 25) or (r_shoulder_angle < 25):
        stage = 'lyog'
    elif ((l_shoulder_angle > 55) or (r_shoulder_angle > 55)) and stage == 'lyog':
        stage = 'wstal'
        counter += 1

    return counter, stage

def wypady_na_meste(l_knee, r_knee, l_shoulder, r_shoulder, l_hip, r_hip, l_ankle, r_ankle, counter, stage):
    l_hip_angle = calculate_angle(l_shoulder, l_hip, l_knee)

    r_hip_angle = calculate_angle(r_shoulder, r_hip, r_knee)

    l_knee_angle = calculate_angle(l_hip, l_knee, l_ankle)

    r_knee_angle = calculate_angle(r_hip, r_knee, r_ankle)

    if (l_knee_angle < 95 and r_knee_angle < 95):
        if l_hip_angle < 95 and r_hip_angle > 170:
            stage = 'sidit'
        elif l_hip_angle > 170 and r_hip_angle < 95:
            stage = 'sidit'
    elif l_knee_angle > 150 and r_knee_angle > 150 and stage == 'sidit':
        stage = 'wstal'
        counter += 1

    return counter, stage


def otwedeniye_nogi_stoya(l_knee, r_knee, l_shoulder, r_shoulder, l_hip, r_hip, counter, stage):
    l_hip_angle = calculate_angle(l_shoulder, l_hip, l_knee)

    r_hip_angle = calculate_angle(r_shoulder, r_hip, r_knee)

    if l_hip_angle < 155 and r_hip_angle > 160:
        stage = 'otwyol'
    elif l_hip_angle > 160 and r_hip_angle < 155:
        stage = 'otwyol'
    elif l_hip_angle > 160 and r_hip_angle > 160 and stage == 'otwyol':
        stage = 'wstal'
        counter += 1

    return counter, stage


def otwody_nogoi_na_boku(l_knee, r_knee, l_shoulder, r_shoulder, l_hip, r_hip, counter, stage):
    l_hip_angle = calculate_angle(l_shoulder, l_hip, l_knee)

    r_hip_angle = calculate_angle(r_shoulder, r_hip, r_knee)

    if l_hip_angle < 133 and r_hip_angle > 160:
        stage = 'otwyol'
    elif l_hip_angle > 160 and r_hip_angle < 133:
        stage = 'otwyol'
    elif l_hip_angle > 160 and r_hip_angle > 160 and stage == 'otwyol':
        stage = 'lejit'
        counter += 1

    return counter, stage


def mostik_s_mahom_nogoi(l_knee, r_knee, l_shoulder, r_shoulder, l_hip, r_hip, l_ankle, r_ankle, counter, stage):
    l_hip_angle = calculate_angle(l_shoulder, l_hip, l_knee)

    r_hip_angle = calculate_angle(r_shoulder, r_hip, r_knee)

    l_knee_angle = calculate_angle(l_hip, l_knee, l_ankle)
    r_knee_angle = calculate_angle(r_hip, r_knee, r_ankle)

    if l_hip_angle < 100 and r_knee_angle < 90:
        stage = 'otwyol'
    elif l_knee_angle < 90 and r_hip_angle < 100:
        stage = 'otwyol'
    elif l_hip_angle > 160 and r_hip_angle > 160 and stage == 'otwyol':
        stage = 'lejit'
        counter += 1

    return counter, stage


def ptica(l_shoulder, r_shoulder, l_hip, r_hip, l_elbow, r_elbow, l_knee, r_knee, r_ankle, l_ankle, counter, stage):
    l_shoulder_angle = calculate_angle(l_elbow, l_shoulder, l_hip)
    r_shoulder_angle = calculate_angle(r_elbow, r_shoulder, r_hip)
    l_knee_angle = calculate_angle(l_hip, l_knee, l_ankle)
    r_knee_angle = calculate_angle(r_hip, r_knee, r_ankle)

    if l_shoulder_angle > 70 and r_shoulder_angle > 70 and l_knee_angle < 20:
        stage = 'wzmah'

    elif l_shoulder_angle < 120 and r_shoulder_angle < 120 and stage == 'wzmah':
        stage = 'wzmahul'
        counter += 1

    return counter, stage


def otjimaniya_v_kobre(l_shoulder, r_shoulder, l_hip, r_hip, l_elbow, r_elbow, l_knee, r_knee,
                       l_wrist, r_wrist, counter, stage):
    l_hip_angle = calculate_angle(l_shoulder, l_hip, l_knee)
    r_hip_angle = calculate_angle(r_shoulder, r_hip, r_knee)

    r_elbow_angle = calculate_angle(r_shoulder, r_elbow, r_wrist)
    l_elbow_angle = calculate_angle(l_shoulder, l_elbow, l_wrist)

    if l_hip_angle > 150 and l_elbow_angle < 100:
        stage = 'pos_A'

    elif r_hip_angle < 135 and r_elbow_angle > 145 and stage == 'pos_A':
        stage = 'pos_B'
        counter += 1

    return counter, stage


def skreshivaniye_ruk_sidya(l_shoulder, r_shoulder, l_hip, r_hip, l_elbow, r_elbow, l_knee, r_knee,
                            r_ankle, l_ankle, counter, stage):
    r_shoulder_angle = calculate_angle(l_shoulder, r_shoulder, r_elbow)
    l_shoulder_angle = calculate_angle(r_shoulder, l_shoulder, l_elbow)

    r_knee_angle = calculate_angle(r_ankle, r_knee, r_hip)
    l_knee_angle = calculate_angle(l_ankle, l_knee, l_hip)

    if l_shoulder_angle < 95 and r_shoulder_angle < 95 and l_knee_angle < 90:
        stage = 'pos_A'

    elif l_shoulder_angle > 115 and r_shoulder_angle > 115 and l_knee_angle < 90 and stage == 'pos_A':
        stage = 'pos_B'
        counter += 1

    return counter, stage


def bokovaya_planka_s_podyomo_taza(l_shoulder, r_shoulder, l_hip, r_hip, l_elbow, r_elbow, l_knee, r_knee,
                                   counter, stage):
    r_shoulder_angle = calculate_angle(r_hip, r_shoulder, r_elbow)
    l_shoulder_angle = calculate_angle(l_hip, l_shoulder, l_elbow)

    r_hip_angle = calculate_angle(r_shoulder, r_hip, r_knee)
    l_hip_angle = calculate_angle(l_shoulder, l_hip, l_knee)

    if r_shoulder_angle > 70 and r_hip_angle > 165 and l_hip_angle > 165:
        stage = 'pos_A'
    elif l_shoulder_angle > 70 and l_hip_angle > 165 and r_hip_angle > 165:
        stage = 'pos_A'
    elif l_shoulder_angle < 70 and l_hip_angle < 165 and r_hip_angle < 165 and stage == 'pos_A':
        stage = 'pos_B'
        counter += 1
    elif r_shoulder_angle < 70 and r_hip_angle < 165 and l_hip_angle < 165 and stage == 'pos_A':
        stage = 'pos_B'
        counter += 1

    return counter, stage


def zahlesty_goleni_s_udarami_ruk(l_shoulder, r_shoulder, l_hip, r_hip, l_elbow, r_elbow, l_knee, r_knee, r_ankle,
                                  l_ankle,
                                  counter, stage):
    r_shoulder_angle = calculate_angle(r_hip, r_shoulder, r_elbow)
    l_shoulder_angle = calculate_angle(l_hip, l_shoulder, l_elbow)



    r_knee_angle = calculate_angle(r_hip, r_knee, r_ankle)
    l_knee_angle = calculate_angle(l_hip, l_knee, l_ankle)

    if r_shoulder_angle > 150 and l_shoulder_angle < 40 and r_knee_angle < 90 and l_knee_angle > 150:
        stage = 'pos_A'


    elif l_shoulder_angle > 150 and r_shoulder_angle < 40 and l_knee_angle < 90 and r_knee_angle > 150 and stage == 'pos_A':
        stage = 'pos_B'
        counter += 1

    return counter, stage


def pryjki_v_prised_s_razvedeniyem_ruk(l_shoulder, r_shoulder, l_hip, r_hip, l_elbow, r_elbow, l_knee, r_knee, r_ankle,
                                       l_ankle,
                                       counter, stage):
    r_shoulder_angle = calculate_angle(r_hip, r_shoulder, r_elbow)
    l_shoulder_angle = calculate_angle(l_hip, l_shoulder, l_elbow)

    r_knee_angle = calculate_angle(r_hip, r_knee, r_ankle)
    l_knee_angle = calculate_angle(l_hip, l_knee, l_ankle)

    r_hip_angle = calculate_angle(r_shoulder, r_hip, r_knee)
    l_hip_angle = calculate_angle(l_shoulder, l_hip, l_knee)

    # r_hip_hip_angle = calculate_angle(r_knee, r_hip, l_hip)
    # l_hip_hip_angle = calculate_angle(l_knee, l_hip, r_hip)

    if r_shoulder_angle > 160 and r_hip_angle > 165 and r_hip_angle < 100 and r_knee_angle > 160 and l_shoulder_angle > 160 and l_hip_angle > 165 and l_hip_angle < 100 and l_knee_angle > 160:
        stage = 'pos_A'


    elif r_shoulder_angle < 90 and r_hip_angle < 120 and l_hip_angle > 150 and r_knee_angle < 130 and l_shoulder_angle < 90 and l_hip_angle < 120 and r_hip_angle > 150 and l_knee_angle < 130 and stage == 'pos_A':
        stage = 'pos_B'
        counter += 1

    return counter, stage


def bokoviye_skruchivaniya_stoya(l_shoulder, r_shoulder, l_hip, r_hip, l_elbow, r_elbow, l_knee, r_knee, r_ankle,
                                 l_ankle,
                                 counter, stage):
    r_shoulder_angle = calculate_angle(r_hip, r_shoulder, r_elbow)
    l_shoulder_angle = calculate_angle(l_hip, l_shoulder, l_elbow)

    r_knee_angle = calculate_angle(r_hip, r_knee, r_ankle)
    l_knee_angle = calculate_angle(l_hip, l_knee, l_ankle)

    r_hip_angle = calculate_angle(r_knee, r_hip, l_hip)
    l_hip_angle = calculate_angle(l_knee, l_hip, r_hip)

    if r_shoulder_angle > 100 and l_shoulder_angle > 100 and r_hip_angle < 100 and l_hip_angle < 100 and r_knee_angle > 160 and l_knee_angle > 160:
        stage = 'pos_A'

    elif r_shoulder_angle < 85 and l_shoulder_angle > 120 and r_hip_angle > 165 and l_hip_angle < 145 and r_knee_angle < 85 and l_knee_angle > 160 and stage == 'pos_A':
        stage = 'pos_B'
        counter += 1



    elif l_shoulder_angle < 85 and r_shoulder_angle > 120 and l_hip_angle > 165 and r_hip_angle < 145 and l_knee_angle < 85 and r_knee_angle > 160 and stage == 'pos_A':
        stage = 'pos_C'

        counter += 1

    return counter, stage


def calculate_angle(a, b, c):
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)

    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
    angle = np.abs(radians*180.0/np.pi)

    if angle > 180:
        angle = 360 - angle

    return angle
















def osnownoy(cap, pose, pris_bool=False, jump_bool=False, pres_bool=False, otjimaniye_bool=False,
             wypady_na_meste_bool=False, otwedeniye_nogi_stoya_bool=False, otwody_nogoi_na_boku_bool=False,
             mostik_s_mahom_nogoi_bool=False, ptica_bool=False, otjimaniya_v_kobre_bool=False,
             skreshivaniye_ruk_sidya_bool=False, bokovaya_planka_s_podyomo_taza_bool=False,
             zahlesty_goleni_s_udarami_ruk_bool=False, pryjki_v_prised_s_razvedeniyem_ruk_bool=False,
             bokoviye_skruchivaniya_stoya_bool=False, counter=0, stage=None):
    ret, frame = cap.read()
    if ret:
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False

        # Make detection (obnarujeniye)
        results = pose.process(image)

        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # Extract landmarks (izwlekayem orintiry)
        try:
            landmarks = results.pose_landmarks.landmark
            # print(landmarks)


            l_shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
                        landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
            l_elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,
                        landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
            l_wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,
                        landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]
            l_hip = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,
                     landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]
            l_knee = [landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,
                     landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y]
            l_ankle = [landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x,
                     landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y]
            r_shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,
                          landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
            r_elbow = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,
                       landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
            r_wrist = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,
                       landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]
            r_hip = [landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x,
                     landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y]
            r_knee = [landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].x,
                      landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].y]
            r_ankle = [landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].x,
                       landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].y]

            if pris_bool:
                pris = prisedaniye(l_shoulder, l_hip, l_knee, r_shoulder, r_hip, r_knee, l_ankle, r_ankle, counter,
                                   stage)
                counter, stage = pris
            elif jump_bool:
                jum = jump(l_shoulder, r_shoulder, l_hip, r_hip, l_knee, r_knee, l_elbow, r_elbow, counter, stage)
                counter, stage = jum
            elif pres_bool:
                pre = pres(l_shoulder, r_shoulder, l_hip, r_hip, l_knee, r_knee, counter, stage, landmarks)
                counter, stage = pre
            elif otjimaniye_bool:
                otjim = otjimaniye(l_elbow, r_elbow, l_shoulder, r_shoulder, l_hip, r_hip, counter, stage)
                counter, stage = otjim
            elif wypady_na_meste_bool:
                wypady = wypady_na_meste(l_knee, r_knee, l_shoulder, r_shoulder, l_hip, r_hip, l_ankle, r_ankle, counter, stage)
                counter, stage = wypady
            elif otwedeniye_nogi_stoya_bool:
                otwed = otwedeniye_nogi_stoya(l_knee, r_knee, l_shoulder, r_shoulder, l_hip, r_hip, counter, stage)
                counter, stage = otwed
            elif otwody_nogoi_na_boku_bool:
                otwod = otwody_nogoi_na_boku(l_knee, r_knee, l_shoulder, r_shoulder, l_hip, r_hip, counter, stage)
                counter, stage = otwod
            elif mostik_s_mahom_nogoi_bool:
                most = mostik_s_mahom_nogoi(l_knee, r_knee, l_shoulder, r_shoulder, l_hip, r_hip, l_ankle, r_ankle, counter, stage)
                counter, stage = most
            elif ptica_bool:
                ptic = ptica(l_shoulder, r_shoulder, l_hip, r_hip, l_elbow, r_elbow, l_knee, r_knee, r_ankle, l_ankle, counter, stage)
                counter, stage = ptic
            elif otjimaniya_v_kobre_bool:
                otjim = otjimaniya_v_kobre(l_shoulder, r_shoulder, l_hip, r_hip, l_elbow, r_elbow, l_knee, r_knee,
                       l_wrist, r_wrist, counter, stage)
                counter, stage = otjim
            elif skreshivaniye_ruk_sidya_bool:
                skresh = skreshivaniye_ruk_sidya(l_shoulder, r_shoulder, l_hip, r_hip, l_elbow, r_elbow, l_knee, r_knee,
                            r_ankle, l_ankle, counter, stage)
                counter, stage = skresh
            elif bokovaya_planka_s_podyomo_taza_bool:
                bokovaya = bokovaya_planka_s_podyomo_taza(l_shoulder, r_shoulder, l_hip, r_hip, l_elbow, r_elbow, l_knee, r_knee,
                                   counter, stage)
                counter, stage = bokovaya
            elif zahlesty_goleni_s_udarami_ruk_bool:
                zahlesty = zahlesty_goleni_s_udarami_ruk(l_shoulder, r_shoulder, l_hip, r_hip, l_elbow, r_elbow, l_knee, r_knee, r_ankle,
                                  l_ankle,
                                  counter, stage)
                counter, stage = zahlesty
            elif pryjki_v_prised_s_razvedeniyem_ruk_bool:
                pryj = pryjki_v_prised_s_razvedeniyem_ruk(l_shoulder, r_shoulder, l_hip, r_hip, l_elbow, r_elbow, l_knee, r_knee, r_ankle,
                                       l_ankle,
                                       counter, stage)
                counter, stage = pryj
            elif bokoviye_skruchivaniya_stoya_bool:
                bokovaya = bokoviye_skruchivaniya_stoya(l_shoulder, r_shoulder, l_hip, r_hip, l_elbow, r_elbow, l_knee, r_knee, r_ankle,
                                 l_ankle,
                                 counter, stage)
                counter, stage = bokovaya


            # prisedaniye(l_shoulder, l_hip, l_knee, r_shoulder, r_hip, r_knee, l_ankle, r_ankle, counter, stage)
            # print('stage: ', stage)
            # print('counter: ', counter)
            # pre = pres(l_shoulder, r_shoulder, l_hip, r_hip, l_knee, r_knee, counter, stage)
            # counter, stage, per, bar = pre
            # jum = jump(l_shoulder, r_shoulder, l_hip, r_hip, l_knee, r_knee, l_elbow, r_elbow, counter, stage)
            # counter, stage = jum
            #
            # # print('l_hip_y: ', landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y)
            # # print('l_ankle_y: ', landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y)
            # print('per: ', per)
            # print('bar: ', bar)

            # otjim = otjimaniye(l_elbow, r_elbow, l_shoulder, r_shoulder, l_hip, r_hip, counter, stage)
            # counter, stage = otjim




            # cv2.rectangle(image, (550, 70), (600, 400), (0, 255, 0), 3)
            # cv2.rectangle(image, (550, int(bar)), (600, 400), (0, 255, 0), cv2.FILLED)
            # cv2.putText(image, f'{int(per)} %', (500, 57), cv2.FONT_HERSHEY_PLAIN, 4, (255, 0, 0), 4)
            # print()




            # angle = calculate_angle(r_elbow, r_shoulder, r_hip)
            #
            # # Visualize (Wizualizirowat)
            # cv2.putText(image, str(angle),
            #             tuple(np.multiply(r_shoulder, [640, 480]).astype(int)),
            #                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
            #             )



        except Exception as ex:
            print(ex)
            pass

        # Render curl counter (Счетчик скручивания рендеринга)
        # Setup status box (Окно состояния установки)
        cv2.rectangle(image, (0, 0), (225, 73), (245, 117, 16), -1)

        # Rep data (Данные о репутации)
        cv2.putText(image, 'REPS', (15, 12),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
        cv2.putText(image, str(counter), (10, 60),
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2, cv2.LINE_AA)

        # Stage data (Данные этапа)
        cv2.putText(image, 'STAGE', (65, 12),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
        cv2.putText(image, stage, (60, 60),
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2, cv2.LINE_AA)

        # risuyet tocki i linii
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                  mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=2), # swet tocki na tele
                                  mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2),) # swet palok na tele

        # print(results)

        return image, counter, stage
