+++
type = "question"
title = "get surrounding buildings to a set of nodes with specific tags"
description = '''Dear all, I want to query overpass-turbo.eu for all buildings that contain at least one node with the tag &quot;country=EU&quot; and &quot;office=government&quot;. I tried so far: node({{bbox}})[country=EU][office=government]; is_in; (way[building](pivot);&amp;gt;;);out;  Test on overpass: http://overpass-turbo.eu/s/MaJ (c...'''
date = "2019-09-09T18:48:00Z"
lastmod = "2019-11-09T22:22:00Z"
weight = 70711
keywords = [ "overpass" ]
aliases = [ "/questions/70711" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [get surrounding buildings to a set of nodes with specific tags](/questions/70711/get-surrounding-buildings-to-a-set-of-nodes-with-specific-tags)

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
<span id="post-70711-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70711-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-70711-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Dear all,</p>
<p>I want to query overpass-turbo.eu for all buildings that contain at least one node with the tag "country=EU" and "office=government".</p>
<p>I tried so far:</p>
<pre><code>node({{bbox}})[country=EU][office=government];
is_in;
(way[building](pivot);&gt;;);out;</code></pre>
<p>Test on overpass: <a href="http://overpass-turbo.eu/s/MaJ">http://overpass-turbo.eu/s/MaJ</a> (courtesy of <a href="https://gis.stackexchange.com/a/116952/149046">mmd</a>)</p>
<p>However, this does not work as areas are not always updated (see discussion with mmd and <a href="https://github.com/drolbr/Overpass-API/issues/285#issuecomment-234764265">on github</a>). The results are not complete and not reliable.</p>
<p>Then, I tested to achieve this with the around operator.</p>
<pre><code>[out:json][timeout:25];
// fetch area “Brussels” to search in
{{geocodeArea:Brussels}}-&gt;.searchArea;
// gather results
node[office=government][country=EU](area.searchArea)-&gt;.offices;
( 
  way[building=yes](around.offices:8);
);
// print results
out body;
(._;&gt;;);
out skel qt;</code></pre>
<p>Test on overpass: <a href="http://overpass-turbo.eu/s/Mbp">http://overpass-turbo.eu/s/Mbp</a></p>
<p>However, here I do not know how to choose the distance of the around operator. The results are either incomplete or I get false positives, i.e. also neighbouring buildings.</p>
<p>Is there a solution to get the surrounding building of a set of nodes with specific tags?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Sep '19, 18:48</strong></p>
<img src="https://secure.gravatar.com/avatar/e1b35acfc03fce595ff9930007997f40?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rriemann&#39;s gravatar image" />
<p><span>rriemann</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rriemann has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-70711" class="comments-container">
<span id="70720"></span>
<div id="comment-70720" class="comment">
<div id="post-70720-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Is it maybe possible to have a foreach loop over all government office and use their geographical location to get all elements on that point (it's possible with the openstreetmap.org context menu query) and then filter out one building?</p>
</div>
<div id="comment-70720-info" class="comment-info">
<span class="comment-age">(10 Sep '19, 09:17)</span> <span class="comment-user userinfo">rriemann</span>
</div>
</div>
<span id="70864"></span>
<div id="comment-70864" class="comment">
<div id="post-70864-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Cross-posted on <a href="https://github.com/drolbr/Overpass-API/issues/542">https://github.com/drolbr/Overpass-API/issues/542</a></p>
</div>
<div id="comment-70864-info" class="comment-info">
<span class="comment-age">(20 Sep '19, 22:49)</span> <span class="comment-user userinfo">rriemann</span>
</div>
</div>
<span id="71067"></span>
<div id="comment-71067" class="comment">
<div id="post-71067-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Is there maybe a work around in a different language? With some python/javascript lib?</p>
</div>
<div id="comment-71067-info" class="comment-info">
<span class="comment-age">(07 Oct '19, 21:19)</span> <span class="comment-user userinfo">rriemann</span>
</div>
</div>
<span id="71462"></span>
<div id="comment-71462" class="comment">
<div id="post-71462-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>My own answer on my last comment: <a href="https://help.openstreetmap.org/questions/55529/how-to-detect-if-point-is-inside-a-building-polygon-with-overpass">https://help.openstreetmap.org/questions/55529/how-to-detect-if-point-is-inside-a-building-polygon-with-overpass</a></p>
</div>
<div id="comment-71462-info" class="comment-info">
<span class="comment-age">(04 Nov '19, 22:34)</span> <span class="comment-user userinfo">rriemann</span>
</div>
</div>
<span id="71575"></span>
<div id="comment-71575" class="comment">
<div id="post-71575-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Has a nice code example that can be useful: <a href="https://pypi.org/project/osmxtract/">https://pypi.org/project/osmxtract/</a></p>
</div>
<div id="comment-71575-info" class="comment-info">
<span class="comment-age">(09 Nov '19, 22:22)</span> <span class="comment-user userinfo">rriemann</span>
</div>
</div>
</div>
<div id="comment-tools-70711" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70711-form-container" class="comment-form-container">
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

<span id="71450"></span>

<div id="answer-container-71450" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71450-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71450-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-71450-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is my best take so far:</p>
<pre><code>[out:json][timeout:25];
{{geocodeArea:Brussels}}-&gt;.searchArea;
// get EU governmental offices nodes
node[office=government][country=EU](area.searchArea)-&gt;.offices;
(
        // get all enclosures from EU governmental offices
        .offices is_in-&gt;.enclosing;
        // limit result to buildings
        way(pivot.enclosing)[building=yes]-&gt;.officebuildings;
);
&#10;.officebuildings out geom;
.offices out meta;</code></pre>
<p>Run in overpass turbo: <a href="http://overpass-turbo.eu/s/NID">http://overpass-turbo.eu/s/NID</a></p>
<p>The problem is yet that some buildings are not marked (most of them?).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Nov '19, 18:53</strong></p>
<img src="https://secure.gravatar.com/avatar/e1b35acfc03fce595ff9930007997f40?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rriemann&#39;s gravatar image" />
<p><span>rriemann</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rriemann has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-71450" class="comments-container">
&#10;</div>
<div id="comment-tools-71450" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71450-form-container" class="comment-form-container">
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

