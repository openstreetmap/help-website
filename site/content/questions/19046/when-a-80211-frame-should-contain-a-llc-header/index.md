+++
type = "question"
title = "When a 802.11 frame should contain a LLC header?"
description = '''Well, the title of the question is the question itself :P I have been looking for the answer into the 802.11-2007 and 2012 standards, but I didn&#x27;t find anything.  Hope you&#x27;ll be able to help me with this. I supose that maybe must be a combination of flag values in the MAC (Medium Access Control) hea...'''
date = "2013-03-01T10:13:00Z"
lastmod = "2013-03-01T15:43:00Z"
weight = 19046
keywords = [ "llc", "header", "802.11" ]
aliases = [ "/questions/19046" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [When a 802.11 frame should contain a LLC header?](/questions/19046/when-a-80211-frame-should-contain-a-llc-header)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19046-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Well, the title of the question is the question itself :P</p><p>I have been looking for the answer into the 802.11-2007 and 2012 standards, but I didn't find anything.</p><p>Hope you'll be able to help me with this.</p><p>I supose that maybe must be a combination of flag values in the MAC (Medium Access Control) header, which determines if the frame needs to carry the LLC header.</p></div><div id="question-tags" class="tags-container tags">llc header 802.11</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Mar '13, 10:13</strong></p><img src="https://secure.gravatar.com/avatar/0345b8194289f7659e3735f5188a83c2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="CapitanShinChan&#39;s gravatar image" /><p>CapitanShinChan<br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="CapitanShinChan has no accepted answers">0%</span></p></div></div><div id="comments-container-19046" class="comments-container"></div><div id="comment-tools-19046" class="comment-tools"></div><div class="clear"></div><div id="comment-19046-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="19081"></span>

<div id="answer-container-19081" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19081-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>An 802.11 frame should contain an LLC header if, and only if, it's a Data frame. The frame type and subtype are part of the Frame Control field in the MAC header; Data is one of the frame type values (the others are Control and Management). The subtype doesn't matter - <em>all</em> Data frames should contain an LLC header, and <em>no</em> other frames should.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Mar '13, 15:43</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-19081" class="comments-container"><span id="60109"></span><div id="comment-60109" class="comment"><div id="post-60109-score" class="comment-score"></div><div class="comment-text"><p>Why <code>Wireshark</code> does not show LLC header in encrypted data packets?</p></div><div id="comment-60109-info" class="comment-info"><span class="comment-age">(16 Mar '17, 06:44)</span> SuBCo</div></div><span id="60125"></span><div id="comment-60125" class="comment"><div id="post-60125-score" class="comment-score"></div><div class="comment-text"><p>Because you have to decrypt the capture.</p><p>LLC exists at a higher OSI layer than the 802.11 header. All data above the WiFi header is encrypted which includes the LLC</p></div><div id="comment-60125-info" class="comment-info"><span class="comment-age">(16 Mar '17, 13:06)</span> Amato_C</div></div></div><div id="comment-tools-19081" class="comment-tools"></div><div class="clear"></div><div id="comment-19081-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

