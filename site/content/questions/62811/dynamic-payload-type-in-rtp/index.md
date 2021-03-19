+++
type = "question"
title = "dynamic payload type in RTP"
description = '''hi. i have a pcap with RTP packets. in this pcap i have no SIP or SDP packets(only RTP).and payload type field is dynamic. How can i find out payload type? ALL payloads start with 0x000001B2? and marker bit is set in all packets. are these packets containing MPEG?  i know that payloa_type=32 has bee...'''
date = "2017-07-15T11:58:00Z"
lastmod = "2017-07-15T12:16:00Z"
weight = 62811
keywords = [ "rtp" ]
aliases = [ "/questions/62811" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [dynamic payload type in RTP](/questions/62811/dynamic-payload-type-in-rtp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62811-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62811-score" class="post-score" title="current number of votes">0</div><span id="post-62811-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi. i have a pcap with RTP packets. in this pcap i have no SIP or SDP packets(only RTP).and payload type field is dynamic. How can i find out payload type? ALL payloads start with 0x000001B2? and marker bit is set in all packets. are these packets containing MPEG? i know that payloa_type=32 has been assigned to MPEG. but is it possible that these packets are MPEG?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-rtp" rel="tag" title="see questions tagged &#39;rtp&#39;">rtp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Jul '17, 11:58</strong></p><img src="https://secure.gravatar.com/avatar/0b6bdfea45d7093830a2a0638a758239?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hhw&#39;s gravatar image" /><p><span>hhw</span><br />
<span class="score" title="10 reputation points">10</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hhw has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>15 Jul '17, 12:12</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-62811" class="comments-container"></div><div id="comment-tools-62811" class="comment-tools"></div><div class="clear"></div><div id="comment-62811-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="62813"></span>

<div id="answer-container-62813" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62813-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62813-score" class="post-score" title="current number of votes">0</div><span id="post-62813-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you have just the RTP stream with no SDP describing it, you can guess about media type (audio, video, image) and codec only by bandwidth, regularity of packet timing and size, and the contents of the payload.</p><p>Other than that, are you sure the 0x000001b2 is part of the payload, can't it be the SSRC which directly precedes it?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jul '17, 12:16</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>15 Jul '17, 12:28</strong> </span></p></div></div><div id="comments-container-62813" class="comments-container"></div><div id="comment-tools-62813" class="comment-tools"></div><div class="clear"></div><div id="comment-62813-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

