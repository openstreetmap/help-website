+++
type = "question"
title = "mysterious IP address"
description = '''Hi I really need some advice , my firewall is blocking the following 192.168.211.178 which is sending from within my network a udp packet. The address cannot be ping and is not registered in my DNS, running wireshark i only see a repeating udp packet from this address every 30 seconds. Also the UDP ...'''
date = "2013-03-09T17:24:00Z"
lastmod = "2013-03-09T18:22:00Z"
weight = 19331
keywords = [ "ip" ]
aliases = [ "/questions/19331" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [mysterious IP address](/questions/19331/mysterious-ip-address)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19331-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19331-score" class="post-score" title="current number of votes">0</div><span id="post-19331-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>I really need some advice , my firewall is blocking the following 192.168.211.178 which is sending from within my network a udp packet. The address cannot be ping and is not registered in my DNS, running wireshark i only see a repeating udp packet from this address every 30 seconds. Also the UDP packet source port is 1111, the mac address is from tyancomp these are the only types of packets from this mac address or IP. I need advice to find thsi machine or possible virus, anybody else seen this type of behavior?</p><p>thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ip" rel="tag" title="see questions tagged &#39;ip&#39;">ip</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Mar '13, 17:24</strong></p><img src="https://secure.gravatar.com/avatar/f05edb811870fa6efc8c6bc872f79384?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hoyt&#39;s gravatar image" /><p><span>hoyt</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hoyt has no accepted answers">0%</span></p></div></div><div id="comments-container-19331" class="comments-container"></div><div id="comment-tools-19331" class="comment-tools"></div><div class="clear"></div><div id="comment-19331-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="19332"></span>

<div id="answer-container-19332" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19332-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19332-score" class="post-score" title="current number of votes">2</div><span id="post-19332-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Usually, you'd track down the physical box by looking at the MAC address tables of your switches to see to which port the MAC you saw is connected to. If you find a port that has multiple MAC addresses you might need to go to the next switch that is connected to that port (if there is another switch; it could just be multiple virtual machine MAC addresses on one port as well).</p><p>Unfortunately not all switches have this functionality, especially not the devices intended for use at home.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Mar '13, 17:30</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-19332" class="comments-container"><span id="19333"></span><div id="comment-19333" class="comment"><div id="post-19333-score" class="comment-score"></div><div class="comment-text"><p>Okay 40 switches will take time to go through,but can be done, but i still do not understand why the only packets associated with this MAC address are these UDP port 1111 packets a linux or windows box generates more than that usually.</p></div><div id="comment-19333-info" class="comment-info"><span class="comment-age">(09 Mar '13, 18:00)</span> <span class="comment-user userinfo">hoyt</span></div></div><span id="19334"></span><div id="comment-19334" class="comment"><div id="post-19334-score" class="comment-score"></div><div class="comment-text"><p>It should be enough to start at the switch where you captured, and work yourself towards the MAC from there. No need to look at all 40 switches, at least it's highly unlikely.</p><p>As soon as you have found the box you can capture everything it does, and also (after having physical access to it) find out what process is using this UDP port, and for what.</p></div><div id="comment-19334-info" class="comment-info"><span class="comment-age">(09 Mar '13, 18:22)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-19332" class="comment-tools"></div><div class="clear"></div><div id="comment-19332-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

