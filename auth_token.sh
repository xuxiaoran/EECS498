CLIENT_ID="amzn1.application-oa2-client.d35b33a31a4c4e1aa673cd1c2f76896d"
CLIENT_SECRET="0d02bdb60adfe623c2a9d3b09e464672f74b70900e6ed0b9d3c928120fa0673d"
CODE=$(<code.txt)
GRANT_TYPE="authorization_code"
REDIRECT_URI="https://localhost:3000/authresponse"


response=$(curl -X POST --data "grant_type=${GRANT_TYPE}&code=${CODE}&client_id=${CLIENT_ID}&client_secret=${CLIENT_SECRET}&redirect_uri=${REDIRECT_URI}" https://api.amazon.com/auth/o2/token)

rm -f -- avsLogin.json
echo ${response} >> avsLogin.json

rm -f -- token.txt
echo $(jq .access_token avsLogin.json) >> token.txt

rm -f -- refresh_token.txt
echo $(jq .refresh_token avsLogin.json) >> refresh_token.txt