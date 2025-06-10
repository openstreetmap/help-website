+++
type = "question"
title = "Remove Geofabrik subregion from database"
description = '''Is there a way to delete just one region from a postgresql-gis database that was downloaded from geofabrik.de and imported using osm2pgsql?  ...or to truncate all data from the necessary tables and start over with a fresh/empty database/table? I followed the instructions at switch2osm and imported N...'''
date = "2019-03-04T22:43:00Z"
lastmod = "2019-03-05T20:06:00Z"
weight = 68262
keywords = [ "geofabrik", "delete", "switch2osm", "sub-region", "database" ]
aliases = [ "/questions/68262" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Remove Geofabrik subregion from database](/questions/68262/remove-geofabrik-subregion-from-database)

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
<span id="post-68262-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68262-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-68262-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is there a way to delete just one region from a postgresql-gis database that was downloaded from <a href="http://geofabrik.de">geofabrik.de</a> and imported using <code>osm2pgsql</code>?</p>
<p>...or to truncate all data from the necessary tables and start over with a fresh/empty database/table?</p>
<p>I followed the instructions at <a href="https://switch2osm.org/manually-building-a-tile-server-18-04-lts/">switch2osm</a> and imported North American sub-region data (<code>.osm.pbf</code>) from <a href="http://download.geofabrik.de/north-america.html">geofabrik.de</a> for the state of Maine using <code>osm2pgsql</code>.</p>
<p>They also have "special" sub regions for the entire US Northeast, which they say "may duplicate data already contained in the other sub regions".</p>
<p>Now that I know how to do it, I'd rather get rid of the Maine data from <code>maine-latest.osm.pbf</code> and replace it with the <code>us-northeast-latest.osm.pbf</code> data.</p>
<p>Is there a straightforward way to do this that I'm overlooking in the docs?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-geofabrik" rel="tag" title="see questions tagged &#39;geofabrik&#39;">geofabrik</span> <span class="post-tag tag-link-delete" rel="tag" title="see questions tagged &#39;delete&#39;">delete</span> <span class="post-tag tag-link-switch2osm" rel="tag" title="see questions tagged &#39;switch2osm&#39;">switch2osm</span> <span class="post-tag tag-link-sub-region" rel="tag" title="see questions tagged &#39;sub-region&#39;">sub-region</span> <span class="post-tag tag-link-database" rel="tag" title="see questions tagged &#39;database&#39;">database</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Mar '19, 22:43</strong></p>
<img src="https://secure.gravatar.com/avatar/940d42e7292c10ce5386ac9503d404ae?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sareneathenodny&#39;s gravatar image" />
<p><span>Sareneathenodny</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sareneathenodny has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Mar '19, 22:44</strong> </span></p>
</div>
</div>
<div id="comments-container-68262" class="comments-container">
&#10;</div>
<div id="comment-tools-68262" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68262-form-container" class="comment-form-container">
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

<span id="68263"></span>

<div id="answer-container-68263" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68263-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68263-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-68263-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Actually, if you import a new region by default it'll remove any previous data, so you may not need to do anything.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Mar '19, 22:50</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-68263" class="comments-container">
<span id="68264"></span>
<div id="comment-68264" class="comment">
<div id="post-68264-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Is that true for non-overlapping regions too? If I download and import north-america-latest.osm.pbf, then as a second, separate step import download and import central-america-latest.osm.pbf, will the data for North America be gone?</p>
</div>
<div id="comment-68264-info" class="comment-info">
<span class="comment-age">(04 Mar '19, 22:57)</span> <span class="comment-user userinfo">Sareneathenodny</span>
</div>
</div>
<span id="68265"></span>
<div id="comment-68265" class="comment">
<div id="post-68265-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Yes, the default action is "create" (which will remove previous data). "append" is available (but is very slow) if you really do want to append, and that can have problems due to unexpected overlaps between the two areas (think ferry routes).</p>
<p>If you want to upload two areas it's probably best to merge first and then load that.</p>
</div>
<div id="comment-68265-info" class="comment-info">
<span class="comment-age">(04 Mar '19, 22:59)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="68266"></span>
<div id="comment-68266" class="comment">
<div id="post-68266-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ah. I see. My thought was to import the 5 separate US-subregions from geofabrik to get a map for just the USA, to save on disk space. So you're saying that could cause issues at the boundaries and that it would be best from a technical standpoint to just get the whole north-america file?</p>
</div>
<div id="comment-68266-info" class="comment-info">
<span class="comment-age">(04 Mar '19, 23:09)</span> <span class="comment-user userinfo">Sareneathenodny</span>
</div>
</div>
<span id="68281"></span>
<div id="comment-68281" class="comment">
<div id="post-68281-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If what you ultimately want is the whole of North America, yes. If you just want some subregions, combine them with osmosis or similar and load the result.</p>
</div>
<div id="comment-68281-info" class="comment-info">
<span class="comment-age">(05 Mar '19, 19:13)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="68284"></span>
<div id="comment-68284" class="comment">
<div id="post-68284-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Great, thanks!</p>
</div>
<div id="comment-68284-info" class="comment-info">
<span class="comment-age">(05 Mar '19, 20:06)</span> <span class="comment-user userinfo">Sareneathenodny</span>
</div>
</div>
</div>
<div id="comment-tools-68263" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68263-form-container" class="comment-form-container">
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

