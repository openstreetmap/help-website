+++
type = "question"
title = "How to get the .txt file back to wireshark?"
description = '''An engineer from our group went to customer site and capture their system using Wireshark. Unfortunately he exported the files each time he capture rather than use the save button on the Wireshark... all these exported files are .txt, and we cannot get them back to wireshark... Can anyone help how w...'''
date = "2012-04-06T16:29:00Z"
lastmod = "2012-04-07T21:01:00Z"
weight = 10000
keywords = [ "text2pcap" ]
aliases = [ "/questions/10000" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to get the .txt file back to wireshark?](/questions/10000/how-to-get-the-txt-file-back-to-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10000-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10000-score" class="post-score" title="current number of votes">0</div><span id="post-10000-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>An engineer from our group went to customer site and capture their system using Wireshark. Unfortunately he exported the files each time he capture rather than use the save button on the Wireshark... all these exported files are .txt, and we cannot get them back to wireshark... Can anyone help how we can get these .txt files back to wireshark? o</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-text2pcap" rel="tag" title="see questions tagged &#39;text2pcap&#39;">text2pcap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Apr '12, 16:29</strong></p><img src="https://secure.gravatar.com/avatar/c26c297d2a45fcc16da26d546ade47c1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Cameron&#39;s gravatar image" /><p><span>Cameron</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Cameron has no accepted answers">0%</span></p></div></div><div id="comments-container-10000" class="comments-container"><span id="10001"></span><div id="comment-10001" class="comment"><div id="post-10001-score" class="comment-score"></div><div class="comment-text"><p>Few lines of how it looks like are here:</p><pre><code>No.     Time           Source                Destination           Protocol Length Info
      1 0.000000000    180.100.132.199       239.255.255.250       SSDP     159    M-SEARCH * HTTP/1.1

Frame 1: 159 bytes on wire (1272 bits), 159 bytes captured (1272 bits)
Ethernet II, Src: Dell_b8:3d:c8 (00:26:b9:b8:3d:c8), Dst: IPv4mcast_7f:ff:fa (01:00:5e:7f:ff:fa)
Internet Protocol Version 4, Src: 180.100.132.199 (180.100.132.199), Dst: 239.255.255.250 (239.255.255.250)
User Datagram Protocol, Src Port: tftp-mcast (1758), Dst Port: ssdp (1900)
Hypertext Transfer Protocol

No.     Time           Source                Destination           Protocol Length Info
      2 2.999851000    180.100.132.199       239.255.255.250       SSDP     159    M-SEARCH * HTTP/1.1

Frame 2: 159 bytes on wire (1272 bits), 159 bytes captured (1272 bits)
Ethernet II, Src: Dell_b8:3d:c8 (00:26:b9:b8:3d:c8), Dst: IPv4mcast_7f:ff:fa (01:00:5e:7f:ff:fa)
Internet Protocol Version 4, Src: 180.100.132.199 (180.100.132.199), Dst: 239.255.255.250 (239.255.255.250)
User Datagram Protocol, Src Port: tftp-mcast (1758), Dst Port: ssdp (1900)
Hypertext Transfer Protocol

No.     Time           Source                Destination           Protocol Length Info
      3 5.306301000    Dell_b8:3d:c8         Broadcast             ARP      42     Who has 180.100.132.1?  Tell 180.100.132.199

Frame 3: 42 bytes on wire (336 bits), 42 bytes captured (336 bits)
Ethernet II, Src: Dell_b8:3d:c8 (00:26:b9:b8:3d:c8), Dst: Broadcast (ff:ff:ff:ff:ff:ff)
Address Resolution Protocol (request)

No.     Time           Source                Destination           Protocol Length Info
      4 7.011831000    180.100.132.199       239.255.255.250       SSDP     159    M-SEARCH * HTTP/1.1</code></pre></div><div id="comment-10001-info" class="comment-info"><span class="comment-age">(06 Apr '12, 16:35)</span> <span class="comment-user userinfo">Cameron</span></div></div></div><div id="comment-tools-10000" class="comment-tools"></div><div class="clear"></div><div id="comment-10000-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10002"></span>

<div id="answer-container-10002" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10002-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10002-score" class="post-score" title="current number of votes">3</div><span id="post-10002-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Cameron has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Unfortunately, you can't - the information shown there doesn't, for example, include the <em>entire</em> contents of the SSDP packet, so some of the raw bytes that from which that packet's information was generated aren't reflected in the output.</p><p>You'll either have to use what information you have there to try to diagnose the customer's issue, or you'll have to send somebody out to the customer's site to get more data (and save it as a pcap or pcap-ng file), or get the customer to capture the data themselves.</p><p>(txt2pcap cannot help here - it takes raw packet data, in the form of a hex dump as text, and converts it to raw binary data in a pcap file. There's no raw packet data in the output you have.)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Apr '12, 20:42</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>06 Apr '12, 21:00</strong> </span></p></div></div><div id="comments-container-10002" class="comments-container"><span id="10003"></span><div id="comment-10003" class="comment"><div id="post-10003-score" class="comment-score"></div><div class="comment-text"><p>Thanks... what amazes me is the guy used the import tool in wireshark, and now he cannot get it back to wireshark... that is weird</p></div><div id="comment-10003-info" class="comment-info"><span class="comment-age">(06 Apr '12, 22:24)</span> <span class="comment-user userinfo">Cameron</span></div></div><span id="10005"></span><div id="comment-10005" class="comment"><div id="post-10005-score" class="comment-score"></div><div class="comment-text"><p>(I assume you meant "export tool".)</p><p>The problem here is that the operation is listed in an "Export" menu. It's <em>not</em> an export tool in the sense of writing out all the captured data; Export-&gt;File-&gt;as "Plain Text" file..., unless you check the "Packet bytes" checkbox, writes out either a human-readable top-level summary of the packet or a human-readable description of what's in the packet, rather than writing out the packet data itself.</p><p>I've sent an e-mail to the wireshark-users list suggesting that it be given a different name, to make it clearer that it does <em>not</em> export the packet data.</p></div><div id="comment-10005-info" class="comment-info"><span class="comment-age">(07 Apr '12, 00:05)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="10009"></span><div id="comment-10009" class="comment"><div id="post-10009-score" class="comment-score"></div><div class="comment-text"><p>Thanks Guy.... Yeah you are right I meant export tool. I wish we knew these info in advance..lol</p></div><div id="comment-10009-info" class="comment-info"><span class="comment-age">(07 Apr '12, 10:32)</span> <span class="comment-user userinfo">Cameron</span></div></div><span id="10011"></span><div id="comment-10011" class="comment"><div id="post-10011-score" class="comment-score"></div><div class="comment-text"><p>That's why I asked on the wireshark-users list - if a better name for the menu item would make it more obvious what those items actually do, and, in particular, that they don't save the capture in a form to be read by Wireshark (or other network analyzers), that would be an improvement.</p></div><div id="comment-10011-info" class="comment-info"><span class="comment-age">(07 Apr '12, 21:01)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-10002" class="comment-tools"></div><div class="clear"></div><div id="comment-10002-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

