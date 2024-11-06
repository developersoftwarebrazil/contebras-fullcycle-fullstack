package rabbitmql

import (
	"fmt"

	"github.com/streadway/amqp"
)

type RabbitClient struct {
	conn    *amqp.Connection
	channel *amqp.Channel
	url     string
}

func newConnection(url string) (*amqp.Connection, *amqp.Channel, error) {
	conn, err := amqp.Dial(url)
	if err != nil {
		return nil, nil, fmt.Errorf("failed to connect to RabbitMQ: %v", err)
	}
	channel, err := conn.Channel()
	if err != nil {
		return nil, nil, fmt.Errorf("failed to open a channel: %v", err)
	}

	return conn, channel, err

}

func NewRabbitClient(connetionURL string) (*RabbitClient, error) {
	conn, channel, err := newConnection(connetionURL)
	if err != nil {
		return nil, err
	}

	return &RabbitClient{
		conn:    conn,
		channel: channel,
		url:     connetionURL,
	}, nil
}

func (client *RabbitClient) ConsumeMessages(exchange, routingKey, queueName string) (<-chan amqp.Delivery, error) {
	err := client.channel.ExchangeDeclare(exchange, "direct", true, true, false, false, nil)

	if err != nil {
		return nil, fmt.Errorf("failed to declare exchange: %v", err)
	}

	queue, err := client.channel.QueueDeclare(queueName, true, true, false, false, nil)
	if err != nil {
		return nil, fmt.Errorf("failed to declare queue: %v", err)
	}

	err = client.channel.QueueBind(queue.Name, routingKey, exchange, false, nil)

	if err != nil {
		return nil, fmt.Errorf("failed to bind queue: %v", err)
	}

	msgs, err := client.channel.Consume(queueName, "goapp", false, false, false, false, nil)
	if err != nil {
		return nil, fmt.Errorf("failed to consume messages from queue: %v", err)
	}
	return msgs, nil
}

// Close terminates the RabbitMQ connection and channel
func (client *RabbitClient) Close() error {
	err := client.channel.Close()
	if err != nil {
		return fmt.Errorf("failed to close channel: %v", err)
	}
	err = client.conn.Close()
	if err != nil {
		return fmt.Errorf("failed to close connection: %v", err)
	}
	return nil
}
