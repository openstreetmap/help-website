+++
type = "question"
title = "Plugin compatible with 1.10 and 1.8"
description = '''I currently have two windows plugins compiled separately for the same dissector, one for version 1.8.x and the other for 1.10.x. If I try using any of these across versions, it throws an error -&amp;gt; &quot;STATUS_ACCESS_VIOLATION: dissector accessed and invalid memory address&quot;. My question is, how do I co...'''
date = "2013-08-01T06:40:00Z"
lastmod = "2013-08-01T09:51:00Z"
weight = 23498
keywords = [ "dissector", "1.8.0", "compatibility", "1.10.0", "plugin" ]
aliases = [ "/questions/23498" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Plugin compatible with 1.10 and 1.8](/questions/23498/plugin-compatible-with-110-and-18)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23498-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I currently have two windows plugins compiled separately for the same dissector, one for version 1.8.x and the other for 1.10.x.</p><p>If I try using any of these across versions, it throws an error -&gt; "STATUS_ACCESS_VIOLATION: dissector accessed and invalid memory address".</p><p>My question is, how do I compile a plugin so that it would be compatible with both 1.8 and 1.10? Or is it not possible?</p></div><div id="question-tags" class="tags-container tags">dissector 1.8.0 compatibility 1.10.0 plugin</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Aug '13, 06:40</strong></p><img src="https://secure.gravatar.com/avatar/46196bc495ce51058590c4e4ae334d22?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SidR&#39;s gravatar image" /><p>SidR<br />
<span class="score" title="245 reputation points">245</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="22 badges"><span class="bronze">●</span><span class="badgecount">22</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SidR has 3 accepted answers">30%</span></p></div></div><div id="comments-container-23498" class="comments-container"></div><div id="comment-tools-23498" class="comment-tools"></div><div class="clear"></div><div id="comment-23498-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="23506"></span>

<div id="answer-container-23506" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23506-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>My question is, how do I compile a plugin so that it would be compatible with both 1.8 and 1.10? Or is it not possible?</p></blockquote><p>You can't, because it's not possible. We make no guarantees that any APIs or ABIs will remain unchanged between major releases. Someday we might come up with APIs and corresponding ABIs that we think won't ever have to be changed in a binary-incompatible or source-incompatible fashion due to new requirements for various protocols or capture file formats or..., but that's not the case now.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Aug '13, 09:51</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-23506" class="comments-container"></div><div id="comment-tools-23506" class="comment-tools"></div><div class="clear"></div><div id="comment-23506-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="23501"></span>

<div id="answer-container-23501" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23501-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>I don't think it's possible as the binary interface generally changes over a major version.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Aug '13, 07:03</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-23501" class="comments-container"></div><div id="comment-tools-23501" class="comment-tools"></div><div class="clear"></div><div id="comment-23501-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

