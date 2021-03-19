+++
type = "question"
title = "data.data wildcard"
description = '''I’ve been trying to get a filter to match a sequence that can appear at any offset but follows a pattern of two set values, a random value, and a final set value. Tried the usual suspects like: data.data contains a4:c3:$$:b2 data.data contains a4:c3:??:b2 data.data contains a4:c3:*:b2 data.data cont...'''
date = "2015-02-15T20:55:00Z"
lastmod = "2015-02-16T06:26:00Z"
weight = 39877
keywords = [ "wildcard", "data.data" ]
aliases = [ "/questions/39877" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [data.data wildcard](/questions/39877/datadata-wildcard)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39877-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I’ve been trying to get a filter to match a sequence that can appear at any offset but follows a pattern of two set values, a random value, and a final set value.</p><p>Tried the usual suspects like:</p><p>data.data contains a4:c3:$$:b2<br />
data.data contains a4:c3:??:b2<br />
data.data contains a4:c3:*:b2<br />
data.data contains a4:c3:[00-ff]:b2<br />
data.data contains a4:c3:[!00]:b2<br />
</p><p>Tried replacing contains with matches.</p><p>How would I go about doing this?</p><p>Thank you.</p></div><div id="question-tags" class="tags-container tags">wildcard data.data</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Feb '15, 20:55</strong></p><img src="https://secure.gravatar.com/avatar/c5a079da8c95753a1960dd595314c3bc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="screenname123049234583&#39;s gravatar image" /><p>screenname12...<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="screenname123049234583 has no accepted answers">0%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 15 Feb '15, 20:59</p></div></div><div id="comments-container-39877" class="comments-container"></div><div id="comment-tools-39877" class="comment-tools"></div><div class="clear"></div><div id="comment-39877-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39887"></span>

<div id="answer-container-39887" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39887-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p><strong>contains</strong> is a plain string search. What you are looking for is <strong>matches</strong> (regular expressions):</p><blockquote><p><a href="http://wiki.wireshark.org/DisplayFilters">http://wiki.wireshark.org/DisplayFilters</a></p></blockquote><p>I have not tested the following, but I think it should work.</p><blockquote><p>data.data matches "a4:c3:..:b2"</p></blockquote><p>However, if the data is binary, you'll have to escape the HEX representation</p><blockquote><p>data.data matches "\xa4.\xc3...\xb2"</p></blockquote><p>I did NOT escape ":" as I don't know if that's an ASCII char in your example, so I used '.' instead.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Feb '15, 06:26</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 Feb '15, 06:28</p></div></div><div id="comments-container-39887" class="comments-container"></div><div id="comment-tools-39887" class="comment-tools"></div><div class="clear"></div><div id="comment-39887-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

