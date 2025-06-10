+++
type = "question"
title = "How to map Scrap Metaller"
description = ''' Identified a metal recycler which does not scrap automobiles, as far as I can tell. It is also not a general purpose recycling center. Having trouble finding the right tags for OSM. What do you think? With the cost of metals going up all the time, these types of places are getting more popular. Loc...'''
date = "2016-08-22T12:34:00Z"
lastmod = "2016-08-23T07:02:00Z"
weight = 51641
keywords = [ "industrial", "recycling", "scrap_metal", "tagging" ]
aliases = [ "/questions/51641" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How to map Scrap Metaller](/questions/51641/how-to-map-scrap-metaller)

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
<span id="post-51641-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51641-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-51641-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p><img src="http://help.openstreetmap.org/upfiles/metal.jpeg" alt="alt text" /> Identified a metal recycler which does not scrap automobiles, as far as I can tell. It is also not a general purpose recycling center. Having trouble finding the right tags for OSM. What do you think? With the cost of metals going up all the time, these types of places are getting more popular. <a href="http://www.openstreetmap.org/#map=17/43.06043/-70.75978">Location on the map - change to satellite view...</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-industrial" rel="tag" title="see questions tagged &#39;industrial&#39;">industrial</span> <span class="post-tag tag-link-recycling" rel="tag" title="see questions tagged &#39;recycling&#39;">recycling</span> <span class="post-tag tag-link-scrap_metal" rel="tag" title="see questions tagged &#39;scrap_metal&#39;">scrap_metal</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Aug '16, 12:34</strong></p>
<img src="https://secure.gravatar.com/avatar/cb68523a12e3580728c6bee495ae602e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtc&#39;s gravatar image" />
<p><span>mtc</span><br />
<span class="score" title="411 reputation points">411</span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="29 badges"><span class="bronze">●</span><span class="badgecount">29</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtc has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Aug '16, 12:41</strong> </span></p>
</div>
</div>
<div id="comments-container-51641" class="comments-container">
&#10;</div>
<div id="comment-tools-51641" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51641-form-container" class="comment-form-container">
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

<span id="51655"></span>

<div id="answer-container-51655" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-51655-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51655-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-51655-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="mtc has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>it is a recycling centre, but just accepts one type of resource. Tag it (the whole area) like this:</p>
<ul>
<li><code>amenity=recycling</code></li>
<li><code>recycling_type=centre</code></li>
<li><code>recycling:metal=yes</code></li>
<li><code>recycling:scrap_metal=yes</code></li>
<li><code>operator=Wentworth</code></li>
<li><code>description=metal recycler which does not scrap automobiles, as far as I can tell. It is also not a general purpose recycling center.</code></li>
</ul>
<p>See <a href="https://wiki.openstreetmap.org/wiki/Tag:amenity%3Drecycling">https://wiki.openstreetmap.org/wiki/Tag:amenity%3Drecycling</a> for details.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Aug '16, 21:27</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Aug '16, 21:27</strong> </span></p>
</div>
</div>
<div id="comments-container-51655" class="comments-container">
<span id="51665"></span>
<div id="comment-51665" class="comment">
<div id="post-51665-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Just to clarify: Instead of just a node <a href="https://www.openstreetmap.org/node/4362278779">https://www.openstreetmap.org/node/4362278779</a> (which does not transport information about the feature's size), I would draw a closed line on the outline of the scrap yard and tag it instead (<a href="https://www.openstreetmap.org/way/297027718">example</a>). It is well visible on the aerial imagery.</p>
</div>
<div id="comment-51665-info" class="comment-info">
<span class="comment-age">(23 Aug '16, 07:02)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-51655" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51655-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="51644"></span>

<div id="answer-container-51644" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-51644-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51644-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-51644-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi have a look at the amenity menu, choose recycling=container, operator=Wentworth Scrap metal and what’s goes into the container below details, for instance scrap metal=yes. Or ad the almost the same specs to the yard if it’s in use as recycling_centre as well. He could accept appliances and aluminium as well.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Aug '16, 14:02</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Aug '16, 14:05</strong> </span></p>
</div>
</div>
<div id="comments-container-51644" class="comments-container">
&#10;</div>
<div id="comment-tools-51644" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51644-form-container" class="comment-form-container">
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

