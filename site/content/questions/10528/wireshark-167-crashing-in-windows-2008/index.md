+++
type = "question"
title = "Wireshark 1.6.7 crashing in Windows 2008"
description = '''Hi: I downloaded wireshark 1.6.7 for windows (32 bits). I am running it in a Windows 2008(32 bits) virtual machine (The hypervisor is Hyper-V) After a period of running wireshark making a capture, it crashes with the following error: Faulting application wireshark.exe, version 1.6.7.41973,  time sta...'''
date = "2012-04-30T09:54:00Z"
lastmod = "2012-04-30T13:45:00Z"
weight = 10528
keywords = [ "windows", "2008", "hyperv", "appcrash" ]
aliases = [ "/questions/10528" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark 1.6.7 crashing in Windows 2008](/questions/10528/wireshark-167-crashing-in-windows-2008)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10528-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10528-score" class="post-score" title="current number of votes">0</div><span id="post-10528-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi:</p><p>I downloaded wireshark 1.6.7 for windows (32 bits). I am running it in a Windows 2008(32 bits) virtual machine (The hypervisor is Hyper-V)</p><p>After a period of running wireshark making a capture, it crashes with the following error:</p><p>Faulting application wireshark.exe, version 1.6.7.41973, time stamp 0x4f7f4286, faulting module libglib-2.0-0.dll, version 2.28.8.0, time stamp 0x4e253544, exception code 0x40000015, fault offset 0x0004c2d8, process id 0xb74, application start time 0x01cd26dd6a840d67.</p><p>The version is Version 1.6.7 (SVN Rev 41973 from /trunk-1.6)</p><p>Any ideas / suggestions</p><p>Regards</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-2008" rel="tag" title="see questions tagged &#39;2008&#39;">2008</span> <span class="post-tag tag-link-hyperv" rel="tag" title="see questions tagged &#39;hyperv&#39;">hyperv</span> <span class="post-tag tag-link-appcrash" rel="tag" title="see questions tagged &#39;appcrash&#39;">appcrash</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Apr '12, 09:54</strong></p><img src="https://secure.gravatar.com/avatar/a3ebb02b9523f3377b6fe50e088bb885?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pappo&#39;s gravatar image" /><p><span>pappo</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pappo has no accepted answers">0%</span></p></div></div><div id="comments-container-10528" class="comments-container"></div><div id="comment-tools-10528" class="comment-tools"></div><div class="clear"></div><div id="comment-10528-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="10529"></span>

<div id="answer-container-10529" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10529-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10529-score" class="post-score" title="current number of votes">0</div><span id="post-10529-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Depending upon the length of "a period of running" and the amount of data collected, one possibility:</p><p><a href="http://wiki.wireshark.org/KnownBugs/OutOfMemory">OutOfMemory</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Apr '12, 10:39</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p><span>Bill Meier ♦♦</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div></div><div id="comments-container-10529" class="comments-container"></div><div id="comment-tools-10529" class="comment-tools"></div><div class="clear"></div><div id="comment-10529-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="10535"></span>

<div id="answer-container-10535" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10535-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10535-score" class="post-score" title="current number of votes">0</div><span id="post-10535-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hi,</p><p>I can create a very similar error message if I run a 32 Bit version of Wireshark on Windows 7 64 Bit and open a file larger 2 GByte (a lot HTTP, which obviously consumes quite some memory).</p><p>As already mentioned, it looks like an OutOfMemory problem. Try to use ring buffers.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Apr '12, 13:45</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-10535" class="comments-container"></div><div id="comment-tools-10535" class="comment-tools"></div><div class="clear"></div><div id="comment-10535-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

