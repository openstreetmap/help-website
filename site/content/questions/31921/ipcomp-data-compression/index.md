+++
type = "question"
title = "Ipcomp data compression"
description = '''How do I see IPComp compressed data in Wireshark?'''
date = "2014-04-17T03:56:00Z"
lastmod = "2014-04-19T14:54:00Z"
weight = 31921
keywords = [ "wireshark" ]
aliases = [ "/questions/31921" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Ipcomp data compression](/questions/31921/ipcomp-data-compression)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31921-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How do I see IPComp compressed data in Wireshark?</p></div><div id="question-tags" class="tags-container tags">wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Apr '14, 03:56</strong></p><img src="https://secure.gravatar.com/avatar/2a6affaad632df832e3346f6791a6eb6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mongiabrothers&#39;s gravatar image" /><p>mongiabrothers<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mongiabrothers has no accepted answers">0%</span></p></div></div><div id="comments-container-31921" class="comments-container"><span id="31923"></span><div id="comment-31923" class="comment"><div id="post-31923-score" class="comment-score"></div><div class="comment-text"><p>What version of Wireshark and what OS?</p></div><div id="comment-31923-info" class="comment-info"><span class="comment-age">(17 Apr '14, 04:04)</span> grahamb ♦</div></div></div><div id="comment-tools-31921" class="comment-tools"></div><div class="clear"></div><div id="comment-31921-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="31995"></span>

<div id="answer-container-31995" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31995-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>How do I see IPComp compressed data in Wireshark?</p></blockquote><p>By creating IPComp traffic (please google how to do that!) and then by applying the following display filter</p><blockquote><p>ipcomp</p></blockquote><p>like frame #200 in the following capture file sample</p><blockquote><p><a href="http://www.pcapr.net/view/bwilkerson/2009/1/2/14/fuzz-2008-04-16-7479.pcap.html">http://www.pcapr.net/view/bwilkerson/2009/1/2/14/fuzz-2008-04-16-7479.pcap.html</a></p></blockquote><p>Hint: You need to create an account to see the full sample!</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Apr '14, 14:54</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-31995" class="comments-container"></div><div id="comment-tools-31995" class="comment-tools"></div><div class="clear"></div><div id="comment-31995-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

