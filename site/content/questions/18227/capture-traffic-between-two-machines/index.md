+++
type = "question"
title = "Capture Traffic Between Two Machines"
description = '''WS 1.8.4 - I&#x27;m wondering how I can capture traffic only between two machines? I basically want the capture filter to get all tcp/ip traffic between just two machines in both directions. Then I&#x27;ll use a display filter to drill deeper than that. I&#x27;ve tried the following commands and close variants (su...'''
date = "2013-02-01T08:01:00Z"
lastmod = "2013-02-01T08:37:00Z"
weight = 18227
keywords = [ "capture-filter" ]
aliases = [ "/questions/18227" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Capture Traffic Between Two Machines](/questions/18227/capture-traffic-between-two-machines)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18227-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>WS 1.8.4 - I'm wondering how I can capture traffic only between two machines? I basically want the capture filter to get all tcp/ip traffic between just two machines in both directions. Then I'll use a display filter to drill deeper than that.</p><p>I've tried the following commands and close variants (substituting &amp;&amp; for and, etc.)</p><p>(ip.src 10.0.0.1 and ip.dst 10.0.0.2) or (ip.dst 10.0.0.1 and ip.src 10.0.0.2) ip.addr==10.0.0.1 &amp;&amp; ip.addr==10.0.0.2</p><p>Its seems like the syntax has changed recently with the 1.8.x versions. I used to be able to just type "src" in the display filter I thought, but that's not even listed in the reference anymore.</p><p>Thanks in advance for any help! Adam</p><p>EDIT: it allows appears that the syntax checker disappeared from edit -&gt; preferences -&gt; capture (according to the doc.)</p></div><div id="question-tags" class="tags-container tags">capture-filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Feb '13, 08:01</strong></p><img src="https://secure.gravatar.com/avatar/ac5f3deb5a4d8a1390493454e4f051b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="amarcionek&#39;s gravatar image" /><p>amarcionek<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="amarcionek has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 01 Feb '13, 08:05</p></div></div><div id="comments-container-18227" class="comments-container"></div><div id="comment-tools-18227" class="comment-tools"></div><div class="clear"></div><div id="comment-18227-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="18228"></span>

<div id="answer-container-18228" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18228-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Ok, I'm going to answer my own question....</p><p>I think on the capture filter side, you can't use the same syntax as the display filter side? I was able to use this in the display filter and it worked:</p><p>tcp and ip.addr==10.0.0.1 &amp;&amp; ip.addr==10.0.0.2</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Feb '13, 08:24</strong></p><img src="https://secure.gravatar.com/avatar/ac5f3deb5a4d8a1390493454e4f051b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="amarcionek&#39;s gravatar image" /><p>amarcionek<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="amarcionek has no accepted answers">0%</span></p></div></div><div id="comments-container-18228" class="comments-container"></div><div id="comment-tools-18228" class="comment-tools"></div><div class="clear"></div><div id="comment-18228-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="18229"></span>

<div id="answer-container-18229" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18229-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>For a capture filter to only see the traffic between two machines: <code>host x.x.x.x &amp;&amp; host y.y.y.y</code>.</p><p>As you have noted capture and display filters are two different things with different syntaxes.</p><p>There are many filter examples around the internet, remember tcpdump filters are capture filters for Wireshark (and TShark) purposes.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Feb '13, 08:37</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-18229" class="comments-container"></div><div id="comment-tools-18229" class="comment-tools"></div><div class="clear"></div><div id="comment-18229-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

