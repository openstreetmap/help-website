+++
type = "question"
title = "NMAKE : fatal error U1077: &#x27;c:&#92;cygwin&#92;bin&#92;bash.EXE&#x27; : return code &#x27;0x1&#x27;  with 1.12.0"
description = '''Hi, When I was running &quot; nmake -f Makefile.nmake setup &quot; at command prompt I am facing error with the unzip. But I think it is taking the unzip from cygwin path only. In the earlier versions this command was working. Your help is valuable. C:&#92;Wireshark_1.12.0&#92;wireshark-1.12.0&amp;gt;nmake -f Makefile.nm...'''
date = "2014-08-01T02:50:00Z"
lastmod = "2014-08-04T06:23:00Z"
weight = 35051
keywords = [ "setup", "nmake" ]
aliases = [ "/questions/35051" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [NMAKE : fatal error U1077: 'c:\\cygwin\\bin\\bash.EXE' : return code '0x1' with 1.12.0](/questions/35051/nmake-fatal-error-u1077-ccygwinbinbashexe-return-code-0x1-with-1120)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35051-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35051-score" class="post-score" title="current number of votes">0</div><span id="post-35051-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>When I was running " nmake -f Makefile.nmake setup " at command prompt I am facing error with the unzip. But I think it is taking the unzip from cygwin path only. In the earlier versions this command was working. Your help is valuable.</p><pre><code>C:\Wireshark_1.12.0\wireshark-1.12.0&gt;nmake -f Makefile.nmake setup

Microsoft (R) Program Maintenance Utility Version 10.00.30319.01
Copyright (C) Microsoft Corporation.  All rights reserved.

ERROR: The contents of &#39;C:\Wireshark-win32-libs-1.12\current_tag.txt&#39; is (unknown).
It should be 2014-06-19.

Can&#39;t find Qt. This will become a problem at some point.
Checking for required applications:
        cl: /cygdrive/c/Program Files/Microsoft Visual Studio 10.0/VC/BIN/cl
        link: /cygdrive/c/Program Files/Microsoft Visual Studio 10.0/VC/BIN/link
        nmake: nmake
        bash: /usr/bin/bash
        bison: /usr/bin/bison
        flex: /usr/bin/flex
        env: /usr/bin/env
        grep: /usr/bin/grep
        /usr/bin/find: /usr/bin/find
        peflags: /usr/bin/peflags
        perl: /usr/bin/perl
        C:\Python27\python.exe: /cygdrive/c/Python27/python.exe
        sed: /usr/bin/sed
        unzip: /usr/bin/unzip
        wget: /usr/bin/wget
        cd &quot;C:\Wireshark-win32-libs-1.12&quot;
        rm -r -f adns-1.0-win32-05ws
        rm -r -f c-ares-1.5.3ws
        rm -r -f c-ares-1.6.0ws
        rm -r -f c-ares-1.7.0-win??ws
        rm -r -f c-ares-1.7.1-win??ws
        rm -r -f c-ares-1.9.1-1-win??ws
        rm -r -f gettext-0.14.5
        rm -r -f gettext-runtime-0.17
        rm -r -f gettext-runtime-0.17-1
        rm -r -f gettext-0.17-1            # win64
        rm -r -f glib
        rm -r -f gnutls-2.8.1-1
        rm -r -f gnutls-2.8.5-*-win??ws
        rm -r -f gnutls-2.10.3-*-win??ws
        rm -r -f gnutls-2.12.18-*-win??ws
        rm -r -f gnutls-3.1.22-*-win??ws
        rm -r -f gtk2
        rm -r -f gtk+
        rm -r -f gtk-wimp
        rm -r -f kfw-2.5
        rm -r -f kfw-3-2-2-final
        rm -r -f kfw-3.2.2-ws1
        rm -r -f kfw-3-2-2-i386-ws-vc6
        rm -r -f libiconv-1.9.1.bin.woe32
        rm -r -f lua5.1
        rm -r -f lua5.1.4
        rm -r -f lua5.2.?
        rm -r -f libsmi-0.4.5
        rm -r -f libsmi-0.4.8
        rm -r -f libsmi-svn-40773-win??ws
        rm -r -f nasm-2.00
        rm -r -f nasm-2.02
        rm -r -f nasm-2.09.08
        rm -r -f pcre-6.4
        rm -r -f pcre-7.0
        rm -r -f portaudio_v19
        rm -r -f portaudio_v19_2
        rm -r -f upx301w
        rm -r -f upx303w
        rm -r -f user-guide
        rm -r -f zlib123
        rm -r -f zlib125
        rm -r -f zlib-1.2.5
        rm -r -f zlib123-dll
        rm -r -f AirPcap_Devpack_1_0_0_594
        rm -r -f AirPcap_Devpack_4_0_0_1480
        rm -r -f AirPcap_Devpack_4_1_0_1622
        rm -r -f GeoIP-1.4.5ws
        rm -r -f GeoIP-1.4.6-win??ws
        rm -r -f GeoIP-1.4.8-win??ws
        rm -r -f GeoIP-1.4.8-*-win??ws
        rm -r -f GeoIP-1.5.1-*-win??ws
        rm -r -f WinSparkle-0.3-44-g2c8d9d3-win??ws
        rm -r -f WpdPack
        cd &quot;C:\Wireshark_1.12.0\wireshark-1.12.0&quot;

****** WinPcap_4_1_3.exe ******
No HTTP proxy specified (http_proxy and HTTP_PROXY are empty).
Downloading WinPcap_4_1_3.exe into &#39;/cygdrive/c/Wireshark-win32-libs-1.12&#39;, installing into .
File `WinPcap_4_1_3.exe&#39; already there; not retrieving.

Extracting &#39;/cygdrive/c/Wireshark-win32-libs-1.12/WinPcap_4_1_3.exe&#39; into &#39;/cygdrive/c/Wireshark-win32-libs-1.12/.&#39;

****** gtk+-bundle_2.24.23-1.1_win32ws.zip ******
No HTTP proxy specified (http_proxy and HTTP_PROXY are empty).
Downloading gtk+-bundle_2.24.23-1.1_win32ws.zip into &#39;/cygdrive/c/Wireshark-win32-libs-1.12&#39;, installing into gtk2
File `gtk+-bundle_2.24.23-1.1_win32ws.zip&#39; already there; not retrieving.

Extracting &#39;/cygdrive/c/Wireshark-win32-libs-1.12/gtk+-bundle_2.24.23-1.1_win32ws.zip&#39; into &#39;/cygdrive/c/Wireshark-win32
-libs-1.12/gtk2&#39;
[/cygdrive/c/Wireshark-win32-libs-1.12/gtk+-bundle_2.24.23-1.1_win32ws.zip]
  End-of-central-directory signature not found.  Either this file is not
  a zipfile, or it constitutes one disk of a multi-part archive.  In the
  latter case the central directory and zipfile comment will be found on
  the last disk(s) of this archive.
unzip:  cannot find zipfile directory in one of /cygdrive/c/Wireshark-win32-libs-1.12/gtk+-bundle_2.24.23-1.1_win32ws.zi
p or
        /cygdrive/c/Wireshark-win32-libs-1.12/gtk+-bundle_2.24.23-1.1_win32ws.zip.zip, and cannot find /cygdrive/c/Wires
hark-win32-libs-1.12/gtk+-bundle_2.24.23-1.1_win32ws.zip.ZIP, period.

ERROR: Couldn&#39;t unpack &#39;/cygdrive/c/Wireshark-win32-libs-1.12/gtk+-bundle_2.24.23-1.1_win32ws.zip&#39;

NMAKE : fatal error U1077: &#39;C:\cygwin\bin\bash.EXE&#39; : return code &#39;0x1&#39;
Stop.</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-setup" rel="tag" title="see questions tagged &#39;setup&#39;">setup</span> <span class="post-tag tag-link-nmake" rel="tag" title="see questions tagged &#39;nmake&#39;">nmake</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Aug '14, 02:50</strong></p><img src="https://secure.gravatar.com/avatar/10646f10c89f6221176215a232f0b0d1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="phaniin&#39;s gravatar image" /><p><span>phaniin</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="phaniin has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>01 Aug '14, 03:08</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-35051" class="comments-container"></div><div id="comment-tools-35051" class="comment-tools"></div><div class="clear"></div><div id="comment-35051-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35052"></span>

<div id="answer-container-35052" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35052-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35052-score" class="post-score" title="current number of votes">1</div><span id="post-35052-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="phaniin has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Looks like your gtk2 bundle zip file is corrupted. Try deleting <code>C:\Wireshark-win32-libs-1.12\gtk+-bundle_2.24.23-1.1_win32ws.zip</code> and then re-running setup.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Aug '14, 03:12</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-35052" class="comments-container"><span id="35053"></span><div id="comment-35053" class="comment"><div id="post-35053-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your answer. I tried that. Result is still the same.</p></div><div id="comment-35053-info" class="comment-info"><span class="comment-age">(01 Aug '14, 04:07)</span> <span class="comment-user userinfo">phaniin</span></div></div><span id="35055"></span><div id="comment-35055" class="comment"><div id="post-35055-score" class="comment-score"></div><div class="comment-text"><p>Works perfectly for me. Can you delete the file again and post the output of the setup run again?</p></div><div id="comment-35055-info" class="comment-info"><span class="comment-age">(01 Aug '14, 05:05)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="35062"></span><div id="comment-35062" class="comment"><div id="post-35062-score" class="comment-score"></div><div class="comment-text"><p><code> Extracting '/cygdrive/c/Wireshark-win32-libs-1.12/WinPcap_4_1_3.exe' into '/cygdrive/c/Wireshark-win32-libs-1.12/.'</code></p><p><code></code></p><p><code>gtk+-bundle_2.24.23-1.1_win32ws.zip  No HTTP proxy specified (http_proxy and HTTP_PROXY are empty). Downloading gtk+-bundle_2.24.23-1.1_win32ws.zip into '/cygdrive/c/Wireshark-win32-libs-1.12', installing into gtk2 --2014-08-01 17:55:51--  http://anonsvn.wireshark.org/wireshark-win32-libs/tags/2014-06-19/packages//gtk+-bundle_2.24.23-1.1_win32ws.zip Resolving anonsvn.wireshark.org (anonsvn.wireshark.org)... 174.137.42.70 Connecting to anonsvn.wireshark.org (anonsvn.wireshark.org)|174.137.42.70|:80... connected. HTTP request sent, awaiting response... 200 OK Length: 1009 [text/html] Saving to: gtk+-bundle_2.24.23-1.1_win32ws.zip'&lt;/p&gt; &lt;p&gt;100%[==========================================================&amp;gt;] 1,009       --.-K/s   in 0s&lt;/p&gt; &lt;p&gt;2014-08-01 17:55:52 (27.5 MB/s) -</code>gtk+-bundle_2.24.23-1.1_win32ws.zip' saved [1009/1009]</code></p><code></code><p>Extracting '/cygdrive/c/Wireshark-win32-libs-1.12/gtk+-bundle_2.24.23-1.1_win32ws.zip' into '/cygdrive/c/Wireshark-win32 -libs-1.12/gtk2' [/cygdrive/c/Wireshark-win32-libs-1.12/gtk+-bundle_2.24.23-1.1_win32ws.zip] End-of-central-directory signature not found. Either this file is not a zipfile, or it constitutes one disk of a multi-part archive. In the latter case the central directory and zipfile comment will be found on the last disk(s) of this archive. unzip: cannot find zipfile directory in one of /cygdrive/c/Wireshark-win32-libs-1.12/gtk+-bundle_2.24.23-1.1_win32ws.zip or /cygdrive/c/Wireshark-win32-libs-1.12/gtk+-bundle_2.24.23-1.1_win32ws.zip.zip, and cannot find /cygdrive/c/Wireshark-win32-libs-1.12/gtk+-bundle_2.24.23-1.1_win32ws.zip.ZIP, period.</p><p>ERROR: Couldn't unpack '/cygdrive/c/Wireshark-win32-libs-1.12/gtk+-bundle_2.24.23-1.1_win32ws.zip'</p></code><p><code>NMAKE : fatal error U1077: 'C:\cygwin\bin\bash.EXE' : return code '0x1' Stop.</code></p></div><div id="comment-35062-info" class="comment-info"><span class="comment-age">(01 Aug '14, 05:42)</span> <span class="comment-user userinfo">phaniin</span></div></div><span id="35063"></span><div id="comment-35063" class="comment"><div id="post-35063-score" class="comment-score">1</div><div class="comment-text"><p>Here's what I got:</p><p><code>  gtk+-bundle_2.24.23-1.1_win32ws.zip  No HTTP proxy specified (http_proxy and HTTP_PROXY are empty). Downloading gtk+-bundle_2.24.23-1.1_win32ws.zip into '/cygdrive/e/Wireshark/Wireshark-win32-libs', installing into gtk2 --2014-08-01 12:19:12--  http://anonsvn.wireshark.org/wireshark-win32-libs/tags/2014-07-27/packages/gtk+-bundle_2.24.23-1.1_win32ws.zip Resolving anonsvn.wireshark.org (anonsvn.wireshark.org)... 174.137.42.70 Connecting to anonsvn.wireshark.org (anonsvn.wireshark.org)|174.137.42.70|:80... connected. HTTP request sent, awaiting response... 200 OK Length: 27843575 (27M) [application/zip] Saving to: 'gtk+-bundle_2.24.23-1.1_win32ws.zip'</code></p><p><code></code></p><p><code>100%[=============================================================&gt;] 27,843,575   253KB/s   in 2m 19s</code></p><code></code><p>2014-08-01 12:21:33 (195 KB/s) - 'gtk+-bundle_2.24.23-1.1_win32ws.zip' saved [27843575/27843575]</p></code><p><code>Extracting '/cygdrive/e/Wireshark/Wireshark-win32-libs/gtk+-bundle_2.24.23-1.1_win32ws.zip' into '/cygdrive/e/Wireshark/Wireshark-win32-libs/gtk2'</code></p><p>Your download looks wrong, you have 1009 bytes instead of 27,843,575</p><p>Note I'm downloading from a different tag directory (I'm building from 'master'). but I did download your tag version via my browser and it was OK.</p><p>Maybe you have an upstream caching proxy? Try downloading the file manually via your browser and putting the file in the expected place.</p></div><div id="comment-35063-info" class="comment-info"><span class="comment-age">(01 Aug '14, 06:18)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="35064"></span><div id="comment-35064" class="comment"><div id="post-35064-score" class="comment-score">1</div><div class="comment-text"><p>Are you able to manually download the file by following this link: <span>htt://anonsvn.wireshark.org/wireshark-win32-libs/tags/2014-06-19/packages//gtk+-bundle_2.24.23-1.1_win32ws.zip</span></p><p>If yes, can you unzip it?</p></div><div id="comment-35064-info" class="comment-info"><span class="comment-age">(01 Aug '14, 06:18)</span> <span class="comment-user userinfo">Pascal Quantin</span></div></div><span id="35065"></span><div id="comment-35065" class="comment not_top_scorer"><div id="post-35065-score" class="comment-score"></div><div class="comment-text"><p>Looks like you have some proxy interfering. When I'm downloading the gtk bundle, I get:</p><pre><code>****** gtk+-bundle_2.24.23-1.1_win32ws.zip ******
No HTTP proxy specified (http_proxy and HTTP_PROXY are empty).
Downloading gtk+-bundle_2.24.23-1.1_win32ws.zip into &#39;/cygdrive/d/dev/Wireshark-
win32-libs-1.12&#39;, installing into gtk2
--2014-08-01 15:21:15--  http://anonsvn.wireshark.org/wireshark-win32-libs/tags/2014-06-19/packages//gtk+-bundle_2.24.23-1.1_win32ws.zip
Resolving anonsvn.wireshark.org (anonsvn.wireshark.org)... 174.137.42.70
Connecting to anonsvn.wireshark.org (anonsvn.wireshark.org)|174.137.42.70|:80...
 connected.
HTTP request sent, awaiting response... 200 OK
Length: 27843575 (27M) [application/zip]
Saving to: `gtk+-bundle_2.24.23-1.1_win32ws.zip&#39;</code></pre><p>=&gt; the reported length is 27843575 bytes [application/zip] while you get 1009 [text/html]</p></div><div id="comment-35065-info" class="comment-info"><span class="comment-age">(01 Aug '14, 06:23)</span> <span class="comment-user userinfo">Pascal Quantin</span></div></div><span id="35067"></span><div id="comment-35067" class="comment not_top_scorer"><div id="post-35067-score" class="comment-score"></div><div class="comment-text"><p>Thanks to both of you( Graham Bloice and Pascal Quantin ).Will check tomorrow once I go to office.</p></div><div id="comment-35067-info" class="comment-info"><span class="comment-age">(01 Aug '14, 07:49)</span> <span class="comment-user userinfo">phaniin</span></div></div><span id="35154"></span><div id="comment-35154" class="comment not_top_scorer"><div id="post-35154-score" class="comment-score"></div><div class="comment-text"><p>As you said, it is the problem with file download only. I tried to download manually from this link. <a href="http://anonsvn.wireshark.org/wireshark-win32-libs/tags/2014-06-19/packages//gtk+-bundle_2.24.23-1.1_win32ws.zip">http://anonsvn.wireshark.org/wireshark-win32-libs/tags/2014-06-19/packages//gtk+-bundle_2.24.23-1.1_win32ws.zip</a> But unable to download. It seems there is a limit on the size of download in our office and some proxy issues also affecting the download.</p><p>Then I copied the file manually to the corresponding folder and now every thing works. Thanks a lot to both of you(Graham Bloice and Pascal Quantin).</p></div><div id="comment-35154-info" class="comment-info"><span class="comment-age">(04 Aug '14, 06:11)</span> <span class="comment-user userinfo">phaniin</span></div></div><span id="35155"></span><div id="comment-35155" class="comment not_top_scorer"><div id="post-35155-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-35155-info" class="comment-info"><span class="comment-age">(04 Aug '14, 06:23)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-35052" class="comment-tools"><span class="comments-showing"> showing 5 of 9 </span> <a href="#" class="show-all-comments-link">show 4 more comments</a></div><div class="clear"></div><div id="comment-35052-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

