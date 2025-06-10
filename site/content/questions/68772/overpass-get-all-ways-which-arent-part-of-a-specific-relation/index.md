+++
type = "question"
title = "[overpass] Get all ways which aren&#x27;t part of a specific relation"
description = '''I&#x27;m trying to write an Overpass query to get all ways (filtered with a specific tag) which aren&#x27;t included in a relation (with a specific tag). Here is my query (edited after maxerickson&#x27;s answer): https://overpass-turbo.eu/s/HXj // Collect all ways with piste:type=nordic and store the result in a v...'''
date = "2019-04-12T14:17:00Z"
lastmod = "2019-04-26T18:52:00Z"
weight = 68772
keywords = [ "overpass" ]
aliases = [ "/questions/68772" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [\[overpass\] Get all ways which aren't part of a specific relation](/questions/68772/overpass-get-all-ways-which-arent-part-of-a-specific-relation)

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
<span id="post-68772-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68772-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-68772-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm trying to write an Overpass query to get all ways (filtered with a specific tag) which aren't included in a relation (with a specific tag).</p>
<p>Here is my query (edited after maxerickson's answer): <a href="https://overpass-turbo.eu/s/HXj">https://overpass-turbo.eu/s/HXj</a></p>
<pre><code>// Collect all ways with piste:type=nordic and store the result in a variable .all
way({{bbox}})[&quot;piste:type&quot;=&quot;nordic&quot;]-&gt;.all;
&#10;// Select all relations, where one of the ways in variable .all is a member
rel[&quot;piste:type&quot;=&quot;nordic&quot;](bw.all);
// ...and for those relations find all related way members
way(r);
&#10;// Calculate the set difference (._ contains all nodes which are member of a relation)
( .all; - ._; );
&#10;// return the result including meta data
out meta;</code></pre>
<p>I followed <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_API_by_Example#Find_all_bus_stops_which_are_not_included_in_a_relation">this example</a>, it's pretty close of what I want to do but for nodes, so I just changed a few things to get ways instead of nodes.</p>
<p>Unfortunately my query doesn't return anything. Do you see anything wrong in my query?</p>
<p>Edit after some debugging:</p>
<p>here a way that the query should return (has a piste:typenordic tag and isn't part of a piste:type=nordic relation): <a href="https://www.openstreetmap.org/way/475719899">https://www.openstreetmap.org/way/475719899</a></p>
<ul>
<li>the way is returned if I tell Overpass to display the .all set: <a href="https://overpass-turbo.eu/s/HXh">https://overpass-turbo.eu/s/HXh</a> → good</li>
<li>the way isn't returned when I search for all way that are part of a relation (lines 5-7): <a href="https://overpass-turbo.eu/s/HXi">https://overpass-turbo.eu/s/HXi</a> → good</li>
<li>so I guess the problem is on the difference between the 2 sets (line 10): why the way 475719899 is removed if it isn't in the ._ set?</li>
</ul>
<p>Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Apr '19, 14:17</strong></p>
<img src="https://secure.gravatar.com/avatar/3465e5058de18b424b5a99b87d284034?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="billux&#39;s gravatar image" />
<p><span>billux</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="billux has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Apr '19, 13:46</strong> </span></p>
</div>
</div>
<div id="comments-container-68772" class="comments-container">
&#10;</div>
<div id="comment-tools-68772" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68772-form-container" class="comment-form-container">
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

<span id="68778"></span>

<div id="answer-container-68778" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68778-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68778-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-68778-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You need something like</p>
<pre><code>area[name=&quot;Sainte-Adèle&quot;]-&gt;.searchArea;
way(area.searchArea)[&quot;piste:type&quot;=&quot;nordic&quot;]-&gt;.all;</code></pre>
<p>to even have anything in <code>.all</code>.</p>
<p>The <code>area</code> query operates on OSM tags, so you have to search based on that. You could use <code>around</code> with a distance and a point (either an OSM node or directly specify lat/lon) if that better matches your intent.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Apr '19, 03:28</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-68778" class="comments-container">
<span id="68781"></span>
<div id="comment-68781" class="comment">
<div id="post-68781-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You're right, actually I wanted to use {{bbox}} first, but replaced it with area when I posted my question. I have updated my question with a link to the Overpass query and more information after trying to debug the query.</p>
</div>
<div id="comment-68781-info" class="comment-info">
<span class="comment-age">(13 Apr '19, 13:53)</span> <span class="comment-user userinfo">billux</span>
</div>
</div>
<span id="68785"></span>
<div id="comment-68785" class="comment">
<div id="post-68785-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I'm not sure <em>why</em>, but naming the second result set helps: <a href="https://overpass-turbo.eu/s/HXB">https://overpass-turbo.eu/s/HXB</a></p>
</div>
<div id="comment-68785-info" class="comment-info">
<span class="comment-age">(13 Apr '19, 17:34)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
<span id="68794"></span>
<div id="comment-68794" class="comment">
<div id="post-68794-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That's strange, I don't understand why ._ can't be used in that case. Anyway the query works as expected now. Thanks!</p>
</div>
<div id="comment-68794-info" class="comment-info">
<span class="comment-age">(14 Apr '19, 22:23)</span> <span class="comment-user userinfo">billux</span>
</div>
</div>
<span id="68972"></span>
<div id="comment-68972" class="comment">
<div id="post-68972-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The <code>.all</code> in the difference statement has <code>._</code> as result set. The next statment <code>._</code> picks that up. Thus, you are subtracting the content of <code>.all</code> from itself. I'm sorry that the syntax is misleading in this case.</p>
</div>
<div id="comment-68972-info" class="comment-info">
<span class="comment-age">(26 Apr '19, 18:52)</span> <span class="comment-user userinfo">Roland Olbricht</span>
</div>
</div>
</div>
<div id="comment-tools-68778" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68778-form-container" class="comment-form-container">
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

