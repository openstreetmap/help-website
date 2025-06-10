+++
type = "question"
title = "Third party node submission"
description = '''Hi, i would like to let users of my app to add nodes without registering to openstreetmap. So basically the adding request are done with my openstreetmap username but from a third party. Is this a feasible/admitted by OSM? If yes, any suggestion to API documentation are welcome. Thanks'''
date = "2015-04-26T18:34:00Z"
lastmod = "2015-04-26T20:26:00Z"
weight = 42605
keywords = [ "api", "3rd_party" ]
aliases = [ "/questions/42605" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Third party node submission](/questions/42605/third-party-node-submission)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-42605-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42605-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-42605-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, i would like to let users of my app to add nodes without registering to openstreetmap. So basically the adding request are done with my openstreetmap username but from a third party.</p>
<p>Is this a feasible/admitted by OSM? If yes, any suggestion to API documentation are welcome.</p>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-3rd_party" rel="tag" title="see questions tagged &#39;3rd_party&#39;">3rd_party</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Apr '15, 18:34</strong></p>
<img src="https://secure.gravatar.com/avatar/d364f8d4490a5dd3c6eb1d37e873d2fe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="xenoky&#39;s gravatar image" />
<p><span>xenoky</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="xenoky has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-42605" class="comments-container">
&#10;</div>
<div id="comment-tools-42605" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42605-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="42606"></span>

<div id="answer-container-42606" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-42606-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42606-score" class="post-score" title="current number of votes">
7
</div>
<span id="post-42606-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>We don't like this for several reasons:</p>
<ul>
<li>OSM mappers would not have a way to get in touch with people adding data; messages, changeset discussions etc. would all end up in your personal account.</li>
<li>Some of your users might contribute copyrighted or otherwise problematic content, and it could become difficult to separate the good from the bad.</li>
<li>You would gain undue influence on what your users map - e.g. because you design the software, you could make sure they only use tags <em>you</em> like and nobody could tell them.</li>
<li>People contributing to OSM through your app might not even know that they are OSM contributors; they wouldn't be part of "our" community but of "yours".</li>
</ul>
<p>It's not completely impossible and exceptions have been made in the past but don't bank on it. Rather, explore how you can use OAuth to let your users seamlessly log in with OSM and then your application can perform edits on their behalf.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Apr '15, 20:26</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Apr '15, 20:26</strong> </span></p>
</div>
</div>
<div id="comments-container-42606" class="comments-container">
&#10;</div>
<div id="comment-tools-42606" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42606-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

