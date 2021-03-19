+++
type = "question"
title = "Wireshark crash after 2 days"
description = '''Hey, I&#x27;ve got an effect with a Wireshark crash. After two days Wireshark crashes with the error: &quot;This application has requested the Runtim to terminate it in an unusual way. Please contacs the application&#x27;s support team&quot;.  The problem signature looks like this: Problem signature:  Problem Event Nam...'''
date = "2012-02-20T01:05:00Z"
lastmod = "2012-02-20T03:51:00Z"
weight = 9137
keywords = [ "crash" ]
aliases = [ "/questions/9137" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark crash after 2 days](/questions/9137/wireshark-crash-after-2-days)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9137-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey,</p><p>I've got an effect with a Wireshark crash. After two days Wireshark crashes with the error: "This application has requested the Runtim to terminate it in an unusual way. Please contacs the application's support team". The problem signature looks like this: Problem signature: Problem Event Name: APPCRASH Application Name: wireshark.exe Application Version: 1.6.5.40429 Application Timestamp: 4f0c8ce1 Fault Module Name: libglib-2.0-0.dll Fault Module Version: 2.26.1.0 Fault Module Timestamp: 4d1b271d Exception Code: 40000015 Exception Offset: 000000000005180e OS Version: 6.1.7600.2.0.0.256.4 Locale ID: 3079 Additional Information 1: 15f2 Additional Information 2: 15f24de02058d998dac1fee4b72e43a7 Additional Information 3: 0687 Additional Information 4: 068767e66177b09845c5e81d040d310b</p><p>Read our privacy statement online: http://go.microsoft.com/fwlink/?linkid=104288&amp;clcid=0x0409</p><p>If the online privacy statement is not available, please read our privacy statement offline: C:Windowssystem32en-USerofflps.txt</p><p>Can somebody say if there is a bug in Wireshark? Or is there something which has to be reconfigured?</p><p>Thank you!</p></div><div id="question-tags" class="tags-container tags">crash</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Feb '12, 01:05</strong></p><img src="https://secure.gravatar.com/avatar/128b142c3a9292444f555b1aad741960?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dranigl&#39;s gravatar image" /><p>dranigl<br />
<span class="score" title="14 reputation points">14</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dranigl has no accepted answers">0%</span></p></div></div><div id="comments-container-9137" class="comments-container"></div><div id="comment-tools-9137" class="comment-tools"></div><div class="clear"></div><div id="comment-9137-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="9138"></span>

<div id="answer-container-9138" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9138-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Assuming you were capturing, for long term captures it's recommended to use dumpcap from a console window. The cause is that Wireshark needs to maintain state information, which only build up over time, eventually exhausting all memory. Running dumpcap with the multiple capture files options is to way to approach these long term captures, since dumpcap is stateless with respect to the packet contents.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Feb '12, 02:51</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-9138" class="comments-container"><span id="9139"></span><div id="comment-9139" class="comment"><div id="post-9139-score" class="comment-score"></div><div class="comment-text"><p>See also: http://wiki.wireshark.org/KnownBugs/OutOfMemory</p></div><div id="comment-9139-info" class="comment-info"><span class="comment-age">(20 Feb '12, 03:01)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-9138" class="comment-tools"></div><div class="clear"></div><div id="comment-9138-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="9140"></span>

<div id="answer-container-9140" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9140-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Was Wireshark capturing for the two days it was running? If so, it's possible that it simply ran out of memory. see the Wiki <a href="http://wiki.wireshark.org/KnownBugs/OutOfMemory">Out of Memory</a> page for more info.</p><p>The exception code is a STATUS_FATAL_APP_EXIT from the c run-time library when abort is called. The faulting module is shown as libglib, and there are a number of places where abort is called in there. If you still have the capture file, and it isn't too big and you can share it, making it available on somewhere such as <a href="http://www.cloudshark.org/">CloudShark</a> might allow folks to dig into the crash a little.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Feb '12, 03:51</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-9140" class="comments-container"></div><div id="comment-tools-9140" class="comment-tools"></div><div class="clear"></div><div id="comment-9140-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

