+++
type = "question"
title = "meadow/buildings accuracy"
description = '''Hello all I&#x27;m trying to draw some meadow areas around my village... the thing is should I intersect the &quot;area&quot; points with the &quot;ways&quot; points to avoid the gap areas between the way and the buildings/nature areas?'''
date = "2012-04-18T10:42:00Z"
lastmod = "2012-04-18T16:48:00Z"
weight = 12117
keywords = [ "ways", "rendering", "area" ]
aliases = [ "/questions/12117" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [meadow/buildings accuracy](/questions/12117/meadowbuildings-accuracy)

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
<span id="post-12117-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12117-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-12117-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello all I'm trying to draw some meadow areas around my <a href="http://www.openstreetmap.org/?lat=41.062298&amp;lon=-8.545524&amp;zoom=18&amp;layers=M" title="village">village</a>...</p>
<p>the thing is should I intersect the "area" points with the "ways" points to avoid the gap areas between the way and the buildings/nature areas?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ways" rel="tag" title="see questions tagged &#39;ways&#39;">ways</span> <span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-area" rel="tag" title="see questions tagged &#39;area&#39;">area</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Apr '12, 10:42</strong></p>
<img src="https://secure.gravatar.com/avatar/eb1abd892f9d1665b032b912f3369131?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rsbarbosa&#39;s gravatar image" />
<p><span>rsbarbosa</span><br />
<span class="score" title="41 reputation points">41</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rsbarbosa has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-12117" class="comments-container">
&#10;</div>
<div id="comment-tools-12117" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12117-form-container" class="comment-form-container">
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

<span id="12132"></span>

<div id="answer-container-12132" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-12132-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12132-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-12132-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="rsbarbosa has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You should glue areas together if one phisicaly start where the other stops (say, a forest adjoining a meadow), but you shouldn't glue an osm area on the side of an osm way, such a a highway (if you did that, you would be describing a field which goes all the way to the middle of the road, which is false).</p>
<p>Concerning buildings and some other types of areas, people usually dont bother making a "hole" in the enclosing area : they just put a big simple "meadow" area and a "building" area inside it.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Apr '12, 12:49</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-12132" class="comments-container">
<span id="12137"></span>
<div id="comment-12137" class="comment">
<div id="post-12137-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>that's exactly my problem! From what I can assume seeing your answer is that the osm way (on the editor) indicates the middle of the road and according to is type it will be rendered by OSM with an specific width thus placing the "holes" between the road and the meadow, forest , building... and I shouldn't really be bother by that...In my view the rendering is worst if it was only a blank area there no building no nothing....</p>
</div>
<div id="comment-12137-info" class="comment-info">
<span class="comment-age">(18 Apr '12, 13:56)</span> <span class="comment-user userinfo">rsbarbosa</span>
</div>
</div>
<span id="12141"></span>
<div id="comment-12141" class="comment">
<div id="post-12141-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>That's it, don't worry about the rendering; correct data is more important. Related to <a href="http://wiki.openstreetmap.org/wiki/Don&#39;t_tag_for_the_renderer">http://wiki.openstreetmap.org/wiki/Don't_tag_for_the_renderer</a></p>
<p>One thing you can do is specify width=* on the highway. Mapnik doesn't yet take it into account, but I'm confident someday it will, improving the rendering.</p>
</div>
<div id="comment-12141-info" class="comment-info">
<span class="comment-age">(18 Apr '12, 16:48)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
</div>
<div id="comment-tools-12132" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12132-form-container" class="comment-form-container">
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

