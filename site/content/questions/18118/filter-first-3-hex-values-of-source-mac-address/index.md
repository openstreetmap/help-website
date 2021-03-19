+++
type = "question"
title = "filter first 3 hex values of source mac address"
description = '''NEWBIE the mac address consists out of 6 hex values. But I want to only filter is on the first 3 hex values (brand info) Is there some kind of wild card I can use, example: ether.src == 00:20:4a:8f:3d:b1 00:20:4a:8f:3d:b1 = Pronet_8f:3d:b1'''
date = "2013-01-30T11:52:00Z"
lastmod = "2013-01-30T12:30:00Z"
weight = 18118
keywords = [ "mac-adddress", "capture-filter" ]
aliases = [ "/questions/18118" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [filter first 3 hex values of source mac address](/questions/18118/filter-first-3-hex-values-of-source-mac-address)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18118-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>NEWBIE</p><p>the mac address consists out of 6 hex values. But I want to only filter is on the first 3 hex values (brand info)</p><p>Is there some kind of wild card I can use, example: ether.src == 00:20:4a:8f:3d:b1</p><p>00:20:4a:8f:3d:b1 = Pronet_8f:3d:b1</p></div><div id="question-tags" class="tags-container tags">mac-adddress capture-filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Jan '13, 11:52</strong></p><img src="https://secure.gravatar.com/avatar/0cd31c4cc89449a9ca65afcb8de21850?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mear1628&#39;s gravatar image" /><p>mear1628<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mear1628 has no accepted answers">0%</span></p></div></div><div id="comments-container-18118" class="comments-container"></div><div id="comment-tools-18118" class="comment-tools"></div><div class="clear"></div><div id="comment-18118-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="18123"></span>

<div id="answer-container-18123" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18123-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can use :</p><pre><code>eth.src[0:3]==00:20:4a</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Jan '13, 12:30</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-18123" class="comments-container"><span id="18237"></span><div id="comment-18237" class="comment"><div id="post-18237-score" class="comment-score"></div><div class="comment-text"><p>Thanks works like a charm!</p></div><div id="comment-18237-info" class="comment-info"><span class="comment-age">(01 Feb '13, 11:25)</span> mear1628</div></div><span id="18251"></span><div id="comment-18251" class="comment"><div id="post-18251-score" class="comment-score"></div><div class="comment-text"><p>@mear1628</p><p>I've converted your "answer" to a comment as that's how this site works, please read the FAQ for details.</p><p>If an answer solves your issue please accept it for the benefit of other users by clicking the checkmark icon next to the answer.</p></div><div id="comment-18251-info" class="comment-info"><span class="comment-age">(01 Feb '13, 23:59)</span> grahamb ♦</div></div></div><div id="comment-tools-18123" class="comment-tools"></div><div class="clear"></div><div id="comment-18123-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="18119"></span>

<div id="answer-container-18119" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18119-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You could try this:</p><blockquote><p><code>eth.src contains 00:20:4a</code><br />
</p></blockquote><p>That will also match your vendor addresses, however also aa:bb:cc:<strong>00:20:4a</strong> or aa:bb:<strong>00:20:4a</strong>:xx, however such a false positive seems to be rather unlikely.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Jan '13, 11:59</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-18119" class="comments-container"></div><div id="comment-tools-18119" class="comment-tools"></div><div class="clear"></div><div id="comment-18119-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

