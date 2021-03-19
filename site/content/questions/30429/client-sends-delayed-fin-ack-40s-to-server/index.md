+++
type = "question"
title = "client sends delayed FIN ACK (40s) to server"
description = '''Hi, We have one application which uses wininet.dll to communicate to server(192.168.0.155).Client (172.16.20.5) requesting some data from http/tcp service from linux server (192.168.0.155). Client is installed on winXP OS. Why client sends FIN ACK after 40s? Why so slow? He should send FIN ACK immed...'''
date = "2014-03-04T23:40:00Z"
lastmod = "2014-03-05T00:20:00Z"
weight = 30429
keywords = [ "ask", "delay", "fin", "quit", "to" ]
aliases = [ "/questions/30429" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [client sends delayed FIN ACK (40s) to server](/questions/30429/client-sends-delayed-fin-ack-40s-to-server)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30429-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, We have one application which uses wininet.dll to communicate to server(192.168.0.155).Client (172.16.20.5) requesting some data from http/tcp service from linux server (192.168.0.155). Client is installed on winXP OS.</p><p>Why client sends FIN ACK after 40s? Why so slow? He should send FIN ACK immediately.</p><p>Client is using wininet.dll to communicate to server . I tried may options while editing reg_keys also, but no success . also tried on win 7 machine but found same logs. How to debug this? What could it be? I traced some of the secure websites ,they also show delay but not so much delay.</p><p><a href="http://cloudshark.org/captures/0691a358e1a9?filter=ip.src%3D%3D172.16.20.5%20%26%26%20ip.dst%3D%3D192.168.0.155">http://cloudshark.org/captures/0691a358e1a9?filter=ip.src%3D%3D172.16.20.5%20%26%26%20ip.dst%3D%3D192.168.0.155</a></p><p><a href="http://cloudshark.org/captures/0691a358e1a9?filter=ip.src%3D%3D172.16.20.5%20%26%26%20ip.dst%3D%3D192.168.0.155">link text</a></p></div><div id="question-tags" class="tags-container tags">ask delay fin quit to</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Mar '14, 23:40</strong></p><img src="https://secure.gravatar.com/avatar/7fe6541df8c091a4f559a422fa224bf3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Abhi&#39;s gravatar image" /><p>Abhi<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Abhi has no accepted answers">0%</span></p></div></div><div id="comments-container-30429" class="comments-container"></div><div id="comment-tools-30429" class="comment-tools"></div><div class="clear"></div><div id="comment-30429-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="30432"></span>

<div id="answer-container-30432" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30432-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>What you have there is completely normal behavior when using HTTP keep-alives. Your client (e.g in frame 136) says "Connection: Keep-Alive" and the server accepts that (e.g in Frame 138), which means that the server allows the client to request multiple documents in one single TCP session. This is useful to avoid opening many connections for many documents.</p><p>After the server sends the requested document in frame 138 it waits another 20 seconds (in case the client needs anything else) and then says "okay, I'm done" by sending a fin in frame 211, because obviously there is no further request. The client accepts that but holds back its own FIN for another 40 seconds in case there are packets coming in out of order. All of this is pretty normal behavior when using FIN to close a connection, because it does not mean that both have to close the connection synchronously. They can do it quite indepentently.</p><p>If you want to avoid this behavior you could try to set the server to disallow keeping connections open, but that will cost performance when the server is requested a lot of documents from a couple of nodes. Or you could try a different web browser, because there are some (like Microsoft IE) that use RST instead of FIN, which is closing the session instantly.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Mar '14, 00:20</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-30432" class="comments-container"><span id="30435"></span><div id="comment-30435" class="comment"><div id="post-30435-score" class="comment-score"></div><div class="comment-text"><p>thanks for ur answer Jasper and clearing the things...</p><p>here we are not using any browser .Installed agent communicate server through 8080 port.</p><p>Can u pls suggest some other options for immediate response rather than 40s delay.<br />
</p></div><div id="comment-30435-info" class="comment-info"><span class="comment-age">(05 Mar '14, 02:03)</span> Abhi</div></div><span id="30437"></span><div id="comment-30437" class="comment"><div id="post-30437-score" class="comment-score"></div><div class="comment-text"><p>Let me ask you one thing first: is it a problem that the connection takes 40s to close the connection? Yes, it is a long time, but it is not really a "delay" when it comes to the actual data transfer. All data is exchanged already, only the session shutdown takes a long time. That usually does not delay the application at all because it is a TCP stack topic.</p><p>The only two reasons to fight the 40s shutdown are 1. you don't like it because it is unnecessary 2. you're opening tons of connections and the client gets into trouble by having too many open connections simultaneously</p><p>If both reasons do not apply you could just ignore the delay for the time being.</p></div><div id="comment-30437-info" class="comment-info"><span class="comment-age">(05 Mar '14, 02:36)</span> Jasper ♦♦</div></div><span id="30463"></span><div id="comment-30463" class="comment"><div id="post-30463-score" class="comment-score"></div><div class="comment-text"><p>we have tried turning off "Connection: Keep-Alive" at server . And now there is NO delay while closing connection. We are testing this option at another level .</p></div><div id="comment-30463-info" class="comment-info"><span class="comment-age">(05 Mar '14, 23:30)</span> Abhi</div></div><span id="30465"></span><div id="comment-30465" class="comment"><div id="post-30465-score" class="comment-score"></div><div class="comment-text"><p>Allow me to add to Jasper response. In general case, the delay in closure of a HTTP session should not be a problem as Jasper has pointed out. In fact, the reason why HTTP keepalive is added in HTTP/1.1 is to improve the performance of the HTTP performance so that each and every HTTP request doesn't have to go through the normal TCP handshake and resulting in more round trips needed and the TCP keepalive allows the clients to reuse the existing session keep the session alive for a little longer.</p><p>BUT, there is a cost to that and this could be a problem (I am not sure if this is the case that you are trying to solve. If not, i'll just leave the settings to default). If you have a very very busy server where you ran out of memory or TCP connections and new connections are having problems to be created due to too many existing connections not being closed fast enough.</p><p>In some cases, I've troubleshooted whereby you want to close the connection immediately when you are doing IPSLA measurements from a device such as routers so that the correct readings are being measured/taken and the correct way to do that is to force the client IPSLA to run HTTP/1.0 rather than requesting it via HTTP/1.1 and that will force the connection to be close immediately.</p><p>Hope that helps!</p></div><div id="comment-30465-info" class="comment-info"><span class="comment-age">(06 Mar '14, 00:15)</span> hunghoong</div></div></div><div id="comment-tools-30432" class="comment-tools"></div><div class="clear"></div><div id="comment-30432-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

