/* dynamic array implementation only deals with integer types */
#include <iostream>

int MAX_SIZE = 2;
// the tail of the array
int tail = -1;

int size(){
  return tail + 1;
}

bool check_max_reached(){
  return tail == MAX_SIZE;
}

int* duplicate_array(int *array){
  int original_max = MAX_SIZE;
  MAX_SIZE = MAX_SIZE * 2;
  int *new_array = new int[MAX_SIZE];
  memset(new_array, 0, sizeof new_array);
  for (int i = 0; i <= original_max; ++i)
  {
    new_array[i] = array[i];
  }
  return new_array;
}

int* right_shift(int *array,int index){
  // std::cout << size();
  for (int i = tail + 1; i >= index; --i)
  {
    array[i] = array[i - 1];
  }
  // for (int i = 0; i < MAX_SIZE; ++i)
  // {
  //   /* code */
  //   std::cout << array[i];
  // }
  // for (int i = 0; i < MAX_SIZE; ++i)
  // {
  //   /* code */
  //   std::cout << "size" << std::endl;;
  //   std::cout << tail + 1 << std::endl;
  //   std::cout << "array" << std::endl;;
  //   std::cout << array[i] << std::endl;;
  // }
  return array;
}

int* insert(int value, int index, int *array){
  tail += 1;
  bool max_reached = check_max_reached();
  if (max_reached){
    int *duplicate = duplicate_array(array);
    int *right_shifted_array = right_shift(duplicate, index);
    right_shifted_array[index] = value;
    return right_shifted_array;
  }else{
    int *right_shifted_array = right_shift(array,index);
    right_shifted_array[index] = value;
    return right_shifted_array;
  }
}

//inserts at the tail
int* insert(int value, int *array){
  tail += 1;
  bool max_reached = check_max_reached();
  if (max_reached){
    int *duplicate = duplicate_array(array);
    int size_of_array = size();
    int index = size_of_array - 1;
    duplicate[index] = value;
    return duplicate;
  }else{
    int size_of_array = size();
    int index = size_of_array - 1;
    array[index] = value;
    return array;
  }
}

void left_shift(int index, int *array){
  for (int i = index; i < size() - 1; ++i) {
    array[i] = array[i + 1];
  }
}

int* remove(int index, int *array){
  left_shift(index,array);
  tail--;
  return array;
}

int* quick_sort(int *array){

}

int* remove_elment(int value, int *array){
  quick_sort(array);

}

int main(){
  // global array to perform operations on
  int array[MAX_SIZE];
  memset(array, 0, sizeof array);
  insert(1, array);
  insert(2, array);
  remove(0,array);
//  int *check = insert(3, array);
//  insert(2, 0, array);
////  insert(3, 0, array);
//  int *check1 =insert(3, 0, array);
//  for (int i = 0; i < MAX_SIZE; ++i)
//  {
//    std::cout << check1[i];
//  }
//  std::cout << std::endl;
//  int *check2 =insert(4, 0, check1);
//  for (int i = 0; i < MAX_SIZE; ++i)
//  {
//    std::cout << check2[i];
//  }
//  std::cout << std::endl;
//  int *check3 = insert(5, 0, check2);
//  int *check4 = insert(6, 0, check3);
//  int *check5 =insert(7, 0, check4);
  for (int i = 0; i < tail + 1; ++i)
  {
    std::cout << array[i] << std::endl;
  }

}