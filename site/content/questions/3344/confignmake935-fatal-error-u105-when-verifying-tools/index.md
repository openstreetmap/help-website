+++
type = "question"
title = "config.nmake(935) : fatal error U105 when verifying tools"
description = '''Hi all, I am trying to enhance wireshark for a protocol for a properitary information. I have installed everything according to developer guide and trying to verify tools. I am getting an error  config.nmake(935) : fatal error U1050: Can&#x27;t find C:wireshark-win32-libsvcredi st_x86.exe. Have you downl...'''
date = "2011-04-05T07:37:00Z"
lastmod = "2011-04-06T08:10:00Z"
weight = 3344
keywords = [ "configuration", "error" ]
aliases = [ "/questions/3344" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [config.nmake(935) : fatal error U105 when verifying tools](/questions/3344/confignmake935-fatal-error-u105-when-verifying-tools)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3344-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3344-score" class="post-score" title="current number of votes">0</div><span id="post-3344-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>I am trying to enhance wireshark for a protocol for a properitary information. I have installed everything according to developer guide and trying to verify tools.</p><p>I am getting an error config.nmake(935) : fatal error U1050: Can't find C:wireshark-win32-libsvcredi st_x86.exe. Have you downloaded it from Microsoft? See the developer's guide sec tion "C-Runtime "Redistributable" files" for details how to get it Stop.</p><p>I have installed redistributable vcredist_x86.exe SP1. What can be problem with this?</p><p>Any help will be appreciated.</p><p>Regards, D.A.Pandharkar</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-configuration" rel="tag" title="see questions tagged &#39;configuration&#39;">configuration</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Apr '11, 07:37</strong></p><img src="https://secure.gravatar.com/avatar/c33cba1d3fea69f74f6c8c0425c16c75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dsprabhu4&#39;s gravatar image" /><p><span>dsprabhu4</span><br />
<span class="score" title="11 reputation points">11</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dsprabhu4 has no accepted answers">0%</span></p></div></div><div id="comments-container-3344" class="comments-container"><span id="3346"></span><div id="comment-3346" class="comment"><div id="post-3346-score" class="comment-score"></div><div class="comment-text"><p>Is vcredist_x86.exe still in your C:\wireshark-win32-libs\ folder?</p></div><div id="comment-3346-info" class="comment-info"><span class="comment-age">(05 Apr '11, 09:10)</span> <span class="comment-user userinfo">multipleinte...</span></div></div><span id="3353"></span><div id="comment-3353" class="comment"><div id="post-3353-score" class="comment-score"></div><div class="comment-text"><p>Hi, this may be a very silly question but do i have to compile for making this wireshark-win32-libs folder?? I am trying to verify tools first so have not build code.</p></div><div id="comment-3353-info" class="comment-info"><span class="comment-age">(05 Apr '11, 13:14)</span> <span class="comment-user userinfo">dsprabhu4</span></div></div><span id="3354"></span><div id="comment-3354" class="comment"><div id="post-3354-score" class="comment-score"></div><div class="comment-text"><p>So long as your build environment is prepared correctly, the libs directory should be handled automatically. Are you following the process outlined in the developer's guide at http://www.wireshark.org/docs/wsdg_html_chunked/ChSetupWin32.html</p></div><div id="comment-3354-info" class="comment-info"><span class="comment-age">(05 Apr '11, 13:53)</span> <span class="comment-user userinfo">multipleinte...</span></div></div><span id="3357"></span><div id="comment-3357" class="comment"><div id="post-3357-score" class="comment-score"></div><div class="comment-text"><p>I am following this process step by step. so i want to verify tools. I am getting error about vcredist exe when i verify tools. Should i go ahead compile with this error so that lib folder will be created and i can copy this executable?</p></div><div id="comment-3357-info" class="comment-info"><span class="comment-age">(05 Apr '11, 14:13)</span> <span class="comment-user userinfo">dsprabhu4</span></div></div><span id="3375"></span><div id="comment-3375" class="comment"><div id="post-3375-score" class="comment-score"></div><div class="comment-text"><p>Thanks a lot, multipleinterfaces. I created this folder manually and copied -vcredist_x86exe. Then i was able to verify tool and compile wireshark code.</p></div><div id="comment-3375-info" class="comment-info"><span class="comment-age">(06 Apr '11, 08:10)</span> <span class="comment-user userinfo">dsprabhu4</span></div></div></div><div id="comment-tools-3344" class="comment-tools"></div><div class="clear"></div><div id="comment-3344-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3359"></span>

<div id="answer-container-3359" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3359-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3359-score" class="post-score" title="current number of votes">1</div><span id="post-3359-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If I understand your situation correctly, then you will need to manually create the libs folder (should be <code>C:\\wireshark-win32-libs-1.4</code> for Wireshark versions 1.4.x following the Developer's Guide) before running <code>nmake</code>, and <code>vcredist_x86.exe</code> needs to be present in the libs folder <em>before</em> attempting to build Wireshark.</p><p>Creating the libs folder and copying vcredist_x86.exe as recommended in http://ask.wireshark.org/questions/3352/copying-vcredist_x86exe-for-ms-vs-2008-express should solve the problem.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Apr '11, 14:45</strong></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p><span>multipleinte...</span><br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="multipleinterfaces has 9 accepted answers">12%</span></p></div></div><div id="comments-container-3359" class="comments-container"></div><div id="comment-tools-3359" class="comment-tools"></div><div class="clear"></div><div id="comment-3359-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

