+++
type = "question"
title = "How to configure router and port mirroring to minimize repeat packets?"
description = '''Folks, My home network is set up as MODEM &amp;lt;--&amp;gt; WAP (WRT54GL) &amp;lt;--&amp;gt; 16 port switch (GS116E). I have a 2nd NIC in my monitor computer connected to a port on the GS116E set up to mirror the computer ports. I do not mirror the NAS or uplink ports. Then I tee at the router which sends a copy o...'''
date = "2012-01-19T19:38:00Z"
lastmod = "2012-01-20T04:07:00Z"
weight = 8489
keywords = [ "duplicate", "configuration", "packets", "mirror" ]
aliases = [ "/questions/8489" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to configure router and port mirroring to minimize repeat packets?](/questions/8489/how-to-configure-router-and-port-mirroring-to-minimize-repeat-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8489-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8489-score" class="post-score" title="current number of votes">0</div><span id="post-8489-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Folks,</p><p>My home network is set up as MODEM &lt;--&gt; WAP (WRT54GL) &lt;--&gt; 16 port switch (GS116E). I have a 2nd NIC in my monitor computer connected to a port on the GS116E set up to mirror the computer ports. I do not mirror the NAS or uplink ports. Then I tee at the router which sends a copy of any traffic handled by the access point (iptables -A POSTROUTING -t mangle -j ROUTE --gw 10.0.0.199 --tee). So far so good.</p><p>By not mirroring the uplink or NAS ports on the switch I don't get extra packets when file transfers occur, nor from traffic bound for the WAN or the WLAN. The one trouble I have left is that any traffic to/from the WAN from a computer on the switch get doubled (one copy from the tee and one from the port mirror).</p><p>Are there any suggestions how I might eliminate the duplicates? Maybe some set of commands at the WAP (WRT54GL running Tomato)?</p><p>I could look for a cheap NAT device to go between the modem and the switch and move the WAP onto the switch I guess, but I was looking for a "no added device" solution.</p><p>THANKS!</p><p>ron &lt;&gt;&lt;</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-duplicate" rel="tag" title="see questions tagged &#39;duplicate&#39;">duplicate</span> <span class="post-tag tag-link-configuration" rel="tag" title="see questions tagged &#39;configuration&#39;">configuration</span> <span class="post-tag tag-link-packets" rel="tag" title="see questions tagged &#39;packets&#39;">packets</span> <span class="post-tag tag-link-mirror" rel="tag" title="see questions tagged &#39;mirror&#39;">mirror</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Jan '12, 19:38</strong></p><img src="https://secure.gravatar.com/avatar/2f26f7bce6a9d3ce0dbad24c7e065ca4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="KK1L&#39;s gravatar image" /><p><span>KK1L</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="KK1L has no accepted answers">0%</span></p></div></div><div id="comments-container-8489" class="comments-container"></div><div id="comment-tools-8489" class="comment-tools"></div><div class="clear"></div><div id="comment-8489-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8503"></span>

<div id="answer-container-8503" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8503-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8503-score" class="post-score" title="current number of votes">0</div><span id="post-8503-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You could capture the traffic with duplicates, and then remove them from the trace file afterwards, using <strong>editpcap -d</strong>. I just answered a similar question <a href="http://ask.wireshark.org/questions/8490/tcp-retransmission-is-detected-instead-of-a-duplicate-ip-packet">here</a>, so you might want to look at that one, too.</p><p>Since I already saw in another post that you're having problems with the MAC addresses in the "duplicate" packets being different (while the rest stays the same) I have to add that editcap -d might not work as expected, though. editcap looks for exact duplicates by calculating MD5 hashs on frames, and if the MAC is different, so is the hash. Which will lead to "duplicates" still remaining in the "cleaned" trace file since the hashs didn't match with the original packets.</p><p>A possible workaround could be to do the cleanup process in a two step way:</p><ol><li>capture the data, including duplicates</li><li>replace the monitor NIC MAC with the original MAC, for example by using a packet editor like <a href="http://bittwist.sourceforge.net/">bittwiste</a>. This could be a very complicated process, since you'll probably have to replace the same monitor NIC MAC with different other, original MACs (of the computer and the router). That could require you to split the trace into separate files for each node first, and I just feel a headache coming up :-)</li><li>Deduplicate the resulting file with <strong>editcap -d</strong></li></ol><p>Other than that, you're probably out of luck, since removing duplicates expects them to be 100% the same, bit by bit.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Jan '12, 04:07</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-8503" class="comments-container"></div><div id="comment-tools-8503" class="comment-tools"></div><div class="clear"></div><div id="comment-8503-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

