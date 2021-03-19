+++
type = "question"
title = "Delta Time (Conversation) field is blank"
description = '''Hi all...  I have a packet capture for traffic between a pair of hosts that covers 15 minutes, and includes 112 TCP connections between the two. Another tool (NetScout) reported that, within this 15 minutes, there was a high response time (160ms), and I want to isolate that request/response pair. (T...'''
date = "2015-07-14T04:44:00Z"
lastmod = "2015-07-14T05:08:00Z"
weight = 44128
keywords = [ "delta_time", "response_time" ]
aliases = [ "/questions/44128" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Delta Time (Conversation) field is blank](/questions/44128/delta-time-conversation-field-is-blank)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44128-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all...<br />
</p><p>I have a packet capture for traffic between a pair of hosts that covers 15 minutes, and includes 112 TCP connections between the two.</p><p>Another tool (NetScout) reported that, within this 15 minutes, there was a high response time (160ms), and I want to isolate that request/response pair. (The average response time between the two was only 1ms, so this particular response time is an outlier that I need to diagnose.)</p><p>It seemed that adding the column "Delta time (conversation)" would allow me to isolate long delays within TCP conversations, but, after adding it, the value in that column is blank, for every frame.</p><p>By the way, I'm using 1.12.1, which I believe is the latest "stable" release.</p><p>Any help in getting Delta time conversation to work - or, for another way to find the high response time - would be greatly appreciated.</p><p>Thx, feenyman99</p></div><div id="question-tags" class="tags-container tags">delta_time response_time</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Jul '15, 04:44</strong></p><img src="https://secure.gravatar.com/avatar/ba0791e3a82c059268b46a45ae90989f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="feenyman99&#39;s gravatar image" /><p>feenyman99<br />
<span class="score" title="96 reputation points">96</span><span title="22 badges"><span class="badge1">●</span><span class="badgecount">22</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="feenyman99 has one accepted answer">25%</span> </br></p></div></div><div id="comments-container-44128" class="comments-container"><span id="44130"></span><div id="comment-44130" class="comment"><div id="post-44130-score" class="comment-score"></div><div class="comment-text"><p>FYI, 1.12.6 is the latest stable (as I type this).</p></div><div id="comment-44130-info" class="comment-info"><span class="comment-age">(14 Jul '15, 05:24)</span> grahamb ♦</div></div></div><div id="comment-tools-44128" class="comment-tools"></div><div class="clear"></div><div id="comment-44128-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44129"></span>

<div id="answer-container-44129" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44129-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>First, Go to Edit &gt; Preferences &gt; Protocols &gt; TCP and turn on "Calculate conversation timestamps.</p><p>Then, in the Packet Details pane, expand the Transmission Control Protocol portion of any TCP packet. Scroll down to the section labeled "[Timestamps]". Expand that section, then right-click on "[Time since previous frame in this TCP stream]" and select "Apply as column."</p><p>Note that the "[Timestamps]" section won't be present unless you've turned on "Calculate conversation timestamps."</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Jul '15, 05:08</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-44129" class="comments-container"></div><div id="comment-tools-44129" class="comment-tools"></div><div class="clear"></div><div id="comment-44129-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

