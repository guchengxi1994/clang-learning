#define CREATEDELL_API_DU _declspec(dllexport)

#include<iostream>
#include "t4_dynamic_link.h"

using namespace std;

void Animal::getWide(int x) {
	wide = x;
}

void CREATEDELL_API_DU Animal::getHigh(int y) {
	high = y;
}

//子类cat中数据输出实现

int CREATEDELL_API_DU Cat::outDate() {
	return (wide + high); wide += wide; high += high;
}

//子类dog数据输出实现
int CREATEDELL_API_DU Dog::outDate() {
	return (wide - high);
}


int CREATEDELL_API_DU exportDate() {
	return 666;
}
