+++
type = "question"
title = "Overpass query to find multipolygon relations with just one member"
description = '''Hi I hacked at this OverPass Wiki example to find multi-polygon relations with just one member. The resulting routine seems to work but looks like it is running unnecessary steps. I&#x27;ve run out of knowledge. Is there anything I can do to tidy it up &amp;amp; make it run more efficiently?  rel({{bbox}})[t...'''
date = "2018-03-19T21:13:00Z"
lastmod = "2018-03-20T14:45:00Z"
weight = 62730
keywords = [ "member", "overpass", "relations", "multipolygon" ]
aliases = [ "/questions/62730" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Overpass query to find multipolygon relations with just one member](/questions/62730/overpass-query-to-find-multipolygon-relations-with-just-one-member)

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
<span id="post-62730-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62730-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-62730-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi</p>
<p>I hacked at <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_API_by_Example#Multipolygons_with_inappropiate_member_roles">this OverPass Wiki example</a> to find multi-polygon relations with just one member. The resulting routine seems to work but looks like it is running unnecessary steps. I've run out of knowledge. Is there anything I can do to tidy it up &amp; make it run more efficiently?</p>
<pre><code>rel({{bbox}})[type=multipolygon]-&gt;.relations;
foreach .relations -&gt; .relation (
  (
   way(r.relation);
  )-&gt;.elem_all;
&#10;  rel.relation( if:elem_all.count(ways) == 1 );
  out geom;
);</code></pre>
<p><a href="http://overpass-turbo.eu/s/x9r">OverpassTurbo Link</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-member" rel="tag" title="see questions tagged &#39;member&#39;">member</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span> <span class="post-tag tag-link-multipolygon" rel="tag" title="see questions tagged &#39;multipolygon&#39;">multipolygon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Mar '18, 21:13</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-62730" class="comments-container">
&#10;</div>
<div id="comment-tools-62730" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62730-form-container" class="comment-form-container">
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

<span id="62735"></span>

<div id="answer-container-62735" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-62735-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62735-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-62735-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="DaveF has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There's a <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Element_Properties_Count">count_members</a> evaluator that looks inside of each individual relation:</p>
<pre><code>[bbox:{{bbox}}];
rel[type=multipolygon](if:count_members() == 1);
out geom;</code></pre>
<p><a href="http://overpass-turbo.eu/s/x9L">http://overpass-turbo.eu/s/x9L</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Mar '18, 00:32</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-62735" class="comments-container">
<span id="62740"></span>
<div id="comment-62740" class="comment">
<div id="post-62740-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ah, thank you. my Google search 'overpass count' wasn't specific enough to find it.</p>
</div>
<div id="comment-62740-info" class="comment-info">
<span class="comment-age">(20 Mar '18, 14:45)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
</div>
<div id="comment-tools-62735" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62735-form-container" class="comment-form-container">
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

