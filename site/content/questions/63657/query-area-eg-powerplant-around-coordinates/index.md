+++
type = "question"
title = "Query area (e.g. power=plant) around coordinates"
description = '''I&#x27;ve got a list of power plant locations. How can I query the presence and id of a power=plant way around this location?'''
date = "2018-05-23T19:13:00Z"
lastmod = "2018-05-24T18:45:00Z"
weight = 63657
keywords = [ "query", "location", "overpass" ]
aliases = [ "/questions/63657" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Query area (e.g. power=plant) around coordinates](/questions/63657/query-area-eg-powerplant-around-coordinates)

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
<span id="post-63657-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63657-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-63657-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've got a list of power plant locations.</p>
<p>How can I query the presence and id of a power=plant way around this location?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span> <span class="post-tag tag-link-location" rel="tag" title="see questions tagged &#39;location&#39;">location</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 May '18, 19:13</strong></p>
<img src="https://secure.gravatar.com/avatar/bdb6a1b49c42d8be4b8d87f3096a3622?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Druzhba&#39;s gravatar image" />
<p><span>Druzhba</span><br />
<span class="score" title="150 reputation points">150</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Druzhba has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-63657" class="comments-container">
<span id="63660"></span>
<div id="comment-63660" class="comment">
<div id="post-63660-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Relative_to_other_elements_.28around.29">https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Relative_to_other_elements_.28around.29</a></p>
</div>
<div id="comment-63660-info" class="comment-info">
<span class="comment-age">(23 May '18, 21:11)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
<span id="63704"></span>
<div id="comment-63704" class="comment">
<div id="post-63704-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Why does it not find <a href="https://www.openstreetmap.org/way/12805981">BMW</a> ?</p>
<pre><code>[out:json][timeout:600];
(
way(around:300,51.404924,12.444895)[&quot;landuse&quot;=&quot;industrial&quot;];
);
out body;
&gt;;
out skel qt;</code></pre>
</div>
<div id="comment-63704-info" class="comment-info">
<span class="comment-age">(24 May '18, 18:25)</span> <span class="comment-user userinfo">Druzhba</span>
</div>
</div>
<span id="63708"></span>
<div id="comment-63708" class="comment">
<div id="post-63708-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That way is more than 300 metres away from the coordinates you're checking. You'll need to increase the "around" distance.</p>
</div>
<div id="comment-63708-info" class="comment-info">
<span class="comment-age">(24 May '18, 18:45)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
</div>
<div id="comment-tools-63657" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63657-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

