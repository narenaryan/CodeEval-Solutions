
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
    var temp int
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
        mainArray := convertToInts(stringArray);
        iteration, _ := strconv.Atoi(strings.Trim(splitArray[1], " "));
        // Finished processing array

        // Starting the Logic of Sort 
        for !isArraySorted(mainArray){
         // If given iterations are over break out
         if count == iteration {
            break;
         }
        for i := 0; i < len(mainArray) - 1; i++ {
            if mainArray[i] > mainArray[i + 1] {
                temp = mainArray[i];
                mainArray[i] = mainArray[i + 1];
                mainArray[i + 1] = temp;
                count += 1;
                break;
            }
        }
    }
    // Print the left over array
    fmt.Printf("%s\n", strings.Join(convertToStrings(mainArray), " "));
    }   
}