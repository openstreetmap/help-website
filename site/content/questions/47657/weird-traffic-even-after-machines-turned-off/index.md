+++
type = "question"
title = "Weird traffic even after machines turned off"
description = '''Hey, I&#x27;m new to the forums but a long time (basic) wireshark user. I&#x27;m seeing some really strange traffic. There is constant activity (+/- 2000 packets per second) between 2 source ip&#x27;s and a destination ip. The source IP&#x27;s are vm&#x27;s which use anywhereusb. The destination IP is from an anywhereusb de...'''
date = "2015-11-17T02:32:00Z"
lastmod = "2015-11-19T02:02:00Z"
weight = 47657
keywords = [ "anywhereusb", "vmware" ]
aliases = [ "/questions/47657" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Weird traffic even after machines turned off](/questions/47657/weird-traffic-even-after-machines-turned-off)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47657-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47657-score" class="post-score" title="current number of votes">0</div><span id="post-47657-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey, I'm new to the forums but a long time (basic) wireshark user. I'm seeing some really strange traffic. There is constant activity (+/- 2000 packets per second) between 2 source ip's and a destination ip. The source IP's are vm's which use anywhereusb. The destination IP is from an anywhereusb device. The strange thing is that the traffic continues even if the source machine is powered off and the anywhereusb device is powered off. The second strange thing is that the MAC address wireshark shows for the anywhereusb device doesn't match with it's actual MAC address. The mac address also isn't traceable in the mac-address-table of our switches. The mac address of the source is correct an can be traced to the port connected to our esx. But as stated before there's even traffic when both machines are turned off. For the moment I'm a bit clueless as to what could be the cause. Below are the summary texts for two records.</p><p>Any help will be much appreciated.</p><p>17369 2015-11-17 09:40:34.939583000 10.7.x.x 10.0.x.x TCP 60 netiq &gt; rtip [SYN] Seq=1902520936 Win=64240[Malformed Packet] Vmware_9c:15:f5 Digiboar_9c:1a:20</p><p>28663 2015-11-17 10:14:12.301107000 10.7.x.y 10.0.x.x TCP 60 brlp-3 &gt; rtip [SYN] Seq=1075763157 Win=64240[Malformed Packet] Vmware_9c:1a:20 Digiboar_44:bf:f5</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-anywhereusb" rel="tag" title="see questions tagged &#39;anywhereusb&#39;">anywhereusb</span> <span class="post-tag tag-link-vmware" rel="tag" title="see questions tagged &#39;vmware&#39;">vmware</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Nov '15, 02:32</strong></p><img src="https://secure.gravatar.com/avatar/1ac83358146d6ff7e3d06c0e590a9285?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pproost&#39;s gravatar image" /><p><span>pproost</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pproost has no accepted answers">0%</span></p></div></div><div id="comments-container-47657" class="comments-container"><span id="47658"></span><div id="comment-47658" class="comment"><div id="post-47658-score" class="comment-score"></div><div class="comment-text"><p>Can you share a capture in a publicly accessible spot, e.g. <a href="http://cloudshark.org">CloudShark</a>?</p></div><div id="comment-47658-info" class="comment-info"><span class="comment-age">(17 Nov '15, 02:55)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="47663"></span><div id="comment-47663" class="comment"><div id="post-47663-score" class="comment-score"></div><div class="comment-text"><p><a href="https://www.cloudshark.org/captures/661de826c909">https://www.cloudshark.org/captures/661de826c909</a></p></div><div id="comment-47663-info" class="comment-info"><span class="comment-age">(17 Nov '15, 04:15)</span> <span class="comment-user userinfo">pproost</span></div></div></div><div id="comment-tools-47657" class="comment-tools"></div><div class="clear"></div><div id="comment-47657-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47692"></span>

<div id="answer-container-47692" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47692-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47692-score" class="post-score" title="current number of votes">1</div><span id="post-47692-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><pre><code>17369 2015-11-17 09:40:34.939583000 10.7.x.x 10.0.x.x TCP 60 netiq &gt; rtip [SYN] Seq=1902520936 Win=64240[Malformed Packet] Vmware_9c:15:f5 Digiboar_9c:1a:20

28663 2015-11-17 10:14:12.301107000 10.7.x.y 10.0.x.x TCP 60 brlp-3 &gt; rtip [SYN] Seq=1075763157 Win=64240[Malformed Packet] Vmware_9c:1a:20 Digiboar_44:bf:f5</code></pre><p>Maybe there are just two packets, because all the packets with the src <code>10.7.0.7</code> have the <code>IP.ID 0xe7e4</code> and all the packets with the src <code>10.7.0.8</code> have the <code>IP.ID 0x3669</code>. When you apply the following filter eno strange packet can be seen any more:</p><pre><code>(!(ip.id == 0xe7e4)) &amp;&amp; !(ip.id == 0x3669)</code></pre><p>So that assumption means that these packets are circling in the network and it doesn´t matter if the src hosts are active or not. The reason for that I just can guess... maybe it is because the destination IP is the network address or the mac is not known in the network or a bug or...???<br />
</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Nov '15, 14:14</strong></p><img src="https://secure.gravatar.com/avatar/3b24b339fc62fb46dced6a443d3202ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christian_R&#39;s gravatar image" /><p><span>Christian_R</span><br />
<span class="score" title="1830 reputation points"><span>1.8k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christian_R has 25 accepted answers">16%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>17 Nov '15, 15:36</strong> </span></p></div></div><div id="comments-container-47692" class="comments-container"><span id="47694"></span><div id="comment-47694" class="comment"><div id="post-47694-score" class="comment-score"></div><div class="comment-text"><p>Hi, thanks for you answer. I also noticed the same thing and I'm suspecting that there's something wrong with the spanning-tree in our network and that there's a kind of flooding going on. But unfortunately my Cisco knowledge isn't good enough to be sure so I'll have to contact our network specialist when I'm back at the office tomorrow.</p></div><div id="comment-47694-info" class="comment-info"><span class="comment-age">(17 Nov '15, 14:23)</span> <span class="comment-user userinfo">pproost</span></div></div><span id="47738"></span><div id="comment-47738" class="comment"><div id="post-47738-score" class="comment-score"></div><div class="comment-text"><p>We're still investigating the network problem/cause but were able to get the rogue packets of the network by creating two vm's with the mac addresses of the rogue packets so the packets had somewhere to go. Maybe it can help someone else with the same problem.</p></div><div id="comment-47738-info" class="comment-info"><span class="comment-age">(19 Nov '15, 01:49)</span> <span class="comment-user userinfo">pproost</span></div></div><span id="47739"></span><div id="comment-47739" class="comment"><div id="post-47739-score" class="comment-score"></div><div class="comment-text"><p>Smart idea with that dummy MAC. Have tried a firmware update at the switches?</p></div><div id="comment-47739-info" class="comment-info"><span class="comment-age">(19 Nov '15, 02:02)</span> <span class="comment-user userinfo">Christian_R</span></div></div></div><div id="comment-tools-47692" class="comment-tools"></div><div class="clear"></div><div id="comment-47692-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

