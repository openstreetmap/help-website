+++
type = "question"
title = "Nominatim: get primary_link, secondary_link ways"
description = '''I can&#x27;t get any information about osm ways primary_link, secondary_link etc. from Nominatim. Seems that there is no information in Nominatim about this roads at all, because, for example, even on https://nominatim.openstreetmap.org/ when i try reverse search for point 55.707947 37.57625 and zoom 16 ...'''
date = "2020-06-01T07:42:00Z"
lastmod = "2020-06-01T08:55:00Z"
weight = 75078
keywords = [ "ways", "search", "nominatim" ]
aliases = [ "/questions/75078" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Nominatim: get primary_link, secondary_link ways](/questions/75078/nominatim-get-primary_link-secondary_link-ways)

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
<span id="post-75078-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75078-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-75078-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I can't get any information about osm ways primary_link, secondary_link etc. from Nominatim. Seems that there is no information in Nominatim about this roads at all, because, for example, even on <a href="https://nominatim.openstreetmap.org/">https://nominatim.openstreetmap.org/</a></p>
<p>when i try reverse search for point 55.707947 37.57625 and zoom 16 I can't get info about osm way 40946080 (but i can find it manually by link in list of points for way 51876561) <a href="https://www.openstreetmap.org/way/40946080">https://www.openstreetmap.org/way/40946080</a></p>
<p>In postgres nominatim db (tables place and placex) i also can't find required osm_id. This case reproduces for ways with tag primary_link, secondary_link</p>
<p>Is there any way to get ways of that types in Nominatim (or, maybe, change data import to my (local) osm db from pbf)?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ways" rel="tag" title="see questions tagged &#39;ways&#39;">ways</span> <span class="post-tag tag-link-search" rel="tag" title="see questions tagged &#39;search&#39;">search</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Jun '20, 07:42</strong></p>
<img src="https://secure.gravatar.com/avatar/6224ae9eca5eafdf72f87fce6a9ce3a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dvf_blm&#39;s gravatar image" />
<p><span>Dvf_blm</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dvf_blm has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-75078" class="comments-container">
&#10;</div>
<div id="comment-tools-75078" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75078-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="75079"></span>

<div id="answer-container-75079" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-75079-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75079-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-75079-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Dvf_blm has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The wiki <a href="https://wiki.openstreetmap.org/wiki/Nominatim">says</a> Nominatim is for named things. The secondary_link you linked to is unnamed, so I wouldn't expect Nominatim to find it.</p>
<p>Depending on your use case <a href="https://wiki.openstreetmap.org/wiki/Overpass">Overpass</a> or Overpass Turbo may do what you like.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Jun '20, 08:33</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-75079" class="comments-container">
&#10;</div>
<div id="comment-tools-75079" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75079-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="75080"></span>

<div id="answer-container-75080" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-75080-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75080-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-75080-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Similar to <a href="https://github.com/osm-search/Nominatim/issues/1747">https://github.com/osm-search/Nominatim/issues/1747</a> edit your import style (<a href="https://github.com/osm-search/Nominatim/tree/master/settings).">https://github.com/osm-search/Nominatim/tree/master/settings).</a> <a href="http://nominatim.org/release-docs/latest/admin/Import-and-Update/#filtering-imported-data">http://nominatim.org/release-docs/latest/admin/Import-and-Update/#filtering-imported-data</a> covers the installation, <a href="http://nominatim.org/release-docs/latest/develop/Import/">http://nominatim.org/release-docs/latest/develop/Import/</a> goes more in-depth on the file format.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Jun '20, 08:55</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-75080" class="comments-container">
&#10;</div>
<div id="comment-tools-75080" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75080-form-container" class="comment-form-container">
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

