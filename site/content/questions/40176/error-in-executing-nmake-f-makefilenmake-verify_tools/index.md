+++
type = "question"
title = "[closed] Error in Executing nmake -f Makefile.nmake verify_tools"
description = '''C:&#92;Workplace&#92;Development&#92;wireshark-1.99.2&amp;gt;nmake -f Makefile.nmake verify_tools  Microsoft (R) Program Maintenance Utility Version 1.50 Copyright (c) Microsoft Corp 1988-94. All rights reserved.  ERROR: The contents of &#x27;C:&#92;Workplace&#92;Development&#92;Wireshark-win32-libs&#92;current_tag.txt&#x27; is (unknown). I...'''
date = "2015-03-02T03:47:00Z"
lastmod = "2015-03-02T04:23:00Z"
weight = 40176
keywords = [ "build_error", "wireshark" ]
aliases = [ "/questions/40176" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] Error in Executing nmake -f Makefile.nmake verify\_tools](/questions/40176/error-in-executing-nmake-f-makefilenmake-verify_tools)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40176-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40176-score" class="post-score" title="current number of votes">0</div><span id="post-40176-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><pre><code>C:\Workplace\Development\wireshark-1.99.2&gt;nmake -f Makefile.nmake verify_tools

Microsoft (R) Program Maintenance Utility   Version 1.50
Copyright (c) Microsoft Corp 1988-94. All rights reserved.

ERROR: The contents of &#39;C:\Workplace\Development\Wireshark-win32-libs\current_tag.txt&#39; is (unknown).
It should be 2014-10-01.

Checking for required applications:
        cl: /cygdrive/c/Program Files/Microsoft Visual Studio 9.0/VC/bin/cl
        link: /usr/bin/link
        nmake: nmake
        bash: /usr/bin/bash
        env: /usr/bin/env
        grep: /usr/bin/grep
        /usr/bin/find: /usr/bin/find
        peflags: /usr/bin/peflags
        perl: /usr/bin/perl
        python: /usr/bin/python
        C:\Qt\4.8\vs2008\bin\qmake: /cygdrive/c/Qt/4.8/vs2008/bin/qmake
        sed: /usr/bin/sed
        unzip: /usr/bin/unzip
        wget: /usr/bin/wget

Can&#39;t find:  C:\Documents and Settings\All Users\Application Data\chocolatey\lib\winflexbison.2.4.3.20140715\tools C:\Documents and Settings\All Users\Application Data\chocolatey\lib\winflexbison.2.4.3.20140715\tools

ERROR: These application(s) are either not installed or simply can&#39;t be found in the current PATH: /usr/bin:/cygdrive/c/WINDOWS/system32:/cygdrive/c/WINDOWS:/cygdrive/c/Python27:/cygdrive/c/Program Files/Microsoft Visual Studio 9.0/VC/bin:/cygdrive/c/Program Files/Microsoft Visual Studio 9.0/Common7/Tools:/cygdrive/c/Program Files/Microsoft Visual Studio 9.0/VC/vcpackages:/cygdrive/c/Program Files/Microsoft SDKs/Windows/v6.0A/bin:/cygdrive/c/WINDOWS/system32:/cygdrive/c/WINDOWS:/cygdrive/c/WINDOWS/system32/wbem:/cygdrive/c/Program Files/Microsoft SQL Server/90/Tools/Binn:/cygdrive/c/WINDOWS/system32/WindowsPowerShell/v1.0:/cygdrive/c/Program Files/TortoiseSVN/bin:/cygdrive/c/Program Files/Microsoft SDKs/Windows/v7.0A/Include:/cygdrive/c/Qt/5.4/mingw491_32/mkspecs/win32-msvc2008:/cygdrive/c/Documents and Settings/All Users/Application Data/chocolatey/bin:/cygdrive/c/Program Files/NSIS:/cygdrive/c/tools/cygwin:/cygdrive/c/Program Files/Microsoft Visual Studio 9.0/VC/bin/x86_amd64:/cygdrive/c/Program Files/HTML Help Workshop:/usr/bin:/cygdrive/c/Workplace/Development/Wireshark-win32-libs/gtk2/bin:/cygdrive/c/bin:/cygdrive/c/Workplace/Development/Wireshark-win32-libs/zlib125.</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-build_error" rel="tag" title="see questions tagged &#39;build_error&#39;">build_error</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Mar '15, 03:47</strong></p><img src="https://secure.gravatar.com/avatar/302a32bb6a6f237c61731914f3657167?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dhruv%20Gupta&#39;s gravatar image" /><p><span>Dhruv Gupta</span><br />
<span class="score" title="6 reputation points">6</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dhruv Gupta has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> closed <strong>02 Mar '15, 04:24</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-40176" class="comments-container"><span id="40179"></span><div id="comment-40179" class="comment"><div id="post-40179-score" class="comment-score"></div><div class="comment-text"><p>Have you actually read the feedback given from verify_tools? Have you followed the developer guide <strong>to the letter</strong>?</p></div><div id="comment-40179-info" class="comment-info"><span class="comment-age">(02 Mar '15, 04:00)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-40176" class="comment-tools"></div><div class="clear"></div><div id="comment-40176-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Duplicate Question" by grahamb 02 Mar '15, 04:24

</div>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="40182"></span>

<div id="answer-container-40182" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40182-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40182-score" class="post-score" title="current number of votes">0</div><span id="post-40182-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The "ERROR" about the missing current_tag.txt can be expected if you have not yet run the "setup" step.</p><p>However, before you do that you must fix your environment as discussed on your <a href="https://ask.wireshark.org/questions/40092/nmake-fatal-error-u1073">other</a> question.</p><p>As this question is mostly irrelevant, I'll close it and ask you to continue by responding to the questions I asked in your other question</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Mar '15, 04:23</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-40182" class="comments-container"></div><div id="comment-tools-40182" class="comment-tools"></div><div class="clear"></div><div id="comment-40182-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

