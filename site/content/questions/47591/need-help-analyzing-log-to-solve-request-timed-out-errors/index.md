+++
type = "question"
title = "Need Help Analyzing Log to Solve Request Timed Out Errors"
description = '''Here is the WireShark capture: http://sunnydaysites.com/wp-content/uploads/2015/11/wireshark.pcapng I am trying to use this tool to determine why I get connection timed out when trying to access hospitalitysolutionsgroup.us (74.86.141.52) from browser on desktop PC in Virginia connected to router (1...'''
date = "2015-11-13T15:04:00Z"
lastmod = "2015-11-18T17:10:00Z"
weight = 47591
keywords = [ "timed", "connection", "out" ]
aliases = [ "/questions/47591" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Need Help Analyzing Log to Solve Request Timed Out Errors](/questions/47591/need-help-analyzing-log-to-solve-request-timed-out-errors)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47591-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47591-score" class="post-score" title="current number of votes">0</div><span id="post-47591-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Here is the WireShark capture: <a href="http://sunnydaysites.com/wp-content/uploads/2015/11/wireshark.pcapng">http://sunnydaysites.com/wp-content/uploads/2015/11/wireshark.pcapng</a></p><p>I am trying to use this tool to determine why I get connection timed out when trying to access hospitalitysolutionsgroup.us (74.86.141.52) from browser on desktop PC in Virginia connected to router (192.168.1.177). Verizon is the ISP, who said the problem is beyond their equipment. Tracert indicates that po2.fcr03.sr04.dal01.networklayer.com at 66.228.118.190 is the last stop before receiving multiple 'Request timed out'. I've contacted SoftLayer which is the owner of networklayer, but no luck. Also contacted Telstra since they are associated with 66.228.118.190. No luck. I noticed their network has a Point of Presence in my city/state, which must be coincidental. I've emailed the NOC in NJ. No answer. I thought the problem could be static.reverse.realssl.com. I see that service is down for dns1.realssl.com for 74.86.12.112. I am new to network operations and WireShark, and could use some help determining where the problem is and who to contact. Thank you!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-timed" rel="tag" title="see questions tagged &#39;timed&#39;">timed</span> <span class="post-tag tag-link-connection" rel="tag" title="see questions tagged &#39;connection&#39;">connection</span> <span class="post-tag tag-link-out" rel="tag" title="see questions tagged &#39;out&#39;">out</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Nov '15, 15:04</strong></p><img src="https://secure.gravatar.com/avatar/9672539fd24c59883c6882757dd4fa6b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JCIMB&#39;s gravatar image" /><p><span>JCIMB</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JCIMB has no accepted answers">0%</span></p></div></div><div id="comments-container-47591" class="comments-container"></div><div id="comment-tools-47591" class="comment-tools"></div><div class="clear"></div><div id="comment-47591-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47600"></span>

<div id="answer-container-47600" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47600-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47600-score" class="post-score" title="current number of votes">1</div><span id="post-47600-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hi, I'd say your own analysis has squeezed all what was possible from the information which can be obtained at your end.</p><p>And you are lucky in terms that the problem is most likely located very close to the remote end of the network path, because my own <code>tracert 74.86.141.52</code> shows the following:<br />
<code>...  17   133 ms   133 ms   134 ms  po1.fcr03.sr04.dal01.networklayer.com [66.228.118.186]  18   134 ms   135 ms   136 ms  74.86.141.52-static.reverse.realssl.com [74.86.141.52]</code><br />
</p><p>So I think that by 45 % it should be enough to contact the site administrators of hospitalitysolutionsgroup.us, describe them the issue and tell them the public IP of the router to which your PC is connected. Your and my tracert taken together indicate that the machine on which their web site is running has a configuration issue preventing them from routing response packets to your router. The possibility that the other interface of 66.228.118.190, looking towards the 74.86.141.52, is down accounts for another 45 %.<br />
</p><p>My reasons to think so are that 66.228.118.190 in your tracert and 66.228.118.186 in mine can be reasonably supposed to share the same subnet and maybe even to operate in load sharing mode. The .190 was able to send an icmp response to your tracert, so the problem is behind it as seen from your perspective, and it is unlikely that there would be more routing hops between .190 and the 74.86.141.52 than between .186 and the 74.86.141.52.</p><p>The remaining 10 % account for unlikely scenarios, like one of the routers in the path which would take source IPs into account when routing and not forwarding packets sent from 74.86.141.52 properly. Most likely, some centralized anti-virus solution could be a source of such activity, if it thinks that the hospitalitysolutionsgoup.us is a source of malware or spam. For that kind of system I'd look close to your end of the path.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Nov '15, 02:43</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>14 Nov '15, 02:44</strong> </span></p></div></div><div id="comments-container-47600" class="comments-container"><span id="47601"></span><div id="comment-47601" class="comment"><div id="post-47601-score" class="comment-score"></div><div class="comment-text"><p>To add a view from a different site. I can access the server without problem and ping/traceroute works as well.</p><pre><code>  4    19 ms    20 ms    18 ms  82.135.16.209
  5    21 ms    21 ms    22 ms  80.81.194.167
  6     *       29 ms    31 ms  50.97.18.208
  7   108 ms   114 ms   108 ms  50.97.18.204
  8   132 ms   131 ms   131 ms  173.192.18.132
  9   145 ms   145 ms   146 ms  173.192.18.136
 10   149 ms   149 ms   149 ms  173.192.18.253
 11   145 ms   145 ms   145 ms  66.228.118.190  &lt;====
 12   147 ms   148 ms   152 ms  74.86.141.52    &lt;====

Trace complete.

68 23.027373000 192.168.90.57 74.86.141.52 TCP 0x2f01 (12033)   66  1732→80 [SYN] Seq=0 Win=8192 Len=0 MSS=1460 WS=4 SACK_PERM=1                

69 23.173791000 74.86.141.52 192.168.90.57 TCP  0x7842 (30786)  66  80→1732 [SYN, ACK] Seq=0 Ack=1 Win=8192 Len=0 MSS=1304 WS=256 SACK_PERM=1               
</code></pre><p>Regards<br />
Kurt</p></div><div id="comment-47601-info" class="comment-info"><span class="comment-age">(14 Nov '15, 03:15)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="47732"></span><div id="comment-47732" class="comment"><div id="post-47732-score" class="comment-score"></div><div class="comment-text"><p>Thanks so much Kurt. I sent your answer to the admin of the destination website that I couldn't reach and he replied that someone from my IP range had been doing what appeared to be an ftp attack to break into someone’s site and that my addresses had been blacklisted. He was able to fix it and now I can now reach the site.</p></div><div id="comment-47732-info" class="comment-info"><span class="comment-age">(18 Nov '15, 17:10)</span> <span class="comment-user userinfo">JCIMB</span></div></div></div><div id="comment-tools-47600" class="comment-tools"></div><div class="clear"></div><div id="comment-47600-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

