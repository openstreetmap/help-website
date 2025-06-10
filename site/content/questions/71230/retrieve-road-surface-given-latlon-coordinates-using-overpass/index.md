+++
type = "question"
title = "Retrieve road surface given lat/lon coordinates using overpass"
description = '''I have some routes represented by lat/lon coordinates of which I want to retrieve the surface   (asphalt, concrete, cobblestone etc) &amp;amp; smoothness of the road.  Therefor I&#x27;m trying to query the road surface of one coordinate point using overpass turbo.  This is what I have so far:  [out:json][tim...'''
date = "2019-10-18T16:38:00Z"
lastmod = "2019-10-18T16:57:00Z"
weight = 71230
keywords = [ "overpassapi", "overpass", "overpass-turbo", "surface" ]
aliases = [ "/questions/71230" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Retrieve road surface given lat/lon coordinates using overpass](/questions/71230/retrieve-road-surface-given-latlon-coordinates-using-overpass)

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
<span id="post-71230-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71230-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-71230-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have some routes represented by lat/lon coordinates of which I want to retrieve the <a href="https://wiki.openstreetmap.org/wiki/Key:surface">surface</a> (asphalt, concrete, cobblestone etc) &amp; smoothness of the road.</p>
<p>Therefor I'm trying to query the road surface of one coordinate point using overpass turbo. This is what I have so far:</p>
<pre><code>[out:json][timeout:25];
(
  // query part for: “surface=*”
  way[&quot;surface&quot;](around:10,51.28845, 4.502601);
);
// print results
out body;
&gt;;
out skel qt;</code></pre>
<p>However this doesn't work, it says that an empty dataset was received.</p>
<p>After increasing the radius a lot, some results are returned, but the list of returned points grows too long. What am i doing wrong? Help or some guidlines would be much appreciated :)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpassapi" rel="tag" title="see questions tagged &#39;overpassapi&#39;">overpassapi</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span> <span class="post-tag tag-link-surface" rel="tag" title="see questions tagged &#39;surface&#39;">surface</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Oct '19, 16:38</strong></p>
<img src="https://secure.gravatar.com/avatar/c299d140b1854195ea8f324c008a2084?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bilgeckers&#39;s gravatar image" />
<p><span>bilgeckers</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bilgeckers has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-71230" class="comments-container">
&#10;</div>
<div id="comment-tools-71230" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71230-form-container" class="comment-form-container">
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

<span id="71231"></span>

<div id="answer-container-71231" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71231-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71231-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-71231-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The <a href="https://www.openstreetmap.org/way/50289792">nearest road</a> to that point doesn't have a surface tag, nor do many of the roads in that area. Of the ways that do have a surface tag, the vast majority are paths, footways or cycleways. If you need to know the surface of the roads, you'll likely need to do an on-the-ground survey yourself.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Oct '19, 16:57</strong></p>
<img src="https://secure.gravatar.com/avatar/087bb38ba920baadf1df9dfc473208ec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alester&#39;s gravatar image" />
<p><span>alester</span><br />
<span class="score" title="6631 reputation points"><span>6.6k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="66 badges"><span class="silver">●</span><span class="badgecount">66</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alester has 37 accepted answers">28%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Oct '19, 16:58</strong> </span></p>
</div>
</div>
<div id="comments-container-71231" class="comments-container">
&#10;</div>
<div id="comment-tools-71231" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71231-form-container" class="comment-form-container">
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

