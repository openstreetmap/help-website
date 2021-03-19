+++
type = "question"
title = "How to calculate bandwidth requirments based upon flows per minute (fpm)?"
description = '''I want to know how can one calculate bandwidth requirements based upon flows and viceversa. Meaning if I had to achieve total of 50,000 netflows what is the bandwidth requirement to produce this number? Is there a formula for this. I&#x27;m using this to size up flow analyzer appliance. If its license sa...'''
date = "2013-04-25T08:53:00Z"
lastmod = "2013-04-25T09:03:00Z"
weight = 20802
keywords = [ "netflow" ]
aliases = [ "/questions/20802" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How to calculate bandwidth requirments based upon flows per minute (fpm)?](/questions/20802/how-to-calculate-bandwidth-requirments-based-upon-flows-per-minute-fpm)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20802-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to know how can one calculate bandwidth requirements based upon flows and viceversa.</p><p>Meaning if I had to achieve total of 50,000 netflows what is the bandwidth requirement to produce this number? Is there a formula for this. I'm using this to size up flow analyzer appliance. If its license says supports 50,000 flows what does this means. How more bandwidth if i increase I would lose the license coverage?</p><p>Kindly help.</p></div><div id="question-tags" class="tags-container tags">netflow</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Apr '13, 08:53</strong></p><img src="https://secure.gravatar.com/avatar/a5e36ef8cc4416aa199a3a82dcb1deb4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lazerz&#39;s gravatar image" /><p>lazerz<br />
<span class="score" title="41 reputation points">41</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lazerz has no accepted answers">0%</span></p></div></div><div id="comments-container-20802" class="comments-container"></div><div id="comment-tools-20802" class="comment-tools"></div><div class="clear"></div><div id="comment-20802-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="20803"></span>

<div id="answer-container-20803" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20803-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can use a netflow bandwidth calculator:</p><blockquote><p><code>http://www.lancope.com/resource-center/netflow-bandwidth-calculator-stealthwatch-calculator/</code><br />
</p></blockquote><p>Regarding your licensing question:</p><blockquote><p>If its license says supports 50,000 flows what does this means</p></blockquote><p>well, that depends on the vendor. I <strong>guess</strong> that license will only accept 50.000 flows per minute and drop every flow that exceeds that number, meaning you will not see the stats of <strong>every</strong> traffic in that case.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Apr '13, 09:03</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-20803" class="comments-container"></div><div id="comment-tools-20803" class="comment-tools"></div><div class="clear"></div><div id="comment-20803-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

