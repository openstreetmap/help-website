+++
type = "question"
title = "Speed up slow &quot;around&quot; query for osm api python 3"
description = '''Hi there! Very new to using OSM and have read the docs but still am not sure about the use. I am trying to match latitude and longitude coordinates to a road (any kind under the &quot;highway&quot;). But each is taking 1 second and I have about 1 million coordinates to check. What is the best approach to spee...'''
date = "2019-02-08T02:32:00Z"
lastmod = "2019-02-08T08:17:00Z"
weight = 67931
keywords = [ "python", "overpass", "around", "highway" ]
aliases = [ "/questions/67931" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Speed up slow "around" query for osm api python 3](/questions/67931/speed-up-slow-around-query-for-osm-api-python-3)

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
<span id="post-67931-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67931-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-67931-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi there! Very new to using OSM and have read the docs but still am not sure about the use.</p>
<p>I am trying to match latitude and longitude coordinates to a road (any kind under the "highway"). But each is taking 1 second and I have about 1 million coordinates to check. What is the best approach to speed things up? If my current approach is completely wrong, please advise on how I should do so!</p>
<p>Unsure on how to get the bbox for the countries I am looking at(only 2) and I've downloaded the .osm files but unsure how to use them.</p>
<p>Currently using the following(c1 and c2 are the coordinates):</p>
<pre><code>api = overpass.API()
qur = &#39;way[&quot;highway&quot;~&quot;.&quot;](around:10,&#39; + c1 + &#39;, &#39;+ c2 +&#39;);&#39; 
data = api.get(qur, verbosity=&#39;geom&#39;)</code></pre>
<p>Thank you!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-python" rel="tag" title="see questions tagged &#39;python&#39;">python</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-around" rel="tag" title="see questions tagged &#39;around&#39;">around</span> <span class="post-tag tag-link-highway" rel="tag" title="see questions tagged &#39;highway&#39;">highway</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Feb '19, 02:32</strong></p>
<img src="https://secure.gravatar.com/avatar/f8530252a39bc017965730eaca4c806b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hellu&#39;s gravatar image" />
<p><span>hellu</span><br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hellu has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Feb '19, 06:13</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-67931" class="comments-container">
&#10;</div>
<div id="comment-tools-67931" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67931-form-container" class="comment-form-container">
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

<span id="67934"></span>

<div id="answer-container-67934" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-67934-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67934-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-67934-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Running a million requests against the Overpass API will get you blocked. Don't do it. The project gives away its data for free, but we have to pay for servers like everyone else does, and checking your one million coordinates for you is not an appropriate use of our server resources.</p>
<p>Also, Nominatim (the geocoder) seems like a much better match for your problem than Overpass, though the same usage restrictions apply.</p>
<p>What you should be doing is setting up your own database, and then querying that. Most likely you'll want to set up a local Nominatim instance, though if you're not interested in administrative entities and really just want the name of the nearest road, a simplified <code>osm2pgsql</code> import and some SQL queries might also be an option. If you set up your own database locally, you'll save a lot of time in network round-trips alone, and you don't compete against other users of the system. If your coordinates are all in the same region or country, you don't even have to load a world-wide data set which will speed up things even further.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Feb '19, 06:52</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Feb '19, 06:53</strong> </span></p>
</div>
</div>
<div id="comments-container-67934" class="comments-container">
<span id="67935"></span>
<div id="comment-67935" class="comment">
<div id="post-67935-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Hi! thanks for the heads up. just to confirm, I should be following this <a href="http://nominatim.org/release-docs/latest/admin/Installation/">http://nominatim.org/release-docs/latest/admin/Installation/</a> to set up my own Nominatim server? and the dataset would the the &lt;countryname&gt;-latest.osm.pbf file?</p>
</div>
<div id="comment-67935-info" class="comment-info">
<span class="comment-age">(08 Feb '19, 07:21)</span> <span class="comment-user userinfo">hellu</span>
</div>
</div>
<span id="67937"></span>
<div id="comment-67937" class="comment">
<div id="post-67937-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes that should work. As I said, depending on what exactly your problem is, other approaches might also work but a standard Nominatim install is certainly a good start.</p>
</div>
<div id="comment-67937-info" class="comment-info">
<span class="comment-age">(08 Feb '19, 08:17)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-67934" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67934-form-container" class="comment-form-container">
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

