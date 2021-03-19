+++
type = "question"
title = "How to debug tshark with exception offset"
description = '''When I debug my version of tshark, warnings showed as below.I want to find the line of code where warnings come out, and wonder know how to do? ** (tshark.exe:22940): WARNING **: Dissector bug, protocol HTTP, in packet 64084  : STATUS_ACCESS_VIOLATION: dissector accessed an invalid memory address  1...'''
date = "2013-12-01T23:38:00Z"
lastmod = "2013-12-02T02:48:00Z"
weight = 27645
keywords = [ "debug", "tshark" ]
aliases = [ "/questions/27645" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to debug tshark with exception offset](/questions/27645/how-to-debug-tshark-with-exception-offset)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27645-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27645-score" class="post-score" title="current number of votes">0</div><span id="post-27645-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When I debug my version of tshark, warnings showed as below.I want to find the line of code where warnings come out, and wonder know how to do?</p><pre><code>** (tshark.exe:22940): WARNING **: Dissector bug, protocol HTTP, in packet 64084
   : STATUS_ACCESS_VIOLATION: dissector accessed an invalid memory address
   140790
** (tshark.exe:22940): WARNING **: Dissector bug, protocol HTTP, in packet 14106
   3: STATUS_ACCESS_VIOLATION: dissector accessed an invalid memory address
   149454
** (tshark.exe:22940): WARNING **: Dissector bug, protocol HTTP, in packet 14957
   7: STATUS_ACCESS_VIOLATION: dissector accessed an invalid memory address
   159059</code></pre><p>I just kown where to print the warning message, and I want to know where the bug is, how to do?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-debug" rel="tag" title="see questions tagged &#39;debug&#39;">debug</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Dec '13, 23:38</strong></p><img src="https://secure.gravatar.com/avatar/13679628c84abac93be65773340d2589?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="metamatrix&#39;s gravatar image" /><p><span>metamatrix</span><br />
<span class="score" title="56 reputation points">56</span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="metamatrix has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>02 Dec '13, 09:52</strong> </span></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p><span>Bill Meier ♦♦</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span></p></div></div><div id="comments-container-27645" class="comments-container"></div><div id="comment-tools-27645" class="comment-tools"></div><div class="clear"></div><div id="comment-27645-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="27652"></span>

<div id="answer-container-27652" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27652-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27652-score" class="post-score" title="current number of votes">0</div><span id="post-27652-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can use one of the usual suspects for debugging an exe on Windows, <a href="http://msdn.microsoft.com/en-us/library/0bxe8ytt.aspx">Visual Studio</a> or <a href="http://blogs.msdn.com/b/emreknlk/archive/2011/03/27/start-debugging-with-windbg.aspx">WinDbg</a>. Using the debugger of choice, start debugging tshark.exe in the wireshark-gtk directory of your build environment, set the arguments to the debugee (tshark) as required, you may need to point the debugger to the source file location, set breakpoints as required and you should be up and running.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Dec '13, 02:48</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-27652" class="comments-container"></div><div id="comment-tools-27652" class="comment-tools"></div><div class="clear"></div><div id="comment-27652-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

