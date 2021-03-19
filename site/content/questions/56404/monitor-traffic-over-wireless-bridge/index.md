+++
type = "question"
title = "Monitor Traffic over wireless bridge"
description = '''When my computer is connected directly to mirror port of switch all works. When I send traffic from mirror port over a wireless bridge I only get broadcast traffic. Help'''
date = "2016-10-15T08:02:00Z"
lastmod = "2016-10-15T08:02:00Z"
weight = 56404
keywords = [ "wirelessbridge" ]
aliases = [ "/questions/56404" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Monitor Traffic over wireless bridge](/questions/56404/monitor-traffic-over-wireless-bridge)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56404-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When my computer is connected directly to mirror port of switch all works. When I send traffic from mirror port over a wireless bridge I only get broadcast traffic. Help</p></div><div id="question-tags" class="tags-container tags">wirelessbridge</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Oct '16, 08:02</strong></p><img src="https://secure.gravatar.com/avatar/1e03bf0be5ba818d94296a430f12a905?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wlm905&#39;s gravatar image" /><p>wlm905<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wlm905 has no accepted answers">0%</span></p></div></div><div id="comments-container-56404" class="comments-container"><span id="56405"></span><div id="comment-56405" class="comment"><div id="post-56405-score" class="comment-score"></div><div class="comment-text"><p>What type of wireless bridge?<br />
</p><p>Bridges like this that I have used operate at layer 2, so make forwarding decisions based on layer 2 information, i.e. MAC addresses. So not really a surprise if a mirror port destination traffic will not make it across the bridge. The missing traffic is unicast (per your comment) and that does not belong at the other side of that bridge. You might, sometimes, benefit from the layer 2 device trying to learn source MACs for the forwarding table by flooding unknown traffic, but I wouldn't count on that.<br />
</p><p>Maybe you want to find a way to encapsulate this unicast traffic and have it sent to you, via unicast, across the bridge? The model could be rpcap, or one of the other streaming capture utilities. It's a little unusual to send mirror port traffic over a wireless bridge - can you share what you are trying to do?</p></div><div id="comment-56405-info" class="comment-info"><span class="comment-age">(15 Oct '16, 08:41)</span> Bob Jones</div></div><span id="56412"></span><div id="comment-56412" class="comment"><div id="post-56412-score" class="comment-score"></div><div class="comment-text"><p>To extend @Bob Jones' explanation, it doesn't really matter whether the bridge is a wireless or wired one.</p><p>A switch or bridge sends frames bearing <strong>destination</strong> MAC addresses yet unknown to it to all output ports (i.e. "floods" all ports with them), so far so good. But it learns the associations between its ports and the MAC addresses from the frames' <strong>source</strong> MAC addresses.</p><p>So what actually happens is that while you monitor the real traffic between, say, MAC address A and MAC address B, both A and B appear as source MAC addresses in the individual frames which the local port of the bridge receives from the monitoring port of the other switch. So it understands both A and B as accessible via its port on which it has seen them, and therefore it doesn't have a reason to forward them to any other port - at best (or worst, as you like) case, it might send them back on the local port.</p><p>In the wired case, you could use a hub rather than a bridge, because a hub is an L1 device, not L2, which means it doesn't care about the MAC addresses. But an ordinary wireless bridge is L2-aware in order not to waste the radio bandwidth by sending traffic not meant for the remote end, so it behaves as described above.</p><p>So encapsulation of the captured frames, as recommended by @Bob Jones, is normally the only way how to deliver the captured traffic anywhere else than to a NIC directly connected to the monitoring port.</p></div><div id="comment-56412-info" class="comment-info"><span class="comment-age">(15 Oct '16, 11:39)</span> sindy</div></div><span id="56424"></span><div id="comment-56424" class="comment"><div id="post-56424-score" class="comment-score"></div><div class="comment-text"><p>Thanks Bob and sindy for responding. Your answers make sense and saved me from a lot of aggravation.</p><p>We run a small wireless ISP and am trying to sniff out Bittorrent use using Wireshark. Our feeder ISP is 6 miles away and I installed a managed switch with a mirror port at that point. All clients including me access this point via UBNT NSM5 radios. Monitoring at the feeder ISP location (at the managed switch) works but is not feasible for any length of time (I'd lose my computer).</p><p>So, now to research encapsulation. Thanks again.</p></div><div id="comment-56424-info" class="comment-info"><span class="comment-age">(16 Oct '16, 11:01)</span> wlm905</div></div></div><div id="comment-tools-56404" class="comment-tools"></div><div class="clear"></div><div id="comment-56404-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

