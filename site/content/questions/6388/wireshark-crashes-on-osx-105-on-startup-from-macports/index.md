+++
type = "question"
title = "Wireshark crashes on OSX 10.5 on startup, from macports"
description = '''I am trying to run wireshark on mac os x 10.5 leopard. I&#x27;ve installed it successfully via port. However, when I try to run it, wireshark crashes immediately. I tried uninstalling and installing from the .dmg file instead, but the same problem occurred. I can run other X11 programs without an issue. ...'''
date = "2011-09-15T07:11:00Z"
lastmod = "2011-09-15T11:33:00Z"
weight = 6388
keywords = [ "osx", "crash", "x11" ]
aliases = [ "/questions/6388" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark crashes on OSX 10.5 on startup, from macports](/questions/6388/wireshark-crashes-on-osx-105-on-startup-from-macports)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6388-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6388-score" class="post-score" title="current number of votes">0</div><span id="post-6388-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to run wireshark on mac os x 10.5 leopard. I've installed it successfully via <code>port</code>.</p><p>However, when I try to run it, wireshark crashes immediately. I tried uninstalling and installing from the <code>.dmg</code> file instead, but the same problem occurred. I can run other X11 programs without an issue. I am getting a <code>EXC_BAD_ACCESS (SIGBUS)</code> type error. Technically it is X11 that is crashing. Here is the dump:</p><pre><code>Process:         X11.bin [59230]
Path:            /Applications/Utilities/X11.app/Contents/MacOS/X11.bin
Identifier:      org.x.X11
Version:         2.1.6 (2.1.6)
Build Info:      X11server-480700~8
Code Type:       X86 (Native)
Parent Process:  X [59229]

Interval Since Last Report:          3437 sec
Crashes Since Last Report:           2
Per-App Interval Since Last Report:  5 sec
Per-App Crashes Since Last Report:   1

Date/Time:       2011-09-15 09:54:27.533 -0400
OS Version:      Mac OS X 10.5.8 (9L31a)
Report Version:  6
Anonymous UUID:  4F0C8C81-F209-47C5-B7EB-A6F069555C52

Exception Type:  EXC_BAD_ACCESS (SIGBUS)
Exception Codes: KERN_PROTECTION_FAILURE at 0x0000000000000000
Crashed Thread:  2

Application Specific Information:
X.Org X Server 1.4.2-apple33 Build Date: 20090617
...
Thread 2 Crashed:
0   X11.bin                         0x00025f38 RootlessGlyphs + 84
1   X11.bin                         0x0011e021 CompositeGlyphs + 163
2   X11.bin                         0x00121b60 ProcRenderCompositeGlyphs + 1526
3   X11.bin                         0x001236e8 ProcRenderDispatch + 60
4   X11.bin                         0x000ec41a XaceCatchExtProc + 173
5   X11.bin                         0x0007dad1 Dispatch + 691
6   X11.bin                         0x0009b497 dix_main + 1818
7   X11.bin                         0x00019526 server_thread + 62
8   libSystem.B.dylib               0x9574d155 _pthread_start + 321
9   libSystem.B.dylib               0x9574d012 thread_start + 34
...
Thread 2 crashed with X86 Thread State (32-bit):
  eax: 0x00000000  ebx: 0x00025ef5  ecx: 0x00000070  edx: 0x006c85c0
  edi: 0x00000003  esi: 0x00025ee4  ebp: 0xb019f618  esp: 0xb019f570
   ss: 0x0000001f  efl: 0x00010206  eip: 0x00025f38   cs: 0x00000017
   ds: 0x0000001f   es: 0x0000001f   fs: 0x0000001f   gs: 0x00000037
  cr2: 0x00000000
...</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-osx" rel="tag" title="see questions tagged &#39;osx&#39;">osx</span> <span class="post-tag tag-link-crash" rel="tag" title="see questions tagged &#39;crash&#39;">crash</span> <span class="post-tag tag-link-x11" rel="tag" title="see questions tagged &#39;x11&#39;">x11</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Sep '11, 07:11</strong></p><img src="https://secure.gravatar.com/avatar/c09e7876d5b9396739ef2723ff910a1c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hopeful&#39;s gravatar image" /><p><span>hopeful</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hopeful has no accepted answers">0%</span></p></div></div><div id="comments-container-6388" class="comments-container"></div><div id="comment-tools-6388" class="comment-tools"></div><div class="clear"></div><div id="comment-6388-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6403"></span>

<div id="answer-container-6403" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6403-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6403-score" class="post-score" title="current number of votes">0</div><span id="post-6403-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If it's X11 that crashes, than it's X11 that has the bug (regardless of whether other X11 programs don't have a problem; if an X server crashes, it's an X server bug, period). Report it to Apple.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Sep '11, 11:33</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-6403" class="comments-container"></div><div id="comment-tools-6403" class="comment-tools"></div><div class="clear"></div><div id="comment-6403-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

