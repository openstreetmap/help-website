+++
type = "question"
title = "capture filter problems: v 1.2.9 on Windows XP WiFi"
description = '''PC &#x27;A&#x27; is an old XP machine monitoring my internal WiFi network and helping debug what PC &#x27;B&#x27; is doing (Wireshark 1.6.2 on Ubuntu 11.10). Both Wiresharks are in promiscuous capture. I want to see UDP packets on a specific port directed at PC B, plus an ICMP packet that B sends in response, AND any p...'''
date = "2013-06-15T17:03:00Z"
lastmod = "2013-06-15T17:03:00Z"
weight = 22099
keywords = [ "xp", "capture-filter" ]
aliases = [ "/questions/22099" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [capture filter problems: v 1.2.9 on Windows XP WiFi](/questions/22099/capture-filter-problems-v-129-on-windows-xp-wifi)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22099-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22099-score" class="post-score" title="current number of votes">0</div><span id="post-22099-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>PC 'A' is an old XP machine monitoring my internal WiFi network and helping debug what PC 'B' is doing (Wireshark 1.6.2 on Ubuntu 11.10).</p><p>Both Wiresharks are in promiscuous capture.</p><p>I want to see UDP packets on a specific port directed at PC B, plus an ICMP packet that B sends in response, AND any packets that B sends prior to the received UDP packet (to track down a Firewall problem).</p><p>Using Wireshark on PC B I 'know what to expect' for most of the time (ie once Wireshark is started, just missing the initial boot etc); which is how I know there are things 'missing' from the trace on PC A.</p><p>If I use (on PC A) the capture filter 'ip proto 1 or ip proto 17' I see MOST (but not all) of the incoming UDP and outgoing ICMP.</p><p>If I add 'or (ether host ab:cd:ef:gh:ij:kl and not ether proto 0x0806)' to the capture filter string, I do not see the incoming UDP anymore (looks like I see only packets sent by the specified host).</p><p>If, instead, I add 'or dst net 224.0.0.0' then I see most of the incoming UDP, &amp; corresponding ICMP, and any IP multi-cast traffic that is sent....but I am missing (by design) any other traffic sent by PC A.</p><p>I saw in the forum a post re special form of display filter (on source IP) needed when traffic is captured from a WiFi interface... ? is there an equivalent that is needed to get the capture filter to work as desired on WiFi?</p><p>OR is my capture filter design/syntax OK, and the missing packets due to bad WiFi, incapable old hardware etc etc ??</p><p>OR is this a known bug/issue with such an old version of Wireshark ? (I looked at upgrade a while back and think I concluded 'not possible without OS upgrade..)</p><p>thanks in advance,,,</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-xp" rel="tag" title="see questions tagged &#39;xp&#39;">xp</span> <span class="post-tag tag-link-capture-filter" rel="tag" title="see questions tagged &#39;capture-filter&#39;">capture-filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Jun '13, 17:03</strong></p><img src="https://secure.gravatar.com/avatar/9cc3300882005b0c2c8bea416a276b64?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="charlieS&#39;s gravatar image" /><p><span>charlieS</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="charlieS has no accepted answers">0%</span></p></div></div><div id="comments-container-22099" class="comments-container"></div><div id="comment-tools-22099" class="comment-tools"></div><div class="clear"></div><div id="comment-22099-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

