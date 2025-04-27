from emotion_detection import EmotionDetector
from arm_movement import ArmAction

run = False
detector = EmotionDetector()
arm = ArmAction()

def main():
    print("Hello, I'm Marky your personal artistic emotion interpreter.")

    while True:
        
        userInput = input("Enter start in the command line to begin.").lower()
        print(userInput)
        
        if userInput == "start":
            #start emotion detection
            run = True
            detector.emotion_detection()
            topEmotions, highestEmotion = detector.get_emotions(run)
            
            print("Top emotions:" + str(topEmotions))
            # print("this is the highest emotion" + str(highestEmotion)+ type(highestEmotion))
            
            ##Extreme Cases##
            print(topEmotions.get(highestEmotion))
            if topEmotions.get(highestEmotion) >= float(95):
                if highestEmotion == 'happy':
                    arm.collect_dark_orange_stamp()
                    arm.draw_row_1()
                    arm.collect_dark_orange_stamp()
                    arm.draw_row_2()
                    arm.collect_dark_orange_stamp()
                    arm.draw_row_3()

                if highestEmotion == 'sad':
                    arm.collect_dark_blue_stamp()
                    arm.draw_row_1()
                    arm.collect_dark_blue_stamp()
                    arm.draw_row_2()
                    arm.collect_dark_blue_stamp()
                    arm.draw_row_3()

                if highestEmotion == 'neutral':
                    arm.collect_dark_green_stamp()
                    arm.draw_row_1()
                    arm.collect_dark_green_stamp()
                    arm.draw_row_2()
                    arm.collect_dark_green_stamp()
                    arm.draw_row_3()

            ##Intermediate Cases##
            if topEmotions.get(highestEmotion) < float(95) and topEmotions.get(highestEmotion) >= float(40):
                print("entered loop")
                #sorting emotions to get second highest emotion
                print("this is the lengthe of the dict" + str(len(topEmotions))+str(topEmotions))
                sorted_emotions = dict(sorted(topEmotions.items(), key=lambda item: item[1], reverse=True))
                print("sorted emotions" + str(sorted_emotions))
                secondHighestEmotion = list(sorted_emotions.keys())[1]
                print("this is the secondHighestEmotion" + str(secondHighestEmotion))

                if highestEmotion == 'happy':
                    if secondHighestEmotion == 'sad':
                        arm.collect_dark_orange_stamp()
                        arm.draw_row_1()
                        arm.collect_light_blue_stamp()
                        arm.draw_row_2()
                        arm.collect_dark_orange_stamp()
                        arm.draw_row_3()
                    if secondHighestEmotion == 'neutral':
                        arm.collect_dark_orange_stamp()
                        arm.draw_row_1()
                        arm.collect_light_green_stamp()
                        arm.draw_row_2()
                        arm.collect_dark_orange_stamp()
                        arm.draw_row_3()

                
                if highestEmotion == 'sad':
                    if secondHighestEmotion == 'happy':
                        arm.collect_dark_blue_stamp()
                        arm.draw_row_1()
                        arm.collect_light_orange_stamp()
                        arm.draw_row_2()
                        arm.collect_dark_blue_stamp()
                        arm.draw_row_3()
                    if secondHighestEmotion == 'neutral':
                        arm.collect_dark_blue_stamp()
                        arm.draw_row_1()
                        arm.collect_light_green_stamp()
                        arm.draw_row_2()
                        arm.collect_dark_blue_stamp()
                        arm.draw_row_3()
                        
                if highestEmotion == 'neutral':
                    if secondHighestEmotion == 'sad':
                        arm.collect_dark_green_stamp()
                        arm.draw_row_1()
                        arm.collect_light_blue_stamp()
                        arm.draw_row_2()
                        arm.collect_dark_green_stamp()
                        arm.draw_row_3()
                    if secondHighestEmotion == 'happy':
                        arm.collect_dark_green_stamp()
                        arm.draw_row_1()
                        arm.collect_light_orange_stamp()
                        arm.draw_row_2()
                        arm.collect_dark_green_stamp()
                        arm.draw_row_3()

            ##Else##
            else:
                arm.collect_light_orange_stamp()
                arm.draw_row_1()
                arm.collect_light_blue_stamp()
                arm.draw_row_2()
                arm.collect_light_green_stamp()
                arm.draw_row_3()

        else:
            break

    detector.close_window()

if __name__ == "__main__":
    main()
    