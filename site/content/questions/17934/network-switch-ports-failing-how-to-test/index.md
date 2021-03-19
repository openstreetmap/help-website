+++
type = "question"
title = "Network switch ports failing - how to test?"
description = '''I have a real odd situation when upgrading the network hardware in our office. I&#x27;m replacing a couple of small unmanaged switches and installing some web managed switches. The network is flat and consists of about 60 windows XP, 7 and 2008 hosts.  The existing switches consists of a TrendNET GB Swit...'''
date = "2013-01-24T07:56:00Z"
lastmod = "2013-01-30T21:30:00Z"
weight = 17934
keywords = [ "failed", "ports" ]
aliases = [ "/questions/17934" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Network switch ports failing - how to test?](/questions/17934/network-switch-ports-failing-how-to-test)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17934-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17934-score" class="post-score" title="current number of votes">0</div><span id="post-17934-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a real odd situation when upgrading the network hardware in our office. I'm replacing a couple of small unmanaged switches and installing some web managed switches. The network is flat and consists of about 60 windows XP, 7 and 2008 hosts.</p><p>The existing switches consists of a TrendNET GB Switch with a uplink to two netgear 10/100 switches. I installed a Dell web managed 48 port GB switch, with an uplink to the Trendnet. After a short time, but sometimes days, the Dell switch will stop passing traffic on a random number of ports. The ports are dispersed around the switch and moving the Ethernet cable to another port will not correct the issue.</p><p>I can only correct it by installing the netgear 10/100 switches back on the trendnet switch and then move the failed connections, 10 maybe sometimes more, to another switch. I've replaced the Dell 3 times. The first time I thought it could be the switch. The second time I tried the switch in both managed mode and unmanaged mode, the third time we updated the firmware on the switch. All three times the situation is the same, after some time ports on the Dell switch will not pass traffic. Some will still continue to operate normally while others do not.</p><p>Now when this happens the client shows its connected but no access, even setting a fixed IP does not help. The ports on the switch appear normal, lights are on and blinking but you cant ping or access any other client on the network. If you move the connection to another switch, it comes up immediately.</p><p>Prior to replacing the 3rd Dell switch I ran WireShark on a laptop connected to the switch. I could not see any traffic that did not seem normal; typical ack, nack, DNS and ARP queries but nothing that stood out as unusual. I recently installed a HP Procurve 1800 GB switch, to replace the Dell, but it soon did the same as the Dell.</p><p>I'm hoping, if you read this far, someone might have a few suggestions as how I might use / connect WireShark in such a way as to help identify the cause of this very unusual behavior.</p><p>Thanks!!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-failed" rel="tag" title="see questions tagged &#39;failed&#39;">failed</span> <span class="post-tag tag-link-ports" rel="tag" title="see questions tagged &#39;ports&#39;">ports</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Jan '13, 07:56</strong></p><img src="https://secure.gravatar.com/avatar/d1209b225027c80b9f7d274baae752a0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mattinnc&#39;s gravatar image" /><p><span>mattinnc</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mattinnc has no accepted answers">0%</span></p></div></div><div id="comments-container-17934" class="comments-container"></div><div id="comment-tools-17934" class="comment-tools"></div><div class="clear"></div><div id="comment-17934-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="17935"></span>

<div id="answer-container-17935" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17935-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17935-score" class="post-score" title="current number of votes">1</div><span id="post-17935-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This has the typical ring to it that usually comes with problems caused by having loops on the network, often related to the Spanning Tree configuration. If you capture on your network, did you see any spanning tree frames? You can filter on them using "stp", and result in BPDU frames showing up. If you do get those - they should show up every 2 seconds (or another regular interval) and they should always be exactly the same. If they're not or if a "topology chance" is flagged you might be in trouble - "might be" because spanning tree frames can also indicate harmless events.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jan '13, 08:37</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-17935" class="comments-container"><span id="17936"></span><div id="comment-17936" class="comment"><div id="post-17936-score" class="comment-score"></div><div class="comment-text"><p>Jasper,</p><p>Thanks for posting. I did not remember seeing any STP packets but I wish I had kept the capture. I initially thought the same thing however I when using the new switches in unmanaged mode, I would not think they would be affected by spanning tree. Also the one time I had the dell switch in managed mode I did turn off spanning tree and did not see any different behavior.</p><p>I'll be installing another HP Procurve and although it does not support STP, I'm hoping I can mirror the ports and see what is happening.</p></div><div id="comment-17936-info" class="comment-info"><span class="comment-age">(24 Jan '13, 09:30)</span> <span class="comment-user userinfo">mattinnc</span></div></div><span id="18108"></span><div id="comment-18108" class="comment"><div id="post-18108-score" class="comment-score"></div><div class="comment-text"><p>Jasper</p><p>Thanks for he post. I did see some stp frames but nothing excessive. They were coming from the cisco router. Interestingly I installed a new HP switch and so far have not seen any issue although I'm not confident it's solved. When some clients loose connectivity it appears as thought they are connected but not traffic is seen from the NIC. If it comes up again I'll check the arp cache and see if it gives me a clue</p></div><div id="comment-18108-info" class="comment-info"><span class="comment-age">(30 Jan '13, 09:18)</span> <span class="comment-user userinfo">mattinnc</span></div></div><span id="18143"></span><div id="comment-18143" class="comment"><div id="post-18143-score" class="comment-score"></div><div class="comment-text"><p>some ideas. It could be STP misconfig (filter BPDU somewhere). Try to turn On STP on every device and every port. Have seen real nightmare when customer looped private-vlan port to public-port on some pvlan switch.</p><p>It could be host spoofing MACs of real hosts and flooding network. So switches filter those macs. Although Win will warn you in such case. Check mac-address-table on switches or turn on port-mac registration.</p></div><div id="comment-18143-info" class="comment-info"><span class="comment-age">(30 Jan '13, 21:30)</span> <span class="comment-user userinfo">v_paranoid</span></div></div></div><div id="comment-tools-17935" class="comment-tools"></div><div class="clear"></div><div id="comment-17935-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="17952"></span>

<div id="answer-container-17952" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17952-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17952-score" class="post-score" title="current number of votes">0</div><span id="post-17952-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Can the hosts access one another, or can they just not access things off the lan? Check the ARP entries on the host to make she they look correct. Secondly check the interface status on the switch. Make sure it is not Admin-Down Err-Disabled or other state.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jan '13, 19:06</strong></p><img src="https://secure.gravatar.com/avatar/f4567d2db9c9f422c664030ac53a1873?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Magnus%20Mortensen&#39;s gravatar image" /><p><span>Magnus Morte...</span><br />
<span class="score" title="56 reputation points">56</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Magnus Mortensen has one accepted answer">50%</span></p></div></div><div id="comments-container-17952" class="comments-container"></div><div id="comment-tools-17952" class="comment-tools"></div><div class="clear"></div><div id="comment-17952-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

