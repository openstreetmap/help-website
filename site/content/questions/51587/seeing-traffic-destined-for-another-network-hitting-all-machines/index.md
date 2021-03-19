+++
type = "question"
title = "[closed] Seeing traffic destined for another network, hitting all machines"
description = '''Hi, We have a site that is set up with 2 subnets, 192.168.50.x which is used for data and 192.168.60.x which is used for voice, both use a 255.255.255.0 mask. These are NOT VLANs, they are purely separate subnets however they traverse the same switches so consequently are part of the same broadcast ...'''
date = "2016-04-12T03:16:00Z"
lastmod = "2016-04-12T03:16:00Z"
weight = 51587
keywords = [ "broadcast", "udp", "networking", "mac-address" ]
aliases = [ "/questions/51587" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] Seeing traffic destined for another network, hitting all machines](/questions/51587/seeing-traffic-destined-for-another-network-hitting-all-machines)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51587-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>We have a site that is set up with 2 subnets, 192.168.50.x which is used for data and 192.168.60.x which is used for voice, both use a 255.255.255.0 mask. These are NOT VLANs, they are purely separate subnets however they traverse the same switches so consequently are part of the same broadcast domain.</p><p>The problem we are having is that when users are using the phones, all of the UDP voice traffic from the 192.168.60.x network is hitting all machines on the 192.168.50.x network. For example, on a machine on 192.168.50.22, we see traffic sourced from 192.168.60.10 (the PBX) destined to 192.168.60.26 but it is hitting all machines? Interestingly, the source MAC address is the default gateway of the PBX server however the destination MAC address is another device related to the PBX.</p><p>Could anybody shed any light as to what is going on here? I suspect the default gateway (which is the same for both subnets, it is just configured with 2 LANs) is rerouting the traffic back to the 192.168.50.x subnet, but why is it hitting all the machines!? It reaping havoc on the network and causing all sorts of network connectivity issues...</p><p>Any guidance would be much appreciated.</p><p>Regards,</p><p>Jonathan.</p></div><div id="question-tags" class="tags-container tags">broadcast udp networking mac-address</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Apr '16, 03:16</strong></p><img src="https://secure.gravatar.com/avatar/8ac8aaabcf360cef154c972fb2a2292a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jonathanbaird&#39;s gravatar image" /><p>jonathanbaird<br />
<span class="score" title="6 reputation points">6</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jonathanbaird has one accepted answer">50%</span></p></div><div class="post-update-info post-update-info-edited"><p>closed 12 Apr '16, 04:26</p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-51587" class="comments-container"><span id="51593"></span><div id="comment-51593" class="comment"><div id="post-51593-score" class="comment-score"></div><div class="comment-text"><p>You should go over to <a href="http://networkengineering.stackexchange.com/">http://networkengineering.stackexchange.com/</a></p></div><div id="comment-51593-info" class="comment-info"><span class="comment-age">(12 Apr '16, 04:26)</span> Jaap ♦</div></div></div><div id="comment-tools-51587" class="comment-tools"></div><div class="clear"></div><div id="comment-51587-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Question is off-topic or not relevant" by Jaap 12 Apr '16, 04:26

</div>

</div>

</div>

