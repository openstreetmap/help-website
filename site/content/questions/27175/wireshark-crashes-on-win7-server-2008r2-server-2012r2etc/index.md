+++
type = "question"
title = "Wireshark Crashes on Win7, Server 2008r2, Server 2012r2...etc"
description = '''Yes, this is another WireShark Crash Question.... So, I&#x27;ve used Wireshark in the following OS&#x27;s:  Win7 x64 Server 2008r2 (x64) Server 2012r2 (x64)  I&#x27;m testing software in an environment consisting of multiple instances of the aforementioned OS&#x27;s.  My filter is ip.addr == 192.168.1.1. (I can&#x27;t give ...'''
date = "2013-11-20T09:43:00Z"
lastmod = "2013-11-20T10:10:00Z"
weight = 27175
keywords = [ "server2012", "server2008", "crash", "win7" ]
aliases = [ "/questions/27175" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark Crashes on Win7, Server 2008r2, Server 2012r2...etc](/questions/27175/wireshark-crashes-on-win7-server-2008r2-server-2012r2etc)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27175-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Yes, this is another WireShark Crash Question....</p><p>So, I've used Wireshark in the following OS's:</p><ul><li>Win7 x64</li><li>Server 2008r2 (x64)</li><li>Server 2012r2 (x64)</li></ul><p>I'm testing software in an environment consisting of multiple instances of the aforementioned OS's.</p><p>My filter is <strong>ip.addr == 192.168.1.1</strong>.</p><p><em>(I can't give the actual IP for security purposes).</em></p><p>I have an SNMP Trap set up on 192.168.1.1 and am using wireshark to make sure errors are sent to the Trap.</p><p>When I have WireShark running, it records the SNMP's just fine. For no reason, it randomly crashes. It doesn't matter which machine I'm using it on.</p><p>I'm using WireShark 1.10.3 (64-bit).</p><p>Any thoughts on this?</p></div><div id="question-tags" class="tags-container tags">server2012 server2008 crash win7</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Nov '13, 09:43</strong></p><img src="https://secure.gravatar.com/avatar/e18d1cfcc0b6db23a9446bf3182672fd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="xenoranger&#39;s gravatar image" /><p>xenoranger<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="xenoranger has no accepted answers">0%</span></p></div></div><div id="comments-container-27175" class="comments-container"></div><div id="comment-tools-27175" class="comment-tools"></div><div class="clear"></div><div id="comment-27175-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="27176"></span>

<div id="answer-container-27176" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27176-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>That's a display filter so Wireshark will be capturing and recording all the other traffic received by the NIC (presumably you're running the capture in promiscuous mode) and is likely to be running out of memory. See the <a href="http://wiki.wireshark.org/KnownBugs/OutOfMemory">OutOfMemory</a> page on the wiki for more info.</p><p>Try setting a capture filter (in the Capture Options dialog) of <code>host 192.168.1.1</code> to restrict the raffic that Wireshark actually receives.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Nov '13, 10:10</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-27176" class="comments-container"><span id="27177"></span><div id="comment-27177" class="comment"><div id="post-27177-score" class="comment-score"></div><div class="comment-text"><p>It might be related to <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=9255">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=9255</a> and <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=8281">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=8281</a></p></div><div id="comment-27177-info" class="comment-info"><span class="comment-age">(20 Nov '13, 11:47)</span> Anders ♦</div></div></div><div id="comment-tools-27176" class="comment-tools"></div><div class="clear"></div><div id="comment-27176-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

