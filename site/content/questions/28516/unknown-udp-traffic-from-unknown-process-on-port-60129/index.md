+++
type = "question"
title = "Unknown UDP traffic from unknown process on port 60129"
description = '''I have some strange UDP traffics on one Win 7 machine on local port 60129 with a huge amount of connection to random computers. What I can&#x27;t figure out from what process it&#x27;s generated. Have used nestat -a -o -p UDP 1 &amp;gt;log.out for a long time but never seen port 60129 in the log file. I have also...'''
date = "2014-01-01T18:40:00Z"
lastmod = "2014-01-01T20:58:00Z"
weight = 28516
keywords = [ "windows7", "udp", "wireshark" ]
aliases = [ "/questions/28516" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Unknown UDP traffic from unknown process on port 60129](/questions/28516/unknown-udp-traffic-from-unknown-process-on-port-60129)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28516-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have some strange UDP traffics on one Win 7 machine on local port 60129 with a huge amount of connection to random computers. What I can't figure out from what process it's generated. Have used nestat -a -o -p UDP 1 &gt;log.out for a long time but never seen port 60129 in the log file. I have also used ProcessMonitor and TCPView but have never seen any hits and at the same time captured traffic with Wireshark. I also used Port Explorer but it didn't either see this traffic as well. So it's only Wrireshark what has shown the traffic.</p><p>I always get port 60129 even after reboot.</p><p>I have tried to kill one process at the time to see if I could stop the traffic haven't been able to find the process in that way either before the computer rebooted. Would like to avoid using this solution if any other can be used.</p><p>Erland</p></div><div id="question-tags" class="tags-container tags">windows7 udp wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Jan '14, 18:40</strong></p><img src="https://secure.gravatar.com/avatar/00bfd676e32a7353fd8e6e06662b2740?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Erland&#39;s gravatar image" /><p>Erland<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Erland has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 02 Jan '14, 01:03</p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span></p></div></div><div id="comments-container-28516" class="comments-container"></div><div id="comment-tools-28516" class="comment-tools"></div><div class="clear"></div><div id="comment-28516-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="28517"></span>

<div id="answer-container-28517" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28517-score" class="post-score" title="current number of votes">4</div></div></td><td><div class="item-right"><div class="answer-body"><p>Apply a display filter of "frame.len &gt; 300" and examine the displayed packets. You will see a lot more ASCII-readable information. It appears to be list of downloadable video files, with heavy emphasis on Asian names. Some of the listings seem to correspond almost exactly in format to listings found at <a href="http://g.e-hentai.org/">http://g.e-hentai.org/</a> [NSFW], including channel numbers. For example, the listing at <a href="http://g.e-hentai.org/g/659825/a5b0490b1f/">http://g.e-hentai.org/g/659825/a5b0490b1f/</a> [NSFW} corresponds to the data in packet 4274.</p><p>It appears that the titles get blasted to multiple addresses almost simultaneously. For example, with that display filter applied, packets 4274, 4275, 4276, 4278, 4279, 4281, 4282, 4284, 4288, 4289, 4291, 4293, 4299, 4300, 4303, 4305, 4307, 4308, and 4310 all seem to be sending the same information to 20 different destinations, all within less than half a second.</p><p>The destination IP addresses appear to resolve to dynamic addresses that are probably assigned to home users. For example, "179.ppp-dhcp.logic.bm (199.172.197.179)" in packet 4281, and "24-217-69-157.dhcp.stls.mo.charter.com (24.217.69.157)" in packet 4275.</p><p>Most of the listings seem to end with ".zip"</p><p>I don't know what's going on, but my first guess would be some sort of file sharing. You might try capturing with Microsoft Network Monitor and see if it will identify the process responsible for these packets. I'd also do a complete system scan with an up-to-date anti-malware scanner.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Jan '14, 20:58</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 02 Jan '14, 05:41</p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p>Bill Meier ♦♦<br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span></p></div></div><div id="comments-container-28517" class="comments-container"><span id="28519"></span><div id="comment-28519" class="comment"><div id="post-28519-score" class="comment-score"></div><div class="comment-text"><p>Thanks for that excellent answer. Hopefully I should be able to find and delete the process now as I have more of an idea what I'm searching for.</p></div><div id="comment-28519-info" class="comment-info"><span class="comment-age">(02 Jan '14, 00:38)</span> Erland</div></div><span id="28549"></span><div id="comment-28549" class="comment"><div id="post-28549-score" class="comment-score"></div><div class="comment-text"><p>P.S.: If possible, please let us know what you find ....</p></div><div id="comment-28549-info" class="comment-info"><span class="comment-age">(03 Jan '14, 06:53)</span> Bill Meier ♦♦</div></div></div><div id="comment-tools-28517" class="comment-tools"></div><div class="clear"></div><div id="comment-28517-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

