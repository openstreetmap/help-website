+++
type = "question"
title = "Interpolating address data outside of the US"
description = '''I believe Nominatim relies on the US TIGER data for interpolating addresses. As such, here in New Zealand, if you query an address that isn&#x27;t in the database it only returns a road section, e.g. https://nominatim.openstreetmap.org/search.php?q=207+Bealey+Avenue%2C+Christchurch&amp;amp;polygon_geojson=1....'''
date = "2020-04-28T11:23:00Z"
lastmod = "2020-04-29T21:05:00Z"
weight = 74443
keywords = [ "nominatim", "address" ]
aliases = [ "/questions/74443" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Interpolating address data outside of the US](/questions/74443/interpolating-address-data-outside-of-the-us)

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
<span id="post-74443-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74443-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74443-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I believe Nominatim relies on the US TIGER data for interpolating addresses. As such, here in New Zealand, if you query an address that isn't in the database it only returns a road section, e.g. <a href="https://nominatim.openstreetmap.org/search.php?q=207+Bealey+Avenue%2C+Christchurch&amp;polygon_geojson=1">https://nominatim.openstreetmap.org/search.php?q=207+Bealey+Avenue%2C+Christchurch&amp;polygon_geojson=1</a>.</p>
<p>I'm experimenting with setting up a server and would really like this functionality (NZ' address data is not bad, but far from perfect).</p>
<p>Is there any way of getting Nominatim to use the OSM data for interpolation?</p>
<p>Alternatively, the TIGER Edge datasets look fairly straightforward and I could probably replicate them for New Zealand using address data from Land Information New Zealand. Has anybody tried this, or can anyone see any reason why it would or wouldn't work?</p>
<p>Many thanks</p>
<p>David</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Apr '20, 11:23</strong></p>
<img src="https://secure.gravatar.com/avatar/2b079d7eebde58255d6c812e4ced9973?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="David_EA&#39;s gravatar image" />
<p><span>David_EA</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="David_EA has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-74443" class="comments-container">
&#10;</div>
<div id="comment-tools-74443" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74443-form-container" class="comment-form-container">
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

<span id="74445"></span>

<div id="answer-container-74445" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74445-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74445-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-74445-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>US TIGER data for streets are only interpolations, the data doesn't contain positions of house numbers directly. You're right that Nominatim has separate logic to import the format and search. At search time for US addresses both OSM and US TIGER data are queried but since US TIGER data isn't rendered on a map it can be difficult to interpret the results sometimes.</p>
<p>OSM tagging schema has <a href="https://wiki.openstreetmap.org/wiki/Addresses#Using_interpolation">https://wiki.openstreetmap.org/wiki/Addresses#Using_interpolation</a> which is used throughout the world in some degree. Here's an example in NZ <a href="https://www.openstreetmap.org/way/266743982">https://www.openstreetmap.org/way/266743982</a> (<a href="https://overpass-turbo.eu/s/To1)">https://overpass-turbo.eu/s/To1)</a> So tagging those in OSM should work just fine.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Apr '20, 14:19</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-74445" class="comments-container">
<span id="74446"></span>
<div id="comment-74446" class="comment">
<div id="post-74446-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I suspect the issue is that licensing for an import of the NZ address database, so adding addresses or address interpolations from it into OSM may not be possible. But if one were setting up their own Nominatim server then there is no problem having it query both OSM data and data from some other source. Since Nominatim has been setup to be able to use TIGER data but not NZ Land Information data, I think the question was would it work to convert the NZ data to the TIGER format.</p>
<p>I know almost nothing about Nominatim, but that sounds like a reasonable way to go to me.</p>
</div>
<div id="comment-74446-info" class="comment-info">
<span class="comment-age">(28 Apr '20, 15:09)</span> <span class="comment-user userinfo">n76</span>
</div>
</div>
<span id="74450"></span>
<div id="comment-74450" class="comment">
<div id="post-74450-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Nominatim keeps the TIGER data in separate database tables so avoid mixing. Have a look at <a href="http://nominatim.org/release-docs/latest/data-sources/US-Tiger/">http://nominatim.org/release-docs/latest/data-sources/US-Tiger/</a> how the data gets converted into <em>.sql files for import so might want to generate similar</em> .sql files. Throughout the Nominatim code base there's the variable CONST_Use_US_Tiger_Data (true, false) that determines when the data should be used. I'm sure there's another check for country_code=us which you'd need to change. <a href="https://lists.openstreetmap.org/pipermail/geocoding/">https://lists.openstreetmap.org/pipermail/geocoding/</a> is good for discussing such projects.</p>
</div>
<div id="comment-74450-info" class="comment-info">
<span class="comment-age">(28 Apr '20, 16:13)</span> <span class="comment-user userinfo">mtmail</span>
</div>
</div>
<span id="74466"></span>
<div id="comment-74466" class="comment">
<div id="post-74466-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for all the feedback. I think making a pseudo-Tiger file might be the way for me to progress as the OSM interpolation tag would need to be set up in thousands of places as we have a high (but not perfect) set of address data from LINZ (which is Creative Commons).</p>
<p>Thanks again</p>
</div>
<div id="comment-74466-info" class="comment-info">
<span class="comment-age">(29 Apr '20, 09:18)</span> <span class="comment-user userinfo">David_EA</span>
</div>
</div>
<span id="74486"></span>
<div id="comment-74486" class="comment">
<div id="post-74486-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://wiki.openstreetmap.org/wiki/LINZ/Address_Import">https://wiki.openstreetmap.org/wiki/LINZ/Address_Import</a> and the linked <a href="https://lists.openstreetmap.org/pipermail/imports/2017-June/thread.html#5014">https://lists.openstreetmap.org/pipermail/imports/2017-June/thread.html#5014</a> has some detail about the licensing.</p>
</div>
<div id="comment-74486-info" class="comment-info">
<span class="comment-age">(29 Apr '20, 21:05)</span> <span class="comment-user userinfo">mtmail</span>
</div>
</div>
</div>
<div id="comment-tools-74445" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74445-form-container" class="comment-form-container">
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

