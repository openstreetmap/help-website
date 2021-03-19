+++
type = "question"
title = "Jitter formula"
description = '''J(1) = J(0) + (|D(0,1)| - J(0))/16 -----&amp;gt; why this factor 16 is used?'''
date = "2013-07-02T00:19:00Z"
lastmod = "2013-07-02T00:32:00Z"
weight = 22540
keywords = [ "formula", "jitter", "rtp" ]
aliases = [ "/questions/22540" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Jitter formula](/questions/22540/jitter-formula)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22540-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>J(1) = J(0) + (|D(0,1)| - J(0))/16 -----&gt; why this factor 16 is used?</p></div><div id="question-tags" class="tags-container tags">formula jitter rtp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Jul '13, 00:19</strong></p><img src="https://secure.gravatar.com/avatar/276dd2e60fd9f342b8fc2d3bd102886e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Surajitm&#39;s gravatar image" /><p>Surajitm<br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Surajitm has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 02 Jul '13, 18:12</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-22540" class="comments-container"></div><div id="comment-tools-22540" class="comment-tools"></div><div class="clear"></div><div id="comment-22540-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22543"></span>

<div id="answer-container-22543" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22543-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>It's defined in the RTP <a href="http://www.ietf.org/rfc/rfc3550.txt">RFC3550</a></p><p>Cite:</p><pre><code>      This algorithm is the optimal first-order estimator and the gain
      parameter 1/16 gives a good noise reduction ratio while
      maintaining a reasonable rate of convergence [22].</code></pre><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Jul '13, 00:32</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-22543" class="comments-container"></div><div id="comment-tools-22543" class="comment-tools"></div><div class="clear"></div><div id="comment-22543-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

