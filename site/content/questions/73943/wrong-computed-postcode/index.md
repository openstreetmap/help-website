+++
type = "question"
title = "wrong &#x27;computed postcode&#x27;"
description = '''Nominatim search for &quot;dukartstrasse, steyr&quot; (Centre Point 48.0362809,14.4202254) and other objects in this area returns objects with a computed postcode of &quot;4407&quot;, which is wrong. The correct postcode is &quot;4400&quot;. When searching with overpass for objects tagged with addr:postcode=4407 or 4400: node  [...'''
date = "2020-04-02T07:44:00Z"
lastmod = "2020-04-02T19:00:00Z"
weight = 73943
keywords = [ "nominatim", "postcode", "computed" ]
aliases = [ "/questions/73943" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [wrong 'computed postcode'](/questions/73943/wrong-computed-postcode)

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
<span id="post-73943-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73943-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73943-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Nominatim search for "dukartstrasse, steyr" (Centre Point 48.0362809,14.4202254) and other objects in this area returns objects with a computed postcode of "4407", which is wrong. The correct postcode is "4400".</p>
<p>When searching with overpass for objects tagged with addr:postcode=4407 or 4400:</p>
<pre><code>node
  [&quot;addr:postcode&quot;=4407]
  (48.0,14.3,48.11,14.6);
out;</code></pre>
<p>one can see that the objects with addr:postcode=4407 are further away (north) than the objects with addr:postcode=4400.</p>
<p>So why is the computed postcode "4407"? And how to correct the computed postcode (without tagging all objects in that area with addr:postcode=4400)?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-postcode" rel="tag" title="see questions tagged &#39;postcode&#39;">postcode</span> <span class="post-tag tag-link-computed" rel="tag" title="see questions tagged &#39;computed&#39;">computed</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Apr '20, 07:44</strong></p>
<img src="https://secure.gravatar.com/avatar/69bc02fd266c84783aa651ec3bc6da6c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="coproc&#39;s gravatar image" />
<p><span>coproc</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="coproc has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Apr '20, 07:45</strong> </span></p>
</div>
</div>
<div id="comments-container-73943" class="comments-container">
&#10;</div>
<div id="comment-tools-73943" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73943-form-container" class="comment-form-container">
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

<span id="73946"></span>

<div id="answer-container-73946" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73946-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73946-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-73946-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="coproc has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The postcode comes from the <a href="https://www.openstreetmap.org/relation/90143/history">relation of Steyr</a>. This used to have a postcode 4407 until 28 days ago. It is now 4400 but Nominatim has not yet picked that up in all of the town. I've forced a reindex and new 4400 should show up everywhere.</p>
<p>That said, when I look at the postcodes that are mapped already, I suspect this relation should not have a postcode tag at all because there is more than one postcode in use in its area. Nominatim will assume that a postcode on a administrative boundary means that it is valid everywhere. See <a href="https://www.openstreetmap.org/user/lonvia/diary/43143">this diary post</a> for details on how postcodes are computed.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Apr '20, 08:20</strong></p>
<img src="https://secure.gravatar.com/avatar/d888b712d85dee0aa304297f2dc697c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lonvia&#39;s gravatar image" />
<p><span>lonvia</span><br />
<span class="score" title="6213 reputation points"><span>6.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lonvia has 43 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-73946" class="comments-container">
<span id="73970"></span>
<div id="comment-73970" class="comment">
<div id="post-73970-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Only the district Steyr-Gleink and areas north of it (outside Steyr) have the postcode 4407. More than 90% of the area of the city of Steyr (and quite a few villages around) have postcode 4400. So we would need also relations for the districts of Steyr, which should then get a postcode assigned.</p>
</div>
<div id="comment-73970-info" class="comment-info">
<span class="comment-age">(02 Apr '20, 18:57)</span> <span class="comment-user userinfo">coproc</span>
</div>
</div>
<span id="73971"></span>
<div id="comment-73971" class="comment">
<div id="post-73971-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>btw: yes, postcode 4400 is now the new default for 'computed postcode' inside Steyr. Thank you!</p>
</div>
<div id="comment-73971-info" class="comment-info">
<span class="comment-age">(02 Apr '20, 19:00)</span> <span class="comment-user userinfo">coproc</span>
</div>
</div>
</div>
<div id="comment-tools-73946" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73946-form-container" class="comment-form-container">
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

