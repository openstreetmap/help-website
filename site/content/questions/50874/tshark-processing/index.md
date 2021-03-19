+++
type = "question"
title = "Tshark Processing"
description = '''Hi All, 1) How to reduce the TSHARK processing time when PCAP file size is more? 2) how to use the &quot;Memory mapped file&quot; with tshark command? Thanks in advancce. Regards, Swathi.'''
date = "2016-03-13T22:33:00Z"
lastmod = "2016-03-13T22:33:00Z"
weight = 50874
keywords = [ "tshark", "wireshark" ]
aliases = [ "/questions/50874" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Tshark Processing](/questions/50874/tshark-processing)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50874-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All,</p><p>1) How to reduce the TSHARK processing time when PCAP file size is more?</p><p>2) how to use the "Memory mapped file" with tshark command?</p><p>Thanks in advancce.</p><p>Regards, Swathi.</p></div><div id="question-tags" class="tags-container tags">tshark wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Mar '16, 22:33</strong></p><img src="https://secure.gravatar.com/avatar/a34282ab2b31d84bc63d5ea83c15d775?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="swathi%20jakkam&#39;s gravatar image" /><p>swathi jakkam<br />
<span class="score" title="6 reputation points">6</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="swathi jakkam has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 13 Mar '16, 23:08</p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span></p></div></div><div id="comments-container-50874" class="comments-container"><span id="50883"></span><div id="comment-50883" class="comment"><div id="post-50883-score" class="comment-score"></div><div class="comment-text"><p>"how to use the "Memory mapped file" with tshark command?" What do you mean by "use the memory mapped file"? TShark and Wireshark don't memory-map the file they read, they just do regular file read operations on it; when <em>capturing</em> traffic, it might memory-map the buffer(s) into which the kernel deposits packets, <em>if</em> both the version of libpcap used and the underlying OS support it (which, for now, means "on Linux with newer libpcap and possibly on FreeBSD with newer libpcap and nowhere else).</p></div><div id="comment-50883-info" class="comment-info"><span class="comment-age">(14 Mar '16, 03:08)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-50874" class="comment-tools"></div><div class="clear"></div><div id="comment-50874-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

