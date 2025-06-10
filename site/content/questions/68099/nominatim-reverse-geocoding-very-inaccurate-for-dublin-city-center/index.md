+++
type = "question"
title = "Nominatim reverse geocoding very inaccurate for Dublin city center"
description = '''Hi all, I&#x27;m using Nominatim and overall it works great and gives mostly accurate results. But for some reason it consistently gives inaccurate results of reverse geocoding specifically for Dublin city center. I created minimal reproduction environment of the issue: https://nominatim-reverse-geocodin...'''
date = "2019-02-21T16:11:00Z"
lastmod = "2019-02-22T12:42:00Z"
weight = 68099
keywords = [ "reversegeocoding", "nominatim" ]
aliases = [ "/questions/68099" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Nominatim reverse geocoding very inaccurate for Dublin city center](/questions/68099/nominatim-reverse-geocoding-very-inaccurate-for-dublin-city-center)

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
<span id="post-68099-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68099-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-68099-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all,</p>
<p>I'm using Nominatim and overall it works great and gives mostly accurate results. But for some reason it consistently gives inaccurate results of reverse geocoding specifically for Dublin city center.</p>
<p>I created minimal reproduction environment of the issue:</p>
<p><a href="https://nominatim-reverse-geocoding.stackblitz.io">https://nominatim-reverse-geocoding.stackblitz.io</a></p>
<p>When you click on the map it'll put a marker on the selected place and a second marker pointed on the result of it's geocoding. Most of the time it'll be couple of streets away or even further with wrong address name.</p>
<p>Oddly enough, when you get farther from the city center, the results become more accurate. First I thought it's the issue with lack of poi data across Ireland, but Galway or Cork, for example, do not suffer from this problem.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-reversegeocoding" rel="tag" title="see questions tagged &#39;reversegeocoding&#39;">reversegeocoding</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Feb '19, 16:11</strong></p>
<img src="https://secure.gravatar.com/avatar/88ae3cf0b7b95410d5ff3476eff1bd86?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tim-k&#39;s gravatar image" />
<p><span>tim-k</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tim-k has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-68099" class="comments-container">
<span id="68100"></span>
<div id="comment-68100" class="comment">
<div id="post-68100-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>At least one of your problems is that you are including historic boundaries such as this one <a href="https://nominatim.openstreetmap.org/details.php?place_id=250604683">https://nominatim.openstreetmap.org/details.php?place_id=250604683</a></p>
</div>
<div id="comment-68100-info" class="comment-info">
<span class="comment-age">(21 Feb '19, 16:52)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="68101"></span>
<div id="comment-68101" class="comment">
<div id="post-68101-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/647/sk53">@SK53</a> what exactly does this mean and how not to include them when doing the request to Nominatim? Thanks.</p>
</div>
<div id="comment-68101-info" class="comment-info">
<span class="comment-age">(21 Feb '19, 17:04)</span> <span class="comment-user userinfo">tim-k</span>
</div>
</div>
<span id="68115"></span>
<div id="comment-68115" class="comment">
<div id="post-68115-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>These are getting treated as current areas; they need to/should be filtered out before loading into Nominatim (e.g., using osmosis with tag-filter, osmfilter, osm2pgsql LUA scripts or the osm2pgsql style file). This might not be everything because the Irish OSM communities server returns better (but still not v. accurate) results <a href="https://nominatim.openstreetmap.ie/reverse.php?format=html&amp;lat=53.34442437807821&amp;lon=-6.2667801617031245&amp;zoom=18.">https://nominatim.openstreetmap.ie/reverse.php?format=html&amp;lat=53.34442437807821&amp;lon=-6.2667801617031245&amp;zoom=18.</a></p>
</div>
<div id="comment-68115-info" class="comment-info">
<span class="comment-age">(22 Feb '19, 12:42)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-68099" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68099-form-container" class="comment-form-container">
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

<span id="68102"></span>

<div id="answer-container-68102" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68102-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68102-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-68102-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="tim-k has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Looks like an issue with the Nominatim software. As <a href="https://help.openstreetmap.org/users/647/sk53">@SK53</a> said Nominatim seems to return historical boundaries (address rank 29) while those should be ignored in the search. <a href="https://nominatim.openstreetmap.org/reverse.php?format=html&amp;lat=53.34442437807821&amp;lon=-6.2667801617031245&amp;zoom=18">https://nominatim.openstreetmap.org/reverse.php?format=html&amp;lat=53.34442437807821&amp;lon=-6.2667801617031245&amp;zoom=18</a> Can you add that to <a href="https://github.com/openstreetmap/Nominatim/issues">https://github.com/openstreetmap/Nominatim/issues</a> ?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Feb '19, 17:33</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-68102" class="comments-container">
<span id="68111"></span>
<div id="comment-68111" class="comment">
<div id="post-68111-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Will do. Thanks.</p>
</div>
<div id="comment-68111-info" class="comment-info">
<span class="comment-age">(22 Feb '19, 10:14)</span> <span class="comment-user userinfo">tim-k</span>
</div>
</div>
<span id="68113"></span>
<div id="comment-68113" class="comment">
<div id="post-68113-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I've raised a new issue on the tracker <a href="https://github.com/openstreetmap/Nominatim/issues/1313">https://github.com/openstreetmap/Nominatim/issues/1313</a></p>
</div>
<div id="comment-68113-info" class="comment-info">
<span class="comment-age">(22 Feb '19, 11:36)</span> <span class="comment-user userinfo">tim-k</span>
</div>
</div>
</div>
<div id="comment-tools-68102" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68102-form-container" class="comment-form-container">
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

