+++
type = "question"
title = "Overpass turbo bbox - reducing amount of data for a relation with many ways"
description = '''I am trying to query on hiking routes http://overpass-turbo.eu/s/q52 using the following centred on London. [out:json][timeout:25]; relation[&quot;route&quot;=&quot;hiking&quot;]({{bbox}}); out geom;  I am finding I getting data I don&#x27;t want which has a performance impact. I think I have two issues.  Some of the relati...'''
date = "2017-06-30T09:53:00Z"
lastmod = "2020-10-14T19:49:00Z"
weight = 56810
keywords = [ "overpass", "overpass-turbo" ]
aliases = [ "/questions/56810" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Overpass turbo bbox - reducing amount of data for a relation with many ways](/questions/56810/overpass-turbo-bbox-reducing-amount-of-data-for-a-relation-with-many-ways)

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
<span id="post-56810-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56810-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-56810-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am trying to query on hiking routes <a href="http://overpass-turbo.eu/s/q52">http://overpass-turbo.eu/s/q52</a> using the following centred on London.</p>
<pre><code>[out:json][timeout:25];
relation[&quot;route&quot;=&quot;hiking&quot;]({{bbox}});
out geom;</code></pre>
<p>I am finding I getting data I don't want which has a performance impact. I think I have two issues.</p>
<ol>
<li>Some of the relations are very big. (3212473 Greenwich Meridian Trail 20469 Thames Path)</li>
<li>I am getting relations that are way outside my viewport (Shakespeare's Way - 71448) and I can't see why.</li>
</ol>
<p>On point 1., can I process the relation - eg only output the ways that appears in my viewport. If I am interested in London I dont want details of the route near lincoln.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Jun '17, 09:53</strong></p>
<img src="https://secure.gravatar.com/avatar/ba18d96cf193429ae1a16c30828ef58d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andrewblack&#39;s gravatar image" />
<p><span>andrewblack</span><br />
<span class="score" title="365 reputation points">365</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andrewblack has 4 accepted answers">57%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Jun '17, 10:25</strong> </span></p>
</div>
</div>
<div id="comments-container-56810" class="comments-container">
<span id="56812"></span>
<div id="comment-56812" class="comment">
<div id="post-56812-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Re Shakespeare's Way - something odd about the data. Investigating further</p>
</div>
<div id="comment-56812-info" class="comment-info">
<span class="comment-age">(30 Jun '17, 12:43)</span> <span class="comment-user userinfo">andrewblack</span>
</div>
</div>
<span id="56823"></span>
<div id="comment-56823" class="comment">
<div id="post-56823-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have an answer to this. Will write up tomorrow</p>
</div>
<div id="comment-56823-info" class="comment-info">
<span class="comment-age">(30 Jun '17, 23:42)</span> <span class="comment-user userinfo">andrewblack</span>
</div>
</div>
</div>
<div id="comment-tools-56810" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56810-form-container" class="comment-form-container">
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

<span id="56998"></span>

<div id="answer-container-56998" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56998-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56998-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-56998-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you want all relations being tagged with route=hiking but only those ways of those relations which are inside your bounding box, you should try following query:</p>
<pre><code>[out:json][timeout:25];
// Store all interesting relations which intersect with the bounding box in
// a set called &quot;interestingrelations&quot;.
relation[&quot;route&quot;=&quot;hiking&quot;]({{bbox}})-&gt;.interestingrelations;
// Store all way members of the relations in the set &quot;interestingrelations&quot;
// in the set &quot;alltheirways&quot;.
way(r.interestingrelations)-&gt;.alltheirways;
// Filter &quot;alltheirways&quot; using a bounding box filter. Store result in &quot;waysinside&quot;.
way.alltheirways({{bbox}})-&gt;.waysinside;
// Output geometry of &quot;waysinside&quot;.
.waysinside out geom;</code></pre>
<p>Features of Overpass QL in use:</p>
<ul>
<li><a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#By_tag_.28has-kv.29">filter by tag</a></li>
<li><a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Recurse_.28n.2C_w.2C_r.2C_bn.2C_bw.2C_br.29">recurse</a></li>
<li><a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Bounding_box">bounding box filter</a></li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Jul '17, 19:47</strong></p>
<img src="https://secure.gravatar.com/avatar/d2a3b905e2632430b47dd9b8de3d8ba0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nakaner&#39;s gravatar image" />
<p><span>Nakaner</span><br />
<span class="score" title="610 reputation points">610</span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nakaner has 3 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-56998" class="comments-container">
<span id="77046"></span>
<div id="comment-77046" class="comment">
<div id="post-77046-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Wow, that is a life saver! Here's how I finally got just the slice of the border of Paraguay that I needed:</p>
<p>relation(389884)-&gt;.interestingrelations;</p>
<p>way(r.interestingrelations)-&gt;.alltheirways;</p>
<p>way.alltheirways(-25.2,-59.5,-24.2,-58)-&gt;.waysinside;</p>
<p>.waysinside out geom;</p>
</div>
<div id="comment-77046-info" class="comment-info">
<span class="comment-age">(12 Oct '20, 08:29)</span> <span class="comment-user userinfo">jidanni</span>
</div>
</div>
<span id="77106"></span>
<div id="comment-77106" class="comment">
<div id="post-77106-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>FYI: <a href="http://overpass-turbo.eu/s/Z1J">http://overpass-turbo.eu/s/Z1J</a> relation(389884); way(r)(-25.2,-59.5,-24.2,-58); out geom;</p>
</div>
<div id="comment-77106-info" class="comment-info">
<span class="comment-age">(14 Oct '20, 19:49)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
</div>
<div id="comment-tools-56998" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56998-form-container" class="comment-form-container">
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

