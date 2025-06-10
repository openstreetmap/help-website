+++
type = "question"
title = "How to see the alt/long of a point on the map?"
description = '''Older answers do point to non-existing solutions, that is why I put this question again. '''
date = "2017-12-28T08:53:00Z"
lastmod = "2017-12-28T22:07:00Z"
weight = 61392
keywords = [ "latitude" ]
aliases = [ "/questions/61392" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to see the alt/long of a point on the map?](/questions/61392/how-to-see-the-altlong-of-a-point-on-the-map)

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
<span id="post-61392-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61392-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-61392-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Older answers do point to non-existing solutions, that is why I put this question again.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-latitude" rel="tag" title="see questions tagged &#39;latitude&#39;">latitude</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Dec '17, 08:53</strong></p>
<img src="https://secure.gravatar.com/avatar/fda17550d196ab0b133fe317391d1ad0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap12soft&#39;s gravatar image" />
<p><span>Jaap12soft</span><br />
<span class="score" title="56 reputation points">56</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap12soft has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-61392" class="comments-container">
&#10;</div>
<div id="comment-tools-61392" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61392-form-container" class="comment-form-container">
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

<span id="61395"></span>

<div id="answer-container-61395" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-61395-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61395-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-61395-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>For nodes it's quite easy - just look at the data of the object and there it is in the header (just before tags), for example:</p>
<p><a href="http://www.openstreetmap.org/node/240866019">http://www.openstreetmap.org/node/240866019</a></p>
<p>50,8449819, 4,3499862</p>
<p>For ways and relations it's simply not available, since they are just the lists of nodes, each with its own lat/lon, so you would have to find centroid, but there's no single method to calculate this.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Dec '17, 09:36</strong></p>
<img src="https://secure.gravatar.com/avatar/e228dd20b7da2a6c8f559e2118ce08d3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kocio&#39;s gravatar image" />
<p><span>kocio</span><br />
<span class="score" title="2054 reputation points"><span>2.1k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kocio has 14 accepted answers">20%</span></p>
</div>
</div>
<div id="comments-container-61395" class="comments-container">
&#10;</div>
<div id="comment-tools-61395" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61395-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="61396"></span>

<div id="answer-container-61396" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-61396-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61396-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-61396-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>thanks for answer.. Put the mouse cursor on a point on the map, click right, choose Center Map Here. In the URL you should see Alt Long like this: www.opens......lat=52.8915&amp;lon=5.0677#map=16/52.8906/5.0676</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Dec '17, 10:50</strong></p>
<img src="https://secure.gravatar.com/avatar/fda17550d196ab0b133fe317391d1ad0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap12soft&#39;s gravatar image" />
<p><span>Jaap12soft</span><br />
<span class="score" title="56 reputation points">56</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap12soft has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-61396" class="comments-container">
<span id="61399"></span>
<div id="comment-61399" class="comment">
<div id="post-61399-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>One remark, it's not Alt, but Lat, shorthand for Latitude. Alt is Altitude (ie. height above sea level).</p>
</div>
<div id="comment-61399-info" class="comment-info">
<span class="comment-age">(28 Dec '17, 17:47)</span> <span class="comment-user userinfo">RicoElectrico</span>
</div>
</div>
<span id="61403"></span>
<div id="comment-61403" class="comment">
<div id="post-61403-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Note South and West are negative values for example <a href="https://www.openstreetmap.org/#map=7/-0.753/-90.934">https://www.openstreetmap.org/#map=7/-0.753/-90.934</a> i sometimes put lat lon values into my car Sat Nav which easier if i have searched for a location on OSM and i do not have full address information</p>
</div>
<div id="comment-61403-info" class="comment-info">
<span class="comment-age">(28 Dec '17, 21:59)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="61404"></span>
<div id="comment-61404" class="comment">
<div id="post-61404-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You may be able to configure your Sat Nav to decimal degrees which is much easier than having to convert OSMs degrees decimal to degrees minutes and seconds.</p>
</div>
<div id="comment-61404-info" class="comment-info">
<span class="comment-age">(28 Dec '17, 22:07)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
</div>
<div id="comment-tools-61396" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61396-form-container" class="comment-form-container">
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

