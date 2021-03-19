+++
type = "question"
title = "Non controlled llsurfup-https packet and connection reset"
description = '''Hello, I&#x27;ve a tcp server socket application listening on 1999 port, and several devices connects to it, through their respective internet connections (routers). The problem is that serveral of this devices have an unexpected connection behaviour, that i&#x27;m going explain. Server IP -&amp;gt; listening on ...'''
date = "2013-08-21T03:36:00Z"
lastmod = "2013-08-21T13:56:00Z"
weight = 23902
keywords = [ "reset", "llsurfup-https" ]
aliases = [ "/questions/23902" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Non controlled llsurfup-https packet and connection reset](/questions/23902/non-controlled-llsurfup-https-packet-and-connection-reset)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23902-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I've a tcp server socket application listening on 1999 port, and several devices connects to it, through their respective internet connections (routers). The problem is that serveral of this devices have an unexpected connection behaviour, that i'm going explain.</p><p>Server IP -&gt; listening on port 1999</p><p>Device IP -&gt; send request from port 1025</p><p>Server &lt;- Device : Send SYN to stablish the connection</p><p>Server -&gt; Device : Send SYN, ACK</p><p>Server &lt;- Device : Send ACK. Connection stablished</p><p>Server &lt;- Device : Send PUSH, ACK Send data to de server (1 packet)</p><p>Server -&gt; Device : ACK, Everything seems to be OK till here</p><p>Server -&gt; Device : PUSH some data from port 1999 to port 1025</p><p>Server -&gt; Device : PUSH the same data than the packet before form port 1999 to port 1184</p><p>Server &lt;- Device : ACK for the PUSH form 1999 to 1184</p><p>The push to the 1184 (llsurfup-https) is unexpected and is not controlled by my application, the correct ACK is lost and the connection is reset after 5 attempts.</p><p>I have not found any suitable information in internet about (llsurfup-https) nor what could be the cause of the problem</p><p>This is the trace, and the problem starts in the line 32. <a href="https://docs.google.com/file/d/0BwiWOLmOB31bbk5Cc0NIeTlMUk0/edit?usp=sharing">https://docs.google.com/file/d/0BwiWOLmOB31bbk5Cc0NIeTlMUk0/edit?usp=sharing</a></p><p>I'd appreciate any help. Thank you in advance!!</p></div><div id="question-tags" class="tags-container tags">reset llsurfup-https</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Aug '13, 03:36</strong></p><img src="https://secure.gravatar.com/avatar/5f8e2c8843008f76b9d6d37fe1b5443a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ferran&#39;s gravatar image" /><p>Ferran<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ferran has no accepted answers">0%</span></p></div></div><div id="comments-container-23902" class="comments-container"></div><div id="comment-tools-23902" class="comment-tools"></div><div class="clear"></div><div id="comment-23902-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="23931"></span>

<div id="answer-container-23931" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23931-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p><strong>Easy one first</strong>: the "llsurfup-https" can be ignored as it is just the client's ephemeral port number that is resolved to this name. So, don't worry about finding information about it.</p><p>Ok, now to the traffic that is going out of your server: <img src="https://osqa-ask.wireshark.org/upfiles/Selection_043_1.png" alt="alt text" /></p><p>Your server is sending the same 13 bytes of data on all active sockets at the same time.</p><p>The ip.id delta in each batch of outbound data suggests that there are 3 additional packets (connections) sent which are not in the trace.</p><p>The interval between the send()s is 10 seconds (+ ~140ms). <code>example: 070d0fff802d0a0b1508040d00</code> The last 8 bytes seems to be a time in seconds in little endian notation as it increments by ten every ten seconds.</p><p>So I doubt that "The push to the 1184 (llsurfup-https) is unexpected and is not controlled by my application" is really not controlled by your application. It is sent over (at least) 2 TCP connections simultaneously so the server must have sent it.</p><p><strong>How do the clients behave?</strong> We are talking about at least two different clients. One tcp.port==1184 responding to your data with data, the other one just acknowledging your data, not sending anything back Here the good case <img src="https://osqa-ask.wireshark.org/upfiles/Selection_045.png" alt="alt text" /> Port 1184 is behaving well returning also 13 bytes when it received your data. The RTT is ~31 ms and your server delay_acks this data, everyone happy!</p><p>Port 1025 is not returning your data but just acking with increasing delays 80ms-166 ms. <img src="https://osqa-ask.wireshark.org/upfiles/Selection_046.png" alt="alt text" /> In Packet 24 the 'client' closes the connection as a FIN is coming in. Note that the ip.ttl is 54 this time while it was 55 on all other ACK packets. In packet 26 your server closes the connection, a FIN is sent out but doesn't get an ACK so you enter retransmission with increasing intervals,</p><p>In packet 31 the 'client' or NAT resets the connection</p><p>So from a distance it looks like the client's application doesn't know how to react on your data.</p><p>The 'client' or NAT is re-using the client port numbers so it is a little tricky to filter on the next connection: <code>tcp.stream eq 2 and frame.number lt 74</code> shows the new connection from a mis-behaving clients, ending up in the same sequence.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Aug '13, 13:56</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p>mrEEde<br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 21 Aug '13, 22:55</p></div></div><div id="comments-container-23931" class="comments-container"></div><div id="comment-tools-23931" class="comment-tools"></div><div class="clear"></div><div id="comment-23931-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

