+++
type = "question"
title = "converting multiple relations into 1 polygon"
description = '''update: fixed Hi there, I&#x27;m trying to merge multiple relations into one polygon area. What i did: In JOSM:  File-&amp;gt;Download an object, choose the type &quot;relation&quot; and give the id, uncheck &quot;Download referents&quot; and check &quot;Download members&quot; remove all admin-centres remove all tags in the tags/members ...'''
date = "2019-04-10T10:01:00Z"
lastmod = "2019-04-10T10:01:00Z"
weight = 68746
keywords = [ "merge", "poly", "relations", "josm" ]
aliases = [ "/questions/68746" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [converting multiple relations into 1 polygon](/questions/68746/converting-multiple-relations-into-1-polygon)

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
<span id="post-68746-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68746-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-68746-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p><strong>update: fixed</strong></p>
<p>Hi there,</p>
<p>I'm trying to merge multiple relations into one polygon area.</p>
<p>What i did:</p>
<p>In JOSM:</p>
<ol>
<li>File-&gt;Download an object, choose the type "relation" and give the id, uncheck "Download referents" and check "Download members"</li>
<li>remove all admin-centres</li>
<li>remove all tags in the tags/members column</li>
<li>removed all inner ways (with lasso tool/select tool)</li>
<li><strong>fix: copy-pasted all to a new layer (CMD-A, CMD-C, CMD-ALT-V)</strong></li>
<li><strong>merged ways with (C) and preserve all ways</strong></li>
<li>Save as .osm</li>
<li>Use osm2poly.pl script for generate the poly file : perl osm2poly.pl data.osm &gt; data.poly</li>
</ol>
<p>But then i get multiple polylines. How can i merge these relations?</p>
<p><em>Add. I based my actions on <a href="/questions/15481/converting-a-relation-into-an-osmosis-polygon-file">https://help.openstreetmap.org/questions/15481/converting-a-relation-into-an-osmosis-polygon-file</a></em></p>
<p>Regards, Ed'</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-merge" rel="tag" title="see questions tagged &#39;merge&#39;">merge</span> <span class="post-tag tag-link-poly" rel="tag" title="see questions tagged &#39;poly&#39;">poly</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span> <span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Apr '19, 10:01</strong></p>
<img src="https://secure.gravatar.com/avatar/1188e2f2f1a4b93de8c03ec5e1afb404?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="eddiebouncer&#39;s gravatar image" />
<p><span>eddiebouncer</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="eddiebouncer has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Apr '19, 10:47</strong> </span></p>
</div>
</div>
<div id="comments-container-68746" class="comments-container">
&#10;</div>
<div id="comment-tools-68746" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68746-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

