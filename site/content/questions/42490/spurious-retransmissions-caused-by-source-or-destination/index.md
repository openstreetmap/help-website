+++
type = "question"
title = "Spurious retransmissions, caused by source or destination?"
description = '''We&#x27;ve got an external appliation which connects to a virtual IP on our firewall (port 80). The virtual IP is relayed to one of our internal servers. The external application was recently moved to new servers (production and test environment) so we had to make some adjustments in our firewall to acco...'''
date = "2015-05-18T02:47:00Z"
lastmod = "2015-05-20T04:59:00Z"
weight = 42490
keywords = [ "spurious", "retransmissions" ]
aliases = [ "/questions/42490" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Spurious retransmissions, caused by source or destination?](/questions/42490/spurious-retransmissions-caused-by-source-or-destination)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42490-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We've got an external appliation which connects to a virtual IP on our firewall (port 80). The virtual IP is relayed to one of our internal servers.</p><p>The external application was recently moved to new servers (production and test environment) so we had to make some adjustments in our firewall to accommodate the new source IP's. For the production environment, everything is working great but for the test environment it isn't. As far as I can tell, the firewall rules are correct and even if we connect the test environment of the external system to the virtual IP of our production server, it still doesn't work.</p><p>When we try to connect the test environment, the only thing I can see in Wireshark on our internal server is a TCP Spurious Retransmission comming in, followed by a TCP Previous Segment not captured going out and finally, TCP ACKed unseen segment comming in. I do know a little bit about networking trafic, but this goes beyond my knowledge.</p><p>I understand that it's impossible to pinpoint exactly what is going on by this post, but it would be great if someone could tell me which server is most likely causing this, the external server or our internal server? Any suggestions are more than welcome!</p><p>Thanks in advance, Arnold</p></div><div id="question-tags" class="tags-container tags">spurious retransmissions</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 May '15, 02:47</strong></p><img src="https://secure.gravatar.com/avatar/ccdc399e2ef24724f858b3d1f0e5c730?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Arnold71&#39;s gravatar image" /><p>Arnold71<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Arnold71 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 18 May '15, 04:51</p></div></div><div id="comments-container-42490" class="comments-container"><span id="42491"></span><div id="comment-42491" class="comment"><div id="post-42491-score" class="comment-score"></div><div class="comment-text"><p>Can you upload a capture file? It's much easier to see what is going on that way - if you need to, sanitize it with TraceWrangler first, then put it on Cloudshark and post the link.</p></div><div id="comment-42491-info" class="comment-info"><span class="comment-age">(18 May '15, 02:53)</span> Jasper ♦♦</div></div><span id="42492"></span><div id="comment-42492" class="comment"><div id="post-42492-score" class="comment-score"></div><div class="comment-text"><p>Without a Trace I think it is not possible to tell you a lot.</p><p>But about the meanings of Spurious Retransmissions you can have a look here: <a href="https://blog.packet-foo.com/2013/06/spurious-retransmissions/">https://blog.packet-foo.com/2013/06/spurious-retransmissions/</a></p><p>And out of your description, it sounds a little bit, that some packets go another way through the network!? But it is just a feeling. So again without a trace it is not possible to tell you some hard facts.</p><p>You coul upload a trace at dropbox, cloudshark or somerwhere else, so somebody can help you further?</p></div><div id="comment-42492-info" class="comment-info"><span class="comment-age">(18 May '15, 02:56)</span> Christian_R</div></div><span id="42493"></span><div id="comment-42493" class="comment"><div id="post-42493-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your fast responses! Ofcourse, you are both totally right about the capture file. I didn't have the file from our last test at hand, so I tried to post this anyway. ;)</p><p>I will organise a new test and post the result here. I read the blog post and it did clarify a lot for me! The only thing I couldn't figure out was if packets actually do get lost or not.</p><p>Anyway, I will get back to you with more information. Thanks again for responing!</p></div><div id="comment-42493-info" class="comment-info"><span class="comment-age">(18 May '15, 03:09)</span> Arnold71</div></div></div><div id="comment-tools-42490" class="comment-tools"></div><div class="clear"></div><div id="comment-42490-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="42576"></span>

<div id="answer-container-42576" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42576-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Further testing revealed a configuration error, somewhere between the external and internal server. Not sure what it was, but the access provider resolved it so this question can be closed. Thank you very much for offering your help!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 May '15, 04:59</strong></p><img src="https://secure.gravatar.com/avatar/ccdc399e2ef24724f858b3d1f0e5c730?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Arnold71&#39;s gravatar image" /><p>Arnold71<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Arnold71 has no accepted answers">0%</span></p></div></div><div id="comments-container-42576" class="comments-container"></div><div id="comment-tools-42576" class="comment-tools"></div><div class="clear"></div><div id="comment-42576-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

