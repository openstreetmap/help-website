+++
type = "question"
title = "How to identify, which codec is used in VOIP rtp packets ?"
description = '''In this pcap file, I can find RTP, RTCP, and STUN packets. I tried to check which packet does negotiate for the codec, but couldnt find it. Can you please share any idea, where should I look to find this negotiation ? '''
date = "2015-05-09T09:08:00Z"
lastmod = "2015-05-09T10:13:00Z"
weight = 42258
keywords = [ "rtcp", "codec", "rtp" ]
aliases = [ "/questions/42258" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to identify, which codec is used in VOIP rtp packets ?](/questions/42258/how-to-identify-which-codec-is-used-in-voip-rtp-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42258-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42258-score" class="post-score" title="current number of votes">0</div><span id="post-42258-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In this pcap file, I can find RTP, RTCP, and STUN packets. I tried to check which packet does negotiate for the codec, but couldnt find it. Can you please share any idea, where should I look to find this negotiation ?</p><p><img src="https://osqa-ask.wireshark.org/upfiles/cp.png" alt="packet_image" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-rtcp" rel="tag" title="see questions tagged &#39;rtcp&#39;">rtcp</span> <span class="post-tag tag-link-codec" rel="tag" title="see questions tagged &#39;codec&#39;">codec</span> <span class="post-tag tag-link-rtp" rel="tag" title="see questions tagged &#39;rtp&#39;">rtp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 May '15, 09:08</strong></p><img src="https://secure.gravatar.com/avatar/4ec917e3556fb6d9c03cc0e39ec7732a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Shas&#39;s gravatar image" /><p><span>Shas</span><br />
<span class="score" title="1 reputation points">1</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Shas has no accepted answers">0%</span></p></img></div></div><div id="comments-container-42258" class="comments-container"></div><div id="comment-tools-42258" class="comment-tools"></div><div class="clear"></div><div id="comment-42258-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="42259"></span>

<div id="answer-container-42259" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42259-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42259-score" class="post-score" title="current number of votes">0</div><span id="post-42259-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Some observations here:</p><ul><li>I see some encrypted TCP communications</li><li>Of the so-called RTP/RTCP packets, most make no real sense (probably trapped by 'try to dissect outside conversation')</li></ul><p>This leads me to believe that the UDP packets also contain some form of encrypted communication, which could be the VoIP packets you are looking for, but which won't reveil there contents.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 May '15, 10:13</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-42259" class="comments-container"></div><div id="comment-tools-42259" class="comment-tools"></div><div class="clear"></div><div id="comment-42259-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

