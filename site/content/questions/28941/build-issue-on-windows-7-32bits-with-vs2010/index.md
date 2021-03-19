+++
type = "question"
title = "build issue on windows 7, 32bits with VS2010"
description = '''Hi all, I got a issue on compiling. after &#x27;nmake -f Makefile.nmake setup&#x27;, the following message was displayed and failed. ... ****** WinPcap_4_1_3.exe ****** No HTTP proxy specified (http_proxy and HTTP_PROXY are empty). Downloading WinPcap_4_1_3.exe into &#x27;/cygdrive/c/Wireshark-win32-libs-1.10&#x27;, in...'''
date = "2014-01-15T17:53:00Z"
lastmod = "2014-01-15T19:05:00Z"
weight = 28941
keywords = [ "build_error" ]
aliases = [ "/questions/28941" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [build issue on windows 7, 32bits with VS2010](/questions/28941/build-issue-on-windows-7-32bits-with-vs2010)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28941-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all, I got a issue on compiling.</p><p>after 'nmake -f Makefile.nmake setup', the following message was displayed and failed.</p><p>...</p><pre><code>****** WinPcap_4_1_3.exe ******
No HTTP proxy specified (http_proxy and HTTP_PROXY are empty).
Downloading WinPcap_4_1_3.exe into &#39;/cygdrive/c/Wireshark-win32-libs-1.10&#39;, installing into .
--2014-01-16 10:40:16--  http://anonsvn.wireshark.org/wireshark-win32-libs/tags/2013-04-22/packages//WinPcap_4_1_3.exe
Resolving anonsvn.wireshark.org (anonsvn.wireshark.org)... 174.137.42.70
Connecting to anonsvn.wireshark.org (anonsvn.wireshark.org)|174.137.42.70|:80... failed: Connection timed out.
Retrying.

--2014-01-16 10:40:38--  (try: 2)  http://anonsvn.wireshark.org/wireshark-win32-libs/tags/2013-04-22/packages//WinPcap_4_1_3.exe
Connecting to anonsvn.wireshark.org (anonsvn.wireshark.org)|174.137.42.70|:80... failed: Connection timed out.
Retrying.</code></pre><p>....</p><p>could u plz inform how to solve this issue? Thank you.</p></div><div id="question-tags" class="tags-container tags">build_error</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Jan '14, 17:53</strong></p><img src="https://secure.gravatar.com/avatar/1093195e125343067453a8d21cec3f03?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ssmage&#39;s gravatar image" /><p>ssmage<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ssmage has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 15 Jan '14, 19:00</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-28941" class="comments-container"></div><div id="comment-tools-28941" class="comment-tools"></div><div class="clear"></div><div id="comment-28941-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="28943"></span>

<div id="answer-container-28943" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28943-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Try to go to <a href="http://anonsvn.wireshark.org/wireshark-win32-libs/tags/2013-04-22/packages/">http://anonsvn.wireshark.org/wireshark-win32-libs/tags/2013-04-22/packages/</a> on the machine on which you're trying to do the build.</p><p>If that works - i.e., if it shows you a page with a bunch of directories and files on it - try the build again.</p><p>If that doesn't work, then there's some networking or server problem, which will probably be reported by your browser. If it's a local networking problem, fix it, and try the build again. If it's a server problem, or a networking problem with equipment that you don't manage, wait for that problem to be fixed and try again.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jan '14, 19:05</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-28943" class="comments-container"></div><div id="comment-tools-28943" class="comment-tools"></div><div class="clear"></div><div id="comment-28943-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

