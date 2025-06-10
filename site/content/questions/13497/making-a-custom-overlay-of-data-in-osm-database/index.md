+++
type = "question"
title = "Making a custom overlay of data in OSM database?"
description = '''I want to make a custom map of data that&#x27;s in open street map. e.g. I want to show all the electric car charging stations mapped, or all the shops in a city that sell halal food, or all the fabric shops in a city, or all the pubs without TVs (these are all use cases). This data can be added to the O...'''
date = "2012-06-13T10:37:00Z"
lastmod = "2012-06-13T16:57:00Z"
weight = 13497
keywords = [ "datadisplay", "pois", "display", "derivative" ]
aliases = [ "/questions/13497" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Making a custom overlay of data in OSM database?](/questions/13497/making-a-custom-overlay-of-data-in-osm-database)

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
<span id="post-13497-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13497-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-13497-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to make a custom map of data that's in open street map. e.g. I want to show all the electric car charging stations mapped, or all the shops in a city that sell halal food, or all the fabric shops in a city, or all the pubs without TVs (these are all use cases). This data can be added to the OSM database. Is there a web site/app/service that will allow non-technical users to just put in the basics (like "includ all nodes tagged amenity=charging_point") and then there'll be a nice slippy map showing main OSM mapnik but with lots of JS popups. This new map can be shared around to the public so that they can see what's where. It would automatically update every day or so, so that if you map new POIs, that would seamlessly show up on your map.</p>
<p>I know OpenStreetBrowser can do this, but (a) that's really hard to use, and (b) No popups.</p>
<p><em>If this doesn't exist, I'll create it myself, but don't want to re-invent the wheel</em></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-datadisplay" rel="tag" title="see questions tagged &#39;datadisplay&#39;">datadisplay</span> <span class="post-tag tag-link-pois" rel="tag" title="see questions tagged &#39;pois&#39;">pois</span> <span class="post-tag tag-link-display" rel="tag" title="see questions tagged &#39;display&#39;">display</span> <span class="post-tag tag-link-derivative" rel="tag" title="see questions tagged &#39;derivative&#39;">derivative</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Jun '12, 10:37</strong></p>
<img src="https://secure.gravatar.com/avatar/16e12e337f6edc3750681492656097ed?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rorym&#39;s gravatar image" />
<p><span>rorym</span><br />
<span class="score" title="5358 reputation points"><span>5.4k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="49 badges"><span class="silver">●</span><span class="badgecount">49</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rorym has 18 accepted answers">11%</span></p>
</div>
</div>
<div id="comments-container-13497" class="comments-container">
&#10;</div>
<div id="comment-tools-13497" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13497-form-container" class="comment-form-container">
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

<span id="13498"></span>

<div id="answer-container-13498" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-13498-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13498-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-13498-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="rorym has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There's a multitude of special-use POI maps like the ones you mention, but I'm not aware of any generic solution where anyone can simply create their own POI map.</p>
<p>The main technical hurdle with that is that you have to keep a reasonably current database of all POIs, and if you want to do it right, you'll not only look at nodes but also at ways (e.g. a shop need not be a node - it could be a building outline way as well). There are some community-operated databases that support thematic queries (e.g. XAPI, Overpass) but building a map where every zoom an pan action sends a new request to them would likely bring them to their knees and would not make for a nice map browsing experience either.</p>
<p>It's not an unsolvable problem but it does require a decent server to run the database on; it cannot be solved by Javascript hacking alone.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Jun '12, 11:13</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Jun '12, 11:13</strong> </span></p>
</div>
</div>
<div id="comments-container-13498" class="comments-container">
&#10;</div>
<div id="comment-tools-13498" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13498-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="13503"></span>

<div id="answer-container-13503" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-13503-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13503-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-13503-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In addition to what Frederik wrote to you, it is possible to do this if with low resources (read cheap webspace) if you do the data processing beforehand. This is a possible approach if there is not much data you want to filter (i.e. it is either a key/combination that is not very much in use or you are satisfied with a small extract like a city) and you don't care that the data is some days old (dependent how old your data is, of course you can also recreate and upload this every day).</p>
<p>With <code>osmconvert</code> and the <code>--all-to-nodes</code> option you can convert all ways and some kind of relations into node-objects. In a second pass you would filter the desired stuff out, e.g. with <code>osmfilter</code>. The resulting files would then be converted again and used in Openlayers or similar for display.</p>
<p>If you want to do it generically (for all tags that are in OSM) you will have to get a database copy of all the data.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Jun '12, 16:57</strong></p>
<img src="https://secure.gravatar.com/avatar/f09c0b7a655fed386e070e036e2da248?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dieterdreist&#39;s gravatar image" />
<p><span>dieterdreist</span><br />
<span class="score" title="3677 reputation points"><span>3.7k</span></span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="67 badges"><span class="bronze">●</span><span class="badgecount">67</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dieterdreist has 4 accepted answers">3%</span></p>
</div>
</div>
<div id="comments-container-13503" class="comments-container">
&#10;</div>
<div id="comment-tools-13503" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13503-form-container" class="comment-form-container">
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

