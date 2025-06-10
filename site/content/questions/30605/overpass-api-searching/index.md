+++
type = "question"
title = "Overpass API Searching"
description = '''I am looking into switching our apps mapping platform away from google maps. After a bit of trail and error, I was able to get a somewhat working example. I however have run into a deal breaking scenario.  The scenario I have is this. Given a users current location, find me all of the POI&#x27;s in their...'''
date = "2014-02-10T23:21:00Z"
lastmod = "2014-02-11T08:54:00Z"
weight = 30605
keywords = [ "overpass", "search" ]
aliases = [ "/questions/30605" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Overpass API Searching](/questions/30605/overpass-api-searching)

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
<span id="post-30605-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30605-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-30605-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am looking into switching our apps mapping platform away from google maps. After a bit of trail and error, I was able to get a somewhat working example. I however have run into a deal breaking scenario.</p>
<p>The scenario I have is this. Given a users current location, find me all of the POI's in their area based on a specific amenity or cuisine type.</p>
<p>Ideally I would like to use the current users lat/lng to determine where they are and then do a radius search based on this.</p>
<p>The question I have is, how do I pass the current users lat/lng into the Overpass api? The only thing I can see is that I can set a bounding box.</p>
<p>This is the current (non working) query that I am using</p>
<p>&lt;osm-script output="json" timeout="25"&gt; &lt;union&gt; &lt;query type="node"&gt; &lt;has-kv k="cuisine" v="coffee_shop"/&gt; &lt;around radius="1000"/&gt; &lt;bbox-query {{bbox}}=""/&gt; &lt;/query&gt; &lt;/union&gt; &lt;print mode="body"/&gt; &lt;recurse type="down"/&gt; &lt;print mode="skeleton" order="quadtile"/&gt; &lt;/osm-script&gt;</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-search" rel="tag" title="see questions tagged &#39;search&#39;">search</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Feb '14, 23:21</strong></p>
<img src="https://secure.gravatar.com/avatar/f11935b171e12c932a5703f8f8134aa7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tempname&#39;s gravatar image" />
<p><span>Tempname</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tempname has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-30605" class="comments-container">
&#10;</div>
<div id="comment-tools-30605" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30605-form-container" class="comment-form-container">
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

<span id="30619"></span>

<div id="answer-container-30619" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-30619-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30619-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-30619-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The Overpass API does actually support this directly in the <em>around</em> statement:</p>
<pre><code>&lt;around radius=&quot;1000&quot; lat=&quot;52.3691&quot; lon=&quot;4.88941&quot; /&gt;</code></pre>
<p>Or see this <a href="http://overpass-turbo.eu/s/2tI">example</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Feb '14, 08:54</strong></p>
<img src="https://secure.gravatar.com/avatar/eca34689e074411e0daca0d994f532b3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tyr_asd&#39;s gravatar image" />
<p><span>tyr_asd</span><br />
<span class="score" title="1196 reputation points"><span>1.2k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="19 badges"><span class="silver">●</span><span class="badgecount">19</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tyr_asd has 11 accepted answers">64%</span></p>
</div>
</div>
<div id="comments-container-30619" class="comments-container">
&#10;</div>
<div id="comment-tools-30619" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30619-form-container" class="comment-form-container">
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

