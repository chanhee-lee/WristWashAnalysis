import build_model
import evaluate

trainfilename = "../../raw/total_gestures_combined.csv" # for all participant
#trainfilename = "../../raw/participant1/gesture_combined1.csv"
savename = "../../model/model_test.pkl"
testfilename = "../../raw/participant4/gesture_combined4.csv"

# Build and Evaluate for Total Gesture 
build_model.bm(trainfilename, savename)
print "Score: " + str(evaluate.ea(savename, testfilename))
print "For: " + str(testfilename)