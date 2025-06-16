+++
type = "question"
title = "Search Results Description"
description = '''I just got my first nominatim instance up and running! Very exciting. I&#x27;ve written a little PHP script to just return the results from Geocode.lookup(). Could someone explain what some of these parameters mean? I couldn&#x27;t find a complete explanation on the wiki. In particular, I&#x27;ve noted the ones I&#x27;...'''
date = "2013-11-06T13:15:00Z"
lastmod = "2013-11-23T12:16:00Z"
weight = 27852
keywords = [ "nominatim" ]
aliases = [ "/questions/27852" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Search Results Description](/questions/27852/search-results-description)

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
<span id="post-27852-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27852-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-27852-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I just got my first nominatim instance up and running! Very exciting. I've written a little PHP script to just return the results from Geocode.lookup(). Could someone explain what some of these parameters mean? I couldn't find a complete explanation on the wiki. In particular, I've noted the ones I'm unsure of with '?'s</p>
<pre><code>osm_type:   ?
osm_id: Surrogate Key?
class:  ?
type:   ?
admin_level:    ?
rank_search:    Hierarchy Rank
rank_address:   Hierarchy Rank
place_id:   Surrogate Key?
country_code:   Country Abbr
langaddress:    Address
placename:  ?
ref:    ?
lon:    Longitude
lat:    Latitude
importance: Based on algorithm
addressimportance:  ?
extra_place ?
aBoundingBox    Bounding Box
label   ?
name    Full name
foundorder  ?</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Nov '13, 13:15</strong></p>
<img src="https://secure.gravatar.com/avatar/cedcf7f648595f10a2eff219e1b94922?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sbryfcz&#39;s gravatar image" />
<p><span>sbryfcz</span><br />
<span class="score" title="56 reputation points">56</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sbryfcz has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-27852" class="comments-container">
<span id="28341"></span>
<div id="comment-28341" class="comment">
<div id="post-28341-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>As you also ask for (at least for me) obvious details, I like to ask if you already read: <a href="https://wiki.openstreetmap.org/wiki/Nominatim#Parameters">https://wiki.openstreetmap.org/wiki/Nominatim#Parameters</a> ?</p>
</div>
<div id="comment-28341-info" class="comment-info">
<span class="comment-age">(21 Nov '13, 16:05)</span> <span class="comment-user userinfo">iii</span>
</div>
</div>
</div>
<div id="comment-tools-27852" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-27852-form-container" class="comment-form-container">
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

<span id="28418"></span>

<div id="answer-container-28418" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-28418-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-28418-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-28418-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The source code now contains a <a href="https://github.com/twain47/Nominatim/blob/master/lib/Geocode.php#L319">short description of these fields</a>. I also recommend to have a look at the SOTM'13 <a href="http://osm.lonvia.de/presentations/2013-nominatim.html">Nominatim presentation</a> where a bit more on the background of the database schema is explained.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Nov '13, 12:16</strong></p>
<img src="https://secure.gravatar.com/avatar/d888b712d85dee0aa304297f2dc697c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lonvia&#39;s gravatar image" />
<p><span>lonvia</span><br />
<span class="score" title="6213 reputation points"><span>6.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lonvia has 43 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-28418" class="comments-container">
&#10;</div>
<div id="comment-tools-28418" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-28418-form-container" class="comment-form-container">
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

