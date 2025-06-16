+++
type = "question"
title = "embed.html Marker Problem"
description = '''I haVe embeded a OSM-POI in a Website using the Iframe-Method (Export to HTML). In Firefox and Chrome this works like a charm. In Inernet Explorer (versions 10 and 11) the iframe remains grey. If i open the embeded url (https://www.openstreetmap.org/export/embed.html?bbox=15.417423248291016%2C48.5488...'''
date = "2015-02-24T11:04:00Z"
lastmod = "2015-02-24T16:50:00Z"
weight = 41312
keywords = [ "osm.org", "javascript", "grey", "embed.html", "error" ]
aliases = [ "/questions/41312" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [embed.html Marker Problem](/questions/41312/embedhtml-marker-problem)

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
<span id="post-41312-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41312-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-41312-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I haVe embeded a OSM-POI in a Website using the Iframe-Method (Export to HTML).</p>
<p>In Firefox and Chrome this works like a charm. In Inernet Explorer (versions 10 and 11) the iframe remains grey.</p>
<p>If i open the embeded url (<a href="https://www.openstreetmap.org/export/embed.html?bbox=15.417423248291016%2C48.54885900556121%2C15.431585311889647%2C48.55517964627281&amp;layer=mapnik&amp;marker=48.55201942461214%2C15.424504280090332"><code>https://www.openstreetmap.org/export/embed.html?bbox=15.417423248291016%2C48.54885900556121%2C15.431585311889647%2C48.55517964627281&amp;layer=mapnik&amp;marker=48.55201942461214%2C15.424504280090332</code></a>) in a new Browser Window i get the following error in the javascript console:</p>
<pre><code>SCRIPT5009: &quot;OSM&quot; ist undefiniert
Datei: embed-5dc5be9a8305fd6a9248aec4b2960eca.js, Zeile: 4, Spalte: 32013</code></pre>
<p>Example Website (in german): <a href="http://www.kfz-gassner.at/">http://www.kfz-gassner.at/</a></p>
<p>Is there something wrong with osm's embed.html?</p>
<p>EDIT: It seems other Browsers have the same Problem. The reason why it worked in FF an Chrome was because elements were retrieved from cache.</p>
<p>EDIT 2: The Javascript error is related with setting markers. If i open the url <a href="https://www.openstreetmap.org/export/embed.html?bbox=15.417423248291016%2C48.54885900556121%2C15.431585311889647%2C48.55517964627281&amp;layer=mapnik"><code>https://www.openstreetmap.org/export/embed.html?bbox=15.417423248291016%2C48.54885900556121%2C15.431585311889647%2C48.55517964627281&amp;layer=mapnik</code></a> (without <code>&amp;marker=48.55201942461214%2C15.424504280090332</code>) the map shows up. Firefox javascript error with marker:</p>
<pre><code>ReferenceError: OSM is not defined
https://www.openstreetmap.org/assets/embed-5dc5be9a8305fd6a9248aec4b2960eca.js
Line 4
...arker(e.marker.split(&quot;,&quot;),{icon:L.icon({iconUrl:OSM.MARKER_ICON,iconSize:new L.P...</code></pre>
<p>EDIT 3: Now (14:55) the Bug is fixed.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm.org" rel="tag" title="see questions tagged &#39;osm.org&#39;">osm.org</span> <span class="post-tag tag-link-javascript" rel="tag" title="see questions tagged &#39;javascript&#39;">javascript</span> <span class="post-tag tag-link-grey" rel="tag" title="see questions tagged &#39;grey&#39;">grey</span> <span class="post-tag tag-link-embed.html" rel="tag" title="see questions tagged &#39;embed.html&#39;">embed.html</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span>
</div>
<div id="question-controls" class="post-controls">
<div class="community-wiki">
This question is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Feb '15, 11:04</strong></p>
<img src="https://secure.gravatar.com/avatar/f15c2c019035eb3d529ec6659be174da?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DonatelloXX&#39;s gravatar image" />
<p><span>DonatelloXX</span><br />
<span class="score" title="61 reputation points">61</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DonatelloXX has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Feb '15, 17:49</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-41312" class="comments-container">
<span id="41318"></span>
<div id="comment-41318" class="comment">
<div id="post-41318-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>and what is the fix to the bug?! Let others with the same problem know it. Update: thanks, <a href="https://help.openstreetmap.org/users/867/vincent-de-phily"></a><a href="https://help.openstreetmap.org/users/867/vincent-de-phily">@Vincent</a>!</p>
</div>
<div id="comment-41318-info" class="comment-info">
<span class="comment-age">(24 Feb '15, 14:45)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-41312" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41312-form-container" class="comment-form-container">
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

<span id="41322"></span>

<div id="answer-container-41322" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-41322-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41322-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-41322-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="aseerel4c26 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Separately <a href="https://github.com/openstreetmap/openstreetmap-website/issues/909">reported and fixed</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Feb '15, 16:50</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-41322" class="comments-container">
&#10;</div>
<div id="comment-tools-41322" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41322-form-container" class="comment-form-container">
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

