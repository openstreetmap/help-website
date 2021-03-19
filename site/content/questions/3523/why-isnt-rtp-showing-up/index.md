+++
type = "question"
title = "Why isn&#x27;t RTP showing up?"
description = '''I&#x27;m new to Wireshark. I did some traces from IP phone over a SIP trunk to the PSTN. Trace shows no RTP, but I know it was being used.  Is RTP off by default? Thanks'''
date = "2011-04-15T13:54:00Z"
lastmod = "2013-04-11T04:09:00Z"
weight = 3523
keywords = [ "rtp", "missing" ]
aliases = [ "/questions/3523" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Why isn't RTP showing up?](/questions/3523/why-isnt-rtp-showing-up)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3523-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm new to Wireshark. I did some traces from IP phone over a SIP trunk to the PSTN. Trace shows no RTP, but I know it was being used.<br />
</p><p>Is RTP off by default?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">rtp missing</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Apr '11, 13:54</strong></p><img src="https://secure.gravatar.com/avatar/a1df3a8fdb2cfdb02781f43e1897a319?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="greekgeek&#39;s gravatar image" /><p>greekgeek<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="greekgeek has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-3523" class="comments-container"><span id="3529"></span><div id="comment-3529" class="comment"><div id="post-3529-score" class="comment-score"></div><div class="comment-text"><p>Hi, If you look in the SIP messages carrying SDP you should see the IP and port used for RTP are those packages in the trace? Wireshark uses the SDP information to find out which packets are RTP if the SDP isn't present. Wireshark can't find the packets. Check out the RTP preferences for other options.</p></div><div id="comment-3529-info" class="comment-info"><span class="comment-age">(16 Apr '11, 01:24)</span> Anders ♦</div></div><span id="20306"></span><div id="comment-20306" class="comment"><div id="post-20306-score" class="comment-score"></div><div class="comment-text"><p>I've got the same problem here. I am taking traces on an RTP stream that uses an SAP announcement with SDP information in it instead of getting the SDP info from RTSP. Wireshark is not recognizing the RTP packets.</p></div><div id="comment-20306-info" class="comment-info"><span class="comment-age">(11 Apr '13, 01:26)</span> Frostybeard</div></div></div><div id="comment-tools-3523" class="comment-tools"></div><div class="clear"></div><div id="comment-3523-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="20325"></span>

<div id="answer-container-20325" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20325-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Go to Preferences | Protocols | RTP, check the box "Try to decode RTP outside of conversations".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Apr '13, 04:09</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-20325" class="comments-container"></div><div id="comment-tools-20325" class="comment-tools"></div><div class="clear"></div><div id="comment-20325-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

