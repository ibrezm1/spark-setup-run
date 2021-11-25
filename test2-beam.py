import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

options = PipelineOptions([
    "--runner=PortableRunner",
    "--job_endpoint=localhost:8099",
    "--environment_type=LOOPBACK"
])
with beam.Pipeline(options) as pipeline:
    result = (
        pipeline
        | beam.Create([1, 2, 3, 4])
        | beam.Map(lambda x: x * 2)
        | beam.CombineGlobally(sum)
        | beam.Map(print)
    )