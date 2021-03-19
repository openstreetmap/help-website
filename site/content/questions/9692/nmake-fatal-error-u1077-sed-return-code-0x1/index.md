+++
type = "question"
title = "NMAKE : fatal error U1077: &#x27;sed&#x27; : return code &#x27;0x1&#x27;"
description = '''When trying to build Wireshark I get NMAKE : fatal error U1077: &#x27;sed&#x27; : return code &#x27;0x1&#x27; Or to be more precise I get : c:&#92;wireshark&amp;gt;nmake -f Makefile.nmake all Microsoft (R) Program Maintenance Utility Version 9.00.30729.01 Copyright (C) Microsoft Corporation. All rights reserved. sed -e s/@VERS...'''
date = "2012-03-22T03:39:00Z"
lastmod = "2012-03-22T04:24:00Z"
weight = 9692
keywords = [ "nmake" ]
aliases = [ "/questions/9692" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [NMAKE : fatal error U1077: 'sed' : return code '0x1'](/questions/9692/nmake-fatal-error-u1077-sed-return-code-0x1)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9692-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When trying to build Wireshark I get NMAKE : fatal error U1077: 'sed' : return code '0x1'</p><p>Or to be more precise I get :</p><p>c:\wireshark&gt;nmake -f Makefile.nmake all</p><p>Microsoft (R) Program Maintenance Utility Version 9.00.30729.01 Copyright (C) Microsoft Corporation. All rights reserved.</p><pre><code>sed -e s/@[email protected]/1.7.1-Hg on the test patrol-/  -e &quot;s/@[email protected]/#define HAVE_C_ARES 1/&quot;  -e &quot;s/@[email protected]//&quot;  -e &quot;s/@[email protected]/#define HAVE_MIT_KERBEROS 1/&quot;  -e &quot;s/@[email protected]//&quot;  -e &quot;s/@[email protected]/#define HAVE_LIBZ 1/&quot;  -e &quot;s/@[email protected]/#define HAVE_LIBPCAP 1/&quot;  -e s/@[email protected]/#define HAVE_PCAP_FINDALLDEVS 1/&quot;  -e &quot;s/@[email protected]/#define HAVE_PCAP_DATALINK_NAME_TO_VAL 1/&quot;  -e s/@[email protected]/#define HAVE_PCAP_DATALINK_VAL_TO_NAME 1/&quot;  -e &quot;s/@[email protected]/#define HAVE_PCAP_DATALINK_VAL_TO_DESCRIPTION 1/&quot;  -e &quot;s/@[email protected]//&quot;  -e &quot;s/@[email protected]/#define HAVE_REMOTE 1/&quot;  -e &quot;s/@[email protected]/#define HAVE_PCAP_REMOTE 1/&quot;  -e &quot;s/@[email protected]/#define HAVE_PCAP_OPEN 1/&quot;-e &quot;s/@[email protected]/#define HAVE_PCAP_OPEN_DEAD 1/&quot;  -e &quot;s/@[email protected]/#define HAVE_PCAP_LIST_DATALINKS 1/&quot;  -e &quot;s/@[email protected]/#define HAVE_PCAP_FREE_DATALINKS 1/&quot;  -e &quot;s/@[email protected]/#define HAVE_PCAP_SET_DATALINK 1/&quot;  -e &quot;s/@[email protected]/#define HAVE_PCAP_SETSAMPLING 1/&quot;  -e &quot;s/@[email protected]/#define HAVE_BPF_IMAGE 1/&quot;  -e &quot;s/@[email protected]/#define HAVE_LIBWIRESHARKDLL 1/&quot;  -e &quot;s/@[email protected]/#define HAVE_LIBGNUTLS 1/&quot;  -e &quot;s/@[email protected]/#define HAVE_LIBGCRYPT 1/&quot;  -e &quot;s/@[email protected]/#define HAVE_LUA 1/&quot;  -e &quot;s/@[email protected]/#define HAVE_LUA_5_1 1/&quot;  -e&quot;s/@[email protected]//&quot;  -e &quot;s/@[email protected]/#define HAVE_AIRPCAP 1/&quot;  -e &quot;s/@[email protected]//&quot;  -e &quot;s/@[email protected]/#define HAVE_LIBPORTAUDIO 1/&quot;  -e &quot;s/@[email protected]//&quot;  -e &quot;s/@[email protected]/#define HAVE_LIBSMI 1/&quot;  -e &quot;s/@[email protected]/#define HAVE_GEOIP 1/&quot;  -e s/@[email protected]/#define HAVE_GEOIP_V6 1/&quot;  -e &quot;s/@[email protected]/#define INET6 1/&quot;  -e &quot;s/@[email protected]/#define HAVE_NTDDNDIS_H 1/&quot;  -e &quot;s/@[email protected]/#define PCAP_NG_DEFAULT 1/&quot;  -e &quot;s/@[email protected]//&quot;  &lt; config.h.win32 &gt; config.h
sed: -e expression #1, char 20: unterminated `s&#39; command
NMAKE : fatal error U1077: &#39;sed&#39; : return code &#39;0x1&#39;
Stop.</code></pre><p>When running verifying tools I get:</p><p>c:\wireshark&gt;nmake -f Makefile.nmake verify_tools</p><p>Microsoft (R) Program Maintenance Utility Version 9.00.30729.01 Copyright (C) Microsoft Corporation. All rights reserved.</p><p>Checking for required applications:</p><pre><code>    cl: /cygdrive/c/Program Files/Microsoft Visual Studio 9.0/VC/BIN/cl
    link: /cygdrive/c/Program Files/Microsoft Visual Studio 9.0/VC/BIN/link
    nmake: /cygdrive/c/Program Files/Microsoft Visual Studio 9.0/VC/BIN/nmake
    mt: /cygdrive/c/Program Files/Microsoft SDKs/Windows/v6.0A/bin/mt
    bash: /usr/bin/bash
    bison: /usr/bin/bison
    flex: /usr/bin/flex
    env: /usr/bin/env
    grep: /usr/bin/grep
    /usr/bin/find: /usr/bin/find
    peflags: /usr/bin/peflags
    perl: /usr/bin/perl
    C:\\Python27\\python.exe: /cygdrive/c/Python27/python.exe
    sed: /usr/bin/sed
    unzip: /usr/bin/unzip
    wget: /usr/bin/wget</code></pre><p>I've reinstalled sed with Cygwin and it hasn't helped. I've tried the solution from <a href="http://ask.wireshark.org/questions/7991/nmake-fatal-error-u1077-sed-return-code-0x1">http://ask.wireshark.org/questions/7991/nmake-fatal-error-u1077-sed-return-code-0x1</a> and no difference.</p><p>Now I don't know what to try, any tips?</p></div><div id="question-tags" class="tags-container tags">nmake</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Mar '12, 03:39</strong></p><img src="https://secure.gravatar.com/avatar/47af2847d3c2019abf1673046f57cc8f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hans-J%C3%B6rgen%20Gunnarsson&#39;s gravatar image" /><p>Hans-Jörgen ...<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hans-Jörgen Gunnarsson has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 22 Mar '12, 04:23</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-9692" class="comments-container"></div><div id="comment-tools-9692" class="comment-tools"></div><div class="clear"></div><div id="comment-9692-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9694"></span>

<div id="answer-container-9694" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9694-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Totally a guess, but looking at the error message, probably something to do with your version string? You have a version string of "1.7.1-Hg on the test patrol-". Try making it something simpler.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Mar '12, 04:24</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-9694" class="comments-container"><span id="9695"></span><div id="comment-9695" class="comment"><div id="post-9695-score" class="comment-score"></div><div class="comment-text"><p>Good guess, problem solved. Thanks.</p></div><div id="comment-9695-info" class="comment-info"><span class="comment-age">(22 Mar '12, 04:41)</span> Hans-Jörgen ...</div></div><span id="9696"></span><div id="comment-9696" class="comment"><div id="post-9696-score" class="comment-score"></div><div class="comment-text"><p>Glad to be of assistance, can you please accept the answer?</p></div><div id="comment-9696-info" class="comment-info"><span class="comment-age">(22 Mar '12, 04:49)</span> grahamb ♦</div></div><span id="27233"></span><div id="comment-27233" class="comment"><div id="post-27233-score" class="comment-score"></div><div class="comment-text"><p>I accepted the answer, as it solved the problem.</p></div><div id="comment-27233-info" class="comment-info"><span class="comment-age">(21 Nov '13, 07:32)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-9694" class="comment-tools"></div><div class="clear"></div><div id="comment-9694-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

