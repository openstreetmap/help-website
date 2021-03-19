+++
type = "question"
title = "Intermittent LAN issues"
description = '''Hi, Every now and then, our LAN interface seems to fail. The router itself (Pfsense) is reachable remotely over the internet during such outage.  Restarting the router always solved the issue. I fired up the packet capture tool on the PFsense during the outage, which you can find here: https://www.c...'''
date = "2016-10-12T01:43:00Z"
lastmod = "2016-10-12T07:28:00Z"
weight = 56306
keywords = [ "arp" ]
aliases = [ "/questions/56306" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Intermittent LAN issues](/questions/56306/intermittent-lan-issues)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56306-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56306-score" class="post-score" title="current number of votes">-1</div><span id="post-56306-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>Every now and then, our LAN interface seems to fail. The router itself (Pfsense) is reachable remotely over the internet during such outage.</p><p>Restarting the router always solved the issue.</p><p>I fired up the packet capture tool on the PFsense during the outage, which you can find here: <a href="https://www.cloudshark.org/captures/66c61a1e0b60">https://www.cloudshark.org/captures/66c61a1e0b60</a></p><p>At first, I thought our VLANS were causing the issue because I was using unmanaged switched (and a single broadcast domain)</p><p>I removed all VLANS, so we only have one LAN interface currently. Still the issue persist.</p><p>Does anybody have a clue where to look for?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-arp" rel="tag" title="see questions tagged &#39;arp&#39;">arp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Oct '16, 01:43</strong></p><img src="https://secure.gravatar.com/avatar/aa37f4a1ef5ed10e622d24d203ab1338?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jortie2&#39;s gravatar image" /><p><span>jortie2</span><br />
<span class="score" title="10 reputation points">10</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jortie2 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>12 Oct '16, 01:47</strong> </span></p></div></div><div id="comments-container-56306" class="comments-container"></div><div id="comment-tools-56306" class="comment-tools"></div><div class="clear"></div><div id="comment-56306-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="56307"></span>

<div id="answer-container-56307" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56307-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56307-score" class="post-score" title="current number of votes">0</div><span id="post-56307-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>All TCP connections that trying to get to the internet (sending a SYN packet) remain unanswered (you can see that when filtering for "tcp"). Also, all ARP requests for 192.168.1.254 (which I guess is the IP of the LAN interface of the pfSense) remain unanswered, at least I don't see any.</p><p>What you could do is take a capture to compare this behavior to a working situation - you'll most likely see SYNs being answered with SYN/ACK packets, and ARP receiving replies telling the MAC address of 192.168.1.254.</p><p>It's quite unusual that ARPs aren't answered anymore - the SYNs being blocked may be explained by some firewall rule setting, but layer 2 should work...</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Oct '16, 02:23</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-56307" class="comments-container"><span id="56310"></span><div id="comment-56310" class="comment"><div id="post-56310-score" class="comment-score"></div><div class="comment-text"><p>Yes, I cant make anything of the ARP issues as well. Also, a firewall rule should either always block, or never block, right?</p><p>What should I do next?</p></div><div id="comment-56310-info" class="comment-info"><span class="comment-age">(12 Oct '16, 02:53)</span> <span class="comment-user userinfo">jortie2</span></div></div><span id="56311"></span><div id="comment-56311" class="comment"><div id="post-56311-score" class="comment-score"></div><div class="comment-text"><p>Does the pfSense continue to run while connections are blocked? What does the "Uptime" value of the dashboard say, is it indicating a recent reboot? Which pfSense version are you running?</p></div><div id="comment-56311-info" class="comment-info"><span class="comment-age">(12 Oct '16, 02:55)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="56312"></span><div id="comment-56312" class="comment"><div id="post-56312-score" class="comment-score"></div><div class="comment-text"><p>Pfsense stays running. I can access the Pfsense remotely (over the internet) during a LAN outage.</p></div><div id="comment-56312-info" class="comment-info"><span class="comment-age">(12 Oct '16, 03:21)</span> <span class="comment-user userinfo">jortie2</span></div></div><span id="56314"></span><div id="comment-56314" class="comment"><div id="post-56314-score" class="comment-score"></div><div class="comment-text"><p>Did you check if the LAN interface is down during the outage? It almost looks like it has to be, because it seems to be completely unresponsive - right now I'd suspect a link down/hardware problem. Maybe someone can go and check link status LEDs during the next outage?</p></div><div id="comment-56314-info" class="comment-info"><span class="comment-age">(12 Oct '16, 04:00)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="56317"></span><div id="comment-56317" class="comment"><div id="post-56317-score" class="comment-score"></div><div class="comment-text"><p>Since you've covered the basics, it's better to head over to pfSense support</p><p><a href="https://www.pfsense.org/get-involved/#join-the-discussion">https://www.pfsense.org/get-involved/#join-the-discussion</a></p></div><div id="comment-56317-info" class="comment-info"><span class="comment-age">(12 Oct '16, 07:06)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="56321"></span><div id="comment-56321" class="comment not_top_scorer"><div id="post-56321-score" class="comment-score"></div><div class="comment-text"><p>The interface is not down during the outage. I will try to replace the hardware</p></div><div id="comment-56321-info" class="comment-info"><span class="comment-age">(12 Oct '16, 07:28)</span> <span class="comment-user userinfo">jortie2</span></div></div></div><div id="comment-tools-56307" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-56307-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

