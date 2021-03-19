+++
type = "question"
title = "What would be the correct way of...?"
description = '''Making a capture filter(I think) that hides packets from 10.1.1.2, only udp and less then 75 length. I&#x27;m really knew so please help. Edit: new* hahahah'''
date = "2014-09-02T20:26:00Z"
lastmod = "2014-09-07T01:27:00Z"
weight = 35943
keywords = [ "filter" ]
aliases = [ "/questions/35943" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [What would be the correct way of...?](/questions/35943/what-would-be-the-correct-way-of)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35943-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Making a capture filter(I think) that hides packets from 10.1.1.2, only udp and less then 75 length. I'm really knew so please help. Edit: new* hahahah</p></div><div id="question-tags" class="tags-container tags">filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Sep '14, 20:26</strong></p><img src="https://secure.gravatar.com/avatar/f24986a3c3f5a0112c7cc5a4d9145591?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="akiyopringle&#39;s gravatar image" /><p>akiyopringle<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="akiyopringle has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 02 Sep '14, 20:26</p></div></div><div id="comments-container-35943" class="comments-container"><span id="35995"></span><div id="comment-35995" class="comment"><div id="post-35995-score" class="comment-score">2</div><div class="comment-text"><p>I.e.:</p><ul><li>you don't want to see packets from 10.1.1.2;</li><li>you only want to see UDP packets (i.e., you don't want to see non-UDP packets);</li><li>you only want to see packets less than 75 bytes long?</li></ul><p>If so, by "length" do you mean the length of the full link-layer packet, including the link-level header (Ethernet header, 802.11 header, etc.), or do you mean the length of the IP packet (not including the length of the link-level header but including the length of the IP header), or the length of the UDP packet (not including the length of the link-level and IP headers but including the length of the UDP header), or the length of the UDP payload (not including the length of the link-level, IP, and UDP headers)?</p></div><div id="comment-35995-info" class="comment-info"><span class="comment-age">(04 Sep '14, 02:33)</span> Guy Harris ♦♦</div></div><span id="36051"></span><div id="comment-36051" class="comment"><div id="post-36051-score" class="comment-score"></div><div class="comment-text"><p>I don't know man. I can't understand half of what you're saying :(</p></div><div id="comment-36051-info" class="comment-info"><span class="comment-age">(07 Sep '14, 01:01)</span> akiyopringle</div></div></div><div id="comment-tools-35943" class="comment-tools"></div><div class="clear"></div><div id="comment-35943-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="36052"></span>

<div id="answer-container-36052" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36052-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>So I'll ignore the length part, as I can't answer that without knowing exactly what you mean by "less than 75 length".</p><p>If by "capture filter" you mean you want to capture live traffic and discard all the traffic in which you're not interested, the filter would be</p><pre><code>not host 10.1.1.2 and udp</code></pre><p>If you have already captured some traffic, and want to display only the packets that aren't from 10.1.1.2 and that are UDP packets, that would be a <em>display</em> filter, and the display filter would be</p><pre><code>!(ip.addr == 10.1.1.2) and udp</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Sep '14, 01:27</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-36052" class="comments-container"></div><div id="comment-tools-36052" class="comment-tools"></div><div class="clear"></div><div id="comment-36052-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

