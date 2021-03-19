+++
type = "question"
title = "How do you get wireshark to scan all subnets in windows?"
description = '''I&#x27;m a bit of a layman with this, so I apologize if I&#x27;m using the wrong terms. Say I have a device that has an IP in it and has no method to reset. I have no idea what the IP/subnet/gateway might be. I have seen wireshark on a Linux machine find the IP of a device like this but in Windows I have only...'''
date = "2012-02-20T11:10:00Z"
lastmod = "2012-02-23T09:37:00Z"
weight = 9144
keywords = [ "windows", "ip", "lost", "subnet" ]
aliases = [ "/questions/9144" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How do you get wireshark to scan all subnets in windows?](/questions/9144/how-do-you-get-wireshark-to-scan-all-subnets-in-windows)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9144-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9144-score" class="post-score" title="current number of votes">0</div><span id="post-9144-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm a bit of a layman with this, so I apologize if I'm using the wrong terms. Say I have a device that has an IP in it and has no method to reset. I have no idea what the IP/subnet/gateway might be. I have seen wireshark on a Linux machine find the IP of a device like this but in Windows I have only been able to find it if I know the IP range it is in 10.X, 192.x etc.<br />
</p><p>If my adapter is not set to an IP in the same range as the device, wireshark will not see any requests from the device. Is this a limitation of windows or is there something else I can try? I've tried but XP Pro SP3 and W7 Ultimate.<br />
</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-ip" rel="tag" title="see questions tagged &#39;ip&#39;">ip</span> <span class="post-tag tag-link-lost" rel="tag" title="see questions tagged &#39;lost&#39;">lost</span> <span class="post-tag tag-link-subnet" rel="tag" title="see questions tagged &#39;subnet&#39;">subnet</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Feb '12, 11:10</strong></p><img src="https://secure.gravatar.com/avatar/bd6e01c0e5ca4140c3b447540212f2d1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wirelark&#39;s gravatar image" /><p><span>wirelark</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wirelark has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-9144" class="comments-container"></div><div id="comment-tools-9144" class="comment-tools"></div><div class="clear"></div><div id="comment-9144-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9146"></span>

<div id="answer-container-9146" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9146-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9146-score" class="post-score" title="current number of votes">1</div><span id="post-9146-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark can only capture packets that "pass through" the interface you are capturing on. Wireshark displays the packets that are captured, only you can determine if those packets belong to your mysterious device as there is nothing in Wireshark to "find" an IP, it only displays them. If you have some means to generate traffic to your device, and that traffic is present on the capturing interface then you should see the packets in Wireshark.</p><p>The packets that are captured depend on your network interface, whether you have promiscuous mode enabled (and whether the interface supports it) and what the interface is connected to (a hub, switch or router).</p><p>Have a look at the <a href="http://wiki.wireshark.org/CaptureSetup">Capture Setup</a> page on the Wiki for more information on capturing.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Feb '12, 12:05</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-9146" class="comments-container"><span id="9184"></span><div id="comment-9184" class="comment"><div id="post-9184-score" class="comment-score"></div><div class="comment-text"><p>I have just been using it to show me the ip broadcast when I first power the device but that only works if my network interface is set to the correct range. I usually know the mac address so it's easy to filter out. It sounds like I need to enable promiscuous mode or find a different network adapter.</p></div><div id="comment-9184-info" class="comment-info"><span class="comment-age">(23 Feb '12, 08:56)</span> <span class="comment-user userinfo">wirelark</span></div></div><span id="9185"></span><div id="comment-9185" class="comment"><div id="post-9185-score" class="comment-score"></div><div class="comment-text"><p>What type of network interface is it? There are plenty of problems with WiFi ones on Windows, but I've not heard of a wired one that won't go into promiscuous mode.</p></div><div id="comment-9185-info" class="comment-info"><span class="comment-age">(23 Feb '12, 09:37)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-9146" class="comment-tools"></div><div class="clear"></div><div id="comment-9146-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

