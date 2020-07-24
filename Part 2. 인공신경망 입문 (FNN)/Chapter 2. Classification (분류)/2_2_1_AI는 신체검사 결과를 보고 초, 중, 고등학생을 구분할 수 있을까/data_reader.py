"""
Author : Byunghyun Ban
Date : 2020.07.17.
"""
import numpy as np
import os
import random


# 데이터를 떠먹여 줄 클래스를 제작합니다.
class DataReader():
    def __init__(self, datadir):
        # 읽어올 파일 이름을 저장할 변수입니다.
        filename = []

        # 학습할 데이터가 저장된 폴더 이름을 입력받습니다.
        self.datadir = datadir

        # 해당 폴더 안에 있는 파일들을 목록화 합니다.
        files = os.listdir(self.datadir)

        # 이번 예제에서는 ".csv"파일을 사용할 계획이므로, ".csv"파일만 골라냅니다.
        for el in files:
            if ".csv" not in el:
                continue
            filename.append(el)

        # 이번 예제에서는 단 하나의 csv 파일만 사용할 계획이므로
        # 폴더 안의 CSV파일 개수가 1개가 아닐 경우 경고를 출력하며 시스템을 종료합니다.
        if len(filename) != 1:
            print("Please Provide Only 1 CSV file in data/ directory.")
            exit(1)

        # 최종 확인된 파일 이름을 지정합니다.
        self.filename = filename[0]

        # 데이터를 저장할 변수들입니다.
        self.train_X = []
        self.train_Y = []
        self.test_X = []
        self.test_Y = []

        # 본격적으로 파일을 읽어옵니다.
        self.read_data()

    # 데이터를 읽어오기 위한 매서드입니다.
    def read_data(self):
        # 파일을 실행합니다.
        file = open(self.datadir + "/" + self.filename)

        # 헤더를 제거합니다.
        file.readline()

        # 데이터와 레이블을 저장하기 위한 변수입니다.
        X = []
        Y = []

        # 파일을 한 줄씩 읽어옵니다.
        for line in file:
            # 컴마를 기준으로 split()을 실행합니다.
            splt = line.split(",")

            # split 결과물을 정리해 X값과 Y값으로 추립니다.
            data, cls = self.process_data(splt)

            # 추려낸 데이터를 저장합니다.
            X.append(data)
            Y.append(cls)

        # 데이터를 np.array 형태로 변환합니다.
        X = np.asarray(X)
        Y = np.asarray(Y)

        # 데이터를 노멀라이즈 합니다. 각 컬럼별 최대값으로 나눠줍니다.
        # 이 과정에서 데이터의 값이 최소 0부터 최대 1까지로 변환됩니다.
        X[:, 0] /= np.max(X[:, 0])
        X[:, 1] /= np.max(X[:, 1])
        X[:, 2] /= np.max(X[:, 2])

        # 트레이닝 데이터와 테스트 데이터를 분리할 것입니다.
        for i in range(len(X)):
            # 매번 임의로 70% 데이터를 트레이닝 데이터로 편입시키고
            # 나머지 30% 데이터를 테스트 데이터로 편입시킵니다.
            # random.random() 기반이므로 실행할 때마다 트레이닝 데이터와 테스트 데이터가
            # 다르게 분배됩니다.
            if random.random() < 0.7:
                self.train_X.append(X[i])
                self.train_Y.append(Y[i])
            else:
                self.test_X.append(X[i])
                self.test_Y.append(Y[i])

        # 최종적으로 변수를 np.array 형태로 정리합니다.
        self.train_X = np.asarray(self.train_X)
        self.train_Y = np.asarray(self.train_Y)
        self.test_X = np.asarray(self.test_X)
        self.test_Y = np.asarray(self.test_Y)

        # 데이터 읽기가 완료되었습니다.
        # 읽어온 데이터의 정보를 출력합니다.
        print("\n\nData Read Done!")
        print("Training X Size : " + str(self.train_X.shape))
        print("Training Y Size : " + str(self.train_Y.shape))
        print("Test X Size : " + str(self.test_X.shape))
        print("Test Y Size : " + str(self.test_Y.shape) + '\n\n')

    # split() 값을 정리하기 위한 매서드입니다.
    def process_data(self, splt):
        # 읽어온 splt 값에서 학교, 성별, 키, 몸무게만 추출합니다.
        school = splt[9]
        gender = splt[13]
        height = float(splt[15])
        weight = float(splt[16])

        # 완성된 데이터를 저장할 변수입니다.
        data = []

        # 키와 몸무게를 삽입합니다.
        data.append(height)
        data.append(weight)

        # 성별을 삽입합니다. 남자일 경우 1, 여자일 경우 0을 삽입합니다.
        if gender == "남":
            data.append(1)
        else:
            data.append(0)

        # 초등학교, 중학교, 고등학교 정보를 원 핫 벡터로 정리합니다.
        # cls는 레이블 역할을 수행합니다.
        if school.endswith("초등학교"):
            cls = [1, 0, 0]
        elif school.endswith("중학교"):
            cls = [0, 1, 0]
        elif school.endswith("고등학교"):
            cls = [0, 0, 1]

        # 결과물을 리턴합니다.
        return data, cls
