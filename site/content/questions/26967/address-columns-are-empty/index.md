+++
type = "question"
title = "address columns are empty"
description = '''Hello,  I have been trying to find the basketball courts in the State of California. I downloaded the osm file for the state, then I imported the data into my database using osm2pgsql. I am able to select data using the following query but for some reason the address columns are empty. The only popu...'''
date = "2013-10-06T22:35:00Z"
lastmod = "2013-10-07T17:53:00Z"
weight = 26967
keywords = [ "address" ]
aliases = [ "/questions/26967" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [address columns are empty](/questions/26967/address-columns-are-empty)

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
<span id="post-26967-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26967-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-26967-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I have been trying to find the basketball courts in the State of California. I downloaded the osm file for the state, then I imported the data into my database using osm2pgsql. I am able to select data using the following query but for some reason the address columns are empty. The only populated columns are osm_id, leisure, sport, and way. How can I go about finding the associated addresses for these records?</p>
<p>select * from planet_osm_polygon where sport = 'basketball'</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Oct '13, 22:35</strong></p>
<img src="https://secure.gravatar.com/avatar/76964d397ef43ae7eac2b4cddbd73cbf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="reza215r&#39;s gravatar image" />
<p><span>reza215r</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="reza215r has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-26967" class="comments-container">
&#10;</div>
<div id="comment-tools-26967" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26967-form-container" class="comment-form-container">
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

<span id="26968"></span>

<div id="answer-container-26968" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-26968-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26968-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-26968-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Are you sure that OSM <em>has</em> these addresses at all? Remember, OSM data doesn't magically appear - it's only there if the person who added the baseball court added the address (or someone else added it later). It is entirely possible that a baseball court can be seen on aerial imagery and therefore mapped, but the address might not even be known to the person adding it in!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Oct '13, 22:51</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-26968" class="comments-container">
<span id="26969"></span>
<div id="comment-26969" class="comment">
<div id="post-26969-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks for the answer. So if I go to www.openstreetmap.org and search with keywords "basketball California", it returns courts with their addresses. Do you happen to know where are those addresses coming from?</p>
<p>Here is an exmple of it: Sports Pitch Basketball Courts, Concha Street, Los Angeles, California, 91001, United States of America</p>
</div>
<div id="comment-26969-info" class="comment-info">
<span class="comment-age">(06 Oct '13, 23:04)</span> <span class="comment-user userinfo">reza215r</span>
</div>
</div>
<span id="26970"></span>
<div id="comment-26970" class="comment">
<div id="post-26970-score" class="comment-score">
5
</div>
<div class="comment-text">
<p>It is taking the location of the object in OSM and doing a reverse geocode to get a street name. If you click on the "view details" link in the search results you will see the actual OSM object that your search found and you can see that it indeed does not have an address mapped on it.</p>
<p>Also I should note that the search is finding that object because of the name=Basketball tag, not because it is tagged with sport=basketball.</p>
</div>
<div id="comment-26970-info" class="comment-info">
<span class="comment-age">(07 Oct '13, 00:53)</span> <span class="comment-user userinfo">ToeBee</span>
</div>
</div>
<span id="26985"></span>
<div id="comment-26985" class="comment">
<div id="post-26985-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>ok, that makes sense, thanks! One quick question though, which column/field should I run the reverse geocode against to in order to extract the address?</p>
</div>
<div id="comment-26985-info" class="comment-info">
<span class="comment-age">(07 Oct '13, 15:20)</span> <span class="comment-user userinfo">reza215r</span>
</div>
</div>
<span id="26988"></span>
<div id="comment-26988" class="comment">
<div id="post-26988-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Reverse geocoding takes a lat/lon and returns an address. So you need the location, not any of the tags. I think Nominatim (which drives the search on osm.org) takes the centroid of the area. You could get this from the linestring column in your database.</p>
</div>
<div id="comment-26988-info" class="comment-info">
<span class="comment-age">(07 Oct '13, 16:44)</span> <span class="comment-user userinfo">ToeBee</span>
</div>
</div>
<span id="26991"></span>
<div id="comment-26991" class="comment">
<div id="post-26991-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Keep in mind that Nominatim limits usage of the public instance. See <a href="https://wiki.openstreetmap.org/wiki/Nominatim_usage_policy#Bulk_Geocoding">https://wiki.openstreetmap.org/wiki/Nominatim_usage_policy#Bulk_Geocoding</a></p>
</div>
<div id="comment-26991-info" class="comment-info">
<span class="comment-age">(07 Oct '13, 17:53)</span> <span class="comment-user userinfo">gormo</span>
</div>
</div>
</div>
<div id="comment-tools-26968" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26968-form-container" class="comment-form-container">
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

