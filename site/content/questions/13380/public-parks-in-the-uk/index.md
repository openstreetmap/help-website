+++
type = "question"
title = "public parks in the uk"
description = '''Is it possible to download the location and name of all public parks in the UK?'''
date = "2012-06-09T18:03:00Z"
lastmod = "2012-06-09T20:03:00Z"
weight = 13380
keywords = [ "park", "public", "uk" ]
aliases = [ "/questions/13380" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [public parks in the uk](/questions/13380/public-parks-in-the-uk)

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
<span id="post-13380-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13380-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-13380-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is it possible to download the location and name of all public parks in the UK?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-park" rel="tag" title="see questions tagged &#39;park&#39;">park</span> <span class="post-tag tag-link-public" rel="tag" title="see questions tagged &#39;public&#39;">public</span> <span class="post-tag tag-link-uk" rel="tag" title="see questions tagged &#39;uk&#39;">uk</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Jun '12, 18:03</strong></p>
<img src="https://secure.gravatar.com/avatar/93abb3d52696bac5a4b0763c1a3fce14?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="noidea&#39;s gravatar image" />
<p><span>noidea</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="noidea has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-13380" class="comments-container">
&#10;</div>
<div id="comment-tools-13380" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13380-form-container" class="comment-form-container">
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

<span id="13384"></span>

<div id="answer-container-13384" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-13384-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13384-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-13384-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>For Query APIs like <a href="http://wiki.openstreetmap.org/wiki/Overpass_API">Overpass API</a> or <a href="http://wiki.openstreetmap.org/wiki/XAPI">XAPI</a> the bounding box will be too large. Therefore the best way seems to get a planet extract of the UK from <a href="http://download.geofabrik.de/osm/">Geofabrik</a> and run <a href="http://wiki.openstreetmap.org/wiki/Osmfilter">osmfilter</a> on it to filter for <a href="http://wiki.openstreetmap.org/wiki/Tag:leisure%3Dpark">leisure=park</a> and maybe name=*. However this will probably return a lot more objects than you are searching for.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Jun '12, 20:03</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Jun '12, 20:04</strong> </span></p>
</div>
</div>
<div id="comments-container-13384" class="comments-container">
&#10;</div>
<div id="comment-tools-13384" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13384-form-container" class="comment-form-container">
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

