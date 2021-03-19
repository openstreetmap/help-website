+++
type = "question"
title = "How do you capture everything except tun0 (openVPN)"
description = '''Hey guys, I need to capture all traffic which is not going through tun0 (openvpn). I have no idea which capture-filter I should use. I hope someone can help me.'''
date = "2015-03-03T13:12:00Z"
lastmod = "2015-03-03T14:20:00Z"
weight = 40227
keywords = [ "capture", "vpn", "tun0" ]
aliases = [ "/questions/40227" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How do you capture everything except tun0 (openVPN)](/questions/40227/how-do-you-capture-everything-except-tun0-openvpn)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40227-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40227-score" class="post-score" title="current number of votes">0</div><span id="post-40227-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey guys, I need to capture all traffic which is not going through tun0 (openvpn). I have no idea which capture-filter I should use. I hope someone can help me.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-vpn" rel="tag" title="see questions tagged &#39;vpn&#39;">vpn</span> <span class="post-tag tag-link-tun0" rel="tag" title="see questions tagged &#39;tun0&#39;">tun0</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Mar '15, 13:12</strong></p><img src="https://secure.gravatar.com/avatar/7673266166fb2d6da24eda66b72cff00?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alexo90&#39;s gravatar image" /><p><span>alexo90</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alexo90 has no accepted answers">0%</span></p></div></div><div id="comments-container-40227" class="comments-container"></div><div id="comment-tools-40227" class="comment-tools"></div><div class="clear"></div><div id="comment-40227-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="40228"></span>

<div id="answer-container-40228" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40228-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40228-score" class="post-score" title="current number of votes">0</div><span id="post-40228-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The OpenVPN traffic usually uses a "real" network card to transport the tunneled data. Default would be on UDP port 1194, so if you capture on your network card you could exclude the tunnel port, e.g. by using "not udp port 1194"</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Mar '15, 13:17</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-40228" class="comments-container"></div><div id="comment-tools-40228" class="comment-tools"></div><div class="clear"></div><div id="comment-40228-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="40230"></span>

<div id="answer-container-40230" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40230-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40230-score" class="post-score" title="current number of votes">0</div><span id="post-40230-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I need to capture all traffic which is not going through tun0 (openvpn).</p></blockquote><p>well, then don't capture on tun0.</p><p>If you need to capture on multiple interfaces, you can use several -i statements. Recent versions of Wireshark/dumpcap/tcpdump do support capturing on multiple interfaces, so you don't have to use '-i any'.</p><p>Another idea is to set a filter on the IP addresses you don't need. Check the routing table to figure out which subnets are being routed to tun0, then use the following capture filter for those networks.</p><blockquote><p>not net 10.x.x.0/24 and not net 10.y.y.0/24 and not ....</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Mar '15, 14:20</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>03 Mar '15, 14:30</strong> </span></p></div></div><div id="comments-container-40230" class="comments-container"></div><div id="comment-tools-40230" class="comment-tools"></div><div class="clear"></div><div id="comment-40230-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

