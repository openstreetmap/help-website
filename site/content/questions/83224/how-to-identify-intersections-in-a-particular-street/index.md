+++
type = "question"
title = "how to identify intersections in a particular street"
description = '''Hi, I greatly need your explanation. I am working on a project and i am to identify all the roads in a particular area. For each of the roads, i&#x27;m to identify and list out all the intersections in order. I donot really know how go about this. Please can somebody give me an explanation? Thanks'''
date = "2022-01-26T20:37:00Z"
lastmod = "2022-01-31T19:50:00Z"
weight = 83224
keywords = [ "intersections" ]
aliases = [ "/questions/83224" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [how to identify intersections in a particular street](/questions/83224/how-to-identify-intersections-in-a-particular-street)

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
<span id="post-83224-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83224-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-83224-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I greatly need your explanation. I am working on a project and i am to identify all the roads in a particular area. For each of the roads, i'm to identify and list out all the intersections in order. I donot really know how go about this. Please can somebody give me an explanation? Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-intersections" rel="tag" title="see questions tagged &#39;intersections&#39;">intersections</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Jan '22, 20:37</strong></p>
<img src="https://secure.gravatar.com/avatar/d91bc4f974e22ffeb60227442e03aafa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Segunlakata&#39;s gravatar image" />
<p><span>Segunlakata</span><br />
<span class="score" title="16 reputation points">16</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Segunlakata has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-83224" class="comments-container">
&#10;</div>
<div id="comment-tools-83224" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83224-form-container" class="comment-form-container">
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

<span id="83229"></span>

<div id="answer-container-83229" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-83229-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83229-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-83229-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This will require some amount of programming. There isn't a web service that does this work for you.</p>
<p>First you must understand that roads can be split into many segments in OSM. The geometry of a street in OSM is represented by nodes with coordinates. Where two streets intersect, they will share the same node.</p>
<p>Hence, one possible approach is:</p>
<ol>
<li>download OSM data for the region of interest.</li>
<li>look at the "way" objects; throw away anything that is not a highway; then combine ways into clusters that have the same street name and where one way ends with the same node the other way begins with, so that you end up with just one way for every street instead of potentially several.</li>
<li>each way consists of several nodes; build an in-memory index that quickly gives you the way for a given node id.</li>
<li>now iterate over all ways, traversing them from westernmost to easternmost node, or whatever makes sense for you, and for each node you encounter, check (using your index) if this node is also in another way than the one you're traversing. if yes, you have found an intersection.</li>
</ol>
<p>Other possible approaches, if you are more comfortable with that, include loading the data into PostGIS and doing everything with SQL commands.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Jan '22, 08:28</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-83229" class="comments-container">
<span id="83277"></span>
<div id="comment-83277" class="comment">
<div id="post-83277-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for your response <a href="https://help.openstreetmap.org/users/104/frederik-ramm">@Frederik Ramm</a>. Your feedback has been very helpful. Can you please re-explain this your statement..."then combine ways into clusters that have the same street name and where one way ends with the same node the other way begins with, so that you end up with just one way for every street instead of potentially several". I am confused. Should I combine all the ways (e.g. highway) irrespective of the street name as one way should I group the the ways based on the street names?</p>
<p>What I did is this. I combined "ways" with the same street name as one way. I then Iterated through the way for a repeated node id, which i assume should be the intersections. I got some results. But while testing the coordinates directly, some of the coordinates were not pointing to intersections on the OpenStreetMap. Is there anything I'm missing?</p>
<p>Thanks</p>
</div>
<div id="comment-83277-info" class="comment-info">
<span class="comment-age">(31 Jan '22, 15:01)</span> <span class="comment-user userinfo">Segunlakata</span>
</div>
</div>
<span id="83279"></span>
<div id="comment-83279" class="comment">
<div id="post-83279-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, using the name as a grouping feature was a good idea. -- Is it possible that you have somehow retained the duplicate nodes that occur where one segment of a street ends and another of the same street begins? Those could be anywhere, not just at intersections, are they maybe responsible?</p>
</div>
<div id="comment-83279-info" class="comment-info">
<span class="comment-age">(31 Jan '22, 18:52)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="83280"></span>
<div id="comment-83280" class="comment">
<div id="post-83280-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Expanding on Frederik's comment, perhaps you have misunderstood the meaning of the segments (ways) that make up a single named street? They do not (in general) correspond to segments between intersections. A street may be split into multiple ways in the data wherever any mapped property of the street changes: the number of lanes, the presence or absence of sidewalks, and so on. Sometimes these coincide with intersections, but often they don't.</p>
</div>
<div id="comment-83280-info" class="comment-info">
<span class="comment-age">(31 Jan '22, 19:50)</span> <span class="comment-user userinfo">alan_gr</span>
</div>
</div>
</div>
<div id="comment-tools-83229" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83229-form-container" class="comment-form-container">
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

