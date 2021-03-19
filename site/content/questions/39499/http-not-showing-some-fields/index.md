+++
type = "question"
title = "HTTP not showing some fields?"
description = '''Hi, I am running Yosemite 10.10.1 and using wireshark too capture HTTP traffic over wifi. I can capture traffic fine, but when i go to check my HTTP GET messages i don&#x27;t have many fields under Hyper Transfer Protocol.  I wan&#x27;t it too look like this: https://maxwellsullivan.files.wordpress.com/2013/0...'''
date = "2015-01-30T06:18:00Z"
lastmod = "2015-02-01T03:15:00Z"
weight = 39499
keywords = [ "http" ]
aliases = [ "/questions/39499" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [HTTP not showing some fields?](/questions/39499/http-not-showing-some-fields)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39499-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39499-score" class="post-score" title="current number of votes">0</div><span id="post-39499-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I am running Yosemite 10.10.1 and using wireshark too capture HTTP traffic over wifi. I can capture traffic fine, but when i go to check my HTTP GET messages i don't have many fields under Hyper Transfer Protocol. I wan't it too look like this: <a href="https://maxwellsullivan.files.wordpress.com/2013/02/wireshark2part2.png">https://maxwellsullivan.files.wordpress.com/2013/02/wireshark2part2.png</a> But my wireshark shows <a href="https://drive.google.com/file/d/0Bz3M17Cg2hwgc1RpRDIzc0V2UU0/view?usp=sharing">https://drive.google.com/file/d/0Bz3M17Cg2hwgc1RpRDIzc0V2UU0/view?usp=sharing</a> I am missing a lot of HTTP fields. How do i fix it?</p><p>Im running Version 1.99.1 (v1.99.1-0-g4c229ca from master)</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Jan '15, 06:18</strong></p><img src="https://secure.gravatar.com/avatar/66e8e8208476bae813f615a060d5e4a5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jacob&#39;s gravatar image" /><p><span>jacob</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jacob has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>30 Jan '15, 10:36</strong> </span></p></div></div><div id="comments-container-39499" class="comments-container"><span id="39504"></span><div id="comment-39504" class="comment"><div id="post-39504-score" class="comment-score"></div><div class="comment-text"><p>Maybe you could post the actual capture file somewhere? Also, what version of Wireshark are you running?</p></div><div id="comment-39504-info" class="comment-info"><span class="comment-age">(30 Jan '15, 08:52)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div><span id="39506"></span><div id="comment-39506" class="comment"><div id="post-39506-score" class="comment-score"></div><div class="comment-text"><p>Which exact version of wireshark are you running? There was a bug in version 1.99 that just got fixed yesterday. (<a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=10798">bug 10798</a>)</p></div><div id="comment-39506-info" class="comment-info"><span class="comment-age">(30 Jan '15, 10:04)</span> <span class="comment-user userinfo">Hadriel</span></div></div></div><div id="comment-tools-39499" class="comment-tools"></div><div class="clear"></div><div id="comment-39499-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39508"></span>

<div id="answer-container-39508" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39508-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39508-score" class="post-score" title="current number of votes">0</div><span id="post-39508-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>That version has the bug - <a href="https://www.wireshark.org/download/automated/osx/">download the latest version</a>. It should (hopefully) be fixed.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Jan '15, 10:50</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p><span>Hadriel</span><br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-39508" class="comments-container"><span id="39534"></span><div id="comment-39534" class="comment"><div id="post-39534-score" class="comment-score"></div><div class="comment-text"><p>Thx, it is working now!</p></div><div id="comment-39534-info" class="comment-info"><span class="comment-age">(01 Feb '15, 03:15)</span> <span class="comment-user userinfo">jacob</span></div></div></div><div id="comment-tools-39508" class="comment-tools"></div><div class="clear"></div><div id="comment-39508-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

