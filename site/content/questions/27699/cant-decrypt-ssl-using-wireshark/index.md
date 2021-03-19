+++
type = "question"
title = "Can&#x27;t decrypt SSL using wireshark"
description = '''Recently I try to decrypt my dropbox connection which is in TLS format. I use the squid as a middle man in Ubuntu13.10, I configure the /etc/squid3.conf as follow, the squid proxy is running at port 3128 and I set the chrome to use the squid proxy running at 127.0.0.1:3128: # Squid normally listens ...'''
date = "2013-12-03T04:44:00Z"
lastmod = "2013-12-03T07:24:00Z"
weight = 27699
keywords = [ "ssl", "ssl-bump", "squid", "wireshark", "dropbox" ]
aliases = [ "/questions/27699" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Can't decrypt SSL using wireshark](/questions/27699/cant-decrypt-ssl-using-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27699-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Recently I try to decrypt my dropbox connection which is in TLS format.</p><p>I use the squid as a middle man in Ubuntu13.10, I configure the /etc/squid3.conf as follow, the squid proxy is running at port 3128 and I set the chrome to use the squid proxy running at 127.0.0.1:3128:</p><pre><code># Squid normally listens to port 3128

always_direct allow all

http_port 3128 ssl-bump cert=/home/lzq-ubuntu/Desktop/cert/sslcerts/127.0.0.1-cert.pem key=/home/lzq-ubuntu/Desktop/cert/sslcerts/private/127.0.0.1-key.pem

#ssl_bump client-first

ssl_bump server-first
</code></pre><p>I generate the key using a .sh file:</p><pre><code>#!/bin/sh

if [ ! -d sslcerts ] ; then
  mkdir sslcerts || die &quot;Couldn&#39;t create sslcerts directory&quot;
fi
if [ ! -d sslcerts/certs ] ; then
  mkdir sslcerts/certs || die &quot;Couldn&#39;t create certs directory&quot;
fi
if [ ! -d sslcerts/private ] ; then
  mkdir sslcerts/private || die &quot;Couldn&#39;t create private directory&quot;
fi
if [ ! -f sslcerts/serial ] ; then
  echo &#39;100001&#39; &gt; sslcerts/serial
fi
touch sslcerts/certindex.txt
if [ ! -f sslcerts/openssl.cnf ] ; then
  cat &lt;&lt;-EOF &gt; sslcerts/openssl.cnf
    #
    # OpenSSL configuration file.
    #

    # Establish working directory.

    dir         = .

    [ ca ]
    default_ca      = CA_default

    [ CA_default ]
    serial          = ./serial
    database        = ./certindex.txt
    new_certs_dir       = ./certs
    certificate     = ./ca_cert.pem
    private_key     = ./private/ca_key.pem
    default_days        = 365
    default_md      = md5
    preserve        = no
    email_in_dn     = no
    nameopt         = default_ca
    certopt         = default_ca
    policy          = policy_anything

    [ policy_match ]
    countryName     = match
    stateOrProvinceName = match
    organizationName    = match
    organizationalUnitName  = match
    commonName      = supplied
    emailAddress        = optional

    [ policy_anything ]
    countryName     = optional
    stateOrProvinceName = optional
    localityName        = optional
    organizationName    = optional
    organizationalUnitName  = optional
    commonName      = supplied
    emailAddress        = optional

    [ req ]
    default_bits        = 1024          # Size of keys
    default_keyfile     = key.pem       # name of generated keys
    default_md      = md5           # message digest algorithm
    string_mask     = nombstr       # permitted characters
    distinguished_name  = req_distinguished_name
    req_extensions      = v3_req

    [ req_distinguished_name ]
    # Variable name             Prompt string
    #-------------------------    ----------------------------------
    0.organizationName  = Organization Name (company)
    organizationalUnitName  = Organizational Unit Name (department, division)
    emailAddress        = Email Address
    emailAddress_max    = 40
    localityName        = Locality Name (city, district)
    stateOrProvinceName = State or Province Name (full name)
    countryName     = Country Name (2 letter code)
    countryName_min     = 2
    countryName_max     = 2
    commonName      = Common Name (hostname, IP, or your name)
    commonName_max      = 64

    # Default values for the above, for consistency and less typing.
    # Variable name         Value
    #------------------------  ------------------------------
    0.organizationName_default  = WebScarab
    localityName_default        = WebScarab
    stateOrProvinceName_default = WebScarab
    countryName_default     = ZA

    [ v3_ca ]
    basicConstraints        = CA:TRUE
    subjectKeyIdentifier        = hash
    authorityKeyIdentifier      = keyid:always,issuer:always

    [ v3_req ]
    basicConstraints        = CA:FALSE
    subjectKeyIdentifier        = hash
    EOF
fi

if [ ! -f sslcerts/private/ca_key.pem -a ! -f sslcerts/ca_cert.p12 ] ; then
  printf &quot;\n\n\n\n\n\n\n&quot; | \
  openssl req -new -x509 -extensions v3_ca -keyout sslcerts/private/ca_key.pem \
    -out sslcerts/ca_cert.pem -days 3650 -config ./sslcerts/openssl.cnf \
    -passin pass:password -passout pass:password
fi

cd sslcerts

# Create the cert for the specified site
if [ ! -f $1-req.pem ] ; then
  printf &quot;\n\n\n\n\n\n$1\n&quot; | \
  openssl req -new -nodes \
    -out $1-req.pem -keyout ./private/$1-key.pem \
    -days 3650 -config ./openssl.cnf
fi

if [ ! -f $1-cert.pem ] ; then
  printf &quot;y\ny\n&quot; | \
  openssl ca -out $1-cert.pem -days 3650 \
    -key password -config ./openssl.cnf -infiles $1-req.pem
fi

if [ ! -f ../$1.p12 ] ; then
  openssl pkcs12 -export -in $1-cert.pem -inkey ./private/$1-key.pem \
    -certfile ca_cert.pem -out ../$1.p12 -password pass:password
fi</code></pre><p>I use the command: <strong>sh cert.sh 127.0.0.1</strong> to generate the key.</p><p>But after loading the key in wireshark, I can not decrypt the flow, I got this log file:</p><pre><code>ssl_association_remove removing TCP 3128 - http handle 0x7f6238467400
Private key imported: KeyID 22:0e:f2:57:3b:ef:cc:1a:ca:35:ea:c3:4b:62:49:60:...
ssl_init IPv4 addr &#39;127.0.0.1&#39; (127.0.0.1) port &#39;3128&#39; filename &#39;/home/lzq-ubuntu/Desktop/cert/sslcerts/private/127.0.0.1-key.pem&#39; password(only for p12 file) &#39;&#39;
ssl_init private key file /home/lzq-ubuntu/Desktop/cert/sslcerts/private/127.0.0.1-key.pem successfully loaded.
association_add TCP port 3128 protocol http handle 0x7f6238467400

dissect_ssl enter frame #6 (first time)
ssl_session_init: initializing ptr 0x7f621ff49038 size 680
  conversation = 0x7f621ff48980, ssl_session = 0x7f621ff49038
  record: offset = 0, reported_length_remaining = 211

dissect_ssl enter frame #8 (first time)
  conversation = 0x7f621ff48980, ssl_session = 0x7f621ff49038
  record: offset = 0, reported_length_remaining = 39

dissect_ssl enter frame #12 (first time)
  conversation = 0x7f621ff48980, ssl_session = 0x7f621ff49038
  record: offset = 0, reported_length_remaining = 246
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 241, ssl state 0x00
association_find: TCP port 53519 found (nil)
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 237 bytes, remaining 246 
packet_from_server: is from server - FALSE
ssl_find_private_key server 127.0.0.1:3128
dissect_ssl3_hnd_hello_common found CLIENT RANDOM -&gt; state 0x01

dissect_ssl enter frame #6 (already visited)
  conversation = 0x7f621ff48980, ssl_session = (nil)
  record: offset = 0, reported_length_remaining = 211

dissect_ssl enter frame #8 (already visited)
  conversation = 0x7f621ff48980, ssl_session = (nil)
  record: offset = 0, reported_length_remaining = 39

dissect_ssl enter frame #12 (already visited)
  conversation = 0x7f621ff48980, ssl_session = (nil)
  record: offset = 0, reported_length_remaining = 246
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 237 bytes, remaining 246 

dissect_ssl enter frame #19 (first time)
ssl_session_init: initializing ptr 0x7f621ff4a568 size 680
  conversation = 0x7f621ff49eb0, ssl_session = 0x7f621ff4a568
  record: offset = 0, reported_length_remaining = 89

dissect_ssl enter frame #21 (first time)
  conversation = 0x7f621ff49eb0, ssl_session = 0x7f621ff4a568
  record: offset = 0, reported_length_remaining = 39

dissect_ssl enter frame #25 (first time)
  conversation = 0x7f621ff49eb0, ssl_session = 0x7f621ff4a568
  record: offset = 0, reported_length_remaining = 74
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 69, ssl state 0x00
association_find: TCP port 53521 found (nil)
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 65 bytes, remaining 74 
packet_from_server: is from server - FALSE
ssl_find_private_key server 127.0.0.1:3128
dissect_ssl3_hnd_hello_common found CLIENT RANDOM -&gt; state 0x01

dissect_ssl enter frame #19 (already visited)
  conversation = 0x7f621ff49eb0, ssl_session = (nil)
  record: offset = 0, reported_length_remaining = 89

dissect_ssl enter frame #21 (already visited)
  conversation = 0x7f621ff49eb0, ssl_session = (nil)
  record: offset = 0, reported_length_remaining = 39

dissect_ssl enter frame #25 (already visited)
  conversation = 0x7f621ff49eb0, ssl_session = (nil)
  record: offset = 0, reported_length_remaining = 74
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 65 bytes, remaining 74 

dissect_ssl enter frame #30 (first time)
  conversation = 0x7f621ff48980, ssl_session = 0x7f621ff49038
  record: offset = 0, reported_length_remaining = 1163
dissect_ssl3_record found version 0x0303(TLS 1.2) -&gt; state 0x11
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 53, ssl state 0x11
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 49 bytes, remaining 58 
dissect_ssl3_hnd_hello_common found SERVER RANDOM -&gt; state 0x13
dissect_ssl3_hnd_srv_hello can&#39;t find cipher suite 0x9C
  record: offset = 58, reported_length_remaining = 1105
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 1091, ssl state 0x13
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 11 offset 63 length 1087 bytes, remaining 1154 
  record: offset = 1154, reported_length_remaining = 9
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 4, ssl state 0x13
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 14 offset 1159 length 0 bytes, remaining 1163 

dissect_ssl enter frame #32 (first time)
  conversation = 0x7f621ff48980, ssl_session = 0x7f621ff49038
  record: offset = 0, reported_length_remaining = 190
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 134, ssl state 0x13
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 16 offset 5 length 130 bytes, remaining 139 
ssl_decrypt_pre_master_secret key exchange 0 different from KEX_RSA (16)
dissect_ssl3_handshake can&#39;t decrypt pre master secret
  record: offset = 139, reported_length_remaining = 51
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
packet_from_server: is from server - FALSE
ssl_change_cipher CLIENT
  record: offset = 145, reported_length_remaining = 45
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 40, ssl state 0x13
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 0 offset 150 length 0 bytes, remaining 190 
dissect_ssl3_handshake iteration 0 type 0 offset 154 length 0 bytes, remaining 190 
dissect_ssl3_handshake iteration 0 type 148 offset 158 length 9736230 bytes, remaining 190 

dissect_ssl enter frame #34 (first time)
  conversation = 0x7f621ff48980, ssl_session = 0x7f621ff49038
  record: offset = 0, reported_length_remaining = 242
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 186, ssl state 0x13
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 4 offset 5 length 182 bytes, remaining 191 
  record: offset = 191, reported_length_remaining = 51
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
packet_from_server: is from server - TRUE
ssl_change_cipher SERVER
  record: offset = 197, reported_length_remaining = 45
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 40, ssl state 0x13
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 214 offset 202 length 6700648 bytes, remaining 242 

dissect_ssl enter frame #35 (first time)
  conversation = 0x7f621ff48980, ssl_session = 0x7f621ff49038
  record: offset = 0, reported_length_remaining = 1147
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 1142, ssl state 0x13
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 53519 found (nil)
association_find: TCP port 3128 found 0x7f62392b2a30

dissect_ssl enter frame #30 (already visited)
  conversation = 0x7f621ff48980, ssl_session = (nil)
  record: offset = 0, reported_length_remaining = 1163
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 49 bytes, remaining 58 
  record: offset = 58, reported_length_remaining = 1105
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 11 offset 63 length 1087 bytes, remaining 1154 
  record: offset = 1154, reported_length_remaining = 9
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 14 offset 1159 length 0 bytes, remaining 1163 

dissect_ssl enter frame #32 (already visited)
  conversation = 0x7f621ff48980, ssl_session = (nil)
  record: offset = 0, reported_length_remaining = 190
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 16 offset 5 length 130 bytes, remaining 139 
  record: offset = 139, reported_length_remaining = 51
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
  record: offset = 145, reported_length_remaining = 45
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 0 offset 150 length 0 bytes, remaining 190 
dissect_ssl3_handshake iteration 0 type 0 offset 154 length 0 bytes, remaining 190 
dissect_ssl3_handshake iteration 0 type 148 offset 158 length 9736230 bytes, remaining 190 

dissect_ssl enter frame #34 (already visited)
  conversation = 0x7f621ff48980, ssl_session = (nil)
  record: offset = 0, reported_length_remaining = 242
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 4 offset 5 length 182 bytes, remaining 191 
  record: offset = 191, reported_length_remaining = 51
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
  record: offset = 197, reported_length_remaining = 45
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 214 offset 202 length 6700648 bytes, remaining 242 

dissect_ssl enter frame #35 (already visited)
  conversation = 0x7f621ff48980, ssl_session = (nil)
  record: offset = 0, reported_length_remaining = 1147
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 53519 found (nil)
association_find: TCP port 3128 found 0x7f62392b2a30

dissect_ssl enter frame #39 (first time)
  conversation = 0x7f621ff49eb0, ssl_session = 0x7f621ff4a568
  record: offset = 0, reported_length_remaining = 1163
dissect_ssl3_record found version 0x0301(TLS 1.0) -&gt; state 0x11
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 53, ssl state 0x11
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 49 bytes, remaining 58 
dissect_ssl3_hnd_hello_common found SERVER RANDOM -&gt; state 0x13
ssl_restore_session can&#39;t find stored session
dissect_ssl3_hnd_srv_hello found CIPHER 0x0035 -&gt; state 0x17
dissect_ssl3_hnd_srv_hello trying to generate keys
ssl_generate_keyring_material not enough data to generate key (0x17 required 0x37 or 0x57)
dissect_ssl3_hnd_srv_hello can&#39;t generate keyring material
  record: offset = 58, reported_length_remaining = 1105
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 1091, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 11 offset 63 length 1087 bytes, remaining 1154 
  record: offset = 1154, reported_length_remaining = 9
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 4, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 14 offset 1159 length 0 bytes, remaining 1163 

dissect_ssl enter frame #41 (first time)
  conversation = 0x7f621ff49eb0, ssl_session = 0x7f621ff4a568
  record: offset = 0, reported_length_remaining = 7
dissect_ssl3_record: content_type 21 Alert
decrypt_ssl3_record: app_data len 2, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available

dissect_ssl enter frame #45 (first time)
  conversation = 0x7f621ff48980, ssl_session = 0x7f621ff49038
  record: offset = 0, reported_length_remaining = 564
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 559, ssl state 0x13
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 3128 found 0x7f62392b2a30

dissect_ssl enter frame #46 (first time)
  conversation = 0x7f621ff48980, ssl_session = 0x7f621ff49038
  record: offset = 0, reported_length_remaining = 176
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 171, ssl state 0x13
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 3128 found 0x7f62392b2a30

dissect_ssl enter frame #39 (already visited)
  conversation = 0x7f621ff49eb0, ssl_session = (nil)
  record: offset = 0, reported_length_remaining = 1163
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 49 bytes, remaining 58 
  record: offset = 58, reported_length_remaining = 1105
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 11 offset 63 length 1087 bytes, remaining 1154 
  record: offset = 1154, reported_length_remaining = 9
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 14 offset 1159 length 0 bytes, remaining 1163 

dissect_ssl enter frame #41 (already visited)
  conversation = 0x7f621ff49eb0, ssl_session = (nil)
  record: offset = 0, reported_length_remaining = 7
dissect_ssl3_record: content_type 21 Alert

dissect_ssl enter frame #45 (already visited)
  conversation = 0x7f621ff48980, ssl_session = (nil)
  record: offset = 0, reported_length_remaining = 564
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 3128 found 0x7f62392b2a30

dissect_ssl enter frame #46 (already visited)
  conversation = 0x7f621ff48980, ssl_session = (nil)
  record: offset = 0, reported_length_remaining = 176
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 3128 found 0x7f62392b2a30</code></pre><p>It seems that the key is loaded successfully, but the app data in each packet are still encryped.</p><p>Help!!!!</p></div><div id="question-tags" class="tags-container tags">ssl ssl-bump squid wireshark dropbox</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Dec '13, 04:44</strong></p><img src="https://secure.gravatar.com/avatar/44959625f5849a8c85cdf05ca9802478?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lzq8272587&#39;s gravatar image" /><p>lzq8272587<br />
<span class="score" title="26 reputation points">26</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lzq8272587 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 03 Dec '13, 07:13</p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-27699" class="comments-container"></div><div id="comment-tools-27699" class="comment-tools"></div><div class="clear"></div><div id="comment-27699-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="27714"></span>

<div id="answer-container-27714" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27714-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>dissect_ssl3_hnd_srv_hello <strong>can't find cipher suite 0x9C</strong></p></blockquote><p>Looks like your Wireshark version (which one is it) does not support cipher 0x9C (TLS_RSA_WITH_AES_128_GCM_SHA256). You could try to force either your browser or squid to another cipher and then check again.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Dec '13, 07:24</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-27714" class="comments-container"><span id="27757"></span><div id="comment-27757" class="comment"><div id="post-27757-score" class="comment-score"></div><div class="comment-text"><p>Thank you very much!!</p><p>My wireshark version is 1.8.3 and after I change my cipher suit in squid.conf I can decrypt the SSL data.</p><p>Thank you very much!!!</p><p>BTW, sometimes I can not visit some website through HTTPS because I used the self-generated certificate and key, and the browser say that:</p><p>"Invalid Server Certificate"</p><p>So is there any idea how can I generate the certificate and key authorized by Dropbox?</p><p>Thanks very much for your help again!!!</p></div><div id="comment-27757-info" class="comment-info"><span class="comment-age">(04 Dec '13, 03:57)</span> lzq8272587</div></div><span id="27759"></span><div id="comment-27759" class="comment"><div id="post-27759-score" class="comment-score"></div><div class="comment-text"><blockquote><p>after I change my cipher suit in squid.conf I can decrypt the SSL data.</p></blockquote><p>good. I believe the latest development build of Wireshark (1.11.x) does support (0x9c - I think I have seen that somewhere). Maybe you want to try it later as well.</p><blockquote><p>So is there any idea how can I generate the certificate and key <strong>authorized by Dropbox</strong>?</p></blockquote><p>"authorized by Dropbox"? There is no way to do <strong>that</strong>, unless you are the owner of Dropbox or a <strong>very, very</strong> skilled hacker ;-)</p><p>I believe this could be a problem with the Squid configuration. I've never used squid for SSL interception, so I don't know what to look for. Maybe it's better to ask that specific question in a Squid forum !?!</p><p>Hint: If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions. For extra points you can up vote the answer (thumb up).</p></div><div id="comment-27759-info" class="comment-info"><span class="comment-age">(04 Dec '13, 04:50)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-27714" class="comment-tools"></div><div class="clear"></div><div id="comment-27714-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

