+++
type = "question"
title = "Error: Unable to open wireshark"
description = '''Hi Ive downlaoded wireshark to my computer a couple of months ago now. Within in the last few weeks i have had trouble with it opneing saying there is an error message saying  &quot;The application was unable to start correctly (0xc000007b) Click Ok to close the application&quot; Bearing in mind i have had no...'''
date = "2012-12-08T12:58:00Z"
lastmod = "2013-06-23T14:33:00Z"
weight = 16727
keywords = [ "error" ]
aliases = [ "/questions/16727" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Error: Unable to open wireshark](/questions/16727/error-unable-to-open-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16727-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16727-score" class="post-score" title="current number of votes">0</div><span id="post-16727-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Ive downlaoded wireshark to my computer a couple of months ago now. Within in the last few weeks i have had trouble with it opneing saying there is an error message saying "The application was unable to start correctly (0xc000007b) Click Ok to close the application" Bearing in mind i have had no previous trouble and then all of a sudden the wirsehark just doesnt operate.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Dec '12, 12:58</strong></p><img src="https://secure.gravatar.com/avatar/b8c261d2bc290118406ffbd96003f9fa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ad2108&#39;s gravatar image" /><p><span>ad2108</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ad2108 has no accepted answers">0%</span></p></div></div><div id="comments-container-16727" class="comments-container"></div><div id="comment-tools-16727" class="comment-tools"></div><div class="clear"></div><div id="comment-16727-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16730"></span>

<div id="answer-container-16730" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16730-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16730-score" class="post-score" title="current number of votes">0</div><span id="post-16730-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Did you remove any copies of the Visual C++ Runtime recently? The 64-bit version of Wireshark 1.8 depends on the 2010 SP1 CRT and 1.6 depends on the 2008 CRT. If this is the case uninstalling and reinstalling Wireshark should fix the problem.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Dec '12, 14:30</strong></p><img src="https://secure.gravatar.com/avatar/6db117a984c6529df88330dc49fb1ee4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gerald%20Combs&#39;s gravatar image" /><p><span>Gerald Combs ♦♦</span><br />
<span class="score" title="3332 reputation points"><span>3.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gerald Combs has 32 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>08 Dec '12, 14:34</strong> </span></p></div></div><div id="comments-container-16730" class="comments-container"><span id="22257"></span><div id="comment-22257" class="comment"><div id="post-22257-score" class="comment-score"></div><div class="comment-text"><p>When I looked in the System32 directory, I found a file named msvcr100_clr0400.dll. I simply made a copy of it and renamed it to msvcr100.dll. The file was placed in the system32 folder. Then it works.</p></div><div id="comment-22257-info" class="comment-info"><span class="comment-age">(23 Jun '13, 14:33)</span> <span class="comment-user userinfo">Marcelo Ferr...</span></div></div></div><div id="comment-tools-16730" class="comment-tools"></div><div class="clear"></div><div id="comment-16730-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

