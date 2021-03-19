+++
type = "question"
title = "ACK after PSH,ACK from same source."
description = ''' While capturing the pcap,i had found some issue like, same source sends PSH,ACK and ACK.Below is the attached screen shot.Is it possible like that.'''
date = "2017-08-01T04:21:00Z"
lastmod = "2017-08-01T04:36:00Z"
weight = 63282
keywords = [ "tcppackets", "packets", "wireshark" ]
aliases = [ "/questions/63282" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [ACK after PSH,ACK from same source.](/questions/63282/ack-after-pshack-from-same-source)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63282-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p><img src="https://osqa-ask.wireshark.org/upfiles/issue_9IkTJn3.png" alt="alt text" /></p><p>While capturing the pcap,i had found some issue like, same source sends PSH,ACK and ACK.Below is the attached screen shot.Is it possible like that.</p></div><div id="question-tags" class="tags-container tags">tcppackets packets wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Aug '17, 04:21</strong></p><img src="https://secure.gravatar.com/avatar/d4bb245da94fc58e60cb3b1ba99589a2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kodamagulla_kalyan&#39;s gravatar image" /><p>kodamagulla_...<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kodamagulla_kalyan has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 01 Aug '17, 04:22</p></div></div><div id="comments-container-63282" class="comments-container"></div><div id="comment-tools-63282" class="comment-tools"></div><div class="clear"></div><div id="comment-63282-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="63283"></span>

<div id="answer-container-63283" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63283-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Sure, that's possible. PSH/ACK just means "this is something the receiver can process right away" - it doesn't mean that there can't be more following it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Aug '17, 04:36</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-63283" class="comments-container"><span id="63284"></span><div id="comment-63284" class="comment"><div id="post-63284-score" class="comment-score"></div><div class="comment-text"><p>Can you please elabrate below q.</p><p>Say in PSH,ACK from x to y seq = 7732 ack =1 len =831. immediate ACK from x to y seq = 8563( 7732 + 831) ack =1 len = 1448 happens.</p><p>So why it has to send again ACK with adding seq with len ? I was assuming this has to be done by the reciever end.</p><p>-Thanks</p></div><div id="comment-63284-info" class="comment-info"><span class="comment-age">(01 Aug '17, 04:49)</span> kodamagulla_...</div></div><span id="63285"></span><div id="comment-63285" class="comment"><div id="post-63285-score" class="comment-score"></div><div class="comment-text"><p>ACK is only increased by the receiver if TCP payload bytes (len value) arrived successfully. If x sends two packets in a row, ACK must not change because nothing was received from y in the meantime.</p></div><div id="comment-63285-info" class="comment-info"><span class="comment-age">(01 Aug '17, 04:55)</span> Jasper ♦♦</div></div></div><div id="comment-tools-63283" class="comment-tools"></div><div class="clear"></div><div id="comment-63283-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

