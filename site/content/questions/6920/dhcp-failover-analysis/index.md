+++
type = "question"
title = "dhcp failover analysis"
description = '''Greetings, I found this http://anonsvn.wireshark.org/wireshark/trunk/epan/dissectors/packet-dhcp-failover.c But I don&#x27;t know what to do with it. I&#x27;m assuming that I might have to compile my own Wireshark with that included, could someone point me in the right direction?'''
date = "2011-10-17T06:32:00Z"
lastmod = "2011-10-17T06:57:00Z"
weight = 6920
keywords = [ "failover", "dhcpd" ]
aliases = [ "/questions/6920" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [dhcp failover analysis](/questions/6920/dhcp-failover-analysis)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6920-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Greetings,</p><p>I found this http://anonsvn.wireshark.org/wireshark/trunk/epan/dissectors/packet-dhcp-failover.c</p><p>But I don't know what to do with it. I'm assuming that I might have to compile my own Wireshark with that included, could someone point me in the right direction?</p></div><div id="question-tags" class="tags-container tags">failover dhcpd</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Oct '11, 06:32</strong></p><img src="https://secure.gravatar.com/avatar/ee78e47ef06a4f65ddbbfb83e8cef9ee?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dtdionne&#39;s gravatar image" /><p>dtdionne<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dtdionne has no accepted answers">0%</span></p></div></div><div id="comments-container-6920" class="comments-container"><span id="6921"></span><div id="comment-6921" class="comment"><div id="post-6921-score" class="comment-score"></div><div class="comment-text"><p>What is you want to do ?</p><p>The dhcp-failover dissector is included in Wireshark and has been for quite some time.</p></div><div id="comment-6921-info" class="comment-info"><span class="comment-age">(17 Oct '11, 06:53)</span> Bill Meier ♦♦</div></div><span id="6922"></span><div id="comment-6922" class="comment"><div id="post-6922-score" class="comment-score"></div><div class="comment-text"><p>Actually, I just took a look at the source tree and that dissector is there. So the question is, why isn't wireshark disecting my failover traffic?</p></div><div id="comment-6922-info" class="comment-info"><span class="comment-age">(17 Oct '11, 06:53)</span> dtdionne</div></div></div><div id="comment-tools-6920" class="comment-tools"></div><div class="clear"></div><div id="comment-6920-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6923"></span>

<div id="answer-container-6923" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6923-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wow, im amazingly akward...here's what I did:</p><p>Click "Analyze" &gt; "Decode as..." &gt; "Transport" &gt; "DHCPFO"</p><p>Wireshark 1.6.2 r.38931 Win64</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Oct '11, 06:57</strong></p><img src="https://secure.gravatar.com/avatar/ee78e47ef06a4f65ddbbfb83e8cef9ee?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dtdionne&#39;s gravatar image" /><p>dtdionne<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dtdionne has no accepted answers">0%</span></p></div></div><div id="comments-container-6923" class="comments-container"><span id="6925"></span><div id="comment-6925" class="comment"><div id="post-6925-score" class="comment-score"></div><div class="comment-text"><p>Alternatively, you might try setting the DHCPFO TCP port preference:</p><p>Edit ! Preferences ! Protocols ! DHCPFO</p><p>The dissector is configured by default to use port 519</p></div><div id="comment-6925-info" class="comment-info"><span class="comment-age">(17 Oct '11, 07:18)</span> Bill Meier ♦♦</div></div></div><div id="comment-tools-6923" class="comment-tools"></div><div class="clear"></div><div id="comment-6923-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

