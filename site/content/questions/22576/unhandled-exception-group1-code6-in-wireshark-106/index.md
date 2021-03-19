+++
type = "question"
title = "Unhandled exception (group=1, code=6) in Wireshark 1.0.6"
description = '''Ok so I am updating to the latest Wireshark-win64-1.10.0 But bear in mind, if you didn&#x27;t fix it, it ain&#x27;t fixed. TShark 1.0.6 (SVN Rev 27387) The command that generated this was: C:&#92;Progra~2&#92;Wireshark&#92;tshark host 199.119.127.205 -S -s 4096 -R &quot;http.request.method == &#92;&quot;POST&#92;&quot;&quot; -w C:&#92;users&#92;markt&#92;Deskt...'''
date = "2013-07-02T15:03:00Z"
lastmod = "2013-07-02T19:27:00Z"
weight = 22576
keywords = [ "libwireshark", "stack", "dump", "tshark" ]
aliases = [ "/questions/22576" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Unhandled exception (group=1, code=6) in Wireshark 1.0.6](/questions/22576/unhandled-exception-group1-code6-in-wireshark-106)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22576-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22576-score" class="post-score" title="current number of votes">-1</div><span id="post-22576-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Ok so I am updating to the latest Wireshark-win64-1.10.0 But bear in mind, if you didn't fix it, it ain't fixed.</p><p>TShark 1.0.6 (SVN Rev 27387)</p><p>The command that generated this was:</p><pre><code>C:\Progra~2\Wireshark\tshark host 199.119.127.205 -S -s 4096 -R &quot;http.request.method == \&quot;POST\&quot;&quot; -w C:\users\markt\Desktop\captures\20130702_%RANDOMSTUFF%.pcap</code></pre><p>The file size generated was 2.20 GB (2,366,529,322 bytes)</p><pre><code>41384.525053 192.168.1.101 -&gt; 199.119.127.205 HTTP POST /ajax/ping HTTP/1.1  (application/x-www-form-urlencoded)
Unhandled exception (group=1, code=6)

This application has requested the Runtime to terminate it in an unusual way.
Please contact the application&#39;s support team for more information.

0:000&gt; k
ChildEBP RetAddr

0017e754 779585f0 ntdll!ZwTerminateProcess+0x12
0017e764 76fb93a6 ntdll!RtlExitUserProcess+0x7a
0017e778 769e3c3a kernel32!ExitProcess+0x12
0017e784 769e3b7b MSVCRT!__crtExitProcess+0x17
0017e7bc 76a39617 MSVCRT!_cinit+0xea
0017e7d0 76a36916 MSVCRT!_exit+0x11
0017eb08 00a6ec96 MSVCRT!abort+0x116
0017eb10 00a6ef08 libwireshark!except_deinit+0x99 [except.c @ 226]
0017eb2c 00a6edc8 libwireshark!except_rethrow+0x1c5 [except.c @ 210]
0017eb3c 00a7720b libwireshark!except_rethrow+0x85 [except.c @ 269]
**0017ebb4 00a6e96d libwireshark!dissect_packet+0x4dd [packet.c @ 349]**
0017ebd0 0041b636 libwireshark!epan_dissect_run+0x21 [epan.c @ 161]
0017ec60 0041af23 tshark!capture_input_closed+0x63a [tshark.c @ 2453]
0017ec98 00417d76 tshark!capture_input_new_packets+0xc8 [tshark.c @ 2027]
0017fccc 0041abef tshark!sync_pipe_gets_nonblock+0x27b [capture_sync.c @ 1216]
0017fce0 00419bc7 tshark!pipe_input_set_handler+0x2a0 [tshark.c @ 1861]
0017ff14 0041daa7 tshark!main+0x159c [tshark.c @ 1614]
0017ff88 7701f271 tshark!mainCRTStartup+0xe3
0017ff94 7799d819 kernel32!BaseThreadInitThunk+0xe
0017ffd4 7799da2b ntdll!__RtlUserThreadStart+0x23
0017ffec 00000000 ntdll!_RtlUserThreadStart+0x1b</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-libwireshark" rel="tag" title="see questions tagged &#39;libwireshark&#39;">libwireshark</span> <span class="post-tag tag-link-stack" rel="tag" title="see questions tagged &#39;stack&#39;">stack</span> <span class="post-tag tag-link-dump" rel="tag" title="see questions tagged &#39;dump&#39;">dump</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Jul '13, 15:03</strong></p><img src="https://secure.gravatar.com/avatar/d3f6348f5e22d7cd8281c103cb6bc1d4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mark_till&#39;s gravatar image" /><p><span>mark_till</span><br />
<span class="score" title="0 reputation points">0</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mark_till has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>03 Jul '13, 18:15</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-22576" class="comments-container"></div><div id="comment-tools-22576" class="comment-tools"></div><div class="clear"></div><div id="comment-22576-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="22584"></span>

<div id="answer-container-22584" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22584-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22584-score" class="post-score" title="current number of votes">1</div><span id="post-22584-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><pre><code>Unhandled exception (group=1, code=6)</code></pre><p>Means, for Wireshark 1.0.6, that tshark ran out of memory--which isn't surprising given the size of your capture file. See the wiki page <a href="http://wiki.wireshark.org/KnownBugs/OutOfMemory">KnownBugs/OutOfMemory</a> for more details.</p><p>But, if you happen to be running on a 64-bit version of Windows and you've got lots of RAM, the newer version of tshark may work better (it will actually use more than 2 Gbytes of RAM).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Jul '13, 19:27</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>03 Jul '13, 18:14</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-22584" class="comments-container"></div><div id="comment-tools-22584" class="comment-tools"></div><div class="clear"></div><div id="comment-22584-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="22581"></span>

<div id="answer-container-22581" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22581-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22581-score" class="post-score" title="current number of votes">0</div><span id="post-22581-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Ok so I am updating to the latest Wireshark-win64-1.10.0 But bear in mind, if you didn't fix it, it ain't fixed.</p></blockquote><p>Wireshark 1.0.6 is really old and chances are good that this specific problem has been fixed some time ago. Please try the latest version and report back your results.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Jul '13, 15:54</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-22581" class="comments-container"></div><div id="comment-tools-22581" class="comment-tools"></div><div class="clear"></div><div id="comment-22581-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

