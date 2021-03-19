+++
type = "question"
title = "Looking for IEC 60870-5 dissector"
description = '''I am looking for IEC 60870-5 101 and/or 104 plugin (dll) for windows 64 bit machine. Where can I download?'''
date = "2017-03-14T10:15:00Z"
lastmod = "2017-03-14T10:34:00Z"
weight = 60069
keywords = [ "iec", "dissector" ]
aliases = [ "/questions/60069" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Looking for IEC 60870-5 dissector](/questions/60069/looking-for-iec-60870-5-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60069-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am looking for IEC 60870-5 101 and/or 104 plugin (dll) for windows 64 bit machine. Where can I download?</p></div><div id="question-tags" class="tags-container tags">iec dissector</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Mar '17, 10:15</strong></p><img src="https://secure.gravatar.com/avatar/d37bb6cf106fdfe0050c1e02fc6fa7e8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ABK&#39;s gravatar image" /><p>ABK<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ABK has no accepted answers">0%</span></p></div></div><div id="comments-container-60069" class="comments-container"></div><div id="comment-tools-60069" class="comment-tools"></div><div class="clear"></div><div id="comment-60069-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="60071"></span>

<div id="answer-container-60071" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60071-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>-104 is a built-in dissector. There is no dissector for -101 as that is normally run over a serial connection, i.e. RS-232 and as such Wireshark doesn't normally include dissectors for such protocols.</p><p>A Google search though found an external project that provides a serial to pcap utility <a href="https://github.com/michaelxzhang/serial_to_pcap">here</a> and a -101 dissector in Lua <a href="https://github.com/michaelxzhang/Wireshark_dissectors">here</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Mar '17, 10:34</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 14 Mar '17, 10:39</p></div></div><div id="comments-container-60071" class="comments-container"><span id="60080"></span><div id="comment-60080" class="comment"><div id="post-60080-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the quick answer. For some reason it does not parse my IEC 104 pcap file (it parses up to the TCP layer only - then it shows the rest as data). I don't see the IEC dissector at the plugin directory. Should it be there? How does it called? From which Wireshark version? Many thanks in advance for the help.</p></div><div id="comment-60080-info" class="comment-info"><span class="comment-age">(15 Mar '17, 00:24)</span> ABK</div></div><span id="60084"></span><div id="comment-60084" class="comment"><div id="post-60084-score" class="comment-score"></div><div class="comment-text"><p>You can confirm the dissector is present and enabled by going to the menu item Analyze -&gt; Enabled Protocols and in the dialog ensure that 104apci and 104asdu are both checked.</p><p>Is your traffic on port 2404, as that's the default port for the dissector?</p><p>If not then right click a packet in the conversation and choose "Decode As ..." and in the resulting dialog choose "104apci" as the protocol.</p><p>You can also set the port in the protocol preferences, again it's named "104apci".</p></div><div id="comment-60084-info" class="comment-info"><span class="comment-age">(15 Mar '17, 03:49)</span> grahamb ♦</div></div></div><div id="comment-tools-60071" class="comment-tools"></div><div class="clear"></div><div id="comment-60071-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

