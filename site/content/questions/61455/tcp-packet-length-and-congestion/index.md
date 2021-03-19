+++
type = "question"
title = "TCP packet length and congestion"
description = '''If we capture packets using tcpdump or Wireshark with a length less than the MTU (length &amp;lt; 1500) -(For example, 74, 108, 788... etc) - is it fair to say that it means there is tcp congestion?'''
date = "2017-05-17T04:45:00Z"
lastmod = "2017-05-17T04:50:00Z"
weight = 61455
keywords = [ "packetloss", "length", "congestion", "tcp", "wireshark" ]
aliases = [ "/questions/61455" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [TCP packet length and congestion](/questions/61455/tcp-packet-length-and-congestion)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61455-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>If we capture packets using tcpdump or Wireshark with a length less than the MTU (length &lt; 1500) -(For example, 74, 108, 788... etc) - is it fair to say that it means there is tcp congestion?</p></div><div id="question-tags" class="tags-container tags">packetloss length congestion tcp wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 May '17, 04:45</strong></p><img src="https://secure.gravatar.com/avatar/6dd3e71b974fad46455a71063cb9c319?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="armodes&#39;s gravatar image" /><p>armodes<br />
<span class="score" title="16 reputation points">16</span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="19 badges"><span class="silver">●</span><span class="badgecount">19</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="armodes has no accepted answers">0%</span></p></div></div><div id="comments-container-61455" class="comments-container"></div><div id="comment-tools-61455" class="comment-tools"></div><div class="clear"></div><div id="comment-61455-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61456"></span>

<div id="answer-container-61456" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61456-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>No. That may only be something to think about if you know that there is a big data transfer with such a volume that all packets can be filled completely up to MSS. If an application has only a few bytes to send it will do that, and it's not because of congestion.</p><p>Take SSH/Telnet for example: pressing a key will send a small packet containing that key (and a few other things), but it's simply a small packet, and not congestion.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 May '17, 04:50</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-61456" class="comments-container"><span id="61457"></span><div id="comment-61457" class="comment"><div id="post-61457-score" class="comment-score"></div><div class="comment-text"><p>OK thank you Jasper. I am using iperf to send a traffic and i was wondering about it.</p></div><div id="comment-61457-info" class="comment-info"><span class="comment-age">(17 May '17, 05:14)</span> armodes</div></div></div><div id="comment-tools-61456" class="comment-tools"></div><div class="clear"></div><div id="comment-61456-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

