+++
type = "question"
title = "Monitor UDP"
description = '''How do I setup wireshark to monitor UDP port 514 from a IP phone?'''
date = "2013-12-16T07:20:00Z"
lastmod = "2013-12-16T07:44:00Z"
weight = 28159
keywords = [ "udp" ]
aliases = [ "/questions/28159" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Monitor UDP](/questions/28159/monitor-udp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28159-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28159-score" class="post-score" title="current number of votes">0</div><span id="post-28159-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How do I setup wireshark to monitor UDP port 514 from a IP phone?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-udp" rel="tag" title="see questions tagged &#39;udp&#39;">udp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Dec '13, 07:20</strong></p><img src="https://secure.gravatar.com/avatar/b82d462d0ba39ca2db872ec04da07caa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tpodlak&#39;s gravatar image" /><p><span>tpodlak</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tpodlak has no accepted answers">0%</span></p></div></div><div id="comments-container-28159" class="comments-container"></div><div id="comment-tools-28159" class="comment-tools"></div><div class="clear"></div><div id="comment-28159-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="28160"></span>

<div id="answer-container-28160" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28160-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28160-score" class="post-score" title="current number of votes">0</div><span id="post-28160-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Assuming the IP phone is connected to a switch, you need to configure a monitor port that will copy all traffic from the port of the IP phone to a port on which you have connected your system with wireshark. Then you can see all traffic from the phone or you can use the capture filter "udp port 514" to only see the syslog data.</p><p>If the frames are vlan tagged, then you can use the capture filter "vlan and udp port 514" instead :-)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Dec '13, 07:44</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-28160" class="comments-container"></div><div id="comment-tools-28160" class="comment-tools"></div><div class="clear"></div><div id="comment-28160-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

