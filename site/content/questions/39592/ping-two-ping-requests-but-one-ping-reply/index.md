+++
type = "question"
title = "Ping: Two ping requests but one ping reply"
description = '''Hello,  I have a machine with two different wireless interfaces (two different PCI cards). I run Wireshark and ping another machine in the same LAN. Wireshark displays two ping requests and one ping reply. The echo requests are exactly the same (same source and destination IP, same source and destin...'''
date = "2015-02-03T01:17:00Z"
lastmod = "2015-02-05T07:48:00Z"
weight = 39592
keywords = [ "reply", "request", "duplicate", "ping", "one" ]
aliases = [ "/questions/39592" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Ping: Two ping requests but one ping reply](/questions/39592/ping-two-ping-requests-but-one-ping-reply)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39592-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39592-score" class="post-score" title="current number of votes">0</div><span id="post-39592-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I have a machine with two different wireless interfaces (two different PCI cards). I run Wireshark and ping another machine in the same LAN. Wireshark displays two ping requests and one ping reply. The echo requests are exactly the same (same source and destination IP, same source and destination MAC address, same TTL, same sequence number, same checksum, everything is the same). Of course I see only one ping reply.</p><p>Does anyone have an idea about this behavior? Any help would be appreciated. Thanks in advance</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-reply" rel="tag" title="see questions tagged &#39;reply&#39;">reply</span> <span class="post-tag tag-link-request" rel="tag" title="see questions tagged &#39;request&#39;">request</span> <span class="post-tag tag-link-duplicate" rel="tag" title="see questions tagged &#39;duplicate&#39;">duplicate</span> <span class="post-tag tag-link-ping" rel="tag" title="see questions tagged &#39;ping&#39;">ping</span> <span class="post-tag tag-link-one" rel="tag" title="see questions tagged &#39;one&#39;">one</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Feb '15, 01:17</strong></p><img src="https://secure.gravatar.com/avatar/d3f5e1c327be84a5f9b27e7ee09b6658?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="johnson91&#39;s gravatar image" /><p><span>johnson91</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="johnson91 has no accepted answers">0%</span></p></div></div><div id="comments-container-39592" class="comments-container"><span id="39596"></span><div id="comment-39596" class="comment"><div id="post-39596-score" class="comment-score"></div><div class="comment-text"><p>What is your OS and which version and what is your Wireshark version?</p></div><div id="comment-39596-info" class="comment-info"><span class="comment-age">(03 Feb '15, 02:41)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="39597"></span><div id="comment-39597" class="comment"><div id="post-39597-score" class="comment-score"></div><div class="comment-text"><p>I use Debian GNU/Linux 7.8 (Wheezy) with kernel 3.2.0-4-amd64 and Wireshark Version 1.8.2</p></div><div id="comment-39597-info" class="comment-info"><span class="comment-age">(03 Feb '15, 02:56)</span> <span class="comment-user userinfo">johnson91</span></div></div></div><div id="comment-tools-39592" class="comment-tools"></div><div class="clear"></div><div id="comment-39592-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39610"></span>

<div id="answer-container-39610" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39610-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39610-score" class="post-score" title="current number of votes">0</div><span id="post-39610-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This may suggest that packet is traversing via two interfaces</p><p>This can happen if you have some kind of a bridge, virtual interfaces or maybe bonding setup and you are running wireshark on all interfaces.</p><p>Try specifying just a single interface and if you have virtual ones specified then use closes to the physical device, for example if you have eth0 and eth0:1 pick eth0</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Feb '15, 09:07</strong></p><img src="https://secure.gravatar.com/avatar/96df873546556d82f89c599816554877?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="izopizo&#39;s gravatar image" /><p><span>izopizo</span><br />
<span class="score" title="202 reputation points">202</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="izopizo has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>03 Feb '15, 09:07</strong> </span></p></div></div><div id="comments-container-39610" class="comments-container"><span id="39613"></span><div id="comment-39613" class="comment"><div id="post-39613-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your answer. I have to physical interfaces (two different MAC addresses), namely wlan0 and wlan1. These two interfaces are configured so that they belong in two differents VLANs. I use only one interface for capturing (wlan0). The problem remains even if I run ping as "ping -I wlan0 IP_addr". Any suggestions?</p></div><div id="comment-39613-info" class="comment-info"><span class="comment-age">(03 Feb '15, 11:41)</span> <span class="comment-user userinfo">johnson91</span></div></div><span id="39632"></span><div id="comment-39632" class="comment"><div id="post-39632-score" class="comment-score"></div><div class="comment-text"><p>From what you've described (same checksum, sequence number etc) it looks like you are seeing the same packet twice.</p><p>As mentioned before I'd investigate network configuration (You've mentioned VLANs, how exactly have you set it up ? )</p><p>Also for comparison I'd run tcpdump -nni wlan0 icmp to see if tcpdump also reports two packets.</p><p>The fact that you are pinging from a given interface and seeing two packets suggests that additional interface along the way.</p></div><div id="comment-39632-info" class="comment-info"><span class="comment-age">(04 Feb '15, 03:06)</span> <span class="comment-user userinfo">izopizo</span></div></div><span id="39659"></span><div id="comment-39659" class="comment"><div id="post-39659-score" class="comment-score"></div><div class="comment-text"><p>Thanks for replying.</p><p>VLANs are configured as follows: One interface has IP 100.100.100.100.x/24 and belongs to VLAN 100.100.100.0/24 and the second interface has IP 200.200.200.y/24 and belongs to VLAN 200.200.200.y/24.</p><p>I run tcpdump -nni wlan0 icmp and I have exactly the same output, as with Wireshark.</p></div><div id="comment-39659-info" class="comment-info"><span class="comment-age">(05 Feb '15, 02:17)</span> <span class="comment-user userinfo">johnson91</span></div></div><span id="39669"></span><div id="comment-39669" class="comment"><div id="post-39669-score" class="comment-score"></div><div class="comment-text"><p>Can you paste output from ip a ls and iwconfig</p></div><div id="comment-39669-info" class="comment-info"><span class="comment-age">(05 Feb '15, 07:48)</span> <span class="comment-user userinfo">izopizo</span></div></div></div><div id="comment-tools-39610" class="comment-tools"></div><div class="clear"></div><div id="comment-39610-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

