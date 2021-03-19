+++
type = "question"
title = "Dumpcap Syntax"
description = '''On a Windows XP system dumpcap keeps creating new files even though &quot;files:3&quot; is used. What is wrong with my syntax? C:&#92;Temp&amp;gt;dumpcap.exe -i1 -b files:3 -b filesize:1 -w test.pcap File: test_00001_20101207114220.pcap Packets: 10 File: test_00002_20101207114223.pcap Packets: 20 File: test_00003_201...'''
date = "2010-12-07T08:48:00Z"
lastmod = "2010-12-07T09:00:00Z"
weight = 1271
keywords = [ "files", "dumpcap" ]
aliases = [ "/questions/1271" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Dumpcap Syntax](/questions/1271/dumpcap-syntax)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1271-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>On a Windows XP system dumpcap keeps creating new files even though "files:3" is used. What is wrong with my syntax?</p><pre><code>C:\Temp&gt;dumpcap.exe -i1 -b files:3 -b filesize:1 -w test.pcap
File: test_00001_20101207114220.pcap
Packets: 10 File: test_00002_20101207114223.pcap
Packets: 20 File: test_00003_20101207114227.pcap
Packets: 29 File: test_00004_20101207114228.pcap
Used CTL-C to quit</code></pre></div><div id="question-tags" class="tags-container tags">files dumpcap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Dec '10, 08:48</strong></p><img src="https://secure.gravatar.com/avatar/2b54913de7bfd696b930bdc190d8ae90?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gary&#39;s gravatar image" /><p>Gary<br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gary has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 07 Dec '10, 09:02</p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span></p></div></div><div id="comments-container-1271" class="comments-container"></div><div id="comment-tools-1271" class="comment-tools"></div><div class="clear"></div><div id="comment-1271-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="1272"></span>

<div id="answer-container-1272" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1272-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>When you use <code>"-b files:3"</code> dumpcap will create a ringbuffer of 3 files. This means it will keep creating new files forever, but it will only keep the latest three, all others will be deleted on the fly.</p><p>If you want to make dumpcap <em>stop</em> after 3 files, you will have to use the <code>"-a"</code> options. So your command would be:</p><pre><code>C:Temp&gt;dumpcap.exe -i1 -a files:3 -a filesize:1 -w test.pcap</code></pre><p>(please notice that you can't mix -a and -b options, so you have to change both).</p><p>BTW this behavior is not Windows specific, dumpcap does the same thing on other platforms.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Dec '10, 09:00</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-1272" class="comments-container"></div><div id="comment-tools-1272" class="comment-tools"></div><div class="clear"></div><div id="comment-1272-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

