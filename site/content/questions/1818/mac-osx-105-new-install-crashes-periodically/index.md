+++
type = "question"
title = "Mac OSX 10.5 New install crashes periodically"
description = '''All I&#x27;ve been able to detect thus far are a series of messages in the console log: &amp;gt; 1/19/11 11:24:48 AM org.x.startx[541] AllocNewConnection: client index = 3, socket fd = 12  &amp;gt; 1/19/11 11:24:48 AM org.x.startx[541] AUDIT: Wed Jan 19 11:24:48 2011: 602 X: client 3 rejected from local host (ui...'''
date = "2011-01-19T10:35:00Z"
lastmod = "2011-01-19T13:06:00Z"
weight = 1818
keywords = [ "osx", "mac", "x11" ]
aliases = [ "/questions/1818" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Mac OSX 10.5 New install crashes periodically](/questions/1818/mac-osx-105-new-install-crashes-periodically)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1818-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>All I've been able to detect thus far are a series of messages in the console log:</p><pre><code>&gt; 1/19/11 11:24:48 AM org.x.startx[541] AllocNewConnection: client index = 3, socket fd = 12  
&gt; 1/19/11 11:24:48 AM org.x.startx[541] AUDIT: Wed Jan 19 11:24:48 2011: 602 X: client 3 rejected from local host (uid 506) 
&gt; 1/19/11 11:24:48 AM org.x.startx[541] Xlib: connection to &quot;:0.0&quot; refused by server
&gt; 1/19/11 11:24:48 AM org.x.startx[541] Xlib: No protocol specified
&gt; 1/19/11 11:24:48 AM org.x.startx[541] .
&gt; 1/19/11 11:24:49 AM org.x.startx[541] .
&gt; 1/19/11 11:24:50 AM org.x.startx[541] giving up.
&gt; 1/19/11 11:24:50 AM org.x.startx[541] xinit:  Operation timed out (errno 60):  unable to connect to X server
&gt; 1/19/11 11:24:50 AM org.x.startx[541] waiting for X server to shut down
&gt; 1/19/11 11:24:51 AM org.x.startx[541] Quitting Xquartz...
&gt; 1/19/11 11:24:51 AM com.apple.launchd[120] ([0x0-0x25025].org.wireshark.Wireshark[499]) Stray process with PGID equal to this dead job: PID 709 PPID 1 dumpcap-bin 
&gt; 1/19/11 11:24:51 AM org.x.startx[541] xinit:  Operation timed out (errno 60):  Server error.</code></pre><p>Am running XQuartz 2.1.6 (xorg-server 1.4.2-apple33), which works with many other applications I run frequently on this Mac, I believe this came from the latest install I made of Xcode.</p><p>Suggestions, please?</p><p>Jon</p></div><div id="question-tags" class="tags-container tags">osx mac x11</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Jan '11, 10:35</strong></p><img src="https://secure.gravatar.com/avatar/aad9333dc07d07e9fdb717441b299c26?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jon_m&#39;s gravatar image" /><p>jon_m<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jon_m has no accepted answers">0%</span></p></div></div><div id="comments-container-1818" class="comments-container"></div><div id="comment-tools-1818" class="comment-tools"></div><div class="clear"></div><div id="comment-1818-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="1819"></span>

<div id="answer-container-1819" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1819-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I've updated to X 2.6.0, still crashing.</p><p>This time I see a suspicious message on a crash report:</p><pre><code>  Library not loaded: /usr/local/lib/libwiretap.0.dylib</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Jan '11, 13:06</strong></p><img src="https://secure.gravatar.com/avatar/aad9333dc07d07e9fdb717441b299c26?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jon_m&#39;s gravatar image" /><p>jon_m<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jon_m has no accepted answers">0%</span></p></div></div><div id="comments-container-1819" class="comments-container"></div><div id="comment-tools-1819" class="comment-tools"></div><div class="clear"></div><div id="comment-1819-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

