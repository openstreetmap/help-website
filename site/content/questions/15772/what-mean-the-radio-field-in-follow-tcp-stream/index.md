+++
type = "question"
title = "What mean the radio field in follow tcp stream?"
description = '''I select the Follow TCP Stream for analyzis a communication, in the first section (A-&amp;gt;B) in red color, the first is a GET (URL), next there is a field: radio= radio&amp;amp;email then there is a email address what mean it? IT is &quot;re-link&quot; me and it attempts send a mail?'''
date = "2012-11-09T07:47:00Z"
lastmod = "2012-11-13T07:26:00Z"
weight = 15772
keywords = [ "follow.tcp.stream" ]
aliases = [ "/questions/15772" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [What mean the radio field in follow tcp stream?](/questions/15772/what-mean-the-radio-field-in-follow-tcp-stream)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15772-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15772-score" class="post-score" title="current number of votes">0</div><span id="post-15772-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I select the Follow TCP Stream for analyzis a communication, in the first section (A-&gt;B) in red color, the first is a GET (URL), next there is a field: radio= radio&amp;email then there is a email address what mean it? IT is "re-link" me and it attempts send a mail?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-follow.tcp.stream" rel="tag" title="see questions tagged &#39;follow.tcp.stream&#39;">follow.tcp.stream</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Nov '12, 07:47</strong></p><img src="https://secure.gravatar.com/avatar/b69f8c2e6eab5c44b74a6447d09eaf77?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jgarzam&#39;s gravatar image" /><p><span>jgarzam</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jgarzam has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>09 Nov '12, 07:48</strong> </span></p></div></div><div id="comments-container-15772" class="comments-container"><span id="15779"></span><div id="comment-15779" class="comment"><div id="post-15779-score" class="comment-score">1</div><div class="comment-text"><p>can you please post that GET request, including the 'radio' part? Without that it's hard to give any useful answer.</p></div><div id="comment-15779-info" class="comment-info"><span class="comment-age">(09 Nov '12, 11:45)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="15822"></span><div id="comment-15822" class="comment"><div id="post-15822-score" class="comment-score"></div><div class="comment-text"><p>GET /example/example/c5.....(URL characters)....dvcmQ!/? radio=radio&amp;<span class="__cf_email__" data-cfemail="a3c6cec2cacf9ec6dbc2ced3cfc6e3">[email protected]</span><a href="http://hotmail.com">hotmail.com</a>&amp;social_opt1=......y=11 HTTP /1.1</p><p>I guess radio= is part of URL, what do you think??</p><p>Thanks Kurt!!!!!!</p></div><div id="comment-15822-info" class="comment-info"><span class="comment-age">(12 Nov '12, 06:28)</span> <span class="comment-user userinfo">jgarzam</span></div></div><span id="15823"></span><div id="comment-15823" class="comment"><div id="post-15823-score" class="comment-score">1</div><div class="comment-text"><p>That's a parameter to the page. All elements after the "?" are parameters in the form "name=value", with multiple parameters separated by "&amp;".</p><p>So the parameter name is radio and the value is radio. Probably due to a radio button on the form that generated the request.</p></div><div id="comment-15823-info" class="comment-info"><span class="comment-age">(12 Nov '12, 06:50)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="15868"></span><div id="comment-15868" class="comment"><div id="post-15868-score" class="comment-score"></div><div class="comment-text"><p>thanks Kurt, thanks grahamb, I really learn something today!!!!</p></div><div id="comment-15868-info" class="comment-info"><span class="comment-age">(13 Nov '12, 07:25)</span> <span class="comment-user userinfo">jgarzam</span></div></div></div><div id="comment-tools-15772" class="comment-tools"></div><div class="clear"></div><div id="comment-15772-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="15833"></span>

<div id="answer-container-15833" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15833-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15833-score" class="post-score" title="current number of votes">1</div><span id="post-15833-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>See, for example, the <a href="http://www.w3.org/TR/1999/REC-html401-19991224/interact/forms.html">the "Forms in HTML documents" chapter</a> of the <a href="http://www.w3.org/TR/1999/REC-html401-19991224/">HTML 4.01 specification</a>. It specifies how fields in HTML forms are used to generate the "query" part of a URI sent in response to, for example, a button pushed on that form.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Nov '12, 11:45</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-15833" class="comments-container"><span id="15869"></span><div id="comment-15869" class="comment"><div id="post-15869-score" class="comment-score"></div><div class="comment-text"><p>thanks very much Guy Harris, I will check the page, I need read it for learn about HTML, thanks!!!</p></div><div id="comment-15869-info" class="comment-info"><span class="comment-age">(13 Nov '12, 07:26)</span> <span class="comment-user userinfo">jgarzam</span></div></div></div><div id="comment-tools-15833" class="comment-tools"></div><div class="clear"></div><div id="comment-15833-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

