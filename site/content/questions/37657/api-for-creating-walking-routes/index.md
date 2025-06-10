+++
type = "question"
title = "API for creating walking routes"
description = '''As far as I know OSM doesn&#x27;t support for route drawing. I need an API advice for adding some markers on the map and showing the walking route between them. I work on this area http://www.openstreetmap.org/#map=17/39.86739/32.74832'''
date = "2014-10-16T18:19:00Z"
lastmod = "2014-10-17T16:28:00Z"
weight = 37657
keywords = [ "footpath", "route", "walking", "footway", "drawing" ]
aliases = [ "/questions/37657" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [API for creating walking routes](/questions/37657/api-for-creating-walking-routes)

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
<span id="post-37657-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37657-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-37657-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>As far as I know OSM doesn't support for route drawing.</p>
<p>I need an API advice for adding some markers on the map and showing the walking route between them.</p>
<p>I work on this area <a href="http://www.openstreetmap.org/#map=17/39.86739/32.74832">http://www.openstreetmap.org/#map=17/39.86739/32.74832</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-footpath" rel="tag" title="see questions tagged &#39;footpath&#39;">footpath</span> <span class="post-tag tag-link-route" rel="tag" title="see questions tagged &#39;route&#39;">route</span> <span class="post-tag tag-link-walking" rel="tag" title="see questions tagged &#39;walking&#39;">walking</span> <span class="post-tag tag-link-footway" rel="tag" title="see questions tagged &#39;footway&#39;">footway</span> <span class="post-tag tag-link-drawing" rel="tag" title="see questions tagged &#39;drawing&#39;">drawing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Oct '14, 18:19</strong></p>
<img src="https://secure.gravatar.com/avatar/3f165821043ce0a3ec0bf6199359cfc7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jedilance&#39;s gravatar image" />
<p><span>Jedilance</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jedilance has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-37657" class="comments-container">
<span id="37700"></span>
<div id="comment-37700" class="comment">
<div id="post-37700-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If Ed's answer is not what you want may be this similar one is. <a href="https://help.openstreetmap.org/questions/25135/how-to-manually-create-a-gps-track-for-biking">https://help.openstreetmap.org/questions/25135/how-to-manually-create-a-gps-track-for-biking</a></p>
</div>
<div id="comment-37700-info" class="comment-info">
<span class="comment-age">(17 Oct '14, 15:35)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
</div>
<div id="comment-tools-37657" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37657-form-container" class="comment-form-container">
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

<span id="37658"></span>

<div id="answer-container-37658" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-37658-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37658-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-37658-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I think there are a number of APIs for routing, though not provided by osm.org directly. The <a href="http://jsrouting.apis.dev.openstreetmap.org/directions?engine=mapquest_foot&amp;route=51.8573%2C1.1633%3B51.9037%2C1.1891#map=13/51.8724/1.1814&amp;layers=N">jsrouting development branch</a> includes a number of options, for example.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Oct '14, 18:54</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-37658" class="comments-container">
&#10;</div>
<div id="comment-tools-37658" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37658-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="37702"></span>

<div id="answer-container-37702" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-37702-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37702-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-37702-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If the "markers on a map" part of the question really means "how do I use a javascript library to display information over the top of some existing tiles" then you might find the links from <a href="http://switch2osm.org/using-tiles/">here</a> useful.</p>
<p>It's possible that <a href="https://umap.openstreetmap.fr/en/">uMap</a> might also work for you - have a look at the various links from <a href="https://bitbucket.org/yohanboniface/umap">here</a> and <a href="https://help.openstreetmap.org/questions/21987/how-to-retrieve-my-data-on-my-own-umap-instance-with-api">this previous question</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Oct '14, 16:28</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Oct '14, 16:29</strong> </span></p>
</div>
</div>
<div id="comments-container-37702" class="comments-container">
&#10;</div>
<div id="comment-tools-37702" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37702-form-container" class="comment-form-container">
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

