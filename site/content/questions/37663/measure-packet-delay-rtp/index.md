+++
type = "question"
title = "Measure packet delay RTP"
description = '''Can we measure Delay in RTP Stream with Wireshark? I know that we have Delta and Difference but its not directly Delay. http://wiki.wireshark.org/RTP_statistics In that link, someone have directly Delay in his stream, there is some way to do that? If not, can we use Delay or Diffrence to get a Delay...'''
date = "2014-11-07T11:54:00Z"
lastmod = "2014-11-11T18:38:00Z"
weight = 37663
keywords = [ "rtp", "voip" ]
aliases = [ "/questions/37663" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Measure packet delay RTP](/questions/37663/measure-packet-delay-rtp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37663-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Can we measure Delay in RTP Stream with Wireshark? I know that we have Delta and Difference but its not directly Delay. <a href="http://wiki.wireshark.org/RTP_statistics">http://wiki.wireshark.org/RTP_statistics</a> In that link, someone have directly Delay in his stream, there is some way to do that? If not, can we use Delay or Diffrence to get a Delay?</p><p>Thanks for answers.</p></div><div id="question-tags" class="tags-container tags">rtp voip</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Nov '14, 11:54</strong></p><img src="https://secure.gravatar.com/avatar/63d441d8d15c157bc188ea2cde792512?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="LordGruch&#39;s gravatar image" /><p>LordGruch<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="LordGruch has no accepted answers">0%</span></p></div></div><div id="comments-container-37663" class="comments-container"><span id="37763"></span><div id="comment-37763" class="comment"><div id="post-37763-score" class="comment-score"></div><div class="comment-text"><p>can you please add <strong>your</strong> definition of <strong>Delay</strong></p></div><div id="comment-37763-info" class="comment-info"><span class="comment-age">(11 Nov '14, 14:34)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-37663" class="comment-tools"></div><div class="clear"></div><div id="comment-37663-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37768"></span>

<div id="answer-container-37768" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37768-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can't directly measure delay for something like RTP, has no acknowledgement protocol, when you are only capturing data at one point. Have a look at the discusson on this thread - <a href="https://ask.wireshark.org/questions/1620/packet-delay">https://ask.wireshark.org/questions/1620/packet-delay</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Nov '14, 18:38</strong></p><img src="https://secure.gravatar.com/avatar/57fbbe2a1e14ccc2a681a28886e5a484?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="martyvis&#39;s gravatar image" /><p>martyvis<br />
<span class="score" title="891 reputation points">891</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="martyvis has 5 accepted answers">7%</span></p></div></div><div id="comments-container-37768" class="comments-container"><span id="37778"></span><div id="comment-37778" class="comment"><div id="post-37778-score" class="comment-score">1</div><div class="comment-text"><p>There is always the round-trip propagation delay if the RTCP reports and filled in correctly and captured. The RTCP dissector supports this, see <a href="http://wiki.wireshark.org/RTCP.">http://wiki.wireshark.org/RTCP.</a></p><p>Bear in mind that this is relative to the capture point, and that using (half) this figure assumes that that both directions have roughly the same delay, and that RTCP frames are treated throughout the network the same as RTP frames.</p></div><div id="comment-37778-info" class="comment-info"><span class="comment-age">(12 Nov '14, 02:20)</span> MartinM</div></div></div><div id="comment-tools-37768" class="comment-tools"></div><div class="clear"></div><div id="comment-37768-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

