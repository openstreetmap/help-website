+++
type = "question"
title = "Wireshark 1.99.6 for Mac OSX 10.10.3: Can´t open preferences file"
description = '''After I fixed up the file system rights by Mac OSX tools I got the following error message: Can&#x27;t open preferences file &quot;/Users/Christian/.wireshark/profiles/WLAN/preferences&quot;: Permission denied. So my question is: What rights do wireshark need? Directory .wireshark is 755 Directory profiles is 755 ...'''
date = "2015-06-08T12:43:00Z"
lastmod = "2015-06-08T22:26:00Z"
weight = 42982
keywords = [ "wireshark1.99", "macosx", "preferences", "error" ]
aliases = [ "/questions/42982" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Wireshark 1.99.6 for Mac OSX 10.10.3: Can´t open preferences file](/questions/42982/wireshark-1996-for-mac-osx-10103-can-t-open-preferences-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42982-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42982-score" class="post-score" title="current number of votes">0</div><span id="post-42982-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>After I fixed up the file system rights by Mac OSX tools I got the following error message:</p><p>Can't open preferences file "/Users/Christian/.wireshark/profiles/WLAN/preferences": Permission denied.</p><p>So my question is: What rights do wireshark need?</p><pre><code>Directory .wireshark is 755
Directory profiles   is 755
Directory WLAN       is 755
File preferences     is 544</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireshark1.99" rel="tag" title="see questions tagged &#39;wireshark1.99&#39;">wireshark1.99</span> <span class="post-tag tag-link-macosx" rel="tag" title="see questions tagged &#39;macosx&#39;">macosx</span> <span class="post-tag tag-link-preferences" rel="tag" title="see questions tagged &#39;preferences&#39;">preferences</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Jun '15, 12:43</strong></p><img src="https://secure.gravatar.com/avatar/3b24b339fc62fb46dced6a443d3202ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christian_R&#39;s gravatar image" /><p><span>Christian_R</span><br />
<span class="score" title="1830 reputation points"><span>1.8k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christian_R has 25 accepted answers">16%</span></p></div></div><div id="comments-container-42982" class="comments-container"></div><div id="comment-tools-42982" class="comment-tools"></div><div class="clear"></div><div id="comment-42982-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="42990"></span>

<div id="answer-container-42990" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42990-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42990-score" class="post-score" title="current number of votes">2</div><span id="post-42990-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Christian_R has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>An octal permissions setting of 544 is binary 101 100 100, or <code>r-x r-- r--</code>; that denies write permission to the owner of the file. Try <code>rw- r-- r--</code>, or 644, which grants write permission to the owner of the file.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Jun '15, 17:33</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-42990" class="comments-container"><span id="42992"></span><div id="comment-42992" class="comment"><div id="post-42992-score" class="comment-score"></div><div class="comment-text"><p>Works great! Thanks!</p></div><div id="comment-42992-info" class="comment-info"><span class="comment-age">(08 Jun '15, 22:26)</span> <span class="comment-user userinfo">Christian_R</span></div></div></div><div id="comment-tools-42990" class="comment-tools"></div><div class="clear"></div><div id="comment-42990-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

