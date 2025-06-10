+++
type = "question"
title = "How merge this three OverPass"
description = '''Good morning, I&#x27;m trying to merge these three OverPass requests into one request... Goal: find bus platforms, bus shelters with bus stops that are not connected to paths Is that possible? Thanking you in advance Sorry, script n°1 is not unreadable, code is not format correctly Script n°1 [out:json][...'''
date = "2020-06-03T12:24:00Z"
lastmod = "2020-06-08T08:25:00Z"
weight = 75115
keywords = [ "overpass", "public-transport", "platform" ]
aliases = [ "/questions/75115" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How merge this three OverPass](/questions/75115/how-merge-this-three-overpass)

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
<span id="post-75115-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75115-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-75115-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Good morning,</p>
<p>I'm trying to merge these three OverPass requests into one request... Goal: find bus platforms, bus shelters with bus stops that are not connected to paths</p>
<p>Is that possible? Thanking you in advance</p>
<p>Sorry, script n°1 is not unreadable, code is not format correctly</p>
<p><strong>Script n°1</strong></p>
<pre><code>[out:json][timeout:25];
(
  node[&quot;highway&quot;=&quot;platform&quot;][&quot;railway&quot;!~&quot;.*&quot;]({{bbox}});
  way[&quot;highway&quot;=&quot;platform&quot;][&quot;railway&quot;!~&quot;.*&quot;]({{bbox}});
  node[&quot;public_transport&quot;=&quot;platform&quot;][&quot;railway&quot;!~&quot;.*&quot;]({{bbox}});
  way[&quot;public_transport&quot;=&quot;platform&quot;][&quot;railway&quot;!~&quot;.*&quot;]({{bbox}});
  node[&quot;amenity&quot;=&quot;shelter&quot;][&quot;shelter_type&quot;=&quot;public_transport&quot;][&quot;railway&quot;!~&quot;.*&quot;]({{bbox}});
  way[&quot;amenity&quot;=&quot;shelter&quot;][&quot;shelter_type&quot;=&quot;public_transport&quot;][&quot;railway&quot;!~&quot;.*&quot;]({{bbox}});
);
out body;
&gt;;
out skel qt;</code></pre>
<p><strong>Script n°2</strong></p>
<pre><code>[bbox:{{bbox}}];
rel; &gt; -&gt; .r;
way; &gt; -&gt; .w;
(( node[&quot;highway&quot;=&quot;bus_stop&quot;]; - node.r; );  - node.w; );
out meta;</code></pre>
<p><strong>Script n°3</strong></p>
<pre><code>[bbox:{{bbox}}];
rel; &gt; -&gt; .r;
way; &gt; -&gt; .w;
(( node[&quot;public_transport&quot;=&quot;stop_position&quot;][&quot;bus&quot;=&quot;yes&quot;]; - node.r; );  - node.w; );
out meta;</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-public-transport" rel="tag" title="see questions tagged &#39;public-transport&#39;">public-transport</span> <span class="post-tag tag-link-platform" rel="tag" title="see questions tagged &#39;platform&#39;">platform</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Jun '20, 12:24</strong></p>
<img src="https://secure.gravatar.com/avatar/2a19ca930e36061b3b1e7efdbdd65a5d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="percherie&#39;s gravatar image" />
<p><span>percherie</span><br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="percherie has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Jun '20, 14:37</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span></p>
</div>
</div>
<div id="comments-container-75115" class="comments-container">
<span id="75117"></span>
<div id="comment-75117" class="comment">
<div id="post-75117-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>In Overpass Turbo use the 'link' to provide routines directly.</p>
<p><a href="https://overpass-turbo.eu/s/UER">https://overpass-turbo.eu/s/UER</a></p>
</div>
<div id="comment-75117-info" class="comment-info">
<span class="comment-age">(03 Jun '20, 13:32)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
</div>
<div id="comment-tools-75115" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75115-form-container" class="comment-form-container">
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

<span id="75122"></span>

<div id="answer-container-75122" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-75122-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75122-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-75122-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Thank you, DaveF,</p>
<p>What I miss is the recovery of the isolated nodes as in the following request. (generate share link is broken with my station)</p>
<p>How to merge everything?</p>
<pre><code>[bbox:{{bbox}}];
way; &gt; -&gt; .w;
(( node[&quot;public_transport&quot;=&quot;stop_position&quot;][&quot;bus&quot;=&quot;yes&quot;]; - node.w; );
out meta;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Jun '20, 16:41</strong></p>
<img src="https://secure.gravatar.com/avatar/2a19ca930e36061b3b1e7efdbdd65a5d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="percherie&#39;s gravatar image" />
<p><span>percherie</span><br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="percherie has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Jun '20, 16:42</strong> </span></p>
</div>
</div>
<div id="comments-container-75122" class="comments-container">
&#10;</div>
<div id="comment-tools-75122" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75122-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="75195"></span>

<div id="answer-container-75195" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-75195-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75195-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-75195-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<pre><code>[out:json][bbox:{{bbox}}];
way; &gt; -&gt; .w;
( node[&quot;highway&quot;=&quot;bus_stop&quot;]; - node.w; );
out meta;
&#10;(
  node[&quot;highway&quot;=&quot;platform&quot;][&quot;railway&quot;!~&quot;.*&quot;]({{bbox}});
  way[&quot;highway&quot;=&quot;platform&quot;][&quot;railway&quot;!~&quot;.*&quot;]({{bbox}});
&#10;  node[&quot;public_transport&quot;=&quot;platform&quot;][&quot;railway&quot;!~&quot;.*&quot;]({{bbox}});
  way[&quot;public_transport&quot;=&quot;platform&quot;][&quot;railway&quot;!~&quot;.*&quot;]({{bbox}});
&#10;  node[&quot;shelter_type&quot;=&quot;public_transport&quot;][&quot;railway&quot;!~&quot;.*&quot;]({{bbox}});
  way[&quot;shelter_type&quot;=&quot;public_transport&quot;][&quot;railway&quot;!~&quot;.*&quot;]({{bbox}});
);
out body;
&gt;;
out skel qt;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Jun '20, 08:25</strong></p>
<img src="https://secure.gravatar.com/avatar/2a19ca930e36061b3b1e7efdbdd65a5d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="percherie&#39;s gravatar image" />
<p><span>percherie</span><br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="percherie has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-75195" class="comments-container">
&#10;</div>
<div id="comment-tools-75195" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75195-form-container" class="comment-form-container">
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

