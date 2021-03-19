+++
type = "question"
title = "NMAKE : fatal error U1073"
description = '''I find this error while i am trying to execute  C:&#92;Workplace&#92;Development&#92;wireshark-1.12.3&amp;gt;nmake -f Makefile.nmake all Microsoft (R) Program Maintenance Utility Version 1.50 Copyright (c) Microsoft Corp 1988-94. All rights reserved. NMAKE : fatal error U1073: don&#x27;t know how to make &#x27;Wireshark-win3...'''
date = "2015-02-26T03:37:00Z"
lastmod = "2015-03-05T01:47:00Z"
weight = 40092
keywords = [ "build", "wireshark" ]
aliases = [ "/questions/40092" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [NMAKE : fatal error U1073](/questions/40092/nmake-fatal-error-u1073)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40092-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40092-score" class="post-score" title="current number of votes">0</div><span id="post-40092-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I find this error while i am trying to execute</p><p>C:\Workplace\Development\wireshark-1.12.3&gt;nmake -f Makefile.nmake all</p><p>Microsoft (R) Program Maintenance Utility Version 1.50 Copyright (c) Microsoft Corp 1988-94. All rights reserved.</p><p>NMAKE : fatal error U1073: don't know how to make 'Wireshark-win32-libs-1.12\c-a res-1.9.1-1-win32ws\bin\libcares-2.dll' Stop.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-build" rel="tag" title="see questions tagged &#39;build&#39;">build</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Feb '15, 03:37</strong></p><img src="https://secure.gravatar.com/avatar/302a32bb6a6f237c61731914f3657167?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dhruv%20Gupta&#39;s gravatar image" /><p><span>Dhruv Gupta</span><br />
<span class="score" title="6 reputation points">6</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dhruv Gupta has no accepted answers">0%</span></p></div></div><div id="comments-container-40092" class="comments-container"><span id="40093"></span><div id="comment-40093" class="comment"><div id="post-40093-score" class="comment-score"></div><div class="comment-text"><p>What does <code>nmake -f makefile.nmake verify_tools</code> show?</p></div><div id="comment-40093-info" class="comment-info"><span class="comment-age">(26 Feb '15, 03:52)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="40116"></span><div id="comment-40116" class="comment"><div id="post-40116-score" class="comment-score"></div><div class="comment-text"><p><code> C:\Workplace\Development\wireshark-1.12.3&gt;nmake -f Makefile.nmake verify_tools</code></p><p><code></code></p><p><code>Microsoft (R) Program Maintenance Utility   Version 1.50 Copyright (c) Microsoft Corp 1988-94. All rights reserved.</code></p><code></code><p>Checking for required applications: cl: /cygdrive/c/Program Files/Microsoft Visual Studio 9.0/VC/bin/x86_amd 64/cl link: /cygdrive/c/Program Files/Microsoft Visual Studio 9.0/VC/BIN/link</p><pre><code>    nmake: nmake
    bash: /usr/bin/bash
    bison: /usr/bin/bison
    flex: /usr/bin/flex
    env: /usr/bin/env
    grep: /usr/bin/grep
    /usr/bin/find: /usr/bin/find
    peflags: /usr/bin/peflags
    perl: /usr/bin/perl
    c:\Qt\4.8\vs2008\bin\qmake: /cygdrive/c/Qt/4.8/vs2008/bin/qmake
    sed: /usr/bin/sed
    unzip: /usr/bin/unzip
    wget: /usr/bin/wget</code></pre></code><p><code></code></p></div><div id="comment-40116-info" class="comment-info"><span class="comment-age">(27 Feb '15, 01:16)</span> <span class="comment-user userinfo">Dhruv Gupta</span></div></div><span id="40117"></span><div id="comment-40117" class="comment"><div id="post-40117-score" class="comment-score"></div><div class="comment-text"><p>Have you run the setup target to download the required packages?</p></div><div id="comment-40117-info" class="comment-info"><span class="comment-age">(27 Feb '15, 01:53)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="40118"></span><div id="comment-40118" class="comment"><div id="post-40118-score" class="comment-score"></div><div class="comment-text"><p>Yes Sir..</p><p>nmake -f Makefile.nmake setup executed successfully..</p></div><div id="comment-40118-info" class="comment-info"><span class="comment-age">(27 Feb '15, 02:25)</span> <span class="comment-user userinfo">Dhruv Gupta</span></div></div><span id="40119"></span><div id="comment-40119" class="comment"><div id="post-40119-score" class="comment-score"></div><div class="comment-text"><p><code> C:\Workplace\Development\wireshark-1.12.3&gt;nmake -f Makefile.nmake setup</code></p><p><code></code></p><p><code>Microsoft (R) Program Maintenance Utility   Version 1.50 Copyright (c) Microsoft Corp 1988-94. All rights reserved.</code></p><code></code><p><code>Checking for required applications:         cl: /cygdrive/c/Program Files/Microsoft Visual Studio 9.0/VC/bin/x86_amd64/cl         link: /usr/bin/link         nmake: nmake         bash: /usr/bin/bash         bison: /usr/bin/bison         flex: /usr/bin/flex         env: /usr/bin/env         grep: /usr/bin/grep         /usr/bin/find: /usr/bin/find         peflags: /usr/bin/peflags         perl: /usr/bin/perl         sed: /usr/bin/sed         unzip: /usr/bin/unzip         wget: /usr/bin/wget         cd "C:\Wireshark-win32-libs-1.12"         rm -r -f adns-1.0-win32-05ws         rm -r -f c-ares-1.5.3ws         rm -r -f c-ares-1.6.0ws         rm -r -f c-ares-1.7.0-win??ws         rm -r -f c-ares-1.7.1-win??ws         rm -r -f c-ares-1.9.1-1-win??ws         rm -r -f gettext-0.14.5         rm -r -f gettext-runtime-0.17         rm -r -f gettext-runtime-0.17-1         rm -r -f gettext-0.17-1            # win64         rm -r -f glib         rm -r -f gnutls-2.8.1-1         rm -r -f gnutls-2.8.5--win??ws         rm -r -f gnutls-2.10.3--win??ws         rm -r -f gnutls-2.12.18--win??ws         rm -r -f gnutls-3.1.22--win??ws         rm -r -f gnutls-3.2.15-*-win??ws         rm -r -f gtk2         rm -r -f gtk+         rm -r -f gtk-wimp         rm -r -f kfw-2.5         rm -r -f kfw-3-2-2-final         rm -r -f kfw-3.2.2-ws1         rm -r -f kfw-3-2-2-i386-ws-vc6         rm -r -f libiconv-1.9.1.bin.woe32         rm -r -f lua5.1         rm -r -f lua5.1.4         rm -r -f lua5.2.?         rm -r -f libsmi-0.4.5         rm -r -f libsmi-0.4.8         rm -r -f libsmi-svn-40773-win??ws         rm -r -f nasm-2.00         rm -r -f nasm-2.02         rm -r -f nasm-2.09.08         rm -r -f pcre-6.4         rm -r -f pcre-7.0         rm -r -f portaudio_v19         rm -r -f portaudio_v19_2         rm -r -f upx301w         rm -r -f upx303w         rm -r -f user-guide         rm -r -f zlib123         rm -r -f zlib125         rm -r -f zlib-1.2.5         rm -r -f zlib123-dll         rm -r -f AirPcap_Devpack_1_0_0_594         rm -r -f AirPcap_Devpack_4_0_0_1480         rm -r -f AirPcap_Devpack_4_1_0_1622         rm -r -f GeoIP-1.4.5ws         rm -r -f GeoIP-1.4.6-win??ws         rm -r -f GeoIP-1.4.8-win??ws</code></p></div><div id="comment-40119-info" class="comment-info"><span class="comment-age">(27 Feb '15, 02:32)</span> <span class="comment-user userinfo">Dhruv Gupta</span></div></div><span id="40120"></span><div id="comment-40120" class="comment not_top_scorer"><div id="post-40120-score" class="comment-score"></div><div class="comment-text"><p>Downloaded all the packages</p><p><code> *** user-guide-g7ea0d6c.zip *** No HTTP proxy specified (http_proxy and HTTP_PROXY are empty). Downloading user-guide-g7ea0d6c.zip into '/cygdrive/c/Wireshark-win32-libs-1.12', installing into user-guide File 'user-guide-g7ea0d6c.zip' already there; not retrieving.</code></p><p><code></code></p><p><code>Extracting '/cygdrive/c/Wireshark-win32-libs-1.12/user-guide-g7ea0d6c.zip' into'/cygdrive/c/Wireshark-win32-libs-1.12/user-guide' Verifying that the DLLs and EXEs in user-guide are executable.</code></p><code></code><p><strong><em><strong><em>upx303w.zip</em></strong></em></strong> No HTTP proxy specified (http_proxy and HTTP_PROXY are empty). Downloading upx303w.zip into '/cygdrive/c/Wireshark-win32-libs-1.12', installing into . File 'upx303w.zip' already there; not retrieving.</p><p>Extracting '/cygdrive/c/Wireshark-win32-libs-1.12/upx303w.zip' into '/cygdrive/c/Wireshark-win32-libs-1.12/.' Verifying that the DLLs and EXEs in . are executable.</p><p><strong><em><strong><em>nasm-2.09.08-win32.zip</em></strong></em></strong> No HTTP proxy specified (http_proxy and HTTP_PROXY are empty). Downloading nasm-2.09.08-win32.zip into '/cygdrive/c/Wireshark-win32-libs-1.12', installing into . File 'nasm-2.09.08-win32.zip' already there; not retrieving.</p><p>Extracting '/cygdrive/c/Wireshark-win32-libs-1.12/nasm-2.09.08-win32.zip' into '/cygdrive/c/Wireshark-win32-libs-1.12/.' Verifying that the DLLs and EXEs in . are executable.</p></code><p><code>Wireshark is ready to build.</code></p></div><div id="comment-40120-info" class="comment-info"><span class="comment-age">(27 Feb '15, 02:34)</span> <span class="comment-user userinfo">Dhruv Gupta</span></div></div></div><div id="comment-tools-40092" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-40092-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="40124"></span>

<div id="answer-container-40124" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40124-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40124-score" class="post-score" title="current number of votes">0</div><span id="post-40124-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>OK, it appears to me that you're attempting to build Wireshark 1.12.3 64 bit using VS2008 and with QT. I'm not entirely sure this will work.</p><p>For 1.12.3 the recommended compiler is VS2010, the Express edition will build as well as regular editions, but VS2013 Community Edition is also free to install and works as well.</p><p>From your output, the first run of verify_tools looks odd, you have the 32 bit amd64 compiler listed and the 32 bit x86 linker and the nmake item should I think have the full path to nmake the same as cl and the linker:</p><pre><code>cl: /cygdrive/c/Program Files/Microsoft Visual Studio 9.0/VC/bin/x86_amd64/cl
link: /cygdrive/c/Program Files/Microsoft Visual Studio 9.0/VC/BIN/link
nmake: nmake</code></pre><p>The second run as part of setup has an incorrect linker (the Cygwin one):</p><pre><code>cl: /cygdrive/c/Program Files/Microsoft Visual Studio 9.0/VC/bin/x86_amd64/cl
link: /usr/bin/link
nmake: nmake</code></pre><p>So there's something odd in your environment. How did you setup the command prompt for building?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Feb '15, 03:54</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-40124" class="comments-container"><span id="40265"></span><div id="comment-40265" class="comment"><div id="post-40265-score" class="comment-score"></div><div class="comment-text"><p>its done.., thanks grahamb</p></div><div id="comment-40265-info" class="comment-info"><span class="comment-age">(04 Mar '15, 19:38)</span> <span class="comment-user userinfo">Dhruv Gupta</span></div></div><span id="40269"></span><div id="comment-40269" class="comment"><div id="post-40269-score" class="comment-score"></div><div class="comment-text"><p>It might help others if you describe what your actual issue was and how you fixed it.</p><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-40269-info" class="comment-info"><span class="comment-age">(05 Mar '15, 01:47)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-40124" class="comment-tools"></div><div class="clear"></div><div id="comment-40124-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

