+++
type = "question"
title = "Wireshark for Precise Timing"
description = '''Hi, I was hoping someone could help me better understand Wireshark timing. I am trying to measure the latency of packets time tagged using a GPS clock. The device time tags the packet and then sends it to a destination. Using the top of the second packet, I am measuring the latency of the device (an...'''
date = "2011-06-20T07:35:00Z"
lastmod = "2011-06-20T07:35:00Z"
weight = 4635
keywords = [ "timestamp", "winpcap", "gps" ]
aliases = [ "/questions/4635" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark for Precise Timing](/questions/4635/wireshark-for-precise-timing)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4635-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I was hoping someone could help me better understand Wireshark timing. I am trying to measure the latency of packets time tagged using a GPS clock. The device time tags the packet and then sends it to a destination. Using the top of the second packet, I am measuring the latency of the device (and simple network) by observing the time difference between when Wireshark reads the packet and the top of the second.</p><p>I have synchronized a Windows PC using a Symmetricom bus level timing card, and I believe Wireshark uses this to get its time prior to a capture. My question is how accurate is this query of the time? I believe I read somewhere that Wireshark uses the WinPcap driver to get time, and that driver has an accuracy of up to 10ms...? And during a capture, how accurate does the time remain for say 100ms? Is the inaccuracy in time constant or does it vary over a given capture?</p><p>Thank you.</p></div><div id="question-tags" class="tags-container tags">timestamp winpcap gps</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Jun '11, 07:35</strong></p><img src="https://secure.gravatar.com/avatar/144e0571de8abdc8fafbd3118bb18f81?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="quintr&#39;s gravatar image" /><p>quintr<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="quintr has no accepted answers">0%</span></p></div></div><div id="comments-container-4635" class="comments-container"></div><div id="comment-tools-4635" class="comment-tools"></div><div class="clear"></div><div id="comment-4635-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

