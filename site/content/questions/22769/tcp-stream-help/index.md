+++
type = "question"
title = "tcp stream help"
description = '''Can anyone help me with this TCP steam/capture? End result is the client using faxfinder can&#x27;t connect to the server. thanks in advance http://img547.imageshack.us/img547/6901/m3o.png'''
date = "2013-07-09T15:04:00Z"
lastmod = "2013-07-10T01:19:00Z"
weight = 22769
keywords = [ "faxfinder", "stream", "tcp", "wireshark" ]
aliases = [ "/questions/22769" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [tcp stream help](/questions/22769/tcp-stream-help)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22769-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Can anyone help me with this TCP steam/capture? End result is the client using faxfinder can't connect to the server.</p><p>thanks in advance</p><p><a href="http://img547.imageshack.us/img547/6901/m3o.png">http://img547.imageshack.us/img547/6901/m3o.png</a></p></div><div id="question-tags" class="tags-container tags">faxfinder stream tcp wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Jul '13, 15:04</strong></p><img src="https://secure.gravatar.com/avatar/61594ee1758f827f387d0468ef2f0067?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wireuser70&#39;s gravatar image" /><p>wireuser70<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wireuser70 has no accepted answers">0%</span></p></div></div><div id="comments-container-22769" class="comments-container"><span id="22826"></span><div id="comment-22826" class="comment"><div id="post-22826-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the prompt replies. I have even more information to share. I ran wireshark captures on the port going to the client on the same switch but I don't see any of the [syn, ack] from the server. Its like the packets are getting lost in the switch.</p></div><div id="comment-22826-info" class="comment-info"><span class="comment-age">(10 Jul '13, 13:09)</span> wireuser70</div></div><span id="22828"></span><div id="comment-22828" class="comment"><div id="post-22828-score" class="comment-score"></div><div class="comment-text"><p>NVM!!!! traffic was leaving a different port on the switch. :P</p></div><div id="comment-22828-info" class="comment-info"><span class="comment-age">(10 Jul '13, 15:56)</span> wireuser70</div></div></div><div id="comment-tools-22769" class="comment-tools"></div><div class="clear"></div><div id="comment-22769-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="22773"></span>

<div id="answer-container-22773" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22773-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>That's an interesting trace. Looks like the client sends a SYN to the server, gets a SYN/ACK back, but instead of finalizing the three way handshake the client aborts with a reset. I have seen something like this before, when the timeout setting for the connection was so short that the client gave up before the SYN/ACK arrived - which meant that the port was already closed when it "finally" came in, resulting in a reset. In your case the timing is relatively fast, so this looks pretty strange.</p><p>I guess you captured at the server (from the name in the title bar) - what you need to do is capture at the client to see what it sees. Maybe the client is innocent and a device between client and server is misbehaving. Capture at the client and the server at the same time, and compare the session handshake between both captures. You should be able to see any difference - but if there isn't any (meaning, you see the exact same SYN - SYN/ACK - RST sequence at the client) your client software is faulty.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Jul '13, 16:44</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 Jul '13, 16:45</p></div></div><div id="comments-container-22773" class="comments-container"></div><div id="comment-tools-22773" class="comment-tools"></div><div class="clear"></div><div id="comment-22773-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="22788"></span>

<div id="answer-container-22788" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22788-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>If there any Firewall or Loadbalancer involved? If so, it may cause the RST packet due to security restrictions. Did you see any ICMP packets in the capture file, like "administratively prohibited"? If so, that would be another sign for a problem with an intermediate system and not client and/or server.</p><p>If neither of the above is true in your environment (which I believe, because of the time deltas between the packets):</p><p>As @Jasper suggested. Please capture at the client and at the server and compare the capture files to figure out who actually sends the RST packet. If possible post the capture file somewhere (google docs, dropbox, etc.), so we can have a look as well.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Jul '13, 01:19</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-22788" class="comments-container"></div><div id="comment-tools-22788" class="comment-tools"></div><div class="clear"></div><div id="comment-22788-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

