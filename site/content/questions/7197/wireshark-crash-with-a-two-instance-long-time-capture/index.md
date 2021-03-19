+++
type = "question"
title = "Wireshark crash with a two instance long time capture"
description = '''Hi, my wireshark crashed over night. Short Version -&amp;gt; I had two instances of Wireshark running. For a long time capture over the weekend I configured multiple capture files (One file every 100MB). It seems like there was a memory overrun anyway. Any idea how to prevent my Shark from crashing? Lon...'''
date = "2011-11-02T06:26:00Z"
lastmod = "2011-11-02T07:18:00Z"
weight = 7197
keywords = [ "instances", "memory", "multiple", "ringbuffer", "wireshark" ]
aliases = [ "/questions/7197" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark crash with a two instance long time capture](/questions/7197/wireshark-crash-with-a-two-instance-long-time-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7197-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, my wireshark crashed over night.</p><p>Short Version -&gt; I had two instances of Wireshark running. For a long time capture over the weekend I configured multiple capture files (One file every 100MB). It seems like there was a memory overrun anyway. Any idea how to prevent my Shark from crashing?</p><p>Long Version -&gt; I'm testing a network device with different scenarios. Tests might run over several days. To have a capture in case of errors occuring I use a Network Tap and a Monitor PC with two NIC and Wireshark installed. For both Wireshark instances (one for send and one for receive direction) a ring buffer with 200 files x 100MB is configured. The OS is Win Server2008R2 64Bit, the message I get is something like "GLib-Error**: gmem.c:136: failed to allocate 429496295 bytes aborting..." The capture aborted after about 7GB of capturefiles, 4GB of memory are installed on the machine.</p><p>I could try to use a second monitor PC, more RAM or a different OS but I hope you give me some ideas before I spend some hours on experiments :)</p></div><div id="question-tags" class="tags-container tags">instances memory multiple ringbuffer wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Nov '11, 06:26</strong></p><img src="https://secure.gravatar.com/avatar/40821acbe45b6e5c4263c37eaf46bb2f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ratlos&#39;s gravatar image" /><p>ratlos<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ratlos has no accepted answers">0%</span></p></div></div><div id="comments-container-7197" class="comments-container"></div><div id="comment-tools-7197" class="comment-tools"></div><div class="clear"></div><div id="comment-7197-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="7199"></span>

<div id="answer-container-7199" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7199-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hi,</p><p>From the <a href="http://wiki.wireshark.org/KnownBugs/OutOfMemory" title="OutOfMemory">Wireshark Wiki</a>:</p><blockquote><p>If Wireshark is running out of memory, that probably means that you're letting it run for a very long time or you're analyzing very large capture files. You may find that another tool does what you want better than Wireshark. Use dumpcap for long term capturing, it's intended for this purpose, or see Tools for other tools which may be more suitable for the task</p></blockquote><p><a href="http://www.wireshark.org/docs/man-pages/dumpcap.html" title="dumpcap">dumpcap</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Nov '11, 07:18</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 02 Nov '11, 09:30</p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p>multipleinte...<br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span></p></div></div><div id="comments-container-7199" class="comments-container"><span id="7200"></span><div id="comment-7200" class="comment"><div id="post-7200-score" class="comment-score"></div><div class="comment-text"><p>Hi Anders,</p><p>thank you for your answer! The disadvantage in my case is, that I want some window where I can see the live traffic (at least during working hours). So a possibility would be to use dumpshark and wireshark simultanously. Dumpshark running with a ringbuffer while wireshark is opened and closed by a script at regular intervals (which should clean up the memory).</p><p>But perhaps there is another tool just for the memory cleaning? Or some other way to handle this bug?</p></div><div id="comment-7200-info" class="comment-info"><span class="comment-age">(02 Nov '11, 09:41)</span> ratlos</div></div></div><div id="comment-tools-7199" class="comment-tools"></div><div class="clear"></div><div id="comment-7199-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

