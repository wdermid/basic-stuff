//decimalrounding.cpp asks the user for a value and decimal point to be rounded to

#include "std_lib_facilities.h"

int main()
{
	double value;
	double decimal;
	double container;
	int precision;
	int power;
	int truncate;
	
	cout<<"===Enter a value to be rounded and to what decimal point===\n";
	cout<<"Value: ";
	while (cin>>value) {
		cout<<"Decimal Point: ";
		cin>>precision;
		power = 1;
		while (precision > 0) {
			power *= 10;
			--precision;
		}
		truncate = value;
		decimal = value - truncate;
		value -= decimal;
		container = decimal * power;
		truncate = container;
		container = truncate;
		decimal *= power*10;
		truncate = decimal;
		truncate %= 10;
		truncate /= 5;
		container += truncate;
		container /= power;
		value += container;
		
		cout<<"Rounded value: "<<value<<"\n";
		cout<<"===Enter a value to be rounded and to what decimal point===\n";
		cout<<"Value: ";
	}
}