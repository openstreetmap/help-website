+++
type = "question"
title = "RTP Stream Analysis shows 0.00 delta and jitter values"
description = '''When analysing individual RTP streams all the colums which should contain ms values are showing 0.00 as with the summary data, e.g.  Max delta = 0.00 ms at packet no. 0  Max jitter = 0.00 ms. Mean jitter = 0.00 ms. Max skew = 0.00 ms. Total RTP packets = 336 (expected 336) Lost RTP packets = 0 (0.00...'''
date = "2011-07-29T02:44:00Z"
lastmod = "2013-03-22T07:40:00Z"
weight = 5358
keywords = [ "skew", "jitter", "rtp", "delta" ]
aliases = [ "/questions/5358" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [RTP Stream Analysis shows 0.00 delta and jitter values](/questions/5358/rtp-stream-analysis-shows-000-delta-and-jitter-values)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5358-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When analysing individual RTP streams all the colums which should contain ms values are showing 0.00 as with the summary data, e.g. Max delta = 0.00 ms at packet no. 0 Max jitter = 0.00 ms. Mean jitter = 0.00 ms. Max skew = 0.00 ms. Total RTP packets = 336 (expected 336) Lost RTP packets = 0 (0.00%) Sequence errors = 0 Duration 6.70 s (0 ms clock drift, corresponding to 1 Hz (+0.00%)</p><p>Is this a config/preferences issue, or is the RTP anlaysis at fault?</p></div><div id="question-tags" class="tags-container tags">skew jitter rtp delta</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Jul '11, 02:44</strong></p><img src="https://secure.gravatar.com/avatar/129aa1df44f1fe6b3398cf08174e2226?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="synack01&#39;s gravatar image" /><p>synack01<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="synack01 has no accepted answers">0%</span></p></div></div><div id="comments-container-5358" class="comments-container"><span id="5372"></span><div id="comment-5372" class="comment"><div id="post-5372-score" class="comment-score"></div><div class="comment-text"><ul><li>Is the setup information in the trace?(in case of SIP the SDP).</li><li>What is the payload type/codec used?</li><li>Which Wireshark version? I think Wireshark needs to know the sample rate and/or packetisation time to do the calculation. You might want to raise a bug report attaching a sample trace illustrating the problem.</li></ul></div><div id="comment-5372-info" class="comment-info"><span class="comment-age">(30 Jul '11, 13:40)</span> Anders ♦</div></div></div><div id="comment-tools-5358" class="comment-tools"></div><div class="clear"></div><div id="comment-5358-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="19752"></span>

<div id="answer-container-19752" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19752-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>good chances that the RTP stack is at fault.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Mar '13, 07:40</strong></p><img src="https://secure.gravatar.com/avatar/a61a39377187ba85feebe6c0da639b66?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="badrigate&#39;s gravatar image" /><p>badrigate<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="badrigate has no accepted answers">0%</span></p></div></div><div id="comments-container-19752" class="comments-container"></div><div id="comment-tools-19752" class="comment-tools"></div><div class="clear"></div><div id="comment-19752-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

