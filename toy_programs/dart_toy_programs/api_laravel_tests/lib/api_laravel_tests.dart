import 'package:http/http.dart' as http;

void main() async{
    final headersList = {
        'Accept': '*/*',
        'User-Agent': 'Thunder Client (https://www.thunderclient.com)' 
    };
    final url = Uri.parse('http://localhost:8000/send_name/Salomon');

    final req = http.Request('GET', url);
    req.headers.addAll(headersList);

    final res = await req.send();
    final resBody = await res.stream.bytesToString();

    if (res.statusCode >= 200 && res.statusCode < 300) {
      print(resBody);
    }
    else {
      print(res.reasonPhrase);
    }
}