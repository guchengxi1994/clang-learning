
#ifdef CREATEDELL_API_DU
#else                                                                            
#define CREATEDELL_API_DU _declspec(dllimport) //当编译时，头文件不参加编译，所以.cpp文件中先定义，后头文件被包含进来，因此外部使用时，为dllexport，而在内部编译时，则为dllimport
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

class  CREATEDELL_API_DU Dog :public Animal     //需要被调用的类（子类dog）
{
public:
	int outDate();
};


int CREATEDELL_API_DU exportDate();