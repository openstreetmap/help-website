+++
type = "question"
title = "ip addresses analysis"
description = '''how can we find out server ip address from the pcap file using wireshark ??? can we create specific filter columns (like protocol, source, destination... etc..) in the packets pane???? pls let me knew '''
date = "2013-05-05T18:24:00Z"
lastmod = "2013-05-06T02:11:00Z"
weight = 20972
keywords = [ "ip" ]
aliases = [ "/questions/20972" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [ip addresses analysis](/questions/20972/ip-addresses-analysis)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20972-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>how can we find out server ip address from the pcap file using wireshark ??? can we create specific filter columns (like protocol, source, destination... etc..) in the packets pane???? pls let me knew</p></div><div id="question-tags" class="tags-container tags">ip</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 May '13, 18:24</strong></p><img src="https://secure.gravatar.com/avatar/0f19aa9efeeb7a1409b85d75ad0ca07c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ark&#39;s gravatar image" /><p>ark<br />
<span class="score" title="16 reputation points">16</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ark has no accepted answers">0%</span></p></div></div><div id="comments-container-20972" class="comments-container"></div><div id="comment-tools-20972" class="comment-tools"></div><div class="clear"></div><div id="comment-20972-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="20980"></span>

<div id="answer-container-20980" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20980-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The server is usually the IP the TCP SYN packets are sent to, while the source of the SYN packets in the client. So you could filter on the SYN packets using "tcp.flags==2" and see which IPs are targeted.</p><p>You can add almost any column you like; either by editing them in the preferences, or by selecting a field in the decode and use the popup menu to "apply as column". The same works if you want to filter on something - select the field in the decode and use the popup menu to "apply as filter".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 May '13, 02:11</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-20980" class="comments-container"></div><div id="comment-tools-20980" class="comment-tools"></div><div class="clear"></div><div id="comment-20980-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="20973"></span>

<div id="answer-container-20973" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20973-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>One way is to click Statistics&gt;Conversations This will open a new window and you can click ipv4 or tcp option to check out the Destination IP/src IP/src port/dst port(4 tuple)</p><p>Yes,You can create display filters for protocol,source,destination etc.There is a filter tab in Filter tool bar to play with lot of options.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 May '13, 19:00</strong></p><img src="https://secure.gravatar.com/avatar/2b038237e64839261fcc88e9fdef2b68?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="krishnayeddula&#39;s gravatar image" /><p>krishnayeddula<br />
<span class="score" title="629 reputation points">629</span><span title="35 badges"><span class="badge1">●</span><span class="badgecount">35</span></span><span title="41 badges"><span class="silver">●</span><span class="badgecount">41</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="krishnayeddula has 3 accepted answers">6%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 05 May '13, 19:28</p></div></div><div id="comments-container-20973" class="comments-container"></div><div id="comment-tools-20973" class="comment-tools"></div><div class="clear"></div><div id="comment-20973-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

