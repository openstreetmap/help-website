+++
type = "question"
title = "error building plugin"
description = '''Hi, I am trying to build a custom dissector as a plugin starting from an existing dissector code, in this case the iec104 dissector (iec104.c). I downloaded the source files for Wireshark and was able to compile the code. As a first test, I just used the existing dissector code of the iec104 protoco...'''
date = "2015-11-04T14:05:00Z"
lastmod = "2016-02-25T05:07:00Z"
weight = 47261
keywords = [ "dissector", "error", "plugin", "custom" ]
aliases = [ "/questions/47261" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [error building plugin](/questions/47261/error-building-plugin)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47261-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47261-score" class="post-score" title="current number of votes">0</div><span id="post-47261-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am trying to build a custom dissector as a plugin starting from an existing dissector code, in this case the iec104 dissector (iec104.c). I downloaded the source files for Wireshark and was able to compile the code. As a first test, I just used the existing dissector code of the iec104 protocol without modifications and tried to compile it as a plugin. I followed all the steps as described in this tutorial: <a href="http://www.sewio.net/open-sniffer/develop/how-to-compile-your-wireshark-dissector/">http://www.sewio.net/open-sniffer/develop/how-to-compile-your-wireshark-dissector/</a></p><p>Still, I am getting the following errors when compiling the plugin:</p><pre><code>ERROR: Cannot determine the location of the VS Common Tools folder.

Microsoft (R) Program Maintenance Utility Version 12.00.21005.1
Copyright (C) Microsoft Corporation.  All rights reserved.

        cl  /DWINPCAP_VERSION=4_1_3 /Zi /W3 /MD /O2 /DWIN32_LEAN_AND_MEAN /DMSC_VER_REQUIRED=1800  /D_CRT_SECURE_NO_DEPRECATE /D_CRT_NONSTDC_NO_DEPRECATE -DPSAPI_VERSION=1 /D_ALLOW_KEYWORD_MACROS /DBUILD_WINDOWS /D_BIND_TO_CURRENT_CRT_VERSION=1 /MP /GS /w34295  /I../.. /Ih:\Documents\DevelopmentWireshark\Wireshark-win32-libs-1.12\gtk2\include\glib-2.0  /Ih:\Documents\DevelopmentWireshark\Wireshark-win32-libs-1.12\gtk2\lib\glib-2.0\include  -DG_DISABLE_DEPRECATED  -DG_DISABLE_SINGLE_INCLUDES  /Ih:\Documents\DevelopmentWireshark\Wireshark-win32-libs-1.12\Wdpack\include -Fd.\ -c packet-iec104.c
Microsoft (R) C/C++ Optimizing Compiler Version 18.00.31101 for x86
Copyright (C) Microsoft Corporation.  All rights reserved.

packet-iec104.c

packet-iec104.c(1810) : error C2099: initializer is not a constant

packet-iec104.c(1810) : warning C4047: &#39;initializing&#39; : &#39;const void *&#39; differs in levels of indirection from &#39;int&#39;

packet-iec104.c(1810) : warning C4047: &#39;initializing&#39; : &#39;guint32&#39; differs in levels of indirection from &#39;char [17]&#39;

packet-iec104.c(1810) : warning C4047: &#39;initializing&#39; : &#39;const char *&#39; differs in levels of indirection from &#39;int&#39;

packet-iec104.c(1810) : warning C4047: &#39;initializing&#39; : &#39;int&#39; differs in levels of indirection from &#39;void *&#39;

packet-iec104.c(1810) : warning C4047: &#39;initializing&#39; : &#39;guint32&#39; differs in levels of indirection from &#39;char [8]&#39;

packet-iec104.c(1810) : warning C4047: &#39;initializing&#39; : &#39;guint32&#39; differs in levels of indirection from &#39;char [7]&#39;

NMAKE : fatal error U1077: &#39;&quot;C:\Program Files\Microsoft Visual Studio 12.0\VC\BI
N\cl.EXE&quot;&#39; : return code &#39;0x2&#39;

Stop.</code></pre><p>Does anyone know what I'm doing wrong? As i said before, I didn't even modify the dissector code yet.</p><p>Many thanks!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span> <span class="post-tag tag-link-plugin" rel="tag" title="see questions tagged &#39;plugin&#39;">plugin</span> <span class="post-tag tag-link-custom" rel="tag" title="see questions tagged &#39;custom&#39;">custom</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Nov '15, 14:05</strong></p><img src="https://secure.gravatar.com/avatar/9b121a939eea20150a5045194794239e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kenny&#39;s gravatar image" /><p><span>kenny</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kenny has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>04 Nov '15, 14:25</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-47261" class="comments-container"><span id="47296"></span><div id="comment-47296" class="comment"><div id="post-47296-score" class="comment-score"></div><div class="comment-text"><p>Presumably your packet-iec104.c is not compatible with your Wireshark version due to some API changes, but without seeing the file content we can only guess.</p></div><div id="comment-47296-info" class="comment-info"><span class="comment-age">(05 Nov '15, 08:48)</span> <span class="comment-user userinfo">Pascal Quantin</span></div></div><span id="47298"></span><div id="comment-47298" class="comment"><div id="post-47298-score" class="comment-score">1</div><div class="comment-text"><p>The question states that they compiled the source code of the dissector successfully in it's normal place and then moved it to a plug-in.</p><p>If changes have been made to packet-iec104.c, then we would need to see them to help further.</p></div><div id="comment-47298-info" class="comment-info"><span class="comment-age">(05 Nov '15, 08:55)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="50500"></span><div id="comment-50500" class="comment"><div id="post-50500-score" class="comment-score"></div><div class="comment-text"><p>I try to do exactly the same thing with another dissector (convert it to plugin and then do my private modifications). I get the same errors.</p><p>The initializer that is not a constant is this one : static hf_register_info hf[] = {...</p><p>I my case, I couldn't use tfs_true_false, I had to re-define it manually.</p></div><div id="comment-50500-info" class="comment-info"><span class="comment-age">(25 Feb '16, 02:24)</span> <span class="comment-user userinfo">atsju2</span></div></div><span id="50506"></span><div id="comment-50506" class="comment"><div id="post-50506-score" class="comment-score"></div><div class="comment-text"><p>That tutorial is now very dated and it commits a cardinal sin (IMHO) of adding Cygwin to the path.</p><p>The issue with tfs_true_false is possibly incorrect export/import of definitions across DLL boundaries of libwireshark and the plugin. Unfortunately I don't know the solution to that.</p></div><div id="comment-50506-info" class="comment-info"><span class="comment-age">(25 Feb '16, 05:07)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-47261" class="comment-tools"></div><div class="clear"></div><div id="comment-47261-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

