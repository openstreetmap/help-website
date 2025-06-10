+++
type = "question"
title = "How to style map to look like google maps?"
description = '''I&#x27;m trying to include map and control it with javascript, just like google maps... Currently I&#x27;m using LeafLet library that is making requests to .. http://b.tile.osm.org/13/2412/3082.png however, styles are off ( weird color, too much information, etc)  How can i color it to look very much like goo...'''
date = "2018-02-12T22:16:00Z"
lastmod = "2020-01-21T15:35:00Z"
weight = 62063
keywords = [ "leaflet", "style", "javascript", "google_maps" ]
aliases = [ "/questions/62063" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to style map to look like google maps?](/questions/62063/how-to-style-map-to-look-like-google-maps)

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
<span id="post-62063-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62063-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-62063-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm trying to include map and control it with javascript, just like google maps...</p>
<p>Currently I'm using LeafLet library that is making requests to ..</p>
<p><a href="http://b.tile.osm.org/13/2412/3082.png">http://b.tile.osm.org/13/2412/3082.png</a></p>
<p>however, styles are off ( weird color, too much information, etc)</p>
<p>How can i color it to look very much like google maps</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-leaflet" rel="tag" title="see questions tagged &#39;leaflet&#39;">leaflet</span> <span class="post-tag tag-link-style" rel="tag" title="see questions tagged &#39;style&#39;">style</span> <span class="post-tag tag-link-javascript" rel="tag" title="see questions tagged &#39;javascript&#39;">javascript</span> <span class="post-tag tag-link-google_maps" rel="tag" title="see questions tagged &#39;google_maps&#39;">google_maps</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Feb '18, 22:16</strong></p>
<img src="https://secure.gravatar.com/avatar/8afd88ea8f653f95e2588769c2cfab6a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="techsin&#39;s gravatar image" />
<p><span>techsin</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="techsin has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-62063" class="comments-container">
<span id="72593"></span>
<div id="comment-72593" class="comment">
<div id="post-72593-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/14744/techsin">@techsin</a> did you manage to find a way to solve your issue?</p>
</div>
<div id="comment-72593-info" class="comment-info">
<span class="comment-age">(21 Jan '20, 14:25)</span> <span class="comment-user userinfo">Dovlet</span>
</div>
</div>
</div>
<div id="comment-tools-62063" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62063-form-container" class="comment-form-container">
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

<span id="72596"></span>

<div id="answer-container-72596" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72596-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72596-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-72596-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You will need a different tile provider that is serving vector tiles and stylesheet editing. Mapbox or Maptiler both offer the option to style your maps yourself.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Jan '20, 15:35</strong></p>
<img src="https://secure.gravatar.com/avatar/e06ed329df6032df14b5639de4d64782?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Spiekerooger&#39;s gravatar image" />
<p><span>Spiekerooger</span><br />
<span class="score" title="3148 reputation points"><span>3.1k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Spiekerooger has 18 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-72596" class="comments-container">
&#10;</div>
<div id="comment-tools-72596" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72596-form-container" class="comment-form-container">
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

