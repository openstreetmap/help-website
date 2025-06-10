+++
type = "question"
title = "extract the Tag:highway width from OSM"
description = '''Hello  Is there a way to extract the width of the road? I notice that the Tag:highway have an attribute called width, but when I use this attribute, it will give me the with of a barrier or a wall, but not the with of secondary or primary road, for example  I&#x27;m just wondering can we extract this inf...'''
date = "2021-06-26T17:00:00Z"
lastmod = "2021-06-26T21:17:00Z"
weight = 80728
keywords = [ "osm" ]
aliases = [ "/questions/80728" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [extract the Tag:highway width from OSM](/questions/80728/extract-the-taghighway-width-from-osm)

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
<span id="post-80728-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80728-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-80728-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello Is there a way to extract the width of the road? I notice that the Tag:highway have an attribute called width, but when I use this attribute, it will give me the with of a barrier or a wall, but not the with of secondary or primary road, for example I'm just wondering can we extract this information.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Jun '21, 17:00</strong></p>
<img src="https://secure.gravatar.com/avatar/00b20ea2eb5708a716896e0d335050f7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rabeeqasem&#39;s gravatar image" />
<p><span>rabeeqasem</span><br />
<span class="score" title="31 reputation points">31</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rabeeqasem has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-80728" class="comments-container">
&#10;</div>
<div id="comment-tools-80728" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80728-form-container" class="comment-form-container">
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

<span id="80741"></span>

<div id="answer-container-80741" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-80741-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80741-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-80741-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="rabeeqasem has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The <code>highway=</code> and <code>width=</code> are both keys in the database, one is not an attribute for another although they are complementary.</p>
<p>The completeness of OSM varies from place to place. Widths are relatively difficult to measure accurately especially on busy roads. Depending on your application you may find that the <a href="https://wiki.openstreetmap.org/wiki/Key:lanes">lanes</a> tags provides a reasonable proxy for a true width. While this is much more widely used the same caveat applies. Only <a href="https://taginfo.openstreetmap.org/keys/?key=highway#combinations">approximately 6%</a> of objects with a highway tag also have lanes tagged (compared with 1.3% for width).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Jun '21, 21:17</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-80741" class="comments-container">
&#10;</div>
<div id="comment-tools-80741" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80741-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="80737"></span>

<div id="answer-container-80737" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-80737-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80737-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-80737-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi are you able to give us an example of the situation ? A possibility is that no one has added the width of the main road, but only the width of the barrier.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Jun '21, 20:43</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
</div>
<div id="comments-container-80737" class="comments-container">
&#10;</div>
<div id="comment-tools-80737" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80737-form-container" class="comment-form-container">
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

