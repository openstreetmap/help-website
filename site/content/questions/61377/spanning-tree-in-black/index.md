+++
type = "question"
title = "Spanning-tree in Black"
description = '''Hi, I was wondering if someone could assist me or guide me on what could be the issue, Recently have had some users complaining of the network a tad bit slow, Im currently running pfSense and did a packet capture though pfSense let run about 3mins. After looking over it saw a lots of ARP requests an...'''
date = "2017-05-12T16:19:00Z"
lastmod = "2017-05-14T02:16:00Z"
weight = 61377
keywords = [ "spanningtree" ]
aliases = [ "/questions/61377" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Spanning-tree in Black](/questions/61377/spanning-tree-in-black)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61377-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61377-score" class="post-score" title="current number of votes">0</div><span id="post-61377-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I was wondering if someone could assist me or guide me on what could be the issue, Recently have had some users complaining of the network a tad bit slow, Im currently running pfSense and did a packet capture though pfSense let run about 3mins. After looking over it saw a lots of ARP requests and a handful of Spanning-tree but in black, I was reading about the Spanning-tree , and correct me if im wrong which is to ensure a loop-free topology for any bridged Ethernet local area network. Right now our Setup is 2 HP switches which the 2nd switch connects to switch 1 nothing complex. But on wireshark it shows Black and saying that the packet was wrong (see packet capture), Also for the ARP request I find it odd because all the LAN has Static IP the DHCP server and the user should not be looking for "who has". Then we also have an SQL server express which run an MRP, which shows the users how long it takes to fill a box in production, they told me it lags alot on chrome, after running the test i saw many TCP retransmission's, but the question is how can debug this or track down the issue? Im attaching the wireshark with the filters</p><p><a href="https://www.mediafire.com/folder/s87uotce7v5wuhm,bzaa43ba6yv6ke2/shared">https://www.mediafire.com/folder/s87uotce7v5wuhm,bzaa43ba6yv6ke2/shared</a></p><p>Thank you</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-spanningtree" rel="tag" title="see questions tagged &#39;spanningtree&#39;">spanningtree</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 May '17, 16:19</strong></p><img src="https://secure.gravatar.com/avatar/dd2630227be6d715406847ade75c3d27?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="killmasta93&#39;s gravatar image" /><p><span>killmasta93</span><br />
<span class="score" title="-1 reputation points">-1</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="killmasta93 has no accepted answers">0%</span></p></div></div><div id="comments-container-61377" class="comments-container"></div><div id="comment-tools-61377" class="comment-tools"></div><div class="clear"></div><div id="comment-61377-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61379"></span>

<div id="answer-container-61379" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61379-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61379-score" class="post-score" title="current number of votes">0</div><span id="post-61379-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><ol><li><p>The spanning tree packets are black (with a default color rule set) because the Ethernet checksum ("Frame Check Sequence", FCS) is zero (meaning, it's "incorrect"). I doubt that this is really true, instead probably being caused by the capture process itself. So I'll say this is just a false positive.</p></li><li><p>ARP has nothing to do with DHCP. ARP is the protocol that tells network nodes (PCs, Routers, etc) what MAC address an IP address is bound to. ARP is always there, except you're running an IPv6 only network, in which case you'd see the same principle implemented via ICMPv6.</p></li><li><p>There are no retransmissions in your 2nd capture, you just captured all packets twice somehow (once without a VLAN tag, once with VLAN tag). The TCP expert of Wireshark gets confused if it sees things twice. But if you remove one half (e.g. the one without the VLAN tags) and export the remaining packets, you'll see that the new file is perfectly fine. To do that, filter on "!(eth.type == 0x8100)" to hide all packets with a VLAN tag and use "Export Specified Packets" from the file menu (make sure the "Displayed" radio button is checked).</p></li></ol><p>So all in all, no problem in your files.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 May '17, 02:02</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-61379" class="comments-container"><span id="61385"></span><div id="comment-61385" class="comment"><div id="post-61385-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the reply, Wow very interesting answer, especially number 3 did not know it can capture the packet twice. So when looking at issue s at latency in a network how can one check it? Been reading and studying about this and most of them say its TCP packet drops or either loops or excessive ARP requests, or i guess what is normal of amount of ARP request?</p><p>Thank you</p></div><div id="comment-61385-info" class="comment-info"><span class="comment-age">(13 May '17, 19:34)</span> <span class="comment-user userinfo">killmasta93</span></div></div><span id="61386"></span><div id="comment-61386" class="comment"><div id="post-61386-score" class="comment-score"></div><div class="comment-text"><p>For more information about TCP analysis and how duplicates can create chaos, check <a href="https://blog.packet-foo.com/2015/03/tcp-analysis-and-the-five-tuple/">https://blog.packet-foo.com/2015/03/tcp-analysis-and-the-five-tuple/</a></p><p>TCP packet loss is the most common reason for latency issues, yes. One way to check if there's really packet loss (and not just retransmissions caused by duplicates) is to verify if you have "previous packet not captured" messages in you capture - if there are none, you don't have packet loss. If you have them, check if there's retransmissions matching the lost sequence numbers, because otherwise it may just be another capture problem.</p><p>Loops aren't really causing latency (well, they do, but that's insignificant in this case), but usually bring whole networks itto a complete overload situation. Which means that basically all communication comes to a halt.</p><p>ARP requests are more or less frequent, and you can try to find devices using excessive ARP. But once a TCP communication starts, ARP isn't involved anymore. So I wouldn't worry that much about it in a TCP latency troubleshooting situation.</p></div><div id="comment-61386-info" class="comment-info"><span class="comment-age">(14 May '17, 02:16)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-61379" class="comment-tools"></div><div class="clear"></div><div id="comment-61379-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

