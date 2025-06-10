+++
type = "question"
title = "Where can I find description of the database structure &quot;Nominatim&quot;?"
description = '''For example, I want decrease the database size. I need to geocode only to the level of the village or town. Can I remove some not usefull data from planet.osm.pbf or from geodatabase &quot;Nominatim&quot;? I do not need streets, suburbs, buildings, etc. So I want remove this data from database or .osm.pbf. Th...'''
date = "2013-12-18T07:25:00Z"
lastmod = "2016-05-05T12:40:00Z"
weight = 29154
keywords = [ "geocoding", "editing", "nominatim", "postgresql", "description" ]
aliases = [ "/questions/29154" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Where can I find description of the database structure "Nominatim"?](/questions/29154/where-can-i-find-description-of-the-database-structure-nominatim)

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
<span id="post-29154-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29154-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-29154-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>For example, I want decrease the database size. I need to geocode only to the level of the village or town. Can I remove some not usefull data from planet.osm.pbf or from geodatabase "Nominatim"? I do not need streets, suburbs, buildings, etc. So I want remove this data from database or .osm.pbf.</p>
<p>The structure of geodatabase "Nominatim" is quite difficult, so I think that the best way is to change osm.pbf file. But I don't know how.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-geocoding" rel="tag" title="see questions tagged &#39;geocoding&#39;">geocoding</span> <span class="post-tag tag-link-editing" rel="tag" title="see questions tagged &#39;editing&#39;">editing</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-description" rel="tag" title="see questions tagged &#39;description&#39;">description</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Dec '13, 07:25</strong></p>
<img src="https://secure.gravatar.com/avatar/aea8cdb05518a630ebad09bd7c777dc3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="amshegar&#39;s gravatar image" />
<p><span>amshegar</span><br />
<span class="score" title="46 reputation points">46</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="amshegar has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-29154" class="comments-container">
<span id="49578"></span>
<div id="comment-49578" class="comment">
<div id="post-49578-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Yes I'd like to see some docs for the DB schema, or just an overview explanation of some of the main database structures of nominatim (AKA the osm2pgsql "gazetteer mode" output?). I thought it would be fairly easy to do geo queries on the nominatim db directly, but the structure is surprisingly "difficult" as you say. I figured out some queries I can do. See my adventures so far here: <a href="http://wiki.openstreetmap.org/wiki/Talk:Nominatim/Development_overview">http://wiki.openstreetmap.org/wiki/Talk:Nominatim/Development_overview</a></p>
</div>
<div id="comment-49578-info" class="comment-info">
<span class="comment-age">(05 May '16, 12:40)</span> <span class="comment-user userinfo">Harry Wood</span>
</div>
</div>
</div>
<div id="comment-tools-29154" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29154-form-container" class="comment-form-container">
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

<span id="29167"></span>

<div id="answer-container-29167" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-29167-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29167-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-29167-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is currently no DB schema description of Nominatim available: <a href="http://wiki.openstreetmap.org/wiki/Category:Nominatim">http://wiki.openstreetmap.org/wiki/Category:Nominatim</a></p>
<p>So you might ask at the OSM-TALK or OSM-DEV <a href="http://wiki.openstreetmap.org/wiki/Mailing_lists">mailinglist</a> or in wiki at the <a href="http://wiki.openstreetmap.org/wiki/Talk:Nominatim">Nominatim disc</a>. A documentation at the wiki would be nice for the community :)</p>
<p>Maybe it's easier to <strong>export your dump</strong> to preprocessed <a href="http://wiki.openstreetmap.org/wiki/Nominatim/Structured">nomiatim NPI files</a> and filter this files before reimporting to get a light DB?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Dec '13, 15:29</strong></p>
<img src="https://secure.gravatar.com/avatar/49a7d0e0408e9cf2f698faac0f4d837a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iii&#39;s gravatar image" />
<p><span>iii</span><br />
<span class="score" title="4892 reputation points"><span>4.9k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="40 badges"><span class="silver">●</span><span class="badgecount">40</span></span><span title="82 badges"><span class="bronze">●</span><span class="badgecount">82</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="iii has 16 accepted answers">10%</span></p>
</div>
</div>
<div id="comments-container-29167" class="comments-container">
<span id="29709"></span>
<div id="comment-29709" class="comment">
<div id="post-29709-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the answer. Can you tell me how convert postgresql database "Nominatim" to the nominatim pre-indexed file?</p>
</div>
<div id="comment-29709-info" class="comment-info">
<span class="comment-age">(09 Jan '14, 10:24)</span> <span class="comment-user userinfo">amshegar</span>
</div>
</div>
<span id="29713"></span>
<div id="comment-29713" class="comment">
<div id="post-29713-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Also I have read that NPI service is currently being deprecated. So I can not download NPI file from MapQuest...</p>
</div>
<div id="comment-29713-info" class="comment-info">
<span class="comment-age">(09 Jan '14, 12:09)</span> <span class="comment-user userinfo">amshegar</span>
</div>
</div>
</div>
<div id="comment-tools-29167" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29167-form-container" class="comment-form-container">
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

