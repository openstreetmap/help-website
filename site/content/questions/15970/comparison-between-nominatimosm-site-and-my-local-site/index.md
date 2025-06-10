+++
type = "question"
title = "Comparison between nominatim.osm site and my local site"
description = '''Hi! In my nominatim database I have imported first time the netherlands.pbf and then updated the database with belgium.osm, luxembourg.osm and a part of germany (using the boundary box option, which included all the regions from Netherlands at the border with Germany and a little bit of Germany near...'''
date = "2012-09-11T15:31:00Z"
lastmod = "2012-09-12T07:59:00Z"
weight = 15970
keywords = [ "comparison", "region", "nominatim", "missing", "database" ]
aliases = [ "/questions/15970" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Comparison between nominatim.osm site and my local site](/questions/15970/comparison-between-nominatimosm-site-and-my-local-site)

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
<span id="post-15970-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15970-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-15970-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi!</p>
<p>In my nominatim database I have imported first time the netherlands.pbf and then updated the database with belgium.osm, luxembourg.osm and a part of germany (using the boundary box option, which included all the regions from Netherlands at the border with Germany and a little bit of Germany near Netherlands). And then re-index the data.</p>
<p>Does anybody know why in <em>nominatim web search</em> after: [50.822684,5.680662] the result is: <strong>Maarendal - nieuwe groeve, Mergelweg, Maastricht, Province of Limburg, Netherlands, 6213, The Netherlands (Cave Entrance)</strong> and in <em>my local site</em> after the same coordinates, the result is: <strong>Maarendal - nieuwe groeve, Mergelweg, Maastricht, 6213, The Netherlands (Cave Entrance)</strong> ? Is <strong>missing Province of Limburg, Netherlands</strong>?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-comparison" rel="tag" title="see questions tagged &#39;comparison&#39;">comparison</span> <span class="post-tag tag-link-region" rel="tag" title="see questions tagged &#39;region&#39;">region</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-missing" rel="tag" title="see questions tagged &#39;missing&#39;">missing</span> <span class="post-tag tag-link-database" rel="tag" title="see questions tagged &#39;database&#39;">database</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Sep '12, 15:31</strong></p>
<img src="https://secure.gravatar.com/avatar/2f496486f3d04cfe5b6d1d8ce9b660af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RoxanaO&#39;s gravatar image" />
<p><span>RoxanaO</span><br />
<span class="score" title="31 reputation points">31</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RoxanaO has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-15970" class="comments-container">
&#10;</div>
<div id="comment-tools-15970" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15970-form-container" class="comment-form-container">
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

<span id="15976"></span>

<div id="answer-container-15976" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-15976-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15976-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-15976-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Using directly the <a href="http://nominatim.openstreetmap.org">nominatim online site</a>, we can see the detailed report about your coordinates here:<br />
<a href="http://nominatim.openstreetmap.org/details.php?place_id=7685557">http://nominatim.openstreetmap.org/details.php?place_id=7685557</a></p>
<p>The missing "province of Limburg" is reported in Nominatim by the <a href="http://www.openstreetmap.org/browse/relation/47793">relation id 47793</a>. You should check that your database contains this relation. I strongly suspect that the country extracts you are using do not have this administrative boundary in which case the relation is missing in your database, explaining your difference. This is because extractors like Geofabrik use clipboards that do not follow exactly the countries borders. You should download a larger extract like Europe and clip your regions yourself into a single planet extract using <a href="http://wiki.openstreetmap.org/wiki/Osmosis">Osmosis</a> for instance.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Sep '12, 16:57</strong></p>
<img src="https://secure.gravatar.com/avatar/0e92f2d89853fd4e04c4b40a921e519b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pieren&#39;s gravatar image" />
<p><span>Pieren</span><br />
<span class="score" title="9847 reputation points"><span>9.8k</span></span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="157 badges"><span class="bronze">●</span><span class="badgecount">157</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pieren has 34 accepted answers">15%</span> </br></p>
</div>
</div>
<div id="comments-container-15976" class="comments-container">
<span id="15987"></span>
<div id="comment-15987" class="comment">
<div id="post-15987-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I have this relation - 47793 (administrative boundary) in my database. The problem is that for Maastricht I have the parent_place_id 0.</p>
</div>
<div id="comment-15987-info" class="comment-info">
<span class="comment-age">(12 Sep '12, 07:59)</span> <span class="comment-user userinfo">RoxanaO</span>
</div>
</div>
</div>
<div id="comment-tools-15976" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15976-form-container" class="comment-form-container">
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

