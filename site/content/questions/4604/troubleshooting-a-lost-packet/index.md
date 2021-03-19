+++
type = "question"
title = "Troubleshooting a lost packet"
description = '''A customer in Taiwan is connection to my secured web server using Chrome. We&#x27;re running javascript (compiled with GWT) in the browser session, sending requests back to the server via the XmlHttpRequest object. There seems to be one particular code path that gets &quot;stuck&quot;; it will seem to be working f...'''
date = "2011-06-16T13:49:00Z"
lastmod = "2011-06-19T14:47:00Z"
weight = 4604
keywords = [ "troubleshooting", "analysis" ]
aliases = [ "/questions/4604" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Troubleshooting a lost packet](/questions/4604/troubleshooting-a-lost-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4604-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>A customer in Taiwan is connection to my secured web server using Chrome. We're running javascript (compiled with GWT) in the browser session, sending requests back to the server via the XmlHttpRequest object. There seems to be one particular code path that gets "stuck"; it will seem to be working fine, and then some change (presumably to the data being sent) will "break" the communication.</p><p>In the httpd access logs, we see 400 responses to these requests, sent after the 120 second timeout elapses. The access log also reports the SSL_PROTOCOL (TLSv1) and the SSL_CIPHER (DHE-RSA-AES256-SHA). We're actually seeing the request line, some of our custom cookies, so the message headers in the request appear to be complete.</p><p>In the httpd error logs, we see a bunch of "(70007)The timeout specified has expired: proxy: prefetch request body failed" as mod_proxy tries to pass the request through to the application server on the back end.</p><p>We set up a dumpcap job, which records traffic from this particular ip-block. Because I wasn't sure how much disk was necessary, I've been using a SNAPLEN of 66 bytes (the data is supposed to be encrypted, so I wasn't expecting any more than that to be useful?)</p><p>Reviewing the capture with Wireshark tells me that each of these failures matches a particular pattern of packets. For example</p><p>Frame 3004: a packet from the client, Len: 69. The gap between this packet and the previous in the tcp.stream is about 9 seconds, so this is clearly the beginning of the problem request (timestamp matches that found in the httpd logs). Wireshark identifies the protocol as "SSL"</p><p>Frame 3005: a packet from the client, Len: 377. Wireshark identifies the protocol as "TLSv1". It also reports TCP Previous segment lost. Some quick math on the actual sequence number vs the expected sequence number suggests about 1530 bytes of data are absent. The arrival of this packet was about 40ms after frame 3004. This is the last packet we see from the client in this tcp.stream</p><p>Frame 3006: ACK sent to the client. The sequence number is ...2669, appears to be the acknowledgement number for both inbound packets in frames 3004 and 3005. The acknowledgement number for the outbound packet is ...2973, which matches the "next sequence number" for frame 3004.</p><p>Two minute pause with no packets exchanged.</p><p>Frame 3140/3141: the server sends an SSL packet pair, which presumably is the status 400 page. Frame 3142: FIN/ACK Frame 3143, etc: throttled retries of the packet sent in Frame 3140.</p><p>One other data point. About 20 seconds after the problem request, we get an http request to report that this logic failed. Our client side code includes a timer object which fails after about 15 seconds, and we drop into logic to report the error (no problems there) followed by a retry attempt (packet sizes on subsequent attempts can be slightly different because the client data changed during the 20 second interval). The retry event failed with the same symptoms.</p><p>As far as I can tell, once we get into this state, the problem persists until the client's browser process is killed and restarted. The server, during the problem interval, is happily fielding other requests, including those of the same type that our giving us problems here.</p><p>And I'm stumped -- this doesn't match anything in my experience. I don't have access to the client network, so I can't currently see what the traffic looks like from that end; we haven't been able to identify a trigger that would allow us to reproduce the problem elsewhere, and my google searches don't seem to find a match for these symptoms.</p></div><div id="question-tags" class="tags-container tags">troubleshooting analysis</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Jun '11, 13:49</strong></p><img src="https://secure.gravatar.com/avatar/8911a98abd797fd928ab9f115becd08c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DanilSuits&#39;s gravatar image" /><p>DanilSuits<br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DanilSuits has no accepted answers">0%</span></p></div></div><div id="comments-container-4604" class="comments-container"></div><div id="comment-tools-4604" class="comment-tools"></div><div class="clear"></div><div id="comment-4604-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="4606"></span>

<div id="answer-container-4606" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4606-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>It also reports TCP Previous segment lost. Some quick math on the actual sequence number vs the expected sequence number suggests about 1530 bytes of data are absent.</p></blockquote><p>This seems to be the most interesting. 1530 bytes missing? That's an odd MTU size...</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Jun '11, 14:37</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-4606" class="comments-container"><span id="4608"></span><div id="comment-4608" class="comment"><div id="post-4608-score" class="comment-score"></div><div class="comment-text"><p>Plus or minus 20, for today's examples. I also need to see if that estimate jibes with the successful saves we saw prior to the incident/after the restart.</p></div><div id="comment-4608-info" class="comment-info"><span class="comment-age">(16 Jun '11, 17:12)</span> DanilSuits</div></div></div><div id="comment-tools-4606" class="comment-tools"></div><div class="clear"></div><div id="comment-4606-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="4626"></span>

<div id="answer-container-4626" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4626-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You might want to use a higher snaplength so that will at least be able to identify the SSL handshake messages that will give you more insight in the datastream.</p><p>Also, a packet capture file (or at least some more output lines) of the complete TCP session will help to help you...</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Jun '11, 14:47</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-4626" class="comments-container"></div><div id="comment-tools-4626" class="comment-tools"></div><div class="clear"></div><div id="comment-4626-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

