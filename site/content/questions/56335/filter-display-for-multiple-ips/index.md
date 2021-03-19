+++
type = "question"
title = "Filter display for multiple IP&#x27;s"
description = '''Hi Can anyone help me to filter a display so that it shows all traffic between just three IP&#x27;s, please? I can successfully filter for two IP&#x27;s, ip.addr==x.x.x.x &amp;amp;&amp;amp; ip.addr==y.y.y.y but trying to filter the display so that it shows three IP&#x27;s results in the majority of the capture being displ...'''
date = "2016-10-13T08:06:00Z"
lastmod = "2016-10-13T09:37:00Z"
weight = 56335
keywords = [ "display-filter" ]
aliases = [ "/questions/56335" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Filter display for multiple IP's](/questions/56335/filter-display-for-multiple-ips)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56335-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>Can anyone help me to filter a display so that it shows all traffic between just three IP's, please?</p><p>I can successfully filter for two IP's,</p><p>ip.addr==x.x.x.x &amp;&amp; ip.addr==y.y.y.y</p><p>but trying to filter the display so that it shows three IP's results in the majority of the capture being displayed.</p><p>Thanks!</p></div><div id="question-tags" class="tags-container tags">display-filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Oct '16, 08:06</strong></p><img src="https://secure.gravatar.com/avatar/f2535a5be4122c39ccb2944dc23e6ad3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Blood&#39;s gravatar image" /><p>Blood<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Blood has no accepted answers">0%</span></p></div></div><div id="comments-container-56335" class="comments-container"></div><div id="comment-tools-56335" class="comment-tools"></div><div class="clear"></div><div id="comment-56335-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="56338"></span>

<div id="answer-container-56338" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56338-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you name the 3 PC's a, b and c then the traffic you want is:</p><pre><code>a -&gt; b or a -&gt; c
b -&gt; a or b -&gt; c
c -&gt; a or c -&gt; b</code></pre><p>So that gives a filter of:</p><pre><code>(ip.src == a &amp;&amp; ((ip.dst == b) || (ip.dst == c))) || (ip.src == b &amp;&amp; ((ip.dst == a) || (ip.dst == c))) || (ip.src == c &amp;&amp; ((ip.dst == a) || (ip.dst == b)))</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Oct '16, 09:37</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 13 Oct '16, 12:34</p></div></div><div id="comments-container-56338" class="comments-container"><span id="56346"></span><div id="comment-56346" class="comment"><div id="post-56346-score" class="comment-score">2</div><div class="comment-text"><p>Going with this notation it should be possible to compress this into</p><p>(ip.addr == A &amp;&amp; (ip.addr == B || ip.addr == C)) || (ip.addr == B &amp;&amp; ip.addr == C)</p><p>First part picks up the legs A &lt;-&gt; B and A &lt;-&gt; C, where the last part covers the leg B &lt;-&gt; C</p></div><div id="comment-56346-info" class="comment-info"><span class="comment-age">(13 Oct '16, 12:08)</span> Jaap ♦</div></div><span id="56508"></span><div id="comment-56508" class="comment"><div id="post-56508-score" class="comment-score"></div><div class="comment-text"><p>Ha! No wonder I could not get it to work.</p><p>Thanks very much for the help!</p></div><div id="comment-56508-info" class="comment-info"><span class="comment-age">(19 Oct '16, 07:48)</span> Blood</div></div></div><div id="comment-tools-56338" class="comment-tools"></div><div class="clear"></div><div id="comment-56338-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

