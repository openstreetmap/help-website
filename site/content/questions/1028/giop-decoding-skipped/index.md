+++
type = "question"
title = "giop decoding skipped?"
description = '''In WireShark 1.4.2 I&#x27;m trying to create pcap dumps of GIOP data so I can peer into the giop details more easily. I&#x27;m starting with a hex dump, converted to pcap with: text2pcap -o dec -T 50,60 c:out.txt c:out.pcap (out.txt is at the end of this message for reference) And opening the resulting pcap f...'''
date = "2010-11-19T15:00:00Z"
lastmod = "2010-11-23T13:08:00Z"
weight = 1028
keywords = [ "giop" ]
aliases = [ "/questions/1028" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [giop decoding skipped?](/questions/1028/giop-decoding-skipped)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1028-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In WireShark 1.4.2 I'm trying to create pcap dumps of GIOP data so I can peer into the giop details more easily.</p><p>I'm starting with a hex dump, converted to pcap with: text2pcap -o dec -T 50,60 c:out.txt c:out.pcap</p><p>(out.txt is at the end of this message for reference)</p><p>And opening the resulting pcap file in WireShark everything down to the TCP frame looks OK except that the payload isn't displayed, not even as raw data.</p><p>Am I missing something?</p><p>Thanks,<br />
Rob</p><p>000000 47 49 4f 50 01 02 00 00 00 00 ca fe 00 00 0d 60<br />
000016 03 00 00 00 00 00 00 00 00 00 00 19 ff 6d 61 6e<br />
000032 61 67 65 72 50 4f 41 fe d0 68 10 4c 01 00 54 b8<br />
000048 00 00 00 00 00 00 00 00 00 00 00 12 6e 65 77 52<br />
000064 65 71 75 65 73 74 48 61 6e 64 6c 65 72 00 00 00<br />
000080 00 00 00 04 00 00 00 05 00 00 00 1e 00 00 00 00<br />
000096 00 00 00 01 00 00 00 0f 31 39 32 2e 31 36 38 2e<br />
000112 36 35 2e 31 38 31 00 00 00 00 00 00 00 00 00 01<br />
000128 00 00 00 0c 00 00 00 00 00 01 00 01 00 01 01 09<br />
000144 00 00 00 0f 00 00 00 20 00 00 00 00 00 00 00 00<br />
000160 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00<br />
000176 01 00 00 00 00 00 00 00 42 45 41 00 00 00 00 04<br />
000192 00 09 02 03<br />
</p></div><div id="question-tags" class="tags-container tags">giop</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Nov '10, 15:00</strong></p><img src="https://secure.gravatar.com/avatar/ab546c7a8054af206861b51e352126ee?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="eboregelna&#39;s gravatar image" /><p>eboregelna<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="eboregelna has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-1028" class="comments-container"></div><div id="comment-tools-1028" class="comment-tools"></div><div class="clear"></div><div id="comment-1028-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="1088"></span>

<div id="answer-container-1088" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1088-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I have an answer to my question:</p><p>The GIOP packets being reported as data sent from webLogic's corba debugging are having their 'message size' field stomped on before being logged. Therefore the GIOP dissector wants to see more data before it reports the packet.</p><p>I avoided the issue for now as I don't really need the sent packets, just the received. If I did need them I'd have my script to extract the data from the logs reconstruct the length from context in the log file.</p><p>-Rob</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Nov '10, 13:08</strong></p><img src="https://secure.gravatar.com/avatar/ab546c7a8054af206861b51e352126ee?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="eboregelna&#39;s gravatar image" /><p>eboregelna<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="eboregelna has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-1088" class="comments-container"></div><div id="comment-tools-1088" class="comment-tools"></div><div class="clear"></div><div id="comment-1088-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

