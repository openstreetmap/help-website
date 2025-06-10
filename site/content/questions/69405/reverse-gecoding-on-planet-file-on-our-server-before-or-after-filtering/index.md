+++
type = "question"
title = "Reverse gecoding on planet file on our server, before or after filtering?"
description = '''Newbie here...but I need to understand basics to plan job. As I understand it this Nominatim Reverse geocoding tool depends on the OSM database to assign country, state, town names to X Y locations, by matching them with listed nodes in OSM DB that already have both xy and geography info (right ?) B...'''
date = "2019-06-01T21:38:00Z"
lastmod = "2019-06-02T00:32:00Z"
weight = 69405
keywords = [ "index", "nominatim", "geocoding", "reverse", "spatial" ]
aliases = [ "/questions/69405" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Reverse gecoding on planet file on our server, before or after filtering?](/questions/69405/reverse-gecoding-on-planet-file-on-our-server-before-or-after-filtering)

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
<span id="post-69405-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69405-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-69405-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Newbie here...but I need to understand basics to plan job. As I understand it this Nominatim Reverse geocoding tool depends on the OSM database to assign country, state, town names to X Y locations, by matching them with listed nodes in OSM DB that already have both xy and geography info (right ?) But if we first filter down a planet file on our server to our few million nodes and points that we want (Bridges, Tunnels etc), and THEN apply reverse geocoding, I dont think that will provide a large enough library of OSM data for it to find matching towns. So is it realistic to add this OSM Names dataset of 22 million place names to the file to provide full library? Is 22 million names searched agains 5 million xy s an unrealistic task? I have read about spatial indexing...would it help if we first indexed our data (even within 50 km is fine enough for us .) Is that a huge task in itself, indexing? Thanks.</p>
<p><a href="https://nominatim.org/release-docs/develop/api/Reverse/">https://nominatim.org/release-docs/develop/api/Reverse/</a></p>
<p><a href="https://osmnames.org/download/">https://osmnames.org/download/</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-index" rel="tag" title="see questions tagged &#39;index&#39;">index</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-geocoding" rel="tag" title="see questions tagged &#39;geocoding&#39;">geocoding</span> <span class="post-tag tag-link-reverse" rel="tag" title="see questions tagged &#39;reverse&#39;">reverse</span> <span class="post-tag tag-link-spatial" rel="tag" title="see questions tagged &#39;spatial&#39;">spatial</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Jun '19, 21:38</strong></p>
<img src="https://secure.gravatar.com/avatar/aa3e93cbd0a635b436a0ca3a776156ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="philip&#39;s gravatar image" />
<p><span>philip</span><br />
<span class="score" title="26 reputation points">26</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="philip has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Jun '19, 00:34</strong> </span></p>
</div>
</div>
<div id="comments-container-69405" class="comments-container">
&#10;</div>
<div id="comment-tools-69405" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69405-form-container" class="comment-form-container">
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

<span id="69406"></span>

<div id="answer-container-69406" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69406-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69406-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-69406-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Nominatim 3.3 allows selecting which data you want to import, see <a href="http://nominatim.org/release-docs/latest/admin/Import-and-Update/#filtering-imported-data">http://nominatim.org/release-docs/latest/admin/Import-and-Update/#filtering-imported-data</a> It sounds like you only need 'admin' which includes all places (cities, villiages) and their hierachy (which county, state, country they belong to). It depends on your hardware of course, number of CPU cores, number of parallel API requests you'll run but 5 millions requests should be possible in 1-2 days.</p>
<blockquote>
<p>would it help if we first indexed our data</p>
</blockquote>
<p>That's not needed. Nominatim's spatial index is global. While sending requests region by region will have a slight performance boost because the database can keep data it recently used in RAM, the extra engineering work isn't worth it.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Jun '19, 23:51</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-69406" class="comments-container">
<span id="69407"></span>
<div id="comment-69407" class="comment">
<div id="post-69407-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Great. Thank you.</p>
</div>
<div id="comment-69407-info" class="comment-info">
<span class="comment-age">(02 Jun '19, 00:32)</span> <span class="comment-user userinfo">philip</span>
</div>
</div>
</div>
<div id="comment-tools-69406" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69406-form-container" class="comment-form-container">
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

