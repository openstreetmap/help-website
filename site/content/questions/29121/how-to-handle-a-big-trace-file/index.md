+++
type = "question"
title = "How to handle a big trace file?"
description = '''Hi experts, I know that open a big trace file by wireshark will be slower than opening a relatively small trace file. How would you deal with it generally? Is there any better way to do this? thanks a lot!'''
date = "2014-01-23T06:51:00Z"
lastmod = "2014-01-27T22:00:00Z"
weight = 29121
keywords = [ "big_trace_file" ]
aliases = [ "/questions/29121" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How to handle a big trace file?](/questions/29121/how-to-handle-a-big-trace-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29121-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi experts,</p><p>I know that open a big trace file by wireshark will be slower than opening a relatively small trace file. How would you deal with it generally? Is there any better way to do this?</p><p>thanks a lot!</p></div><div id="question-tags" class="tags-container tags">big_trace_file</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Jan '14, 06:51</strong></p><img src="https://secure.gravatar.com/avatar/2d1a8885858c8435654658b25f489bd9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SteveZhou&#39;s gravatar image" /><p>SteveZhou<br />
<span class="score" title="191 reputation points">191</span><span title="27 badges"><span class="badge1">●</span><span class="badgecount">27</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="34 badges"><span class="bronze">●</span><span class="badgecount">34</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SteveZhou has no accepted answers">0%</span></p></div></div><div id="comments-container-29121" class="comments-container"></div><div id="comment-tools-29121" class="comment-tools"></div><div class="clear"></div><div id="comment-29121-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="29122"></span>

<div id="answer-container-29122" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29122-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>There are two ways</p><ul><li>get a real fast system (CPU) with lots of RAM (several Gig) and with a 64 bit OS</li><li>split the capture file with <strong>editcap</strong></li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Jan '14, 07:51</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-29122" class="comments-container"><span id="29148"></span><div id="comment-29148" class="comment"><div id="post-29148-score" class="comment-score"></div><div class="comment-text"><p>thank you, Kurt. [to myself notes: editcap is an application located in the wireshark installation direcotry, just as tshark.]</p></div><div id="comment-29148-info" class="comment-info"><span class="comment-age">(25 Jan '14, 07:05)</span> SteveZhou</div></div><span id="29149"></span><div id="comment-29149" class="comment"><div id="post-29149-score" class="comment-score"></div><div class="comment-text"><p>By the way, is there any options for tshark which can read just part of the trace file so that we don't need to load the entire trace, it will also reduce time for loading data.</p></div><div id="comment-29149-info" class="comment-info"><span class="comment-age">(25 Jan '14, 07:07)</span> SteveZhou</div></div><span id="29162"></span><div id="comment-29162" class="comment"><div id="post-29162-score" class="comment-score"></div><div class="comment-text"><p>Hm, do you mean something like this?</p><p>-Y "frame.time_relative &gt; 30 and frame.time_relative &lt; 40"</p><p>-Y " frame.numbger gt 45000 and frame.number le 55000"</p></div><div id="comment-29162-info" class="comment-info"><span class="comment-age">(25 Jan '14, 22:19)</span> mrEEde</div></div><span id="29209"></span><div id="comment-29209" class="comment"><div id="post-29209-score" class="comment-score"></div><div class="comment-text"><p>Hi mrEEde,</p><p>sorry, I have no experience with tshark before so I'm trying to understand what you typed. I found the following two options for tshark:</p><p>-R &lt;read filter=""&gt; packet Read filter in Wireshark display filter syntax -Y &lt;display filter=""&gt; packet displaY filter in Wireshark display filter syntax</p><p>My goal is to read just part of a big trace file just like you mentioned above. But would tshark actually read the entire big trace file into memory and then apply display filter by running the -R or -Y option? If that is the case, tshark still needs to read the entire big file and consume lot of time.</p></div><div id="comment-29209-info" class="comment-info"><span class="comment-age">(27 Jan '14, 17:55)</span> SteveZhou</div></div></div><div id="comment-tools-29122" class="comment-tools"></div><div class="clear"></div><div id="comment-29122-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="29213"></span>

<div id="answer-container-29213" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29213-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>"sorry, I have no experience with tshark before so I'm trying to understand what you typed. I found the following two options for tshark:</p><p>-R &lt;read filter=""&gt; packet Read filter in Wireshark display filter syntax -Y &lt;display filter=""&gt; packet displaY filter in Wireshark display filter syntax"</p></blockquote><p>tshark -Y reads a trace record and applies a filter to it. If the filter condition is true, the packet will be processed (displayed or with -w written to a new file.)<br />
The trace file will not be read completely but on a packet by packet basis.</p><pre><code>tshark -r t1_400k.pcap -R &quot;frame.number gt 10000 and frame.number le 11000&quot; -w just1k.pcapng
tshark: -R without -2 is deprecated. For single-pass filtering use -Y
tshark -r t1_400k.pcap -Y &quot;frame.number gt 10000 and frame.number le 11000&quot; -w just1k.pcapng</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Jan '14, 22:00</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p>mrEEde<br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></p></div></div><div id="comments-container-29213" class="comments-container"></div><div id="comment-tools-29213" class="comment-tools"></div><div class="clear"></div><div id="comment-29213-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

