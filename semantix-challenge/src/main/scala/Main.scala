object Main {

  def main(args: Array[String]): Unit = {
    val sc = GenerateSparkContext.getInstance()
    val textFile = sc.textFile("semantix.txt")
    val counts = textFile.flatMap(line => line.split(" "))
      .map(word => (word , 1))
      .reduceByKey(_ + _)
    counts.saveAsTextFile( "semantix" )
  }
}