import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Aura',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.blueGrey),
        useMaterial3: true,
      ),
      home: const LoginScreen(),
    );
  }
}

// Login Screen UI
class LoginScreen extends StatefulWidget {
  const LoginScreen({super.key});

  @override
  State<LoginScreen> createState() => _LoginScreenState();
}

class _LoginScreenState extends State<LoginScreen> {
  final TextEditingController _usernameController = TextEditingController(text: 'testuser');
  final TextEditingController _passwordController = TextEditingController(text: 'bankofanthos');
  bool _isLoading = false;

  Future<void> _login() async {
    setState(() {
      _isLoading = true;
    });

    print('--- Attempting Login ---');
    print('Username: ${_usernameController.text}');

    final client = http.Client();
    try {
      final loginUrl = Uri.parse('http://34.41.186.197/login');
      print('Login URL: $loginUrl');

      final request = http.Request('POST', loginUrl)
        ..bodyFields = {
          'username': _usernameController.text,
          'password': _passwordController.text,
        }
        ..followRedirects = false; // Do not follow redirects

      final streamedResponse = await client.send(request);

      print('Login Response Status Code: ${streamedResponse.statusCode}');
      print('Login Response Headers: ${streamedResponse.headers}');

      if (streamedResponse.statusCode == 302) {
        final cookies = streamedResponse.headers['set-cookie'];
        if (cookies != null) {
          final tokenCookie = cookies.split(';').firstWhere(
                (c) => c.trim().startsWith('token='),
            orElse: () => '',
          );

          if (tokenCookie.isNotEmpty) {
            final token = tokenCookie.split('=')[1];
            print('Successfully extracted token: $token');

            if (mounted) {
              Navigator.pushReplacement(
                context,
                MaterialPageRoute(
                  builder: (context) => ChatScreen(token: token, userId: _usernameController.text),
                ),
              );
            }
            return; // Exit after successful navigation
          }
        }
      }
      final response = await http.Response.fromStream(streamedResponse);
      throw Exception('Login failed. Status: ${response.statusCode}, Body: ${response.body}');

    } catch (e) {
      print('Login Error: ${e.toString()}');
      if (mounted) {
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(content: Text('Login failed: ${e.toString()}')),
        );
      }
    } finally {
      client.close();
      if (mounted) {
        setState(() {
          _isLoading = false;
        });
      }
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Aura Financial'),
      ),
      body: Center(
        child: Padding(
          padding: const EdgeInsets.all(24.0),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: <Widget>[
              TextField(
                controller: _usernameController,
                decoration: const InputDecoration(labelText: 'Username'),
              ),
              const SizedBox(height: 16),
              TextField(
                controller: _passwordController,
                obscureText: true,
                decoration: const InputDecoration(labelText: 'Password'),
              ),
              const SizedBox(height: 24),
              _isLoading
                  ? const CircularProgressIndicator()
                  : ElevatedButton(
                      onPressed: _login,
                      child: const Text('Login'),
                    ),
            ],
          ),
        ),
      ),
    );
  }
}


// Chat Screen UI
class ChatScreen extends StatefulWidget {
  final String token;
  final String userId;
  const ChatScreen({super.key, required this.token, required this.userId});

  @override
  State<ChatScreen> createState() => _ChatScreenState();
}

class _ChatScreenState extends State<ChatScreen> {
  final TextEditingController _messageController = TextEditingController();
  final List<Map<String, String>> _messages = [];
  bool _isLoading = false;
  String? _sessionId;

  Future<void> _sendMessage() async {
    final message = _messageController.text;
    if (message.isEmpty) {
      return;
    }

    print('Start of _sendMessage, current _sessionId: $_sessionId');

    final userMessage = {'sender': 'user', 'text': message};

    setState(() {
      _messages.add(userMessage);
      _isLoading = true;
    });
    _messageController.clear();

    final agentUrl = Uri.parse('http://34.135.12.119/chat');
    
    final requestBody = json.encode({
      'message': '$message token:${widget.token} accountID:1011226111',
      'user_id': widget.userId,
      'session_id': _sessionId,
    });

    print('--- Sending message to agent ---');
    print('Agent URL: $agentUrl');
    print('Request Body: $requestBody');
    
    try {
      final response = await http.post(
        agentUrl,
        headers: {'Content-Type': 'application/json'},
        body: requestBody,
      );

      print('Agent Response Status Code: ${response.statusCode}');
      print('Agent Response Body: ${response.body}');

      if (response.statusCode == 200) {
        final responseBody = json.decode(response.body);
        final agentResponse = responseBody['response'];
        
        print('Received session_id from backend: ${responseBody['session_id']}');
        // Save the session ID for subsequent requests
        _sessionId = responseBody['session_id']; 
        print('Updated _sessionId to: $_sessionId');

        setState(() {
          _messages.add({'sender': 'agent', 'text': agentResponse});
        });
      } else {
        setState(() {
          _messages.add({'sender': 'agent', 'text': 'Error: ${response.body}'});
        });
      }

    } catch (e) {
      print('Agent Request Error: ${e.toString()}');
      setState(() {
        _messages.add({'sender': 'agent', 'text': 'Error: Could not connect to the agent.'});
      });
    } finally {
      setState(() {
        _isLoading = false;
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    final sampleQuestions = [
      'What\'s my account balance?',
      'Where did my money go last month?',
      'What was my biggest expense recently?',
      'Give me a tip for saving money',
    ];

    return Scaffold(
      appBar: AppBar(
        title: const Text('Chat with Aura'),
      ),
      body: Column(
        children: [
          Expanded(
            child: ListView.builder(
              padding: const EdgeInsets.all(16.0),
              itemCount: _messages.length,
              itemBuilder: (context, index) {
                final message = _messages[index];
                final isUser = message['sender'] == 'user';
                return Align(
                  alignment: isUser ? Alignment.centerRight : Alignment.centerLeft,
                  child: Container(
                    margin: const EdgeInsets.symmetric(vertical: 4.0),
                    padding: const EdgeInsets.all(12.0),
                    decoration: BoxDecoration(
                      color: isUser ? Colors.blueGrey[100] : Colors.grey[200],
                      borderRadius: BorderRadius.circular(16.0),
                    ),
                    child: Text(message['text']!),
                  ),
                );
              },
            ),
          ),
          if (_isLoading)
            const Padding(
              padding: EdgeInsets.all(8.0),
              child: CircularProgressIndicator(),
            ),
          Padding(
            padding: const EdgeInsets.symmetric(horizontal: 8.0),
            child: Wrap(
              spacing: 8.0,
              runSpacing: 4.0,
              children: sampleQuestions.map((question) {
                return ActionChip(
                  label: Text(question),
                  onPressed: () {
                    _messageController.text = question;
                    _sendMessage();
                  },
                );
              }).toList(),
            ),
          ),
          Padding(
            padding: const EdgeInsets.all(8.0),
            child: Row(
              children: [
                Expanded(
                  child: TextField(
                    controller: _messageController,
                    decoration: const InputDecoration(
                      hintText: 'Ask Aura a question...',
                      border: OutlineInputBorder(),
                    ),
                    onSubmitted: (_) => _sendMessage(),
                  ),
                ),
                IconButton(
                  icon: const Icon(Icons.send),
                  onPressed: _sendMessage,
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}