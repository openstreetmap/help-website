+++
type = "question"
title = "GameOver Zues on NAT network"
description = '''I am attempting to find the computer infected with GameOver Zeus virus on my NAT network. I have a smoothwall open source firewall and Microsoft SBS 2011 server on the network. How would I capture the information required. This is what CBL Abuse suggest to get delisted. NEW! The Gameover Zeus/Tovar ...'''
date = "2014-08-14T13:26:00Z"
lastmod = "2014-08-14T13:26:00Z"
weight = 35490
keywords = [ "helpt" ]
aliases = [ "/questions/35490" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [GameOver Zues on NAT network](/questions/35490/gameover-zues-on-nat-network)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35490-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am attempting to find the computer infected with GameOver Zeus virus on my NAT network. I have a smoothwall open source firewall and Microsoft SBS 2011 server on the network.</p><p>How would I capture the information required.</p><p>This is what CBL Abuse suggest to get delisted.</p><p>NEW! The Gameover Zeus/Tovar project has set up a "lighthouse IP". The lighthouse IP has been set up to help administrators find the Gameover Zeus infection on NAT networks. The theory is simple: every time an infected PC attempts to connect to a Command&amp;Control sinkhole (see below for a partial list), the infected PC will also send a UDP packet to IP address 72.52.116.52 on port 4643 (though we suggest logging all ports). By configuring that address into your firewall, you can log which local IP address is attempting to contact 72.52.116.52, and thereby find and remediate the infection.</p><p>If you are connected to us via a computer you believe may be infected, this link should help confirm your suspicion: Online Gameover Zeus Detector</p><p>REMEMBER Gameover Zeus DOES NOT communicate over port 25 at all. It has nothing to do with email. Do not waste your time fiddling around with port 25 firewall rules.</p><p>To find an infected computer on a NATted LAN you are searching for a local machine that is trying to make connections to a Zeus Command and Control (C&amp;C) server on the Internet. These C&amp;C servers have been taken over by our partners and they are giving us reports about which IPs are trying to talk to them. It is those IP addresses that are infected.</p><p>If you have full logs of your firewall activity at the time this occurred, you can look in the logs for the time/sinkhole IP and destination port information given below.</p><p>If you do not have full logs, you will need to set up a sniffer or firewall rules to catch and log attempts to talk to the C&amp;C.</p></div><div id="question-tags" class="tags-container tags">helpt</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Aug '14, 13:26</strong></p><img src="https://secure.gravatar.com/avatar/68401bb0be423bb46e96f316768b24cd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Trinard&#39;s gravatar image" /><p>Trinard<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Trinard has no accepted answers">0%</span></p></div></div><div id="comments-container-35490" class="comments-container"><span id="35491"></span><div id="comment-35491" class="comment"><div id="post-35491-score" class="comment-score"></div><div class="comment-text"><p>(Deleted by mistake.. Sorry)</p></div><div id="comment-35491-info" class="comment-info"><span class="comment-age">(14 Aug '14, 13:38)</span> Bill Meier ♦♦</div></div><span id="35493"></span><div id="comment-35493" class="comment"><div id="post-35493-score" class="comment-score"></div><div class="comment-text"><p>I think you'll get more appropriate help over at the smoothwall support facilities, they'll tell you how to log the traffic.</p></div><div id="comment-35493-info" class="comment-info"><span class="comment-age">(14 Aug '14, 14:46)</span> grahamb ♦</div></div><span id="35503"></span><div id="comment-35503" class="comment"><div id="post-35503-score" class="comment-score"></div><div class="comment-text"><p>I agree with grahamb, that your question really translates to how do you configure your firewall to log certain traffic. That's not really a wireshark question. But assuming you know how to configure your firewall to log certain events, then "CBL Abuse" lays it out pretty straightforward. This virus attempts to send a UDP packet to 72.52.116.52:4643. So by logging traffic on your firewall with a destination address of 72.52.116.52, you will be able to identify the source IP address, and thereby identify the infected computer.</p></div><div id="comment-35503-info" class="comment-info"><span class="comment-age">(15 Aug '14, 05:11)</span> smp</div></div></div><div id="comment-tools-35490" class="comment-tools"></div><div class="clear"></div><div id="comment-35490-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

