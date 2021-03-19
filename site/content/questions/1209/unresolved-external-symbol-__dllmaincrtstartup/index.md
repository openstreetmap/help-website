+++
type = "question"
title = "unresolved external symbol __DllMainCRTStartup"
description = '''When building Wireshark under Windows 7, I receive the error above after changing to the wsutil directory. I&#x27;m not familiar with biulding DLLs, but I would have thought the DllMainCRTStartup function should have been found in one of the *.c files within wsutil - but it isn&#x27;t. Here&#x27;s the output I get...'''
date = "2010-12-02T07:50:00Z"
lastmod = "2010-12-03T16:12:00Z"
weight = 1209
keywords = [ "symbol", "unresolved", "external", "__dllmaincrtstartup" ]
aliases = [ "/questions/1209" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [unresolved external symbol \_\_DllMainCRTStartup](/questions/1209/unresolved-external-symbol-__dllmaincrtstartup)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1209-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1209-score" class="post-score" title="current number of votes">0</div><span id="post-1209-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When building Wireshark under Windows 7, I receive the error above after changing to the wsutil directory. I'm not familiar with biulding DLLs, but I would have thought the DllMainCRTStartup function should have been found in one of the *.c files within wsutil - but it isn't. Here's the output I get from running the "nmake -f Makefile.nmake all" command: &lt;previous packages="" built="" correctly...=""&gt; cd wsutil "C:Program Files (x86)Microsoft Visual Studio 8VCBINnmake.exe" / -f Makefile.nmake</p><p>Microsoft (R) Program Maintenance Utility Version 8.00.50727.762 Copyright (C) Microsoft Corporation. All rights reserved.</p><pre><code>    link  /INCREMENTAL:NO /NOLOGO -entry:_DllMainCRTStartup -dll kernel32.lib  ws2_32.lib mswsock.lib advapi32.lib bufferoverflowu.lib  /DEBUG /MACHINE:x86 /MANIFEST:no  /DEF:l</code></pre><p>ibwsutil.def /OUT:libwsutil.dll /IMPLIB:libwsutil.lib ..imagelibwsutil.res file_util.obj inet_aton.obj inet_ntop.obj inet_pton.obj mpe g-audio.obj privileges.obj str_util.obj type_util.obj strptime.obj unicode-utils.obj wsgetopt.obj C:wireshark-win32-libsgtk2libglib-2.0.lib C:wireshark-win32-libsgtk2libgmodule-2.0.lib C:wireshark-win32-libsgtk2libgobject-2.0.lib Creating library libwsutil.lib and object libwsutil.exp LINK : error LNK2001: unresolved external symbol __DllMainCRTStartup libwsutil.dll : fatal error LNK1120: 1 unresolved externals NMAKE : fatal error U1077: '"C:Program Files (x86)Microsoft Visual Studio 8VCBINlink.EXE"' : return code '0x460' Stop. NMAKE : fatal error U1077: '"C:Program Files (x86)Microsoft Visual Studio 8VCBINnmake.exe"' : return code '0x2' Stop.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-symbol" rel="tag" title="see questions tagged &#39;symbol&#39;">symbol</span> <span class="post-tag tag-link-unresolved" rel="tag" title="see questions tagged &#39;unresolved&#39;">unresolved</span> <span class="post-tag tag-link-external" rel="tag" title="see questions tagged &#39;external&#39;">external</span> <span class="post-tag tag-link-__dllmaincrtstartup" rel="tag" title="see questions tagged &#39;__dllmaincrtstartup&#39;">__dllmaincrtstartup</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Dec '10, 07:50</strong></p><img src="https://secure.gravatar.com/avatar/431cae126bbbaa91e2ce9aa3e1743a24?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Saul&#39;s gravatar image" /><p><span>Saul</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Saul has no accepted answers">0%</span></p></div></div><div id="comments-container-1209" class="comments-container"></div><div id="comment-tools-1209" class="comment-tools"></div><div class="clear"></div><div id="comment-1209-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="1210"></span>

<div id="answer-container-1210" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1210-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1210-score" class="post-score" title="current number of votes">0</div><span id="post-1210-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I don't specifically know what the problem is....</p><p>I have no troubles when building with Visual Studio 2008 (VC9).</p><p>I notice you appear to be building with Visual Studio 2005 (VC8).</p><p>Have you commented / uncommented the proper lines in config.nmake to indicate the compiler you are using ?</p><p>(config.make as distributed indicates that Visual Studio 2008 (VC9) is being used).</p><p>Is there any particular reason you are using VC8 ? Wireshark is built using VC9 these days.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Dec '10, 08:50</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p><span>Bill Meier ♦♦</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>02 Dec '10, 09:19</strong> </span></p></div></div><div id="comments-container-1210" class="comments-container"><span id="1228"></span><div id="comment-1228" class="comment"><div id="post-1228-score" class="comment-score"></div><div class="comment-text"><p>Yes, I modified the config.nmake file to account for the correct version of VS. The reason I'm using VC8 is because that is the version I own - and I can't afford to upgrade at the moment.</p><p>I did note that even though my user account has administrator privileges under Windows 7, there are times that subdirectory creation fails. I will be backing out the various tools (for example, TortoiseSVN never worked properly) and will be re-installing everything specifically as administrator.</p></div><div id="comment-1228-info" class="comment-info"><span class="comment-age">(03 Dec '10, 08:42)</span> <span class="comment-user userinfo">Saul</span></div></div><span id="1229"></span><div id="comment-1229" class="comment"><div id="post-1229-score" class="comment-score"></div><div class="comment-text"><p>Just as an FYI:</p><p>A free version of VS2008 (VS2008EE) can be downloaded from Microsoft.</p><p>See: http://www.wireshark.org/docs/wsdg_html_chunked /ChSetupWin32.html#ChSetupMSVC</p></div><div id="comment-1229-info" class="comment-info"><span class="comment-age">(03 Dec '10, 08:50)</span> <span class="comment-user userinfo">Bill Meier ♦♦</span></div></div><span id="1237"></span><div id="comment-1237" class="comment"><div id="post-1237-score" class="comment-score"></div><div class="comment-text"><p>Yep - tried that. Downloaded the VS2008 and installed it. Did a "distclean" - made sure I ran the correct batch file to set up the path, yada yada - and still bombed out at the same point with the same error. I ran all this as the "adminstrator" under Windows 7.</p></div><div id="comment-1237-info" class="comment-info"><span class="comment-age">(03 Dec '10, 16:11)</span> <span class="comment-user userinfo">Saul</span></div></div><span id="1238"></span><div id="comment-1238" class="comment"><div id="post-1238-score" class="comment-score"></div><div class="comment-text"><p>BTW: I did remember to change config.nmake back to the correct VS2008) version before doing the nmake ... all.</p></div><div id="comment-1238-info" class="comment-info"><span class="comment-age">(03 Dec '10, 16:12)</span> <span class="comment-user userinfo">Saul</span></div></div></div><div id="comment-tools-1210" class="comment-tools"></div><div class="clear"></div><div id="comment-1210-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

