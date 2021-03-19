+++
type = "question"
title = "wireshark placement"
description = '''Hey guys, I would appreciate some help on the following scenario.  We are running a backup of the Exchange Server to a NAS device.  The Exchange Server (backup agent installed) is connected via a HP Procurve 2500 Switch to the Backup software. The Backup Server is connected via another HP switch to ...'''
date = "2015-03-20T01:06:00Z"
lastmod = "2015-03-20T01:34:00Z"
weight = 40711
keywords = [ "placement", "wireshark" ]
aliases = [ "/questions/40711" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [wireshark placement](/questions/40711/wireshark-placement)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40711-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey guys,</p><p>I would appreciate some help on the following scenario.</p><p>We are running a backup of the Exchange Server to a NAS device.</p><p>The Exchange Server (backup agent installed) is connected via a HP Procurve 2500 Switch to the Backup software. The Backup Server is connected via another HP switch to a NAS device. The problem is that our daily backup fails with a communication error (almost always at same byte count).</p><p>My question is where would I have to place wireshark, also which capture filter should I use ( If I track everything I’m afraid our systems may suffer performance issues). So should I place Wireshark between the Exchange and Backup Server (or on both )? Or between the Backup Server and the NAS with a capture filter Backup Servers IP + NAS IP.</p><p>From a test capture it looks like it runs over SMB2.</p><p>Any suggestion much appreciated !</p></div><div id="question-tags" class="tags-container tags">placement wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Mar '15, 01:06</strong></p><img src="https://secure.gravatar.com/avatar/2b3f26f3a24449776af62dd8cca7715a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="adasko&#39;s gravatar image" /><p>adasko<br />
<span class="score" title="86 reputation points">86</span><span title="34 badges"><span class="badge1">●</span><span class="badgecount">34</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="adasko has no accepted answers">0%</span></p></div></div><div id="comments-container-40711" class="comments-container"></div><div id="comment-tools-40711" class="comment-tools"></div><div class="clear"></div><div id="comment-40711-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="40715"></span>

<div id="answer-container-40715" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40715-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you can, capture between Exchange and Backup and between Backup and NAS simultaneously. The capture filter can be "host Exchange and host Backup". You can use the same host syntax for the other side "host Backup and host NAS". Replace the names in the capture filter with the relevant IPs. Afterwards you can upload the packet captures to Cloudshark if you need help analyzing them.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Mar '15, 01:34</strong></p><img src="https://secure.gravatar.com/avatar/721b9692d2a30fc3b386b7fae9a44220?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland&#39;s gravatar image" /><p>Roland<br />
<span class="score" title="764 reputation points">764</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland has 9 accepted answers">13%</span></p></div></div><div id="comments-container-40715" class="comments-container"><span id="40716"></span><div id="comment-40716" class="comment"><div id="post-40716-score" class="comment-score"></div><div class="comment-text"><p>thank you. and what about if the Full backup ALWAYS fails on 109 GB. could this be an indication that the Server is corrupted in some way ? i can see that the Exchange DB's System State are being backed up.</p><p>many thanks</p></div><div id="comment-40716-info" class="comment-info"><span class="comment-age">(20 Mar '15, 03:28)</span> adasko</div></div><span id="40718"></span><div id="comment-40718" class="comment"><div id="post-40718-score" class="comment-score"></div><div class="comment-text"><p>I assume you have enough free space on the NAS :) It depends what you see in the packet capture. Do you see TCP Windows Full or TCP Zero Window for a long period of time?</p></div><div id="comment-40718-info" class="comment-info"><span class="comment-age">(20 Mar '15, 04:17)</span> Roland</div></div><span id="40719"></span><div id="comment-40719" class="comment"><div id="post-40719-score" class="comment-score"></div><div class="comment-text"><p>yes place is enough. let me do the Wireshark capture and check. will post about the results. thank you !</p></div><div id="comment-40719-info" class="comment-info"><span class="comment-age">(20 Mar '15, 04:23)</span> adasko</div></div><span id="40735"></span><div id="comment-40735" class="comment"><div id="post-40735-score" class="comment-score"></div><div class="comment-text"><p>if i have the trace file. should i filter only for SMB /SMB2 like with a filter "smb or smb2" because i cannot see much TCP packets</p></div><div id="comment-40735-info" class="comment-info"><span class="comment-age">(20 Mar '15, 08:19)</span> adasko</div></div><span id="40736"></span><div id="comment-40736" class="comment"><div id="post-40736-score" class="comment-score">1</div><div class="comment-text"><p>SMB runs on top of TCP. Filter for the relevant tcp stream, look at what happens in the packet capture when the backup fails.</p></div><div id="comment-40736-info" class="comment-info"><span class="comment-age">(20 Mar '15, 08:25)</span> Roland</div></div></div><div id="comment-tools-40715" class="comment-tools"></div><div class="clear"></div><div id="comment-40715-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

