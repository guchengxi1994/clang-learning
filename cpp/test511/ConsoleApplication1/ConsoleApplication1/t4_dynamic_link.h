
#ifdef CREATEDELL_API_DU
#else                                                                            
#define CREATEDELL_API_DU _declspec(dllimport) //������ʱ��ͷ�ļ����μӱ��룬����.cpp�ļ����ȶ��壬��ͷ�ļ�����������������ⲿʹ��ʱ��Ϊdllexport�������ڲ�����ʱ����Ϊdllimport
#endif 

class CREATEDELL_API_DU  Animal {
public:
	virtual int outDated() = 0;
	void getWide(int x);
	void getHigh(int y);
	int wide;
	int high;
};

class CREATEDELL_API_DU Cat:Animal {
public:
	int outDate();
};

class  CREATEDELL_API_DU Dog :public Animal     //��Ҫ�����õ��ࣨ����dog��
{
public:
	int outDate();
};


int CREATEDELL_API_DU exportDate();