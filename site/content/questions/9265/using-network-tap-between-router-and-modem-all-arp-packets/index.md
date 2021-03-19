+++
type = "question"
title = "Using Network Tap between router and modem; All ARP packets?"
description = '''Hi, I installed a TAP between my router and modem so I can get answers when the internet gets slow. My idea was to get all the outgoing traffic from the router mirrored and then capture it with Wireshark. I&#x27;ve turned promiscuous mode on but all I&#x27;m getting is ARP packets (see screenshot). I&#x27;m a novi...'''
date = "2012-02-28T01:08:00Z"
lastmod = "2012-02-28T01:08:00Z"
weight = 9265
keywords = [ "tap" ]
aliases = [ "/questions/9265" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Using Network Tap between router and modem; All ARP packets?](/questions/9265/using-network-tap-between-router-and-modem-all-arp-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9265-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I installed a TAP between my router and modem so I can get answers when the internet gets slow. My idea was to get all the outgoing traffic from the router mirrored and then capture it with Wireshark. I've turned promiscuous mode on but all I'm getting is ARP packets (see screenshot). I'm a novice at networking; any help would be greatly appreciated.</p><p><img src="http://i.imgur.com/YTwoN.png" alt="All ARP packets" /></p><p>The tap I'm using is the <a href="http://www.dual-comm.com/port-mirroring-LAN_switch.htm">Dualcomm DCSW-1005</a> and my network looks like this:</p><p><img src="http://i.imgur.com/nASAP.jpg" alt="Dualcomm TAP should mirror traffic from the router to the monitoring computer" /></p><p>The DCSW-1005 manual says this about port mirroring:</p><blockquote><p>DCSW-1005 ... provides port mirroring function in which outgoing and incoming packets associated with Port 1 (Target Port) are forwarded to Port 5 (Monitor Port). Such a port-mirroring mechanism is hardware-configured and therefore no software setup is necessary.</p><p>Incoming and outgoing packets of Port 1 are 'copied' to Port 5 while Port 5 also operates as a normal port sending and receiving its 'own' packets.</p></blockquote><p>Darren</p></div><div id="question-tags" class="tags-container tags">tap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Feb '12, 01:08</strong></p><img src="https://secure.gravatar.com/avatar/890cfeb384c825616c0898ba3dab9ede?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wahtermelon&#39;s gravatar image" /><p>wahtermelon<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wahtermelon has no accepted answers">0%</span></p></img></div></div><div id="comments-container-9265" class="comments-container"><span id="63973"></span><div id="comment-63973" class="comment"><div id="post-63973-score" class="comment-score"></div><div class="comment-text"><p>Did you ever find a solution to this?</p></div><div id="comment-63973-info" class="comment-info"><span class="comment-age">(17 Oct '17, 09:52)</span> Cevestas</div></div><span id="64065"></span><div id="comment-64065" class="comment"><div id="post-64065-score" class="comment-score"></div><div class="comment-text"><p><a href="https://ask.wireshark.org/users/44226/cevestas">@Cevestas</a>, the Question above shows only packets with broadcast L2 destination address to make it to the capturing interface. If you have the same experience, as I assume from your comment, see <a href="https://ask.wireshark.org/questions/64033/promiscuous-mode-nic-adapter-setup-required">this recent question</a> whose answers deal with most likely causes of this, regardless how exactly the copy of the 3rd party traffic is obtained (tap, hub, mirroring switch).</p></div><div id="comment-64065-info" class="comment-info"><span class="comment-age">(21 Oct '17, 05:19)</span> sindy</div></div></div><div id="comment-tools-9265" class="comment-tools"></div><div class="clear"></div><div id="comment-9265-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

