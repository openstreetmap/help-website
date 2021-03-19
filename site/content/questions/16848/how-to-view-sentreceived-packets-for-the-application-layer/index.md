+++
type = "question"
title = "How to view sent/received packets for the application layer?"
description = '''Hello everyone  I have a school project that i&#x27;m working on, and some of the questions are to:  Show the number of packets sent and received for each application layer.  Can anyone please assist me with this.  Thanks in advance '''
date = "2012-12-13T13:56:00Z"
lastmod = "2012-12-14T07:26:00Z"
weight = 16848
keywords = [ "application", "layer", "packets" ]
aliases = [ "/questions/16848" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to view sent/received packets for the application layer?](/questions/16848/how-to-view-sentreceived-packets-for-the-application-layer)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16848-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello everyone</p><p>I have a school project that i'm working on, and some of the questions are to: Show the number of packets sent and received for each application layer. Can anyone please assist me with this.</p><p>Thanks in advance</p></div><div id="question-tags" class="tags-container tags">application layer packets</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Dec '12, 13:56</strong></p><img src="https://secure.gravatar.com/avatar/1225dd685cae2e4eeb47c9556eff83fe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ahad917&#39;s gravatar image" /><p>ahad917<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ahad917 has no accepted answers">0%</span></p></div></div><div id="comments-container-16848" class="comments-container"></div><div id="comment-tools-16848" class="comment-tools"></div><div class="clear"></div><div id="comment-16848-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="16850"></span>

<div id="answer-container-16850" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16850-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Take a look at the Statistics/Protocol Hierarchy menu option, you might want to filter from there to gather what you need if the statistics in itself aren't enough.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Dec '12, 14:26</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-16850" class="comments-container"><span id="16856"></span><div id="comment-16856" class="comment"><div id="post-16856-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the reply Jasper,</p><p>Do you have any idea on which of the packets are sent and which are received?</p></div><div id="comment-16856-info" class="comment-info"><span class="comment-age">(13 Dec '12, 17:14)</span> ahad917</div></div></div><div id="comment-tools-16850" class="comment-tools"></div><div class="clear"></div><div id="comment-16850-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="16884"></span>

<div id="answer-container-16884" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16884-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Take a look at</p><blockquote><p><code>Statistics -&gt; Conversations</code><br />
</p></blockquote><p>You will get a list of the different protocol layers and some information about the number of packets/bytes and the direction.</p><p>Regarding your question:</p><blockquote><p><code>which packets are sent and which are received</code><br />
</p></blockquote><p>There is no direction associated with an IP packet, as both the client and the server send <strong>and</strong> receive packets. So you can't answer that question unless you specify the context. So, if you say:</p><blockquote><p><code>which packets are sent by the client</code><br />
</p></blockquote><p>You will have to look at all packets where the client IP is the source IP.</p><blockquote><p><code>which packets are received by the client</code><br />
</p></blockquote><p>You will have to look at all packets where the client IP is the destination IP.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Dec '12, 07:26</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-16884" class="comments-container"></div><div id="comment-tools-16884" class="comment-tools"></div><div class="clear"></div><div id="comment-16884-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

