+++
type = "question"
title = "How to mark a blocked street for cars"
description = '''I want to mark a street which is blocked for cars but free for bicyles and pedestrians'''
date = "2013-07-01T20:49:00Z"
lastmod = "2013-07-01T22:51:00Z"
weight = 23878
keywords = [ "street", "blocked" ]
aliases = [ "/questions/23878" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to mark a blocked street for cars](/questions/23878/how-to-mark-a-blocked-street-for-cars)

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
<span id="post-23878-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23878-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-23878-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to mark a street which is blocked for cars but free for bicyles and pedestrians</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-street" rel="tag" title="see questions tagged &#39;street&#39;">street</span> <span class="post-tag tag-link-blocked" rel="tag" title="see questions tagged &#39;blocked&#39;">blocked</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Jul '13, 20:49</strong></p>
<img src="https://secure.gravatar.com/avatar/980748b19149c76e4b4438c82c671f72?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Brano%20Stofko&#39;s gravatar image" />
<p><span>Brano Stofko</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Brano Stofko has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Jul '13, 22:36</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span></p>
</div>
</div>
<div id="comments-container-23878" class="comments-container">
&#10;</div>
<div id="comment-tools-23878" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23878-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="23884"></span>

<div id="answer-container-23884" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-23884-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23884-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-23884-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>How best to represent this depends on how the street is actually blocked.</p>
<p><a href="https://www.openstreetmap.org/?lat=53.121851&amp;lon=-1.265678&amp;zoom=18&amp;layers=M">Here</a> is one example where the footpath/sidewalk along the main road is raised, but there's a join to the old road (closed off to prevent it being used as a rat-run). Here the implicit access tags on the "highway=footway" prevent vehicular access (in your case you'd want to pick an appropriate highway tag and add "bicycle=yes" if bicycle access isn't implicit.</p>
<p>There's a slightly different example <a href="https://www.openstreetmap.org/?lat=53.137986&amp;lon=-1.56041&amp;zoom=18&amp;layers=M">here</a>. In this example there road's still there, but there's something large preventing vehicular access (actually a large planter rather than a bollard). There are also explicit access signs on a short stretch of road, which <a href="https://www.openstreetmap.org/browse/way/115930687">have been mapped</a>.</p>
<p>So to sum up:</p>
<ol>
<li>Split the road as required.</li>
<li>Choose an appropriate highway tag for each section, if necessary.</li>
<li>Add extra access tags, if necessary.</li>
<li>Add any explicit obstructions (e.g. bollards).</li>
</ol>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Jul '13, 22:51</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-23884" class="comments-container">
&#10;</div>
<div id="comment-tools-23884" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23884-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="23881"></span>

<div id="answer-container-23881" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-23881-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23881-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-23881-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>A search of the Wiki (documentation) using altenativly barrier or bollard should answer your question.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Jul '13, 21:41</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Jul '13, 21:44</strong> </span></p>
</div>
</div>
<div id="comments-container-23881" class="comments-container">
<span id="23882"></span>
<div id="comment-23882" class="comment">
<div id="post-23882-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="https://wiki.openstreetmap.org/wiki/Access">https://wiki.openstreetmap.org/wiki/Access</a> may also be relevant.</p>
</div>
<div id="comment-23882-info" class="comment-info">
<span class="comment-age">(01 Jul '13, 21:44)</span> <span class="comment-user userinfo">gnurk</span>
</div>
</div>
</div>
<div id="comment-tools-23881" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23881-form-container" class="comment-form-container">
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

