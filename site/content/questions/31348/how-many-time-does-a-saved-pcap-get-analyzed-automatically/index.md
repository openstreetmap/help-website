+++
type = "question"
title = "How many time does a saved pcap get analyzed automatically?"
description = '''I have a small pcap with just one packet in it. I also have a Lua dissector that analyzes the protocol used in the packet. There is a line of debug info in the dissector. The debug info should only be output once if the packet is analyzed once. To my surprise, when I click on the pcap in Wireshark, ...'''
date = "2014-04-01T07:58:00Z"
lastmod = "2014-04-01T09:13:00Z"
weight = 31348
keywords = [ "analyzed", "multiple", "pcap", "times" ]
aliases = [ "/questions/31348" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How many time does a saved pcap get analyzed automatically?](/questions/31348/how-many-time-does-a-saved-pcap-get-analyzed-automatically)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31348-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>I have a small pcap with just one packet in it. I also have a Lua dissector that analyzes the protocol used in the packet. There is a line of debug info in the dissector. The debug info should only be output once if the packet is analyzed once.</p><p>To my surprise, when I click on the pcap in Wireshark, the debug info is output multiple times. In Mac it is output 18 times, and in Windows, it is output 3 times.</p><p>Why is this?</p></div><div id="question-tags" class="tags-container tags">analyzed multiple pcap times</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Apr '14, 07:58</strong></p><img src="https://secure.gravatar.com/avatar/b18cada3e3589f311e24f5ffbd1737bc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="YXI&#39;s gravatar image" /><p>YXI<br />
<span class="score" title="21 reputation points">21</span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="YXI has no accepted answers">0%</span></p></div></div><div id="comments-container-31348" class="comments-container"></div><div id="comment-tools-31348" class="comment-tools"></div><div class="clear"></div><div id="comment-31348-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="31352"></span>

<div id="answer-container-31352" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31352-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>First the entire file is read is read in sequence then packets are read "by the GUI" to display them. If a packet is "clicked" it will be re-read if the packet list is scrolled the packet the packets that becomes vissible will be re-read. Why the MAC (Qt?) version reads them 18 times I don't know.(There is a bug report about that.)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Apr '14, 09:13</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-31352" class="comments-container"><span id="31436"></span><div id="comment-31436" class="comment"><div id="post-31436-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Why the MAC (Qt?) version reads them 18 times I don't know.</p></blockquote><p>don't they claim to have the better (best) system? So, I guess they do everything better than windows, even analyzing a frame in Wireshark. And what is better than 3 times? Of course: 18 times ;-))</p></div><div id="comment-31436-info" class="comment-info"><span class="comment-age">(02 Apr '14, 13:57)</span> Kurt Knochner ♦</div></div><span id="31440"></span><div id="comment-31440" class="comment"><div id="post-31440-score" class="comment-score"></div><div class="comment-text"><p>But it only takes the Mac the same time to analyze it 18 times, as it takes Windows to analyze it 3 times. ;)</p></div><div id="comment-31440-info" class="comment-info"><span class="comment-age">(02 Apr '14, 14:11)</span> Hadriel</div></div><span id="31441"></span><div id="comment-31441" class="comment"><div id="post-31441-score" class="comment-score"></div><div class="comment-text"><p>dammit .....</p></div><div id="comment-31441-info" class="comment-info"><span class="comment-age">(02 Apr '14, 14:17)</span> Kurt Knochner ♦</div></div><span id="31442"></span><div id="comment-31442" class="comment"><div id="post-31442-score" class="comment-score"></div><div class="comment-text"><p>What about Linux? I bet those smart guys can make in one shot and less than half the time, it takes to boil an egg in the center of the sun.</p></div><div id="comment-31442-info" class="comment-info"><span class="comment-age">(02 Apr '14, 14:18)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-31352" class="comment-tools"></div><div class="clear"></div><div id="comment-31352-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

