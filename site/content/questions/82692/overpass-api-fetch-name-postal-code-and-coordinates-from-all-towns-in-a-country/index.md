+++
type = "question"
title = "Overpass API: fetch name, postal code and coordinates from all towns in a country"
description = '''Hello, I&#x27;m here from a project where we need structured geodata. For this, I found the Overpass API, which seems to do exactly what we need. The Reason for this is that OpenGeoDB is currently offline, and we want to cover a wider area than what we currently have. We basically need the name, zip code...'''
date = "2021-11-26T09:52:00Z"
lastmod = "2021-11-26T14:54:00Z"
weight = 82692
keywords = [ "overpassapi", "data", "overpass-ql" ]
aliases = [ "/questions/82692" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Overpass API: fetch name, postal code and coordinates from all towns in a country](/questions/82692/overpass-api-fetch-name-postal-code-and-coordinates-from-all-towns-in-a-country)

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
<span id="post-82692-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82692-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82692-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I'm here from a project where we need structured geodata. For this, I found the Overpass API, which seems to do exactly what we need.</p>
<p>The Reason for this is that OpenGeoDB is currently offline, and we want to cover a wider area than what we currently have.</p>
<p>We basically need the name, zip code and coordinates of all cities, towns and villages of a country. So very similar to what OpenGeoDB offered.</p>
<p>Unfortunately I'm not that into the complex topic of OSM data and the Overpass API and I think you guys here know a lot better about it :)</p>
<p>Can you help me to build an Overpass API query that can provide this data?</p>
<p>With kind regards Lena</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpassapi" rel="tag" title="see questions tagged &#39;overpassapi&#39;">overpassapi</span> <span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span> <span class="post-tag tag-link-overpass-ql" rel="tag" title="see questions tagged &#39;overpass-ql&#39;">overpass-ql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Nov '21, 09:52</strong></p>
<img src="https://secure.gravatar.com/avatar/0fd41c0e2a83be66e0ddaf487defe8c3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Feuerhamster&#39;s gravatar image" />
<p><span>Feuerhamster</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Feuerhamster has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-82692" class="comments-container">
&#10;</div>
<div id="comment-tools-82692" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82692-form-container" class="comment-form-container">
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

<span id="82693"></span>

<div id="answer-container-82693" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82693-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82693-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-82693-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Trying to do this with the publicly available Overpass API is going to be a painful road paved with lots of timeouts. (Painful for you <em>and</em> the server.) So don't do it. Instead, take the OpenStreetMap data for your country of interest (eg from download.geofabrik.de) and then either filter out the "place nodes" with a tool like <code>osmium</code> or <code>osmfilter</code>, or load the while file into a PostGIS database with the <code>osm2pgsql</code> tool and then run SQL queries to your heart's content.</p>
<p>Zip codes is going to be a problem, they will only be available for very few countries and they are not usually linked directly to a place (since the same place can have 1, 10, or 100 zip codes). If the country you are looking at <em>has</em> good coverage of post code polygons then you can use the database approach to find out which post code polygon a place is in. If not, you can sometimes at least "guess" by looking at some individual addresses near the centre of the place.</p>
<p>Do not assume that you can simply get from OSM what you previously got from OpenGeoDB without spending a few days on it. As far as I know, OpenGeoDB also has a hierarchy that lets you see which city is in which county is in which state and so on, something that you will have to compute yourself when working with OSM.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Nov '21, 10:21</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-82693" class="comments-container">
&#10;</div>
<div id="comment-tools-82693" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82693-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="82697"></span>

<div id="answer-container-82697" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82697-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82697-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82697-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Sorry not to answer you question, but you might want to look at wikidata instead of OSM for this kind of queries.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Nov '21, 14:54</strong></p>
<img src="https://secure.gravatar.com/avatar/9434692e9afccaf03af5acf20b3a3279?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_mlet&#39;s gravatar image" />
<p><span>H_mlet</span><br />
<span class="score" title="5443 reputation points"><span>5.4k</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="H_mlet has 40 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-82697" class="comments-container">
&#10;</div>
<div id="comment-tools-82697" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82697-form-container" class="comment-form-container">
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

