+++
type = "question"
title = "Problems with limiting overpass results to admin boundaries"
description = '''Hey all, whilst I thought I was somewhat getting the hang over the Overpass API, a fairly basic usecase has me stumped! I want to extract the enclosing administrative boundary when providing a lat and long, looking to extract levels 10, 9 and 8.  I have been able to extract all surrounding relations...'''
date = "2021-07-14T20:51:00Z"
lastmod = "2021-08-22T18:50:00Z"
weight = 80975
keywords = [ "admin_boundary", "overpass-turbo" ]
aliases = [ "/questions/80975" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Problems with limiting overpass results to admin boundaries](/questions/80975/problems-with-limiting-overpass-results-to-admin-boundaries)

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
<span id="post-80975-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80975-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-80975-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hey all,</p>
<p>whilst I thought I was somewhat getting the hang over the Overpass API, a fairly basic usecase has me stumped!</p>
<p>I want to extract the enclosing administrative boundary when providing a lat and long, looking to extract levels 10, 9 and 8.</p>
<p>I have been able to extract all surrounding relations by doing the following query, which pulls back far too much information including the county, country and UK as a whole:</p>
<pre><code>   [timeout:25][out:json];
    is_in(52.0246,0.80801)-&gt;.a;way(pivot.a);out tags ;relation(pivot.a);out tags bb;</code></pre>
<p>I have tried to limit the results with:</p>
<pre><code>area[&#39;admin_level&#39;=&#39;10&#39;];</code></pre>
<p>and various relations but that hasn't limited the results at all. Could someone please help? Much appreciated!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-admin_boundary" rel="tag" title="see questions tagged &#39;admin_boundary&#39;">admin_boundary</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Jul '21, 20:51</strong></p>
<img src="https://secure.gravatar.com/avatar/3a8741e4f134361ff5187b09a39dc16a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nikotime&#39;s gravatar image" />
<p><span>nikotime</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nikotime has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-80975" class="comments-container">
&#10;</div>
<div id="comment-tools-80975" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80975-form-container" class="comment-form-container">
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

<span id="80982"></span>

<div id="answer-container-80982" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-80982-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80982-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-80982-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="nikotime has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you want only those relations tagged with admin_level=10 you can say it when requesting them:</p>
<pre><code>[timeout:25][out:json];
is_in(52.0246,0.80801)-&gt;.a;
relation(pivot.a)[admin_level=10];
out tags bb;</code></pre>
<p>If you want even those with admin_level 8 and 9 then the code gets slightly larger:</p>
<pre><code>[timeout:25][out:json];
is_in(52.0246,0.80801)-&gt;.a;
relation(pivot.a)(if:t[&quot;admin_level&quot;]&gt;=8 &amp;&amp; t[&quot;admin_level&quot;]&lt;=10);
out tags bb;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Jul '21, 11:57</strong></p>
<img src="https://secure.gravatar.com/avatar/9c8957ccf79025bf749665ebec2bdfa2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MarcoR&#39;s gravatar image" />
<p><span>MarcoR</span><br />
<span class="score" title="687 reputation points">687</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MarcoR has 5 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-80982" class="comments-container">
<span id="80995"></span>
<div id="comment-80995" class="comment">
<div id="post-80995-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thats absolutely spot on. Thanks so much Marco for your help!</p>
</div>
<div id="comment-80995-info" class="comment-info">
<span class="comment-age">(16 Jul '21, 08:16)</span> <span class="comment-user userinfo">nikotime</span>
</div>
</div>
</div>
<div id="comment-tools-80982" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80982-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="81417"></span>

<div id="answer-container-81417" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-81417-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81417-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81417-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<pre><code>is_in(52.0246,0.80801);
rel(pivot)[admin_level~&quot;[2,8,9,10]&quot;];
out geom;</code></pre>
<p>No requirement to store output in a variable (a) if only to be used once. Pivot will used the default output.</p>
<p>Regex is used to filter the required admin_level. Note the 'something like' symbol.</p>
<p>Pivot converts area to objects.</p>
<p>Edit:</p>
<p>To output just the tags there's no need to pivot</p>
<pre><code>is_in(52.0246,0.80801);
area._[admin_level~&quot;[2,8,9,10]&quot;]; 
out tags;</code></pre>
<p>PS If you're just wanting to output a list, maybe take a look at <code>out:csv</code>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Aug '21, 18:50</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Aug '21, 19:21</strong> </span></p>
</div>
</div>
<div id="comments-container-81417" class="comments-container">
&#10;</div>
<div id="comment-tools-81417" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81417-form-container" class="comment-form-container">
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

