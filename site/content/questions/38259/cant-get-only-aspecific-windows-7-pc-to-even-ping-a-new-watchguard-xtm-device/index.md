+++
type = "question"
title = "Can’t get only aspecific Windows 7 PC to even ping a new WatchGuard XTM device"
description = '''Hello experts, I need help troubleshooting an issue I never ever had before. I can’t get only a specific Windows 7 PC to reach a new WatchGuard XTM device. Currently it is statically-configured using a temporary IP address 192.168.1.2/24. The old WatchGuard Firebox X Edge is configured using IP addr...'''
date = "2014-12-01T10:30:00Z"
lastmod = "2014-12-01T17:21:00Z"
weight = 38259
keywords = [ "arp", "windows", "icmp", "ping" ]
aliases = [ "/questions/38259" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Can’t get only aspecific Windows 7 PC to even ping a new WatchGuard XTM device](/questions/38259/cant-get-only-aspecific-windows-7-pc-to-even-ping-a-new-watchguard-xtm-device)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38259-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38259-score" class="post-score" title="current number of votes">0</div><span id="post-38259-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello experts,</p><p>I need help troubleshooting an issue I never ever had before.</p><p>I can’t get only a specific Windows 7 PC to reach a new WatchGuard XTM device. Currently it is statically-configured using a temporary IP address 192.168.1.2/24. The old WatchGuard Firebox X Edge is configured using IP address 192.168.1.1/24.</p><p>For the love of god, I can’t get only that specific Windows 7 PC to even ping the new WatchGuard XTM device using the temporary IP address 192.168.1.2/24. Apart from this issue, everything is working just fine. Believe me, we have tried almost everything to figure out this issue and no luck.</p><p>From within the new WatchGuard XTM device, you downloaded a packet capture file to help us diagnose the problem. When sending out a continuous ping from another computer on the same network (using IP address 192.168.1.252/24), the packet capture file downloaded from the new WatchGuard XTM device shows ARP Requests from host 192.168.1.252 and ARP Replies from host 192.168.1.2 as we would normally expect. When sending out a continuous ping from the affected computer (using IP address 192.168.1.114/24 or another IP address on the same network), however the packet capture file downloaded from the new WatchGuard XTM device does not even show any ARP Request from host 192.168.1.114 (or whatever) and, as a result, no ARP Replies from host 192.168.1.2 as we would normally expect.</p><p>Even more strange, all packet capture files downloaded from the new WatchGuard XTM device are quite large (several hundred MB) as we would normally expect, while packet capture files generated from within the affected computer are very small (less 30 KB // 254 packets captured with no capture filter).</p><p>Any help would be greatly appreciated.</p><p>Thanks and Regards,</p><p>Massimiliano</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-arp" rel="tag" title="see questions tagged &#39;arp&#39;">arp</span> <span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-icmp" rel="tag" title="see questions tagged &#39;icmp&#39;">icmp</span> <span class="post-tag tag-link-ping" rel="tag" title="see questions tagged &#39;ping&#39;">ping</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Dec '14, 10:30</strong></p><img src="https://secure.gravatar.com/avatar/12c253b33e00ccf9922ea29923370000?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrizzi2&#39;s gravatar image" /><p><span>mrizzi2</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrizzi2 has no accepted answers">0%</span></p></div></div><div id="comments-container-38259" class="comments-container"></div><div id="comment-tools-38259" class="comment-tools"></div><div class="clear"></div><div id="comment-38259-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38268"></span>

<div id="answer-container-38268" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38268-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38268-score" class="post-score" title="current number of votes">0</div><span id="post-38268-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>the new WatchGuard XTM device does not even show any ARP Request from host 192.168.1.114 (or whatever) and, as a result, no ARP Replies from host 192.168.1.2</p></blockquote><p>One possible reason for that behaviour could be a static ARP entry on your PC (192.168.1.114) for 192.168.1.2, for whatever reason. Please check that.</p><p>What do you get, if you run the following command:</p><blockquote><p>arp -a | find "192.168.1.2"</p></blockquote><p>Another option would be: 192.168.1.2 is configured as an additional IP address on the Windows PC, possibly on a different (removable) network adapter. What do you get if you run the following commands:</p><blockquote><p>route print | find "192.168.1.2"</p></blockquote><p>and</p><blockquote><p>ifconfig -a | find "192.168.1.2"</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Dec '14, 17:21</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-38268" class="comments-container"></div><div id="comment-tools-38268" class="comment-tools"></div><div class="clear"></div><div id="comment-38268-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

