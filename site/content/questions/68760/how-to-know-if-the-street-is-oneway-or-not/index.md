+++
type = "question"
title = "How to know if the street is oneway or not"
description = '''Hi!  I am using overpass turbo to extract data from OpenStreetMap. I export the data in Json format and in the data I can find information about the speed at the road for an example. But I also want to know if the road is a oneway road or not. How can I write the code to tell me if it is a oneway or...'''
date = "2019-04-11T10:32:00Z"
lastmod = "2019-04-12T06:21:00Z"
weight = 68760
keywords = [ "overpass-turbo", "highway", "oneway" ]
aliases = [ "/questions/68760" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to know if the street is oneway or not](/questions/68760/how-to-know-if-the-street-is-oneway-or-not)

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
<span id="post-68760-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68760-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-68760-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi! I am using overpass turbo to extract data from OpenStreetMap. I export the data in Json format and in the data I can find information about the speed at the road for an example. But I also want to know if the road is a oneway road or not. How can I write the code to tell me if it is a oneway or not? This is my code for residential roads now.</p>
<pre><code>  &lt;query type=&quot;way&quot; into=&quot;data&quot;&gt;
    &lt;bbox-query {{bbox}}/&gt;
    &lt;has-kv k=&quot;highway&quot; v=&quot;residential&quot;/&gt;
  &lt;/query&gt;</code></pre>
<p>What do I need to add? Sincerely, Gustav</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span> <span class="post-tag tag-link-highway" rel="tag" title="see questions tagged &#39;highway&#39;">highway</span> <span class="post-tag tag-link-oneway" rel="tag" title="see questions tagged &#39;oneway&#39;">oneway</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Apr '19, 10:32</strong></p>
<img src="https://secure.gravatar.com/avatar/887638889ae8c64730350622782182dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gustav&#39;s gravatar image" />
<p><span>Gustav</span><br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gustav has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Apr '19, 12:31</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-68760" class="comments-container">
&#10;</div>
<div id="comment-tools-68760" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68760-form-container" class="comment-form-container">
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

<span id="68766"></span>

<div id="answer-container-68766" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68766-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68766-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-68766-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You do not have to adapt your query if you want all residential roads. The reply will also contain oneway streets. Those streets will have the extra tag oneway=yes or oneway=-1. The latter means that the oneway is in the opposite direction of the drawing of the way.</p>
<p>If you only want oneway streets, you have to add</p>
<p>&lt;has-kv k="oneway" regv="yes|-1"/&gt;</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Apr '19, 06:21</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-68766" class="comments-container">
&#10;</div>
<div id="comment-tools-68766" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68766-form-container" class="comment-form-container">
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

