+++
type = "question"
title = "Problem packaging wireshark"
description = '''Hi,  I have a problem when i&#x27;m packaging wireshark : nmake -f Makefile.nmake packaging I obtain this error :  e.nmake Microsoft (R) Program Maintenance Utility Version 12.00.21005.1 Copyright (C) Microsoft Corporation. All rights reserved.   if exist ..&#92;..&#92;docbook&#92;user-guide.chm xcopy ..&#92;..&#92;docbook&#92;...'''
date = "2015-09-24T01:15:00Z"
lastmod = "2015-09-25T02:40:00Z"
weight = 46094
keywords = [ "packaging" ]
aliases = [ "/questions/46094" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Problem packaging wireshark](/questions/46094/problem-packaging-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46094-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46094-score" class="post-score" title="current number of votes">0</div><span id="post-46094-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have a problem when i'm packaging wireshark : nmake -f Makefile.nmake packaging</p><p>I obtain this error :</p><p>e.nmake</p><pre><code>Microsoft (R) Program Maintenance Utility Version 12.00.21005.1
Copyright (C) Microsoft Corporation.  All rights reserved.

        if exist ..\..\docbook\user-guide.chm xcopy ..\..\docbook\user-guide.chm
 . /Y /D
        if exist E:\Developpement\Wireshark-win64-libs\user-guide\user-guide.chm
 xcopy E:\Developpement\Wireshark-win64-libs\user-guide\user-guide.chm . /Y /D
0 fichier(s) copié(s)
        rm -f E:\Developpement\wireshark\packaging\nsis\..\..\wireshark-gtk2\uninstall_installer.exe
        &quot;\Program Files (x86)\NSIS\makensis.exe&quot; uninstall.nsi
&#39;\Program&#39; n&#39;est pas reconnu en tant que commande interne ou externe, un programme exécutable ou un fichier de commandes.
NMAKE : fatal error U1077: &#39;&quot;\Program Files (x86)\NSIS\makensis.exe&#39; : return code &#39;0x1&#39;
Stop.
NMAKE : fatal error U1077: &#39;&quot;E:\Visual Studio\VC\BIN\amd64\nmake.exe&quot;&#39; : return code &#39;0x2&#39;
Stop.</code></pre><p>Anybody know how to help me ?</p><p>thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-packaging" rel="tag" title="see questions tagged &#39;packaging&#39;">packaging</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Sep '15, 01:15</strong></p><img src="https://secure.gravatar.com/avatar/5bbfe79da86421b772518d0d96dbb08c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hystreal&#39;s gravatar image" /><p><span>Hystreal</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hystreal has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>24 Sep '15, 01:58</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-46094" class="comments-container"></div><div id="comment-tools-46094" class="comment-tools"></div><div class="clear"></div><div id="comment-46094-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="46097"></span>

<div id="answer-container-46097" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46097-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46097-score" class="post-score" title="current number of votes">1</div><span id="post-46097-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Somethings up with the path to makensis.exe. Do you have NSIS installed? The expected location appears to be <code>"\Program Files (x86)\NSIS\makensis.exe"</code>, which looks a bit odd without a drive letter.</p><p>Check what you have in config.nmake for the variable MAKENSIS?</p><p>Actually looking at the master version of config.nmake, I think there's an opportunity for improvement:</p><pre><code>#
# Optional: Build the NSIS installer.
#
# If NSIS is installed in a standard location (under Program Files
# or Program Files (x86)) you shouldn&#39;t have to change anything.
#
# If NSIS is installed in a custom location uncomment the following
# line and adjust the path accordingly.
#

#MAKENSIS=&quot;\custom\path\to\NSIS\makensis.exe&quot;

# Find NSIS automatically
!IF !DEFINED(MAKENSIS)
!IF EXIST(&quot;$(PROGRAM_FILES)\NSIS\makensis.exe&quot;)
MAKENSIS=&quot;$(PROGRAM_FILES)\NSIS\makensis.exe&quot;
!ELSE IF EXIST(&quot;$(PROGRAM_FILES_W6432)\NSIS\makensis.exe&quot;)
MAKENSIS=&quot;$(PROGRAM_FILES_W6432)\NSIS\makensis.exe&quot;
!ELSE IF EXIST(&quot;\Program Files (x86)\NSIS\makensis.exe&quot;)
MAKENSIS=&quot;\Program Files (x86)\NSIS\makensis.exe&quot;
!ENDIF
!ENDIF</code></pre><p>This code implies that we look for makensis.exe, firstly in the <code>$PROGRAM_FILES\NSIS</code> directory, then in <code>$(PROGRAM_FILES_W6432)\NSIS</code> (which is the same place on my x64 win 7) and then in the hard-coded path <code>\Program Files (x86)\NSIS</code>, which is what you seem to have ended up with.</p><p>The latter part should probably be:</p><pre><code>!ELSE IF EXIST(&quot;$(PROGRAM_FILES_x86))\NSIS\makensis.exe&quot;)
MAKENSIS=&quot;$(PROGRAM_FILES_x86))\NSIS\makensis.exe&quot;</code></pre><p>along with a preceding:</p><pre><code>PROGRAM_FILES_x86 = $(ProgramFiles(x86))</code></pre><p>where the other path variables are defined (<code>PROGRAM_FILES</code> &amp; <code>PROGRAM_FILES</code>).</p><p>Odd that your copy of NSIS seems to have installed a 32 bit version.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Sep '15, 02:16</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-46097" class="comments-container"><span id="46140"></span><div id="comment-46140" class="comment"><div id="post-46140-score" class="comment-score"></div><div class="comment-text"><p>thanks, the problem was here.</p><p>But finally i have directly write my NSIS.exe path because others synthaxes didn't work :/</p></div><div id="comment-46140-info" class="comment-info"><span class="comment-age">(25 Sep '15, 01:39)</span> <span class="comment-user userinfo">Hystreal</span></div></div><span id="46146"></span><div id="comment-46146" class="comment"><div id="post-46146-score" class="comment-score"></div><div class="comment-text"><p>This is being looked at <a href="">here</a>.</p><p>Could you help out by adding the following lines to config.nmake just after the assignment of <code>PROGRAM_FILES_W6432</code>, then run <code>nmake -f Makefile.nmake verify_tools</code> and then report back with the output?</p><pre><code>!message PF is: $(PROGRAM_FILES)
!message PFW6432 is: $(PROGRAM_FILES_W6432)
!error stop here</code></pre><p>You can remove the lines after the test.</p></div><div id="comment-46146-info" class="comment-info"><span class="comment-age">(25 Sep '15, 02:40)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-46097" class="comment-tools"></div><div class="clear"></div><div id="comment-46097-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

