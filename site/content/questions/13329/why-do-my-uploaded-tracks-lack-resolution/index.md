+++
type = "question"
title = "Why do my uploaded tracks lack resolution?"
description = '''If I Alt Click a track to make it a way, is it supposed to have the same amount of points as the original gpx? My hiking tracks are recorded at 3 sec. intervals, and look fine in Mapsource. However, once uploaded to OSM they seem to lack resolution. Is what I am seeing typical for an upload? MapSour...'''
date = "2012-06-08T00:00:00Z"
lastmod = "2012-06-09T21:13:00Z"
weight = 13329
keywords = [ "track", "resolution", "gpx", "upload", "mapsource" ]
aliases = [ "/questions/13329" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Why do my uploaded tracks lack resolution?](/questions/13329/why-do-my-uploaded-tracks-lack-resolution)

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
<span id="post-13329-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13329-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-13329-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>If I Alt Click a track to make it a way, is it supposed to have the same amount of points as the original gpx? My hiking tracks are recorded at 3 sec. intervals, and look fine in Mapsource. However, once uploaded to OSM they seem to lack resolution. Is what I am seeing typical for an upload?<br />
<a href="http://webpages.charter.net/zeeland5/GeoCaching/PineCreek_MS.JPG">MapSource track</a></p>
<p><a href="http://webpages.charter.net/zeeland5/GeoCaching/PineCreek_OSM.JPG">OSM track</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-track" rel="tag" title="see questions tagged &#39;track&#39;">track</span> <span class="post-tag tag-link-resolution" rel="tag" title="see questions tagged &#39;resolution&#39;">resolution</span> <span class="post-tag tag-link-gpx" rel="tag" title="see questions tagged &#39;gpx&#39;">gpx</span> <span class="post-tag tag-link-upload" rel="tag" title="see questions tagged &#39;upload&#39;">upload</span> <span class="post-tag tag-link-mapsource" rel="tag" title="see questions tagged &#39;mapsource&#39;">mapsource</span>
</div>
<div id="question-controls" class="post-controls">
<div class="community-wiki">
This question is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Jun '12, 00:00</strong></p>
<img src="https://secure.gravatar.com/avatar/fe6ff08a507060cbb945a4ee56c393fe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zeeland5&#39;s gravatar image" />
<p><span>zeeland5</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zeeland5 has no accepted answers">0%</span> </br></p>
</div>
</div>
<div id="comments-container-13329" class="comments-container">
<span id="13364"></span>
<div id="comment-13364" class="comment">
<div id="post-13364-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Not an answer to your question, but one thing that is worth mentioning is that you probably don't want to have quite as many nodes in a way as one-every-3-seconds-at-walking-pace would give you (especially if you're walking in a straight line).</p>
</div>
<div id="comment-13364-info" class="comment-info">
<span class="comment-age">(08 Jun '12, 17:52)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-13329" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13329-form-container" class="comment-form-container">
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

<span id="13387"></span>

<div id="answer-container-13387" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-13387-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13387-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-13387-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>GPS traces are not suited for direct upload to OSM as already mentioned by SomeoneElse. They usually contain too many points and simply converting them to a way doesn't create the required junctions/connections with surrounding ways. You should always create the way by yourself, adding points where necessary and omitting points when the way is just straight.</p>
<p>The Wiki has multiple pages about processing GPS traces:</p>
<ul>
<li><a href="http://wiki.openstreetmap.org/wiki/Upload">uploading a GPX file</a>: this is not necessary for adding ways in OSM, but might help other people later when editing those ways again</li>
<li>using a GPX file with <a href="http://wiki.openstreetmap.org/wiki/Potlatch_2">Potlatch</a>: <a href="http://wiki.openstreetmap.org/wiki/Potlatch_2/Primer#GPS_data_.2F_My_tracks">loading previously uploaded traces</a> and <a href="http://wiki.openstreetmap.org/wiki/Potlatch_2/Primer#Creating_Features">creating points and ways</a></li>
<li>using a GPX file with <a href="http://wiki.openstreetmap.org/wiki/Josm">JOSM</a>: <a href="http://wiki.openstreetmap.org/wiki/JOSM/Guide#Load_a_local_GPX_file">loading a local trace</a> and <a href="http://wiki.openstreetmap.org/wiki/JOSM/Basic_editing#Adding_a_way">adding a way</a></li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Jun '12, 21:13</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Jun '12, 21:15</strong> </span></p>
</div>
</div>
<div id="comments-container-13387" class="comments-container">
&#10;</div>
<div id="comment-tools-13387" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13387-form-container" class="comment-form-container">
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

