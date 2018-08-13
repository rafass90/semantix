import org.apache.spark.{SparkConf, SparkContext}

object GenerateSparkContext {

  def getInstance(): SparkContext = {
    val appName: String = "Main"
    val conf = new SparkConf().setAppName("Main").setMaster("local[2]").set("spark.executor.memory", "2g")
    new SparkContext(conf)
  }
}
