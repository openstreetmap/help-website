+++
type = "question"
title = "Xapi Problems camp_sites"
description = '''Hi, I want to get all Campingsites in a area, but many campsites are missing when i call following Xapi: http://www.overpass-api.de/api/xapi?node[tourism=camp_site][bbox=10.65674,49.33228,11.71143,50.35948] e.g Die Campinginsel (164951603) there are many others missing. E.G. Sommerach... I don&#x27;t und...'''
date = "2016-07-26T07:56:00Z"
lastmod = "2016-07-26T15:39:00Z"
weight = 51099
keywords = [ "overpass", "xapi" ]
aliases = [ "/questions/51099" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Xapi Problems camp_sites](/questions/51099/xapi-problems-camp_sites)

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
<span id="post-51099-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51099-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-51099-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I want to get all Campingsites in a area, but many campsites are missing when i call following Xapi:</p>
<p><a href="http://www.overpass-api.de/api/xapi?node%5Btourism=camp_site%5D%5Bbbox=10.65674,49.33228,11.71143,50.35948%5D">http://www.overpass-api.de/api/xapi?node[tourism=camp_site][bbox=10.65674,49.33228,11.71143,50.35948]</a></p>
<p>e.g Die Campinginsel (164951603) there are many others missing. E.G. Sommerach... I don't understand because the tag tourism=camp_site is correctly set.</p>
<p>greetings from Bamberg/Germany Rainer</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-xapi" rel="tag" title="see questions tagged &#39;xapi&#39;">xapi</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Jul '16, 07:56</strong></p>
<img src="https://secure.gravatar.com/avatar/34b47f643d640c5bee2254d2456b6ada?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rr001&#39;s gravatar image" />
<p><span>rr001</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rr001 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Jul '16, 08:36</strong> </span></p>
</div>
</div>
<div id="comments-container-51099" class="comments-container">
<span id="51100"></span>
<div id="comment-51100" class="comment">
<div id="post-51100-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I've seen this is an area not a poi. my really problem is to import pois into my Android Locus how can i get all camp_sites areas and show them as pois in my android app? is this possible?</p>
</div>
<div id="comment-51100-info" class="comment-info">
<span class="comment-age">(26 Jul '16, 08:08)</span> <span class="comment-user userinfo">rr001</span>
</div>
</div>
</div>
<div id="comment-tools-51099" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51099-form-container" class="comment-form-container">
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

<span id="51103"></span>

<div id="answer-container-51103" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-51103-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51103-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-51103-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="rr001 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Not sure about Overpass, but in Overpass Turbo, you can do this:</p>
<pre><code>[out:json]
[timeout:25]
;
(
  node
    [&quot;tourism&quot;=&quot;camp_site&quot;]
    (10.65674,49.33228,11.71143,50.35948);
  way
    [&quot;tourism&quot;=&quot;camp_site&quot;]
    (10.65674,49.33228,11.71143,50.35948);
);
out body;
&gt;;
out skel qt;</code></pre>
<p>which returns both nodes and ways tagged camp_site.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Jul '16, 13:04</strong></p>
<img src="https://secure.gravatar.com/avatar/8200fa5c0cc8feb096558c5972a6191c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Piskvor&#39;s gravatar image" />
<p><span>Piskvor</span><br />
<span class="score" title="1266 reputation points"><span>1.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="35 badges"><span class="bronze">●</span><span class="badgecount">35</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Piskvor has 9 accepted answers">37%</span></p>
</div>
</div>
<div id="comments-container-51103" class="comments-container">
<span id="51111"></span>
<div id="comment-51111" class="comment">
<div id="post-51111-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>thank you i didn't know that there are ways and relations too that was it. but in Locus this camingSites where shown as Tracks Never Mind, it's not the best but it's ok for me</p>
</div>
<div id="comment-51111-info" class="comment-info">
<span class="comment-age">(26 Jul '16, 15:12)</span> <span class="comment-user userinfo">rr001</span>
</div>
</div>
<span id="51112"></span>
<div id="comment-51112" class="comment">
<div id="post-51112-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>You can use 'out center;' to have Overpass API convert the areas to pois:</p>
<p><a href="http://overpass-turbo.eu/s/hvP">http://overpass-turbo.eu/s/hvP</a></p>
<p>Don't miss the 'GPX' option under the Export function.</p>
</div>
<div id="comment-51112-info" class="comment-info">
<span class="comment-age">(26 Jul '16, 15:39)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
</div>
<div id="comment-tools-51103" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51103-form-container" class="comment-form-container">
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

