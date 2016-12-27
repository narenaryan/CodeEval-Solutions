
package main

import ("fmt"
        "log"
        "bufio"
        "os"
        "strings"
        "strconv"
        )

func convertToInts(arr []string) []int{
    /* Function for converting an array of strings to integers*/
    finalArr := make([]int, len(arr));
    for index,val := range arr {
        finalArr[index], _ = strconv.Atoi(val);
    }
    return finalArr;
}

func convertToStrings(arr []int) []string {
    finalArr := make([]string, len(arr));
    for index,val := range arr {
        finalArr[index] = strconv.Itoa(val);
    }
    return finalArr;   
}

func isArraySorted(arr []int) bool {
    /* Function for saying whether a given array is sorted or not */
    max := arr[0];
    for i := 1; i < len(arr); i++ {
        if max > arr[i] {
            return false;
        } else {
            max = arr[i];
        }
    }
    return true;
}

func main() {
    file, err := os.Open(os.Args[1])
    if err != nil {
        log.Fatal(err)
    }   
    defer file.Close()
    scanner := bufio.NewScanner(file)

    // For every line of file
    for scanner.Scan() {
        count := 0
        //'scanner.Text()' represents the test case, do something with it
        splitArray := strings.Split(scanner.Text(), "|")
        stringArray := strings.Split(strings.Trim(splitArray[0], " "), " ");
    }   
}