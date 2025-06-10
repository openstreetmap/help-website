+++
type = "question"
title = "[closed] Overpass Turbo doesn&#x27;t find all parkings"
description = '''I&#x27;m newbie on Overpass Turbo. In JOSM I entered following query: area[&quot;name&quot;=&quot;Arboga kommun&quot;]; nwr[&quot;amenity&quot;=&quot;parking&quot;](area); out;  But it only returns parking&#x27;s mapped on nodes, but not parking areas. All of these have tag &quot;amenity=parking&quot;. What do I wrong?'''
date = "2022-07-23T15:03:00Z"
lastmod = "2022-07-23T18:35:00Z"
weight = 85202
keywords = [ "overpass-turbo" ]
aliases = [ "/questions/85202" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [\[closed\] Overpass Turbo doesn't find all parkings](/questions/85202/closed-overpass-turbo-doesnt-find-all-parkings)

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
<span id="post-85202-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85202-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-85202-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm newbie on Overpass Turbo.</p>
<p>In JOSM I entered following query:</p>
<pre><code>area[&quot;name&quot;=&quot;Arboga kommun&quot;];
nwr[&quot;amenity&quot;=&quot;parking&quot;](area);
out;</code></pre>
<p>But it only returns parking's mapped on nodes, but not parking areas. All of these have tag "amenity=parking".</p>
<p>What do I wrong?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Jul '22, 15:03</strong></p>
<img src="https://secure.gravatar.com/avatar/7fbbe44e24bdb695025fddb0879817a5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Msiipola&#39;s gravatar image" />
<p><span>Msiipola</span><br />
<span class="score" title="227 reputation points">227</span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="18 badges"><span class="silver">●</span><span class="badgecount">18</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Msiipola has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Jul '22, 18:36</strong> </span></p>
</div>
</div>
<div id="comments-container-85202" class="comments-container">
&#10;</div>
<div id="comment-tools-85202" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85202-form-container" class="comment-form-container">
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

<span id="85203"></span>

<div id="answer-container-85203" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-85203-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85203-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-85203-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Msiipola has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><code>out</code> on its own doesn't download the lat/lon for nodes that make up ways, so can't display them.</p>
<pre><code>area[name=&quot;Arboga kommun&quot;];
nwr[amenity=parking](area);
(._;&gt;;); out meta;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Jul '22, 18:09</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-85203" class="comments-container">
<span id="85204"></span>
<div id="comment-85204" class="comment">
<div id="post-85204-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the clarification! I knew I had missed something!</p>
</div>
<div id="comment-85204-info" class="comment-info">
<span class="comment-age">(23 Jul '22, 18:35)</span> <span class="comment-user userinfo">Msiipola</span>
</div>
</div>
</div>
<div id="comment-tools-85203" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85203-form-container" class="comment-form-container">
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

