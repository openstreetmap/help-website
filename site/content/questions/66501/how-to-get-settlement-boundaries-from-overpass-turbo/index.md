+++
type = "question"
title = "How to get settlement boundaries from Overpass Turbo?"
description = '''I&#x27;m a developer but I&#x27;m brand new to using Overpass.  I&#x27;m trying to get polygons for &quot;inhabited areas&quot; (villages, towns, cities) in the UK. They don&#x27;t have to be perfect outlines, just rough outlines are fine.  This is what I&#x27;ve got so far, but it returns points rather than polygons, plus it only re...'''
date = "2018-10-26T22:38:00Z"
lastmod = "2018-10-28T06:43:00Z"
weight = 66501
keywords = [ "overpass", "overpass-turbo" ]
aliases = [ "/questions/66501" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to get settlement boundaries from Overpass Turbo?](/questions/66501/how-to-get-settlement-boundaries-from-overpass-turbo)

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
<span id="post-66501-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66501-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-66501-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm a developer but I'm brand new to using Overpass.</p>
<p>I'm trying to get polygons for "inhabited areas" (villages, towns, cities) in the UK. They don't have to be perfect outlines, just rough outlines are fine.</p>
<p>This is what I've got so far, but it returns points rather than polygons, plus it only returns mid-size settlements; how would I get bigger and smaller ones too?</p>
<pre><code>[out:json][timeout:25]; // fetch area “england” to search in {{geocodeArea:england}}-&gt;.searchArea; // gather results (   // query part for: “town”   node[&quot;place&quot;=&quot;town&quot;](area.searchArea); way[&quot;place&quot;=&quot;town&quot;](area.searchArea);  relation[&quot;place&quot;=&quot;town&quot;](area.searchArea); ); // print results out body;
&gt;; out skel qt;</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Oct '18, 22:38</strong></p>
<img src="https://secure.gravatar.com/avatar/c58d8413fa737692a8d20e63a23af85d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cakehoover&#39;s gravatar image" />
<p><span>cakehoover</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cakehoover has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-66501" class="comments-container">
&#10;</div>
<div id="comment-tools-66501" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66501-form-container" class="comment-form-container">
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

<span id="66506"></span>

<div id="answer-container-66506" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-66506-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66506-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-66506-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>First, you only look for place="town", but OSM uses different values for settlements depending on the size, see the <a href="https://wiki.openstreetmap.org/wiki/Key:place">wiki</a>. Furthermore the boundaries are mapped as <a href="https://wiki.openstreetmap.org/wiki/Tag:boundary=administrative">administrative boundary relations</a>.</p>
<p>Instead of writing the query yourself, you might use <a href="https://wambachers-osm.website/boundaries/">Wambacher's website</a> to download the administrative boundaries in a variety of formats.</p>
<p>Long time ago, I wrote this Overpass <a href="http://overpass-turbo.eu/s/D9e">query</a> to retrieve admin levels 8 and 9. It can easily be adapted to retrieve all levels. Note it's written in the older XML-format.</p>
<p>You should also expect that the lowest level of settlements might not be mapped with administrative boundaries. I'm thinking of hamlets and neighbourhoods here.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Oct '18, 07:14</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-66506" class="comments-container">
<span id="66507"></span>
<div id="comment-66507" class="comment">
<div id="post-66507-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks! I think the problem is that the UK simply doesn't consistently have administrative boundaries for towns and settlements (in some cases administrative regions overlap with towns, but frequently not), so using administrative regions isn't going to help me. If I was interested in admin boundaries, this would be a good suggestion. Instead I'm going to use these boundaries <a href="http://geoportal.statistics.gov.uk/datasets/built-up-areas-december-2011-boundaries-v2">http://geoportal.statistics.gov.uk/datasets/built-up-areas-december-2011-boundaries-v2</a></p>
</div>
<div id="comment-66507-info" class="comment-info">
<span class="comment-age">(27 Oct '18, 13:17)</span> <span class="comment-user userinfo">cakehoover</span>
</div>
</div>
<span id="66518"></span>
<div id="comment-66518" class="comment">
<div id="post-66518-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>OSM does not have any objects which correspond to urban areas. I wrote a series of blog posts on the subject, including identifying various approaches to finding such bounds using OSM data. A perhaps more recent version of British (excluding NI) urban areas is available is OS OpenData Strategic or Meridian. There is also a settlement &amp; locality dataset for Scotland which may be a subset of that which you have located.</p>
</div>
<div id="comment-66518-info" class="comment-info">
<span class="comment-age">(28 Oct '18, 06:43)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-66506" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66506-form-container" class="comment-form-container">
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

