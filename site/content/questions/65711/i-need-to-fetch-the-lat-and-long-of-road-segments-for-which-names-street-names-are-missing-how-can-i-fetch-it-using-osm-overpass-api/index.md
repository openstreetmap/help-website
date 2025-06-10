+++
type = "question"
title = "I need to fetch the lat and long of road segments for which names (street names) are missing? How can i fetch it using OSM Overpass API?"
description = '''I need to fetch the lat and long of road segments for which names (street names) are missing? How can i fetch it using OSM Overpass API? I tried to tweak a code i already had but it didn&#x27;t yield any result, the code i used is below &amp;lt;osm-script output=&quot;json&quot; timeout=&quot;200&quot;&amp;gt;   &amp;lt;id-query {{nomi...'''
date = "2018-09-03T14:06:00Z"
lastmod = "2018-09-03T16:07:00Z"
weight = 65711
keywords = [ "streetnames" ]
aliases = [ "/questions/65711" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [I need to fetch the lat and long of road segments for which names (street names) are missing? How can i fetch it using OSM Overpass API?](/questions/65711/i-need-to-fetch-the-lat-and-long-of-road-segments-for-which-names-street-names-are-missing-how-can-i-fetch-it-using-osm-overpass-api)

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
<span id="post-65711-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65711-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65711-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I need to fetch the lat and long of road segments for which names (street names) are missing? How can i fetch it using OSM Overpass API? I tried to tweak a code i already had but it didn't yield any result, the code i used is below</p>
<p>&lt;osm-script output="json" timeout="200"&gt; &lt;id-query {{nominatimarea:washington}}="" into="Area"/&gt; &lt;union&gt; &lt;query type="node"&gt; &lt;has-kv k="highway" v="*"/&gt; &lt;has-kv k="name" v=""/&gt; &lt;area-query from="Area"/&gt; &lt;/query&gt; &lt;query type="way"&gt; &lt;has-kv k="highway" v="*"/&gt; &lt;has-kv k="name" v=""/&gt; &lt;area-query from="Area"/&gt; &lt;/query&gt; &lt;query type="relation"&gt; &lt;has-kv k="highway" v="*"/&gt; &lt;has-kv k="name" v=""/&gt; &lt;area-query from="Area"/&gt; &lt;/query&gt; &lt;/union&gt; &lt;union&gt; &lt;item/&gt; &lt;recurse type="down"/&gt; &lt;/union&gt; &lt;print mode="body"/&gt; &lt;/osm-script&gt;</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-streetnames" rel="tag" title="see questions tagged &#39;streetnames&#39;">streetnames</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Sep '18, 14:06</strong></p>
<img src="https://secure.gravatar.com/avatar/aaa0fcd50fb2770a18655928d767cdea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Phaneshwar&#39;s gravatar image" />
<p><span>Phaneshwar</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Phaneshwar has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-65711" class="comments-container">
&#10;</div>
<div id="comment-tools-65711" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65711-form-container" class="comment-form-container">
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

<span id="65717"></span>

<div id="answer-container-65717" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-65717-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65717-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-65717-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Here's the script I use to find unnamed residential highways:</p>
<pre><code>[bbox:{{bbox}}];
way[highway=residential][!name];
out center;</code></pre>
<p>I don't know the xml language but I think you may need to use regex negation to check for missing keys, <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Language_Guide#Negation">https://wiki.openstreetmap.org/wiki/Overpass_API/Language_Guide#Negation</a></p>
<p>I use <code>out center;</code> because it works better for large areas in Overpass Turbo.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Sep '18, 15:25</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-65717" class="comments-container">
<span id="65719"></span>
<div id="comment-65719" class="comment">
<div id="post-65719-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks Max but when i replaced the bbox with actual area name and tried overpass turbo gaveup for memory reasons. can you suggest a more optimzed way i can pull all the roads (not just residential) for a particular area along with lat and long of the segment? thank you again for your help!</p>
</div>
<div id="comment-65719-info" class="comment-info">
<span class="comment-age">(03 Sep '18, 15:38)</span> <span class="comment-user userinfo">Phaneshwar</span>
</div>
</div>
<span id="65720"></span>
<div id="comment-65720" class="comment">
<div id="post-65720-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I doubt the public Overpass instance will work for a large region, especially if you start including service roads and the like. I use that query to clean up Tiger data and there will often be many thousands of unnamed residentials in just part of a state.</p>
<p>Using a pbf extract and <a href="https://wiki.openstreetmap.org/wiki/Osmconvert">osmconvert</a>/<a href="https://wiki.openstreetmap.org/wiki/Osmfilter">osmfilter</a> is probably the simplest way to go.</p>
</div>
<div id="comment-65720-info" class="comment-info">
<span class="comment-age">(03 Sep '18, 15:45)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
<span id="65721"></span>
<div id="comment-65721" class="comment">
<div id="post-65721-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>you should at least exclude anything with noname=yes, assuming you actually want roads without a name that perhaps should have one.</p>
</div>
<div id="comment-65721-info" class="comment-info">
<span class="comment-age">(03 Sep '18, 16:07)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-65717" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65717-form-container" class="comment-form-container">
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

