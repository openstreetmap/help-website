+++
type = "question"
title = "Filter for duplicate sequence numbers"
description = '''Hello, here is the background to my question:  It is suspected that the traffic going into a switch interface is being looped out the same interface again. To prove or disprove I captured the traffic in both directions on said interface.  If traffic were to looped out the same Interface I should see...'''
date = "2014-04-14T06:49:00Z"
lastmod = "2014-04-14T07:15:00Z"
weight = 31791
keywords = [ "duplicate", "number", "sequence" ]
aliases = [ "/questions/31791" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Filter for duplicate sequence numbers](/questions/31791/filter-for-duplicate-sequence-numbers)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31791-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>here is the background to my question:</p><p>It is suspected that the traffic going into a switch interface is being looped out the same interface again. To prove or disprove I captured the traffic in both directions on said interface.</p><p>If traffic were to looped out the same Interface I should see the same packet twice. The easiest way to show this would be to filter for duplicate sequence numbers (I stand to be corrected on this).</p><p>How do I do this in wireshark without specifying an exact sequene number?</p><p>Best regards, Tim</p></div><div id="question-tags" class="tags-container tags">duplicate number sequence</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Apr '14, 06:49</strong></p><img src="https://secure.gravatar.com/avatar/abcfc237339afb7488160102878d6c02?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="timmeh&#39;s gravatar image" /><p>timmeh<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="timmeh has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 14 Apr '14, 08:10</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-31791" class="comments-container"></div><div id="comment-tools-31791" class="comment-tools"></div><div class="clear"></div><div id="comment-31791-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="31792"></span>

<div id="answer-container-31792" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31792-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You cannot filter on dependencies between two packets, but in your case you could look for tcp.analysis.retransmission since a duplicate packet would be flagged as retransmission by the TCP expert. That way the expert does the dependency check for you and you can just filter on the retransmission.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Apr '14, 07:15</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-31792" class="comments-container"><span id="31793"></span><div id="comment-31793" class="comment"><div id="post-31793-score" class="comment-score"></div><div class="comment-text"><p>Hello,</p><p>thanks for the info. This significantly reduced the number of packets to check and should get me the answer I need.</p><p>Thank you!</p><p>Best regards, Tim</p></div><div id="comment-31793-info" class="comment-info"><span class="comment-age">(14 Apr '14, 07:34)</span> timmeh</div></div></div><div id="comment-tools-31792" class="comment-tools"></div><div class="clear"></div><div id="comment-31792-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

