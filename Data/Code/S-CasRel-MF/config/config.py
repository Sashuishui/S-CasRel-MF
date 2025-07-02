class Config():
    def __init__(self):
        self.dataset = "test"
        self.rel_num = 50
        self.bert_path = "../lert" # 绝对路径 bert
        self.train_data = "./dataset/" + self.dataset + "/train_data.json"
        self.dev_data = "./dataset/" + self.dataset + "/dev_data.json"
        self.test_data = "./dataset/" + self.dataset + "/dev_data.json"
        self.schema = "./dataset/" + self.dataset + "/schemas.json"
        self.log = "log/{}_log.log".format(self.dataset)
        self.learning_rate = 1e-5
        self.batch_size = 32
        self.epoch = 400
        self.step = 5
        self.val_epoch = 5
        self.h_bar = 0.5
        self.t_bar = 0.5
        self.save_model = "checkpoint/{}_model.pt".format(self.dataset)
        self.dev_result = "dev_result/{}_dev.json".format(self.dataset)
        self.test_result = "test_result/{}_test.json".format(self.dataset)