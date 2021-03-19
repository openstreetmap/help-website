+++
type = "question"
title = "version 2 performance on Mac"
description = '''I&#x27;ve installed the release version of 2.0.0 on my Mac and while the fast startup is great, I get constant beachballs and non-responsiveness from the application when capturing packets. I&#x27;m running Mac OS X 10.11.1 on a Mac Pro with a 3.7Ghz quad-core Xeon E5 and 16GB ram. None of my other applicatio...'''
date = "2015-11-25T03:38:00Z"
lastmod = "2015-11-25T08:16:00Z"
weight = 47958
keywords = [ "performance", "mac", "2.0", "unresponsive", "wireshark" ]
aliases = [ "/questions/47958" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [version 2 performance on Mac](/questions/47958/version-2-performance-on-mac)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47958-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've installed the release version of 2.0.0 on my Mac and while the fast startup is great, I get constant beachballs and non-responsiveness from the application when capturing packets. I'm running Mac OS X 10.11.1 on a Mac Pro with a 3.7Ghz quad-core Xeon E5 and 16GB ram. None of my other applications are affected, it seems like Wireshark itself is going periodically unresponsive. Is this intended, or a bug?</p><p>Cheers, James</p></div><div id="question-tags" class="tags-container tags">performance mac 2.0 unresponsive wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Nov '15, 03:38</strong></p><img src="https://secure.gravatar.com/avatar/e5c24d2187f4342f27122afb329efb33?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="James%20Dore&#39;s gravatar image" /><p>James Dore<br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="James Dore has no accepted answers">0%</span></p></div></div><div id="comments-container-47958" class="comments-container"></div><div id="comment-tools-47958" class="comment-tools"></div><div class="clear"></div><div id="comment-47958-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="47978"></span>

<div id="answer-container-47978" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47978-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Another common cause of Wireshark reporting that it's busy is if:</p><ol><li>You have network name resolution enabled</li><li>(and) you're not using asynchronous resolution</li></ol><p>Actually I think the transport name resolution has also been known to be very slow on Macs too. You might want to try disabling all the name resolution options.</p><p>(Of course if the problem really is too much traffic then this won't help--you could check Wireshark's CPU usage during the busy times to know if it's really working hard or if it's blocked doing something slow like doing a synchronous DNS request.)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Nov '15, 08:16</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-47978" class="comments-container"><span id="47979"></span><div id="comment-47979" class="comment"><div id="post-47979-score" class="comment-score"></div><div class="comment-text"><p>Ah, that made a BIG difference, thanks!</p></div><div id="comment-47979-info" class="comment-info"><span class="comment-age">(25 Nov '15, 08:24)</span> James Dore</div></div></div><div id="comment-tools-47978" class="comment-tools"></div><div class="clear"></div><div id="comment-47978-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="47960"></span>

<div id="answer-container-47960" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47960-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>It's most certainly not intended, but can happen when you capture on a link that is really busy. You should avoid capturing with the Wireshark GUI and use dumpcap instead.</p><p>See <a href="https://blog.packet-foo.com/2013/05/the-notorious-wireshark-out-of-memory-problem/">https://blog.packet-foo.com/2013/05/the-notorious-wireshark-out-of-memory-problem/</a> for some insights on why dumpcap is the better choice.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Nov '15, 03:41</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 25 Nov '15, 03:41</p></div></div><div id="comments-container-47960" class="comments-container"><span id="47961"></span><div id="comment-47961" class="comment"><div id="post-47961-score" class="comment-score"></div><div class="comment-text"><p>Excellent, very useful.</p></div><div id="comment-47961-info" class="comment-info"><span class="comment-age">(25 Nov '15, 03:53)</span> James Dore</div></div></div><div id="comment-tools-47960" class="comment-tools"></div><div class="clear"></div><div id="comment-47960-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

