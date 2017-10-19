import os
import shutil
from psychopy.tools.fileerrortools import handleFileCollision
import pickle
global saved


def dm11_start(data, expInfo, logging, thisExp, _thisDir, expName):
    global saved
    base = u'V:\\users\\Aaron'
    date = data.getDateStr(format='%y%m%d')
    filename = '%s\\%s_%s\\%s\\vis' % (base, date,
                                       expInfo['participant'], expInfo['Run'])
    directory = os.path.dirname(filename)
    if not os.path.exists(directory):
        os.makedirs(directory)
    saved = False
    logging.filename = filename + '.log'
    thisExp.filename = filename
    src = _thisDir + '\\' + expName + '.psyexp'
    des = directory + '\\' + expName + '.psyexp'
    if os.path.exists(des):
        des = handleFileCollision(des, fileCollisionMethod='rename')
    shutil.copy(src, des)
    print('copied %s to %s' % (src, des))
    return filename


def dm11_trial(filename, trials):
    global saved
    if not saved:
        p_filename = filename + '.p'
        if os.path.exists(p_filename):
            p_filename = handleFileCollision(p_filename, fileCollisionMethod='rename')
        pickle.dump(trials, open(p_filename, 'wb'))
        saved = True
        print('Saved to %s' % p_filename)
