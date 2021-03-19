+++
type = "question"
title = "Using Google Protobuf to Export Full Packet Dissection Data via Named Pipe"
description = '''Apologies in advance if this question is a bit long-ish. I&#x27;ve been wondering why Wireshark/tshark doesn&#x27;t offer the option to export full packet dissection data via named pipe (serialized binary data). Is this due to design philosophy, lack of offers to write the code, or some other reason? Of cours...'''
date = "2017-07-10T15:14:00Z"
lastmod = "2017-07-11T02:27:00Z"
weight = 62651
keywords = [ "pipe", "export", "protobuf" ]
aliases = [ "/questions/62651" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Using Google Protobuf to Export Full Packet Dissection Data via Named Pipe](/questions/62651/using-google-protobuf-to-export-full-packet-dissection-data-via-named-pipe)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62651-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Apologies in advance if this question is a bit long-ish.</p><p>I've been wondering why Wireshark/tshark doesn't offer the option to export full packet dissection data via named pipe (serialized binary data). Is this due to design philosophy, lack of offers to write the code, or some other reason? Of course, packet dissection data can be written out to stdout or a file in xml format. Perhaps this meets most needs?</p><p>Reason for the question is that I needed a dissection data export option that was more efficient than xml. My solution was to modify tshark so it can leverage Google Protocol Buffers to export packet dissection data as serialized binary data. Serialized dissection data is written out to a named pipe. Protobuf dissect tree creation, serialization, export code is all written in C++ and takes advantage of all the optimization work Google has put into its Protobuf library. The client/read side of the pipe can be written in any language supported by the Protobuf library. I wrote mine in Python. The client reads and parses the serialized dissection data (again) using Google Protobuf lib recreating dissection tree data on client side.</p><p>Would it be advantageous to incorporate the above Protobuf approach into the Wireshark project or would the community consider it unnecessary or perhaps undesirable?</p><p>If you're curious about implementation, you can see my project at the following location: <a href="https://gitlab.com/MLandriscina/protoShark.git.">https://gitlab.com/MLandriscina/protoShark.git.</a> This is the first time that I've used Protobuf, so I wouldn't be surprised to discover that better implementations are possible.</p></div><div id="question-tags" class="tags-container tags">pipe export protobuf</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Jul '17, 15:14</strong></p><img src="https://secure.gravatar.com/avatar/8796d1959a2bd93f101396e870584341?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="markLand&#39;s gravatar image" /><p>markLand<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="markLand has no accepted answers">0%</span></p></div></div><div id="comments-container-62651" class="comments-container"></div><div id="comment-tools-62651" class="comment-tools"></div><div class="clear"></div><div id="comment-62651-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="62660"></span>

<div id="answer-container-62660" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62660-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I think the best place to discuss this would be the <a href="https://www.wireshark.org/mailman/listinfo/wireshark-dev">developer mailing list</a>.</p><p>A guide to submitting changes can be found on the wiki <a href="https://wiki.wireshark.org/CreatingPatches">here</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Jul '17, 02:27</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-62660" class="comments-container"></div><div id="comment-tools-62660" class="comment-tools"></div><div class="clear"></div><div id="comment-62660-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

