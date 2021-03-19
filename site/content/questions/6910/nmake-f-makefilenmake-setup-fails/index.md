+++
type = "question"
title = "nmake -f Makefile.nmake setup Fails"
description = '''Anyone know what I&#x27;m missing to cause the uzip err during the make setup? &amp;gt;nmake -f Makefile.nmake setup  Microsoft (R) Program Maintenance Utility Version 10.00.30319.01 Copyright (C) Microsoft Corporation. All rights reserved.  Checking for required applications:  cl: /cygdrive/c/Program Files/...'''
date = "2011-10-16T16:36:00Z"
lastmod = "2014-05-30T07:43:00Z"
weight = 6910
keywords = [ "development" ]
aliases = [ "/questions/6910" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [nmake -f Makefile.nmake setup Fails](/questions/6910/nmake-f-makefilenmake-setup-fails)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6910-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6910-score" class="post-score" title="current number of votes">1</div><span id="post-6910-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Anyone know what I'm missing to cause the uzip err during the make setup?</p><pre><code>&gt;nmake -f Makefile.nmake setup

Microsoft (R) Program Maintenance Utility Version 10.00.30319.01
Copyright (C) Microsoft Corporation.  All rights reserved.

Checking for required applications:
        cl: /cygdrive/c/Program Files/Microsoft Visual Studio 10.0/VC/bin/cl
        link: /cygdrive/c/Program Files/Microsoft Visual Studio 10.0/VC/bin/link

        nmake: /cygdrive/c/Program Files/Microsoft Visual Studio 10.0/VC/bin/nmake
        mt: /cygdrive/c/Program Files/Microsoft SDKs/Windows/v7.0A/bin/mt
        bash: /usr/bin/bash
        bison: /cygdrive/c/Program Files/GnuWin32/bin/bison
        flex: /cygdrive/c/Program Files/GnuWin32/bin/flex
        env: /usr/bin/env
        grep: /usr/bin/grep
        /usr/bin/find: /usr/bin/find
        perl: /cygdrive/c/Perl/bin/perl
        C:\Python27\python.exe: /cygdrive/c/Python27/python.exe
        sed: /usr/bin/sed
        unzip: /cygdrive/c/oracle/product/10.2.0/client_2/bin/unzip
        wget: /cygdrive/c/wget/wget
        cd C:\wireshark-win32-libs-1.6
        rm -r -f adns-1.0-win32-05ws
        rm -r -f c-ares-1.5.3ws
        rm -r -f c-ares-1.6.0ws
        rm -r -f c-ares-1.7.0-win??ws
        rm -r -f c-ares-1.7.1-win??ws
        rm -r -f gettext-0.14.5
        rm -r -f gettext-runtime-0.17
        rm -r -f gettext-runtime-0.17-1
        rm -r -f gettext-0.17-1            # win64
        rm -r -f glib
        rm -r -f gnutls-2.8.1-1
        rm -r -f gnutls-2.8.5-*-win??ws
        rm -r -f gnutls-2.10.3-*-win??ws
        rm -r -f gtk2
        rm -r -f gtk+
        rm -r -f gtk-wimp
        rm -r -f kfw-2.5
        rm -r -f kfw-3.2.2-ws1
        rm -r -f kfw-3.2.2-i386-ws-vc6
        rm -r -f libiconv-1.9.1.bin.woe32
        rm -r -f lua5.1
        rm -r -f lua5.1.4
        rm -r -f libsmi-0.4.5
        rm -r -f libsmi-0.4.8
        rm -r -f nasm-2.00
        rm -r -f nasm-2.02
        rm -r -f nasm-2.09.08
        rm -r -f pcre-6.4
        rm -r -f pcre-7.0
        rm -r -f portaudio_v19
        rm -r -f portaudio_v19_2
        rm -r -f user-guide
        rm -r -f WpdPack
        rm -r -f AirPcap_Devpack_1_0_0_594
        rm -r -f AirPcap_Devpack_4_0_0_1480
        rm -r -f AirPcap_Devpack_4_1_0_1622
        rm -r -f zlib123
        rm -r -f zlib-1.2.5
        rm -r -f zlib123-dll
        rm -r -f upx301w
        rm -r -f upx303w
        rm -r -f GeoIP-1.4.5ws
        rm -r -f GeoIP-1.4.6-win??ws
        cd &quot;C:\Documents and Settings\mwoscek\My Documents\Develop\wireshark\wireshark-1.6.2&quot;

****** gtk+-bundle_2.22.1-20101227_win32.zip ******
No HTTP proxy specified (http_proxy and HTTP_PROXY are empty).
Downloading gtk+-bundle_2.22.1-20101227_win32.zip into /cygdrive/c/wireshark-win
32-libs-1.6, installing into gtk2
File `gtk+-bundle_2.22.1-20101227_win32.zip&#39; already there; not retrieving.

Extracting /cygdrive/c/wireshark-win32-libs-1.6/gtk+-bundle_2.22.1-20101227_win3
2.zip into /cygdrive/c/wireshark-win32-libs-1.6/gtk2
unzip:  cannot find either /cygdrive/c/wireshark-win32-libs-1.6/gtk+-bundle_2.22
.1-20101227_win32.zip or /cygdrive/c/wireshark-win32-libs-1.6/gtk+-bundle_2.22.1
-20101227_win32.zip.zip.

ERROR: Couldn&#39;t unpack /cygdrive/c/wireshark-win32-libs-1.6/gtk+-bundle_2.22.1-2
0101227_win32.zip

NMAKE : fatal error U1077: &#39;C:\cygwin\bin\bash.EXE&#39; : return code &#39;0x1&#39;
Stop.</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Oct '11, 16:36</strong></p><img src="https://secure.gravatar.com/avatar/16ee3260cae2e4ee17ce5ddf04a567aa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="marwos&#39;s gravatar image" /><p><span>marwos</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="marwos has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>16 Oct '11, 17:20</strong> </span></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-6910" class="comments-container"></div><div id="comment-tools-6910" class="comment-tools"></div><div class="clear"></div><div id="comment-6910-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6911"></span>

<div id="answer-container-6911" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6911-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6911-score" class="post-score" title="current number of votes">6</div><span id="post-6911-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><pre><code>unzip:/cygdrive/c/oracle/product/10.2.0/client_2/bin/unzip</code></pre><p>Looks like your path is such that a different unzip than the cygwin unzip is being invoked.</p><pre><code>cl: /cygdrive/c/Program Files/Microsoft VisualStudio 10.0/VC/bin/cl
link: /cygdrive/c/Program Files/Microsoft Visual Studio 10.0/VC/bin/link
nmake: /cygdrive/c/Program Files/Microsoft Visual Studio 10.0/VC/bin/nmake
mt: /cygdrive/c/Program Files/Microsoft SDKs/Windows/v7.0A/bin/mt
bash:/usr/bin/bash
bison: /cygdrive/c/Program Files/GnuWin32/bin/bison
flex: /cygdrive/c/Program Files/GnuWin32/bin/flex
env: /usr/bin/env
grep: /usr/bin/grep
/usr/bin/find: /usr/bin/find
perl: /cygdrive/c/Perl/bin/perl
C:Python27python.exe: /cygdrive/c/Python27/python.exe
sed: /usr/bin/sed
unzip:/cygdrive/c/oracle/product/10.2.0/client_2/bin/unzip
wget: /cygdrive/c/wget/wget</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Oct '11, 16:57</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p><span>Bill Meier ♦♦</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div></div><div id="comments-container-6911" class="comments-container"><span id="6930"></span><div id="comment-6930" class="comment"><div id="post-6930-score" class="comment-score"></div><div class="comment-text"><p>I dont have cygwin's unzip, only:</p><blockquote><p>ls /usr/bin/<em>unzip</em> /usr/bin/bunzip2.exe /usr/bin/gunzip</p></blockquote><p>I suppose a reinstall of cygwin is needed?</p></div><div id="comment-6930-info" class="comment-info"><span class="comment-age">(17 Oct '11, 12:15)</span> <span class="comment-user userinfo">marwos</span></div></div><span id="6931"></span><div id="comment-6931" class="comment"><div id="post-6931-score" class="comment-score"></div><div class="comment-text"><p>OK -Have to manually select packages needed from the cygwin install. Done...</p></div><div id="comment-6931-info" class="comment-info"><span class="comment-age">(17 Oct '11, 12:27)</span> <span class="comment-user userinfo">marwos</span></div></div><span id="6932"></span><div id="comment-6932" class="comment"><div id="post-6932-score" class="comment-score"></div><div class="comment-text"><p>Answers converted to comments in keeping with the style of a "Q&amp;A" site.</p><p>Please see the FAQ for info.</p></div><div id="comment-6932-info" class="comment-info"><span class="comment-age">(17 Oct '11, 13:15)</span> <span class="comment-user userinfo">Bill Meier ♦♦</span></div></div><span id="6933"></span><div id="comment-6933" class="comment"><div id="post-6933-score" class="comment-score"></div><div class="comment-text"><p>Issue with mt version and VC10? zlib1.dll.manifest : general error c1010070: Failed to load and parse the manifest. The system cannot find the file specified. NMAKE : fatal error U1077: '"C:Program FilesMicrosoft SDKsWindowsv7.0Abinmt.exe"' : return code '0x1f' Stop.</p></div><div id="comment-6933-info" class="comment-info"><span class="comment-age">(17 Oct '11, 13:44)</span> <span class="comment-user userinfo">marwos</span></div></div><span id="6934"></span><div id="comment-6934" class="comment"><div id="post-6934-score" class="comment-score"></div><div class="comment-text"><p>it sounds like you need to adjust MSC_VARIANT in config.nmake to indicate that you're using VC10 (VS 2010). The default is VC9 (VS2008).</p><p>Please see http://www.wireshark.org/docs/wsdg_html_chunked/ChSetupWin32.html#ChSetupMSVC</p><p>and follow the instructions therein.</p></div><div id="comment-6934-info" class="comment-info"><span class="comment-age">(17 Oct '11, 14:10)</span> <span class="comment-user userinfo">Bill Meier ♦♦</span></div></div><span id="6935"></span><div id="comment-6935" class="comment not_top_scorer"><div id="post-6935-score" class="comment-score"></div><div class="comment-text"><p>Bill -Thanks!</p></div><div id="comment-6935-info" class="comment-info"><span class="comment-age">(17 Oct '11, 15:00)</span> <span class="comment-user userinfo">marwos</span></div></div><span id="33201"></span><div id="comment-33201" class="comment not_top_scorer"><div id="post-33201-score" class="comment-score"></div><div class="comment-text"><p>what are all your environment variables?</p></div><div id="comment-33201-info" class="comment-info"><span class="comment-age">(30 May '14, 07:38)</span> <span class="comment-user userinfo">aman</span></div></div><span id="33203"></span><div id="comment-33203" class="comment not_top_scorer"><div id="post-33203-score" class="comment-score"></div><div class="comment-text"><p><span>@aman</span>: Just a small hint: This is a <strong>very old</strong> question (Oct '11) and the OP (<span>@marwos</span>) was seen the last time on 14 Sep '12. So, chances are pretty bad, that he/she will ever answer your question.</p><p>In most of the cases it does not make sense to update questions older than a few months, especially if there is a valid answer, like here ;-))</p><p>If you have a similar problem, feel free to ask your own question!</p></div><div id="comment-33203-info" class="comment-info"><span class="comment-age">(30 May '14, 07:43)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-6911" class="comment-tools"><span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a></div><div class="clear"></div><div id="comment-6911-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

