+++
type = "question"
title = "Decrypt SSL Traffic destined for Squid Proxy Server"
description = '''I am trying to decrypt SSL traffic between a client (Firefox) and a Squid Proxy server that is using ssl-jump. The SSL certificate on the server is a private cert linked to the ssl-bump feature. I am using tshark to dump the SSL traffic. I know all the certificates work fine because when I take Squi...'''
date = "2011-05-31T23:00:00Z"
lastmod = "2011-06-01T23:13:00Z"
weight = 4303
keywords = [ "ssl", "squid", "decrypt" ]
aliases = [ "/questions/4303" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Decrypt SSL Traffic destined for Squid Proxy Server](/questions/4303/decrypt-ssl-traffic-destined-for-squid-proxy-server)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4303-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to decrypt SSL traffic between a client (Firefox) and a Squid Proxy server that is using ssl-jump. The SSL certificate on the server is a private cert linked to the ssl-bump feature. I am using tshark to dump the SSL traffic.</p><p>I know all the certificates work fine because when I take Squid out of the path I can decrypt the traffic. However as soon as the SSL traffic is destined for the proxy on port 3128 I can't decrypt it.</p><p>For example I can create a client key, run up a server on 4443 using openssl and dump the traffic with these commands.</p><ol><li><p>openssl req -new -x509 -nodes -out client.pem -keyout client.key -subj /CN=Moi/O=Foo/C=NL</p></li><li><p>openssl s_server -ssl3 -cipher AES256-SHA -accept 4443 -www -CAfile client.pem -verify 1 -key privkey.pem</p></li><li><p>sudo tshark -o "ssl.desegment_ssl_records: TRUE" -o "ssl.desegment_ssl_application_data: TRUE" -o "ssl.keys_list: 10.1.0.126,4443,http,/home/me/privkey.pem" -o "ssl.debug_file: /home/me/.wireshark-log" -i eth0 -R "tcp.port == 4443"</p></li><li><p>(echo GET /?s=my+query+string HTTP/1.0; echo ; sleep 1) | openssl s_client -connect 10.1.0.126:4443 -ssl3 -cert client.pem -key client.key</p></li></ol><p>However I can't dissect the traffic when I send via Squid, I have tried the 'http' and 'data' dissector to no avail ;(</p><p>tshark -o "ssl.desegment_ssl_records: TRUE" -o "ssl.desegment_ssl_application_data: TRUE" -o "ssl.keys_list:0.0.0.0,3128,data,/home/me/privkey.pem" -o "ssl.debug_file: /home/me/.wireshark-log" -i eth0 -R "tcp.port == 3128"</p><p>Is there a way to decrypt the traffic when it I am using Squid proxy and certificates I have configured to use via Squid's ssl-bump?</p><p>Regards,</p><p>Michael</p></div><div id="question-tags" class="tags-container tags">ssl squid decrypt</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 May '11, 23:00</strong></p><img src="https://secure.gravatar.com/avatar/0a4073f9af645419ed04a899fdd42d1b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cloudjunky&#39;s gravatar image" /><p>cloudjunky<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cloudjunky has no accepted answers">0%</span></p></div></div><div id="comments-container-4303" class="comments-container"></div><div id="comment-tools-4303" class="comment-tools"></div><div class="clear"></div><div id="comment-4303-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="4326"></span>

<div id="answer-container-4326" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4326-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>When you use ssl-bump, Squid becomes a man-in-the-middle. This means there are actaully two ssl sessions. One between the client and squid, the other between squid and the server.</p><p>You should be able to decrypt the session between squid and the server, however, for the session between the client and squid, there is a new certificate being created by squid. Of course it does not have the server key, so a new key is generated and used for that session. Therefor you can't decrypt it...</p><p>...however, in very recent automated development builds, you can use the openssl s_client output (in which the Master Secret is logged) to decrypt the session. See <a href="http://ask.wireshark.org/questions/4229/follow-ssl-stream-using-master-key-and-session-id">this question</a> for more details.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Jun '11, 23:13</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-4326" class="comments-container"></div><div id="comment-tools-4326" class="comment-tools"></div><div class="clear"></div><div id="comment-4326-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

