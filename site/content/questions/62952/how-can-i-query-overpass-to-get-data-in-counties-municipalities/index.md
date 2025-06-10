+++
type = "question"
title = "How can I query overpass to get data in counties-&gt;municipalities?"
description = '''I want to create a tricky overpass query, but im not sure how to do it and im hoping someone knows the answer I want to  Find all counties in Norway (admin_level=4) Find all municipalities in these counties (admin_level=7) Find all place=farm in these municipalities Output a list of some sorts where...'''
date = "2018-04-08T19:30:00Z"
lastmod = "2018-04-12T00:42:00Z"
weight = 62952
keywords = [ "overpass", "overpass-turbo", "overpass-ql" ]
aliases = [ "/questions/62952" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How can I query overpass to get data in counties-\>municipalities?](/questions/62952/how-can-i-query-overpass-to-get-data-in-counties-municipalities)

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
<span id="post-62952-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62952-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-62952-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to create a tricky overpass query, but im not sure how to do it and im hoping someone knows the answer</p>
<p>I want to</p>
<ol>
<li>Find all counties in Norway (admin_level=4)</li>
<li>Find all municipalities in these counties (admin_level=7)</li>
<li>Find all place=farm in these municipalities</li>
<li>Output a list of some sorts where its possible to separate the municipalities</li>
</ol>
<p>I did try to create something in overpass-turbo, but it quickly became a mess and didn't output what I wanted</p>
<p>Help!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span> <span class="post-tag tag-link-overpass-ql" rel="tag" title="see questions tagged &#39;overpass-ql&#39;">overpass-ql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Apr '18, 19:30</strong></p>
<img src="https://secure.gravatar.com/avatar/f882e7865ffe23339fbaa71c9f576065?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="FredrikLindseth&#39;s gravatar image" />
<p><span>FredrikLindseth</span><br />
<span class="score" title="815 reputation points">815</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="24 badges"><span class="silver">●</span><span class="badgecount">24</span></span><span title="35 badges"><span class="bronze">●</span><span class="badgecount">35</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="FredrikLindseth has 2 accepted answers">13%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Apr '18, 19:45</strong> </span></p>
</div>
</div>
<div id="comments-container-62952" class="comments-container">
&#10;</div>
<div id="comment-tools-62952" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62952-form-container" class="comment-form-container">
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

<span id="62962"></span>

<div id="answer-container-62962" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-62962-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62962-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-62962-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="FredrikLindseth has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It's currently not possible to restrict an <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#By_area_.28area.29">area query with an area</a>, so it is necessary to use map_to_area calls to work down through the areas.</p>
<p>You can see at the top I've commented out the code to fetch all the admin_level 4 entities in Norway and instead just fetch 1 of them, because the script times out with more than 1. Anyway, <a href="http://overpass-turbo.eu/s/xKi">this script</a> emits the tags for each admin_level=4 and then emits the tags for each admin_level=7 and then any place=farm found within that admin_level=7. So processed as a stream, each farm will belong to the last seen county and municipality.</p>
<pre><code>[out:json][timeout:150];
//area[admin_level=2]//[&quot;name:en&quot;=Norway]-&gt;.country;
//(way(area.country)[admin_level=4];
// rel(area.country)[admin_level=4];
//)-&gt;.counties;
( rel[admin_level=4][name=Nordland];
  //rel[admin_level=4][name=&quot;Trøndelag&quot;];
)-&gt;.counties;
foreach.counties(
  out tags;
  map_to_area-&gt;.countya;
  (way(area.countya)[admin_level=7];
   rel(area.countya)[admin_level=7];
  )-&gt;.munis;
  foreach.munis(
    out tags;
    map_to_area-&gt;.munia;
    (node(area.munia)[place=farm];
     way(area.munia)[place=farm];
     rel(area.munia)[place=farm];
     );
    out center;
  );
);</code></pre>
<p>You can also look at <a href="https://github.com/drolbr/Overpass-API/issues/187">https://github.com/drolbr/Overpass-API/issues/187</a> for some discussion of how to fetch points with containing areas.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Apr '18, 19:32</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-62962" class="comments-container">
<span id="62983"></span>
<div id="comment-62983" class="comment">
<div id="post-62983-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That worked very well! I changed the output to <code>out number</code> too, since that was what I really was after.</p>
</div>
<div id="comment-62983-info" class="comment-info">
<span class="comment-age">(12 Apr '18, 00:42)</span> <span class="comment-user userinfo">FredrikLindseth</span>
</div>
</div>
</div>
<div id="comment-tools-62962" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62962-form-container" class="comment-form-container">
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

