+++
type = "question"
title = "NLB only works with Wireshark capturing"
description = '''How is this for weird, we have been having some issues with a Microsoft NLB cluster so I put wireshark on one of the nodes, stopped and powered off the second node. The cluster stopped working after a short while (part of the issue we have been trying to resolve). This means that hitting the vIP for...'''
date = "2015-02-03T03:55:00Z"
lastmod = "2015-02-03T14:15:00Z"
weight = 39600
keywords = [ "windows", "nlb", "portable", "iis" ]
aliases = [ "/questions/39600" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [NLB only works with Wireshark capturing](/questions/39600/nlb-only-works-with-wireshark-capturing)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39600-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39600-score" class="post-score" title="current number of votes">0</div><span id="post-39600-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How is this for weird, we have been having some issues with a Microsoft NLB cluster so I put wireshark on one of the nodes, stopped and powered off the second node. The cluster stopped working after a short while (part of the issue we have been trying to resolve). This means that hitting the vIP for the cluster did not return the website hosted on the server. I ran wireshark on my laptop, saw the request and then the TCP retransmission. No replies at all. I then ran wireshark on the server, and immediately the site works. I stop capturing (wireshark still running) and it stops working. Start capture, starts working. I can reproduce this at will. Anyone have any idea what is causing this?</p><p>The server is Server 2012R2 as a VMware VM. (ESXi 5.5). Running NLB set up in IGMP Multicast mode. IIS 8.5 with ARR 3. Wireshark is 1.12.2 PortableApp. WinPCAP is 4.1.0.2980</p><p>Other information that might be useful: Static ARP is done on a Watchguard firewall There is also a static ARP entry and CAM table entries on the Cisco 2960 stack connected to all the hosts. Routing for this VLAN is done on the watchguard</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-nlb" rel="tag" title="see questions tagged &#39;nlb&#39;">nlb</span> <span class="post-tag tag-link-portable" rel="tag" title="see questions tagged &#39;portable&#39;">portable</span> <span class="post-tag tag-link-iis" rel="tag" title="see questions tagged &#39;iis&#39;">iis</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Feb '15, 03:55</strong></p><img src="https://secure.gravatar.com/avatar/0cb5be8afa7f845c51fd976ff06f9307?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cakelord&#39;s gravatar image" /><p><span>cakelord</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cakelord has no accepted answers">0%</span></p></div></div><div id="comments-container-39600" class="comments-container"></div><div id="comment-tools-39600" class="comment-tools"></div><div class="clear"></div><div id="comment-39600-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39601"></span>

<div id="answer-container-39601" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39601-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39601-score" class="post-score" title="current number of votes">2</div><span id="post-39601-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="cakelord has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>When you capture traffic with Wireshark the NIC will be put into promiscuous mode by default. This means the NIC will forward all frames to the OS. In normal (non-promiscuous mode) the NIC only forwards:</p><ul><li>Unicast frames for the mac-address of the system</li><li>Broadcast frames</li><li>Multicast frames, but only for the multicast groups to which the system was subscribed</li></ul><p>So, if starting a wireshark trace makes the setup work, it is most probably because some frames were rejected by the NIC otherwise. Most likely the multicast frames.</p><p>You can do a little test by making a trace with wireshark while you disable the option to put the NIC in multicast mode (go to capture settings, double-click on the interface on which you want to capture and disable "prmiscuous mode"). My bet is that now the server won't respond, just like when no capture was made.</p><p>You can look at the differences between the capture with promiscuous mode on and the capture with promiscuous mode off to learn which frames were dropped by the NIC. I'm no NLB expert, but my bet is you need to configure something on the server to make it accept the multicast traffic in a multicast NLB setup.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Feb '15, 04:16</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-39601" class="comments-container"><span id="39602"></span><div id="comment-39602" class="comment"><div id="post-39602-score" class="comment-score"></div><div class="comment-text"><p>I think that is most likely the issue, restarting the server and un-installing WinPCAP has made it work. That makes me think that when I stopped a capture in wireshark (I will have run one before and just forgotten) I will have taken the NIC out of Promiscuous mode and NLB didn't know to put it back into that mode. I have a snapshot before these changes I will do some testing on later and see if I can confirm it. Thanks</p></div><div id="comment-39602-info" class="comment-info"><span class="comment-age">(03 Feb '15, 04:25)</span> <span class="comment-user userinfo">cakelord</span></div></div><span id="39616"></span><div id="comment-39616" class="comment"><div id="post-39616-score" class="comment-score"></div><div class="comment-text"><p>also, VMware and Microsoft NLB can get into trouble when the ESXi sends RARP frames to the network, e.g. when a VM moves via vMotion or when a snapshot is taken/removed.</p></div><div id="comment-39616-info" class="comment-info"><span class="comment-age">(03 Feb '15, 14:15)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-39601" class="comment-tools"></div><div class="clear"></div><div id="comment-39601-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

