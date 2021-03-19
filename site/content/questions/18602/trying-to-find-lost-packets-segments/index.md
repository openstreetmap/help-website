+++
type = "question"
title = "Trying to find lost packets (segments)"
description = '''Is there a way that when you run wireshark to ONLY capture lost segments. Or how do I set it to ONLY capture TCP when running the capture?'''
date = "2013-02-13T10:58:00Z"
lastmod = "2013-02-13T11:17:00Z"
weight = 18602
keywords = [ "segment", "lost" ]
aliases = [ "/questions/18602" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Trying to find lost packets (segments)](/questions/18602/trying-to-find-lost-packets-segments)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18602-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is there a way that when you run wireshark to <strong>ONLY</strong> capture lost segments. Or how do I set it to <strong>ONLY</strong> capture TCP when running the capture?</p></div><div id="question-tags" class="tags-container tags">segment lost</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Feb '13, 10:58</strong></p><img src="https://secure.gravatar.com/avatar/1401f0a95294cd2b20ca35e52dfcfac7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dejavu&#39;s gravatar image" /><p>Dejavu<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dejavu has no accepted answers">0%</span></p></div></div><div id="comments-container-18602" class="comments-container"></div><div id="comment-tools-18602" class="comment-tools"></div><div class="clear"></div><div id="comment-18602-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="18605"></span>

<div id="answer-container-18605" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18605-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Is there a way that when you run wireshark to ONLY capture lost segments.</p></blockquote><p>well, as the segment is <strong>lost</strong> there is no way to <strong>capture</strong> it with wireshark ;-)) Why do you want to do that?</p><p>Maybe a <a href="http://wiki.wireshark.org/DisplayFilters">display filter</a> that detects 'lost segments' is what you need: <strong>tcp.analysis.lost_segment</strong></p><blockquote><p>Or how do I set it to ONLY capture TCP</p></blockquote><p>you can use the following <a href="http://wiki.wireshark.org/CaptureFilters">capture filter</a>: <strong>tcp</strong></p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Feb '13, 11:17</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 13 Feb '13, 13:35</p></div></div><div id="comments-container-18605" class="comments-container"><span id="18606"></span><div id="comment-18606" class="comment"><div id="post-18606-score" class="comment-score"></div><div class="comment-text"><p>Is there a way for it to capture only lost segments?</p></div><div id="comment-18606-info" class="comment-info"><span class="comment-age">(13 Feb '13, 11:24)</span> Dejavu</div></div><span id="18610"></span><div id="comment-18610" class="comment"><div id="post-18610-score" class="comment-score"></div><div class="comment-text"><p>as I said. There is no way to capture something that is <strong>lost</strong>, as lost means: it is <strong>not</strong> there ;-)</p><p>What are you trying to do?</p></div><div id="comment-18610-info" class="comment-info"><span class="comment-age">(13 Feb '13, 13:04)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-18605" class="comment-tools"></div><div class="clear"></div><div id="comment-18605-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

