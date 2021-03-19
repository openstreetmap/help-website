+++
type = "question"
title = "Capture POST requests or websites"
description = '''What is the best way to capture websites? You can type http in the filter, but it is still pretty tedious to find the websites visited and POST requests (because it also shows getting images, css file etc.). Is there anyway I could see the websites nicely? Thanks.'''
date = "2014-05-02T06:37:00Z"
lastmod = "2014-05-02T06:46:00Z"
weight = 32395
keywords = [ "wpa2" ]
aliases = [ "/questions/32395" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Capture POST requests or websites](/questions/32395/capture-post-requests-or-websites)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32395-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32395-score" class="post-score" title="current number of votes">0</div><span id="post-32395-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>What is the best way to capture websites? You can type <code>http</code> in the filter, but it is still pretty tedious to find the websites visited and POST requests (because it also shows getting images, css file etc.). Is there anyway I could see the websites nicely? Thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wpa2" rel="tag" title="see questions tagged &#39;wpa2&#39;">wpa2</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 May '14, 06:37</strong></p><img src="https://secure.gravatar.com/avatar/eeca75356089d0569c63dfc514d7f19d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tttttttttttt2&#39;s gravatar image" /><p><span>tttttttttttt2</span><br />
<span class="score" title="34 reputation points">34</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tttttttttttt2 has no accepted answers">0%</span></p></div></div><div id="comments-container-32395" class="comments-container"></div><div id="comment-tools-32395" class="comment-tools"></div><div class="clear"></div><div id="comment-32395-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32396"></span>

<div id="answer-container-32396" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32396-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32396-score" class="post-score" title="current number of votes">1</div><span id="post-32396-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="tttttttttttt2 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You could use the Statistics menu, there are some entries for HTTP which will show you the requests in a tree view. It's not very comfortable though.</p><p>If you're looking for some way to actually reconstruct and view the web pages as seen by the user Wireshark doesn't help, except for the HTTP object export functionality you can find in the File menu. But then you'd have to open the exported pages as files in a web browser to look at them.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 May '14, 06:40</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-32396" class="comments-container"><span id="32397"></span><div id="comment-32397" class="comment"><div id="post-32397-score" class="comment-score"></div><div class="comment-text"><p><span>@Jasper</span> thank you so much for your help. Yeah, I've tried statistics, I can select http.host for example, but I can't (I think) to see just POST requests for example. And no, I don't want to reconstruct and view web pages.</p></div><div id="comment-32397-info" class="comment-info"><span class="comment-age">(02 May '14, 06:43)</span> <span class="comment-user userinfo">tttttttttttt2</span></div></div><span id="32398"></span><div id="comment-32398" class="comment"><div id="post-32398-score" class="comment-score"></div><div class="comment-text"><p>What I usually do is just to filter on "http.request.method" to see all requests (GET, POST etc). If you don't want GIFs etc. showing up you could exclude them by adding things 'and not http.request.full_uri contains ".gif"' or something like that.</p><p>The other way to go could be to use the list of requests and export the packet list view to csv. Then go and use Excel (or any other spread sheet tool) to work on the list outside of Wireshark.</p></div><div id="comment-32398-info" class="comment-info"><span class="comment-age">(02 May '14, 06:46)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-32396" class="comment-tools"></div><div class="clear"></div><div id="comment-32396-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

