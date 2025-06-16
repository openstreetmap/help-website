+++
type = "question"
title = "Query place_id"
description = '''Is there any way to query data by the place_id that is returned when reverse-geocoding a place. I was able to get a place_id from this reverse geocode: http://nominatim.openstreetmap.org/reverse?format=json&amp;amp;lat=52.5487429714954&amp;amp;lon=-1.81602098644987&amp;amp;zoom=18&amp;amp;addressdetails=1 Now I wou...'''
date = "2014-10-17T20:45:00Z"
lastmod = "2014-10-18T09:23:00Z"
weight = 37714
keywords = [ "reversegeocoding", "place", "id", "geocoder" ]
aliases = [ "/questions/37714" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Query place_id](/questions/37714/query-place_id)

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
<span id="post-37714-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37714-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-37714-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is there any way to query data by the place_id that is returned when reverse-geocoding a place.</p>
<p>I was able to get a place_id from this reverse geocode: <a href="http://nominatim.openstreetmap.org/reverse?format=json&amp;lat=52.5487429714954&amp;lon=-1.81602098644987&amp;zoom=18&amp;addressdetails=1">http://nominatim.openstreetmap.org/reverse?format=json&amp;lat=52.5487429714954&amp;lon=-1.81602098644987&amp;zoom=18&amp;addressdetails=1</a></p>
<p>Now I would like to run something to get the name of the place back using the id. It seems that the system has the capabilities because typing the place_id in the url of this works: <a href="https://nominatim.openstreetmap.org/details.php?place_id=82367732">https://nominatim.openstreetmap.org/details.php?place_id=82367732</a></p>
<p>The issue is when I run something like this I have no luck: <a href="http://nominatim.openstreetmap.org/search?q=82367732&amp;format=json&amp;polygon=1&amp;addressdetails=1">http://nominatim.openstreetmap.org/search?q=82367732&amp;format=json&amp;polygon=1&amp;addressdetails=1</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-reversegeocoding" rel="tag" title="see questions tagged &#39;reversegeocoding&#39;">reversegeocoding</span> <span class="post-tag tag-link-place" rel="tag" title="see questions tagged &#39;place&#39;">place</span> <span class="post-tag tag-link-id" rel="tag" title="see questions tagged &#39;id&#39;">id</span> <span class="post-tag tag-link-geocoder" rel="tag" title="see questions tagged &#39;geocoder&#39;">geocoder</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Oct '14, 20:45</strong></p>
<img src="https://secure.gravatar.com/avatar/23ebc6af1be18021a1c767471786d5b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chaudha&#39;s gravatar image" />
<p><span>chaudha</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chaudha has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-37714" class="comments-container">
&#10;</div>
<div id="comment-tools-37714" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37714-form-container" class="comment-form-container">
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

<span id="37728"></span>

<div id="answer-container-37728" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-37728-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37728-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-37728-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>place_id is a nominatim internal identifier. I'd recommend to use the actual OSM objects (nodes/ways/relations) returned by the query instead.</p>
<p>Please see this post: <a href="/questions/21542/nominatim-place-id">https://help.openstreetmap.org/questions/21542/nominatim-place-id</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Oct '14, 08:53</strong></p>
<img src="https://secure.gravatar.com/avatar/264d84ab05b942224b05960903eba7a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmd&#39;s gravatar image" />
<p><span>mmd</span><br />
<span class="score" title="5682 reputation points"><span>5.7k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="53 badges"><span class="silver">●</span><span class="badgecount">53</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mmd has 44 accepted answers">37%</span></p>
</div>
</div>
<div id="comments-container-37728" class="comments-container">
<span id="37730"></span>
<div id="comment-37730" class="comment">
<div id="post-37730-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>In other words: Use the <em>osm_id</em> and <em>osm_type</em> contained in Nominatim's response in order to query the corresponding OSM element. In your case the element would be <a href="https://www.openstreetmap.org/way/90394420">way 90394420</a>.</p>
</div>
<div id="comment-37730-info" class="comment-info">
<span class="comment-age">(18 Oct '14, 09:23)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-37728" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37728-form-container" class="comment-form-container">
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

