+++
type = "question"
title = "Bandwidth I/O graph and packet capture mode"
description = '''Dear all, Is it possible to get an accurate and correct Bandwidth I/O graph without capturing full packet? In addition, if there is need for long capture time required, do you have recommendation or precaution? Thanks.'''
date = "2013-10-22T20:08:00Z"
lastmod = "2013-10-28T08:32:00Z"
weight = 26307
keywords = [ "bandwidth", "packet-capture" ]
aliases = [ "/questions/26307" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Bandwidth I/O graph and packet capture mode](/questions/26307/bandwidth-io-graph-and-packet-capture-mode)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26307-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Dear all,</p><p>Is it possible to get an accurate and correct Bandwidth I/O graph without capturing full packet?</p><p>In addition, if there is need for long capture time required, do you have recommendation or precaution?</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags">bandwidth packet-capture</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Oct '13, 20:08</strong></p><img src="https://secure.gravatar.com/avatar/1c609caed0650f22ccc1ffd5f4706a65?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Applepie2&#39;s gravatar image" /><p>Applepie2<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Applepie2 has no accepted answers">0%</span></p></div></div><div id="comments-container-26307" class="comments-container"></div><div id="comment-tools-26307" class="comment-tools"></div><div class="clear"></div><div id="comment-26307-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="26470"></span>

<div id="answer-container-26470" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26470-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Is it possible to get an accurate and correct Bandwidth I/O graph without capturing full packet?</p></blockquote><p>yes, as Wireshark uses the information about the frame length, stored in the pcap file for each frame.</p><blockquote><p>In addition, if there is need for long capture time required, do you have recommendation or precaution?</p></blockquote><p>Yes.</p><ul><li>reduce the amount of captured data by using 'strict' capture filters</li><li><strong>capture with dumpcap</strong> instead of Wireshark. Don't use tshark either. Both are rather analyzing tools than capture tools.</li><li>If you want to capture with Wireshark (not recommended for a long period of time)</li><li>add enough RAM to your capturing machine (2 Gig is 'nothing' nowadays ;-))</li><li>use a 64 Bit OS, to be able to use that RAM</li><li>reduce the captured frame size (option -s for tcpdump and/or dumpcap)</li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Oct '13, 08:32</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 28 Oct '13, 08:34</p></div></div><div id="comments-container-26470" class="comments-container"></div><div id="comment-tools-26470" class="comment-tools"></div><div class="clear"></div><div id="comment-26470-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

