+++
type = "question"
title = "how to display flowid alongwith frame number for each packet of a pcap using tshark/wireshark"
description = '''Is there any concept of flow id in tshark ? When i searched for filters, i found out that tcp.stream exists but its equivalent for udp i.e udp.stream doesn&#x27;t exist. When i open a pcap, by default it shows the frame number, ip addresses, info etc. In one column i also need the flow id of each packet ...'''
date = "2012-10-20T22:06:00Z"
lastmod = "2012-10-30T03:05:00Z"
weight = 15118
keywords = [ "flow", "packet-capture", "pcap", "tshark", "wireshark" ]
aliases = [ "/questions/15118" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [how to display flowid alongwith frame number for each packet of a pcap using tshark/wireshark](/questions/15118/how-to-display-flowid-alongwith-frame-number-for-each-packet-of-a-pcap-using-tsharkwireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15118-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15118-score" class="post-score" title="current number of votes">0</div><span id="post-15118-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is there any concept of flow id in tshark ? When i searched for filters, i found out that <strong>tcp.stream</strong> exists but its equivalent for udp i.e <strong>udp.stream</strong> doesn't exist. When i open a pcap, by default it shows the frame number, ip addresses, info etc. In one column i also need the flow id of each packet alongwith the frame number. Does tshark provide such support ? If not, Is there any way i can do this ?</p><p>I have written a program where i am reading a pcap file, packet by packet and i need the flowid for each packet read. If i use tshark command as</p><pre><code> ./tshark -r in.pcap -z conv,tcp</code></pre><p>it displays the packet number alongwith some other details, but i want the flowid also to be displayed which i can read in my program.</p><p>any help will be greatly appreciated. thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-flow" rel="tag" title="see questions tagged &#39;flow&#39;">flow</span> <span class="post-tag tag-link-packet-capture" rel="tag" title="see questions tagged &#39;packet-capture&#39;">packet-capture</span> <span class="post-tag tag-link-pcap" rel="tag" title="see questions tagged &#39;pcap&#39;">pcap</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Oct '12, 22:06</strong></p><img src="https://secure.gravatar.com/avatar/ce14610470a60c9adcc5f03599f66608?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="viks&#39;s gravatar image" /><p><span>viks</span><br />
<span class="score" title="16 reputation points">16</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="viks has no accepted answers">0%</span></p></div></div><div id="comments-container-15118" class="comments-container"><span id="15287"></span><div id="comment-15287" class="comment"><div id="post-15287-score" class="comment-score"></div><div class="comment-text"><p>i just need the udp flow id (similar to that given by tcp.stream for the tcp flows) for the udp packets. plz let me know how to do that ? thanks</p></div><div id="comment-15287-info" class="comment-info"><span class="comment-age">(26 Oct '12, 01:08)</span> <span class="comment-user userinfo">viks</span></div></div></div><div id="comment-tools-15118" class="comment-tools"></div><div class="clear"></div><div id="comment-15118-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="15328"></span>

<div id="answer-container-15328" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15328-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15328-score" class="post-score" title="current number of votes">1</div><span id="post-15328-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="viks has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Unfortunately, there is no "UDP stream/flow" recorded in Wireshark. The best you can do is to print the UDP conversations and then filter on the connection parameters (IP + port) with a script in a second run.</p><blockquote><p><code>tshark -n -q -r input.cap -z conv,udp</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Oct '12, 04:20</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-15328" class="comments-container"><span id="15348"></span><div id="comment-15348" class="comment"><div id="post-15348-score" class="comment-score"></div><div class="comment-text"><p><span>@kurt</span> : thanks for the reply. for the tshark command that u told, i will get the src(ip+port), dest(ip+port) and that alongwith transport proto (tcp/udp) will give me the 5tuple. Now how to calculate flowid from that. Can you please let me know how to calculate that using some script or c code ? Is there some already existing library which provides this functionality ?</p></div><div id="comment-15348-info" class="comment-info"><span class="comment-age">(30 Oct '12, 00:16)</span> <span class="comment-user userinfo">viks</span></div></div><span id="15356"></span><div id="comment-15356" class="comment"><div id="post-15356-score" class="comment-score"></div><div class="comment-text"><p><span>@viks</span>, there is no "flowid" or anything similar, neither in UDP nor in Wireshark. However, you can "simulate" that in your script. As soon as the first packet with a yet unseen 5-tupel appears, you remember that conversation as "flow" number #1, then you proceed in the same way with all other conversations. Usually this is done with a hash table where the 5-tuple is the key to the hash table.</p></div><div id="comment-15356-info" class="comment-info"><span class="comment-age">(30 Oct '12, 03:05)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-15328" class="comment-tools"></div><div class="clear"></div><div id="comment-15328-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

