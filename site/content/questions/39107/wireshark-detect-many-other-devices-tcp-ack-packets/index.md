+++
type = "question"
title = "WireShark detect many other devices TCP ACK packets"
description = '''Hi,  My PC IP is 1.177, but when I run WireShark, I always detect many many TCP ACK packets from 2.105 to 1.74, which our backup servers. I know 2.105 need backup all things to 1.74 during day time. but why my PC 1.177 can detect those packets? those packets need over 90% on my PC WireShark log. I c...'''
date = "2015-01-13T19:36:00Z"
lastmod = "2015-01-15T19:04:00Z"
weight = 39107
keywords = [ "packets", "tcp" ]
aliases = [ "/questions/39107" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [WireShark detect many other devices TCP ACK packets](/questions/39107/wireshark-detect-many-other-devices-tcp-ack-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39107-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39107-score" class="post-score" title="current number of votes">0</div><span id="post-39107-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, My PC IP is 1.177, but when I run WireShark, I always detect many many TCP ACK packets from 2.105 to 1.74, which our backup servers. I know 2.105 need backup all things to 1.74 during day time. but why my PC 1.177 can detect those packets? those packets need over 90% on my PC WireShark log. I checked and there is no mirroring port. Does anyone have idea about it ? it's virus or faulty nic?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-packets" rel="tag" title="see questions tagged &#39;packets&#39;">packets</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Jan '15, 19:36</strong></p><img src="https://secure.gravatar.com/avatar/3df6170b483811676868e385abe112a2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hardwater&#39;s gravatar image" /><p><span>Hardwater</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hardwater has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>14 Jan '15, 15:12</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-39107" class="comments-container"></div><div id="comment-tools-39107" class="comment-tools"></div><div class="clear"></div><div id="comment-39107-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="39119"></span>

<div id="answer-container-39119" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39119-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39119-score" class="post-score" title="current number of votes">1</div><span id="post-39119-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This kind of thing happens when switches have to flood frames to all ports because they don't have the MAC address of the target IP in their MAC/CAM table. This often happens if a switch is really under heavy load and the MAC/CAM table is too small to keep all relevant IP-MAC combinations in memory.</p><p>You should really check your switch (login to the switch console) to see how utilized it is. My guess is you should see lots of warning messages as soon as you do.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Jan '15, 00:54</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-39119" class="comments-container"><span id="39134"></span><div id="comment-39134" class="comment"><div id="post-39134-score" class="comment-score"></div><div class="comment-text"><p>Thanks, Jasper. After I moved 1.74 to another switch, the traffic stops now. But I still got some kinds of traffic for another servers. Also I'm keeping get ping time out in whole network. I'm not sure if it's related to it. Sometimes after 10 seconds I get one Ping time out, some time around 1 or 2 mins. before I'm thinking of STP issue, but time period is not right for STP.</p><p>Do you think after reboot switch will fix this issue. our core switch is HP 5800 and edge switches all HP 5210</p><p>Many Thanks</p></div><div id="comment-39134-info" class="comment-info"><span class="comment-age">(14 Jan '15, 14:26)</span> <span class="comment-user userinfo">Hardwater</span></div></div><span id="39135"></span><div id="comment-39135" class="comment"><div id="post-39135-score" class="comment-score"></div><div class="comment-text"><p>Hi, Jasper, I just checked switches MAC address table size, they can hole 32000 Mac address, I think it's enough for our network.</p></div><div id="comment-39135-info" class="comment-info"><span class="comment-age">(14 Jan '15, 14:39)</span> <span class="comment-user userinfo">Hardwater</span></div></div><span id="39136"></span><div id="comment-39136" class="comment"><div id="post-39136-score" class="comment-score"></div><div class="comment-text"><p>Here's the output from the switch:</p><pre><code>MAC TYPE            LEARNED    USER-DEFINED  SYSTEM-DEFINED IN-USE    AVAILABLE
Dynamic   Unicast   853        0             4              857
Static    Unicast   0          3             28             31        1024
Total     Unicast                                           888       32768

Dynamic Multicast   0          0             0              0
Static  Multicast   0          13            12             25        256
Total   Multicast                                           25        0</code></pre><p>but total Multicast available as above is 0, is it something about it?</p></div><div id="comment-39136-info" class="comment-info"><span class="comment-age">(14 Jan '15, 14:43)</span> <span class="comment-user userinfo">Hardwater</span></div></div></div><div id="comment-tools-39119" class="comment-tools"></div><div class="clear"></div><div id="comment-39119-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="39174"></span>

<div id="answer-container-39174" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39174-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39174-score" class="post-score" title="current number of votes">1</div><span id="post-39174-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Is there asymmetric routing in your environment? When the 1.74 communicates back to the 2.105 over a different path than the active routing engine in the network, then the FDB entry of a switch in the other path might be flushed due to a lower timeout of the FDB entry than the ARP entry.</p><p>This means that the routing engine has to flush the traffic since it no longer has the entry in the FDB (because return traffic does not pass this switch so it's table is not refreshed).</p><p>Please check the presence of the mac address of 1.74 on the switches when you see the ACK's coming by.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jan '15, 12:56</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-39174" class="comments-container"><span id="39180"></span><div id="comment-39180" class="comment"><div id="post-39180-score" class="comment-score"></div><div class="comment-text"><p>Thanks, SYN-bit, Not only 2.105 have this issue, even the same subnet 1.XXX also have this issue. When I got ping time out, I can see those unexpected TCP ACK packets between other vlan 1 servers (they plugged in same core switch) Currently we have 3 HP S5800 switch stacking together to become one core. Before 1.74 plug into core 1, and then I plug it to core 3, I can see mac address table on core switches pick up new port immediately. But still can detected those unexpected TCP packets to 1.74. I doubt if there is any know bug for HP S5800 currently? Anyway, I logged a request to HP and hope they can have some idea as well.</p></div><div id="comment-39180-info" class="comment-info"><span class="comment-age">(15 Jan '15, 19:04)</span> <span class="comment-user userinfo">Hardwater</span></div></div></div><div id="comment-tools-39174" class="comment-tools"></div><div class="clear"></div><div id="comment-39174-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

