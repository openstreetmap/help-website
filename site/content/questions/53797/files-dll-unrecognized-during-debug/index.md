+++
type = "question"
title = "Files DLL unrecognized during debug"
description = '''Hello everyone, I have a problem for few days, when I would like to debug my Wireshark version. After that Wireshark finish the &quot;Loading module preferences&quot; a message error appear and said that &quot;QT5PrintSupportd.dll&quot; or &quot;wiretap-2.0.4.dll&quot; wasn&#x27;t founded. Neither wireshark.exe nor wireshark-gtk.exe ...'''
date = "2016-07-04T00:33:00Z"
lastmod = "2016-07-05T04:48:00Z"
weight = 53797
keywords = [ "debug", "qtprintsupport", "dll" ]
aliases = [ "/questions/53797" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Files DLL unrecognized during debug](/questions/53797/files-dll-unrecognized-during-debug)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53797-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53797-score" class="post-score" title="current number of votes">0</div><span id="post-53797-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello everyone,</p><p>I have a problem for few days, when I would like to debug my Wireshark version. After that Wireshark finish the "Loading module preferences" a message error appear and said that "QT5PrintSupportd.dll" or "wiretap-2.0.4.dll" wasn't founded. Neither wireshark.exe nor wireshark-gtk.exe work but unfortunately both files exist in the debug folder and if I launch tshark it works perfectly.</p><p>Here is my debug output from visual studio:</p><p><a href="http://pastebin.com/3Z7cUM7N">Wireshark Debug</a></p><p>Best regards,</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-debug" rel="tag" title="see questions tagged &#39;debug&#39;">debug</span> <span class="post-tag tag-link-qtprintsupport" rel="tag" title="see questions tagged &#39;qtprintsupport&#39;">qtprintsupport</span> <span class="post-tag tag-link-dll" rel="tag" title="see questions tagged &#39;dll&#39;">dll</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Jul '16, 00:33</strong></p><img src="https://secure.gravatar.com/avatar/1e089af1440cad240cf3e9651ec1b2fd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stezerow&#39;s gravatar image" /><p><span>stezerow</span><br />
<span class="score" title="6 reputation points">6</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stezerow has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>04 Jul '16, 00:44</strong> </span></p></div></div><div id="comments-container-53797" class="comments-container"><span id="53799"></span><div id="comment-53799" class="comment"><div id="post-53799-score" class="comment-score"></div><div class="comment-text"><p>Do Wireshark.exe or wireshark-gtk.exe work if you run them from the command line?</p></div><div id="comment-53799-info" class="comment-info"><span class="comment-age">(04 Jul '16, 02:39)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="53800"></span><div id="comment-53800" class="comment"><div id="post-53800-score" class="comment-score"></div><div class="comment-text"><p>No they don't work neither with the msbuild command. It's strange because I have already managed to compile them before</p></div><div id="comment-53800-info" class="comment-info"><span class="comment-age">(04 Jul '16, 03:01)</span> <span class="comment-user userinfo">stezerow</span></div></div></div><div id="comment-tools-53797" class="comment-tools"></div><div class="clear"></div><div id="comment-53797-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53801"></span>

<div id="answer-container-53801" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53801-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53801-score" class="post-score" title="current number of votes">0</div><span id="post-53801-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Something's broken in your build. Assuming you're using a CMake build, delete your build directory, create a new one, regenerate the build files with <code>CMake ...</code> and then build again.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Jul '16, 03:04</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-53801" class="comments-container"><span id="53820"></span><div id="comment-53820" class="comment"><div id="post-53820-score" class="comment-score"></div><div class="comment-text"><p>I have used the CMake and build again but the same problem appear. I think the problem comes from the "Loading Prefences" fail and I have founded a solution proposed in <a href="https://ask.wireshark.org/questions/26361/loading-configuration-files">this subject</a>.</p></div><div id="comment-53820-info" class="comment-info"><span class="comment-age">(04 Jul '16, 23:52)</span> <span class="comment-user userinfo">stezerow</span></div></div><span id="53822"></span><div id="comment-53822" class="comment"><div id="post-53822-score" class="comment-score"></div><div class="comment-text"><p>The issues in the related questions all seem to be down to issues with WinPcap, and calls made by dumpcap hanging. This just causes the UI to freeze and doesn't generate error messages about DLL's not being found.</p><p>Are you still getting the messages about DLL's not being found?</p></div><div id="comment-53822-info" class="comment-info"><span class="comment-age">(05 Jul '16, 01:33)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="53826"></span><div id="comment-53826" class="comment"><div id="post-53826-score" class="comment-score"></div><div class="comment-text"><p>I notice that now I can run the .exe generated by the msbuild command. But the DLL messages still appear and they stop the debug</p></div><div id="comment-53826-info" class="comment-info"><span class="comment-age">(05 Jul '16, 02:26)</span> <span class="comment-user userinfo">stezerow</span></div></div><span id="53828"></span><div id="comment-53828" class="comment"><div id="post-53828-score" class="comment-score"></div><div class="comment-text"><p>You're running the exe from the command line or attempting to run in the Visual Studio debugger?</p><p>If the latter, see <a href="https://ask.wireshark.org/questions/53760/visual-studio-unable-to-start-program-and-dlls-not-found">this</a> question.</p></div><div id="comment-53828-info" class="comment-info"><span class="comment-age">(05 Jul '16, 02:49)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="53829"></span><div id="comment-53829" class="comment"><div id="post-53829-score" class="comment-score"></div><div class="comment-text"><p>I'm attempting to run in the Visual Studio debugger. I have tried with your command from the link but it didn't succeed for me</p></div><div id="comment-53829-info" class="comment-info"><span class="comment-age">(05 Jul '16, 04:36)</span> <span class="comment-user userinfo">stezerow</span></div></div><span id="53830"></span><div id="comment-53830" class="comment not_top_scorer"><div id="post-53830-score" class="comment-score"></div><div class="comment-text"><p>When running under the Visual Studio debugger, you must add the full path\to\run\RelWthDebInfo to the shell path before starting Visual Studio <strong>from the same shell</strong>.</p></div><div id="comment-53830-info" class="comment-info"><span class="comment-age">(05 Jul '16, 04:48)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-53801" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-53801-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

