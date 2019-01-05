#include<iostream>
#include<conio.h>
#include<vector>
#include<windows.h>
#include<string>
#include<fstream>

using namespace std;

struct nhanVien{
	string manv;
	string hoten;
	int tuoi;
	long int luongcb;
};

typedef struct nhanVien nv;

vector< nv > dsnv; //list of staff

//adding a staff to staff list
//input: a staff
//output: a staff added to staff list
void addingAStaff(nv a){
	dsnv.push_back(a);
}

//get the original staff list from the company
//input: company name, which is also file's name
//output: staff list got data from the file
void getStaffFromFile(string file_name){
	ifstream infile;
	infile.open(file_name.c_str());
	while (!infile.eof())
	{
		nv temp;
		getline(infile, temp.manv);
		getline(infile, temp.hoten);
		infile>>temp.tuoi; infile.ignore(256, '\n');
		infile>>temp.luongcb; infile.ignore(256, '\n');
		addingAStaff(temp);
	}
	infile.close();
}

//create a staff using keyboard
//input: nothing
//output: a staff
nv createAStaffUsingKeyboard(){
	nv temp;
	cout<<"Please type in the staff info:\n";
	cout<<"ID: "; fflush(stdin); getline(cin, temp.manv);
	cout<<"Full name: "; fflush(stdin); getline(cin, temp.hoten);
	cout<<"Age: "; cin>>temp.tuoi;
	cout<<"Salary: "; cin>>temp.luongcb;
	return temp;
}

//add new staff to company's staff file
//input: company name, which is also file's name
//output: new staff's data written in file
void addingNewStaffToFile(string file_name, nv a){
	ofstream outfile;
	outfile.open(file_name.c_str(), ios::out | ios::app);
	outfile<<endl<<a.manv<<endl;
	outfile<<a.hoten<<endl;
	outfile<<a.tuoi<<endl;
	outfile<<a.luongcb;
	outfile.close();
}

//check if a staff exists in list
//input: staff id
//output: index of the staff with that id
int staffIndex(string a){
	for (int i=0; i<dsnv.size(); i++)
		if (a.compare(dsnv[i].manv)==0) return i;
	return -1;
}

//remove a staff from staff list
//input: staff ID
//output: staff removed from staff list
void removeAStaff(string a){
	int target = staffIndex(a);
	if (target<0)
		cout<<"\nStaff not found.";
	else
	{
		dsnv.erase(dsnv.begin() + target);
		cout<<"\nStaff removed.";
	}
}

//look for a staff by their id
//input: staff id
//output: staff info printed to console
bool lookForAStaff(string a){
	system("cls");
	if (staffIndex(a)<0) cout<<"Staff not found.";
	else
	{
		int ind=staffIndex(a);		
		cout<<"\nFull name:\t"<< dsnv[ind].hoten;
		cout<<"\nID:\t\t"<< dsnv[ind].manv;
		cout<<"\nAge:\t\t"<< dsnv[ind].tuoi;
		cout<<"\nSalary:\t\t"<<dsnv[ind].luongcb;
	}
}

//edit a staff info
//input: staff id
//output: a staff's info changed
void editStaff(string id){
	int ind = staffIndex(id);
	if (ind<0) cout<<"Staff not found.";
	else
	{
		cout<<"Please type in the staff's new info:\n";
		cout<<"New ID: "; fflush(stdin); getline(cin, dsnv[ind].manv);
		cout<<"New full name: "; fflush(stdin); getline(cin, dsnv[ind].hoten);
		cout<<"New age: "; cin>>dsnv[ind].tuoi;
		cout<<"New salary: "; cin>>dsnv[ind].luongcb;
	}
}

//print staff list to console
//input: nothing
//output: staff list printed to console
void printStaffList(){
	system("cls");
	for (int i=0; i<dsnv.size(); i++)
	{
		cout<<"\nFull name:\t"<< dsnv[i].hoten;
		cout<<"\nID:\t\t"<< dsnv[i].manv;
		cout<<"\nAge:\t\t"<< dsnv[i].tuoi;
		cout<<"\nSalary:\t\t"<<dsnv[i].luongcb;
		cout<<endl;
	}
}

main(){
	string company_name;
	cout<<"Which company do you want to work with? "; cin>>company_name;
	while (company_name.compare("companyA")!=0 and company_name.compare("companyB")!=0 and company_name.compare("companyC")!=0 and company_name.compare("companyD")!=0)
	{
		fflush(stdin);
		cout<<"Please type in an existed company! "; cin>>company_name;
	}
	company_name += ".txt";
	getStaffFromFile(company_name);
	while (true)
	{
		int control;
		system("cls");
		cout<<"0. Exit.\n";
		cout<<"1. Add a staff.\n";
		cout<<"2. Remove a staff.\n";
		cout<<"3. Look for a staff.\n";
		cout<<"4. Edit a sfaff.\n";
		cout<<"5. Print staff list.\n";
		cout<<"Please choose a number from the menu: "; cin>>control;
		if (control==0)
		{
			cout<<"Programme exited.\n";
			getch();
			break;
		}
		if (control==1)
		{
			nv a;
			a=createAStaffUsingKeyboard();
			addingAStaff(a);
			addingNewStaffToFile(company_name, a);
		}
		if (control==2)
		{
			string a;
			cout<<"Please type in the ID of the fired staff: ";
			fflush(stdin); getline(cin, a);
			removeAStaff(a);
		}
		if (control==3)
		{
			string a;
			cout<<"Please type in the ID of the staff: "; fflush(stdin); getline(cin, a);
			lookForAStaff(a);
		}
		if (control==4)
		{
			string target;
			cout<<"Please type in the ID of the staff: "; fflush(stdin); getline(cin, target);
			editStaff(target);
		}
		if (control==5) printStaffList();
		getch();
	}
}
