+++
type = "question"
title = "What filter can I use to exclude TCP retransmissions"
description = '''Hi All, I am using tshark to analyze data from a pcap file, i want to exclude all the tcp retransmission packets, is there any filter to exclude them(i don&#x27;t want them in my data) and with which field i should use that filter in my tshark.  Any help would be highly appreciated. Thank you'''
date = "2017-04-19T12:50:00Z"
lastmod = "2017-04-20T06:26:00Z"
weight = 60900
keywords = [ "filter", "retransmissions", "tcp" ]
aliases = [ "/questions/60900" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [What filter can I use to exclude TCP retransmissions](/questions/60900/what-filter-can-i-use-to-exclude-tcp-retransmissions)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60900-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All,</p><p>I am using tshark to analyze data from a pcap file, i want to exclude all the tcp retransmission packets, is there any filter to exclude them(i don't want them in my data) and with which field i should use that filter in my tshark.</p><p>Any help would be highly appreciated.</p><p>Thank you</p></div><div id="question-tags" class="tags-container tags">filter retransmissions tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Apr '17, 12:50</strong></p><img src="https://secure.gravatar.com/avatar/3c5efc7cfe5ef8e05bd2f756df40afa3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sreenu19&#39;s gravatar image" /><p>sreenu19<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sreenu19 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>converted to question 20 Apr '17, 00:30</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-60900" class="comments-container"><span id="60906"></span><div id="comment-60906" class="comment"><div id="post-60906-score" class="comment-score"></div><div class="comment-text"><p>Your "answer" has been converted to a question as that's how this site works. Please read the FAQ for more information.</p></div><div id="comment-60906-info" class="comment-info"><span class="comment-age">(20 Apr '17, 00:31)</span> grahamb ♦</div></div></div><div id="comment-tools-60900" class="comment-tools"></div><div class="clear"></div><div id="comment-60900-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="60921"></span>

<div id="answer-container-60921" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60921-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>First you need to ensure that the TCP preference <code>Analyze TCP sequence numbers</code> is enabled.</p><p>Then you can find TCP retransmissions using the field <code>tcp.analysis.retransmission</code>. Obviously to filter them out use <code>!tcp.analysis.retransmission</code>.</p><p>You may also be interested in the TCP preference <code>Do not call subdissectors for error packets</code>: when enabled upper-level protocol dissectors (like HTTP) aren't called for TCP retransmissions (and other "errors").</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Apr '17, 06:26</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-60921" class="comments-container"></div><div id="comment-tools-60921" class="comment-tools"></div><div class="clear"></div><div id="comment-60921-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

