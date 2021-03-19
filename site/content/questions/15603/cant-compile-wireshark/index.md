+++
type = "question"
title = "can&#x27;t compile wireshark"
description = '''I got an error while compiling wireshark. erf.c erf.c(654) : error C2220: warning treated as error - no &#x27;object&#x27; file generated erf.c(654) : warning C4244: &#x27;=&#x27; : conversion from &#x27;gint64&#x27; to &#x27;int&#x27;, possible lo ss of data mp2t.c mp2t.c(121) : error C2220: warning treated as error - no &#x27;object&#x27; file ge...'''
date = "2012-11-06T22:10:00Z"
lastmod = "2012-11-07T22:19:00Z"
weight = 15603
keywords = [ "compile", "error" ]
aliases = [ "/questions/15603" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [can't compile wireshark](/questions/15603/cant-compile-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15603-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15603-score" class="post-score" title="current number of votes">0</div><span id="post-15603-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I got an error while compiling wireshark.</p><p>erf.c erf.c(654) : error C2220: warning treated as error - no 'object' file generated erf.c(654) : warning C4244: '=' : conversion from 'gint64' to 'int', possible lo ss of data mp2t.c mp2t.c(121) : error C2220: warning treated as error - no 'object' file generated</p><p>mp2t.c(121) : warning C4244: '=' : conversion from 'guint64' to 'int', possible loss of data Generating Code... NMAKE : fatal error U1077: 'cl' : return code '0x2' Stop. NMAKE : fatal error U1077: '"C:\Program Files\Microsoft Platform SDK\Bin\nmake.e xe"' : return code '0x2' Stop.</p><p>i find many post on internet and forum i found that it can be avoided by doing</p><p>In the top-level Wireshark directory config.h:</p><h1 id="comment-out-the-following-if-warnings-are-not-to-be-treated-as-errors">Comment out the following if warnings are not to be treated as errors</h1><p>WARNINGS_ARE_ERRORS=-WX</p><p>but in config.h i didn't find this tag.</p><p>Wireshark version - 1.8.3 OS - Windows 7 Visual studio 2005.</p><p>i followed <a href="http://www.codeproject.com/Articles/19426/Creating-Your-Own-Custom-Wireshark-Dissector">http://www.codeproject.com/Articles/19426/Creating-Your-Own-Custom-Wireshark-Dissector</a> link to build the code.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-compile" rel="tag" title="see questions tagged &#39;compile&#39;">compile</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Nov '12, 22:10</strong></p><img src="https://secure.gravatar.com/avatar/9350908b20cf6e624a23a2db7b0fba7f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ishan&#39;s gravatar image" /><p><span>ishan</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ishan has no accepted answers">0%</span></p></div></div><div id="comments-container-15603" class="comments-container"><span id="15654"></span><div id="comment-15654" class="comment"><div id="post-15654-score" class="comment-score"></div><div class="comment-text"><p>WARNINGS_ARE_ERRORS is in config.nmake (for Windows builds). In the release versions (e.g., 1.8.3) then it should already be commented out. So I'm not sure why you're getting "warning treated as error"...</p></div><div id="comment-15654-info" class="comment-info"><span class="comment-age">(07 Nov '12, 10:12)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div></div><div id="comment-tools-15603" class="comment-tools"></div><div class="clear"></div><div id="comment-15603-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="15612"></span>

<div id="answer-container-15612" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15612-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15612-score" class="post-score" title="current number of votes">1</div><span id="post-15612-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The instructions in the link you provided are based on a very old toolchain (VS2005) but look like they should work. I'm not aware of that many people building with VS2005 these days, and you may have more success with a more up to date toolchain, e.g. VS2010 Express.</p><p>The definitive guide to building Wireshark is the <a href="http://www.wireshark.org/docs/wsdg_html_chunked/">Wireshark Developers Guide</a> that is kept current by Wireshark Core Developers. You must follow each step in the Guide to the letter, omitting or varying any steps is likely to lead to build failures.</p><p>Finally, have you made any modifications to the source files before attempting the build (apart from config.nmake)? If so, please try to complete a build with unmodified source files first just to prove your build environment.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Nov '12, 00:19</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-15612" class="comments-container"><span id="15675"></span><div id="comment-15675" class="comment"><div id="post-15675-score" class="comment-score"></div><div class="comment-text"><p>Thanks grahamb ,</p><p>i followed the steps there and i was able to install and build Wireshark.</p><p>Two observation which i want to mention which will help users.</p><ol><li>Their might be issues during installation of Visual studio 2010 , while installing silverlight it might rollback the installation. To avoid that , uninstall the all silverlight version from Add nad remove programs in control pannel and if their are issues during uninstall process of silverlight then go to <a href="http://support.microsoft.com/mats/Program_Install_and_Uninstall/">http://support.microsoft.com/mats/Program_Install_and_Uninstall/</a> and fix the problem by running it.</li><li>It is usual that during installation of visual studio 2010 , after downloading all packages , the setup itself rollback. So don't worry , it is installed on your system and move to next step in installation guide.</li></ol></div><div id="comment-15675-info" class="comment-info"><span class="comment-age">(07 Nov '12, 22:19)</span> <span class="comment-user userinfo">ishan</span></div></div></div><div id="comment-tools-15612" class="comment-tools"></div><div class="clear"></div><div id="comment-15612-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

