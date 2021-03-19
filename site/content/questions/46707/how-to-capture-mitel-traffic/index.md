+++
type = "question"
title = "How to capture Mitel traffic"
description = '''I&#x27;m new to wireshark. I installed wireshark. I started running captures but I&#x27;m not seeing anything that looks like Mitel phone traffic. I&#x27;m looking for UDP or RTP traffic.  Should I see the IP addresses of the phones in the capture? Are there special settings in Wireshark to capture Mitel phone tra...'''
date = "2015-10-19T12:30:00Z"
lastmod = "2015-10-28T14:47:00Z"
weight = 46707
keywords = [ "mitel" ]
aliases = [ "/questions/46707" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [How to capture Mitel traffic](/questions/46707/how-to-capture-mitel-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46707-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46707-score" class="post-score" title="current number of votes">0</div><span id="post-46707-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm new to wireshark. I installed wireshark. I started running captures but I'm not seeing anything that looks like Mitel phone traffic. I'm looking for UDP or RTP traffic.<br />
</p><p>Should I see the IP addresses of the phones in the capture?</p><p>Are there special settings in Wireshark to capture Mitel phone traffic?</p><p>Thanks,</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-mitel" rel="tag" title="see questions tagged &#39;mitel&#39;">mitel</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Oct '15, 12:30</strong></p><img src="https://secure.gravatar.com/avatar/1160d201b39e5284b4730e159da17e88?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Carl&#39;s gravatar image" /><p><span>Carl</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Carl has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-46707" class="comments-container"></div><div id="comment-tools-46707" class="comment-tools"></div><div class="clear"></div><div id="comment-46707-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="46713"></span>

<div id="answer-container-46713" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46713-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46713-score" class="post-score" title="current number of votes">0</div><span id="post-46713-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It all depends on what signalling protocol these Mitel devices use. Is it proprietary, it's probably not dissected. Is it one of (check Wireshark <a href="https://wiki.wireshark.org/VoIP_calls">wiki for VoIP calls</a>) known protocols then it will. Otherwise go into the RTP protocol dissector preferences and tick 'Try to dissect RTP outside of conversations'. This will dissect eligible UDP packets as RTP.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Oct '15, 13:30</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>20 Oct '15, 08:11</strong> </span></p></div></div><div id="comments-container-46713" class="comments-container"></div><div id="comment-tools-46713" class="comment-tools"></div><div class="clear"></div><div id="comment-46713-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="46754"></span>

<div id="answer-container-46754" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46754-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46754-score" class="post-score" title="current number of votes">0</div><span id="post-46754-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Yes you will see IP Addresses....</p><p>Are your phones on a different subnet? you could filter on that subnet? something like;</p><p>ip.addr == 192.168.10.0/24 (subnet for mitel phones)</p><p>Mitel should also mark with DSCP value of ef, so you could filter by that;</p><p>ip.dsfield == 184</p><p>Regards</p><p>Warren</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Oct '15, 05:19</strong></p><img src="https://secure.gravatar.com/avatar/4488347a0278bd48c6afc5cb5413d31f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Warren%20Sullivan&#39;s gravatar image" /><p><span>Warren Sullivan</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Warren Sullivan has no accepted answers">0%</span></p></div></div><div id="comments-container-46754" class="comments-container"></div><div id="comment-tools-46754" class="comment-tools"></div><div class="clear"></div><div id="comment-46754-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="47038"></span>

<div id="answer-container-47038" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47038-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47038-score" class="post-score" title="current number of votes">0</div><span id="post-47038-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I dare to ask... are you sure the traffic to/from the phones gets "somehow" to the Ethernet interface on which you capture? I.e. does the traffic flow through the machine on which you run the wireshark, or have you configured a span port on the switch through which the phones' traffic is running and connected it to the machine?</p><p>Regards,</p><p>Pavel</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Oct '15, 14:47</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>28 Oct '15, 14:47</strong> </span></p></div></div><div id="comments-container-47038" class="comments-container"></div><div id="comment-tools-47038" class="comment-tools"></div><div class="clear"></div><div id="comment-47038-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

