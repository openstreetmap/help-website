+++
type = "question"
title = "Problem with SSL, maybe IIS7?"
description = '''Ok, so I have tried and tried and I cannot get the SSL connection to be decrypted. I export the key using the certificate manager on my Windows 2008 R2 server. I tell it to export the private key, do no use strong encryption, and then I give it a password. I export that out, then do openssl with: op...'''
date = "2010-09-30T13:51:00Z"
lastmod = "2010-10-01T14:01:00Z"
weight = 383
keywords = [ "ssl", "iis7" ]
aliases = [ "/questions/383" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Problem with SSL, maybe IIS7?](/questions/383/problem-with-ssl-maybe-iis7)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-383-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-383-score" class="post-score" title="current number of votes">1</div><span id="post-383-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Ok, so I have tried and tried and I cannot get the SSL connection to be decrypted.</p><p>I export the key using the certificate manager on my Windows 2008 R2 server. I tell it to export the private key, do no use strong encryption, and then I give it a password. I export that out, then do openssl with:</p><p>openssl pkcs12 -nodes -nocerts -in "mycer.pfx" -out "mycer.pem"</p><p>I then put that on the server and put the following in the wireshark SSL protocols</p><p>10.100.101.35,443,http,C:\mycer.pem</p><p>and load it up and it doesn't work. Here's the data from the debug:</p><pre><code>ssl_init keys string:
10.100.101.35,443,http,C:\mycer.pem;
ssl_init found host entry 10.100.101.35,443,http,C:\mycer.pem
ssl_init addr &#39;10.100.101.35&#39; port &#39;443&#39; filename &#39;C:\mycer.pem&#39; password(only for p12 file) &#39;(null)&#39;
Private key imported: KeyID b5:8a:14:21:92:bd:79:c8:06:fd:57:c4:56:f4:0b:34:...
ssl_init private key file C:\mycer.pem successfully loaded
association_add TCP port 443 protocol http handle 000000000677A670
ssl_init found host entry 
ssl_init entry malformed can&#39;t find port in &#39;&#39;</code></pre><p>and I don't know if that's an error or not. If I try and do the follow SSL it just shows a blank screen. Anybody have any ideas?</p><p>============= UPDATE =============</p><p>Ok, I had a semicolon on the end (I had removed it before posting here, thinking it wasn't relevant). Anyways, I removed that and now I just get this in the log</p><pre><code>ssl_init keys string:
10.100.101.35,443,http,C:\mycer.pem
ssl_init found host entry 10.100.101.35,443,http,C:\mycer.pem
ssl_init addr &#39;10.100.101.35&#39; port &#39;443&#39; filename &#39;C:\mycer.pem&#39; password(only for p12 file) &#39;(null)&#39;
Private key imported: KeyID b4:8a:14:21:95:bd:79:c8:06:fd:54:c4:56:f3:0b:34:...
ssl_init private key file C:\mycer.pem successfully loaded
association_add TCP port 443 protocol http handle 00000000066DDF40

dissect_ssl enter frame #4 (first time)
ssl_session_init: initializing ptr 0000000009051C88 size 672
  conversation = 0000000009051948, ssl_session = 0000000009051C88
  record: offset = 0, reported_length_remaining = 90
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 85, ssl state 0x00
association_find: TCP port 1431 found 0000000000000000
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 81 bytes, remaining 90 
packet_from_server: is from server - FALSE
ssl_find_private_key server 10.100.101.35:443
dissect_ssl3_hnd_hello_common found CLIENT RANDOM -&gt; state 0x01

dissect_ssl enter frame #5 (first time)
  conversation = 0000000009051948, ssl_session = 0000000009051C88
  record: offset = 0, reported_length_remaining = 71
dissect_ssl3_record found version 0x0300 -&gt; state 0x11
dissect_ssl3_record: content_type 20
dissect_ssl3_change_cipher_spec
packet_from_server: is from server - FALSE
ssl_change_cipher CLIENT
  record: offset = 6, reported_length_remaining = 65
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 60, ssl state 0x11
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 60 offset 11 length 14578034 bytes, remaining 71

dissect_ssl enter frame #6 (first time)
  conversation = 0000000009051948, ssl_session = 0000000009051C88
  record: offset = 0, reported_length_remaining = 608
dissect_ssl3_record: content_type 23
decrypt_ssl3_record: app_data len 603, ssl state 0x11
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 1431 found 0000000000000000
association_find: TCP port 443 found 0000000007455440

dissect_ssl enter frame #4 (already visited)
  conversation = 0000000009051948, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 90
dissect_ssl3_record: content_type 22
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 81 bytes, remaining 90

dissect_ssl enter frame #5 (already visited)
  conversation = 0000000009051948, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 71
dissect_ssl3_record: content_type 20
dissect_ssl3_change_cipher_spec
  record: offset = 6, reported_length_remaining = 65
dissect_ssl3_record: content_type 22
dissect_ssl3_handshake iteration 1 type 60 offset 11 length 14578034 bytes, remaining 71

dissect_ssl enter frame #6 (already visited)
  conversation = 0000000009051948, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 608
dissect_ssl3_record: content_type 23
association_find: TCP port 1431 found 0000000000000000
association_find: TCP port 443 found 0000000007455440

dissect_ssl enter frame #8 (first time)
  conversation = 0000000009051948, ssl_session = 0000000009051C88
  record: offset = 0, reported_length_remaining = 555
dissect_ssl3_record: content_type 23
decrypt_ssl3_record: app_data len 550, ssl state 0x11
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 1431 found 0000000000000000
association_find: TCP port 443 found 0000000007455440

dissect_ssl enter frame #8 (already visited)
  conversation = 0000000009051948, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 555
dissect_ssl3_record: content_type 23
association_find: TCP port 1431 found 0000000000000000
association_find: TCP port 443 found 0000000007455440</code></pre><p>as far as the cipher, I don't see any DH. The "Client Hello" Info message says "TLSV1" next to it. Even if I force it to use SSLv3 though it still does not decrypt properly.</p><p>And no, I never see any Info message that says "Certificate" specifically. All I see if this:</p><pre><code>1   2010-10-01 09:16:55.089510  firewal_0e:55:3a    Broadcast   ARP Who has 10.100.101.35?  Tell 10.100.101.1
2   2010-10-01 09:16:55.128255  xxx.xxx.xxx.xxx 10.100.101.35   TCP rgtp &gt; https [SYN] Seq=0 Win=8192 Len=0 MSS=1460 WS=2 SACK_PERM=1
3   2010-10-01 09:16:55.229766  xxx.xxx.xxx.xxx 10.100.101.35   TCP rgtp &gt; https [ACK] Seq=1 Ack=1 Win=262140 Len=0
4   2010-10-01 09:16:55.229807  xxx.xxx.xxx.xxx 10.100.101.35   SSLv3   Client Hello
5   2010-10-01 09:16:55.331682  xxx.xxx.xxx.xxx 10.100.101.35   SSLv3   Change Cipher Spec, Encrypted Handshake Message
6   2010-10-01 09:16:55.337238  xxx.xxx.xxx.xxx 10.100.101.35   SSLv3   Application Data
7   2010-10-01 09:16:55.441479  xxx.xxx.xxx.xxx 10.100.101.35   TCP rgtp &gt; https [ACK] Seq=770 Ack=1628 Win=262140 Len=0
8   2010-10-01 09:16:55.457850  xxx.xxx.xxx.xxx 10.100.101.35   SSLv3   Application Data
9   2010-10-01 09:16:55.568862  xxx.xxx.xxx.xxx 10.100.101.35   TCP rgtp &gt; https [ACK] Seq=1325 Ack=4548 Win=262140 Len=0
10  2010-10-01 09:16:55.670162  xxx.xxx.xxx.xxx 10.100.101.35   TCP rgtp &gt; https [ACK] Seq=1325 Ack=7468 Win=262140 Len=0
11  2010-10-01 09:16:55.670353  xxx.xxx.xxx.xxx 10.100.101.35   TCP rgtp &gt; https [ACK] Seq=1325 Ack=10388 Win=262140 Len=0
12  2010-10-01 09:16:55.670382  xxx.xxx.xxx.xxx 10.100.101.35   TCP rgtp &gt; https [ACK] Seq=1325 Ack=11982 Win=262140 Len=0
13  2010-10-01 09:18:00.641878  xxx.xxx.xxx.xxx 10.100.101.35   TCP rgtp &gt; https [RST, ACK] Seq=1325 Ack=11982 Win=0 Len=0</code></pre><p>Note: I changed the source IP to xxx.xxx.xxx.xxx just for security reasons, it is shown as a real registered IP on my screen.</p><p>Hopefully all that data helps to figure this out. Let me know if I need to provide anything else.</p><p>Thanks for the help!!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span> <span class="post-tag tag-link-iis7" rel="tag" title="see questions tagged &#39;iis7&#39;">iis7</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Sep '10, 13:51</strong></p><img src="https://secure.gravatar.com/avatar/83eafe0b6b6f863cd8588e6d756e0fab?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Buck&#39;s gravatar image" /><p><span>Buck</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Buck has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>01 Oct '10, 06:22</strong> </span></p></div></div><div id="comments-container-383" class="comments-container"></div><div id="comment-tools-383" class="comment-tools"></div><div class="clear"></div><div id="comment-383-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="384"></span>

<div id="answer-container-384" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-384-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-384-score" class="post-score" title="current number of votes">1</div><span id="post-384-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Buck has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Looks like you have an additional ";" at the end of this key definition that is generating the last two lines of the ssl-debug that you posted. This should however not influence the decryption of your traffic.</p><p>Three main sources for not being able to decrypt are:</p><ul><li>The key can't be loaded (which is not true in your case), due to the wrong file format</li><li>The capture file does not contain the full ssl handshake (does your trace show the "Certificate" handshake message from the server?)</li><li>The chosen cipher is a DH cipher (you can verify the chosen cipher in the ServerHello message, does it contain DH in the name? if it does, try to force your testclient to not use DH ciphers)</li></ul><hr /><p>Response to your update:</p><p>In your trace, only the traffic from the client to the server is shown. Wireshark also needs the traffic from the server to the client to do the decryption.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Sep '10, 14:03</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>01 Oct '10, 06:54</strong> </span></p></div></div><div id="comments-container-384" class="comments-container"><span id="387"></span><div id="comment-387" class="comment"><div id="post-387-score" class="comment-score"></div><div class="comment-text"><p>The problem is I have a lot of different web sites on the server, so I'm trying to filter out the other website data. What would be the best filter? I have tried</p><p>(ip.src_host == xxx.xxx.xxx.xxx &amp;&amp; ip.dst_host == 10.100.101.35) || (ip.dst_host == xxx.xxx.xxx.xxx &amp;&amp; ip.src_host == 10.100.101.35)</p><p>and</p><p>host 10.100.101.35 or host xxx.xxx.xxx.xxx as the capture filter. What should I be using to correctly filter out the data?</p></div><div id="comment-387-info" class="comment-info"><span class="comment-age">(01 Oct '10, 07:06)</span> <span class="comment-user userinfo">Buck</span></div></div><span id="388"></span><div id="comment-388" class="comment"><div id="post-388-score" class="comment-score"></div><div class="comment-text"><p>Looks like you are using the right filters (well, it's ip.src and ip.dst, but I'm sure you used those).</p><p>Where did you make the tracefile, it could be that traffic to and from the server are taking other paths. In that case you need to either take captures at two points or find a place where both flows travel the same path.</p><p>Or it could be that one side of the connection is vlan tagged while the other is not. In that case, could you try the following capture filter?</p><p>host 10.100.101.35 or host xxx.xxx.xxx.xxx or (vlan and (host 10.100.101.35 or host xxx.xxx.xxx.xxx))</p></div><div id="comment-388-info" class="comment-info"><span class="comment-age">(01 Oct '10, 07:14)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="389"></span><div id="comment-389" class="comment"><div id="post-389-score" class="comment-score"></div><div class="comment-text"><p>Well, I don't think the filters are causing it, cause I removed them all and just ran the trace real quick and I still could not decipher the SSL.</p><p>I do have two network cards in my server though, one for incoming traffic (no gateway specified), and one for outgoing traffic (gateway specified). I guess that means that's where the problem is occurring? If that's the case though, how do I capture from both interfaces at the same time?</p></div><div id="comment-389-info" class="comment-info"><span class="comment-age">(01 Oct '10, 07:20)</span> <span class="comment-user userinfo">Buck</span></div></div><span id="390"></span><div id="comment-390" class="comment"><div id="post-390-score" class="comment-score"></div><div class="comment-text"><p>If I switch it to the other interface, I seem to get both sides talking, although every request from my server to the destination is a black line and it says the header checksum is incorrect. I still can't decrypt the traffic, but I suppose that's because some packets must still be on the other interface? I do see the "Server Hello, Certificate, Server Hello Done" now</p></div><div id="comment-390-info" class="comment-info"><span class="comment-age">(01 Oct '10, 07:28)</span> <span class="comment-user userinfo">Buck</span></div></div><span id="391"></span><div id="comment-391" class="comment"><div id="post-391-score" class="comment-score"></div><div class="comment-text"><p>When Wireshark detects bad checksums, it will not perform decryption, as the data is not trustworthy. However, if you have bad checksums on all outgoing packets, that is most likely the result of TCP checksum offloading. In that case disabling checksum checking at the TCP layer will help.</p><p>You can disable TCP checksum checking in the TCP protocol preferences.</p></div><div id="comment-391-info" class="comment-info"><span class="comment-age">(01 Oct '10, 07:39)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="393"></span><div id="comment-393" class="comment not_top_scorer"><div id="post-393-score" class="comment-score"></div><div class="comment-text"><p>Ok, I didn't have it on the TCP, but I disabled it on the IP protocol and that seems to have removed the black lines, still can't decipher the SSL though.</p></div><div id="comment-393-info" class="comment-info"><span class="comment-age">(01 Oct '10, 07:48)</span> <span class="comment-user userinfo">Buck</span></div></div><span id="394"></span><div id="comment-394" class="comment not_top_scorer"><div id="post-394-score" class="comment-score"></div><div class="comment-text"><p>Sounds like it might be checksum offloading at the IP layer. You might want to disable Checksum Checking in the IP protocol preferences too, although I'm not sure whether that will actually make a difference on whether Wireshark will decrypt or not.</p><p>Maybe it's easier to capture on a spanport that mirrors both interfaces?</p></div><div id="comment-394-info" class="comment-info"><span class="comment-age">(01 Oct '10, 07:51)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="395"></span><div id="comment-395" class="comment not_top_scorer"><div id="post-395-score" class="comment-score"></div><div class="comment-text"><p>Maybe it's still the cipher being a DH cipher. Can you look at the details of the "ServerHello" message and tell me what cipher has been chosen (BTW the cipher is not the SSL/TLS version that you mentioned earlier).</p></div><div id="comment-395-info" class="comment-info"><span class="comment-age">(01 Oct '10, 07:55)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="396"></span><div id="comment-396" class="comment not_top_scorer"><div id="post-396-score" class="comment-score"></div><div class="comment-text"><p>I see Cipher Suite: TLS_RSA_WITH_AES_128_CBC_SHA (0x002f)</p></div><div id="comment-396-info" class="comment-info"><span class="comment-age">(01 Oct '10, 07:57)</span> <span class="comment-user userinfo">Buck</span></div></div><span id="397"></span><div id="comment-397" class="comment not_top_scorer"><div id="post-397-score" class="comment-score"></div><div class="comment-text"><p>Wireshark should be able to decrypt that, so it's something else. I think it will be very hard to help you any further without being able to look at the tracefiles themselves.</p><p>My bet would be that the setup with two interfaces is interfering, so if you are able to capture on a spanport that mirrors both interfaces, that would be my best bet.</p></div><div id="comment-397-info" class="comment-info"><span class="comment-age">(01 Oct '10, 08:01)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="398"></span><div id="comment-398" class="comment not_top_scorer"><div id="post-398-score" class="comment-score"></div><div class="comment-text"><p>This server runs on a VMWare ESXi box as well, do you think that would cause any sort of problem?</p></div><div id="comment-398-info" class="comment-info"><span class="comment-age">(01 Oct '10, 08:16)</span> <span class="comment-user userinfo">Buck</span></div></div><span id="403"></span><div id="comment-403" class="comment not_top_scorer"><div id="post-403-score" class="comment-score"></div><div class="comment-text"><p>ok, think I got this sorted out. It was really a combination of the problem above combined with an error with the client who was connecting (which was what I was double checking in the first place). Now I just have a different question, but I'll make a new thread for that. Thanks for all your help SYNbit - I'm able to successfully decrypt SSL connections from different clients now :)</p></div><div id="comment-403-info" class="comment-info"><span class="comment-age">(01 Oct '10, 13:29)</span> <span class="comment-user userinfo">Buck</span></div></div><span id="404"></span><div id="comment-404" class="comment not_top_scorer"><div id="post-404-score" class="comment-score"></div><div class="comment-text"><p>Glad to be of help!</p><p>Just out of curiosity, what was the combination of problems?</p></div><div id="comment-404-info" class="comment-info"><span class="comment-age">(01 Oct '10, 14:01)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div></div><div id="comment-tools-384" class="comment-tools"><span class="comments-showing"> showing 5 of 13 </span> <a href="#" class="show-all-comments-link">show 8 more comments</a></div><div class="clear"></div><div id="comment-384-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="385"></span>

<div id="answer-container-385" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-385-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-385-score" class="post-score" title="current number of votes">0</div><span id="post-385-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There's an empty entry trailing the first one. That's what this says:</p><p><code>ssl_init found host entry</code></p><p>That's what the parser barfs on (it shouldn't). Clean up the preference entry (no trailing spaces, etc) and try again.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Sep '10, 14:08</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-385" class="comments-container"></div><div id="comment-tools-385" class="comment-tools"></div><div class="clear"></div><div id="comment-385-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

