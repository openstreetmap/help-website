+++
type = "question"
title = "Typing &quot;x&quot; in display filter crashes Wireshark 1.12.6"
description = '''I&#x27;ve built Wireshark 1.12.6 from the source tarball on the download page. The only change I&#x27;ve made is adding a single dissector, which was working pretty solidly in the 1.10.x series. In the 1.12.6 version when I go to type an x in the display filter (such as protocol.somefield == 0x12), Wireshark ...'''
date = "2015-08-05T07:18:00Z"
lastmod = "2015-08-06T12:22:00Z"
weight = 44869
keywords = [ "filter", "crash", "display" ]
aliases = [ "/questions/44869" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Typing "x" in display filter crashes Wireshark 1.12.6](/questions/44869/typing-x-in-display-filter-crashes-wireshark-1126)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44869-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've built Wireshark 1.12.6 from the source tarball on the download page. The only change I've made is adding a single dissector, which was working pretty solidly in the 1.10.x series. In the 1.12.6 version when I go to type an x in the display filter (such as protocol.somefield == 0x12), Wireshark immediately hangs and crashes upon typing the "x".</p><p>Thanks, Brian</p></div><div id="question-tags" class="tags-container tags">filter crash display</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Aug '15, 07:18</strong></p><img src="https://secure.gravatar.com/avatar/ca4d08b00778143dab07e2cde30f653c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="brwiese&#39;s gravatar image" /><p>brwiese<br />
<span class="score" title="26 reputation points">26</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="brwiese has one accepted answer">50%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 05 Aug '15, 08:27</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-44869" class="comments-container"><span id="44870"></span><div id="comment-44870" class="comment"><div id="post-44870-score" class="comment-score"></div><div class="comment-text"><p>is 'protocol' in 'protocol.somefield' your protocol or an already existing protocol?</p></div><div id="comment-44870-info" class="comment-info"><span class="comment-age">(05 Aug '15, 07:26)</span> Jaap ♦</div></div></div><div id="comment-tools-44869" class="comment-tools"></div><div class="clear"></div><div id="comment-44869-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44909"></span>

<div id="answer-container-44909" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44909-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Found the problem. My value_string variables did not have "{ 0, NULL }" as the last value. This didn't seem to be a problem in the 1.8.x and 1.10.x series, but who knows.</p><p>Thanks, Brian</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Aug '15, 12:22</strong></p><img src="https://secure.gravatar.com/avatar/ca4d08b00778143dab07e2cde30f653c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="brwiese&#39;s gravatar image" /><p>brwiese<br />
<span class="score" title="26 reputation points">26</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="brwiese has one accepted answer">50%</span></p></div></div><div id="comments-container-44909" class="comments-container"><span id="44913"></span><div id="comment-44913" class="comment"><div id="post-44913-score" class="comment-score"></div><div class="comment-text"><p>So it was your protocol, and yes, the final {0, NULL} tuple is important, also in 1.8 and 1.10. You just got lucky, I guess.</p></div><div id="comment-44913-info" class="comment-info"><span class="comment-age">(06 Aug '15, 22:42)</span> Jaap ♦</div></div></div><div id="comment-tools-44909" class="comment-tools"></div><div class="clear"></div><div id="comment-44909-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

