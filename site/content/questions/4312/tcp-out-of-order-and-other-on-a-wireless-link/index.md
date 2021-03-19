+++
type = "question"
title = "TCP out-of-order and other on a wireless link"
description = '''Hello everybody. I&#x27;m troubleshooting a network with Wireshark and, being new to deep traffic analysis, maybe some of you could give some advice to understand what&#x27;s happening. Let me depict the scenario:  Internet  |  | &amp;lt;-Wired link  |  Core LAN  |  |  Branch#1--------Branch#2   ^  |  Wireless 5,...'''
date = "2011-06-01T02:15:00Z"
lastmod = "2011-06-16T03:43:00Z"
weight = 4312
keywords = [ "wireless", "out-of-order" ]
aliases = [ "/questions/4312" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [TCP out-of-order and other on a wireless link](/questions/4312/tcp-out-of-order-and-other-on-a-wireless-link)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4312-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello everybody.</p><p>I'm troubleshooting a network with Wireshark and, being new to deep traffic analysis, maybe some of you could give some advice to understand what's happening.</p><p>Let me depict the scenario:</p><pre><code>            Internet
               |
               |    &lt;-Wired link
               |
            Core LAN
               |
               |
    Branch#1--------Branch#2

               ^
               |
        Wireless 5,8 GHz PMP link</code></pre><p>Branch#1 uses the link only for basic office Internet access, browsing and mail. Branch#2 surfes the Internet and uses an application running on a server in the Core LAN.</p><p>Users in Branch#1 don't report problems for now. User in Branch#2 (only three) complain about "expired connections" when using their TCP application. All I could get from application support was "it is due to lost connectivity to server". But when the issue (randomly) appeared, access to Internet was up, so there was no lost connectivity.</p><p>I used the Packet Monitoring tool in the firewall connecting all networks and exported to Wireshark. One of the samples showed that 28% of captured packets were (almost half) downlink TCP out-of-order, retransmissions, fast retransmissions and lost segments (from Internet to Branch#1) and (the rest) uplink Duplicated ACKs (from Branch#1 to Internet).</p><p>About Branch#2, another sample showed similar statics from or to Application Server, except for Duplicated ACKs, much less than for Branch#1. I know it's not very comprehensive but maybe significant, I still don't want to go deeper without knowing what and where to look for.</p><p>The fact is that, prior to installing the wireless link, users in Branch#2 connected to the application server through an ADSL router and Logmein Hamachi software (I didn't know it, some kind of virtual VPN) and they only complained about slowness. Now, response from server is quick but annoying. I wonder if this issue could be related to the wireless link behaviour and if it's usual on such links. Maybe some of you have some experience with them. I browsed the forum but I didn't find some useful clue in similar cases.</p><p>Thank you all.</p><p>Regards.</p></div><div id="question-tags" class="tags-container tags">wireless out-of-order</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Jun '11, 02:15</strong></p><img src="https://secure.gravatar.com/avatar/7c31c4e7640e4bee439cf0af16eb7201?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="CVA23&#39;s gravatar image" /><p>CVA23<br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="CVA23 has no accepted answers">0%</span></p></div></div><div id="comments-container-4312" class="comments-container"><span id="4321"></span><div id="comment-4321" class="comment"><div id="post-4321-score" class="comment-score"></div><div class="comment-text"><p>It is possible to determine the direction of the packet loss if you know what to look for. But given that BR1 users are not complaining, I would start with looking at the setup at BR2. For example, do the users have a duplex mismatch? Does the uplink to the wireless router have a duplex mismatch? Also, how did you perform the capture on the FW? Did you capture incoming <em>and</em> outgoing interface at the same time? It's possible that your wireless signal is weak and is causing this issue, but you have to start to divide and conquer. Start at BR2 and see if the problem is local or not.</p></div><div id="comment-4321-info" class="comment-info"><span class="comment-age">(01 Jun '11, 17:00)</span> hansangb</div></div><span id="4322"></span><div id="comment-4322" class="comment"><div id="post-4322-score" class="comment-score"></div><div class="comment-text"><p>It would also help if you can post the binary capture files somewhere (you can use snaplen of 96 or so bytes. There's no need to see the full packet size.</p></div><div id="comment-4322-info" class="comment-info"><span class="comment-age">(01 Jun '11, 17:01)</span> hansangb</div></div><span id="4330"></span><div id="comment-4330" class="comment"><div id="post-4330-score" class="comment-score"></div><div class="comment-text"><p>If packet loss is an issue you want to identify the point where packets are lost. As hansangb pointed out, BR2 configuration might be the key. When it comes to wireless you might have obstacles like trees between sites.</p><p>After following hansangb's advice on duplex mismatch I would pinpoint the traffic-leg where you loose packets by capturing at the core and branch 2 uplink simultaneously. (Guess that's what he meant with "divide and conquuer".</p></div><div id="comment-4330-info" class="comment-info"><span class="comment-age">(02 Jun '11, 06:27)</span> packethunter</div></div></div><div id="comment-tools-4312" class="comment-tools"></div><div class="clear"></div><div id="comment-4312-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="4590"></span>

<div id="answer-container-4590" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4590-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Sorry for being so late after I posted this question, but I had to park this case for a time while solving another ones.</p><p>Thanks to hansangb and packethunter for your answers. In fact, I divided and conquered:</p><p>First, I tuned the wireless links, there were too much re-registrations causing the link to be reestablished.</p><p>Second, I checked the firewall and found dropped packets caused by "Invalid TCP flag". Through the firewall TAC I tuned the TCP timeout and dropped packets disappeared.</p><p>Since then, conflictive packets went down from 28% to 2%. I don't know if even 2% is too much in such configuration, but I know that users don't complain and that's enough for now.</p><p>In any case, I'm still monitoring these networks to be sure it's working fine because I'm suspecting of some misconfigured or compromised PC in the Branch#1 or Branch#2 network according to what I could see (one of the earlier captures showed an upload to a "uncommon" url). Unluckly, those networks aren't still under my management and I can't go farther by now. And wireless links are always subject to uncontrolled factors, so I must go on watching.</p><p>Thank you all.</p><p>Regards.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Jun '11, 03:43</strong></p><img src="https://secure.gravatar.com/avatar/7c31c4e7640e4bee439cf0af16eb7201?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="CVA23&#39;s gravatar image" /><p>CVA23<br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="CVA23 has no accepted answers">0%</span></p></div></div><div id="comments-container-4590" class="comments-container"></div><div id="comment-tools-4590" class="comment-tools"></div><div class="clear"></div><div id="comment-4590-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

