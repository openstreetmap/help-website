+++
type = "question"
title = "SSL Record Layer vs SSLv3 Record Layer"
description = '''Hi, I have two captures, one of an successful SSL handshake, and one of an unsuccessful SSL handshake (server never responded with server hello but instead sent a FIN,ACK). The successful one displays in wireshark protocol column as SSLv3, and in the decoding window shows like so: Secure Socket Laye...'''
date = "2012-09-21T02:39:00Z"
lastmod = "2012-09-21T03:30:00Z"
weight = 14419
keywords = [ "ssl", "sslv3", "wireshark" ]
aliases = [ "/questions/14419" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [SSL Record Layer vs SSLv3 Record Layer](/questions/14419/ssl-record-layer-vs-sslv3-record-layer)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14419-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have two captures, one of an successful SSL handshake, and one of an unsuccessful SSL handshake (server never responded with server hello but instead sent a FIN,ACK).</p><p>The successful one displays in wireshark protocol column as SSLv3, and in the decoding window shows like so:</p><pre><code>Secure Socket Layer
    SSLv3 Record Layer: Handshake Protocol: Client Hello
        Content Type: Handshake (22)
        Version: SSL 3.0 (0x0300)
        Length: 117
        Handshake Protocol: Client Hello</code></pre><p>The unsuccessful one shows in wireshark protocol column as merely SSL (not SSLv3), and in the decoding window as:</p><pre><code>Secure Socket Layer
    SSL Record Layer: Handshake Protocol: Client Hello
        Content Type: Handshake (22)
        Version: SSL 3.0 (0x0300)
        Length: 117
        Handshake Protocol: Client Hello</code></pre><p>Both have SSL3.0 in the version field, so what subtle difference is wireshark detecting that makes it display as SSL rather than SSLv3 ?</p><p>Thanks in advance for any help you can offer.</p></div><div id="question-tags" class="tags-container tags">ssl sslv3 wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Sep '12, 02:39</strong></p><img src="https://secure.gravatar.com/avatar/dff1ae27592f30f7991ebdd5aa3898ed?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="adrian777uk&#39;s gravatar image" /><p>adrian777uk<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="adrian777uk has no accepted answers">0%</span></p></div></div><div id="comments-container-14419" class="comments-container"></div><div id="comment-tools-14419" class="comment-tools"></div><div class="clear"></div><div id="comment-14419-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14422"></span>

<div id="answer-container-14422" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14422-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The subtle difference is (without looking at the actual trace, so I might be wrong) that in the unsuccesful case, the SSL record has version 2 and the SSL handshake message has version 3.0. Does your SSL record start with 0x80 or with 0x16?</p><p>In the transition from SSLv2 to SSLv3 backward compatibility was ensured by using a SSLv2 record layer header. But today most servers won't allow (the insecure) SSLv2 protocol, so if the client tries a SSLv2 compatible handshake, the server just denies the connection.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Sep '12, 03:30</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-14422" class="comments-container"><span id="14423"></span><div id="comment-14423" class="comment"><div id="post-14423-score" class="comment-score"></div><div class="comment-text"><p>Thanks. I think they both start with 22 (0x16) as they both have</p><pre><code>    Content Type: Handshake (22)
    Version: SSL 3.0 (0x0300)</code></pre><p>in the header. Here's a more comprehensive dump of the unsuccessful one:</p><pre><code>No.     Time            Source                Destination           Protocol Info
    542 16:06:25.801354 172.16.0.15           10.185.116.11         SSL      Client Hello

Frame 542 (176 bytes on wire, 176 bytes captured)
Internet Protocol, Src: 172.16.0.15 (172.16.0.15), Dst: 10.185.116.11 (10.185.116.11)
    Version: 4
    Header length: 20 bytes
    Differentiated Services Field: 0x00 (DSCP 0x00: Default; ECN: 0x00)
        0000 00.. = Differentiated Services Codepoint: Default (0x00)
        .... ..0. = ECN-Capable Transport (ECT): 0
        .... ...0 = ECN-CE: 0
    Total Length: 162
    Identification: 0xb641 (46657)
    Flags: 0x02 (Don&#39;t Fragment)
        0.. = Reserved bit: Not Set
        .1. = Don&#39;t fragment: Set
        ..0 = More fragments: Not Set
    Fragment offset: 0
    Time to live: 64
    Protocol: TCP (0x06)
    Header checksum: 0x5931 [correct]
        [Good: True]
        [Bad : False]
    Source: 172.16.0.15 (172.16.0.15)
    Destination: 10.185.116.11 (10.185.116.11)
Transmission Control Protocol, Src Port: 39767 (39767), Dst Port: https (443), Seq: 1, Ack: 1, Len: 122
    Source port: 39767 (39767)
    Destination port: https (443)
    [Stream index: 2]
    Sequence number: 1    (relative sequence number)
    [Next sequence number: 123    (relative sequence number)]
    Acknowledgement number: 1    (relative ack number)
    Header length: 20 bytes
    Flags: 0x18 (PSH, ACK)
        0... .... = Congestion Window Reduced (CWR): Not set
        .0.. .... = ECN-Echo: Not set
        ..0. .... = Urgent: Not set
        ...1 .... = Acknowledgement: Set
        .... 1... = Push: Set
        .... .0.. = Reset: Not set
        .... ..0. = Syn: Not set
        .... ...0 = Fin: Not set
    Window size: 5440
    Checksum: 0x41dd [validation disabled]
        [Good Checksum: False]
        [Bad Checksum: False]
    [SEQ/ACK analysis]
        [Number of bytes in flight: 122]
Secure Socket Layer
    SSL Record Layer: Handshake Protocol: Client Hello
        Content Type: Handshake (22)
        Version: SSL 3.0 (0x0300)
        Length: 117
        Handshake Protocol: Client Hello
            Handshake Type: Client Hello (1)
            Length: 113
            Version: SSL 3.0 (0x0300)
            Random
                gmt_unix_time: Sep 10, 2012 16:06:25.000000000
                random_bytes: BF21E5DA81585DA77701ED324B3A8C03938A4375A6EFB741...
            Session ID Length: 32
            Session ID: 37DFA6901134DA4015FD365E790211A85D98C05504D18347...
            Cipher Suites Length: 42
            Cipher Suites (21 suites)
            Compression Methods Length: 1
            Compression Methods (1 method)
                Compression Method: null (0)</code></pre><p>and the successful one:</p><pre><code>No.     Time                       Source                Destination           Protocol Info
    401 2012-09-21 09:45:04.539900 172.16.100.10         10.185.116.11         SSLv3    Client Hello

Frame 401 (176 bytes on wire, 176 bytes captured)
Internet Protocol, Src: 172.16.100.10 (172.16.100.10), Dst: 10.185.116.11 (10.185.116.11)
    Version: 4
    Header length: 20 bytes
    Differentiated Services Field: 0x00 (DSCP 0x00: Default; ECN: 0x00)
        0000 00.. = Differentiated Services Codepoint: Default (0x00)
        .... ..0. = ECN-Capable Transport (ECT): 0
        .... ...0 = ECN-CE: 0
    Total Length: 162
    Identification: 0x92ff (37631)
    Flags: 0x02 (Don&#39;t Fragment)
        0.. = Reserved bit: Not Set
        .1. = Don&#39;t fragment: Set
        ..0 = More fragments: Not Set
    Fragment offset: 0
    Time to live: 64
    Protocol: TCP (0x06)
    Header checksum: 0x1878 [correct]
    Source: 172.16.100.10 (172.16.100.10)
    Destination: 10.185.116.11 (10.185.116.11)
Transmission Control Protocol, Src Port: 33386 (33386), Dst Port: https (443), Seq: 1, Ack: 1, Len: 122
    Source port: 33386 (33386)
    Destination port: https (443)
    [Stream index: 2]
    Sequence number: 1    (relative sequence number)
    [Next sequence number: 123    (relative sequence number)]
    Acknowledgement number: 1    (relative ack number)
    Header length: 20 bytes
    Flags: 0x18 (PSH, ACK)
        0... .... = Congestion Window Reduced (CWR): Not set
        .0.. .... = ECN-Echo: Not set
        ..0. .... = Urgent: Not set
        ...1 .... = Acknowledgement: Set
        .... 1... = Push: Set
        .... .0.. = Reset: Not set
        .... ..0. = Syn: Not set
        .... ...0 = Fin: Not set
    Window size: 5840
    Checksum: 0xb900 [validation disabled]
        [Good Checksum: False]
        [Bad Checksum: False]
    [SEQ/ACK analysis]
        [Number of bytes in flight: 122]
Secure Socket Layer
    SSLv3 Record Layer: Handshake Protocol: Client Hello
        Content Type: Handshake (22)
        Version: SSL 3.0 (0x0300)
        Length: 117
        Handshake Protocol: Client Hello
            Handshake Type: Client Hello (1)
            Length: 113
            Version: SSL 3.0 (0x0300)
            Random
                gmt_unix_time: Sep 21, 2012 09:45:04.000000000
                random_bytes: 6AEA044A8357E2C4599E20EAB712601A1C224D3B63C4F2B4...
            Session ID Length: 32
            Session ID: 1C2938C6CCE3EA7E117CAC9623B9B0DC17E13E480B166D26...
            Cipher Suites Length: 42
            Cipher Suites (21 suites)
            Compression Methods Length: 1
            Compression Methods (1 method)
                Compression Method: null (0)</code></pre></div><div id="comment-14423-info" class="comment-info"><span class="comment-age">(21 Sep '12, 03:50)</span> adrian777uk</div></div><span id="14425"></span><div id="comment-14425" class="comment"><div id="post-14425-score" class="comment-score"></div><div class="comment-text"><p>OK, I just tested it myself, Wireshark will only set the info column to SSLv3 when it sees the ServerHello. I think this is due to the SSLv2, SSLv3 scenario I sketched in my first response. So in fact you have two (almost) identical ClientHello's.</p><p>Then it is either the source IP which might not be allowed to connect or the server might limit the amount of connections? What kind of server are you running? Does the FIN come straight after the ClientHello or is there a delay between them?</p></div><div id="comment-14425-info" class="comment-info"><span class="comment-age">(21 Sep '12, 04:09)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-14422" class="comment-tools"></div><div class="clear"></div><div id="comment-14422-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

