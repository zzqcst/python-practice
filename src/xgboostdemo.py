import xgboost as xgb
from sklearn.metrics import accuracy_score
dtrain = xgb.DMatrix("../data/agaricus.txt.train")
dtest = xgb.DMatrix("../data/agaricus.txt.test")
'''
max_depth： 树的最大深度。缺省值为6，取值范围为：[1,∞]
eta：为了防止过拟合，更新过程中用到的收缩步长。在每次提升计算之后，算法会直接获得新特征的权重。 
eta通过缩减特征的权重使提升计算过程更加保守。缺省值为0.3，取值范围为：[0,1]
silent：取0时表示打印出运行时信息，取1时表示以缄默方式运行，不打印运行时信息。缺省值为0
objective： 定义学习任务及相应的学习目标，“binary:logistic” 表示二分类的逻辑回归问题，输出为概率。
'''
param = {'max_depth':2, 'eta':1, 'silent':0, 'objective':'binary:logistic' }


# 设置boosting迭代计算次数
num_round = 2
bst = xgb.train(param, dtrain, num_round)
train_preds = bst.predict(dtest)
train_predictions = [round(value) for value in train_preds]
y_train = dtrain.get_label() #值为输入数据的第一行
train_accuracy = accuracy_score(y_train, train_predictions)
print("Train Accuary: %.2f%%" % (train_accuracy * 100.0))