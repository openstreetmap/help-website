+++
type = "question"
title = "How to best define organisation boundary / relation"
description = '''There are numerous prestigious sites in the world that contain several features. When searching for a prestigious site, users might expect to be taken to the bounds of the site. Within the site, users might be able to identify particular points of interest etc. There is therefore a topology. Two exa...'''
date = "2015-09-27T13:55:00Z"
lastmod = "2015-09-27T20:34:00Z"
weight = 45611
keywords = [ "place", "boundary", "admin_boundary", "relation", "relations" ]
aliases = [ "/questions/45611" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to best define organisation boundary / relation](/questions/45611/how-to-best-define-organisation-boundary-relation)

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
<span id="post-45611-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45611-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-45611-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>There are numerous prestigious sites in the world that contain several features. When searching for a prestigious site, users might expect to be taken to the bounds of the site. Within the site, users might be able to identify particular points of interest etc.</p>
<p>There is therefore a topology.</p>
<p>Two examples:</p>
<ul>
<li><a href="http://www.openstreetmap.org/relation/5537968">Spetchley Park Gardens</a></li>
<li><a href="http://www.openstreetmap.org/relation/5527857">Goodwood</a></li>
</ul>
<p>To date I have marked such civil boundaries as "boundary -&gt; administrative" within a relation because:</p>
<ol>
<li>I am unaware of a more appropriate type.</li>
<li>such civil boundaries are often a collection of land parcels, which is an administrative concern(?)</li>
<li>I did not include an <a href="https://wiki.openstreetmap.org/wiki/Tag:boundary%3Dadministrative">admin level</a> attribute to avoid conflict with well known jurisdictions</li>
</ol>
<p>Furthermore, the nominatim search rankings are good (<a href="https://nominatim.openstreetmap.org/search.php?q=Spetchley+Park+Gardens">Spetchley Park Gardens</a> / <a href="https://nominatim.openstreetmap.org/search.php?q=Goodwood+UK">Goodwood</a>) - where bus stops etc. are secondary to the place.</p>
<p>I am keen to learn if there is a more appropriate way to represent such relations and if there is a perceived abuse of tags. Perhaps a "place" value is more appropriate?</p>
<p>This problem seems clearer with national parks / protected areas such as <a href="http://www.openstreetmap.org/relation/2678988">New Forest</a>.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-place" rel="tag" title="see questions tagged &#39;place&#39;">place</span> <span class="post-tag tag-link-boundary" rel="tag" title="see questions tagged &#39;boundary&#39;">boundary</span> <span class="post-tag tag-link-admin_boundary" rel="tag" title="see questions tagged &#39;admin_boundary&#39;">admin_boundary</span> <span class="post-tag tag-link-relation" rel="tag" title="see questions tagged &#39;relation&#39;">relation</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Sep '15, 13:55</strong></p>
<img src="https://secure.gravatar.com/avatar/fb21edcf78d1b7e3be00b6d31d7dd0e4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="snodnipper&#39;s gravatar image" />
<p><span>snodnipper</span><br />
<span class="score" title="126 reputation points">126</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="snodnipper has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-45611" class="comments-container">
&#10;</div>
<div id="comment-tools-45611" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45611-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="45614"></span>

<div id="answer-container-45614" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-45614-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45614-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-45614-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You tagged the as tourism=attraction, so there is no need to tag it with an administrative boundary. This is also incorrect IMHO. Administrative boundaries are for countries, cities, boroughs, etc. Not for tourist attraction. Nominatim will also find the feature when it is something else, such as a tourist attraction</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Sep '15, 18:08</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-45614" class="comments-container">
&#10;</div>
<div id="comment-tools-45614" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45614-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="45617"></span>

<div id="answer-container-45617" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-45617-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45617-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-45617-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There seem to be problems with the geometry at the moment as well. This can also lead to Nominatim ignoring it.</p>
<p><a href="http://ra.osmsurround.org/analyzeRelation?relationId=5527857&amp;noCache=true&amp;_noCache=on">http://ra.osmsurround.org/analyzeRelation?relationId=5527857&amp;noCache=true&amp;_noCache=on</a> <a href="http://ra.osmsurround.org/analyzeRelation?relationId=5537968&amp;noCache=true&amp;_noCache=on">http://ra.osmsurround.org/analyzeRelation?relationId=5537968&amp;noCache=true&amp;_noCache=on</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Sep '15, 18:40</strong></p>
<img src="https://secure.gravatar.com/avatar/81868786ff539d9a5b1f21ed57b6e13a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="csmale&#39;s gravatar image" />
<p><span>csmale</span><br />
<span class="score" title="81 reputation points">81</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="csmale has one accepted answer">16%</span></p>
</div>
</div>
<div id="comments-container-45617" class="comments-container">
<span id="45618"></span>
<div id="comment-45618" class="comment">
<div id="post-45618-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>quite correct, thanks. I removed the outer boundary (on roads etc.) to leave only the various POIs. Searching for "Goodwood" displays the relation as the top hit and the relation analyzer says everything is all <a href="http://ra.osmsurround.org/analyzeRelation?relationId=5527857&amp;noCache=true&amp;_noCache=on">ok</a>. Thanks.</p>
</div>
<div id="comment-45618-info" class="comment-info">
<span class="comment-age">(27 Sep '15, 20:34)</span> <span class="comment-user userinfo">snodnipper</span>
</div>
</div>
</div>
<div id="comment-tools-45617" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45617-form-container" class="comment-form-container">
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

