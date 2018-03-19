CLIENT_ID="amzn1.application-oa2-client.d35b33a31a4c4e1aa673cd1c2f76896d"
DEVICE_TYPE_ID="javier_MacBook"
DEVICE_SERIAL_NUMBER="123456"
REDIRECT_URI="https://localhost:3000/authresponse"
RESPONSE_TYPE="code"
SCOPE="alexa:all"
SCOPE_DATA="{\"alexa:all\": {\"productID\": \"$DEVICE_TYPE_ID\", \"productInstanceAttributes\": {\"deviceSerialNumber\": \"${DEVICE_SERIAL_NUMBER}\"}}}"

function urlencode() {
  perl -MURI::Escape -ne 'chomp;print uri_escape($_),"\n"'
}

AUTH_URL="https://www.amazon.com/ap/oa?client_id=${CLIENT_ID}&scope=$(echo $SCOPE | urlencode)&scope_data=$(echo $SCOPE_DATA | urlencode)&response_type=${RESPONSE_TYPE}&redirect_uri=$(echo $REDIRECT_URI | urlencode)"

rm -f -- avsLogin.txt
echo ${AUTH_URL} >> avsLogin.txt