+++
type = "question"
title = "Out of order: tcp re-ordering already executed?"
description = '''It&#x27;s suppossed that the TCP layer should re-order the packets correctly before it passes to the application layer. In the capture we get with tcpdump and then analysed with wireshark, are there any re-ordering involved already? I&#x27;m trying to understand if the data we capture is already processed by ...'''
date = "2014-04-01T09:14:00Z"
lastmod = "2014-04-01T09:22:00Z"
weight = 31353
keywords = [ "tcpdump", "out-of-order", "wireshark" ]
aliases = [ "/questions/31353" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Out of order: tcp re-ordering already executed?](/questions/31353/out-of-order-tcp-re-ordering-already-executed)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31353-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>It's suppossed that the TCP layer should re-order the packets correctly before it passes to the application layer. In the capture we get with tcpdump and then analysed with wireshark, are there any re-ordering involved already?</p><p>I'm trying to understand if the data we capture is already processed by the tcp layer or not.</p><p>Thanks!</p></div><div id="question-tags" class="tags-container tags">tcpdump out-of-order wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Apr '14, 09:14</strong></p><img src="https://secure.gravatar.com/avatar/3a3c901a8719769ab2385d6e78c8a26e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdisSolar&#39;s gravatar image" /><p>EdisSolar<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdisSolar has no accepted answers">0%</span></p></div></div><div id="comments-container-31353" class="comments-container"></div><div id="comment-tools-31353" class="comment-tools"></div><div class="clear"></div><div id="comment-31353-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="31355"></span>

<div id="answer-container-31355" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31355-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>No, Wireshark does not reorder packets, it shows the packets in the order they arrived at the capture device (which may or may not be the same as on the stack of the actual receiver).</p><p>The only thing that may fool you is the fact that Wireshark sometimes changes the info column when "Allow Subdisectors to reassemble TCP streams" is enabled (which it is by default). You can turn that feature of in the TCP settings in the preferences dialog under "Protocols".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Apr '14, 09:22</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-31355" class="comments-container"></div><div id="comment-tools-31355" class="comment-tools"></div><div class="clear"></div><div id="comment-31355-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

