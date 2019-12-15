#include <stdio.h>
#include <math.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <iterator>
#include <sstream>
#include <string>

using namespace std;

int fuelRequired (int mass) {
  return (floor(mass/3) - 2);
}

int main () {
  ifstream infile("./input.txt");
  string line;
  vector<int> module_masses;
  
  while (getline(infile, line)) {
    istringstream iss(line);
    int n;
    while (iss >> n) {
      module_masses.push_back(n);
    } 
  }
  
  int sum = 0;
  for( int i = 0; i < module_masses.size(); i = i + 1) {
    sum = sum + fuelRequired(module_masses[i]);
  }
  cout << "Total fuel required: " << sum << endl;
  
  return 0;
}

