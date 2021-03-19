+++
type = "question"
title = "Server Certificate packet format"
description = '''I can&#x27;t find a writeup on the format of the Server Certificate - i.e. what all the bytes are and the different variations. I have a couple of TLS/SSL books and papers, but they don&#x27;t have anything on the actual format of the packet. Can someone point me in that direction? I&#x27;m trying to figure out wh...'''
date = "2017-07-05T08:34:00Z"
lastmod = "2017-07-05T09:21:00Z"
weight = 62528
keywords = [ "ssl", "certificate" ]
aliases = [ "/questions/62528" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Server Certificate packet format](/questions/62528/server-certificate-packet-format)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62528-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I can't find a writeup on the format of the Server Certificate - i.e. what all the bytes are and the different variations. I have a couple of TLS/SSL books and papers, but they don't have anything on the actual format of the packet. Can someone point me in that direction? I'm trying to figure out where the public key is embedded and what all the other bytes mean.</p><p>Thanks.</p><p>Sutton</p></div><div id="question-tags" class="tags-container tags">ssl certificate</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Jul '17, 08:34</strong></p><img src="https://secure.gravatar.com/avatar/9f303f38b9221d23f72e6d2e5a651184?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dodge55&#39;s gravatar image" /><p>dodge55<br />
<span class="score" title="21 reputation points">21</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dodge55 has no accepted answers">0%</span></p></div></div><div id="comments-container-62528" class="comments-container"></div><div id="comment-tools-62528" class="comment-tools"></div><div class="clear"></div><div id="comment-62528-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="62534"></span>

<div id="answer-container-62534" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62534-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The Certificate message is defined in <a href="https://tools.ietf.org/html/rfc5246#section-7.4.2">RFC 5246, Section. 7.4.2</a>:</p><pre><code>  opaque ASN.1Cert&lt;1..2^24-1&gt;;
  struct {
      ASN.1Cert certificate_list&lt;0..2^24-1&gt;;
  } Certificate;</code></pre><p>In TLS, this notation for <code>certificate_list</code> means that there is a vector with a length prefix (three bytes since the maximum value is 2<sup>24</sup>-1) followed by zero or more <code>ASN.1Cert</code> types. These are also vectors with a three byte length prefix followed by an ASN.1-encoded X.509 certificate.</p><p>In Wireshark, you can select the Certificate field, expand it subfields and study the bytes view at the bottom of the screen. See for example this screenshot where the Certificate is selected with a sample file (linked at the bottom of this post):</p><p><a href="https://osqa-ask.wireshark.org/upfiles/screenshot_gDuZdcT.png"><img src="https://osqa-ask.wireshark.org/upfiles/screenshot_gDuZdcT.png" alt="Screenshot of Wireshark with Certificate message selected" /></a></p><p>Alternatively, you can export the selected ASN.1 bytes for inspection with alternative tools. Right-click on the selected Certificate field and use the <em>Export Packet Bytes</em> (Ctrl-H) option. Save the file as <code>file.der</code> (for example). Then you can study its contents using the <code>openssl</code> tool:</p><pre><code>$ openssl x509 -inform DER -in cert.der -noout -text
Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number:
            f5:11:56:e9:b6:1e:35:c9
    Signature Algorithm: sha256WithRSAEncryption
        Issuer: CN = localhost
        Validity
            Not Before: Feb  7 11:30:11 2015 GMT
            Not After : Mar  9 11:30:11 2015 GMT
        Subject: CN = localhost
        Subject Public Key Info:
            Public Key Algorithm: rsaEncryption
                Public-Key: (1024 bit)
                Modulus:
                    00:9b:a9:75:12:18:1c:46:06:dc:8d:11:b8:f7:f4:
                    ...
                    d2:56:fe:22:59:c8:51:68:a1
                Exponent: 65537 (0x10001)
        ...</code></pre><p>An alternative tool that displays the mechanical interpretation, completely with offsets, lengths and the contents:</p><pre><code>$ openssl asn1parse -in cert.der -inform DER -i -dump
    0:d=0  hl=4 l= 502 cons: SEQUENCE          
    4:d=1  hl=4 l= 351 cons:  SEQUENCE          
    8:d=2  hl=2 l=   3 cons:   cont [ 0 ]        
   10:d=3  hl=2 l=   1 prim:    INTEGER           :02
   13:d=2  hl=2 l=   9 prim:   INTEGER           :F51156E9B61E35C9
   24:d=2  hl=2 l=  13 cons:   SEQUENCE          
   26:d=3  hl=2 l=   9 prim:    OBJECT            :sha256WithRSAEncryption
   37:d=3  hl=2 l=   0 prim:    NULL              
   ...
  115:d=2  hl=3 l= 159 cons:   SEQUENCE          
  118:d=3  hl=2 l=  13 cons:    SEQUENCE          
  120:d=4  hl=2 l=   9 prim:     OBJECT            :rsaEncryption
  131:d=4  hl=2 l=   0 prim:     NULL              
  133:d=3  hl=3 l= 141 prim:    BIT STRING        
      0000 - 00 30 81 89 02 81 81 00-9b a9 75 12 18 1c 46 06   .0........u...F.
      0010 - dc 8d 11 b8 f7 f4 21 99-0b 1b 96 6b 42 f1 4b 48   ......!....kB.KH
      ...
      0080 - 56 fe 22 59 c8 51 68 a1-02 03 01 00 01            V.&quot;Y.Qh......
    ...</code></pre><p>Documentation for these two tools can be found here:</p><ul><li><a href="https://www.openssl.org/docs/manmaster/man1/x509.html">x509(1)</a></li><li><a href="https://www.openssl.org/docs/manmaster/man1/asn1parse.html">asn1parse(1)</a></li></ul><p>The capture I used above is taken from the <a href="https://wiki.wireshark.org/SampleCaptures#SSL_with_decryption_keys">SampleCaptures wiki</a>, http2-16-ssl.pcapng.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Jul '17, 09:21</strong></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p>Lekensteyn<br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lekensteyn has 32 accepted answers">30%</span></p></img></div></div><div id="comments-container-62534" class="comments-container"><span id="62543"></span><div id="comment-62543" class="comment"><div id="post-62543-score" class="comment-score"></div><div class="comment-text"><p>Many thanks for that. In looking at the RFC and my Wireshark output, there are several byte sequences in the Certificate that are not referenced in either the RFC or the Wireshark output. For example, between the version and the serial number, there are 2 undocumented bytes. And, the first 12 bytes of the certificate before the version number don't seem to be documented. At least WS skips over those. Any idea what those are?</p><p>Sutton</p></div><div id="comment-62543-info" class="comment-info"><span class="comment-age">(05 Jul '17, 11:45)</span> dodge55</div></div><span id="62544"></span><div id="comment-62544" class="comment"><div id="post-62544-score" class="comment-score"></div><div class="comment-text"><p>ASN.1 BER (Basic Encoding Rules) use TLV (type-length-value) encoding of fields, so in particular the two bytes you mention, "between" the version and the serial number, say the following:</p><p><code>02</code> - integer</p><p><code>09</code> - consisting of 9 octets</p><p>The information that the meaning of this 9-byte integer is a serial number is implicit, as the serial number is the second item of the certificate as defined in X.509:</p><pre><code>Certificate ::= SIGNED SEQUENCE{
    version [0]Version DEFAULT 1988,
    serialNumber SerialNumber,
    signature Algorithmidentifier
    issuer Name
    validity Validity,
    subject Name,
    subjectPublicKeyInfo SubjectPublicKeyInfo}

Version ::= INTEGER { 1988(0)}
SerialNumber ::= INTEGER
Validity ::=
SEQUENCE{
notBefore UTCTime,
notAfter UTCTime}

...</code></pre><p>Both the sender and the recipient know what to expect at what place as they both "know" the ASN.1 description.</p><p>Similarly, the <code>02:01</code> "before" the version say that the version is a single-octet integer, and the <code>30:82:01:5f:a0:03</code> together say that what follows is a structure called <code>signedCertificate</code>.</p><p>Most Wireshark dissectors prefer readability to detailed explanation of the structure, so this information is not added to the dissection tree.</p></div><div id="comment-62544-info" class="comment-info"><span class="comment-age">(05 Jul '17, 12:06)</span> sindy</div></div><span id="62545"></span><div id="comment-62545" class="comment"><div id="post-62545-score" class="comment-score"></div><div class="comment-text"><p>Thanks. In many of the other packet descriptions (RFC and books), TLV bytes are explicitly mentioned. So, I thought it may be that, but I wasn't totally sure. Being somewhat new to SSL, I like to be sure. Thanks for responding.</p></div><div id="comment-62545-info" class="comment-info"><span class="comment-age">(05 Jul '17, 12:58)</span> dodge55</div></div><span id="62546"></span><div id="comment-62546" class="comment"><div id="post-62546-score" class="comment-score"></div><div class="comment-text"><p>Actually, ASN.1 BER are more complex than just TLV, as more than a single byte may be used to encode the type and more than a single byte may be used to encode the length, or the length may not be specified at all. Second, ASN.1 has its own standard including the BER, X.690, where all this is detailed; X.509 refers to X.690 many times, often adding constraints where X.690 is not strict enough. With ITU recommendations, you rarely find everything you need in a single one, and the reference chains may be really long.</p></div><div id="comment-62546-info" class="comment-info"><span class="comment-age">(05 Jul '17, 13:09)</span> sindy</div></div><span id="62548"></span><div id="comment-62548" class="comment"><div id="post-62548-score" class="comment-score"></div><div class="comment-text"><p>Disclaimer have not looked at the actual trace. The wiredhark ber decoder has a preference to show internal ber decoding if you are really interested in the gory details.</p></div><div id="comment-62548-info" class="comment-info"><span class="comment-age">(05 Jul '17, 14:40)</span> Anders ♦</div></div><span id="62605"></span><div id="comment-62605" class="comment not_top_scorer"><div id="post-62605-score" class="comment-score"></div><div class="comment-text"><p>I see the TLV occurrences in the packet. However, still not sure how the 30:82:01:5f:a0:03 is decoded to a structure 'signedCertificate'. Maybe you can elaborate. My packet has 2 such 30:82:... sections.</p><p>"Similarly, the 02:01 "before" the version say that the version is a single-octet integer, and the 30:82:01:5f:a0:03 together say that what follows is a structure called signedCertificate."</p></div><div id="comment-62605-info" class="comment-info"><span class="comment-age">(07 Jul '17, 07:46)</span> dodge55</div></div><span id="62606"></span><div id="comment-62606" class="comment not_top_scorer"><div id="post-62606-score" class="comment-score"></div><div class="comment-text"><p>Follow the suggestion of <a href="https://ask.wireshark.org/users/42/anders">@Anders</a>: go <code>Edit-&gt;Preferences-&gt;Protocols-&gt;BER</code> and click the topmost option - <code>Show internal BER encapsulation tokens</code>.</p><p>That way, Wireshark will show you the meaning of the individual bytes.</p></div><div id="comment-62606-info" class="comment-info"><span class="comment-age">(07 Jul '17, 07:50)</span> sindy</div></div></div><div id="comment-tools-62534" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-62534-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="62531"></span>

<div id="answer-container-62531" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62531-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The certificate used is an X.509 certificate, see <a href="https://tools.ietf.org/html/rfc5280">RFC 5280</a> (updated by <a href="https://tools.ietf.org/html/rfc6818">RFC 6818</a>).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Jul '17, 09:03</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-62531" class="comments-container"><span id="62532"></span><div id="comment-62532" class="comment"><div id="post-62532-score" class="comment-score"></div><div class="comment-text"><p>Thanks. Big help. Not sure why I never found that and my books and papers don't reference that RFC in the certificate section.</p></div><div id="comment-62532-info" class="comment-info"><span class="comment-age">(05 Jul '17, 09:13)</span> dodge55</div></div><span id="62533"></span><div id="comment-62533" class="comment"><div id="post-62533-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-62533-info" class="comment-info"><span class="comment-age">(05 Jul '17, 09:14)</span> cmaynard ♦♦</div></div></div><div id="comment-tools-62531" class="comment-tools"></div><div class="clear"></div><div id="comment-62531-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

