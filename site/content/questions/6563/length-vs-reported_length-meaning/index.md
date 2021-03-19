+++
type = "question"
title = "length vs reported_length meaning"
description = '''Hello guys, I am a beginner. There is a question as below: What&#x27;s the difference between the tvb_length() and tvb_reported_length() or &quot;length&quot; and &quot;reported length&quot;? Thanks for you answers! Sam'''
date = "2011-09-26T08:25:00Z"
lastmod = "2011-09-26T10:33:00Z"
weight = 6563
keywords = [ "development" ]
aliases = [ "/questions/6563" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [length vs reported\_length meaning](/questions/6563/length-vs-reported_length-meaning)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6563-score" class="post-score" title="current number of votes">2</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Hello guys,</p><p>I am a beginner. There is a question as below:</p><p>What's the difference between the <code>tvb_length()</code> and <code>tvb_reported_length()</code> or "length" and "reported length"?</p><p>Thanks for you answers!</p><p>Sam</p></div><div id="question-tags" class="tags-container tags">development</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Sep '11, 08:25</strong></p><img src="https://secure.gravatar.com/avatar/e9d668dd28830dd8f79d4dbb56e5f2bc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sam&#39;s gravatar image" /><p>Sam<br />
<span class="score" title="51 reputation points">51</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sam has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 Sep '11, 21:42</p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-6563" class="comments-container"></div><div id="comment-tools-6563" class="comment-tools"></div><div class="clear"></div><div id="comment-6563-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="6567"></span>

<div id="answer-container-6567" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6567-score" class="post-score" title="current number of votes">4</div></div></td><td><div class="item-right"><div class="answer-body"><p><code>tvb_length()</code> reports the actual amount of data in the TVB, while <code>tvb_reported_length()</code> reports the amount of data there should be according to the underlying protocol.</p><p>Why this difference? For one, the capture can be made in such a way that only the first x bytes of the frame are stored. Then the TVB contents will be less than the reported length.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Sep '11, 10:33</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-6567" class="comments-container"><span id="34390"></span><div id="comment-34390" class="comment"><div id="post-34390-score" class="comment-score"></div><div class="comment-text"><p>"Underlying protocol" meaning the "layer carrying the data" right? For example, the underlying protocol of HTTP is TCP.</p></div><div id="comment-34390-info" class="comment-info"><span class="comment-age">(03 Jul '14, 09:59)</span> Lekensteyn</div></div></div><div id="comment-tools-6567" class="comment-tools"></div><div class="clear"></div><div id="comment-6567-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="6565"></span>

<div id="answer-container-6565" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6565-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>I think Bill Meier's <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=5403#c13">comment 13</a> in bug <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=5403">5403</a> sum it up nicely, but just to be clear in case you're not familiar with snaplens: During packet capturing, it is possible and sometimes desirable to only capture up to some maximum number of bytes per packet, and not necessarily the whole packet. Wireshark, tshark, dumpcap, (and other packet capturing tools) all have an option for setting this limit and it's generally referred to as the snaplen.</p><p>When using a snaplen then, the packet can be truncated when captured; however, the original length - i.e. the number of bytes that would have been captured had a snaplen not been set - is still known. So, we have the length, which is the number of bytes actually captured and the reported_length, which is the number of bytes that would have been captured if a snaplen had not been used.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Sep '11, 10:19</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-6565" class="comments-container"><span id="6588"></span><div id="comment-6588" class="comment"><div id="post-6588-score" class="comment-score"></div><div class="comment-text"><p>Thanks, it's very helpful for me.</p><p>Regards, Sam</p></div><div id="comment-6588-info" class="comment-info"><span class="comment-age">(27 Sep '11, 05:39)</span> Sam</div></div></div><div id="comment-tools-6565" class="comment-tools"></div><div class="clear"></div><div id="comment-6565-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

