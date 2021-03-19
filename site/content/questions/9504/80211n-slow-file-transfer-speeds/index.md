+++
type = "question"
title = "802.11n slow file transfer speeds"
description = '''So hoping to get some input on this, a solution even. I&#x27;m experiencing slow file transfer speeds (56Mb/s) from my wireless laptop to a wired (Gigabit) server. I&#x27;ve tried on another computer and it&#x27;s faster (80Mb/s) but still not where I&#x27;d expect with 802.11N. Setup:  - WNDR3700 Netgear router, dualb...'''
date = "2012-03-12T22:30:00Z"
lastmod = "2013-03-20T10:44:00Z"
weight = 9504
keywords = [ "speed", "wlan", "802.11n" ]
aliases = [ "/questions/9504" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [802.11n slow file transfer speeds](/questions/9504/80211n-slow-file-transfer-speeds)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9504-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9504-score" class="post-score" title="current number of votes">0</div><span id="post-9504-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>So hoping to get some input on this, a solution even. I'm experiencing slow file transfer speeds (56Mb/s) from my wireless laptop to a wired (Gigabit) server. I've tried on another computer and it's faster (80Mb/s) but still not where I'd expect with 802.11N.</p><p>Setup: - WNDR3700 Netgear router, dualband, 2.4GHz is b/g (using WEP), 5GHz is n (using WPA AES). Different SSIDs for the two bands. - Windows 7 laptop with an Intel WiFi Link 5100 AGN, connected to the router at n/5GHz. - Windows 7 desktop with a Dell Wireless 1520 N, connected to the router at n/5GHz. - Windows Home Server, wired to the router with gigabit cable (cat6).</p><p>I've tested using LAN Speed test and just writing a file, getting around 50-60Mb/s or ~7MB/s. Considering the router is marketed as 300Mb/s I'm expecting something better than 60Mb/s. If I understand correctly the max I'd hit is 150Mb/s? I've been searching online for a few hours trying various things but I'm not getting anywhere. I'd think I should be able to at least match the 80Mb/s I'm getting from the desktop. But ideally I'd like them both to be better.</p><p>Any advice is appreciated. Thanks in advance.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-speed" rel="tag" title="see questions tagged &#39;speed&#39;">speed</span> <span class="post-tag tag-link-wlan" rel="tag" title="see questions tagged &#39;wlan&#39;">wlan</span> <span class="post-tag tag-link-802.11n" rel="tag" title="see questions tagged &#39;802.11n&#39;">802.11n</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Mar '12, 22:30</strong></p><img src="https://secure.gravatar.com/avatar/3e52132436a8ee63b9754f46c008da01?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chemnerd&#39;s gravatar image" /><p><span>chemnerd</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chemnerd has no accepted answers">0%</span></p></div></div><div id="comments-container-9504" class="comments-container"></div><div id="comment-tools-9504" class="comment-tools"></div><div class="clear"></div><div id="comment-9504-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="9532"></span>

<div id="answer-container-9532" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9532-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9532-score" class="post-score" title="current number of votes">0</div><span id="post-9532-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>One thing you must never forget is the pure fact that wireless networks are prone to interference and collisions. Imagine your AP as a Hub, <em>not</em> as a switch. So just by having two devices associated, both of them <em>share</em> available bandwidth. In b/g networks you could say that as a rule of thumb if everything works perfect, you get around 50% of the "available" bandwidth when testing, which was around 22-26 MBits at "54MBit" 802.11g networks. Now there are numerous myths about what you can get out of 802.11n, but I personally wouldn't even think of effectively getting 150MBit would be a default for home equipment.</p><p>One thing you can do to compare your Laptop and Desktop PC is check for the number of antennas. If I'm not totally wrong, 802.11n only reaches max speeds with 3x3 antennas, MIMO and packet bundling, if both sides agree on that. Most notebooks are shipped with 2x2 wireless NICs, reducing the throughput a little. But like said, don't expect miracles there - 50 to 80 MBits is not too bad from my perspective.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Mar '12, 03:27</strong></p><img src="https://secure.gravatar.com/avatar/36b41326bff63eb5ad73a0436914e05c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Landi&#39;s gravatar image" /><p><span>Landi</span><br />
<span class="score" title="2269 reputation points"><span>2.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Landi has 28 accepted answers">28%</span></p></div></div><div id="comments-container-9532" class="comments-container"></div><div id="comment-tools-9532" class="comment-tools"></div><div class="clear"></div><div id="comment-9532-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="19690"></span>

<div id="answer-container-19690" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19690-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19690-score" class="post-score" title="current number of votes">0</div><span id="post-19690-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>A few other things to remember in particular about 802.11N is that in order to obtain the highest thruput bandwidth, there needs to be MIMO (Multiple Input Multiple Output)type antennas on both ends of the radio link. When this is the case and the radio environment supports the use of multiple data streams is when you get the higher thruput/bandwidth. If you have individual antennas which are pointing in different directions, then multiple streams is not really an option unless the RF signals happen to bounce back to the far end MIMO antenna.</p><p>In addition the signal strength and signal to noise ratio needs to be very good. If other non 802.11N (ie. 802.11 a,b,g) access points are operating in the same area &amp; possible sharing the same channel being used (2.4/5.8 GHz) then contention for the channel can occur with the resulting drop in thruput,increase in noise level which reduces the signal to noise ratio, increases response times/latency, dropped radio links and reacquiring access points.</p><p>There may also be the issue of wether or not you are using a 40 MHz wide N channel vs 20 MHz wide non 802.11N channels and where the overlap is happening between the two. This is worse on 2.4 Ghz as the number of avaiable non-overlapping channels is only 3 (Ch 1, 6 and 11).</p><p>Hope this helps you.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Mar '13, 10:44</strong></p><img src="https://secure.gravatar.com/avatar/d484352f1ec05e7d8cfa9fa05c0fea89?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Radionick&#39;s gravatar image" /><p><span>Radionick</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Radionick has no accepted answers">0%</span></p></div></div><div id="comments-container-19690" class="comments-container"></div><div id="comment-tools-19690" class="comment-tools"></div><div class="clear"></div><div id="comment-19690-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

