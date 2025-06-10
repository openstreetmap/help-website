+++
type = "question"
title = "OverpassAPI returns a file with old data"
description = '''Hi all. 1) I updated this relation: http://www.openstreetmap.org/relation/4661740 2) Then I send a query: http://overpass-api.de/api/interpreter?data=node(337580513);is_in;out;  In the file within area 3604661740 I don&#x27;t see any updated info. Is there any delays between OSM and overpass? How long?'''
date = "2016-05-11T16:47:00Z"
lastmod = "2016-05-19T20:35:00Z"
weight = 49679
keywords = [ "overpass" ]
aliases = [ "/questions/49679" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [OverpassAPI returns a file with old data](/questions/49679/overpassapi-returns-a-file-with-old-data)

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
<span id="post-49679-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49679-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-49679-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all.</p>
<pre><code>1) I updated this relation: http://www.openstreetmap.org/relation/4661740
2) Then I send a query: http://overpass-api.de/api/interpreter?data=node(337580513);is_in;out;</code></pre>
<p>In the file within area <strong>3604661740</strong> I don't see any updated info. Is there any delays between OSM and overpass? How long?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 May '16, 16:47</strong></p>
<img src="https://secure.gravatar.com/avatar/1565cd50c70d1108a514e12877171c5f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bear_ukraine&#39;s gravatar image" />
<p><span>bear_ukraine</span><br />
<span class="score" title="41 reputation points">41</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bear_ukraine has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 May '16, 16:52</strong> </span></p>
</div>
</div>
<div id="comments-container-49679" class="comments-container">
&#10;</div>
<div id="comment-tools-49679" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49679-form-container" class="comment-form-container">
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

<span id="49680"></span>

<div id="answer-container-49680" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-49680-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49680-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-49680-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="bear_ukraine has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can find the exact timestamps in the Overpass API response, in particular in the attribute values osm_base and areas.</p>
<pre><code>&lt;meta osm_base=&quot;2016-05-11T17:18:02Z&quot; areas=&quot;2016-05-10T06:41:02Z&quot;/&gt;</code></pre>
<ul>
<li><code>osm_base</code> refers to the timestamp, when nodes, ways and relations were last updated on the server by applying minutely diff files. Usually the delay will just be a few minutes.</li>
<li><code>areas</code> refers to the timestamp, when the area creation job on the server started to run the last time. The lag can be between 24 and 48 hours at the moment. This is subject to changes in the way the update job runs on the server. Reason being that this is quite a resource intensive task, which needs some time to finish.</li>
</ul>
<p>Just have a bit of patience, your changes will most likely be reflected in the areas by tomorrow.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 May '16, 18:24</strong></p>
<img src="https://secure.gravatar.com/avatar/264d84ab05b942224b05960903eba7a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmd&#39;s gravatar image" />
<p><span>mmd</span><br />
<span class="score" title="5682 reputation points"><span>5.7k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="53 badges"><span class="silver">●</span><span class="badgecount">53</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mmd has 44 accepted answers">37%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 May '16, 18:28</strong> </span></p>
</div>
</div>
<div id="comments-container-49680" class="comments-container">
<span id="49729"></span>
<div id="comment-49729" class="comment">
<div id="post-49729-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Just want to mention that in my case it was needed to wait ~48 hours</p>
</div>
<div id="comment-49729-info" class="comment-info">
<span class="comment-age">(18 May '16, 15:37)</span> <span class="comment-user userinfo">bear_ukraine</span>
</div>
</div>
<span id="49748"></span>
<div id="comment-49748" class="comment">
<div id="post-49748-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The area creation lag was addressed in the following Github ticket: <a href="https://github.com/drolbr/Overpass-API/issues/141">https://github.com/drolbr/Overpass-API/issues/141</a> - However, the delta solution mentioned there is not yet productive. In the ticket you will also find some comparison chart from last summer.</p>
</div>
<div id="comment-49748-info" class="comment-info">
<span class="comment-age">(19 May '16, 20:35)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
</div>
<div id="comment-tools-49680" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49680-form-container" class="comment-form-container">
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

