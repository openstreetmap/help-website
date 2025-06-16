+++
type = "question"
title = "How do I download all schools from OSM?"
description = '''How would I best obtain all the schools (amenity=school) in the OSM database? This question asks how to do it for a specific location: https://help.openstreetmap.org/questions/11004/download-a-map-and-extract-position-from-places-like-schools-hospitals-etc And the answer is the use the Overpass API ...'''
date = "2018-09-05T16:57:00Z"
lastmod = "2018-09-06T01:08:00Z"
weight = 65762
keywords = [ "download", "amenity", "school" ]
aliases = [ "/questions/65762" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How do I download all schools from OSM?](/questions/65762/how-do-i-download-all-schools-from-osm)

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
<span id="post-65762-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65762-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65762-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How would I best obtain all the schools (amenity=school) in the OSM database?</p>
<p>This question asks how to do it for a specific location: <a href="/questions/11004/download-a-map-and-extract-position-from-places-like-schools-hospitals-etc">https://help.openstreetmap.org/questions/11004/download-a-map-and-extract-position-from-places-like-schools-hospitals-etc</a></p>
<p>And the answer is the use the Overpass API or XAPI.</p>
<p>In my case, I want <em>all</em> the schools. The following is a question along those lines: <a href="/questions/13827/download-amenities">https://help.openstreetmap.org/questions/13827/download-amenities</a></p>
<p>However it dates back to 2012, and the most upvoted answer recommends to download a full planet dump (tens to hundreds of gigs) and retrieve what you want using a tool like Osmosis or OSMFilter.</p>
<p>Is there a better way?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-download" rel="tag" title="see questions tagged &#39;download&#39;">download</span> <span class="post-tag tag-link-amenity" rel="tag" title="see questions tagged &#39;amenity&#39;">amenity</span> <span class="post-tag tag-link-school" rel="tag" title="see questions tagged &#39;school&#39;">school</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Sep '18, 16:57</strong></p>
<img src="https://secure.gravatar.com/avatar/73c98df240b6e2e52164347a040fca82?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mitchus&#39;s gravatar image" />
<p><span>mitchus</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mitchus has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Sep '18, 17:14</strong> </span></p>
</div>
</div>
<div id="comments-container-65762" class="comments-container">
&#10;</div>
<div id="comment-tools-65762" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65762-form-container" class="comment-form-container">
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

<span id="65763"></span>

<div id="answer-container-65763" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-65763-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65763-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-65763-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="mitchus has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you need all the school data (~1 million of uses around the world), downloading planet file in PBF, which is only ~40 GB (not hundreds), and filtering them is the best option. Overpass has limits and might slow down your browser with such amount of data.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Sep '18, 18:08</strong></p>
<img src="https://secure.gravatar.com/avatar/e228dd20b7da2a6c8f559e2118ce08d3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kocio&#39;s gravatar image" />
<p><span>kocio</span><br />
<span class="score" title="2054 reputation points"><span>2.1k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kocio has 14 accepted answers">20%</span></p>
</div>
</div>
<div id="comments-container-65763" class="comments-container">
<span id="65767"></span>
<div id="comment-65767" class="comment">
<div id="post-65767-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>After having downloaded the planet file, you could now use the Osmium command line tool (which wasn't available in 2012) to filter out the schools you are interested in. You have a big request and you need to be prepared to put a little bit of work in - OSM gives you all the data for free but it can't afford to give you the processing for free too.</p>
</div>
<div id="comment-65767-info" class="comment-info">
<span class="comment-age">(05 Sep '18, 20:01)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="65772"></span>
<div id="comment-65772" class="comment">
<div id="post-65772-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>See the examples in documentation:</p>
<p><a href="https://osmcode.org/osmium-tool/manual.html#filtering-by-tags">https://osmcode.org/osmium-tool/manual.html#filtering-by-tags</a></p>
</div>
<div id="comment-65772-info" class="comment-info">
<span class="comment-age">(05 Sep '18, 23:26)</span> <span class="comment-user userinfo">kocio</span>
</div>
</div>
<span id="65773"></span>
<div id="comment-65773" class="comment">
<div id="post-65773-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Note that you can use curl or wget whatever to retrieve a result from Overpass-API. Then the server limitations are likely to be the only issue.</p>
<p>Still, for global results Overpass-API is unlikely to be the right approach.</p>
</div>
<div id="comment-65773-info" class="comment-info">
<span class="comment-age">(06 Sep '18, 01:08)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
</div>
<div id="comment-tools-65763" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65763-form-container" class="comment-form-container">
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

