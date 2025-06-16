+++
type = "question"
title = "Filter Nominatim results"
description = '''I want to implement an auto-complete search feature in my website, but it should only return municipalities (admin_level=&quot;8&quot;). Is there a way to filter for this using the Nominatim API? Or should I use osmosis and cross-check the results? E.g, &#x27;Utrecht&#x27; returns the province, the city, etc, but I onl...'''
date = "2013-02-03T11:06:00Z"
lastmod = "2013-02-03T18:24:00Z"
weight = 19551
keywords = [ "filter", "nominatim", "municipality" ]
aliases = [ "/questions/19551" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Filter Nominatim results](/questions/19551/filter-nominatim-results)

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
<span id="post-19551-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19551-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-19551-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to implement an auto-complete search feature in my website, but it should only return municipalities (admin_level="8"). Is there a way to filter for this using the Nominatim API? Or should I use osmosis and cross-check the results?</p>
<p>E.g, 'Utrecht' returns the province, the city, etc, but I only want the municipality. <a href="http://nominatim.openstreetmap.org/search?q=utrecht&amp;format=json&amp;countrycodes=nl">http://nominatim.openstreetmap.org/search?q=utrecht&amp;format=json&amp;countrycodes=nl</a></p>
<p>If I have to use osmosis, how would I go about it?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-municipality" rel="tag" title="see questions tagged &#39;municipality&#39;">municipality</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Feb '13, 11:06</strong></p>
<img src="https://secure.gravatar.com/avatar/01a15e676e981786748ca533fac0fc31?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ocky7&#39;s gravatar image" />
<p><span>ocky7</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ocky7 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Feb '13, 16:28</strong> </span></p>
</div>
</div>
<div id="comments-container-19551" class="comments-container">
<span id="19555"></span>
<div id="comment-19555" class="comment">
<div id="post-19555-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Also check out <a href="/questions/2980/how-do-i-list-all-the-streets-in-a-city-with-nominatim">this question</a>.</p>
</div>
<div id="comment-19555-info" class="comment-info">
<span class="comment-age">(03 Feb '13, 18:24)</span> <span class="comment-user userinfo">ocky7</span>
</div>
</div>
</div>
<div id="comment-tools-19551" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19551-form-container" class="comment-form-container">
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

<span id="19554"></span>

<div id="answer-container-19554" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-19554-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19554-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-19554-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I downloaded my country extract from <a href="http://download.geofabrik.de/">Geofabrik</a>. Then I ran the following osmosis command on the downloaded osm.pbf file:</p>
<pre><code>$ osmosis --read-pbf file=netherlands.osm.pbf --bounding-box left=4 right=5 top=54 bottom=50 --way-key-value value keyValueList=admin_level.8 --tag-filter reject-nodes --tag-filter reject-relations --write-xml municipalities_nl.osm</code></pre>
<p>Which generates an OSM XML file with all the municipality ways. Although I'd like the related polygons as well.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Feb '13, 18:14</strong></p>
<img src="https://secure.gravatar.com/avatar/01a15e676e981786748ca533fac0fc31?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ocky7&#39;s gravatar image" />
<p><span>ocky7</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ocky7 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Feb '13, 20:17</strong> </span></p>
</div>
</div>
<div id="comments-container-19554" class="comments-container">
&#10;</div>
<div id="comment-tools-19554" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19554-form-container" class="comment-form-container">
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

