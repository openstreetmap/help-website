+++
type = "question"
title = "Adding address for geocode lookup with Nominatim"
description = '''Sorry for the newbie question but after doing a lot of research on OpenStreetMap I am still confused as to how everything works. At this point I have setup my own server with Nominatim so that I can perform as many lookups as I want and add data that might not have the approved OSM license. The prob...'''
date = "2013-05-26T23:42:00Z"
lastmod = "2013-05-31T01:43:00Z"
weight = 22787
keywords = [ "imports", "nominatim", "geocoder", "address" ]
aliases = [ "/questions/22787" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Adding address for geocode lookup with Nominatim](/questions/22787/adding-address-for-geocode-lookup-with-nominatim)

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
<span id="post-22787-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22787-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-22787-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Sorry for the newbie question but after doing a lot of research on OpenStreetMap I am still confused as to how everything works.</p>
<p>At this point I have setup my own server with Nominatim so that I can perform as many lookups as I want and add data that might not have the approved OSM license.</p>
<p>The problem I am running into is that there is not enough detail in the database. I have tried importing the TIGER data (not sure if it worked) but I am still missing a lot of data. So I would like to import the county property data.</p>
<p>The data that I have contains polygon shapes for the parcel and address information.</p>
<p>So the questions...</p>
<ul>
<li>Are the polygons just four nodes connected as a way?</li>
<li>If I tag the address information will Nominatim be able to use the addresses for searching.</li>
<li>How do I describe the polygons in openstreetmap to indicate parcel data?</li>
</ul>
<p>Sorry for being long winded but this has been very confusing to me.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-imports" rel="tag" title="see questions tagged &#39;imports&#39;">imports</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-geocoder" rel="tag" title="see questions tagged &#39;geocoder&#39;">geocoder</span> <span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 May '13, 23:42</strong></p>
<img src="https://secure.gravatar.com/avatar/959fa3c2c5e43f36162876ae97305a44?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chung1&#39;s gravatar image" />
<p><span>chung1</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chung1 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 May '13, 23:43</strong> </span></p>
</div>
</div>
<div id="comments-container-22787" class="comments-container">
&#10;</div>
<div id="comment-tools-22787" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22787-form-container" class="comment-form-container">
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

<span id="22870"></span>

<div id="answer-container-22870" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-22870-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22870-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-22870-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Polygons can be as simple as a way using a list of nodes. They can also be relations of ways but for your purposes a simple way joining a set of nodes is probably best. See the wiki for a definition of the <a href="https://wiki.openstreetmap.org/wiki/Osm_format">OSM file format</a>.</p>
<p>There is currently no convention I'm aware of for importing parcel data into osm so doing this 'correctly' probably isn't possible. See: <a href="https://wiki.openstreetmap.org/wiki/Parcel">https://wiki.openstreetmap.org/wiki/Parcel</a></p>
<p>I would suggest tagging the parcels as building=yes and then using the <a href="https://wiki.openstreetmap.org/wiki/Addr">https://wiki.openstreetmap.org/wiki/Addr</a> tags. For your purposes it will probably provide the best result for least work.</p>
<p><strong>PLEASE NOTE: This is assuming you are importing the data straight into nominatim. This would not be suitable for importing into OSM database itself.</strong> That would be a completely different topic.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 May '13, 18:55</strong></p>
<img src="https://secure.gravatar.com/avatar/bda08a105bb6a4a606d47c1b27187fac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="twain&#39;s gravatar image" />
<p><span>twain</span><br />
<span class="score" title="2381 reputation points"><span>2.4k</span></span><span title="25 badges"><span class="silver">●</span><span class="badgecount">25</span></span><span title="38 badges"><span class="bronze">●</span><span class="badgecount">38</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="twain has 15 accepted answers">40%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 May '13, 18:56</strong> </span></p>
</div>
</div>
<div id="comments-container-22870" class="comments-container">
<span id="22898"></span>
<div id="comment-22898" class="comment">
<div id="post-22898-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the answer. Is there a link that explains the difference between Nominatim and the OSM database. My understanding was that Nominatim used the OSM database to perform the lookup but I think I am a little confused.</p>
</div>
<div id="comment-22898-info" class="comment-info">
<span class="comment-age">(31 May '13, 01:43)</span> <span class="comment-user userinfo">chung1</span>
</div>
</div>
</div>
<div id="comment-tools-22870" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22870-form-container" class="comment-form-container">
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

