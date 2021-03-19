+++
type = "question"
title = "Network Crash"
description = '''My local network keeps crashing during the night and I am having to reboot my vpn server every morning. I heard about this wireshark and decided to install it and capture data from my local network and while the network is down this is what I am getting: 11 06:34:10.245845000 IntelCor_3a:e9:9f Broad...'''
date = "2015-09-11T06:22:00Z"
lastmod = "2015-09-11T06:22:00Z"
weight = 45786
keywords = [ "broadcast" ]
aliases = [ "/questions/45786" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Network Crash](/questions/45786/network-crash)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45786-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>My local network keeps crashing during the night and I am having to reboot my vpn server every morning. I heard about this wireshark and decided to install it and capture data from my local network and while the network is down this is what I am getting:</p><p>11 06:34:10.245845000 IntelCor_3a:e9:9f Broadcast ARP 42 who has 00.000.00.000? Tell 11.111.11.11</p><p>This is the only item that is being captured so I have pages and pages of this exact same message.</p><p>I have entered zero's and one's for the ip address so that I can keep our IP address private. Can someone tell me what could possible be wrong. Have been working on this issue for almost three weeks and I am going nuts trying to figure this out.</p><p>Thanks Tony</p></div><div id="question-tags" class="tags-container tags">broadcast</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Sep '15, 06:22</strong></p><img src="https://secure.gravatar.com/avatar/6cf746d618d3a24f6e42ca127be649b5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tonyc&#39;s gravatar image" /><p>tonyc<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tonyc has no accepted answers">0%</span></p></div></div><div id="comments-container-45786" class="comments-container"><span id="45787"></span><div id="comment-45787" class="comment"><div id="post-45787-score" class="comment-score"></div><div class="comment-text"><p>Not much to go on. Is the real "has" IP relevant to your systems?</p></div><div id="comment-45787-info" class="comment-info"><span class="comment-age">(11 Sep '15, 06:40)</span> grahamb ♦</div></div><span id="45788"></span><div id="comment-45788" class="comment"><div id="post-45788-score" class="comment-score"></div><div class="comment-text"><p>Hello grahamb</p><p>Yes the real IP address is for our main system (basically our main frame) and the "tell" is my vpn server which provides internet to all pc's locally and allows other vpn servers (satalite locations) to dial in and have access to the main frame as well across the vpn. The switches that I use locally are all unmanaged.</p></div><div id="comment-45788-info" class="comment-info"><span class="comment-age">(11 Sep '15, 07:06)</span> tonyc</div></div><span id="45790"></span><div id="comment-45790" class="comment"><div id="post-45790-score" class="comment-score"></div><div class="comment-text"><p>Do you have any filtering on your captures? That message is a broadcast, so I suspect other traffic, including the non-broadcast response, isn't being captured.</p><p>Note that for long-term captures, you should really use dumpcap from the command line, Wireshark (and tshark) will run out of memory due to the state they keep.</p></div><div id="comment-45790-info" class="comment-info"><span class="comment-age">(11 Sep '15, 07:45)</span> grahamb ♦</div></div><span id="45792"></span><div id="comment-45792" class="comment"><div id="post-45792-score" class="comment-score"></div><div class="comment-text"><p>There is no filtering on the capture. This is the only message that keeps coming up in Wireshark and nothing else, no answer from the "has" at all, the network just keeps asking and asking and asking.</p></div><div id="comment-45792-info" class="comment-info"><span class="comment-age">(11 Sep '15, 08:31)</span> tonyc</div></div><span id="45793"></span><div id="comment-45793" class="comment"><div id="post-45793-score" class="comment-score"></div><div class="comment-text"><p>Then something is preventing you capturing all the traffic. On which host or switch are you capturing?</p></div><div id="comment-45793-info" class="comment-info"><span class="comment-age">(11 Sep '15, 08:39)</span> grahamb ♦</div></div><span id="45808"></span><div id="comment-45808" class="comment not_top_scorer"><div id="post-45808-score" class="comment-score"></div><div class="comment-text"><p>Run a packet capture on the vpn server and also check the arp table. Do it for a working and a non working state.</p></div><div id="comment-45808-info" class="comment-info"><span class="comment-age">(12 Sep '15, 05:23)</span> Roland</div></div></div><div id="comment-tools-45786" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-45786-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

