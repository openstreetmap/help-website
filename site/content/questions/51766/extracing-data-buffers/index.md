+++
type = "question"
title = "Extracing data buffers"
description = '''I have a capture with about 60 packets. Was able to filter down to just the data buffers, but haven&#x27;t found a way to put all the buffers into an text file, that I can annotate later. '''
date = "2016-04-18T14:00:00Z"
lastmod = "2016-04-19T06:23:00Z"
weight = 51766
keywords = [ "extractbuffers" ]
aliases = [ "/questions/51766" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Extracing data buffers](/questions/51766/extracing-data-buffers)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51766-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a capture with about 60 packets. Was able to filter down to just the data buffers, but haven't found a way to put all the buffers into an text file, that I can annotate later.</p></div><div id="question-tags" class="tags-container tags">extractbuffers</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Apr '16, 14:00</strong></p><img src="https://secure.gravatar.com/avatar/5ef9fb3dead46b09fbdf0f2f48592990?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Harpo2&#39;s gravatar image" /><p>Harpo2<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Harpo2 has no accepted answers">0%</span></p></div></div><div id="comments-container-51766" class="comments-container"></div><div id="comment-tools-51766" class="comment-tools"></div><div class="clear"></div><div id="comment-51766-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51784"></span>

<div id="answer-container-51784" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51784-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>but haven't found a way to put all the buffers into an text file,</p></blockquote><p>There are several options to do that. See my answers to similar questions.</p><blockquote><p><a href="https://ask.wireshark.org/questions/38998/automating-extraction-of-udp-payload-from-pcap-file">https://ask.wireshark.org/questions/38998/automating-extraction-of-udp-payload-from-pcap-file</a><br />
<a href="https://ask.wireshark.org/questions/35353/exporting-payload-data-in-binary-file">https://ask.wireshark.org/questions/35353/exporting-payload-data-in-binary-file</a><br />
<a href="https://ask.wireshark.org/questions/47183/bulk-extraction-of-udp-payload-data">https://ask.wireshark.org/questions/47183/bulk-extraction-of-udp-payload-data</a><br />
<a href="https://ask.wireshark.org/questions/29693/export-selected-packet-bytes-how-to-cut-off-the-payload-in-a-pcap-file">https://ask.wireshark.org/questions/29693/export-selected-packet-bytes-how-to-cut-off-the-payload-in-a-pcap-file</a><br />
</p><p>that I can annotate later.</p></blockquote><p>You can annotate the frame in Wireshark if it's a pcap-ng.</p><p>Right click a frame and select <strong>Packet Comment</strong>. Comments will be stored in the pcap-ng if you save the file.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Apr '16, 06:23</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-51784" class="comments-container"></div><div id="comment-tools-51784" class="comment-tools"></div><div class="clear"></div><div id="comment-51784-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

