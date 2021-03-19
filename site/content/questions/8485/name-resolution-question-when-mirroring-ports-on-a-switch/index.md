+++
type = "question"
title = "Name resolution question when mirroring ports on a switch..."
description = '''Folks, I am relatively new to Wireshark. I am monitoring my home network traffic by mirroring a port on my GS116E sent to a second NIC on one of my PCs. I have my router (WRT54GL) set up to tee POSTROUTED traffic to this monitor NIC as well. This is working well and I see all the wired, wireless, an...'''
date = "2012-01-19T17:08:00Z"
lastmod = "2012-01-20T19:51:00Z"
weight = 8485
keywords = [ "ip", "mac", "switch", "mirroring" ]
aliases = [ "/questions/8485" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Name resolution question when mirroring ports on a switch...](/questions/8485/name-resolution-question-when-mirroring-ports-on-a-switch)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8485-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8485-score" class="post-score" title="current number of votes">0</div><span id="post-8485-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Folks,</p><p>I am relatively new to Wireshark. I am monitoring my home network traffic by mirroring a port on my GS116E sent to a second NIC on one of my PCs. I have my router (WRT54GL) set up to tee POSTROUTED traffic to this monitor NIC as well. This is working well and I see all the wired, wireless, and WAN traffic.</p><p>The question I have is about the mirrored packets often showing up as TCP Retransmissions (in red on black) with the <strong><em>destination decoded as the original destination</em></strong> rather than the monitor NIC destination. The original packet shows matching destination IP and MAC addresses. The teed packet shows the original IP destination and the monitor NIC's MAC address. The content of both packets is otherwise identical. So the data is being sent twice and to the correct MACs, but being displayed in a way I would not have expected.</p><p>Here is how I mirror at the router which creates the extra LAN traffic sent to the monitor NIC: iptables -A POSTROUTING -t mangle -j ROUTE --gw 10.0.0.199 --tee</p><p><img src="http://home.comcast.net/~kk1l/NameResolution.jpg" alt="screen copy of an example" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ip" rel="tag" title="see questions tagged &#39;ip&#39;">ip</span> <span class="post-tag tag-link-mac" rel="tag" title="see questions tagged &#39;mac&#39;">mac</span> <span class="post-tag tag-link-switch" rel="tag" title="see questions tagged &#39;switch&#39;">switch</span> <span class="post-tag tag-link-mirroring" rel="tag" title="see questions tagged &#39;mirroring&#39;">mirroring</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Jan '12, 17:08</strong></p><img src="https://secure.gravatar.com/avatar/2f26f7bce6a9d3ce0dbad24c7e065ca4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="KK1L&#39;s gravatar image" /><p><span>KK1L</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="KK1L has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>19 Jan '12, 20:05</strong> </span></p></div></div><div id="comments-container-8485" class="comments-container"></div><div id="comment-tools-8485" class="comment-tools"></div><div class="clear"></div><div id="comment-8485-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8502"></span>

<div id="answer-container-8502" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8502-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8502-score" class="post-score" title="current number of votes">2</div><span id="post-8502-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I'm not a iptables specialist, but I think what you're doing is to have the router mangle all packets to be sent to an additional destination, which is your Wireshark NIC. So what you have there is not the same as a "normal" SPAN port, but some sort of packet manipulation/duplication process that will also change the MAC address of the destination in order to be able to deliver it at all.</p><p>Usually, a SPAN/Mirror/Monitor/Roving port (or whatever the vendor calls it) is a layer two copy process that simply copies the frame to the port where the analyzer is connected to, without modifying it at all. Your solution is sort of a higher layer workaround, which has the side effects of modifying the MAC address, if I am not mistaken.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Jan '12, 03:56</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-8502" class="comments-container"><span id="8527"></span><div id="comment-8527" class="comment"><div id="post-8527-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the reply Jasper. You are right about the iptables action. Wireshark must be looking at the IPV4 rather than EthernetII. I have to assume that is the correct place for it to look because I am just getting my feet wet in this level of network decoding.</p></div><div id="comment-8527-info" class="comment-info"><span class="comment-age">(20 Jan '12, 19:51)</span> <span class="comment-user userinfo">KK1L</span></div></div></div><div id="comment-tools-8502" class="comment-tools"></div><div class="clear"></div><div id="comment-8502-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

