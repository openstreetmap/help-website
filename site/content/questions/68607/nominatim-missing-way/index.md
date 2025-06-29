+++
type = "question"
title = "Nominatim missing way"
description = '''Hi, I&#x27;m using Nominatim to reverse geocode an OSM way. However there are some ways that cannot be geocoded. Please see: https://nominatim.openstreetmap.org/reverse?osm_id=126761805&amp;amp;osm_type=W I&#x27;m revisioning this using overpass api (that&#x27;s where I got the way id from) and it shows some info. htt...'''
date = "2019-04-02T10:36:00Z"
lastmod = "2019-04-02T10:58:00Z"
weight = 68607
keywords = [ "reversegeocoding", "nominatim", "overpass-turbo", "highway", "osm" ]
aliases = [ "/questions/68607" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Nominatim missing way](/questions/68607/nominatim-missing-way)

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
<span id="post-68607-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68607-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-68607-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I'm using Nominatim to reverse geocode an OSM way. However there are some ways that cannot be geocoded. Please see: <a href="https://nominatim.openstreetmap.org/reverse?osm_id=126761805&amp;osm_type=W">https://nominatim.openstreetmap.org/reverse?osm_id=126761805&amp;osm_type=W</a></p>
<p>I'm revisioning this using overpass api (that's where I got the way id from) and it shows some info. <a href="https://overpass-turbo.eu/s/HAv">https://overpass-turbo.eu/s/HAv</a></p>
<p>Why does Nominatim return <code>Unable to geocode</code>? Does it mean that Overpass and Nominatim API use different databases? Or is Nominatim cutting off some ways by default?</p>
<p>Thanks,</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-reversegeocoding" rel="tag" title="see questions tagged &#39;reversegeocoding&#39;">reversegeocoding</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span> <span class="post-tag tag-link-highway" rel="tag" title="see questions tagged &#39;highway&#39;">highway</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Apr '19, 10:36</strong></p>
<img src="https://secure.gravatar.com/avatar/709a50f4434a5236a949f4e5c7dbc2fb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Yura&#39;s gravatar image" />
<p><span>Yura</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Yura has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-68607" class="comments-container">
&#10;</div>
<div id="comment-tools-68607" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68607-form-container" class="comment-form-container">
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

<span id="68608"></span>

<div id="answer-container-68608" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68608-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68608-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-68608-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Yura has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Nominatim only imports features with names or reference numbers. <a href="https://wiki.openstreetmap.org/wiki/Nominatim/Development_overview#Tags_processed">https://wiki.openstreetmap.org/wiki/Nominatim/Development_overview#Tags_processed</a> Overpass might be better suited if you're looking for unnamed ways.</p>
<p>If you run your own instance of Nominatim you can change the defaults to import more (or less) <a href="https://github.com/openstreetmap/Nominatim/issues/1340">https://github.com/openstreetmap/Nominatim/issues/1340</a></p>
<p>For lookup of features by OSM type and OSM id, the /lookup endpoint will be faster <a href="http://nominatim.org/release-docs/latest/api/Lookup/">http://nominatim.org/release-docs/latest/api/Lookup/</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Apr '19, 10:58</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-68608" class="comments-container">
&#10;</div>
<div id="comment-tools-68608" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68608-form-container" class="comment-form-container">
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

