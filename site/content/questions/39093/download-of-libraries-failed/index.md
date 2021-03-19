+++
type = "question"
title = "Download of Libraries failed"
description = '''Hello, today I downloaded the newest Wireshark sources and tried to run &quot;nmake Makefile.nmake setup&quot;, but the following error occured:  *** . *** No HTTP proxy specified (http_proxy and HTTP_PROXY are empty). Downloading . into &#x27;/cygdrive/c/Users/LucaAdrian/Desktop/Wireshark&#x27;, installing into USBSRV...'''
date = "2015-01-13T08:38:00Z"
lastmod = "2015-01-13T09:58:00Z"
weight = 39093
keywords = [ "libraries", "download", "setup", "gtk", "build" ]
aliases = [ "/questions/39093" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Download of Libraries failed](/questions/39093/download-of-libraries-failed)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39093-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39093-score" class="post-score" title="current number of votes">0</div><span id="post-39093-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>today I downloaded the newest Wireshark sources and tried to run "nmake Makefile.nmake setup", but the following error occured:</p><pre><code>*** . ***
No HTTP proxy specified (http_proxy and HTTP_PROXY are empty).
Downloading . into &#39;/cygdrive/c/Users/LucaAdrian/Desktop/Wireshark&#39;, installing
into USBSRV\wireshark\Wireshark-win64-libs-1.12
File `index.html&#39; already there, will not retrieve.
Extracting &#39;/cygdrive/c/Users/LucaAdrian/Desktop/Wireshark/.&#39; into &#39;/cygdrive/c/
Users/LucaAdrian/Desktop/Wireshark/USBSRV\wireshark\Wireshark-win64-libs-1.12&#39;
*** gtk2 ***
No HTTP proxy specified (http_proxy and HTTP_PROXY are empty).
Downloading gtk2 into &#39;/cygdrive/c/Users/LucaAdrian/Desktop/Wireshark&#39;, installi
ng into USBSRV\wireshark\Wireshark-win64-libs-1.12
--17:17:52--  http://anonsvn.wireshark.org/wireshark-win64-libs/tags/2014-10-01/
packages/gtk2
           =&gt; `gtk2&#39;
Connecting to anonsvn.wireshark.org:80... connected!
HTTP request sent, awaiting response... 404 Not Found
17:17:53 ERROR 404: Not Found.
ERROR: Can&#39;t download http://anonsvn.wireshark.org/wireshark-win64-libs/tags/201
4-10-01/packages//gtk2
NMAKE : fatal error U1077: &quot;C:\cygwin64\bin\bash.EXE&quot;: Rückgabe-Code &quot;0x1&quot;
Stop.</code></pre><p>I use Windows 8.1 64bit, VisualStudio2013 and a 64bit build environment. BTW I don't use any proxy for my internet connection.</p><p>Thankfully lal12</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-libraries" rel="tag" title="see questions tagged &#39;libraries&#39;">libraries</span> <span class="post-tag tag-link-download" rel="tag" title="see questions tagged &#39;download&#39;">download</span> <span class="post-tag tag-link-setup" rel="tag" title="see questions tagged &#39;setup&#39;">setup</span> <span class="post-tag tag-link-gtk" rel="tag" title="see questions tagged &#39;gtk&#39;">gtk</span> <span class="post-tag tag-link-build" rel="tag" title="see questions tagged &#39;build&#39;">build</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Jan '15, 08:38</strong></p><img src="https://secure.gravatar.com/avatar/cc56ba9bd225bd68cea09a404ecc0b6e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lal12&#39;s gravatar image" /><p><span>lal12</span><br />
<span class="score" title="36 reputation points">36</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lal12 has 2 accepted answers">33%</span></p></div></div><div id="comments-container-39093" class="comments-container"></div><div id="comment-tools-39093" class="comment-tools"></div><div class="clear"></div><div id="comment-39093-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="39097"></span>

<div id="answer-container-39097" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39097-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39097-score" class="post-score" title="current number of votes">0</div><span id="post-39097-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="lal12 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I just changed the WIRESHARK_BASE_DIR and it worked. The problem was a space character in the path, I am just confused how this leads to an Error 404 and a wrong download file name.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Jan '15, 09:27</strong></p><img src="https://secure.gravatar.com/avatar/cc56ba9bd225bd68cea09a404ecc0b6e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lal12&#39;s gravatar image" /><p><span>lal12</span><br />
<span class="score" title="36 reputation points">36</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lal12 has 2 accepted answers">33%</span></p></div></div><div id="comments-container-39097" class="comments-container"><span id="39098"></span><div id="comment-39098" class="comment"><div id="post-39098-score" class="comment-score"></div><div class="comment-text"><p>This is the cludgy interface between Windows and Unix that is Cygwin. Something probably ins't quoted properly so the path is split into two arguments.</p></div><div id="comment-39098-info" class="comment-info"><span class="comment-age">(13 Jan '15, 09:58)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-39097" class="comment-tools"></div><div class="clear"></div><div id="comment-39097-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="39094"></span>

<div id="answer-container-39094" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39094-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39094-score" class="post-score" title="current number of votes">0</div><span id="post-39094-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Something seems to be wrong with the URL for the package download. If you got to the <a href="http://anonsvn.wireshark.org/wireshark-win64-libs/tags/2014-10-01/packages/">packages download page</a> you can see the x64 gtk2 packages listed such as gtk+-bundle_2.24.23-1.1_win64ws.zip.</p><p>When I run setup (for x86) the gtk2 package request looks like this:</p><pre><code>****** gtk+-bundle_2.24.23-1.1_win32ws.zip ******
No HTTP proxy specified (http_proxy and HTTP_PROXY are empty).
Downloading gtk+-bundle_2.24.23-1.1_win32ws.zip into &#39;/cygdrive/e/Wireshark/Wire
shark-win32-libs&#39;, installing into gtk2
File &#39;gtk+-bundle_2.24.23-1.1_win32ws.zip&#39; already there; not retrieving.</code></pre><p>So it looks as though something is up in your working copy. Have you made any changes at all, i.e. to config.nmake?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Jan '15, 09:12</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-39094" class="comments-container"><span id="39095"></span><div id="comment-39095" class="comment"><div id="post-39095-score" class="comment-score"></div><div class="comment-text"><p>It is the same error no matter whether I make changes or not to the config.nmake (I tried this also with the original unchanged files)</p></div><div id="comment-39095-info" class="comment-info"><span class="comment-age">(13 Jan '15, 09:16)</span> <span class="comment-user userinfo">lal12</span></div></div></div><div id="comment-tools-39094" class="comment-tools"></div><div class="clear"></div><div id="comment-39094-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

