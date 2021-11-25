import apache_beam as beam

with beam.Pipeline() as pipeline:
    result = (
        pipeline
        | beam.Create([1, 2, 3, 4])
        | beam.Map(lambda x: x * 2)
        | beam.CombineGlobally(sum)
        | beam.Map(print)
    )