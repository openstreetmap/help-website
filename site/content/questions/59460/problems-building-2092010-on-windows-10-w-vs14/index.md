+++
type = "question"
title = "Problems building 2.0.9/2.0.10 on Windows 10 w/ VS14"
description = '''Hi guys I&#x27;ve just upgraded my work laptop to Windows 10, and have reset my build environment, and after successfully building 2.2.4 (and having a couple of minor kinks to work out) I&#x27;ve decided to go back and build 2.0.9 or 2.0.10 I&#x27;m consistently getting the following error when building the soluti...'''
date = "2017-02-15T20:01:00Z"
lastmod = "2017-02-16T02:32:00Z"
weight = 59460
keywords = [ "win32", "build_error", "build", "epan" ]
aliases = [ "/questions/59460" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Problems building 2.0.9/2.0.10 on Windows 10 w/ VS14](/questions/59460/problems-building-2092010-on-windows-10-w-vs14)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59460-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi guys I've just upgraded my work laptop to Windows 10, and have reset my build environment, and after successfully building 2.2.4 (and having a couple of minor kinks to work out) I've decided to go back and build 2.0.9 or 2.0.10 I'm consistently getting the following error when building the solution</p><pre><code> 88&gt;ClCompile:
      capture_preferences_frame.cpp
112&gt;C:\Program Files (x86)\Windows Kits\8.1\Include\um\ws2tcpip.h(560): error C2373: &#39;ws_inet_pton&#39;: redefinition; different type modifiers (compiling source file C:\Wireshark\wireshark-2.0.9\epan\addr_resolv.c) [C:\Wireshark\build32\epan\epan.vcxproj]
      C:\Wireshark\wireshark-2.0.9\wsutil/inet_v6defs.h(42): note: see declaration of &#39;ws_inet_pton&#39; (compiling source file C:\Wireshark\wireshark-2.0.9\epan\addr_resolv.c)
112&gt;C:\Program Files (x86)\Windows Kits\8.1\Include\um\ws2tcpip.h(576): error C2373: &#39;ws_inet_ntop&#39;: redefinition; different type modifiers (compiling source file C:\Wireshark\wireshark-2.0.9\epan\addr_resolv.c) [C:\Wireshark\build32\epan\epan.vcxproj]
      C:\Wireshark\wireshark-2.0.9\wsutil/inet_v6defs.h(44): note: see declaration of &#39;ws_inet_ntop&#39; (compiling source file C:\Wireshark\wireshark-2.0.9\epan\addr_resolv.c)
      asn1.c
105&gt;ClCompile:
      proto_tree_model.c
113&gt;Link:</code></pre><p>Any ideas on what's going on with this? It's a bit unusual that both 2.0.9 and 2.0.10 have the issue on windows. Cheers</p></div><div id="question-tags" class="tags-container tags">win32 build_error build epan</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Feb '17, 20:01</strong></p><img src="https://secure.gravatar.com/avatar/c4a59238ef906285e110fa429a9a94b9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Scott%20Harman&#39;s gravatar image" /><p>Scott Harman<br />
<span class="score" title="46 reputation points">46</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Scott Harman has one accepted answer">50%</span></p></div></div><div id="comments-container-59460" class="comments-container"></div><div id="comment-tools-59460" class="comment-tools"></div><div class="clear"></div><div id="comment-59460-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="59463"></span>

<div id="answer-container-59463" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59463-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>MSVC2015 toolchain is not supported by Wireshark 2.0.X branch. Official versions are built with MSVC2013, so if you install this version it should work.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Feb '17, 02:32</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-59463" class="comments-container"><span id="59468"></span><div id="comment-59468" class="comment"><div id="post-59468-score" class="comment-score"></div><div class="comment-text"><p>More info here <a href="https://ask.wireshark.org/questions/49976/vs2015-error-c2220-define-ws_inet_pton-not-found">https://ask.wireshark.org/questions/49976/vs2015-error-c2220-define-ws_inet_pton-not-found</a></p></div><div id="comment-59468-info" class="comment-info"><span class="comment-age">(16 Feb '17, 06:25)</span> Anders ♦</div></div><span id="59543"></span><div id="comment-59543" class="comment"><div id="post-59543-score" class="comment-score"></div><div class="comment-text"><p>Yeah - I'm an idiot. Previous laptop had both products on there, and only used MSVC2013 for building wireshark and nothing else. Forgot I'd done that.</p></div><div id="comment-59543-info" class="comment-info"><span class="comment-age">(19 Feb '17, 22:10)</span> Scott Harman</div></div></div><div id="comment-tools-59463" class="comment-tools"></div><div class="clear"></div><div id="comment-59463-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

