+++
type = "question"
title = "Monitor Ethernet though serial ports RS232 or USB"
description = '''How I can monitor Ethernet&#x27;s packets through a &quot;null modem of ethernet interface&quot; or connection direct (in a serial port RS232 or USB) with WireShark.'''
date = "2012-02-08T16:49:00Z"
lastmod = "2012-02-08T20:29:00Z"
weight = 8912
keywords = [ "ethernet", "rs232", "monitor", "usb" ]
aliases = [ "/questions/8912" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Monitor Ethernet though serial ports RS232 or USB](/questions/8912/monitor-ethernet-though-serial-ports-rs232-or-usb)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8912-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8912-score" class="post-score" title="current number of votes">0</div><span id="post-8912-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How I can monitor Ethernet's packets through a "null modem of ethernet interface" or connection direct (in a serial port RS232 or USB) with WireShark.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ethernet" rel="tag" title="see questions tagged &#39;ethernet&#39;">ethernet</span> <span class="post-tag tag-link-rs232" rel="tag" title="see questions tagged &#39;rs232&#39;">rs232</span> <span class="post-tag tag-link-monitor" rel="tag" title="see questions tagged &#39;monitor&#39;">monitor</span> <span class="post-tag tag-link-usb" rel="tag" title="see questions tagged &#39;usb&#39;">usb</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Feb '12, 16:49</strong></p><img src="https://secure.gravatar.com/avatar/1602793d84169e0a19af1fd5e6657902?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Walter&#39;s gravatar image" /><p><span>Walter</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Walter has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>28 Feb '12, 19:49</strong> </span></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-8912" class="comments-container"></div><div id="comment-tools-8912" class="comment-tools"></div><div class="clear"></div><div id="comment-8912-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8914"></span>

<div id="answer-container-8914" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8914-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8914-score" class="post-score" title="current number of votes">0</div><span id="post-8914-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Well, to do it with an RS-232 device, the first step would be to get an RS-232 serial port that runs at the same speed as your Ethernet. That's not likely to happen - I know of no RS-232 ports that can run at 10 megabits/second, much less the speed of modern Ethernets - so, unless the Ethernet has next to no traffic on it, even if somebody were to make a device that transfers Ethernet packets over an RS-232 interface, it wouldn't be able to capture most of the traffic on the Ethernet.</p><p>To do it with a USB device, get a USB Ethernet interface, plug it into the Ethernet in question, and capture on that interface. This is no different from capturing on any other type of Ethernet interface; see <a href="http://wiki.wireshark.org/CaptureSetup/Ethernet">the Wireshark Wiki page on Ethernet traffic capture</a> for information, including information about capturing on switched networks (which is more difficult than capturing on non-switched networks).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Feb '12, 20:29</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-8914" class="comments-container"></div><div id="comment-tools-8914" class="comment-tools"></div><div class="clear"></div><div id="comment-8914-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

