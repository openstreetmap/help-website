+++
type = "question"
title = "Can I configure Wireshark to work with xampp"
description = '''I recently installed xampp (Apache Friend) on my laptop and I wanted to capture GET requests made by my browser. I installed Wireshark, but cannot see hoe to configure it to do what I want. It lists 4 interfaces, and I tried each one. The &#x27;interfaces&#x27; shows 4 choices, and I tried each one.'''
date = "2013-03-29T07:52:00Z"
lastmod = "2013-03-29T08:34:00Z"
weight = 19929
keywords = [ "apache", "xampp" ]
aliases = [ "/questions/19929" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Can I configure Wireshark to work with xampp](/questions/19929/can-i-configure-wireshark-to-work-with-xampp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19929-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I recently installed xampp (Apache Friend) on my laptop and I wanted to capture GET requests made by my browser. I installed Wireshark, but cannot see hoe to configure it to do what I want. It lists 4 interfaces, and I tried each one.</p><p>The 'interfaces' shows 4 choices, and I tried each one.</p></div><div id="question-tags" class="tags-container tags">apache xampp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Mar '13, 07:52</strong></p><img src="https://secure.gravatar.com/avatar/aec991cd671b33d85d27aa5c6b3a8452?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AndyS01&#39;s gravatar image" /><p>AndyS01<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AndyS01 has no accepted answers">0%</span></p></div></div><div id="comments-container-19929" class="comments-container"></div><div id="comment-tools-19929" class="comment-tools"></div><div class="clear"></div><div id="comment-19929-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="19930"></span>

<div id="answer-container-19930" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19930-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You don't say what your OS is, but if it's Windows then Wireshark can't capture requests made to the local machine, that is if you run the browser on the same machine as the web server. This is because the MS network stack recognises that the packet is local so "short-circuits" the packet and the WinPCap driver that Wireshark uses to capture doesn't see the packet.</p><p>If your OS is not windows, then capturing on the loopback adaptor should do the trick.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Mar '13, 08:34</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 29 Mar '13, 12:35</p></div></div><div id="comments-container-19930" class="comments-container"><span id="19944"></span><div id="comment-19944" class="comment"><div id="post-19944-score" class="comment-score"></div><div class="comment-text"><p>I'm running Windows 7 (32 bit)</p><p>When my browser (Opera) is running on the local machine, it still does GET requests, though.</p><p>Because I can see the Apache php/perl stuff, perhaps I could modify the handler for multipart packet transfers to fire off a log message with details about the packet. I looked around and I saw that there were dozens of php and perl code that reference 'multipart'. Perhaps I could modify one of those?</p></div><div id="comment-19944-info" class="comment-info"><span class="comment-age">(29 Mar '13, 13:55)</span> AndyS01</div></div><span id="19945"></span><div id="comment-19945" class="comment"><div id="post-19945-score" class="comment-score"></div><div class="comment-text"><p>The browser/web server combination on the same machine will work without issues, but Wireshark won't be able to capture the traffic.</p><p>Network Monitor from MS might be able to capture the traffic and Wireshark can open the NM capture files.</p></div><div id="comment-19945-info" class="comment-info"><span class="comment-age">(29 Mar '13, 14:43)</span> grahamb ♦</div></div><span id="19955"></span><div id="comment-19955" class="comment"><div id="post-19955-score" class="comment-score"></div><div class="comment-text"><p>@AndyS01</p><p>I converted your first "answer" to a comment as that's how this site works, it's not a forum, please see the FAQ for more info.</p><p>As your second "answer" was a duplicate of the converted comment I've deleted it.</p><p>Can you clarify your subsequent question and how it refers to Wireshark as Wireshark only handles network traffic, not log files?</p></div><div id="comment-19955-info" class="comment-info"><span class="comment-age">(30 Mar '13, 05:49)</span> grahamb ♦</div></div><span id="19979"></span><div id="comment-19979" class="comment"><div id="post-19979-score" class="comment-score"></div><div class="comment-text"><p>I'm sorry, I got off track a bit. I still need to capture network traffic generated by the Apache server that's running under xampp. My xampp <strong>httpg.conf</strong> file is configured to a servername of &lt;myipaddress&gt; (instead of localhost), and my browser address is something like this: "http://&lt;myipaddress&gt;/test.html". The test.html code gets a filename and uploads it using 'enctype="multipart/form-data'. I expect to see several HTTP GET requests, but Wireshark does not capture them. In Wireshark, I selected all 4 interfaces.</p></div><div id="comment-19979-info" class="comment-info"><span class="comment-age">(31 Mar '13, 16:51)</span> AndyS01</div></div><span id="19983"></span><div id="comment-19983" class="comment"><div id="post-19983-score" class="comment-score"></div><div class="comment-text"><p>As I mentioned n my reply, the issue is not with the xampp stack or configuration, but with the Windows network stack and WinPCap.</p><p>On Windows, packets addressed to the local host (whether that is localhost or an IP that the host has) aren't captured by WinPCap.</p><p>See the Wiki page on <a href="http://wiki.wireshark.org/CaptureSetup/Loopback">Loopback Capturing</a> for more info and a number of ways that may allow you to capture the traffic you want.</p><p>The two easiest ways I know of to capture the traffic you want are:</p><ol><li>Run the client side on a different machine to the server.</li><li>Use Network Monitor from MS to make the capture, then open the captures in Wireshark.</li></ol></div><div id="comment-19983-info" class="comment-info"><span class="comment-age">(01 Apr '13, 00:40)</span> grahamb ♦</div></div></div><div id="comment-tools-19930" class="comment-tools"></div><div class="clear"></div><div id="comment-19930-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

