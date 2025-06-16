+++
type = "question"
title = "Troubleshooting Maproulette"
description = '''Im trying to craft a Maproulette challenge to find parking with access-tags with this query: {{geocodeArea:bergen}}-&amp;gt;.searchArea; (  node[&quot;amenity&quot;=&quot;parking&quot;][&quot;access&quot;!~&quot;.*&quot;](area.searchArea);  way[&quot;amenity&quot;=&quot;parking&quot;][&quot;access&quot;!~&quot;.*&quot;](area.searchArea);  relation[&quot;amenity&quot;=&quot;parking&quot;][&quot;access&quot;!~&quot;.*...'''
date = "2017-09-23T22:09:00Z"
lastmod = "2017-09-25T20:13:00Z"
weight = 59806
keywords = [ "overpass", "maproulette" ]
aliases = [ "/questions/59806" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Troubleshooting Maproulette](/questions/59806/troubleshooting-maproulette)

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
<span id="post-59806-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-59806-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-59806-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Im trying to craft a Maproulette challenge to find parking with access-tags with <a href="http://overpass-turbo.eu/s/rVs">this</a> query:</p>
<pre><code>{{geocodeArea:bergen}}-&gt;.searchArea;
(
  node[&quot;amenity&quot;=&quot;parking&quot;][&quot;access&quot;!~&quot;.*&quot;](area.searchArea);
  way[&quot;amenity&quot;=&quot;parking&quot;][&quot;access&quot;!~&quot;.*&quot;](area.searchArea);
  relation[&quot;amenity&quot;=&quot;parking&quot;][&quot;access&quot;!~&quot;.*&quot;](area.searchArea);
);
out body geom qt;
&gt;;</code></pre>
<p>But when I build the challenge it fails (Status: failed).</p>
<p>How can I troubleshoot what the problem is? The query gives me valid data when ran in Overpass and I can't find any logs or errors at the Maproulette website.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-maproulette" rel="tag" title="see questions tagged &#39;maproulette&#39;">maproulette</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Sep '17, 22:09</strong></p>
<img src="https://secure.gravatar.com/avatar/f882e7865ffe23339fbaa71c9f576065?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="FredrikLindseth&#39;s gravatar image" />
<p><span>FredrikLindseth</span><br />
<span class="score" title="815 reputation points">815</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="24 badges"><span class="silver">●</span><span class="badgecount">24</span></span><span title="35 badges"><span class="bronze">●</span><span class="badgecount">35</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="FredrikLindseth has 2 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-59806" class="comments-container">
&#10;</div>
<div id="comment-tools-59806" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-59806-form-container" class="comment-form-container">
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

<span id="59815"></span>

<div id="answer-container-59815" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-59815-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-59815-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-59815-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="FredrikLindseth has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The geocodeArea in <code>{{geocodeArea:bergen}}-&gt;.searchArea;</code> originated with Overpass-Turbo and likely isn't supported by Maproulette. Replacing it with the Overpass API area id will probably get it to work.</p>
<p>The <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#By_element_id">Overpass QL documentation</a> describes area ids as follows:</p>
<pre><code>Note that area ids need to be derived from an existing OSM way by adding 2400000000 to its OSM id or in case of a relation by adding 3600000000 respectively.</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Sep '17, 02:31</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-59815" class="comments-container">
<span id="59832"></span>
<div id="comment-59832" class="comment">
<div id="post-59832-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That did fix my problem! Thanks.</p>
</div>
<div id="comment-59832-info" class="comment-info">
<span class="comment-age">(25 Sep '17, 20:13)</span> <span class="comment-user userinfo">FredrikLindseth</span>
</div>
</div>
</div>
<div id="comment-tools-59815" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-59815-form-container" class="comment-form-container">
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

