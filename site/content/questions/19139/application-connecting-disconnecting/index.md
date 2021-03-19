+++
type = "question"
title = "Application Connecting/ Disconnecting"
description = '''Hello I have two Windows 2008 Servers that function as a client/server application. ServerA is the client ServerB is the server ServerA needs to connect to ServerB, however keeps reporting frequent Disconnections in the Application log. I ran continous ping from ServerA to ServerB which was fine. Th...'''
date = "2013-03-04T16:57:00Z"
lastmod = "2013-03-05T10:40:00Z"
weight = 19139
keywords = [ "disconnect", "troubleshooting" ]
aliases = [ "/questions/19139" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Application Connecting/ Disconnecting](/questions/19139/application-connecting-disconnecting)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19139-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello</p><p>I have two Windows 2008 Servers that function as a client/server application.</p><p>ServerA is the client ServerB is the server</p><p>ServerA needs to connect to ServerB, however keeps reporting frequent Disconnections in the Application log. I ran continous ping from ServerA to ServerB which was fine. The latency was ok too.</p><p>I figure the next step is to launch WS for more detailed info, but could anyone give me any pointers on what I'm looking for? (I realise the question is a bit vague!)</p></div><div id="question-tags" class="tags-container tags">disconnect troubleshooting</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Mar '13, 16:57</strong></p><img src="https://secure.gravatar.com/avatar/01e83725a9ab911ceacb32eb9dcde317?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TonyRobbins1978&#39;s gravatar image" /><p>TonyRobbins1978<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TonyRobbins1978 has no accepted answers">0%</span></p></div></div><div id="comments-container-19139" class="comments-container"></div><div id="comment-tools-19139" class="comment-tools"></div><div class="clear"></div><div id="comment-19139-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="19158"></span>

<div id="answer-container-19158" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19158-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>but could anyone give me any pointers on what I'm looking for?</p></blockquote><p>I would do it this way.</p><ul><li>get a PC that is able to run Wireshark</li><li>if you don't have a separate PC, the second best option is to run Wireshark on both servers in parallel. The third best option is to run Wireshark on one of the servers.</li><li>capture data and wait until the server reports those 'frequent disconnects' in its log.</li><li>stop Wireshark</li><li>Take the timestamp from the log and look at the captured data in that time window (+/- a few seconds/minutes)</li><li>"Disconnects", as reported by the application may have several reasons. Start to look for TCP RESETS and closed connections (FIN) in Wireshark.</li></ul><blockquote><p>(I realise the question is a bit vague!)</p></blockquote><ul><li>it's hard to tell you what to look for, if we know nothing about the application, the protocol, etc. Can you add some more details about the communication (HTTP, HTTPS, own protocol, TCP/UDP, etc.)</li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Mar '13, 10:40</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-19158" class="comments-container"><span id="19165"></span><div id="comment-19165" class="comment"><div id="post-19165-score" class="comment-score"></div><div class="comment-text"><p>Thank you for taking the time to answer. I can certainly run WS on both servers, that won't be an issue. The application speaks on its own port (lets say port 4000). Am I correct in saying that I run the trace and wait for the disconnects then filter on the IP addresses or port number? I had a test run when I saw the errors and don't see any RSETS but I do see FIN, ACK packets. Is this the same as a FIN, i.e the first FIN, ACK I see is the from the server requesting the closure? Second question, is there anything in the traces, apart from the time, that I can use to identify the same packets</p></div><div id="comment-19165-info" class="comment-info"><span class="comment-age">(05 Mar '13, 11:25)</span> TonyRobbins1978</div></div><span id="19167"></span><div id="comment-19167" class="comment"><div id="post-19167-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Am I correct in saying that I run the trace and wait for the disconnects then filter on the IP addresses or port number?</p></blockquote><p>well, filtering on the IP address and the port should go into the capture filter to limit the amount of data you record (<a href="http://wiki.wireshark.org/CaptureFilters).">http://wiki.wireshark.org/CaptureFilters).</a></p><p>After you see the messages in the application log, stop Wireshark. Take the timestamp from the application log error message and look 'around' that time within the Wireshark trace, if you see anything 'unusual' (whatever that may be for your specific protocol).</p><blockquote><p>Is this the same as a FIN, i.e the first FIN, ACK I see is the from the server requesting the closure?</p></blockquote><p>FIN and FIN, ACK are both part of the connection tear down and you will see that frequently for TCP connections, <strong>expect</strong> your protocol relies on a long lived TCP connection. So it may or may not indicate a problem if you see FIN packets.</p><blockquote><p>Second question, is there anything in the traces, apart from the time, that I can use to identify the same packets</p></blockquote><p>Without any knowledge about the protocol? None that I know of.</p></div><div id="comment-19167-info" class="comment-info"><span class="comment-age">(05 Mar '13, 11:36)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-19158" class="comment-tools"></div><div class="clear"></div><div id="comment-19158-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

