+++
type = "question"
title = "Wireshark crash"
description = '''Hi, I was recently introduced to wireshark to help me troubleshoot a problomatic network where the switches kept repeatidly crashing.  To get me started I picked up a book called Practical Packet Analysis: Using Wireshark to Solve Real-World Network Problems by Chris Sanders which has been of great ...'''
date = "2011-07-18T00:39:00Z"
lastmod = "2011-07-18T00:57:00Z"
weight = 5087
keywords = [ "crash", "wireshark" ]
aliases = [ "/questions/5087" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark crash](/questions/5087/wireshark-crash)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5087-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I was recently introduced to wireshark to help me troubleshoot a problomatic network where the switches kept repeatidly crashing.</p><p>To get me started I picked up a book called Practical Packet Analysis: Using Wireshark to Solve Real-World Network Problems by Chris Sanders which has been of great help.</p><p>I am currently leaving my laptop onsite at the customers house colelcting data over 3/4 day periods and I am finding that when I return to collect the laptop Wireshark has recently crashed.</p><p>I have set my Capture options to use multiple files and start a new file every 2 hours. this was to try and keep memory usage down and in event of a crash leave me with at least some data.</p><p>After looking at event viewer in Windows Vista I can see this error:</p><p>Faulting application wireshark.exe, version 1.6.0.37592, time stamp 0x4dee5505, faulting module libgdk-win32-2.0-0.dll, version 2.22.1.0, time stamp 0x4d1898fe, exception code 0xc0000005, fault offset 0x00007475, process id 0xd4c, application start time 0x01cc42ff531e6942.</p><p>Not sure if this helps? I have noticed both times that Apple Software Updater is running and is awating instruction.</p><p>to note. The network has not crashed while I have been monitoring.</p></div><div id="question-tags" class="tags-container tags">crash wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Jul '11, 00:39</strong></p><img src="https://secure.gravatar.com/avatar/8a60278b9a8149b6f35e8fbf89b7f475?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="timelapse&#39;s gravatar image" /><p>timelapse<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="timelapse has no accepted answers">0%</span></p></div></div><div id="comments-container-5087" class="comments-container"></div><div id="comment-tools-5087" class="comment-tools"></div><div class="clear"></div><div id="comment-5087-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="5088"></span>

<div id="answer-container-5088" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5088-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The best way to do long-term captures is to use dumpcap instead of Wireshark. Dumpcap is used by Wireshark under the hood. It just collects network packets and writes them to disc. Wireshark also does some analysis and can have an increasing memory footprint resulting in a crash.</p><p>Also it's better to use capture size as a means of switching to the next file, that way you can set up a ringbuffer that will never grow beyond a certain size, so it won't fill up the discs. I have used dumpcap in that way to capture for months at a time.</p><p>You can use dumpcap like this:</p><pre><code>dumpcap -w &lt;file.pcap&gt; -i &lt;interface&gt; -b filesize:100000 -b files:100 -f &quot;&lt;filter&gt;&quot;</code></pre><p>Meaning, create a ring buffer of 100 files of 100MB each (when the 101st file is created, the 1st one is automatically deleted). Disk usage will therefor never grow beyond 10GB.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Jul '11, 00:57</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-5088" class="comments-container"><span id="5094"></span><div id="comment-5094" class="comment"><div id="post-5094-score" class="comment-score"></div><div class="comment-text"><p>Hi, thanks for the quick reply. Taken onboard the comments re capture size and ring buffer. Thanks!Will give that a shot.</p><p>Where do i enter dumpcap command?</p></div><div id="comment-5094-info" class="comment-info"><span class="comment-age">(18 Jul '11, 02:20)</span> timelapse</div></div><span id="5096"></span><div id="comment-5096" class="comment"><div id="post-5096-score" class="comment-score"></div><div class="comment-text"><p>You can enter the command in a CMD window. You might want to add the path to wireshark in your path environment variable (richtclick on computer-&gt;properties-&gt;advanced system settings-&gt;environment_variables, then search for "Path" and add the path to your Wireshark directory), so you can start dumpcap from any folder.</p></div><div id="comment-5096-info" class="comment-info"><span class="comment-age">(18 Jul '11, 02:27)</span> SYN-bit ♦♦</div></div><span id="5097"></span><div id="comment-5097" class="comment"><div id="post-5097-score" class="comment-score"></div><div class="comment-text"><p>:) much appreciated.</p></div><div id="comment-5097-info" class="comment-info"><span class="comment-age">(18 Jul '11, 02:53)</span> timelapse</div></div></div><div id="comment-tools-5088" class="comment-tools"></div><div class="clear"></div><div id="comment-5088-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

