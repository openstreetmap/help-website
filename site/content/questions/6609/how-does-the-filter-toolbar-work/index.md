+++
type = "question"
title = "how does the filter toolbar work ?"
description = '''I would like to know how the filter works ...I would like to know the files which help in the working of this filter. I&#x27;m trying to create trigger but to do so i would like to know the entire working of filters and the files related to it '''
date = "2011-09-28T00:41:00Z"
lastmod = "2011-10-01T02:29:00Z"
weight = 6609
keywords = [ "development" ]
aliases = [ "/questions/6609" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [how does the filter toolbar work ?](/questions/6609/how-does-the-filter-toolbar-work)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6609-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6609-score" class="post-score" title="current number of votes">0</div><span id="post-6609-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>I would like to know how the filter works ...I would like to know the files which help in the working of this filter. I'm trying to create trigger but to do so i would like to know the entire working of filters and the files related to it</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Sep '11, 00:41</strong></p><img src="https://secure.gravatar.com/avatar/264adc05b644c1ab2d670b4773a12392?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="flashkicker&#39;s gravatar image" /><p><span>flashkicker</span><br />
<span class="score" title="109 reputation points">109</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="19 badges"><span class="silver">●</span><span class="badgecount">19</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="flashkicker has 5 accepted answers">41%</span></p></div></div><div id="comments-container-6609" class="comments-container"></div><div id="comment-tools-6609" class="comment-tools"></div><div class="clear"></div><div id="comment-6609-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6611"></span>

<div id="answer-container-6611" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6611-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6611-score" class="post-score" title="current number of votes">1</div><span id="post-6611-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="flashkicker has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Check out the <a href="http://anonsvn.wireshark.org/wireshark/trunk/epan/dfilter/">display filter directory</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Sep '11, 02:34</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-6611" class="comments-container"><span id="6613"></span><div id="comment-6613" class="comment"><div id="post-6613-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the help .......</p></div><div id="comment-6613-info" class="comment-info"><span class="comment-age">(28 Sep '11, 02:55)</span> <span class="comment-user userinfo">flashkicker</span></div></div><span id="6665"></span><div id="comment-6665" class="comment"><div id="post-6665-score" class="comment-score"></div><div class="comment-text"><p>is triggers only related to filters? I read some previous questions about triggers in bugzilla where i came to know that trigcap.c plays the role of triggers in wireshark.</p></div><div id="comment-6665-info" class="comment-info"><span class="comment-age">(01 Oct '11, 02:27)</span> <span class="comment-user userinfo">Terrestrial ...</span></div></div><span id="6666"></span><div id="comment-6666" class="comment"><div id="post-6666-score" class="comment-score"></div><div class="comment-text"><p>work of trigcap:It uses the BPF to find start and stop conditions. Between the two it saves captured packets to a file.</p><p>Thanks to Jaap.</p></div><div id="comment-6666-info" class="comment-info"><span class="comment-age">(01 Oct '11, 02:29)</span> <span class="comment-user userinfo">Terrestrial ...</span></div></div></div><div id="comment-tools-6611" class="comment-tools"></div><div class="clear"></div><div id="comment-6611-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

