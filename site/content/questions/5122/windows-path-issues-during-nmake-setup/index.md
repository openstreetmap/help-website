+++
type = "question"
title = "Windows path issues during nmake setup"
description = '''I seem to be having issues with the POSIX paths that have been implemented in Wireshark 1.6.1. I&#x27;m on a Windows XP Pro box. During the setup, the file is being downloaded. I can clearly see it, but I cannot see it through the cygdrive path. If I run the unzip program using the cygdrive path, I get t...'''
date = "2011-07-19T06:58:00Z"
lastmod = "2011-07-21T03:55:00Z"
weight = 5122
keywords = [ "windows", "xp", "posix" ]
aliases = [ "/questions/5122" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Windows path issues during nmake setup](/questions/5122/windows-path-issues-during-nmake-setup)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5122-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I seem to be having issues with the POSIX paths that have been implemented in Wireshark 1.6.1. I'm on a Windows XP Pro box.</p><p>During the setup, the file is being downloaded. I can clearly see it, but I cannot see it through the cygdrive path. If I run the unzip program using the cygdrive path, I get the same error, but if I go the the libs folder and run the unzip program, it unzips fine. So what am I missing here?</p><p>Here is the command output:</p><pre><code>C:\wireshark-1.6.1&gt;nmake -f Makefile.nmake setup

Microsoft (R) Program Maintenance Utility Version 9.00.21022.08
Copyright (C) Microsoft Corporation.  All rights reserved.

ERROR: The contents of C:\wireshark-win32-libs-1.6\current_tag.txt is (unknown).

It should be 2011-05-19.

Checking for required applications:
        cl: /cygdrive/c/Program Files/Microsoft Visual Studio 9.0/VC/BIN/cl
        link: /cygdrive/c/Program Files/Microsoft Visual Studio 9.0/VC/BIN/link

        nmake: /cygdrive/c/Program Files/Microsoft Visual Studio 9.0/VC/BIN/nmak
e
        mt: /cygdrive/c/Program Files/Microsoft SDKs/Windows/v6.0A/bin/mt
        bash: /usr/bin/bash
        bison: /usr/bin/bison
        flex: /usr/bin/flex
        env: /usr/bin/env
        grep: /cygdrive/c/Program Files/Borland/Delphi7/Bin/grep
        /usr/bin/find: /usr/bin/find
        perl: /usr/bin/perl
        C:\Python27\python.exe: /cygdrive/c/Python27/python.exe
        sed: /usr/bin/sed
        unzip: /cygdrive/c/oracle/product/10.2.0/client_1/bin/unzip
        wget: /usr/bin/wget
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
        cd &quot;C:\wireshark-1.6.1&quot;

****** gtk+-bundle_2.22.1-20101227_win32.zip ******
No HTTP proxy specified (http_proxy and HTTP_PROXY are empty).
Downloading gtk+-bundle_2.22.1-20101227_win32.zip into /cygdrive/c/wireshark-win
32-libs-1.6, installing into gtk2
--2011-07-19 09:50:46--  http://anonsvn.wireshark.org/wireshark-win32-libs/tags/
2011-05-19/packages//gtk+-bundle_2.22.1-20101227_win32.zip
Resolving anonsvn.wireshark.org (anonsvn.wireshark.org)... 69.4.231.53
Connecting to anonsvn.wireshark.org (anonsvn.wireshark.org)|69.4.231.53|:80... c
onnected.
HTTP request sent, awaiting response... 200 OK
Length: 24516284 (23M) [application/octet-stream]
Saving to: `gtk+-bundle_2.22.1-20101227_win32.zip&#39;

100%[======================================&gt;] 24,516,284  1.20M/s   in 29s

2011-07-19 09:51:15 (816 KB/s) - `gtk+-bundle_2.22.1-20101227_win32.zip&#39; saved [
24516284/24516284]

Extracting /cygdrive/c/wireshark-win32-libs-1.6/gtk+-bundle_2.22.1-20101227_win3
2.zip into /cygdrive/c/wireshark-win32-libs-1.6/gtk2
unzip:  cannot find either /cygdrive/c/wireshark-win32-libs-1.6/gtk+-bundle_2.22
.1-20101227_win32.zip or /cygdrive/c/wireshark-win32-libs-1.6/gtk+-bundle_2.22.1
-20101227_win32.zip.zip.

ERROR: Couldn&#39;t unpack /cygdrive/c/wireshark-win32-libs-1.6/gtk+-bundle_2.22.1-2
0101227_win32.zip

NMAKE : fatal error U1077: &#39;d:\cygwin\bin\bash.EXE&#39; : return code &#39;0x1&#39;
Stop.

C:\wireshark-1.6.1&gt;</code></pre></div><div id="question-tags" class="tags-container tags">windows xp posix</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Jul '11, 06:58</strong></p><img src="https://secure.gravatar.com/avatar/64d3e7cc29f59f89292957675d95d3c1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="geckofx&#39;s gravatar image" /><p>geckofx<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="geckofx has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 27 Feb '13, 20:31</p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-5122" class="comments-container"></div><div id="comment-tools-5122" class="comment-tools"></div><div class="clear"></div><div id="comment-5122-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="5124"></span>

<div id="answer-container-5124" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5124-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Don't run the build in a bash shell, use the Windows cmd shell.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Jul '11, 07:20</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-5124" class="comments-container"><span id="5133"></span><div id="comment-5133" class="comment"><div id="post-5133-score" class="comment-score"></div><div class="comment-text"><p>I am running it in a cmd shell. This same exact process works perfectly for 1.4.x</p></div><div id="comment-5133-info" class="comment-info"><span class="comment-age">(19 Jul '11, 10:51)</span> geckofx</div></div></div><div id="comment-tools-5124" class="comment-tools"></div><div class="clear"></div><div id="comment-5124-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="5153"></span>

<div id="answer-container-5153" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5153-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I'd have a look at what's in your path. From the mass of output (we don't really need to the output from distclean) the bit that verifies your environment set up shows the following:</p><pre><code>...
grep: /cygdrive/c/Program Files/Borland/Delphi7/Bin/grep
...
unzip: /cygdrive/c/oracle/product/10.2.0/client_1/bin/unzip</code></pre><p>I think you need to fix this, particularly the unzip and things might work a bit better.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Jul '11, 03:55</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-5153" class="comments-container"><span id="18952"></span><div id="comment-18952" class="comment"><div id="post-18952-score" class="comment-score"></div><div class="comment-text"><p>Hi, I was getting the same error since last week. Thanks grahamb for drawing attention. :)</p></div><div id="comment-18952-info" class="comment-info"><span class="comment-age">(27 Feb '13, 19:54)</span> ankurjain</div></div></div><div id="comment-tools-5153" class="comment-tools"></div><div class="clear"></div><div id="comment-5153-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

