+++
type = "question"
title = "Finding duplicate IP addresses"
description = '''The link https://www.safaribooksonline.com/library/view/packet-analysis-with/9781785887819/ch07s04.html states that you can use the arp.duplicate-address-frame Wireshark filter to display duplicate IP information frames. It goes on to say that you open the ARP_Duplicate_IP.pcap file and apply the ar...'''
date = "2017-01-31T07:22:00Z"
lastmod = "2017-01-31T08:03:00Z"
weight = 59180
keywords = [ "arp", "ip", "duplicate" ]
aliases = [ "/questions/59180" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Finding duplicate IP addresses](/questions/59180/finding-duplicate-ip-addresses)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59180-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>The link <a href="https://www.safaribooksonline.com/library/view/packet-analysis-with/9781785887819/ch07s04.html">https://www.safaribooksonline.com/library/view/packet-analysis-with/9781785887819/ch07s04.html</a> states that you can use the arp.duplicate-address-frame Wireshark filter to display duplicate IP information frames. It goes on to say that you open the ARP_Duplicate_IP.pcap file and apply the arp.duplicate-address-frame filter. After installing Wireshark I do not see any pcap files on the installed PC and do not see any arp.duplicate filters. What am I missing? Also, if there is another way to find duplicate IP addresses, please provide step-by-step directions. I'm new to Wireshark.</p></div><div id="question-tags" class="tags-container tags">arp ip duplicate</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Jan '17, 07:22</strong></p><img src="https://secure.gravatar.com/avatar/27950bcd1352123bd8b525a077d6cdae?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Willie%20T&#39;s gravatar image" /><p>Willie T<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Willie T has no accepted answers">0%</span></p></div></div><div id="comments-container-59180" class="comments-container"></div><div id="comment-tools-59180" class="comment-tools"></div><div class="clear"></div><div id="comment-59180-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="59182"></span>

<div id="answer-container-59182" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59182-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>This is a snapshot of part of the book, which (assumed) also provides the referenced capture files. These do not come with a Wireshark installation.</p><p>The arp.duplicate-address-frame display filter can indeed be used to filter ARP packets which cause this field to be generated. It can be found in <a href="https://www.wireshark.org/docs/dfref/a/arp.html">this list</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Jan '17, 08:03</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-59182" class="comments-container"><span id="59188"></span><div id="comment-59188" class="comment"><div id="post-59188-score" class="comment-score"></div><div class="comment-text"><p>I had seen that web page and the line with arp.duplicate-address-frame. However, in Wireshark I could not figure out how to reference arp.duplicatate-address-frame as a filter. When I click on the drop down for the capture filters, the only ones that I see related to arp are "No ARP: not arp" and "No ARP and no DNS:not arp and !(udp.port == 53)". I did install WinPcap. Guess I must be missing something.</p></div><div id="comment-59188-info" class="comment-info"><span class="comment-age">(31 Jan '17, 10:46)</span> Willie T</div></div></div><div id="comment-tools-59182" class="comment-tools"></div><div class="clear"></div><div id="comment-59182-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

