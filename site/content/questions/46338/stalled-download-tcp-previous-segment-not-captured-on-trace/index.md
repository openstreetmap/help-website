+++
type = "question"
title = "Stalled download (TCP Previous segment not captured on trace)"
description = '''Hi, I&#x27;m having a tough time debugging a network issue. I&#x27;m downloading some files through HTTP/1.1 and, sometimes, i get stalled downloads after the client downloads some Kb. I think that the server persistent connections logic is somehow buggy but it could also be caused by the client or how i am u...'''
date = "2015-10-02T06:42:00Z"
lastmod = "2015-10-05T14:20:00Z"
weight = 46338
keywords = [ "stall", "http", "persistent" ]
aliases = [ "/questions/46338" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Stalled download (TCP Previous segment not captured on trace)](/questions/46338/stalled-download-tcp-previous-segment-not-captured-on-trace)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46338-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I'm having a tough time debugging a network issue. I'm downloading some files through HTTP/1.1 and, sometimes, i get stalled downloads after the client downloads some Kb.</p><p>I think that the server persistent connections logic is somehow buggy but it could also be caused by the client or how i am using it. However, i suspect it is a server issue because i don't get these problems with other servers but i get them with several clients (Erlang HTTP clients). Unfortunately i can't know which software is ran by the server.</p><p>In the attached capture i can see a connection (tcp.stream eq 3) that shows some errors until the client finally times out and closes it (first tried with FIN, then with RST).</p><p><a href="https://www.cloudshark.org/captures/224e9e432f4c">https://www.cloudshark.org/captures/224e9e432f4c</a></p><p>What do these "TCP Previous segment not captured", retransmission and duplicated packets mean? What is happening? Can i blame the server?</p><p>PD: I have truncated the capture, both in number of packets (deleted pakcets after client RST) and in packet size (200 bytes) in order to upload it</p></div><div id="question-tags" class="tags-container tags">stall http persistent</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Oct '15, 06:42</strong></p><img src="https://secure.gravatar.com/avatar/9b3c18c938a856ca17492f04d22dda3b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alexvf&#39;s gravatar image" /><p>alexvf<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alexvf has no accepted answers">0%</span></p></div></div><div id="comments-container-46338" class="comments-container"></div><div id="comment-tools-46338" class="comment-tools"></div><div class="clear"></div><div id="comment-46338-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="46370"></span>

<div id="answer-container-46370" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46370-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>"What do these "TCP Previous segment not captured", retransmission and duplicated packets mean?"<br />
This is an indication of packet loss. If only this server is having the problem then the packet loss occurs close to this server.<br />
The client is giving up after more than 14 seconds.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Oct '15, 14:20</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p>mrEEde<br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></br></p></div></div><div id="comments-container-46370" class="comments-container"><span id="46374"></span><div id="comment-46374" class="comment"><div id="post-46374-score" class="comment-score"></div><div class="comment-text"><p>Is it compatible with the server dropping the connection (maybe a firewall DROP?) I would assume that if it were not by the packets arriving from server near the end of capture @ 21.99 ...</p></div><div id="comment-46374-info" class="comment-info"><span class="comment-age">(06 Oct '15, 01:46)</span> alexvf</div></div><span id="46380"></span><div id="comment-46380" class="comment"><div id="post-46380-score" class="comment-score"></div><div class="comment-text"><p>The server is retransmitting with a very high RTO of more than 10s as seen at the client.</p><p>This indicates that also the retransmitted packets were dropped somewhere for a yet to be identified reason.</p><p>Neither the server nor a FW is dropping the connection though as it is the client that is sending a FIN to terminate</p></div><div id="comment-46380-info" class="comment-info"><span class="comment-age">(06 Oct '15, 06:40)</span> mrEEde</div></div><span id="46383"></span><div id="comment-46383" class="comment"><div id="post-46383-score" class="comment-score"></div><div class="comment-text"><p>Thank you for the responses, mrEEde.</p><p>Yes, the client times out and closes the connection if it does not get X bytes in Y seconds (currently X = 100 Kb, Y = 15 s), which is enforced due to client application requirements. When the problem occurs, it usually downloads 30-70 Kb in those 15 seconds.</p><p>So i can only guess that both the client and the server are behaving right and someone in the middle is delaying the communication.</p><p>As i said, the client is under my control up to some limit but i know nothing about the server, let alone about the network. In this scenario, i would appreciate any advice that helps me debugging the problem.</p></div><div id="comment-46383-info" class="comment-info"><span class="comment-age">(06 Oct '15, 11:24)</span> alexvf</div></div><span id="46400"></span><div id="comment-46400" class="comment"><div id="post-46400-score" class="comment-score"></div><div class="comment-text"><p>Unless you have access to somebody willing to support you at the server side you're pretty much at the end of your analysis. The problem is packet loss close to the server side that is causing timer based retransmissions which are delaying the TCP connection.</p></div><div id="comment-46400-info" class="comment-info"><span class="comment-age">(07 Oct '15, 08:21)</span> mrEEde</div></div></div><div id="comment-tools-46370" class="comment-tools"></div><div class="clear"></div><div id="comment-46370-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

