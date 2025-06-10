+++
type = "question"
title = "Best way to query train lines?"
description = '''Hello, I&#x27;d like to get all the disused train lines in France. The following query can time-out, and iOT isn&#x27;t happy if I run it again (&quot;Check your quota&quot;): [out:json][timeout:25];  //Metropolitan France 1403916 rel(1403916); map_to_area -&amp;gt; .searchArea;  (  way[railway~&quot;(disused|abandoned)&quot;](area....'''
date = "2021-08-25T18:44:00Z"
lastmod = "2021-08-26T18:11:00Z"
weight = 81484
keywords = [ "overpass-turbo" ]
aliases = [ "/questions/81484" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Best way to query train lines?](/questions/81484/best-way-to-query-train-lines)

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
<span id="post-81484-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81484-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81484-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I'd like to get all the disused train lines in France.</p>
<p>The following query can time-out, and iOT isn't happy if I run it again ("Check your quota"):</p>
<pre><code>[out:json][timeout:25];
&#10;//Metropolitan France 1403916
rel(1403916);
map_to_area -&gt; .searchArea;
&#10;(
  way[railway~&quot;(disused|abandoned)&quot;](area.searchArea);
);
&#10;out geom;</code></pre>
<p>Is there a better way, possibly using the command-line?</p>
<p>Thank you.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Aug '21, 18:44</strong></p>
<img src="https://secure.gravatar.com/avatar/222fc1ad4f1993620a21cb57fa816f16?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Shohreh&#39;s gravatar image" />
<p><span>Shohreh</span><br />
<span class="score" title="85 reputation points">85</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Shohreh has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-81484" class="comments-container">
&#10;</div>
<div id="comment-tools-81484" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81484-form-container" class="comment-form-container">
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

<span id="81503"></span>

<div id="answer-container-81503" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-81503-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81503-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-81503-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Shohreh has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you're after actual closed railways the popular tags are:</p>
<pre><code>area(3600008640);
way[~&quot;(disused:railway|abandoned:railway)&quot;~&quot;^rail$&quot;](area); 
out geom;</code></pre>
<p>I've used a smaller relation for ease of explanation. For the whole of France &amp; Corsica use area(3601403916); (~20mb)</p>
<p>If you're specifically after tags which aren't the above then you'll almost certainly need to split your search into smaller areas as using the 'railway' key searched <em>all</em> values for it, which returns quite a bit more data than just 'rail'.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Aug '21, 15:38</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-81503" class="comments-container">
<span id="81507"></span>
<div id="comment-81507" class="comment">
<div id="post-81507-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks much for the syntax.</p>
</div>
<div id="comment-81507-info" class="comment-info">
<span class="comment-age">(26 Aug '21, 17:26)</span> <span class="comment-user userinfo">Shohreh</span>
</div>
</div>
</div>
<div id="comment-tools-81503" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81503-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="81508"></span>

<div id="answer-container-81508" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-81508-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81508-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81508-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Addendum to original answer:</p>
<p>You may get away with calling this just once, for the whole of the country (~40mb). The Regex '^' &amp; '$' means the search has to start &amp; end with those words so, in fact, it's only searching for whole words.</p>
<pre><code>area(3601403916);
way[railway~&quot;^(disused|abandoned)$&quot;](area);
out geom;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Aug '21, 18:01</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-81508" class="comments-container">
<span id="81509"></span>
<div id="comment-81509" class="comment">
<div id="post-81509-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'll give it a try, and see if OT doesn't complain with my querying too much data.</p>
</div>
<div id="comment-81509-info" class="comment-info">
<span class="comment-age">(26 Aug '21, 18:11)</span> <span class="comment-user userinfo">Shohreh</span>
</div>
</div>
</div>
<div id="comment-tools-81508" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81508-form-container" class="comment-form-container">
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

