defmodule ChatWeb.RoomChannel do
  use ChatWeb, :channel

  def join("room:lobby", payload, socket) do
    if authorized?(payload) do
      send(self(), :after_join)
      {:ok, socket}
    else
      {:error, %{reason: "unauthorized"}}
    end
  end

  # Channels can be used in a request/response fashion
  # by sending replies to requests from the client
  def handle_in("ping", payload, socket) do
    {:reply, {:ok, payload}, socket}
  end

  # It is also common to receive messages from the client and
  # broadcast to everyone in the current topic (room:lobby).
  def handle_in("shout", payload, socket) do
    Chat.Message.changeset(%Chat.Message{}, payload) |> Chat.Repo.insert
    
    # Get message from sender
    message = payload["message"]

    # Build request to send message to Chatbot AI
    body = "{\"key\":\"#{message}\"}"
    header = [{"Content-Type", "application/json"}]

    HTTPoison.start   
    response = HTTPoison.post!("http://localhost:5002/chatbot", body, header).body
    robotResponse = Poison.decode!(~s(#{response}));

    # Broadcast original message
    broadcast socket, "shout", payload

    # Broadcast chatbot response message
    Chat.Message.changeset(%Chat.Message{}, robotResponse) |> Chat.Repo.insert
    broadcast socket, "shout", robotResponse
    

    {:noreply, socket}
  end

  def handle_info(:after_join, socket) do
    Chat.Message.get_messages()
    |> Enum.each(fn msg -> push(socket, "shout", %{
        name: msg.name,
        message: msg.message,
      }) end)
    {:noreply, socket} # :noreply
  end

  # Add authorization logic here as required.
  defp authorized?(_payload) do
    true
  end
end
