class Path(object):
# HRDN-DEMOIRE
    @staticmethod
    def train_dir():
        #training data path
        train_path = '/database/jhkim/Moire_generated/gray_affine_train/'

        #validating data path
        val_path = '/database/jhkim/Moire_generated/gray_affine_valid/'

        #save model into save_path
        save_path = '/database/jhkim/PTHfolder/HRDN-affine_gray/'

        return train_path,val_path,save_path

    @staticmethod
    def test_dir():
        #testing data path
        in_dir = '/database/jhkim/AutoModel_정포커스/grayconcat2/'

        #save result into result_dir
        out_dir = '/database/jhkim/Result/affine_result/'

        return in_dir, out_dir

    @staticmethod
    def model_dir():
        return '/home/jhkim/DataSet/PTH_folder/0521/HRDN_generatedMoire_grayP=27.659_0518_13_19_51.pth' # 잘됨. 
