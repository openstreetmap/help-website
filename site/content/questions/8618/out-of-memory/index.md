+++
type = "question"
title = "Out Of Memory"
description = '''I encountered the following message &quot;Out Of Memory!&quot; when opening a CAP file. The file size is 1,180,929 KB. The workstation I am using has an Intel Core i5 Processor, 4 GB Memory with Windows 7 32 Bit. I would like to find out if upgrading to a workstation with an Intel Core i7 Processor, 8 GB Memo...'''
date = "2012-01-26T00:57:00Z"
lastmod = "2012-01-26T23:08:00Z"
weight = 8618
keywords = [ "out-of-memory" ]
aliases = [ "/questions/8618" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Out Of Memory](/questions/8618/out-of-memory)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8618-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I encountered the following message "Out Of Memory!" when opening a CAP file. The file size is 1,180,929 KB. The workstation I am using has an Intel Core i5 Processor, 4 GB Memory with Windows 7 32 Bit. I would like to find out if upgrading to a workstation with an Intel Core i7 Processor, 8 GB Memory with Windows 7 64 Bit will be able to overcome this issue. Thanks!</p></div><div id="question-tags" class="tags-container tags">out-of-memory</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Jan '12, 00:57</strong></p><img src="https://secure.gravatar.com/avatar/992a134fbd2c00d988e4f405e177a24d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Danny%20Chan&#39;s gravatar image" /><p>Danny Chan<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Danny Chan has no accepted answers">0%</span></p></div></div><div id="comments-container-8618" class="comments-container"></div><div id="comment-tools-8618" class="comment-tools"></div><div class="clear"></div><div id="comment-8618-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="8621"></span>

<div id="answer-container-8621" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8621-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Have you checked to <a href="http://wiki.wireshark.org/KnownBugs/OutOfMemory">OutOfMemory</a> wiki page already? You may want to look into using the latest Wireshark version and/or splitting your capture file using editcap.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Jan '12, 01:22</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-8621" class="comments-container"><span id="8622"></span><div id="comment-8622" class="comment"><div id="post-8622-score" class="comment-score"></div><div class="comment-text"><p>I totally agree with Jaap With files that big I would try Pilot.</p></div><div id="comment-8622-info" class="comment-info"><span class="comment-age">(26 Jan '12, 04:46)</span> thetechfirm</div></div></div><div id="comment-tools-8621" class="comment-tools"></div><div class="clear"></div><div id="comment-8621-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="8645"></span>

<div id="answer-container-8645" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8645-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>In theory, a 64-bit version of Windows <em>and</em> a 64-bit version of Wireshark (which requires an OS that supports 64-bit programs, meaning, for Windows, a 64-bit version) should help, as long as you have a big enough paging file. See <a href="http://windows.microsoft.com/en-US/windows-vista/Change-the-size-of-virtual-memory">this article from Microsoft</a> on setting the paging file's maximum size (which would presumably default to 24 GB on the upgraded machine).</p><p>However, <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=5979">bug 5979 in the Wireshark bug database</a> says that 64-bit Wireshark doesn't appear to actually be 64-bit in a useful sense; we haven't yet figured out what the heck is going on there. 2GB is less than the default <em>minimum</em> page file size on any machine where you'd be likely to run 64-bit Windows, as that's 300MB more than the main memory size, so I doubt it's an issue with the paging file. (I think that, given what the Microsoft article says, you'd get warning dialogs from the system if you run out of paging file space.)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Jan '12, 23:08</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-8645" class="comments-container"><span id="21234"></span><div id="comment-21234" class="comment"><div id="post-21234-score" class="comment-score"></div><div class="comment-text"><p>I am running Win7 x64 SP1 with 8GB of memory, and I run into Wireshark out of memory conditions with even captures as small at 100MB (even using tshark!). I suppose that means I should donate to Wireshark for development efforts? ;)</p></div><div id="comment-21234-info" class="comment-info"><span class="comment-age">(17 May '13, 12:57)</span> mlan</div></div><span id="21239"></span><div id="comment-21239" class="comment"><div id="post-21239-score" class="comment-score"></div><div class="comment-text"><p>No. You should use dumpcap instead of tShark/Wireshark. File size doesn't matter that much, because the out of memory is not caused by packet bytes but by the analysis structures Wireshark/tShark create in memory while capturing. dumpcap doesn't do this, it just writes packets to file.</p></div><div id="comment-21239-info" class="comment-info"><span class="comment-age">(17 May '13, 13:11)</span> Jasper ♦♦</div></div><span id="21242"></span><div id="comment-21242" class="comment"><div id="post-21242-score" class="comment-score"></div><div class="comment-text"><p>The "use dumpcap" rule isn't a general solution to all out-of-memory problems. It's a specific solution to the "I'm running {Wireshark, TShark} for a very long period of time, capturing traffic, and it runs out of memory" problem.</p><p>The full solution is to run dumpcap in a mode where, instead of saving all packet data to a single file (which just defers the problem - when you try to read that big file with Wireshark or TShark, it'd still run out of memory), it saves to a sequence of files, keeping each file limited in size.</p><p>If you're running out of memory with a 100MB file, that might just be a bug. At least on a 64-bit Mac, I've been able to read a gzipped file that's about 265MB (so it's even bigger uncompressed) - it took a while on the original machine I tried it on, which had only 4MB main memory, and it created a fair bit of extra swap space in the process, but it did work.</p></div><div id="comment-21242-info" class="comment-info"><span class="comment-age">(17 May '13, 13:30)</span> Guy Harris ♦♦</div></div><span id="21245"></span><div id="comment-21245" class="comment"><div id="post-21245-score" class="comment-score"></div><div class="comment-text"><p>I use dumpcap for my captures, but was trying to use tshark to filter a 100MB pcap created with dumpcap. That is when I experienced the OOM condition. Is it possible to use dumpcap to filter an existing pcap file?</p></div><div id="comment-21245-info" class="comment-info"><span class="comment-age">(17 May '13, 16:29)</span> mlan</div></div><span id="21247"></span><div id="comment-21247" class="comment"><div id="post-21247-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Is it possible to use dumpcap to filter an existing pcap file?</p></blockquote><p>No, but <em>if</em> you can use a capture filter rather than a full-blown display filter, you can use tcpdump:</p><pre><code>tcpdump -r {input file} -w {output file} {filter}</code></pre></div><div id="comment-21247-info" class="comment-info"><span class="comment-age">(17 May '13, 16:50)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-8645" class="comment-tools"></div><div class="clear"></div><div id="comment-8645-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

