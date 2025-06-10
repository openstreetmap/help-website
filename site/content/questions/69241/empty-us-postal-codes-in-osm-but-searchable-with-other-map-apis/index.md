+++
type = "question"
title = "Empty US postal codes in OSM but searchable with other map APIs"
description = '''Hi, My use case is to do forward geocoding using on premise Nominatim/OSM API for US region.  So far, we have discovered about 2600 post codes that OSM does not recognize, but the same set of post codes return a valid response from other commercial APIs like Bing, USPS etc.  Post codes 10043, 36685,...'''
date = "2019-05-20T09:26:00Z"
lastmod = "2019-05-21T16:04:00Z"
weight = 69241
keywords = [ "postalcode", "geodata", "nominatim", "usa", "missing" ]
aliases = [ "/questions/69241" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Empty US postal codes in OSM but searchable with other map APIs](/questions/69241/empty-us-postal-codes-in-osm-but-searchable-with-other-map-apis)

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
<span id="post-69241-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69241-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-69241-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, My use case is to do forward geocoding using on premise Nominatim/OSM API for US region. So far, we have discovered about 2600 post codes that OSM does not recognize, but the same set of post codes return a valid response from other commercial APIs like Bing, USPS etc. Post codes 10043, 36685, 99711 are such examples. Also, if I do reverse geocoding with lat/long obtained from other sources for the list of 2600+ post codes we have, Nominatim returns a different post code.</p>
<p>Please let me know if :</p>
<ul>
<li>this is an expected behavior?</li>
<li>there was a reason why these post codes were dropped - like they are not valid anymore; invalid codes etc.?</li>
<li>there is a process within OSM community to drop/update such data regularly based on any rules (and what those rules are, if any)?</li>
</ul>
<p>Thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-postalcode" rel="tag" title="see questions tagged &#39;postalcode&#39;">postalcode</span> <span class="post-tag tag-link-geodata" rel="tag" title="see questions tagged &#39;geodata&#39;">geodata</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-usa" rel="tag" title="see questions tagged &#39;usa&#39;">usa</span> <span class="post-tag tag-link-missing" rel="tag" title="see questions tagged &#39;missing&#39;">missing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 May '19, 09:26</strong></p>
<img src="https://secure.gravatar.com/avatar/7d0a0ee22bd5801ffd33075d7d20c2cb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="globetrotter&#39;s gravatar image" />
<p><span>globetrotter</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="globetrotter has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 May '19, 11:21</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span></p>
</div>
</div>
<div id="comments-container-69241" class="comments-container">
&#10;</div>
<div id="comment-tools-69241" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69241-form-container" class="comment-form-container">
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

<span id="69247"></span>

<div id="answer-container-69247" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69247-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69247-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-69247-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In the US OSM is lacking a lot of post codes (they just haven't been mapped yet). Nominatim (i.e. the Nominatim hosted on the OSM web site) draws on TIGER data additionally to the OSM data to find post codes and house numbers in the US. If the postcode is not found it seems to be not present in the TIGER data. I have no idea if Nominatim constantly updates this data set or if a snap shot from some point in the past is used.</p>
<p>Looking up 10043 it appears to me this is an individual post code for Citibank. It's likely that only geographic post codes are used to pinpoint objects but not post codes designated to entities.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 May '19, 14:49</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-69247" class="comments-container">
<span id="69256"></span>
<div id="comment-69256" class="comment">
<div id="post-69256-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/10133/tzorn">@TZorn</a> does it mean that data like Citibank's would not be available in TIGER? I have imported TIGER 2018 data, which is the latest, into our on-premise OSM database.</p>
</div>
<div id="comment-69256-info" class="comment-info">
<span class="comment-age">(21 May '19, 09:39)</span> <span class="comment-user userinfo">globetrotter</span>
</div>
</div>
<span id="69258"></span>
<div id="comment-69258" class="comment">
<div id="post-69258-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I have no clue. It was just a hypothesis seeing your issue. Maybe someone else here has more insights.</p>
</div>
<div id="comment-69258-info" class="comment-info">
<span class="comment-age">(21 May '19, 11:20)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
<span id="69261"></span>
<div id="comment-69261" class="comment">
<div id="post-69261-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>TIGER doesn't have USPS zip codes, but rather "Zip Code Tabulation Areas" (ZCTA) which aggregate zip codes by block for Census purposes. This makes them somewhat useful for zip codes that cover large areas, but otherwise of limited use. (See also the wikipedia page: <a href="https://en.wikipedia.org/wiki/ZIP_Code_Tabulation_Area)">https://en.wikipedia.org/wiki/ZIP_Code_Tabulation_Area)</a></p>
<p>The wikipedia page about zip codes has a good reminder about their limitations for other purposes: "Despite the geographic derivation of most ZIP Codes, the codes themselves do not represent geographic regions; in general, they correspond to address groups or delivery routes. As a consequence, ZIP Code "areas" can overlap, be subsets of each other, or be artificial constructs with no geographic area"</p>
</div>
<div id="comment-69261-info" class="comment-info">
<span class="comment-age">(21 May '19, 16:04)</span> <span class="comment-user userinfo">neuhausr</span>
</div>
</div>
</div>
<div id="comment-tools-69247" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69247-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="69249"></span>

<div id="answer-container-69249" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69249-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69249-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-69249-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Usually it's missing OSM data, sometimes addresses have been mapped wrong (typos). Just last week I added a missing 5 digit US postcode, specifically I added a postcode to an elementary school. Commercial providers often license data from the US Postal Service which includes PO boxes or postalcodes assigned to companies, that licensed data cannot be imported into OpenStreetMap. Can you share your list of missing 5 digit postal codes, e.g. on <a href="https://pastebin.com/">https://pastebin.com/</a> ?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 May '19, 15:02</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-69249" class="comments-container">
<span id="69255"></span>
<div id="comment-69255" class="comment">
<div id="post-69255-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/150/mtmail"></a><a href="https://help.openstreetmap.org/users/150/mtmail">@mtmail</a> thank you, for the details. the list of missing zip codes that we discovered is available here: <a href="https://pastebin.com/wwbcPJqN">https://pastebin.com/wwbcPJqN</a></p>
</div>
<div id="comment-69255-info" class="comment-info">
<span class="comment-age">(21 May '19, 09:35)</span> <span class="comment-user userinfo">globetrotter</span>
</div>
</div>
</div>
<div id="comment-tools-69249" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69249-form-container" class="comment-form-container">
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

