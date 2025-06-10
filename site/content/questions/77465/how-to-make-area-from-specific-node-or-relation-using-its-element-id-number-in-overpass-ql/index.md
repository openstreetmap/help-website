+++
type = "question"
title = "How to make area from specific node or relation, using it&#x27;s element id number in Overpass QL?"
description = '''I can make an area in Overpass QL, using name and relation attributes (tags) filter of element, something like this: area[&quot;name:en&quot;=&quot;Moscow Oblast&quot;][&quot;boundary&quot;=&quot;administrative&quot;][&quot;admin_level&quot;=&quot;4&quot;]-&amp;gt;.region; (node(area.region)[place=&quot;city&quot;];node(area.region)[place=&quot;town&quot;];); out;  But searching vi...'''
date = "2020-11-09T09:34:00Z"
lastmod = "2020-11-09T13:19:00Z"
weight = 77465
keywords = [ "overpass" ]
aliases = [ "/questions/77465" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to make area from specific node or relation, using it's element id number in Overpass QL?](/questions/77465/how-to-make-area-from-specific-node-or-relation-using-its-element-id-number-in-overpass-ql)

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
<span id="post-77465-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77465-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-77465-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I can make an area in Overpass QL, using name and relation attributes (tags) filter of element, something like this:</p>
<pre><code>area[&quot;name:en&quot;=&quot;Moscow Oblast&quot;][&quot;boundary&quot;=&quot;administrative&quot;][&quot;admin_level&quot;=&quot;4&quot;]-&gt;.region;
(node(area.region)[place=&quot;city&quot;];node(area.region)[place=&quot;town&quot;];);
out;</code></pre>
<p>But searching via name is not so stable, and will broke if element name is changed. So much better (for performance too) is to make an area from element id. Here is example of searching relation via it's element id:</p>
<pre><code>rel(51490);
out;</code></pre>
<p>And can't understand, how to pass element type and id to area query? Something like this:</p>
<pre><code>area(rel(51490))-&gt;.region;
(node(area.region)[place=&quot;city&quot;];node(area.region)[place=&quot;town&quot;];);
out;</code></pre>
<p>or other variants like <code>area["id"=51490]-&gt;.region;</code> or <code>area["type"="rel"]["rel"=51490])-&gt;.region;</code> don't works.</p>
<p>Can anyone give me an example, how to make area from OSM element by it's id?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Nov '20, 09:34</strong></p>
<img src="https://secure.gravatar.com/avatar/eb9070e348bc332987d2935bbcf23a50?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Murz&#39;s gravatar image" />
<p><span>Murz</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Murz has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-77465" class="comments-container">
&#10;</div>
<div id="comment-tools-77465" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77465-form-container" class="comment-form-container">
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

<span id="77473"></span>

<div id="answer-container-77473" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-77473-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77473-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-77473-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>From the wiki:</p>
<blockquote>
<p>By convention the area id can be calculated from an existing OSM way by adding 2400000000 to its OSM id, or in case of a relation by adding 3600000000 respectively.</p>
</blockquote>
<p><a href="https://overpass-turbo.eu/s/ZTF">https://overpass-turbo.eu/s/ZTF</a></p>
<pre><code>area(3600051490);
node(area)[place~&quot;^(city|town)$&quot;];
out;</code></pre>
<p>Multiple areas can be combined (note the 'id:'):</p>
<pre><code>area(id:3600058447,3600058437,3600058446); // England, Wales, Scotland</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Nov '20, 12:38</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Nov '20, 19:32</strong> </span></p>
</div>
</div>
<div id="comments-container-77473" class="comments-container">
<span id="77474"></span>
<div id="comment-77474" class="comment">
<div id="post-77474-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for solution! It is very interesting trick with id's, that I don't know before.</p>
</div>
<div id="comment-77474-info" class="comment-info">
<span class="comment-age">(09 Nov '20, 12:42)</span> <span class="comment-user userinfo">Murz</span>
</div>
</div>
</div>
<div id="comment-tools-77473" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77473-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="77475"></span>

<div id="answer-container-77475" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-77475-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77475-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-77475-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Other solution, provided from <a href="https://help.openstreetmap.org/users/8708/mmd">@mmd</a>, is to use result of fist search via id of element as area, example:</p>
<pre><code>rel(51490);map_to_area-&gt;.region;
node(area.region)[place=&quot;city&quot;];
out;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Nov '20, 12:43</strong></p>
<img src="https://secure.gravatar.com/avatar/eb9070e348bc332987d2935bbcf23a50?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Murz&#39;s gravatar image" />
<p><span>Murz</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Murz has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Nov '20, 12:43</strong> </span></p>
</div>
</div>
<div id="comments-container-77475" class="comments-container">
<span id="77476"></span>
<div id="comment-77476" class="comment">
<div id="post-77476-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That's basically the same but with a conversion: <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Map_way.2Frelation_to_area_.28map_to_area.29">https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Map_way.2Frelation_to_area_.28map_to_area.29</a></p>
<hr />
<p>btw where did <a href="https://help.openstreetmap.org/users/8708/mmd">@mmd</a> post the reply?</p>
</div>
<div id="comment-77476-info" class="comment-info">
<span class="comment-age">(09 Nov '20, 13:01)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
<span id="77477"></span>
<div id="comment-77477" class="comment">
<div id="post-77477-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>In Slack, because I ask similar question in Slack too, but before creating question here.</p>
</div>
<div id="comment-77477-info" class="comment-info">
<span class="comment-age">(09 Nov '20, 13:19)</span> <span class="comment-user userinfo">Murz</span>
</div>
</div>
</div>
<div id="comment-tools-77475" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77475-form-container" class="comment-form-container">
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

