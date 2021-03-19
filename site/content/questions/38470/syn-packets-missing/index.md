+++
type = "question"
title = "SYN Packets Missing"
description = '''Hi, I&#x27;m using WS v1.10.11. When viewing a pcapng file after the capture has stopped, I&#x27;m noticing no initial SYN packets. I can see the SYN/ACK packets but no SYN packets. If I save the capture and view the pcapng on another system (same WS version), the SYN packets are not present, so it seems that...'''
date = "2014-12-09T03:00:00Z"
lastmod = "2014-12-30T05:44:00Z"
weight = 38470
keywords = [ "syn", "missing_packets" ]
aliases = [ "/questions/38470" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [SYN Packets Missing](/questions/38470/syn-packets-missing)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38470-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38470-score" class="post-score" title="current number of votes">0</div><span id="post-38470-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I'm using WS v1.10.11. When viewing a pcapng file after the capture has stopped, I'm noticing no initial SYN packets. I can see the SYN/ACK packets but no SYN packets.</p><p>If I save the capture and view the pcapng on another system (same WS version), the SYN packets are <em>not</em> present, so it seems that the SYN packets are not being captured on the first system.</p><p>I've tried uninstalling/reinstalling WS, reinstall the NIC drivers (updated as well), and uninstalled/reinstalled WinPcap (v4.1.3), yet the result is the same.</p><p>thanks, J</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-syn" rel="tag" title="see questions tagged &#39;syn&#39;">syn</span> <span class="post-tag tag-link-missing_packets" rel="tag" title="see questions tagged &#39;missing_packets&#39;">missing_packets</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Dec '14, 03:00</strong></p><img src="https://secure.gravatar.com/avatar/791c3a844bb1629d3a685adab364e2d1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JTech_17&#39;s gravatar image" /><p><span>JTech_17</span><br />
<span class="score" title="41 reputation points">41</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JTech_17 has no accepted answers">0%</span></p></div></div><div id="comments-container-38470" class="comments-container"></div><div id="comment-tools-38470" class="comment-tools"></div><div class="clear"></div><div id="comment-38470-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="38472"></span>

<div id="answer-container-38472" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38472-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38472-score" class="post-score" title="current number of votes">0</div><span id="post-38472-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>What OS? If on Windows are you missing all packets in the SYN direction? If so then it might be due to av/firewall/endpoint protection software.</p><p>Note that 1.10.11 is somewhat old, the stable version is currently 1.12.2.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Dec '14, 03:31</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-38472" class="comments-container"><span id="38478"></span><div id="comment-38478" class="comment"><div id="post-38478-score" class="comment-score"></div><div class="comment-text"><p>Win7 Ent. I've disabled the fw and AV - same result. The second system is identical in hardware and OS with no issue. It may simply be a bad Win7 image. Thought I'd ask and see if there was a simple fix before starting from scratch and re-imaging. thx, J</p></div><div id="comment-38478-info" class="comment-info"><span class="comment-age">(09 Dec '14, 05:40)</span> <span class="comment-user userinfo">JTech_17</span></div></div><span id="38479"></span><div id="comment-38479" class="comment"><div id="post-38479-score" class="comment-score"></div><div class="comment-text"><p>You didn't say if all packets in the SYN direction are missing, or just the SYN.</p><p>As you suggest I also believe that the issue is during capture, thus viewing the capture file on a second system is unlikely to change the result. If you can capture the SYN on the second system though that does suggest an issue with the first. Disabling AV etc. may not be enough, you might have to remove them completely.</p></div><div id="comment-38479-info" class="comment-info"><span class="comment-age">(09 Dec '14, 05:44)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-38472" class="comment-tools"></div><div class="clear"></div><div id="comment-38472-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="38794"></span>

<div id="answer-container-38794" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38794-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38794-score" class="post-score" title="current number of votes">0</div><span id="post-38794-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>To resolve my particular issue, I had the workstation re-imaged. Installed my initial version 1.10.11 and WS is working well; SYN packets are being seen (as well as all other packets). AV is on, Win firewall is on, all of my apps re-installed, and the system is operating like my secondary workstation.</p><p>It's a tough step but in my case it was an option since it is standard procedure to backup apps and data on the corporate back end. I wouldn't recommend this if you don't have a proper backup.</p><p>J</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Dec '14, 05:44</strong></p><img src="https://secure.gravatar.com/avatar/791c3a844bb1629d3a685adab364e2d1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JTech_17&#39;s gravatar image" /><p><span>JTech_17</span><br />
<span class="score" title="41 reputation points">41</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JTech_17 has no accepted answers">0%</span></p></div></div><div id="comments-container-38794" class="comments-container"></div><div id="comment-tools-38794" class="comment-tools"></div><div class="clear"></div><div id="comment-38794-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

