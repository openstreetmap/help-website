+++
type = "question"
title = "Getting all places lying within the boundary=administrative and matching by name"
description = '''I am trying to get all place=* nodes lying within boundary=administrative area and matching by name but it always times out even for very small bbox. Is there a problem in my query? [out:xml][bbox:{{bbox}}][timeout:120]; ( area({{bbox}})[&quot;boundary&quot;=&quot;administrative&quot;][name]; )-&amp;gt;.admins; ( node({{bb...'''
date = "2023-01-13T16:32:00Z"
lastmod = "2023-01-13T19:03:00Z"
weight = 86498
keywords = [ "overpass" ]
aliases = [ "/questions/86498" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Getting all places lying within the boundary=administrative and matching by name](/questions/86498/getting-all-places-lying-within-the-boundaryadministrative-and-matching-by-name)

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
<span id="post-86498-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86498-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86498-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am trying to get all place=* nodes lying within boundary=administrative area and matching by name but it always times out even for very small bbox. Is there a problem in my query?</p>
<p><code>[out:xml][bbox:{{bbox}}][timeout:120]; ( area({{bbox}})["boundary"="administrative"][name]; )-&gt;.admins; ( node({{bbox}})[place][name]; )-&gt;.places; foreach.admins-&gt;.admin( node.places(area.admin)(if: t["name"]==admin.t["name"]); (._;&gt;;); out; );</code></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Jan '23, 16:32</strong></p>
<img src="https://secure.gravatar.com/avatar/db688265cd49a0db2789c30419274086?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="star_Martin_star&#39;s gravatar image" />
<p><span>star_Martin_...</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="star_Martin_star has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-86498" class="comments-container">
&#10;</div>
<div id="comment-tools-86498" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86498-form-container" class="comment-form-container">
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

<span id="86499"></span>

<div id="answer-container-86499" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-86499-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86499-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-86499-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="star_Martin_star has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Not 100% sure, but I think area on;y works on specifically named objects so I've searched for relations &amp; then converted them to areas. Unsure what area your searching so I've added an admin_level to restrict the output.</p>
<p><a href="https://overpass-turbo.eu/s/1q7p">https://overpass-turbo.eu/s/1q7p</a></p>
<pre><code>[bbox:{{bbox}}];
rel[boundary=administrative][admin_level=6][name];
map_to_area;
for(t[&quot;name&quot;]) {
node(area)[place][name](if:t[&quot;name&quot;] == _.val);
out meta center;
};</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Jan '23, 19:03</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-86499" class="comments-container">
&#10;</div>
<div id="comment-tools-86499" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86499-form-container" class="comment-form-container">
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

