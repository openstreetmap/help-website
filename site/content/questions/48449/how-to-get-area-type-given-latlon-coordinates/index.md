+++
type = "question"
title = "How to get area type given lat/lon coordinates ?"
description = '''Hi - sorry if this question seems stupid.  Given a lat/lon coordinates, I&#x27;d like to known if the point is in a lake, in a forest or on an highway for instance. Nominatim geocoding gives me the nearest node thus it does not really answer my need. What&#x27;s the right way / tool to use to get that ? Thank...'''
date = "2016-03-02T13:23:00Z"
lastmod = "2016-03-02T16:49:00Z"
weight = 48449
keywords = [ "reversegeocoding", "geocoding", "coordinates", "area" ]
aliases = [ "/questions/48449" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to get area type given lat/lon coordinates ?](/questions/48449/how-to-get-area-type-given-latlon-coordinates)

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
<span id="post-48449-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48449-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-48449-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi -</p>
<p>sorry if this question seems stupid. Given a lat/lon coordinates, I'd like to known if the point is in a lake, in a forest or on an highway for instance.</p>
<p>Nominatim geocoding gives me the nearest node thus it does not really answer my need.</p>
<p>What's the right way / tool to use to get that ?</p>
<p>Thanks a lot for your help</p>
<p>-- david</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-reversegeocoding" rel="tag" title="see questions tagged &#39;reversegeocoding&#39;">reversegeocoding</span> <span class="post-tag tag-link-geocoding" rel="tag" title="see questions tagged &#39;geocoding&#39;">geocoding</span> <span class="post-tag tag-link-coordinates" rel="tag" title="see questions tagged &#39;coordinates&#39;">coordinates</span> <span class="post-tag tag-link-area" rel="tag" title="see questions tagged &#39;area&#39;">area</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Mar '16, 13:23</strong></p>
<img src="https://secure.gravatar.com/avatar/878fd3d25e7dd8ba8c0fb59e7e450587?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dmercier90&#39;s gravatar image" />
<p><span>dmercier90</span><br />
<span class="score" title="76 reputation points">76</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dmercier90 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Mar '16, 14:30</strong> </span></p>
</div>
</div>
<div id="comments-container-48449" class="comments-container">
&#10;</div>
<div id="comment-tools-48449" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48449-form-container" class="comment-form-container">
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

<span id="48450"></span>

<div id="answer-container-48450" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48450-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48450-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-48450-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="dmercier90 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is exactly what "query feature" on the <a href="http://osm.org/">http://osm.org/</a> map does, using <a href="http://wiki.openstreetmap.org/wiki/Overpass_turbo">Overpass Turbo</a>:</p>
<pre><code>[timeout:5][out:json];is_in(lat,lon)-&gt;.a;way(pivot.a);out tags geom({{bbox}});relation(pivot.a);out tags bb;</code></pre>
<p>Where you need to replace <code>lon</code> and <code>lat</code> with the coordinates of the point, and replace <code>{{bbox}}</code> by the current map bounding box (if you need that). This gives you the elements <em>surrounding</em> the given point. Note that this also returns administrative boundaries (county, state, etc.), not just physical elements - you'd need to filter on this, perhaps by throwing away <code>boundary</code> relations etc. See e.g. <a href="http://overpass-api.de/api/convert?data=%5Btimeout%3A5%5D%5Bout%3Ajson%5D%3Bis_in(50.08417%2C14.35882)-%3E.a%3Bway(pivot.a)%3Bout%20tags%20geom(50.08157175512576%2C14.357349872589111%2C50.08436684351692%2C14.374194145202637)%3Brelation(pivot.a)%3Bout%20tags%20bb%3B&amp;target=compact">this query</a> - note that the largest enclosing feature is the entire country.</p>
<p>Also, this will give you <em>enclosing</em> features - so for a highway (which is usually an unclosed way), you wouldn't get a usable result. For that, you may need the other query, "nearby features":</p>
<pre><code>[timeout:5][out:json];(node(around:radius,lat,lon);way(around:radius,lat,lon));out tags geom({{bbox}});relation(around:radius,lat,lon);out geom({{bbox}});</code></pre>
<p>Again, you need to replace <code>lon</code>,<code>lat</code>,<code>{{bbox}}</code>, and in addition <code>radius</code> (how far from the point to look, not sure of the unit) with your data. See e.g. <a href="http://overpass-api.de/api/interpreter?data=%5Bout%3Ajson%5D%5Btimeout%3A5%5D%3B%28node%28around%3A35%2C50%2E08417%2C14%2E35882%29%3Bway%28around%3A35%2C50%2E08417%2C14%2E35882%29%3B%29%3Bout%20tags%20geom%2850%2E0824805209559%2C14%2E355810284614563%2C50%2E08604657192704%2C14%2E362789392471315%29%3Brelation%28around%3A22%2E5%2C50%2E08417%2C14%2E35882%29%3Bout%20body%20geom%2850%2E0824805209559%2C14%2E355810284614563%2C50%2E08604657192704%2C14%2E362789392471315%29%3B%0A">this query</a> - note that by setting the radius too high, there will be many objects; but with a radius too low, there may not be anything found. Depending on your goal, perhaps you might want to start out small and increase the radius in a few steps.</p>
<p>Pay attention also to the freshness data returned with results - Overpass uses its own cache, and updates it from the main db; this can sometimes take <em>days</em>, so newest edits may not be returned in the results immediately.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Mar '16, 14:44</strong></p>
<img src="https://secure.gravatar.com/avatar/8200fa5c0cc8feb096558c5972a6191c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Piskvor&#39;s gravatar image" />
<p><span>Piskvor</span><br />
<span class="score" title="1266 reputation points"><span>1.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="35 badges"><span class="bronze">●</span><span class="badgecount">35</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Piskvor has 9 accepted answers">37%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Mar '16, 16:51</strong> </span></p>
</div>
</div>
<div id="comments-container-48450" class="comments-container">
<span id="48451"></span>
<div id="comment-48451" class="comment">
<div id="post-48451-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks a lot for your fast answer Piskvor !</p>
<p>I'm going to have a look at Overpass, it seems it will help for sure. Btw I didn't found any access to overpass API from <a href="http://osm.org">http://osm.org</a>, maybe something's missing me or I didn't understand. As far as I know osm.org reverse geocoding is using Nominatim, not Overpass.</p>
<p>Example queries you have provided will be very usefull, thanks again.</p>
</div>
<div id="comment-48451-info" class="comment-info">
<span class="comment-age">(02 Mar '16, 15:00)</span> <span class="comment-user userinfo">dmercier90</span>
</div>
</div>
<span id="48452"></span>
<div id="comment-48452" class="comment">
<div id="post-48452-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Overpass is accessed when you use the "Query features" tool, the "?" at the bottom of the right button bar.</p>
</div>
<div id="comment-48452-info" class="comment-info">
<span class="comment-age">(02 Mar '16, 15:11)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
<span id="48454"></span>
<div id="comment-48454" class="comment">
<div id="post-48454-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks Maxerickson, I'm going to change my glasses :)</p>
</div>
<div id="comment-48454-info" class="comment-info">
<span class="comment-age">(02 Mar '16, 15:24)</span> <span class="comment-user userinfo">dmercier90</span>
</div>
</div>
<span id="48455"></span>
<div id="comment-48455" class="comment">
<div id="post-48455-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>To correct answer, it seems is_in takes (lat,lon), not (lon,lat)</p>
</div>
<div id="comment-48455-info" class="comment-info">
<span class="comment-age">(02 Mar '16, 16:27)</span> <span class="comment-user userinfo">dmercier90</span>
</div>
</div>
<span id="48456"></span>
<div id="comment-48456" class="comment">
<div id="post-48456-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, good catch! Silly me, edited.</p>
</div>
<div id="comment-48456-info" class="comment-info">
<span class="comment-age">(02 Mar '16, 16:49)</span> <span class="comment-user userinfo">Piskvor</span>
</div>
</div>
</div>
<div id="comment-tools-48450" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48450-form-container" class="comment-form-container">
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

