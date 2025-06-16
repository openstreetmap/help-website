+++
type = "question"
title = "how to reduce polygon_geojson co-ordinates"
description = '''Hi to all, We can get co-ordinates for a region(city/state/country) using polygon_geojson=1 in nominatim url. It will give large amount of data(co-ordinates) for large regions(example for a country). Now i want to reduce the co-ordinates count. How it is possible?'''
date = "2015-07-09T10:15:00Z"
lastmod = "2019-02-26T15:09:00Z"
weight = 44057
keywords = [ "coordinates", "nominatim", "admin_boundary", "polygon", "geojson" ]
aliases = [ "/questions/44057" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [how to reduce polygon_geojson co-ordinates](/questions/44057/how-to-reduce-polygon_geojson-co-ordinates)

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
<span id="post-44057-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44057-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-44057-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi to all,</p>
<p>We can get co-ordinates for a region(city/state/country) using polygon_geojson=1 in nominatim url. It will give large amount of data(co-ordinates) for large regions(example for a country). Now i want to reduce the co-ordinates count. How it is possible?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-coordinates" rel="tag" title="see questions tagged &#39;coordinates&#39;">coordinates</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-admin_boundary" rel="tag" title="see questions tagged &#39;admin_boundary&#39;">admin_boundary</span> <span class="post-tag tag-link-polygon" rel="tag" title="see questions tagged &#39;polygon&#39;">polygon</span> <span class="post-tag tag-link-geojson" rel="tag" title="see questions tagged &#39;geojson&#39;">geojson</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Jul '15, 10:15</strong></p>
<img src="https://secure.gravatar.com/avatar/1ffa52ca3632b5a0cf02b51459b7529b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rajavelu_M&#39;s gravatar image" />
<p><span>Rajavelu_M</span><br />
<span class="score" title="253 reputation points">253</span><span title="45 badges"><span class="badge1">●</span><span class="badgecount">45</span></span><span title="48 badges"><span class="silver">●</span><span class="badgecount">48</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rajavelu_M has one accepted answer">33%</span></p>
</div>
</div>
<div id="comments-container-44057" class="comments-container">
<span id="44059"></span>
<div id="comment-44059" class="comment">
<div id="post-44059-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Are you asking for an algorithm for simplifying a polygon?</p>
</div>
<div id="comment-44059-info" class="comment-info">
<span class="comment-age">(09 Jul '15, 10:25)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="44060"></span>
<div id="comment-44060" class="comment">
<div id="post-44060-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/158/scai"></a><a href="https://help.openstreetmap.org/users/158/scai">@scai</a>: yes. An algorithm for simplifying a polygon is fine. For example <a href="http://nominatim.openstreetmap.org/search?q=India&amp;polygon_geojson=1&amp;format=json">http://nominatim.openstreetmap.org/search?q=India&amp;polygon_geojson=1&amp;format=json</a> The above url gives 1.5MB data. I want to reduce co-ordinates and the size to around 200kb.</p>
</div>
<div id="comment-44060-info" class="comment-info">
<span class="comment-age">(09 Jul '15, 10:35)</span> <span class="comment-user userinfo">Rajavelu_M</span>
</div>
</div>
<span id="44063"></span>
<div id="comment-44063" class="comment">
<div id="post-44063-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>gpsbabel can <a href="https://wiki.openstreetmap.org/wiki/Using_filters_with_GPSBabel#Simplifying_tracks">simplify tracks</a> which could be an option depending on what you are trying to do.</p>
</div>
<div id="comment-44063-info" class="comment-info">
<span class="comment-age">(09 Jul '15, 11:41)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="44123"></span>
<div id="comment-44123" class="comment">
<div id="post-44123-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>... or try JOSM offline editor (not sure whether it can load geojson, but it has a simplify feature for lines)... or maybe QGIS?</p>
</div>
<div id="comment-44123-info" class="comment-info">
<span class="comment-age">(10 Jul '15, 20:25)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
</div>
<div id="comment-tools-44057" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44057-form-container" class="comment-form-container">
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

<span id="68161"></span>

<div id="answer-container-68161" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68161-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68161-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-68161-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I was trying to do the same and found that using param polygon_threshold=0.009 is usefull</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Feb '19, 15:09</strong></p>
<img src="https://secure.gravatar.com/avatar/47d77f38a7c24a48cdaf9476db8670a1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="shaniqwa&#39;s gravatar image" />
<p><span>shaniqwa</span><br />
<span class="score" title="16 reputation points">16</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="shaniqwa has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-68161" class="comments-container">
&#10;</div>
<div id="comment-tools-68161" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68161-form-container" class="comment-form-container">
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

