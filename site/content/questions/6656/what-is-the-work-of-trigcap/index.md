+++
type = "question"
title = "what is the work of trigcap?"
description = '''Can any one explain the main objective of trigcap.c and also its functioning briefly?'''
date = "2011-10-01T00:12:00Z"
lastmod = "2011-10-01T01:06:00Z"
weight = 6656
keywords = [ "triggers" ]
aliases = [ "/questions/6656" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [what is the work of trigcap?](/questions/6656/what-is-the-work-of-trigcap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6656-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Can any one explain the main objective of trigcap.c and also its functioning briefly?</p></div><div id="question-tags" class="tags-container tags">triggers</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Oct '11, 00:12</strong></p><img src="https://secure.gravatar.com/avatar/968cc7ddfc48322ffbd1d7f5e3d37b85?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Terrestrial%20shark&#39;s gravatar image" /><p>Terrestrial ...<br />
<span class="score" title="96 reputation points">96</span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="28 badges"><span class="silver">●</span><span class="badgecount">28</span></span><span title="29 badges"><span class="bronze">●</span><span class="badgecount">29</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Terrestrial shark has 3 accepted answers">42%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 01 Oct '11, 02:54</p></div></div><div id="comments-container-6656" class="comments-container"></div><div id="comment-tools-6656" class="comment-tools"></div><div class="clear"></div><div id="comment-6656-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6659"></span>

<div id="answer-container-6659" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6659-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>It uses the BPF to find start and stop conditions. Between the two it saves captured packets to a file.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Oct '11, 01:06</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-6659" class="comments-container"><span id="6661"></span><div id="comment-6661" class="comment"><div id="post-6661-score" class="comment-score"></div><div class="comment-text"><p>i'm just a beginner so could you please explain me how to use it at runtime? can you forward or post the info related to this here?</p></div><div id="comment-6661-info" class="comment-info"><span class="comment-age">(01 Oct '11, 01:09)</span> Terrestrial ...</div></div><span id="6667"></span><div id="comment-6667" class="comment"><div id="post-6667-score" class="comment-score"></div><div class="comment-text"><p>It's a command line tool with the following syntax: <code>trigcap -w outfile -b begin -e end [-f capture] [-i iface] [-s snaplen] [-p] [-q] [-d [-d [-d [-d]]]]</code></p><p>When capture filter expression <code>begin</code> becomes true start capturing frames in <code>outfile</code> until capture filter expression <code>end</code> becomes true. Example:</p><p><code>tripcap -w mycap.pcap -b "ip[0]!=45" -e "tcp[tcpflags]&amp;tcp-syn==tcp-syn"</code></p><p>This starts capturing frames into mycap.pcap after an IPv4 packet with options is seen, and stops after TCP syn flag is seen.</p></div><div id="comment-6667-info" class="comment-info"><span class="comment-age">(01 Oct '11, 02:36)</span> Jaap ♦</div></div><span id="6668"></span><div id="comment-6668" class="comment"><div id="post-6668-score" class="comment-score"></div><div class="comment-text"><p>cmd prompt isn't recognizing it as a process.what should be my path at the dos prompt? (Also i didn't found any executable called trigcap inside the wireshark folder)</p></div><div id="comment-6668-info" class="comment-info"><span class="comment-age">(01 Oct '11, 02:53)</span> Terrestrial ...</div></div><span id="6671"></span><div id="comment-6671" class="comment"><div id="post-6671-score" class="comment-score"></div><div class="comment-text"><p>i read bug 2039 and came to know that windows cannot run the trigcap. But thats the matter of year 2007. Any new updates with triggers on windows now?</p></div><div id="comment-6671-info" class="comment-info"><span class="comment-age">(01 Oct '11, 03:58)</span> Terrestrial ...</div></div><span id="6695"></span><div id="comment-6695" class="comment"><div id="post-6695-score" class="comment-score"></div><div class="comment-text"><p>This would indeed be fabulous if we had a tool like trigcap in the wireshark suite :-) imagin what fun troubleshooting will get if you would only have to trace on certain conditions!</p></div><div id="comment-6695-info" class="comment-info"><span class="comment-age">(04 Oct '11, 05:20)</span> Marc</div></div></div><div id="comment-tools-6659" class="comment-tools"></div><div class="clear"></div><div id="comment-6659-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

