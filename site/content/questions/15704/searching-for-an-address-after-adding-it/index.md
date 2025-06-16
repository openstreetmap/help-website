+++
type = "question"
title = "Searching for an address after adding it"
description = '''Hi, I am new to OSM and have a question. I added a few locations/addresses to the map. How long should it take for these changes to applied in such a way that I can search for the address and successfully get a result back? I read in some places the map might not get updated for weeks or months, and...'''
date = "2012-08-31T05:02:00Z"
lastmod = "2012-09-01T00:16:00Z"
weight = 15704
keywords = [ "changes", "update", "address" ]
aliases = [ "/questions/15704" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Searching for an address after adding it](/questions/15704/searching-for-an-address-after-adding-it)

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
<span id="post-15704-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15704-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-15704-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I am new to OSM and have a question. I added a few locations/addresses to the map. How long should it take for these changes to applied in such a way that I can search for the address and successfully get a result back? I read in some places the map might not get updated for weeks or months, and other places said within minutes. I'm also more concerned about searching for the address, not necessarily seeing it on the map.</p>
<p>Thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-changes" rel="tag" title="see questions tagged &#39;changes&#39;">changes</span> <span class="post-tag tag-link-update" rel="tag" title="see questions tagged &#39;update&#39;">update</span> <span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 Aug '12, 05:02</strong></p>
<img src="https://secure.gravatar.com/avatar/43f538e86733e722312e5ba38b7512ad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="down2party&#39;s gravatar image" />
<p><span>down2party</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="down2party has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-15704" class="comments-container">
&#10;</div>
<div id="comment-tools-15704" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15704-form-container" class="comment-form-container">
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

<span id="15724"></span>

<div id="answer-container-15724" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-15724-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15724-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-15724-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="down2party has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I think I now see what happened here.<br />
</p>
<p>The building was added as changeset 12924638 and included an addr:street of "New Castle Road" but "New Castle Road" itself wasn't added until changeset 12926499, nearly 5 hours later, by which time nominatim had already indexed the building - and not being able to find the street given just linked it to the nearest road (Arch Road).</p>
<p>It is helpful (and more common) that roads are added to places before buildings but this should be resolved as an update bug in nominatim.</p>
<p>I've edited this area to clean up the building outline and as a result the building was re-indexed. It now looks like it has the correct address.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Aug '12, 15:50</strong></p>
<img src="https://secure.gravatar.com/avatar/bda08a105bb6a4a606d47c1b27187fac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="twain&#39;s gravatar image" />
<p><span>twain</span><br />
<span class="score" title="2381 reputation points"><span>2.4k</span></span><span title="25 badges"><span class="silver">●</span><span class="badgecount">25</span></span><span title="38 badges"><span class="bronze">●</span><span class="badgecount">38</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="twain has 15 accepted answers">40%</span> </br></p>
</div>
</div>
<div id="comments-container-15724" class="comments-container">
<span id="15738"></span>
<div id="comment-15738" class="comment">
<div id="post-15738-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks so much for your assistance twain! I am new to OSM and didn't know street was missing the first time around, or that it even worked that way. I noticed later it was missing and went back to add it. Searching for "4718 New Castle Road, Stockton, CA" works now. Oddly, searching for "4718 New Castle Road, Stockton, CA 95215" does not work.</p>
</div>
<div id="comment-15738-info" class="comment-info">
<span class="comment-age">(01 Sep '12, 00:16)</span> <span class="comment-user userinfo">down2party</span>
</div>
</div>
</div>
<div id="comment-tools-15724" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15724-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="15710"></span>

<div id="answer-container-15710" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-15710-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15710-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-15710-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Searching and rendering are two different things, that's why the rendering intervals don't apply for searching addresses. For searching we currently use <a href="https://wiki.openstreetmap.org/wiki/Nominatim">Nominatim</a> which had several update problems in the past, also due to our recent license change. But now it should update more regularly I guess so that your data should appear soon. The date of the last update can be viewed at <a href="http://nominatim.openstreetmap.org/">nominatim.openstreetmap.org</a> at the top of the page.</p>
<p>If you think your data should already be searchable, but isn't, please be more specific and give use some information about your changes, ideally the ID of an object or of a changeset.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Aug '12, 06:22</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-15710" class="comments-container">
<span id="15712"></span>
<div id="comment-15712" class="comment">
<div id="post-15712-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your input. I am seeing some things updated and others not - I believe there are just some missing pieces that I dont understand yet. Maybe someone can help me figure it out. First example, I'm trying to create an address in Stockton, CA. Somehow the city of Stockton is not married to the postal code 95215. So if I search for</p>
<address>
, Stockton, CA 95215 - it won't find it. Also, the search is finding the street but not the specific address, even though I put in the house number and street name. Changeset: 12926499
</address>
</div>
<div id="comment-15712-info" class="comment-info">
<span class="comment-age">(31 Aug '12, 06:58)</span> <span class="comment-user userinfo">down2party</span>
</div>
</div>
<span id="15714"></span>
<div id="comment-15714" class="comment">
<div id="post-15714-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The <a href="https://www.openstreetmap.org/browse/way/178719020/history">building</a> I assume you are talking about has been added on 2012/08/30 which is also the date of Nominatim's last update, so I suggest to wait for the next update first.</p>
<p>But you are probably right about the <a href="https://wiki.openstreetmap.org/wiki/Key:postal_code">postal code</a>, I can't find it anywhere <a href="http://nominatim.openstreetmap.org/details.php?place_id=148850659">here</a>. Seems like postal codes are missing a lot in this area.</p>
</div>
<div id="comment-15714-info" class="comment-info">
<span class="comment-age">(31 Aug '12, 07:39)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="15716"></span>
<div id="comment-15716" class="comment">
<div id="post-15716-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You can check also this building on <a href="http://nominatim.openstreetmap.org/details?osmtype=W&amp;osmid=178719020">this page</a>.</p>
</div>
<div id="comment-15716-info" class="comment-info">
<span class="comment-age">(31 Aug '12, 09:51)</span> <span class="comment-user userinfo">NicolasDumoulin</span>
</div>
</div>
<span id="15722"></span>
<div id="comment-15722" class="comment">
<div id="post-15722-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Nicolas, this is the building I'm trying to add. It does not show up in search with the address. (It finds the street name, but not the specific address).</p>
<p>Is there any way to tie the building to the postal code so it will show up in search? Even thought he postal code is missing? Thanks for all the valuable help.</p>
</div>
<div id="comment-15722-info" class="comment-info">
<span class="comment-age">(31 Aug '12, 15:16)</span> <span class="comment-user userinfo">down2party</span>
</div>
</div>
<span id="15723"></span>
<div id="comment-15723" class="comment">
<div id="post-15723-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>As far as I can tell from the comments the address you are searching for is there: <a href="http://nominatim.openstreetmap.org/search.php?q=4718+Arch+Road%2C+Stockton%2C+CA+95215">http://nominatim.openstreetmap.org/search.php?q=4718+Arch+Road%2C+Stockton%2C+CA+95215</a></p>
<p>if this is not the address you are looking for can you give it and the osm id of the feature you are expecting to be found?</p>
</div>
<div id="comment-15723-info" class="comment-info">
<span class="comment-age">(31 Aug '12, 15:31)</span> <span class="comment-user userinfo">twain</span>
</div>
</div>
</div>
<div id="comment-tools-15710" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15710-form-container" class="comment-form-container">
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

