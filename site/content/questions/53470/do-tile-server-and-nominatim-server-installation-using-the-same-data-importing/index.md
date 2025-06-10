+++
type = "question"
title = "do tile server and nominatim server installation using the same data importing"
description = '''I want to build a server that provides maps, reverse geocoding and search, I am a newbie to this field and I have tried separate tutorials to build OSM server then Nominatim server on the same box , I saw all of them importing the same OSM data into PostgreSQL database . Now, my question is: is it t...'''
date = "2016-12-10T22:16:00Z"
lastmod = "2016-12-10T22:58:00Z"
weight = 53470
keywords = [ "nominatim", "osm" ]
aliases = [ "/questions/53470" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [do tile server and nominatim server installation using the same data importing](/questions/53470/do-tile-server-and-nominatim-server-installation-using-the-same-data-importing)

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
<span id="post-53470-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53470-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-53470-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to build a server that provides maps, reverse geocoding and search, I am a newbie to this field and I have tried separate tutorials to build OSM server then Nominatim server on the same box , I saw all of them importing the same OSM data into PostgreSQL database . Now, my question is: is it the same data processed in the two methods? or Do I have to go through the same process of importing data in the two cases? what I think is that, OSM data is imported to PostgreSQL in installing OSM server the same way as it is imported in installing Nominatim server nad the different resides in using rendering tiles in the first and finding addresses in the second. am I right in this ? if that the case, then we can use the same database for the two servers but with different tables . appreciate any help</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Dec '16, 22:16</strong></p>
<img src="https://secure.gravatar.com/avatar/a53f40937325cb800f2a79b6083a9412?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="johntaa&#39;s gravatar image" />
<p><span>johntaa</span><br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="johntaa has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-53470" class="comments-container">
&#10;</div>
<div id="comment-tools-53470" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53470-form-container" class="comment-form-container">
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

<span id="53474"></span>

<div id="answer-container-53474" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53474-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53474-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-53474-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Currently they need to be in two separate databases. They can be on the same server of course. Nominatim names it's database 'nominatim' by default so you don't have to worry about one system overriding data of the other.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Dec '16, 22:58</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-53474" class="comments-container">
&#10;</div>
<div id="comment-tools-53474" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53474-form-container" class="comment-form-container">
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

