+++
type = "question"
title = "How to get names from buildings?"
description = '''Hi All, I&#x27;m looking for a way to get the names of buildings in an overpasss query as result. As you can see in the picture below, the line 480228940 has the name &quot;Ehemaliges Hallenbad Wallau&quot;. So I&#x27;m looking for a way to get all the coordinates of e.g. &quot;Hallenbad&quot; buildings in a specific bounding bo...'''
date = "2019-03-14T10:50:00Z"
lastmod = "2019-03-15T08:58:00Z"
weight = 68372
keywords = [ "buildings", "lines", "names" ]
aliases = [ "/questions/68372" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to get names from buildings?](/questions/68372/how-to-get-names-from-buildings)

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
<span id="post-68372-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68372-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-68372-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi All,</p>
<p>I'm looking for a way to get the names of buildings in an overpasss query as result. As you can see in the picture below, the line 480228940 has the name "Ehemaliges Hallenbad Wallau". So I'm looking for a way to get all the coordinates of e.g. "Hallenbad" buildings in a specific bounding box.</p>
<p>Unfortunately I don't have any clue how I to set up the query and any suggestions are welcome!</p>
<p>BR, Tom</p>
<p><img src="https://help.openstreetmap.org/upfiles/Query.png" alt="alt text" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-buildings" rel="tag" title="see questions tagged &#39;buildings&#39;">buildings</span> <span class="post-tag tag-link-lines" rel="tag" title="see questions tagged &#39;lines&#39;">lines</span> <span class="post-tag tag-link-names" rel="tag" title="see questions tagged &#39;names&#39;">names</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Mar '19, 10:50</strong></p>
<img src="https://secure.gravatar.com/avatar/655b1b625bf0b298bfb575336fda85e9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GIS_Wanderer&#39;s gravatar image" />
<p><span>GIS_Wanderer</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GIS_Wanderer has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-68372" class="comments-container">
&#10;</div>
<div id="comment-tools-68372" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68372-form-container" class="comment-form-container">
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

<span id="68373"></span>

<div id="answer-container-68373" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68373-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68373-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-68373-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>All <a href="https://wiki.openstreetmap.org/wiki/Buildings">OSM Buildings</a> are supposed to be tagged with <code>building=*</code>, so searching for that should work. Unfortunately, it seems that there's not a lot of buildings with names in that area :(</p>
<p>Here's the query: (<a href="http://overpass-turbo.eu/s/GZx">Try it</a>)</p>
<pre><code>[timeout: 240]
[out: json]
// choose a bbox:
[bbox: {{bbox}}] // search within the bbox of the map to the right (in-browser only)
// [bbox: south, west, north, east] // your custom bbox
;
&#10;// all nodes, ways or relations with a &#39;building=*&#39; tag and a &#39;name=*&#39; tag
// (remove the &quot; [name]&quot; to find all buildings)
(
  node [building] [name];
  way  [building] [name];
  rel  [building] [name];
);
&#10;
// choose an output option:
out geom; // output coordinate data needed for display + tags.
//out tags; // output only the tags</code></pre>
<p>The names, and all other tags, are included in the data returned by the query.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Mar '19, 13:48</strong></p>
<img src="https://secure.gravatar.com/avatar/c75de9e74a304beb41b705c6bba09db5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="owoce&#39;s gravatar image" />
<p><span>owoce</span><br />
<span class="score" title="61 reputation points">61</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="owoce has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-68373" class="comments-container">
<span id="68376"></span>
<div id="comment-68376" class="comment">
<div id="post-68376-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>you can get the centers by replacing <code>out geom;</code> with <code>out center;</code>. take a look <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Standalone_queries">here</a> for a list of all the <code>out</code> options.</p>
</div>
<div id="comment-68376-info" class="comment-info">
<span class="comment-age">(14 Mar '19, 17:20)</span> <span class="comment-user userinfo">owoce</span>
</div>
</div>
<span id="68379"></span>
<div id="comment-68379" class="comment">
<div id="post-68379-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/16398/owoce">@owoce</a> Sorry, your comment ended up here. I tried to convert <a href="https://help.openstreetmap.org/users/16400/gis_wanderer">@GIS_Wanderer</a>'s answer to a comment but OSQA (the software running OSM help) screwed up because there is a bug which prevents to convert answers that have been edited. I can't move your comment back because then another error occurs :(</p>
</div>
<div id="comment-68379-info" class="comment-info">
<span class="comment-age">(15 Mar '19, 08:58)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-68373" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68373-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="68374"></span>

<div id="answer-container-68374" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68374-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68374-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-68374-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi owoce,</p>
<p>thanks for your fast feedback! I checked out your code and indeed the map stays empty. Even when I try the complete name</p>
<pre><code>way  [building] [name=&#39;Ehemaliges Hallenbad Wallau&#39;];</code></pre>
<p>the map stays empty. Is there a way to use place holders instead? E.g. <em>hallenbad</em> or even only <em>bad</em>.</p>
<p>I tried some other queries and for now the ouput are highlighted lines of the building shown in the map. Is there a way to get only one GPS location (lat / lon) per result?</p>
<p>BR, Tom</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Mar '19, 15:19</strong></p>
<img src="https://secure.gravatar.com/avatar/655b1b625bf0b298bfb575336fda85e9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GIS_Wanderer&#39;s gravatar image" />
<p><span>GIS_Wanderer</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GIS_Wanderer has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Mar '19, 15:20</strong> </span></p>
</div>
</div>
<div id="comments-container-68374" class="comments-container">
<span id="68375"></span>
<div id="comment-68375" class="comment">
<div id="post-68375-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>The example in your screenshot is tagged as a construction area, not a building, so it won't show up in a query for buildings. If that's an example of the objects you're trying to retrieve, then it might not be buildings that you need to search for. Can you maybe edit your question to add more context about your ultimate goal? For example, once you get your results, what will you be doing with them? That might help us suggest a better way to reach that goal.</p>
</div>
<div id="comment-68375-info" class="comment-info">
<span class="comment-age">(14 Mar '19, 15:39)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
</div>
<div id="comment-tools-68374" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68374-form-container" class="comment-form-container">
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

