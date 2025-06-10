+++
type = "question"
title = "Are all nodes in OSMdata POIs ？"
description = '''Since I want to covert an OSM file to a shapefile, I need to know if all nodes in OSM are POIs. Should I delete the nodes which are not POI? And different people will upload different nodes using GPS even though they are on the same road, so how do we define this road? I&#x27;m a newcomer and don&#x27;t have ...'''
date = "2012-10-16T09:14:00Z"
lastmod = "2012-10-16T10:55:00Z"
weight = 16913
keywords = [ "poi" ]
aliases = [ "/questions/16913" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Are all nodes in OSMdata POIs ？](/questions/16913/are-all-nodes-in-osmdata-pois)

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
<span id="post-16913-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16913-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-16913-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Since I want to covert an OSM file to a shapefile, I need to know if all nodes in OSM are POIs. Should I delete the nodes which are not POI?</p>
<p>And different people will upload different nodes using GPS even though they are on the same road, so how do we define this road?</p>
<p>I'm a newcomer and don't have much knowledge about OSM.I hope somebody can help me :-)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-poi" rel="tag" title="see questions tagged &#39;poi&#39;">poi</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Oct '12, 09:14</strong></p>
<img src="https://secure.gravatar.com/avatar/4664de39ba848f6e10f0f39f7ed2a3ec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="HC_bunny&#39;s gravatar image" />
<p><span>HC_bunny</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="HC_bunny has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Oct '12, 10:17</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/6c2dd6a39d3f38f1bb47a8c1fe8325e2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sleske&#39;s gravatar image" />
<p><span>sleske</span><br />
<span class="score" title="4090 reputation points"><span>4.1k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="78 badges"><span class="bronze">●</span><span class="badgecount">78</span></span></p>
</div>
</div>
<div id="comments-container-16913" class="comments-container">
&#10;</div>
<div id="comment-tools-16913" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16913-form-container" class="comment-form-container">
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

<span id="16914"></span>

<div id="answer-container-16914" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-16914-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16914-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-16914-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Of roughly 1.6 billion nodes in OSM (as of October 2012), only 70 million - less than 5% - have at least one tag, which is a prerequisite for being a POI. Even a node with a tag need not be a POI; sometimes, even the nodes used to support an imported geometry are tagged with a "source" or similar tag.</p>
<p>If you want to convert OSM data to shape files, use one of the existing utilities osm2shp or osmjs, or import into PostGIS with osm2pgsql or imposm and export to shape from there. Enter "shapefile" in the search box above to see other questions and answers about this.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Oct '12, 09:24</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-16914" class="comments-container">
<span id="16915"></span>
<div id="comment-16915" class="comment">
<div id="post-16915-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Also, not all POIs are nodes - some are drawn as areas.</p>
</div>
<div id="comment-16915-info" class="comment-info">
<span class="comment-age">(16 Oct '12, 10:34)</span> <span class="comment-user userinfo">EdLoach ♦</span>
</div>
</div>
<span id="16916"></span>
<div id="comment-16916" class="comment">
<div id="post-16916-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Also, take some days and read the OSM wiki ... starting for example at <a href="http://wiki.openstreetmap.org/wiki/Elements">http://wiki.openstreetmap.org/wiki/Elements</a> or the Main Page</p>
</div>
<div id="comment-16916-info" class="comment-info">
<span class="comment-age">(16 Oct '12, 10:55)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
</div>
<div id="comment-tools-16914" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16914-form-container" class="comment-form-container">
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

