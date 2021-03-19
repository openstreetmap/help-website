+++
type = "question"
title = "VS2013:  Unable to start program ... ALL_BUILD Access denied"
description = '''I&#x27;ve managed to successfully build Wireshark using the Visual Studio 2013 Community Edition IDE. It&#x27;s built Wireshark.exe in C:&#92;Development&#92;wireshark&#92;build&#92;run&#92;Debug with C:&#92;Development&#92;wireshark being my Wireshark base directory. I can double click on the exe and all works fine. I then try to run i...'''
date = "2015-11-05T03:59:00Z"
lastmod = "2015-11-05T04:43:00Z"
weight = 47283
keywords = [ "visual-studio" ]
aliases = [ "/questions/47283" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [VS2013: Unable to start program ... ALL\_BUILD Access denied](/questions/47283/vs2013-unable-to-start-program-all_build-access-denied)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47283-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47283-score" class="post-score" title="current number of votes">1</div><span id="post-47283-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>I've managed to successfully build Wireshark using the Visual Studio 2013 Community Edition IDE. It's built Wireshark.exe in C:\Development\wireshark\build\run\Debug with C:\Development\wireshark being my Wireshark base directory. I can double click on the exe and all works fine.</p><p>I then try to run it in VS2013 by clicking on the green arrow here:</p><p><img src="https://osqa-ask.wireshark.org/upfiles/debug.png" alt="alt text" /></p><p>I next get this:</p><p><img src="https://osqa-ask.wireshark.org/upfiles/projects-out-of-date.png" alt="alt text" /></p><p>and I choose Yes to build them. This seems to complete but then I get:</p><p><img src="https://osqa-ask.wireshark.org/upfiles/access_denied.png" alt="alt text" /></p><p>If I try to run again, I get the prompt for the projects out of date and then the same error.</p><p>I've searched around on the web and many people seem to have had this type of problem with other builds but I can't find anything approaching a resolution. In desperation I deleted all of the source and used git clone to download the source again, but I get the same problem.</p><p>So once again I throw myself on your mercy. Any guidance gratefully received.</p><p>Best regards...Paul</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-visual-studio" rel="tag" title="see questions tagged &#39;visual-studio&#39;">visual-studio</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Nov '15, 03:59</strong></p><img src="https://secure.gravatar.com/avatar/2e1b4057f2ff59fe059b23cc6571abaf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PaulOfford&#39;s gravatar image" /><p><span>PaulOfford</span><br />
<span class="score" title="131 reputation points">131</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="32 badges"><span class="silver">●</span><span class="badgecount">32</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PaulOfford has 5 accepted answers">11%</span></p></img></div></div><div id="comments-container-47283" class="comments-container"></div><div id="comment-tools-47283" class="comment-tools"></div><div class="clear"></div><div id="comment-47283-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47284"></span>

<div id="answer-container-47284" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47284-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47284-score" class="post-score" title="current number of votes">4</div><span id="post-47284-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="PaulOfford has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>In the VS Solution Explorer Window, right click "Executables\wireshark" and select ""Set as StartUp Project".</p><p>I do get a warning about androidump not being able to start as it can't find the wiretap DLL, but unless you're intending to use androiddump, that's not an issue for you now, although it is a bug.</p><p>The nice thing about CMake, is that it leaves your source tree untouched, to recover a "broken" build, all you need to do is delete your build directory and then create it again, run CMake and then build. You can also have both x86 and x64 builds (in different directories) at the same time.</p><p>I've no idea why the VS IDE considers the project out of date when built with MSBuild, hopefully allowing VS to compile the build itself will update whatever timestamp magic it needs so that should be a once only issue (until you compile with MSBuild again).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Nov '15, 04:15</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>05 Nov '15, 04:45</strong> </span></p></div></div><div id="comments-container-47284" class="comments-container"><span id="47289"></span><div id="comment-47289" class="comment"><div id="post-47289-score" class="comment-score"></div><div class="comment-text"><p>Thanks Graham - that's flipping excellent.</p></div><div id="comment-47289-info" class="comment-info"><span class="comment-age">(05 Nov '15, 04:43)</span> <span class="comment-user userinfo">PaulOfford</span></div></div></div><div id="comment-tools-47284" class="comment-tools"></div><div class="clear"></div><div id="comment-47284-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

