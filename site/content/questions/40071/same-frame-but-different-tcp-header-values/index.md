+++
type = "question"
title = "Same Frame but Different TCP Header Values"
description = '''Hi, I am using wireshark installed on a windows host with 2 nic. The first one is attached to the source L2 switch (where the Web Server is connected) and the other one is attached to the destination L2 switch (where the Client is connected). I&#x27;m trying to follow packets from source to destination i...'''
date = "2015-02-25T08:34:00Z"
lastmod = "2015-02-25T15:34:00Z"
weight = 40071
keywords = [ "sequencenumber", "seq" ]
aliases = [ "/questions/40071" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Same Frame but Different TCP Header Values](/questions/40071/same-frame-but-different-tcp-header-values)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40071-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I am using wireshark installed on a windows host with 2 nic. The first one is attached to the source L2 switch (where the Web Server is connected) and the other one is attached to the destination L2 switch (where the Client is connected). I'm trying to follow packets from source to destination in order to find out if any delay is present. The odd thing is that the a packet sniffed from the source L2 switch have a different sequence number and a different ack number if it is sniffed from the destination L2 switch. I am sure that I'm seeing the same packet by checking its size and the timestamp for a given timelapse.The protocol is SSL over TCP port 1981. It is a custom web service. Can anyone explain why this is happening? Thank you</p></div><div id="question-tags" class="tags-container tags">sequencenumber seq</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Feb '15, 08:34</strong></p><img src="https://secure.gravatar.com/avatar/9083cb198c38416e91d9d8a9cca77bfb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="badenia1&#39;s gravatar image" /><p>badenia1<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="badenia1 has no accepted answers">0%</span></p></div></div><div id="comments-container-40071" class="comments-container"></div><div id="comment-tools-40071" class="comment-tools"></div><div class="clear"></div><div id="comment-40071-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="40076"></span>

<div id="answer-container-40076" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40076-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>There's one universal rule, and that is that a packet must have the same sequence and ack number, no matter WHERE you capture it. Sequence and ack number cannot change on the way. The only thing that could fool Wireshark into showing two different sequence/ack numbers is when you use relative numbers. So please verify that you are looking at absolute sequence and ack numbers (there's a setting for this in the TCP dissector preferences).</p><p>If the absolute sequence/ack nubers are different, it's NOT the same packet. It does not matter if size or timestamp may be seemingly correct if those two aren't the same. So please use absolute numbers and check your findings again.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Feb '15, 15:34</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 Feb '15, 00:52</p></div></div><div id="comments-container-40076" class="comments-container"><span id="40080"></span><div id="comment-40080" class="comment"><div id="post-40080-score" class="comment-score"></div><div class="comment-text"><p>You are right man! Changing TCP dissector preferences made my data reliable, and the packets now have the same tcp header values across my whole LAN. Great answer! Thanks</p></div><div id="comment-40080-info" class="comment-info"><span class="comment-age">(26 Feb '15, 00:47)</span> badenia1</div></div><span id="40081"></span><div id="comment-40081" class="comment"><div id="post-40081-score" class="comment-score"></div><div class="comment-text"><p>You're welcome :)</p></div><div id="comment-40081-info" class="comment-info"><span class="comment-age">(26 Feb '15, 00:53)</span> Jasper ♦♦</div></div></div><div id="comment-tools-40076" class="comment-tools"></div><div class="clear"></div><div id="comment-40076-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

