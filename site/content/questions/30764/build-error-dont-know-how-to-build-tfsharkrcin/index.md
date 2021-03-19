+++
type = "question"
title = "Build Error : &quot;don&#x27;t know how to build tfshark.rc.in&quot;"
description = '''Hello, I try to build wireshark with the bins. Every time i try to make : nmake -f Makefile.nmake all  I get :  Microsoft (R) Program Maintenance Utility Version 10.00.30319.01  Copyright (C) Microsoft Corporation. All rights reserved.  Can&#x27;t find Qt. This will become a problem at some point.  cd to...'''
date = "2014-03-13T06:38:00Z"
lastmod = "2014-03-13T13:30:00Z"
weight = 30764
keywords = [ "build_error", "tfshark.rc.in", "tfshark" ]
aliases = [ "/questions/30764" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Build Error : "don't know how to build tfshark.rc.in"](/questions/30764/build-error-dont-know-how-to-build-tfsharkrcin)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30764-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30764-score" class="post-score" title="current number of votes">0</div><span id="post-30764-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I try to build wireshark with the bins. Every time i try to make :</p><pre><code>nmake -f Makefile.nmake all</code></pre><p>I get :</p><pre><code>    Microsoft (R) Program Maintenance Utility Version 10.00.30319.01
    Copyright (C) Microsoft Corporation.  All rights reserved.
    Can&#39;t find Qt. This will become a problem at some point.
        cd tools
        &quot;C:\Program Files (x86)\Microsoft Visual Studio 10.0\VC\BIN\nmake.exe&quot; /
                   -f Makefile.nmake

    Microsoft (R) Program Maintenance Utility Version 10.00.30319.01
    Copyright (C) Microsoft Corporation.  All rights reserved.

        cd lemon
        ..\native-nmake &quot;C:\Program Files (x86)\Microsoft Visual Studio 10.0\VC\
   BIN\nmake.exe&quot; /                   -f Makefile.nmake
   Setting environment for using Microsoft Visual Studio 2010 x86 tools.

Microsoft (R) Program Maintenance Utility Version 10.00.30319.01
Copyright (C) Microsoft Corporation.  All rights reserved.

        cd ..
        cd ..
        cd image
        &quot;C:\Program Files (x86)\Microsoft Visual Studio 10.0\VC\BIN\nmake.exe&quot; /
                   -f Makefile.nmake

     Microsoft (R) Program Maintenance Utility Version 10.00.30319.01
     Copyright (C) Microsoft Corporation.  All rights reserved.

     NMAKE : fatal error U1073: don&#39;t know how to make &#39;tfshark.rc.in&#39;
     Stop.
     NMAKE : fatal error U1077: &#39;&quot;C:\Program Files (x86)\Microsoft Visual Studio 10.0
     \VC\BIN\nmake.exe&quot;&#39; : return code &#39;0x2&#39;
     Stop.</code></pre><p>I don't know the Problem. I have try many things try to build a 32bit and a 64 bit and many athor things. The Problem is every time the same.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-build_error" rel="tag" title="see questions tagged &#39;build_error&#39;">build_error</span> <span class="post-tag tag-link-tfshark.rc.in" rel="tag" title="see questions tagged &#39;tfshark.rc.in&#39;">tfshark.rc.in</span> <span class="post-tag tag-link-tfshark" rel="tag" title="see questions tagged &#39;tfshark&#39;">tfshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Mar '14, 06:38</strong></p><img src="https://secure.gravatar.com/avatar/3378e4af34b02834b98e8a896efe303c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Alias_alias&#39;s gravatar image" /><p><span>Alias_alias</span><br />
<span class="score" title="21 reputation points">21</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Alias_alias has no accepted answers">0%</span></p></div></div><div id="comments-container-30764" class="comments-container"><span id="30765"></span><div id="comment-30765" class="comment"><div id="post-30765-score" class="comment-score"></div><div class="comment-text"><p>Are you building from the latest hit version?</p></div><div id="comment-30765-info" class="comment-info"><span class="comment-age">(13 Mar '14, 06:45)</span> <span class="comment-user userinfo">Anders ♦</span></div></div></div><div id="comment-tools-30764" class="comment-tools"></div><div class="clear"></div><div id="comment-30764-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="30778"></span>

<div id="answer-container-30778" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30778-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30778-score" class="post-score" title="current number of votes">1</div><span id="post-30778-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Alias_alias has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>tfshark.rc.in was not part of Makefile.am. It should be fixed in v1.11.3-rc1-1950-gf3f77bd. Please update your tar.bz2 copy.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Mar '14, 13:30</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-30778" class="comments-container"></div><div id="comment-tools-30778" class="comment-tools"></div><div class="clear"></div><div id="comment-30778-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

