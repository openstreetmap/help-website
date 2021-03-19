+++
type = "question"
title = "Compare Two Captures Feature Missing in WireShark 2.0?"
description = '''Accord to the docs: https://www.wireshark.org/docs/wsug_html_chunked/ChStatCompareCaptureFiles.html there should be a feature to compare two captures. I have searched high and low through the software and I am unable to find it anywhere. Was this feature removed? Am I blind? '''
date = "2016-04-12T13:48:00Z"
lastmod = "2017-01-07T10:32:00Z"
weight = 51611
keywords = [ "capture", "compare", "documentation" ]
aliases = [ "/questions/51611" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Compare Two Captures Feature Missing in WireShark 2.0?](/questions/51611/compare-two-captures-feature-missing-in-wireshark-20)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51611-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Accord to the docs: <a href="https://www.wireshark.org/docs/wsug_html_chunked/ChStatCompareCaptureFiles.html">https://www.wireshark.org/docs/wsug_html_chunked/ChStatCompareCaptureFiles.html</a></p><p>there should be a feature to compare two captures. I have searched high and low through the software and I am unable to find it anywhere. Was this feature removed? Am I blind?</p></div><div id="question-tags" class="tags-container tags">capture compare documentation</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Apr '16, 13:48</strong></p><img src="https://secure.gravatar.com/avatar/c93638efc9f829ac8021e933d49b2622?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tyler01&#39;s gravatar image" /><p>tyler01<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tyler01 has no accepted answers">0%</span></p></div></div><div id="comments-container-51611" class="comments-container"></div><div id="comment-tools-51611" class="comment-tools"></div><div class="clear"></div><div id="comment-51611-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="51613"></span>

<div id="answer-container-51613" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51613-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>It's probably a feature that has not yet been ported to 2.x - but if you're interested in comparing two captures, take a look at the "Workbench" tool (previously named TraceMatcher) available at Tribelab:</p><p><a href="https://community.tribelab.com/enrol/index.php?id=15">https://community.tribelab.com/enrol/index.php?id=15</a></p><p>You'll need to create an account before being able to access the page and download it, but its free.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Apr '16, 14:53</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-51613" class="comments-container"></div><div id="comment-tools-51613" class="comment-tools"></div><div class="clear"></div><div id="comment-51613-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="58579"></span>

<div id="answer-container-58579" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58579-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I noticed from the TribeLab stats that there has been a burst of interest in this post so I thought I should provide an update.</p><p>The Workbench Proof of Concept that Jasper referred to had packet matching and Syncro capability (keeping two traces in step). The new production release of Workbench (still free) doesn't yet have this capability. However, we expect to make this feature available again within the next two months.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Jan '17, 10:32</strong></p><img src="https://secure.gravatar.com/avatar/2e1b4057f2ff59fe059b23cc6571abaf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PaulOfford&#39;s gravatar image" /><p>PaulOfford<br />
<span class="score" title="131 reputation points">131</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="32 badges"><span class="silver">●</span><span class="badgecount">32</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PaulOfford has 5 accepted answers">11%</span></p></div></div><div id="comments-container-58579" class="comments-container"></div><div id="comment-tools-58579" class="comment-tools"></div><div class="clear"></div><div id="comment-58579-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

