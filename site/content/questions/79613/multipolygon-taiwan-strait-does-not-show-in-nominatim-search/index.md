+++
type = "question"
title = "Multipolygon Taiwan Strait does not show in Nominatim search"
description = '''Hello, When I search &quot;Taiwan Strait&quot; ( https://www.openstreetmap.org/search?query=Taiwan%20Strait ), the correct multipolyon result ( https://www.openstreetmap.org/relation/9348353, it&#x27;s a big one so might take a while to load ) does not shown in the result. I checked the multipolyon in JOSM and it&#x27;...'''
date = "2021-04-11T22:51:00Z"
lastmod = "2021-04-12T11:03:00Z"
weight = 79613
keywords = [ "nominatim", "strait", "multipolygon" ]
aliases = [ "/questions/79613" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Multipolygon Taiwan Strait does not show in Nominatim search](/questions/79613/multipolygon-taiwan-strait-does-not-show-in-nominatim-search)

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
<span id="post-79613-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79613-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-79613-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>When I search "Taiwan Strait" ( <a href="https://www.openstreetmap.org/search?query=Taiwan%20Strait">https://www.openstreetmap.org/search?query=Taiwan%20Strait</a> ), the correct multipolyon result ( <a href="https://www.openstreetmap.org/relation/9348353,">https://www.openstreetmap.org/relation/9348353,</a> it's a big one so might take a while to load ) does not shown in the result.</p>
<p>I checked the multipolyon in JOSM and it's quite complex one.</p>
<p>Is this a bug in Nominatim or issue in the strait multipolygon?</p>
<p>Thanks in advance!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-strait" rel="tag" title="see questions tagged &#39;strait&#39;">strait</span> <span class="post-tag tag-link-multipolygon" rel="tag" title="see questions tagged &#39;multipolygon&#39;">multipolygon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Apr '21, 22:51</strong></p>
<img src="https://secure.gravatar.com/avatar/e39830800041c01c0ad201916e2c4065?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="strongwillow&#39;s gravatar image" />
<p><span>strongwillow</span><br />
<span class="score" title="65 reputation points">65</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="strongwillow has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Apr '21, 22:54</strong> </span></p>
</div>
</div>
<div id="comments-container-79613" class="comments-container">
&#10;</div>
<div id="comment-tools-79613" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79613-form-container" class="comment-form-container">
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

<span id="79616"></span>

<div id="answer-container-79616" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-79616-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79616-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-79616-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Mapping these bays and straits as multipolygons is error prone (they are easy to break), pollutes the database with countless versions (every time someone splits a pice of coastline, a new version of the relation must be uploaded), creates giant objects that complicate editing for everyone (there is a reason we don't map oceans as polygons...), and serves no purpose that could not equally be served by a node. When I encounter polygons like that, I usually replace them with a node. I have done that here now.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Apr '21, 00:06</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-79616" class="comments-container">
<span id="79618"></span>
<div id="comment-79618" class="comment">
<div id="post-79618-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi <a href="https://help.openstreetmap.org/users/104/frederik-ramm">@Frederik</a>, I also don't like this kind of super large multipolygon for all sorts of reasons. Thanks for confirming this is bad mapping.</p>
<p>However I don't quite agree to replace that with just a node. A strait node is rendered usually insignificantly. How about a simple polygon like English Channel: <a href="https://www.openstreetmap.org/way/920269202">https://www.openstreetmap.org/way/920269202</a> It's a rough approximation but it's good enough for different purpose</p>
</div>
<div id="comment-79618-info" class="comment-info">
<span class="comment-age">(12 Apr '21, 09:31)</span> <span class="comment-user userinfo">strongwillow</span>
</div>
</div>
<span id="79621"></span>
<div id="comment-79621" class="comment">
<div id="post-79621-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>That English Channel polygon is terrible. It doesn't even have holes for the Channel Islands. It will break anything which renders water polygons above land.</p>
</div>
<div id="comment-79621-info" class="comment-info">
<span class="comment-age">(12 Apr '21, 11:03)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
</div>
<div id="comment-tools-79616" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79616-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="79614"></span>

<div id="answer-container-79614" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-79614-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79614-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-79614-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The main polygon looks broken when I inspect with the JOSM editor. All elements (ways) exist but there's two gaps and some ways are not in the correct order. Sadly <a href="http://ra.osmsurround.org/analyzeRelation">http://ra.osmsurround.org/analyzeRelation</a> times out for me for this relation, it's huge. Once fixed Nominatim will import it and link the node to the relation (based on position and wikidata id).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Apr '21, 23:06</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-79614" class="comments-container">
<span id="79615"></span>
<div id="comment-79615" class="comment">
<div id="post-79615-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>for example a gap between <a href="https://www.openstreetmap.org/way/207552518">https://www.openstreetmap.org/way/207552518</a> and <a href="https://www.openstreetmap.org/way/225761779">https://www.openstreetmap.org/way/225761779</a></p>
</div>
<div id="comment-79615-info" class="comment-info">
<span class="comment-age">(11 Apr '21, 23:09)</span> <span class="comment-user userinfo">mtmail</span>
</div>
</div>
<span id="79617"></span>
<div id="comment-79617" class="comment">
<div id="post-79617-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for checking. Indeed large multipolygon tends to break</p>
</div>
<div id="comment-79617-info" class="comment-info">
<span class="comment-age">(12 Apr '21, 09:24)</span> <span class="comment-user userinfo">strongwillow</span>
</div>
</div>
</div>
<div id="comment-tools-79614" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79614-form-container" class="comment-form-container">
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

