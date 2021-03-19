+++
type = "question"
title = "Bridging on a raspberry Pi, previous not seen and freezing after a while"
description = '''Hi People, I assume this is just a limitation of the Pi, but I thought I&#x27;d ask anyway. I have added a TeckNet USB Ethernet Adapter to my Pi. I have set up a bridge with the first card and it works fine. I can Start tshark on bri0 and that goes great. I am connecting the the Pi with Putty and running...'''
date = "2014-11-02T05:10:00Z"
lastmod = "2014-11-06T00:23:00Z"
weight = 37538
keywords = [ "bridge", "raspberry" ]
aliases = [ "/questions/37538" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Bridging on a raspberry Pi, previous not seen and freezing after a while](/questions/37538/bridging-on-a-raspberry-pi-previous-not-seen-and-freezing-after-a-while)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37538-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37538-score" class="post-score" title="current number of votes">0</div><span id="post-37538-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi People,</p><p>I assume this is just a limitation of the Pi, but I thought I'd ask anyway.</p><p>I have added a TeckNet USB Ethernet Adapter to my Pi. I have set up a bridge with the first card and it works fine. I can Start tshark on bri0 and that goes great. I am connecting the the Pi with Putty and running tshark with a "host IP not broadcast and not multicast"filter.</p><p>After around 4 or 5 minutes however the bridge freezes up, the laptop I am sending over the bridge loses connection and 2 seconds later the Pi freezes and requires a hard reset.</p><p>If I do this without Putty, it goes longer, but freezes anyway. Has anyone else got this working long term? I have already stopped X from loading to save memory. Raspian is the OS, it does not matter whether I output to file or just to console. I am just trying to make an affordable inline box to cut before printers, lan shares and the like.</p><p>I am not noticing any untoward usage of memory, so I am thinking something else is leaking..</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-bridge" rel="tag" title="see questions tagged &#39;bridge&#39;">bridge</span> <span class="post-tag tag-link-raspberry" rel="tag" title="see questions tagged &#39;raspberry&#39;">raspberry</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Nov '14, 05:10</strong></p><img src="https://secure.gravatar.com/avatar/05ba95262a3352e3af4ba69c0ec0dff2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DarrenWright&#39;s gravatar image" /><p><span>DarrenWright</span><br />
<span class="score" title="216 reputation points">216</span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DarrenWright has 5 accepted answers">26%</span></p></div></div><div id="comments-container-37538" class="comments-container"></div><div id="comment-tools-37538" class="comment-tools"></div><div class="clear"></div><div id="comment-37538-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37539"></span>

<div id="answer-container-37539" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37539-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37539-score" class="post-score" title="current number of votes">0</div><span id="post-37539-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="DarrenWright has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I have added a TeckNet USB Ethernet Adapter to my Pi.<br />
...<br />
2 seconds later the Pi freezes and requires a hard reset.<br />
</p></blockquote><p>sounds like a kernel freeze, either due to hardware or software (driver) problems. You should try to nail down the problem by eliminating possible trouble sources:</p><p>Use a different USB Ethernet adapter. If the system still freezes, it's rather likely that there is a problem with the Pi hardware or the kernel/drivers. In that case, try a different kernel.</p><p>BTW: Does that happen if you are <strong>not running</strong> tshark/tcpdump on the bridge interface?</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Nov '14, 05:56</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-37539" class="comments-container"><span id="37547"></span><div id="comment-37547" class="comment"><div id="post-37547-score" class="comment-score"></div><div class="comment-text"><p>so, I just ran it through for 5 Hours straight without tshark, just with the bridge active and doing random things every now and then. works fine, connected using eth0; I have also tshark running direct on the Pi NIC (bridge disabled and usb card gone) also no problems. Looks like it really could be a driver problem. I'll enable debugging later on maybe.</p><p>It's also only got the standard wireshark / tshark installs from the repository. I'll see if ther is something newer available.</p><p>Edit: Added card info (eth0 Pi interface / eth1 usb Interface)</p></div><div id="comment-37547-info" class="comment-info"><span class="comment-age">(02 Nov '14, 13:25)</span> <span class="comment-user userinfo">DarrenWright</span></div></div><span id="37604"></span><div id="comment-37604" class="comment"><div id="post-37604-score" class="comment-score"></div><div class="comment-text"><p>WIll look further at the driver setup for Raspian. I have connected the adapter to a laptop running Ubuntu 14.04 and setup the same bridge. It works fine there.</p><p>I will mark Kurts as correct answer, not sure if itt is kernel though. probably more the driver itself.</p></div><div id="comment-37604-info" class="comment-info"><span class="comment-age">(06 Nov '14, 00:23)</span> <span class="comment-user userinfo">DarrenWright</span></div></div></div><div id="comment-tools-37539" class="comment-tools"></div><div class="clear"></div><div id="comment-37539-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

