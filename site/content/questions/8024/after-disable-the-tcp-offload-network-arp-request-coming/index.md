+++
type = "question"
title = "after disable the tcp offload network arp request coming"
description = '''after disable the tcp offload on three server only, and run wireshark on my server arp request is coming, before disable tcp offload my network was normal.  kindly help , is it issue or normal thing  0 0 Dell_e5:d8:59 Broadcast ARP 60 FALSE Gratuitous ARP for 192.168.0.120 (Reply) 1 21.278276 21.278...'''
date = "2011-12-17T02:35:00Z"
lastmod = "2011-12-17T02:50:00Z"
weight = 8024
keywords = [ "arp", "issue", "network" ]
aliases = [ "/questions/8024" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [after disable the tcp offload network arp request coming](/questions/8024/after-disable-the-tcp-offload-network-arp-request-coming)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8024-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8024-score" class="post-score" title="current number of votes">0</div><span id="post-8024-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>after disable the tcp offload on three server only, and run wireshark on my server arp request is coming, before disable tcp offload my network was normal. kindly help , is it issue or normal thing</p><pre><code>0   0   Dell_e5:d8:59   Broadcast   ARP 60  FALSE   Gratuitous ARP for 192.168.0.120 (Reply)    1
21.278276   21.278276   Dell_e8:99:59   Broadcast   ARP 60  FALSE   Who has 192.168.2.100?  Tell 192.168.2.117  2
0.000901    21.279177   D-Link_be:dd:c3 Broadcast   ARP 60  FALSE   Who has 192.168.2.117?  Tell 192.168.2.100  3
9.481865    30.761042   Dell_e5:d8:59   Broadcast   ARP 60  FALSE   Gratuitous ARP for 192.168.0.120 (Reply)    4
15.343019   46.104061   Dell_e6:c4:ac   Broadcast   ARP 60  FALSE   Who has 192.168.2.100?  Tell 192.168.2.116  5
0.000908    46.104969   D-Link_be:dd:c3 Broadcast   ARP 60  FALSE   Who has 192.168.2.116?  Tell 192.168.2.100  6
15.374804   61.479773   Dell_e5:d8:59   Broadcast   ARP 60  FALSE   Gratuitous ARP for 192.168.0.120 (Reply)    7
30.759868   92.239641   Dell_e5:d8:59   Broadcast   ARP 60  FALSE   Gratuitous ARP for 192.168.0.120 (Reply)    8
30.759856   122.999497  Dell_e5:d8:59   Broadcast   ARP 60  FALSE   Gratuitous ARP for 192.168.0.120 (Reply)    9
30.761067   153.760564  Dell_e5:d8:59   Broadcast   ARP 60  FALSE   Gratuitous ARP for 192.168.0.120 (Reply)    10
29.08981    182.850374  Dell_e6:c2:a7   Broadcast   ARP 60  FALSE   Who has 192.168.2.100?  Tell 192.168.2.125  11
0.000878    182.851252  D-Link_be:dd:c3 Broadcast   ARP 60  FALSE   Who has 192.168.2.125?  Tell 192.168.2.100  12
1.628007    184.479259  Dell_e5:d8:59   Broadcast   ARP 60  FALSE   Gratuitous ARP for 192.168.0.120 (Reply)    13
1.504338    185.983597  Dell_e8:94:4b   Broadcast   ARP 60  FALSE   Who has 192.168.2.100?  Tell 192.168.2.126  14
0.000918    185.984515  D-Link_be:dd:c3 Broadcast   ARP 60  FALSE   Who has 192.168.2.126?  Tell 192.168.2.100  15
15.894551   201.879066  Dell_e8:9e:86   Broadcast   ARP 42  FALSE   Who has 192.168.2.100?  Tell 192.168.2.3    16
0.000274    201.87934   D-Link_be:dd:c3 Dell_e8:9e:86   ARP 60  FALSE   192.168.2.100 is at 5c:d9:98:be:dd:c3   17
0.000673    201.880019  D-Link_be:dd:c3 Broadcast   ARP 60  FALSE   Who has 192.168.2.3?  Tell 192.168.2.100    19
0.000003    201.880022  Dell_e8:9e:86   D-Link_be:dd:c3 ARP 42  FALSE   192.168.2.3 is at 14:fe:b5:e8:9e:86 20
13.224288   215.239135  Dell_e5:d8:59   Broadcast   ARP 60  FALSE   Gratuitous ARP for 192.168.0.120 (Reply)    46
30.759934   245.999069  Dell_e5:d8:59   Broadcast   ARP 60  FALSE   Gratuitous ARP for 192.168.0.120 (Reply)    47
3.992188    255.985896  Dell_e6:c4:ac   Broadcast   ARP 60  FALSE   Who has 192.168.2.100?  Tell 192.168.2.116  49
0.000917    255.986813  D-Link_be:dd:c3 Broadcast   ARP 60  FALSE   Who has 192.168.2.116?  Tell 192.168.2.100  50
0.000231    269.99975   Dell_e8:b0:a5   Broadcast   ARP 60  FALSE   Who has 192.168.2.100?  Tell 192.168.2.2    61
0.000876    270.000626  D-Link_be:dd:c3 Broadcast   ARP 60  FALSE   Who has 192.168.2.2?  Tell 192.168.2.100    62
2.696277    276.760045  Dell_e5:d8:59   Broadcast   ARP 60  FALSE   Gratuitous ARP for 192.168.0.120 (Reply)    67
1.298432    307.478784  Dell_e5:d8:59   Broadcast   ARP 60  FALSE   Gratuitous ARP for 192.168.0.120 (Reply)    84
1.150452    338.238632  Dell_e5:d8:59   Broadcast   ARP 60  FALSE   Gratuitous ARP for 192.168.0.120 (Reply)    103
1.904422    357.00038   D-LinkIn_1f:ec:2a   Broadcast   ARP 60  FALSE   Who has 192.168.2.100?  Tell 192.168.2.1    114
0.000845    357.001225  D-Link_be:dd:c3 Broadcast   ARP 60  FALSE   Who has 192.168.2.1?  Tell 192.168.2.100    115
2.15736 368.99849   Dell_e5:d8:59   Broadcast   ARP 60  FALSE   Gratuitous ARP for 192.168.0.120 (Reply)    122
1.623439    399.759534  Dell_e5:d8:59   Broadcast   ARP 60  FALSE   Gratuitous ARP for 192.168.0.120 (Reply)    141
0.63662 430.4783    Dell_e5:d8:59   Broadcast   ARP 60  FALSE   Gratuitous ARP for 192.168.0.120 (Reply)    159
0.085976    461.238138  Dell_e5:d8:59   Broadcast   ARP 60  FALSE   Gratuitous ARP for 192.168.0.120 (Reply)    178</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-arp" rel="tag" title="see questions tagged &#39;arp&#39;">arp</span> <span class="post-tag tag-link-issue" rel="tag" title="see questions tagged &#39;issue&#39;">issue</span> <span class="post-tag tag-link-network" rel="tag" title="see questions tagged &#39;network&#39;">network</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Dec '11, 02:35</strong></p><img src="https://secure.gravatar.com/avatar/ad926725faf36607ffbd9349f38dabf7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="drawat&#39;s gravatar image" /><p><span>drawat</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="drawat has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>17 Dec '11, 02:42</strong> </span></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span></p></div></div><div id="comments-container-8024" class="comments-container"></div><div id="comment-tools-8024" class="comment-tools"></div><div class="clear"></div><div id="comment-8024-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8025"></span>

<div id="answer-container-8025" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8025-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8025-score" class="post-score" title="current number of votes">0</div><span id="post-8025-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>What is considered normal all depends on the way your network has been set up. The ARP's look OK to me, apart from the ones from 192.168.0.120. Is this a /24 subnet, then it is on the wrong subnet. If it is a /22 or greater, then it's fine.</p><p>However, ARP requests are totally independent on whether you do TCP offloading (checksum, segmentation or even chimney), so I don't really get our question.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Dec '11, 02:50</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-8025" class="comments-container"></div><div id="comment-tools-8025" class="comment-tools"></div><div class="clear"></div><div id="comment-8025-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

