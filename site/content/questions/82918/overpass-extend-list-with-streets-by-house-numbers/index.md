+++
type = "question"
title = "Overpass: Extend list with streets by house numbers"
description = '''Hello, I am using Overpass to list all streets for an area. Now I want to extend the query with the house numbers. Preferably the smallest and largest house number per street. Do you have any ideas? I found another query for house numbers. Is it possible to combine them? Here is my query so far: [ou...'''
date = "2021-12-30T13:23:00Z"
lastmod = "2021-12-31T10:11:00Z"
weight = 82918
keywords = [ "overpass", "housenumbers" ]
aliases = [ "/questions/82918" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Overpass: Extend list with streets by house numbers](/questions/82918/overpass-extend-list-with-streets-by-house-numbers)

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
<span id="post-82918-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82918-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82918-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I am using Overpass to list all streets for an area. Now I want to extend the query with the house numbers. Preferably the smallest and largest house number per street. Do you have any ideas? I found another query for house numbers. Is it possible to combine them?</p>
<p>Here is my query so far:</p>
<p>[out:csv(key;false)]; {{plz=33039}} area[postal_code="{{plz}}"]; way(area)[highway~"^trunk$|^primary$|^secondary$|^tertiary$|^unclassified$|^residential$|^primary_link$|^living_street$|^service$|^pedestrian$|^track$|^road$|^footway$|^bridleway$|^path$"][name]; for (t["name"]) ( make stat num=count(ways),key=_.val,len=sum(length()); out; );</p>
<p>Here is the query for house numbers:</p>
<p>[out:csv("addr:housenumber")][timeout:25]; {{geocodeArea:Nieheim}}-&gt;.searchArea;</p>
<p>( nwr["building"]["addr:street"="Steinheimer Straße"]<a href="area.searchArea">"addr:housenumber"</a>; ); out body;</p>
<blockquote>
<p>; out skel qt;</p>
</blockquote>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-housenumbers" rel="tag" title="see questions tagged &#39;housenumbers&#39;">housenumbers</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Dec '21, 13:23</strong></p>
<img src="https://secure.gravatar.com/avatar/9ef1464b1fd6b33c9a796c14a1f19ada?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="elvitas&#39;s gravatar image" />
<p><span>elvitas</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="elvitas has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-82918" class="comments-container">
<span id="82924"></span>
<div id="comment-82924" class="comment">
<div id="post-82924-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Your routines appear to be incomplete. Provide OP links to them.</p>
</div>
<div id="comment-82924-info" class="comment-info">
<span class="comment-age">(30 Dec '21, 20:36)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
</div>
<div id="comment-tools-82918" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82918-form-container" class="comment-form-container">
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

<span id="82925"></span>

<div id="answer-container-82925" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82925-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82925-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82925-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Naik Muhammad Rind [</p>
<blockquote>
<p><code>![link text][1]</code></p>
</blockquote>
<p>]<a href="http://">1</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Dec '21, 10:11</strong></p>
<img src="https://secure.gravatar.com/avatar/b9f49f7856fda3b7ea1391c9c6902ad6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Naik%20M%20Rind&#39;s gravatar image" />
<p><span>Naik M Rind</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Naik M Rind has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-82925" class="comments-container">
&#10;</div>
<div id="comment-tools-82925" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82925-form-container" class="comment-form-container">
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

