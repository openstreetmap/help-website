+++
type = "question"
title = "how do i capture all traffic on a switch"
description = '''I am trying to capture all traffic passing through a switch but i got only my traffic with the switch not other devices traffic though the port i used is configured as VLAN with other computers. Our instructor told us it is a WireShark setting issue, how do i change the setting to capture all traffi...'''
date = "2013-04-11T04:47:00Z"
lastmod = "2013-04-12T05:00:00Z"
weight = 20328
keywords = [ "capture", "all", "traffic", "switch" ]
aliases = [ "/questions/20328" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [how do i capture all traffic on a switch](/questions/20328/how-do-i-capture-all-traffic-on-a-switch)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20328-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20328-score" class="post-score" title="current number of votes">0</div><span id="post-20328-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to capture all traffic passing through a switch but i got only my traffic with the switch not other devices traffic though the port i used is configured as VLAN with other computers. Our instructor told us it is a WireShark setting issue, how do i change the setting to capture all traffic on that switch ???</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-all" rel="tag" title="see questions tagged &#39;all&#39;">all</span> <span class="post-tag tag-link-traffic" rel="tag" title="see questions tagged &#39;traffic&#39;">traffic</span> <span class="post-tag tag-link-switch" rel="tag" title="see questions tagged &#39;switch&#39;">switch</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Apr '13, 04:47</strong></p><img src="https://secure.gravatar.com/avatar/583b809745fa45690fa8b950c5d28714?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ashraf&#39;s gravatar image" /><p><span>Ashraf</span><br />
<span class="score" title="16 reputation points">16</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ashraf has no accepted answers">0%</span></p></div></div><div id="comments-container-20328" class="comments-container"></div><div id="comment-tools-20328" class="comment-tools"></div><div class="clear"></div><div id="comment-20328-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="20333"></span>

<div id="answer-container-20333" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20333-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20333-score" class="post-score" title="current number of votes">4</div><span id="post-20333-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Ashraf has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I am trying to capture all traffic passing through a switch but i got only my traffic with the switch not other devices traffic</p></blockquote><p>A switch will never forward 'other' traffic (traffic that is not directed to your ethernet mac address + broadcast) to your port unless you tell it to do so. So, if you did not configure a mirror port on the switch, you will only see this kind of traffic.</p><ul><li>your own traffic</li><li>traffic to multicast and/or broadcast addresses</li></ul><p>Please read the following Wiki article: <a href="http://wiki.wireshark.org/CaptureSetup/Ethernet">http://wiki.wireshark.org/CaptureSetup/Ethernet</a></p><blockquote><p>Our instructor told us it is a WireShark setting issue,</p></blockquote><p>I suggest your instructor reads the article as well ;-) and then this book: <a href="http://www.wiresharkbook.com/">http://www.wiresharkbook.com/</a> ;-))</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Apr '13, 05:55</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-20333" class="comments-container"><span id="20362"></span><div id="comment-20362" class="comment"><div id="post-20362-score" class="comment-score">1</div><div class="comment-text"><p>His or her instructor probably thinks enabling promiscuous mode is sufficient. As you note, the instructor is mistaken, and should read the Wireshark Wiki article in question ("and the novice was enlightened").</p></div><div id="comment-20362-info" class="comment-info"><span class="comment-age">(11 Apr '13, 18:36)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="20368"></span><div id="comment-20368" class="comment"><div id="post-20368-score" class="comment-score"></div><div class="comment-text"><p>So the VLAN don't make a broadcast domain for it's port ??</p></div><div id="comment-20368-info" class="comment-info"><span class="comment-age">(12 Apr '13, 01:16)</span> <span class="comment-user userinfo">Ashraf</span></div></div><span id="20380"></span><div id="comment-20380" class="comment"><div id="post-20380-score" class="comment-score">1</div><div class="comment-text"><p>A VLAN is a <strong>broadcast</strong> domain (or at least it should be - some switches don't take it very serious ;-)). But that does not help to receive <strong>non-broadcast</strong> traffic on a port, other than the traffic that is directed to the mac address of the device on that port.</p></div><div id="comment-20380-info" class="comment-info"><span class="comment-age">(12 Apr '13, 05:00)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-20333" class="comment-tools"></div><div class="clear"></div><div id="comment-20333-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

