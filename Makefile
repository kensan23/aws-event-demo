build:
	@sam build
deploy:
	@sam deploy
produce:
	@python src/Producer/producer.py
local-sns:
	@sam local invoke --event events/snsevent.json event-demo-sqs-function
local-kinesis:
	@sam local invoke --event events/kinesisevent.json pevent-demo-stream-function
local-eventbridge:
	@sam local invoke --event events/ebevent.json event-demo-eventbridge-function