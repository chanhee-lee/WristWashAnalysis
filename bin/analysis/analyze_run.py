import build_model
import evaluate

trainfilename = "../../raw/total_gestures_combined.csv" # for all participant
#trainfilename = "../../raw/participant3/gesture_combined3.csv"
savename = "../../model/model_test.pkl"
testfilename = "../../raw/participant5/gesture_combined5.csv"

# Build and Evaluate for Total Gesture 
build_model.bm(trainfilename, savename)
print "Model Used: " + str(trainfilename)
print "Score: " + str(evaluate.ea(savename, testfilename))
print "For: " + str(testfilename)