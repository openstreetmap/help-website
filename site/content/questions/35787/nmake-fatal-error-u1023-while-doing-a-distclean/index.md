+++
type = "question"
title = "Nmake fatal error U1023 while doing a distclean"
description = '''I&#x27;m getting a error (U1023) while executing nmake -f Makefile.nmake distclean. Error code U1023 appears to be a syntax error. Can someone point me in the right direction to fix this? Is there any log I should look at to find out where distclean is failing? I&#x27;m pasting the last few lines of the outpu...'''
date = "2014-08-27T00:30:00Z"
lastmod = "2014-08-27T02:51:00Z"
weight = 35787
keywords = [ "makefile.nmake", "distclean" ]
aliases = [ "/questions/35787" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Nmake fatal error U1023 while doing a distclean](/questions/35787/nmake-fatal-error-u1023-while-doing-a-distclean)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35787-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm getting a error (U1023) while executing nmake -f Makefile.nmake distclean. Error code U1023 appears to be a syntax error. Can someone point me in the right direction to fix this? Is there any log I should look at to find out where distclean is failing? I'm pasting the last few lines of the output here</p><pre><code>        &quot;C:\Program Files\Microsoft Visual Studio 10.0\VC\Bin\nmake.exe&quot; /
             -f Makefile.nmake distclean

Microsoft (R) Program Maintenance Utility Version 10.00.30319.01 Copyright (C) Microsoft Corporation.  All rights reserved.

        rm -rf *.chm                     *.fo                    *.hhc
         *.hhp                   *.pdf                   *.validated  developer-guide.xml  wsdg_chm           wsdg_html.zip       wsdg_html_chunk ed.zip   wsug_chm      wsug_html.zip           wsug_html_chunked.zip  htmlhelp.*      release_notes_chm       release-notes.html      release
-notes.txt       git_version.xml                 user-guide.zip          wsluarm  wsdg_html               wsdg_html_chunked       wsug_html      wsug_ht ml_chunked       wsluarm_src
        cd ../help
        &quot;C:\Program Files\Microsoft Visual Studio 10.0\VC\Bin\nmake.exe&quot; /
             -f Makefile.nmake distclean

Microsoft (R) Program Maintenance Utility Version 10.00.30319.01 Copyright (C) Microsoft Corporation.  All rights reserved.

        rm -rf faq.txt
        cd ../packaging/nsis
        &quot;C:\Program Files\Microsoft Visual Studio 10.0\VC\Bin\nmake.exe&quot; /
             -f Makefile.nmake distclean

Microsoft (R) Program Maintenance Utility Version 10.00.30319.01 Copyright (C) Microsoft Corporation.  All rights reserved.

Makefile.nmake(201) : fatal error U1023: syntax error in expression Stop. NMAKE : fatal error U1077: &#39;&quot;C:\Program Files\Microsoft Visual Studio 10.0\VC\Bi n\nmake.exe&quot;&#39; : return code &#39;0x2&#39; Stop.</code></pre></div><div id="question-tags" class="tags-container tags">makefile.nmake distclean</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Aug '14, 00:30</strong></p><img src="https://secure.gravatar.com/avatar/94048b3e53f1991544b01d988e5b4ee4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="shishir127&#39;s gravatar image" /><p>shishir127<br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="shishir127 has no accepted answers">0%</span></p></div></div><div id="comments-container-35787" class="comments-container"><span id="35790"></span><div id="comment-35790" class="comment"><div id="post-35790-score" class="comment-score"></div><div class="comment-text"><p>Where are your source file from, e.g. git or source package and which branch or version?</p><p>Have you made any changes to the sources?</p></div><div id="comment-35790-info" class="comment-info"><span class="comment-age">(27 Aug '14, 02:50)</span> grahamb ♦</div></div><span id="35792"></span><div id="comment-35792" class="comment"><div id="post-35792-score" class="comment-score"></div><div class="comment-text"><p>I had downloaded the source tarball a few weeks ago because git is blocked. The file name is wireshark-1.12.1rc0-37-gafce994.tar.bz2 if that gives you a clue about the revision.</p></div><div id="comment-35792-info" class="comment-info"><span class="comment-age">(27 Aug '14, 03:31)</span> shishir127</div></div></div><div id="comment-tools-35787" class="comment-tools"></div><div class="clear"></div><div id="comment-35787-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35791"></span>

<div id="answer-container-35791" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35791-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>It appears somethings up with the commands in the distclean target of packaging\nsis\Makefile.nmake which does a simple rm of the built installers and also calls the clean target which rm's some other files.<br />
</p><p>There are a few expressions in the two targets, you can insert simple echo '-$(EXPRESSION)-' statements in those targets to see whats up with them.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Aug '14, 02:51</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span> </br></p></div></div><div id="comments-container-35791" class="comments-container"><span id="35794"></span><div id="comment-35794" class="comment"><div id="post-35794-score" class="comment-score"></div><div class="comment-text"><p>Inserting the echo statements didn't help much because there is a syntax error in including the sources for dftest_LIBS. The syntax error is in the 11th line from the top, "epan\dfilter\dfilter.lib \"</p><p>dftest_LIBS= wiretap\wiretap-$(WTAP_VERSION).lib \</p><pre><code>wsock32.lib user32.lib psapi.lib \

$(GLIB_LIBS) \

wsutil\libwsutil.lib \

$(GNUTLS_LIBS) \</code></pre><p>!IFDEF ENABLE_LIBWIRESHARK</p><pre><code>epan\libwireshark.lib \</code></pre><p>!ELSE epan\dissectors\dissectors.lib \</p><pre><code>epan\wireshark.lib \

epan\dfilter\dfilter.lib \

epan\ftypes\ftypes.lib \

$(C_ARES_LIBS) \

$(ADNS_LIBS) \

$(ZLIB_LIBS) \

$(SMI_LIBS)</code></pre><p>!ENDIF</p></div><div id="comment-35794-info" class="comment-info"><span class="comment-age">(27 Aug '14, 03:55)</span> shishir127</div></div></div><div id="comment-tools-35791" class="comment-tools"></div><div class="clear"></div><div id="comment-35791-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

