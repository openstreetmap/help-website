+++
type = "question"
title = "Compile slow and LTE MAC Over UDP Issue???"
description = '''I use wireshark ver 2.2.2 under windows 64bit when I only modify one line code, I find all source files are re-compiled again, the time is so long. How to set to only compile updated files? another question: I want to analysis LTE MAC PDU over UDP, how to do it. I modify as follows:  heur_dissector_...'''
date = "2017-05-09T03:19:00Z"
lastmod = "2017-05-09T04:40:00Z"
weight = 61300
keywords = [ "mac-udp" ]
aliases = [ "/questions/61300" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Compile slow and LTE MAC Over UDP Issue???](/questions/61300/compile-slow-and-lte-mac-over-udp-issue)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61300-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61300-score" class="post-score" title="current number of votes">0</div><span id="post-61300-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I use wireshark ver 2.2.2 under windows 64bit when I only modify one line code, I find all source files are re-compiled again, the time is so long. How to set to only compile updated files?</p><p>another question: I want to analysis LTE MAC PDU over UDP, how to do it. I modify as follows: heur_dissector_add("udp", dissect_mac_lte_heur, "MAC-LTE over UDP", "mac_lte_udp", proto_mac_lte, HEURISTIC_DISABLE); change into: heur_dissector_add("udp", dissect_mac_lte_heur, "MAC-LTE over UDP", "mac_lte_udp", proto_mac_lte, HEURISTIC_ENABLE); HEURISTIC_DISABLE -&gt; HEURISTIC_ENABLE</p><p>but sub-dissector of UDP still don't include "MAC-LTE over UDP" in heur_list</p><p>hope to get your help, so thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-mac-udp" rel="tag" title="see questions tagged &#39;mac-udp&#39;">mac-udp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 May '17, 03:19</strong></p><img src="https://secure.gravatar.com/avatar/b9c70dcf8369b3a5562ad7de575a22be?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="commonstar&#39;s gravatar image" /><p><span>commonstar</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="commonstar has no accepted answers">0%</span></p></div></div><div id="comments-container-61300" class="comments-container"></div><div id="comment-tools-61300" class="comment-tools"></div><div class="clear"></div><div id="comment-61300-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61302"></span>

<div id="answer-container-61302" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61302-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61302-score" class="post-score" title="current number of votes">0</div><span id="post-61302-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Please raise a separate item for each question as that's how this site works, see the FAQ for more info.</p><p>Answering your first question, presumably you are building using CMake from the command line and simply executing <code>msbuild /m /p:Configuration=RelWithDebInfo Wireshark.sln</code>, then VS will only rebuild the required parts. There is a lot of output, but if you redirect it to a file (<code>2&gt;&amp;1 &gt; file.txt</code>) and check in file.txt you should only see the compiler (<code>CL.exe</code>) called for the modified files and then the linker (<code>link.exe</code>) as required e.g. to produce libepan, then libwireshark.dll and also every other dll or executable that depends on libepan.</p><p>On my build VM (VirtualBox, 4 cores of an i7 running Windows 10) a build where no files have changed is around 8 seconds (run in a PowerShell prompt using PS Measure-Command for timing):</p><pre><code>E:\Wireshark\build64&gt; Measure-Command { msbuild /m /p:Configuration=RelWithDebInfo Wireshark.sln 2&gt;&amp;1 &gt; C:\temp\build.txt }

Days              : 0
Hours             : 0
Minutes           : 0
Seconds           : 7
Milliseconds      : 425
Ticks             : 74250526
TotalDays         : 8.59381087962963E-05
TotalHours        : 0.00206251461111111
TotalMinutes      : 0.123750876666667
TotalSeconds      : 7.4250526
TotalMilliseconds : 7425.0526</code></pre><p>And if I change a dissector source file and rebuild:</p><pre><code>E:\Wireshark\build64&gt; Measure-Command { msbuild /m /p:Configuration=RelWithDebInfo Wireshark.sln 2&gt;&amp;1 &gt; C:\temp\build.txt }

Days              : 0
Hours             : 0
Minutes           : 0
Seconds           : 43
Milliseconds      : 649
Ticks             : 436493534
TotalDays         : 0.000505200849537037
TotalHours        : 0.0121248203888889
TotalMinutes      : 0.727489223333333
TotalSeconds      : 43.6493534
TotalMilliseconds : 43649.3534</code></pre><p>You can speed up the rebuild by developing your dissector as a plugin, in that case there is no library rebuild only the compile and link of the plugin DLL.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 May '17, 04:40</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-61302" class="comments-container"></div><div id="comment-tools-61302" class="comment-tools"></div><div class="clear"></div><div id="comment-61302-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

