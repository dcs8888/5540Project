from pyspark import SparkContext
import argparse

def args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', type=str, help='Input File', required=True)
    parser.add_argument('-o', '--output', type=str, help='Output File', required=True)

    args_list = parser.parse_args()
    input = args_list.input
    output = args_list.output
    
    return input, output

def main():
    input, output = args()
    
    log_file = input
    spark_content = SparkContext("local", "Word Count")
    data = spark_content.textFile(log_file)
    
    word_count = data.flatMap(lambda x: x.split('\n')).map(lambda x:(x,1)).reduceByKey(lambda x,y:x+y).map(lambda x:(x[1],x[0])).sortByKey(False)
    word_count.saveAsTextFile(output)

if __name__ == '__main__':
    main()
