+++
type = "question"
title = "query nodes by attributes of connected ways"
description = '''I&#x27;m am trying to extract a set of nodes that represent signalized intersections with bike infrastructure leading into them.  the trouble I have run into is that I don&#x27;t think there is a way to query nodes according to the attributes of the ways that connect to them.  Is that correct? If it is I can ...'''
date = "2021-06-03T13:09:00Z"
lastmod = "2021-06-03T15:37:00Z"
weight = 80398
keywords = [ "overpass", "overpass-turbo" ]
aliases = [ "/questions/80398" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [query nodes by attributes of connected ways](/questions/80398/query-nodes-by-attributes-of-connected-ways)

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
<span id="post-80398-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80398-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-80398-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm am trying to extract a set of nodes that represent signalized intersections with bike infrastructure leading into them.</p>
<p>the trouble I have run into is that I don't think there is a way to query nodes according to the attributes of the ways that connect to them.</p>
<p>Is that correct? If it is I can download the data and run the query as a join on the to and from OSM_ID's of the way in postgres. this will be fairly time consuming though so i wanted to first check and see whether anyone had a way to do this in overpass or overpass turbo.</p>
<p>thanks for any and all suggestions.</p>
<p>edit: I can query nodes and ways separately in overpass turbo using:</p>
<p><code>node [highway=traffic_signals] ({{bbox}}); out; way [bicycle=designated] ({{bbox}}); out;</code></p>
<p>but my goal is to return the subset of that query that is nodes connected to a line where bicycle=designated.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Jun '21, 13:09</strong></p>
<img src="https://secure.gravatar.com/avatar/58c0088fb71bfa1bbce14bc4ce03249b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hughkelley&#39;s gravatar image" />
<p><span>hughkelley</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hughkelley has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Jun '21, 14:06</strong> </span></p>
</div>
</div>
<div id="comments-container-80398" class="comments-container">
<span id="80399"></span>
<div id="comment-80399" class="comment">
<div id="post-80399-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Post a link to an example. What code have you got at the moment?</p>
</div>
<div id="comment-80399-info" class="comment-info">
<span class="comment-age">(03 Jun '21, 13:48)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
<span id="80400"></span>
<div id="comment-80400" class="comment">
<div id="post-80400-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>edited to include example illustrating what is not useful to me. is the question not clear?</p>
</div>
<div id="comment-80400-info" class="comment-info">
<span class="comment-age">(03 Jun '21, 14:07)</span> <span class="comment-user userinfo">hughkelley</span>
</div>
</div>
</div>
<div id="comment-tools-80398" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80398-form-container" class="comment-form-container">
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

<span id="80401"></span>

<div id="answer-container-80401" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-80401-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80401-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-80401-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="hughkelley has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You need to <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Recurse_.28n.2C_w.2C_r.2C_bn.2C_bw.2C_br.29">recurse</a> down from the ways to find the appropriate child nodes.</p>
<pre><code>[bbox:{{bbox}}];
way[bicycle=designated];
node(w)[highway=traffic_signals];
out center;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Jun '21, 15:37</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-80401" class="comments-container">
&#10;</div>
<div id="comment-tools-80401" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80401-form-container" class="comment-form-container">
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

