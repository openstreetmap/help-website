+++
type = "question"
title = "scrollbar floats upwards - can&#x27;t see latest packets"
description = '''I&#x27;m running wireshark v2.2.7 on windows 10 32bit, the scrollbar keeps floating upwards and I can&#x27;t see the newest packets as they come in. I drag the scrollbar down to the bottom but as soon I release the mouse it floats upwards again. This never happened on previous wireshark versions. A search on ...'''
date = "2017-06-19T01:02:00Z"
lastmod = "2017-06-19T09:40:00Z"
weight = 62116
keywords = [ "scrollbar" ]
aliases = [ "/questions/62116" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [scrollbar floats upwards - can't see latest packets](/questions/62116/scrollbar-floats-upwards-cant-see-latest-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62116-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm running wireshark v2.2.7 on windows 10 32bit, the scrollbar keeps floating upwards and I can't see the newest packets as they come in. I drag the scrollbar down to the bottom but as soon I release the mouse it floats upwards again. This never happened on previous wireshark versions. A search on google shows up bug reports about this but there's no solution I can see.</p></div><div id="question-tags" class="tags-container tags">scrollbar</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Jun '17, 01:02</strong></p><img src="https://secure.gravatar.com/avatar/a3aeb3e02b7672911169cf411c38dd0b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="neuronetv&#39;s gravatar image" /><p>neuronetv<br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="neuronetv has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 19 Jun '17, 08:11</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-62116" class="comments-container"></div><div id="comment-tools-62116" class="comment-tools"></div><div class="clear"></div><div id="comment-62116-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="62127"></span>

<div id="answer-container-62127" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62127-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Another possibility (depending on the exact symptom) is <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=12074">bug 12074</a>. The workaround for that bug is to disable (DNS) name resolution.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Jun '17, 09:40</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-62127" class="comments-container"><span id="62213"></span><div id="comment-62213" class="comment"><div id="post-62213-score" class="comment-score"></div><div class="comment-text"><p>ok thanks for these responses. I disabled DNS name resolution and now the cursor stays where it should and I can see the new packets as they come in. Hope this bug gets resolved soon</p></div><div id="comment-62213-info" class="comment-info"><span class="comment-age">(21 Jun '17, 09:18)</span> neuronetv</div></div><span id="62300"></span><div id="comment-62300" class="comment"><div id="post-62300-score" class="comment-score"></div><div class="comment-text"><p>A fix for the bug was merged last week so it should be fixed in 2.4.0 as well as 2.2.8.</p></div><div id="comment-62300-info" class="comment-info"><span class="comment-age">(26 Jun '17, 06:36)</span> JeffMorriss ♦</div></div></div><div id="comment-tools-62127" class="comment-tools"></div><div class="clear"></div><div id="comment-62127-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="62126"></span>

<div id="answer-container-62126" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62126-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, this is almost certainly <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=11034">Bug 11034</a>. The bug is still open and so there's no fix available yet.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Jun '17, 08:10</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-62126" class="comments-container"></div><div id="comment-tools-62126" class="comment-tools"></div><div class="clear"></div><div id="comment-62126-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

