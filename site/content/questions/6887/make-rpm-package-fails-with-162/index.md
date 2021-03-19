+++
type = "question"
title = "make rpm-package fails with 1.6.2"
description = '''Hi. I have just downloaded 1.6.2 Build is ok. (make works) Now trying to make a rpm (make rpm-package). It failed. First I had an issue with krb5.h missing. I added package kerberos devel. Now I have error Kerberos not found &quot;checking wether the Kerberos library is Hedimdal or MIT... no configure: e...'''
date = "2011-10-14T02:35:00Z"
lastmod = "2011-10-14T06:59:00Z"
weight = 6887
keywords = [ "kerberos", "make", "rpm-package" ]
aliases = [ "/questions/6887" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [make rpm-package fails with 1.6.2](/questions/6887/make-rpm-package-fails-with-162)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6887-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6887-score" class="post-score" title="current number of votes">0</div><span id="post-6887-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi.</p><p>I have just downloaded 1.6.2 Build is ok. (make works)</p><p>Now trying to make a rpm (make rpm-package). It failed. First I had an issue with krb5.h missing. I added package kerberos devel. Now I have error Kerberos not found</p><p>"checking wether the Kerberos library is Hedimdal or MIT... no configure: error: Kerberos not found"</p><p>If I am able to build with make, shouldn't I be able to make rpm-package ???</p><p>Thanks</p><p>Chris</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-kerberos" rel="tag" title="see questions tagged &#39;kerberos&#39;">kerberos</span> <span class="post-tag tag-link-make" rel="tag" title="see questions tagged &#39;make&#39;">make</span> <span class="post-tag tag-link-rpm-package" rel="tag" title="see questions tagged &#39;rpm-package&#39;">rpm-package</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Oct '11, 02:35</strong></p><img src="https://secure.gravatar.com/avatar/bd299b3680beb7713576358a70120457?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="blinde&#39;s gravatar image" /><p><span>blinde</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="blinde has no accepted answers">0%</span></p></div></div><div id="comments-container-6887" class="comments-container"></div><div id="comment-tools-6887" class="comment-tools"></div><div class="clear"></div><div id="comment-6887-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6888"></span>

<div id="answer-container-6888" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6888-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6888-score" class="post-score" title="current number of votes">1</div><span id="post-6888-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="blinde has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Maybe... Check what 'configure' options are used when making the RPM (in the .spec file). Maybe they're not the same as what you're configuring with.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Oct '11, 06:14</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-6888" class="comments-container"><span id="6890"></span><div id="comment-6890" class="comment"><div id="post-6890-score" class="comment-score"></div><div class="comment-text"><p>Yep. U right.</p><p>In fact in the .spec file there is a --with-krb5... I removed it and it works...</p><p>Thanks</p></div><div id="comment-6890-info" class="comment-info"><span class="comment-age">(14 Oct '11, 06:59)</span> <span class="comment-user userinfo">blinde</span></div></div></div><div id="comment-tools-6888" class="comment-tools"></div><div class="clear"></div><div id="comment-6888-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

