+++
type = "question"
title = "osmfilter to extract all admin boundaries as areas and all places as dots"
description = '''Before importing a huge world osm file with using osm2pgsql, I was recommended to use osmfilter to filter the input file down first. So that an osm file used for import only contains data that I need. The final goal is to get all admin boundaries as areas, and all places as dots (like cities, villag...'''
date = "2017-07-03T11:15:00Z"
lastmod = "2017-07-03T23:11:00Z"
weight = 56848
keywords = [ "osmfilter" ]
aliases = [ "/questions/56848" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [osmfilter to extract all admin boundaries as areas and all places as dots](/questions/56848/osmfilter-to-extract-all-admin-boundaries-as-areas-and-all-places-as-dots)

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
<span id="post-56848-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56848-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-56848-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Before importing a huge <code>world</code> osm file with using <code>osm2pgsql</code>, I was recommended to use <code>osmfilter</code> to filter the input file down first. So that an osm file used for import only contains data that I need.</p>
<p>The final goal is to get all admin boundaries as areas, and all places as dots (like cities, villages, suburbs and so on). This data will be used in the following way:</p>
<ul>
<li>admin boundaries are used to render a very simple map of a particular country (infographics)</li>
<li>places are used to put cities (as dots) on that map</li>
</ul>
<p>That's basically all we need from the data.</p>
<p>We would like to automated populating data, so using <code>osmtools</code> sounds okay.</p>
<p>Тow, if the first stage is to filter down the big OSM file, what's the best configuration to only have data described above and nothing else? So that the final database is of small size and can be queried very fastly.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmfilter" rel="tag" title="see questions tagged &#39;osmfilter&#39;">osmfilter</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Jul '17, 11:15</strong></p>
<img src="https://secure.gravatar.com/avatar/c9a1577cedad5cf1af59379a5bd6721b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="meglio&#39;s gravatar image" />
<p><span>meglio</span><br />
<span class="score" title="40 reputation points">40</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="meglio has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-56848" class="comments-container">
&#10;</div>
<div id="comment-tools-56848" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56848-form-container" class="comment-form-container">
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

<span id="56862"></span>

<div id="answer-container-56862" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56862-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56862-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-56862-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I don't know how to do that with osmfilter. But with <a href="http://osmcode.org/osmium-tool/">Osmium</a> it is simple:</p>
<pre><code>osmium tags-filter planet.osm.pbf n/place=city r/type=boundary -o filtered.osm.pbf</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Jul '17, 18:03</strong></p>
<img src="https://secure.gravatar.com/avatar/2d4dfcdcde73aa5e2ffa4a9b3a7cb51d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jochen%20Topf&#39;s gravatar image" />
<p><span>Jochen Topf</span><br />
<span class="score" title="5244 reputation points"><span>5.2k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jochen Topf has 32 accepted answers">31%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Jul '17, 18:03</strong> </span></p>
</div>
</div>
<div id="comments-container-56862" class="comments-container">
<span id="56864"></span>
<div id="comment-56864" class="comment">
<div id="post-56864-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks <a href="https://help.openstreetmap.org/users/112/jochen-topf">@Jochen</a>. In some cases, places can be represented as boundaries; in other cases, they can be represented as nodes. Is there any way to get only dots (nodes) and never boundaries for all my filtered places?</p>
</div>
<div id="comment-56864-info" class="comment-info">
<span class="comment-age">(03 Jul '17, 23:11)</span> <span class="comment-user userinfo">meglio</span>
</div>
</div>
</div>
<div id="comment-tools-56862" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56862-form-container" class="comment-form-container">
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

