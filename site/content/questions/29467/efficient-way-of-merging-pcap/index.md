+++
type = "question"
title = "Efficient way of Merging PCAP"
description = '''I have nearly 20 PCAP files inside a directory which needs to be merged, so what I do is this $ls | tee list.txt  $mergecap -w Merged.pcap $(cat list.txt) Is there a better way of doing this ???'''
date = "2014-02-05T10:08:00Z"
lastmod = "2014-02-05T12:52:00Z"
weight = 29467
keywords = [ "merge", "ubuntu" ]
aliases = [ "/questions/29467" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Efficient way of Merging PCAP](/questions/29467/efficient-way-of-merging-pcap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29467-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have nearly 20 PCAP files inside a directory which needs to be merged, so what I do is this</p><p><code>$ls | tee list.txt  $mergecap -w Merged.pcap $(cat list.txt)</code></p><p>Is there a better way of doing this ???</p></div><div id="question-tags" class="tags-container tags">merge ubuntu</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Feb '14, 10:08</strong></p><img src="https://secure.gravatar.com/avatar/bc835c49c84e7410e78b82e40ac9620e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ashiq&#39;s gravatar image" /><p>Ashiq<br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ashiq has no accepted answers">0%</span></p></div></div><div id="comments-container-29467" class="comments-container"></div><div id="comment-tools-29467" class="comment-tools"></div><div class="clear"></div><div id="comment-29467-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29470"></span>

<div id="answer-container-29470" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29470-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>what about this:</p><blockquote><p>mergecap -w Merged.pcap `ls`</p></blockquote><p>ls is in backticks!</p><p>or this</p><blockquote><p>mergecap -w Merged.pcap *</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Feb '14, 12:52</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 05 Feb '14, 12:53</p></div></div><div id="comments-container-29470" class="comments-container"></div><div id="comment-tools-29470" class="comment-tools"></div><div class="clear"></div><div id="comment-29470-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

