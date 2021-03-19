+++
type = "question"
title = "How to Packet capture in TCP Offload engines?"
description = '''I am working on TCP Offload engine(for Iscsi). I am looking a way to capture those offloaded(to the chip) packets(TCP and Iscsi) with wireshark. My colleagues are saying that only 3rd party test equipment is the alternative(which sits in between iscsi initiator and iscsi target) for looking in to pa...'''
date = "2013-04-09T15:54:00Z"
lastmod = "2013-04-09T16:01:00Z"
weight = 20254
keywords = [ "iscsi", "tcpoffload" ]
aliases = [ "/questions/20254" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How to Packet capture in TCP Offload engines?](/questions/20254/how-to-packet-capture-in-tcp-offload-engines)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20254-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am working on TCP Offload engine(for Iscsi). I am looking a way to capture those offloaded(to the chip) packets(TCP and Iscsi) with wireshark. My colleagues are saying that only 3rd party test equipment is the alternative(which sits in between iscsi initiator and iscsi target) for looking in to packets. I want to double confirm with experts here.Thanks.</p></div><div id="question-tags" class="tags-container tags">iscsi tcpoffload</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Apr '13, 15:54</strong></p><img src="https://secure.gravatar.com/avatar/2b038237e64839261fcc88e9fdef2b68?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="krishnayeddula&#39;s gravatar image" /><p>krishnayeddula<br />
<span class="score" title="629 reputation points">629</span><span title="35 badges"><span class="badge1">●</span><span class="badgecount">35</span></span><span title="41 badges"><span class="silver">●</span><span class="badgecount">41</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="krishnayeddula has 3 accepted answers">6%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 Apr '13, 15:54</p></div></div><div id="comments-container-20254" class="comments-container"></div><div id="comment-tools-20254" class="comment-tools"></div><div class="clear"></div><div id="comment-20254-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="20255"></span>

<div id="answer-container-20255" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20255-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you want to see the real packets that actually were transferred on the network you need a device in the middle, or at least not on sender or receiver. You can't trust what you see on the sending PC.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Apr '13, 16:01</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 Apr '13, 16:02</p></div></div><div id="comments-container-20255" class="comments-container"><span id="20256"></span><div id="comment-20256" class="comment"><div id="post-20256-score" class="comment-score"></div><div class="comment-text"><p>In my case both target and initiator are connected b2b.I am not worrying about the trust but a way to capture in this scenario(Where packets are offloaded to iscsi enabled chip).</p></div><div id="comment-20256-info" class="comment-info"><span class="comment-age">(09 Apr '13, 16:09)</span> krishnayeddula</div></div><span id="20276"></span><div id="comment-20276" class="comment"><div id="post-20276-score" class="comment-score">1</div><div class="comment-text"><p>By 'you can't trust' @Jasper meant: You (probably) can't capture offloaded packets. As you will never know for sure which packets will be offloaded, you can't trust any capture result on any of the involved machines. As he (and you colleagues) said: Capture the line with a TAP or a mirror port of a switch.</p></div><div id="comment-20276-info" class="comment-info"><span class="comment-age">(10 Apr '13, 05:43)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-20255" class="comment-tools"></div><div class="clear"></div><div id="comment-20255-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

