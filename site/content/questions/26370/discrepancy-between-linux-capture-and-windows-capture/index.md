+++
type = "question"
title = "discrepancy between linux capture and windows capture"
description = '''Wireshark 1.10.2 (64 bit) on Windows 7, Wireshark 1.10 on Ubuntu 13.04 (compiled from source) I have been troubleshooting a network that contains several Windows Embedded Std 7 POS systems and a back office PC that runs Win 7 Pro. When I first looked at the network I was amazed at the volume of erro...'''
date = "2013-10-24T10:33:00Z"
lastmod = "2013-10-24T10:33:00Z"
weight = 26370
keywords = [ "windows", "differences", "dump", "linux" ]
aliases = [ "/questions/26370" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [discrepancy between linux capture and windows capture](/questions/26370/discrepancy-between-linux-capture-and-windows-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26370-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Wireshark 1.10.2 (64 bit) on Windows 7, Wireshark 1.10 on Ubuntu 13.04 (compiled from source)</p><p>I have been troubleshooting a network that contains several Windows Embedded Std 7 POS systems and a back office PC that runs Win 7 Pro. When I first looked at the network I was amazed at the volume of errors (dup ack, retrans, tcp out of order). My initial look was with the back office PC on a hub with a laptop running Win 7 Pro and wireshark. Wondering if I had an interface issue, I put a netoptics tap on the back office PC connection. My windows laptop only has one wired ethernet interface so I put a Ubuntu Linux box with two wired interfaces and when I captured with it the errors magically 'disappeared'. I then bought a USB -&gt; wired ethernet dongle for my laptop and ran wireshark on both interfaces (still on the tap) and the errors show again. I have never seen this situation before and don't know where to turn next - I can't trust any captures done on my Windows 7 laptop now and can't take my Linux desktop PC with me on the road!</p><p>Why would Wireshark on windows be showing that the network has errors (thousands of them per minute) but on Linux it is clean?<br />
</p><p>If I run a tcpdump (or dumpcap) capture on the Linux box then copy the file to the Windows machine, it does not have the errors showing.</p><p>I wonder if this is a winpcap issue or a wireshark issue?</p></div><div id="question-tags" class="tags-container tags">windows differences dump linux</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Oct '13, 10:33</strong></p><img src="https://secure.gravatar.com/avatar/6bd95527de0eb7974ffb23e6169010ee?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PhilN&#39;s gravatar image" /><p>PhilN<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PhilN has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 24 Oct '13, 10:38</p></div></div><div id="comments-container-26370" class="comments-container"><span id="26371"></span><div id="comment-26371" class="comment"><div id="post-26371-score" class="comment-score"></div><div class="comment-text"><p>Maybe pertinent as well.... I used an Ubuntu Live CD in the laptop that normally runs Windows and captured via tcpdump (using built in interface and USB-&gt;ethernet dongle) and came up with a clean capture that way as well. I then used windump and captured two separate files (one from each interface) and merged them. That was even worse.</p><p>This is definitely a difference between windows and linux and how they capture but I can't fathom how there can be such a difference.<br />
</p></div><div id="comment-26371-info" class="comment-info"><span class="comment-age">(24 Oct '13, 10:37)</span> PhilN</div></div><span id="26475"></span><div id="comment-26475" class="comment"><div id="post-26475-score" class="comment-score"></div><div class="comment-text"><p>From your description, I don't fully understand when the error occurs. Can you please describe your test cases and the results as detailed as possible?</p></div><div id="comment-26475-info" class="comment-info"><span class="comment-age">(28 Oct '13, 08:51)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-26370" class="comment-tools"></div><div class="clear"></div><div id="comment-26370-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

