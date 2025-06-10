+++
type = "question"
title = "Can anyone help me with this overpass query?"
description = '''Sorry I am new to this API. It&#x27;s not very easy to learn. I&#x27;ve worked with API for 5 years and never seen something so confusing lol.  I&#x27;m trying to search a coordinate and find the building around it. So far I can search a coordinate and check if a feature is in it. But what I want to do is if it is...'''
date = "2022-10-26T21:55:00Z"
lastmod = "2022-10-27T16:28:00Z"
weight = 86001
keywords = [ "overpass", "osm" ]
aliases = [ "/questions/86001" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Can anyone help me with this overpass query?](/questions/86001/can-anyone-help-me-with-this-overpass-query)

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
<span id="post-86001-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86001-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86001-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Sorry I am new to this API. It's not very easy to learn. I've worked with API for 5 years and never seen something so confusing lol.</p>
<p>I'm trying to search a coordinate and find the building around it. So far I can search a coordinate and check if a feature is in it. But what I want to do is if it is not on that coordinate I want to be able to search 20 meter radius to check if it's there. So far my query looks like this. Below code will output the building at that coordinate, which works.</p>
<pre><code>[out:json];
is_in(42.1214989,-88.4187053);
area._[building~&quot;^(industrial|warehouse)$&quot;];
(._;&gt;;);
out geom;</code></pre>
<p>I tried this code and can't get it to work. I tried 100 of different variants. I'm close.</p>
<pre><code>[out:json];
area._[building~&quot;^(industrial|warehouse)$&quot;(around:200,42.1214989,-88.4187053);
(._;&gt;;);
out geom;</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Oct '22, 21:55</strong></p>
<img src="https://secure.gravatar.com/avatar/b3924436d51bf954e5256776d626bedc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="KrisMapper&#39;s gravatar image" />
<p><span>KrisMapper</span><br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="KrisMapper has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Oct '22, 22:02</strong> </span></p>
</div>
</div>
<div id="comments-container-86001" class="comments-container">
&#10;</div>
<div id="comment-tools-86001" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86001-form-container" class="comment-form-container">
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

<span id="86009"></span>

<div id="answer-container-86009" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-86009-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86009-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86009-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<pre><code>way[building~&quot;^(industrial|warehouse)$&quot;](around:200,42.1214989,-88.4187053);
out geom;</code></pre>
<p><code>Area</code> does not work with <code>around</code>.</p>
<p><code>._</code> is the default set from the previous command, so it can't be used in the initial statement.</p>
<p>You were missing a closing square bracket.</p>
<p>I'm also still confused by area/is_in/around/pivot commands. for instance if you search for <code>boundary</code> using your first routine it returns data, but doesn't output them.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Oct '22, 16:28</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Oct '22, 16:29</strong> </span></p>
</div>
</div>
<div id="comments-container-86009" class="comments-container">
&#10;</div>
<div id="comment-tools-86009" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86009-form-container" class="comment-form-container">
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

