+++
type = "question"
title = "overpass query addresses near a street with the same name and a special tag"
description = '''For a mapping project we have identified a large number of streets that are about to change names.  So they are easy to query (this is just one of 15 examples).  Now we need to map the affected addresses. I&#x27;m thinking of a loop that will go through the highways. It should return any objects tagged w...'''
date = "2018-10-24T19:05:00Z"
lastmod = "2018-10-24T21:58:00Z"
weight = 66446
keywords = [ "overpass", "overpass-turbo" ]
aliases = [ "/questions/66446" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [overpass query addresses near a street with the same name and a special tag](/questions/66446/overpass-query-addresses-near-a-street-with-the-same-name-and-a-special-tag)

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
<span id="post-66446-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66446-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-66446-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>For a <a href="https://wiki.openstreetmap.org/wiki/WikiProject_Belgium/Municipality_Fusions">mapping project</a> we have identified a large number of streets that are about to change names.<br />
So they are <a href="http://overpass-turbo.eu/s/D5k">easy to query</a> (this is just one of 15 examples).</p>
<p>Now we need to map the affected addresses. I'm thinking of a loop that will go through the highways. It should return any objects tagged with and addr:street that is identical to one of the "name" values of the previous query. But only if they are within, say, 250 meter of the object with this name. From what I've seen, this should be possible, but I don't really know how to start.</p>
<p>Once the streetname changes take effect, the query can be adapted to compare highway old_name to addr:street, a query which should then over time result in an empty dataset.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Oct '18, 19:05</strong></p>
<img src="https://secure.gravatar.com/avatar/1df835d513b1282e0edd7405d29cd8d9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joost%20schouppe&#39;s gravatar image" />
<p><span>joost schouppe</span><br />
<span class="score" title="3427 reputation points"><span>3.4k</span></span><span title="24 badges"><span class="badge1">●</span><span class="badgecount">24</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="87 badges"><span class="bronze">●</span><span class="badgecount">87</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joost schouppe has 9 accepted answers">12%</span> </br></p>
</div>
</div>
<div id="comments-container-66446" class="comments-container">
&#10;</div>
<div id="comment-tools-66446" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66446-form-container" class="comment-form-container">
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

<span id="66447"></span>

<div id="answer-container-66447" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-66447-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66447-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-66447-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="joost schouppe has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Try <a href="http://overpass-turbo.eu/s/D5q">http://overpass-turbo.eu/s/D5q</a></p>
<pre><code>[out:xml][timeout:120];
( area[&quot;name&quot;=&quot;Vlaanderen&quot;][&quot;admin_level&quot;=&quot;4&quot;]; )-&gt;.b;
( area[&quot;name&quot;=&quot;Deinze&quot;][admin_level=8](area.b); )-&gt;.a;
way[&quot;highway&quot;][name=Warandestraat](area.a)(area.b)-&gt;.streets;
foreach.streets-&gt;.street(
  nwr(around.street:250)[&quot;addr:street&quot;](if: t[&quot;addr:street&quot;]==street.set(t[&quot;name&quot;]));
  (._;&gt;;);
  out;
);</code></pre>
<p>The foreach statement goes through the input set one element at a time storing the element in .street so it is available inside of the if: block.</p>
<p>I stuck the street name in there to speed up testing, you'd obviously want to remove that.</p>
<p>(The blog posts about recent releases, like <a href="https://dev.overpass-api.de/blog/final_0_7_54.html">https://dev.overpass-api.de/blog/final_0_7_54.html</a> continue to be the best source of examples for stuff like the if: block there)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Oct '18, 20:04</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-66447" class="comments-container">
<span id="66448"></span>
<div id="comment-66448" class="comment">
<div id="post-66448-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks! Those release notes are a bit above me unfortunately. I try to learn something every time though. Anyway, if I try this for an entire level 8 admin area, it seems to be too much for the server. But we can always do it one by one if needed.</p>
</div>
<div id="comment-66448-info" class="comment-info">
<span class="comment-age">(24 Oct '18, 20:15)</span> <span class="comment-user userinfo">joost schouppe</span>
</div>
</div>
</div>
<div id="comment-tools-66447" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66447-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="66453"></span>

<div id="answer-container-66453" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-66453-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66453-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-66453-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="http://overpass-turbo.eu/s/D5H">http://overpass-turbo.eu/s/D5H</a></p>
<pre><code>[out:xml][timeout:120];
area[&quot;name&quot;=&quot;Vlaanderen&quot;][&quot;admin_level&quot;=&quot;4&quot;];
//if you want to restrit to one municipality, uncomment the next line
//area[&quot;name&quot;=&quot;Deinze&quot;][admin_level=8](area);
way[&quot;fixme:name&quot;](area);
way._[&quot;highway&quot;]-&gt;.streets;
foreach.streets-&gt;.street(
  nwr(around.street:250)[&quot;addr:street&quot;](if: t[&quot;addr:street&quot;]==street.set(t[&quot;name&quot;]));
  out geom;
);</code></pre>
<p>minors improvements based on maxerickson query to avoid "out of memory" issue for the whole set :</p>
<ul>
<li>reduce the (area.a)(area.b) to only one area test (the 2nd area is already a part of the first one)</li>
<li>line 5 : avoid to store the area with a name due we only use it once at the next line</li>
<li>line 5+6 : get first list with "fixme:name" (less objets) before checking if a highway tag exist</li>
<li>line 9 : change "(._;&gt;;); out;" into "out geom;"</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Oct '18, 21:58</strong></p>
<img src="https://secure.gravatar.com/avatar/b0e6f32e447cf622521868f58d0792d5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="marc_marc&#39;s gravatar image" />
<p><span>marc_marc</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="marc_marc has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-66453" class="comments-container">
&#10;</div>
<div id="comment-tools-66453" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66453-form-container" class="comment-form-container">
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

