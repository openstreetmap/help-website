+++
type = "question"
title = "compile 1.10 fails using vs2013"
description = '''Hi Experts, Is VS2013 supported to build 1.10 or 1.12? I have VS2013 and the compile of master copy is successful. While the compile of 1.10 or 1.12 branch failed ( I have latest 1.10 downloaded using git): &amp;gt; git clone -b master-1.10 --single-branch https://code.wireshark.org/review/wireshark wir...'''
date = "2016-01-02T13:00:00Z"
lastmod = "2016-01-02T16:56:00Z"
weight = 48796
keywords = [ "vs2013", "1.10" ]
aliases = [ "/questions/48796" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [compile 1.10 fails using vs2013](/questions/48796/compile-110-fails-using-vs2013)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48796-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48796-score" class="post-score" title="current number of votes">0</div><span id="post-48796-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Experts,</p><p>Is VS2013 supported to build 1.10 or 1.12?</p><p>I have VS2013 and the compile of master copy is successful. While the compile of 1.10 or 1.12 branch failed ( I have latest 1.10 downloaded using git): &gt; git clone -b master-1.10 --single-branch <a href="https://code.wireshark.org/review/wireshark">https://code.wireshark.org/review/wireshark</a> wireshark110</p><p>On 1.10 branch, I noticed cmake doesn't download libraries - so basically I'm re-using the libraries that was downloaded for master copy. Reported issue on cmake of 1.10 is: "CMake Error: The following variables are used in this project, but they are set to NOTFOUND. Please set them or make sure they are set and tested correctly in the CMake files: GMODULE2_LIBRARIES (ADVANCED) linked by target "wiretap" in directory C:/Development/wireshark110/wiretap"</p><p>Any idea to around this? I'm following the Developer's Guide for the build task.</p><p>Thanks Jack</p><p>p.s. My environment is WIN7, VS 2013 win32 version, target is win32; I have following files under C:\Development\wireshark-win32-libs\gtk2\lib : gmodule-2.0.lib gtk2 version is 2.24.23</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-vs2013" rel="tag" title="see questions tagged &#39;vs2013&#39;">vs2013</span> <span class="post-tag tag-link-1.10" rel="tag" title="see questions tagged &#39;1.10&#39;">1.10</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Jan '16, 13:00</strong></p><img src="https://secure.gravatar.com/avatar/e1984914b8c461cdc39fe81b37c37b98?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JackaJack&#39;s gravatar image" /><p><span>JackaJack</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JackaJack has no accepted answers">0%</span></p></div></div><div id="comments-container-48796" class="comments-container"></div><div id="comment-tools-48796" class="comment-tools"></div><div class="clear"></div><div id="comment-48796-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48802"></span>

<div id="answer-container-48802" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48802-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48802-score" class="post-score" title="current number of votes">1</div><span id="post-48802-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="JackaJack has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>VS2013 is OK for 1.12, but unknown if it works for 1.10. The official builds for 1.10 and 1.12 used VS2010.</p><p>For both 1.10 and 1.12, the Windows build system is nmake. The Windows build system for 2.0 onwards is CMake. I'm not aware of any on-line location of the Developers Guide for earlier versions (i.e. nmake), but the sources for it will be in the appropriate source branches.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Jan '16, 14:56</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-48802" class="comments-container"><span id="48805"></span><div id="comment-48805" class="comment"><div id="post-48805-score" class="comment-score"></div><div class="comment-text"><p>Graham, thanks for the prompt answer. This is helpful. I tried to move on w/ "cmake" today and hit a lot configuration issues. Will go with 1.12 wsdg via "nmake".</p></div><div id="comment-48805-info" class="comment-info"><span class="comment-age">(02 Jan '16, 16:56)</span> <span class="comment-user userinfo">JackaJack</span></div></div></div><div id="comment-tools-48802" class="comment-tools"></div><div class="clear"></div><div id="comment-48802-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

