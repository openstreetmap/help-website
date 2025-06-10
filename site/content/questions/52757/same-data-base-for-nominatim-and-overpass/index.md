+++
type = "question"
title = "Same data base for Nominatim and Overpass?"
description = '''I thought Nominatim and Overpass have the same data base. But the tags in the search results are quite different e.g. has this request in Overpass  http://overpass-turbo.eu/s/jK8 more information for the same node than this in Nominatim http://nominatim.openstreetmap.org/reverse.php?format=json&amp;amp;...'''
date = "2016-10-31T11:07:00Z"
lastmod = "2016-11-03T07:23:00Z"
weight = 52757
keywords = [ "overpass", "nominatim", "osm", "query", "tags" ]
aliases = [ "/questions/52757" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Same data base for Nominatim and Overpass?](/questions/52757/same-data-base-for-nominatim-and-overpass)

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
<span id="post-52757-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52757-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-52757-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I thought Nominatim and Overpass have the same data base. But the tags in the search results are quite different e.g. has this request in Overpass</p>
<p><a href="http://overpass-turbo.eu/s/jK8">http://overpass-turbo.eu/s/jK8</a></p>
<p>more information for the same node than this in Nominatim</p>
<p><a href="http://nominatim.openstreetmap.org/reverse.php?format=json&amp;osm_type=N&amp;osm_id=3721152636&amp;extratags=1&amp;namedetails=1">http://nominatim.openstreetmap.org/reverse.php?format=json&amp;osm_type=N&amp;osm_id=3721152636&amp;extratags=1&amp;namedetails=1</a></p>
<p>In this case of a charging station, 'voltage', 'socket', and 'capacity' are interesting values!</p>
<p>I do not want to host two databases, but I would like to have all the possible information! Overpass is a bit slow so preferably I would like to use Nominatim, which seems to have less infomation.</p>
<p>Is there any setting which I missed to improve the Nominatim result?</p>
<p>Thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span> <span class="post-tag tag-link-tags" rel="tag" title="see questions tagged &#39;tags&#39;">tags</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 Oct '16, 11:07</strong></p>
<img src="https://secure.gravatar.com/avatar/d001d4c331042ef1dade5af6ed5f7ac2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="autumnus&#39;s gravatar image" />
<p><span>autumnus</span><br />
<span class="score" title="121 reputation points">121</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="autumnus has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-52757" class="comments-container">
&#10;</div>
<div id="comment-tools-52757" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52757-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="52758"></span>

<div id="answer-container-52758" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-52758-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52758-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-52758-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Overpass API returns all tags of the object since querying for specific tags is one of the main purposes of this API.</p>
<p>Nominatim in contrast is a geocoder. It doesn't need information like 'voltage', 'socket', and 'capacity' to answer geocoding requests. Stripping the database of unnecessary information will probably lead to faster search results, reduced time during import and updates and less disk space requirements.</p>
<p>However Nominatim will always include <code>osm_type</code> and <code>osm_id</code> information. The type and ID allows you to retrieve the original OSM object, for example using the main OSM API.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Oct '16, 11:36</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-52758" class="comments-container">
<span id="52760"></span>
<div id="comment-52760" class="comment">
<div id="post-52760-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for that very fast reply! That is what I feared: it seems there is no way around using two services, right?</p>
</div>
<div id="comment-52760-info" class="comment-info">
<span class="comment-age">(31 Oct '16, 13:26)</span> <span class="comment-user userinfo">autumnus</span>
</div>
</div>
</div>
<div id="comment-tools-52758" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52758-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="52807"></span>

<div id="answer-container-52807" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-52807-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52807-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-52807-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Thanks to openSource I found another solution which fits my purpose: <em>Nominatim</em> uses <em>osm2pgsql</em> to fill the database. And this filters which tags are put into the extratags-column. For testing I added a few lines in the code to also fill all remaining tags in the same column. Maybe this is a solution which is not according to the usual usage of Nominatim, but that is what I wanted.</p>
<p>I just wanted to tell you this way of changing <em>Nominatims</em> behaviour by code change.</p>
<p>Be aware that this way ALL tags are taken also (at least in my case) less usefull like</p>
<ul>
<li>"TMC:cid_58:tabcd_1:Class"</li>
<li>"TMC:cid_58:tabcd_1:NextLocationCode"</li>
<li>"roof:shape"</li>
</ul>
<p>or</p>
<ul>
<li>"roof:material"</li>
</ul>
<p>By the way: The lines I added are in file output-gazetteer.cpp in the osm2pgsql folder: in the</p>
<p><code>function void place_tag_processor::process_tags(const taglist_t &amp;tags)</code></p>
<p>in the for-loop I appended the else-clause</p>
<pre><code>323         } else if (item-&gt;key == &quot;building&quot;) {
324             placebuilding = true;
325         } else {
326             extratags.push_back(&amp;*item);
327         }</code></pre>
<p>After that change you have to recompile and just import as usual.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Nov '16, 07:23</strong></p>
<img src="https://secure.gravatar.com/avatar/d001d4c331042ef1dade5af6ed5f7ac2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="autumnus&#39;s gravatar image" />
<p><span>autumnus</span><br />
<span class="score" title="121 reputation points">121</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="autumnus has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Nov '16, 10:57</strong> </span></p>
</div>
</div>
<div id="comments-container-52807" class="comments-container">
&#10;</div>
<div id="comment-tools-52807" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52807-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="52761"></span>

<div id="answer-container-52761" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-52761-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52761-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-52761-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can go in the other direction, use the <code>is_in</code> operator to get some of the information Nominatim provides from Overpass. Here's your query modified to fetch the node and then the containing areas:</p>
<p><a href="http://overpass-turbo.eu/s/jKs">http://overpass-turbo.eu/s/jKs</a></p>
<p>Be sure to inspect the data tab to see the areas returned, they aren't visible on the map.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Oct '16, 14:09</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-52761" class="comments-container">
<span id="52763"></span>
<div id="comment-52763" class="comment">
<div id="post-52763-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Good to know 'is_in' exists. But Overpass already has the more interesting tags for my purpose even in the basic request. What I wanted originally was the improvement of the Nominatim-request.</p>
</div>
<div id="comment-52763-info" class="comment-info">
<span class="comment-age">(31 Oct '16, 14:56)</span> <span class="comment-user userinfo">autumnus</span>
</div>
</div>
</div>
<div id="comment-tools-52761" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52761-form-container" class="comment-form-container">
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

