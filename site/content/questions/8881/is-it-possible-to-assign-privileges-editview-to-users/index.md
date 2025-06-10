+++
type = "question"
title = "Is it possible to assign privileges (edit/view) to users?"
description = '''I want some users to be able to view the map, others view +edit. How can this be accomplished?  edit: on a private osm server.'''
date = "2011-11-07T20:27:00Z"
lastmod = "2011-11-08T16:56:00Z"
weight = 8881
keywords = [ "user" ]
aliases = [ "/questions/8881" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Is it possible to assign privileges (edit/view) to users?](/questions/8881/is-it-possible-to-assign-privileges-editview-to-users)

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
<span id="post-8881-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8881-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-8881-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want some users to be able to view the map, others view +edit. How can this be accomplished? edit: on a private osm server.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-user" rel="tag" title="see questions tagged &#39;user&#39;">user</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Nov '11, 20:27</strong></p>
<img src="https://secure.gravatar.com/avatar/dc9b01669c0702f230fa57c384b947a8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alexz&#39;s gravatar image" />
<p><span>alexz</span><br />
<span class="score" title="225 reputation points">225</span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alexz has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Nov '11, 21:39</strong> </span></p>
</div>
</div>
<div id="comments-container-8881" class="comments-container">
&#10;</div>
<div id="comment-tools-8881" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8881-form-container" class="comment-form-container">
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

<span id="8883"></span>

<div id="answer-container-8883" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8883-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8883-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-8883-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="alexz has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is not a question about OpenStreetMap and therefore off-topic on this site.</p>
<p>When you talk about "view the map", if you mean the map tiles, then a simple web server based user authentication could solve your problem. As for editing, the OSM server already has used authentication for that. If you want (your version of) the OSM API to only respond to data requests for authenticated users, you will have to amend the Rails code with the appropriate authentication checks. If you want to combine both, and make it so that even tiles are only served to users who have an account with the Rails system then you could hack up a custom authentication module for your web server that authenticates against the Rails backend's user database.</p>
<p>But as I said, this has nothing to do with OSM any more.<br />
</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Nov '11, 08:06</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span> </br></p>
</div>
</div>
<div id="comments-container-8883" class="comments-container">
<span id="8888"></span>
<div id="comment-8888" class="comment">
<div id="post-8888-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>... these special questions dealing with the core software that OSM use could be better placed for examole on <a href="http://lists.openstreetmap.org/listinfo/rails-dev">http://lists.openstreetmap.org/listinfo/rails-dev</a> or some other developer mailing list.</p>
</div>
<div id="comment-8888-info" class="comment-info">
<span class="comment-age">(08 Nov '11, 16:56)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
</div>
<div id="comment-tools-8883" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8883-form-container" class="comment-form-container">
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

