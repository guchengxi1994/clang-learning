
#ifndef HEADER_H_INCLUDED
#define HEADER_H_INCLUDED




#endif // HEADER_H_INCLUDED

class _T2_Box
{
public:
	_T2_Box();
	~_T2_Box();


	double getLength();
	double getHeight();
	double getWidth();
	void set(double len, double wid, double hei);
	double getSize();

private:
	double length;
	double width;
	double height;
};

double _T2_Box::getLength() {
	return this->length;
}

double _T2_Box::getHeight() {
	return this->height;
}

double _T2_Box::getWidth() {
	return this->width;
}

double _T2_Box::getSize() {
	return this->width*this->height*this->length;
}

void _T2_Box::set(double len, double wid, double hei) {
	this->height = hei;
	this->length = len;
	this->width = wid;
};

_T2_Box::_T2_Box()
{
}

_T2_Box::~_T2_Box()
{
}

class _T2_Box_Child:public _T2_Box
{
public:
	_T2_Box_Child();
	~_T2_Box_Child();
	virtual void fun()
	{
		std::cout << "dingding" << std::endl;
	}

private:
	
};

_T2_Box_Child::_T2_Box_Child()
{
}

_T2_Box_Child::~_T2_Box_Child()
{
}