+++
type = "question"
title = "(overpass turbo) Children relations missing."
description = '''Why don&#x27;t all showing here: [out:csv(::type, ::id, name, admin_level, parent_id)]; rel(148838)-&amp;gt;.c; .c map_to_area; rel(area)[admin_level=&quot;4&quot;][boundary=administrative][type!=multilinestring]; out;  show here: [out:csv(::type, ::id, name, admin_level, parent_id)]; rel(148838)-&amp;gt;.c; .c map_to_are...'''
date = "2018-07-30T22:43:00Z"
lastmod = "2018-07-31T11:55:00Z"
weight = 65034
keywords = [ "overpass", "overpass-turbo", "relations" ]
aliases = [ "/questions/65034" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [(overpass turbo) Children relations missing.](/questions/65034/overpass-turbo-children-relations-missing)

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
<span id="post-65034-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65034-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65034-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Why don't all showing here:</p>
<pre><code>[out:csv(::type, ::id, name, admin_level, parent_id)];
rel(148838)-&gt;.c;
.c map_to_area;
rel(area)[admin_level=&quot;4&quot;][boundary=administrative][type!=multilinestring];
out;</code></pre>
<p>show here:</p>
<pre><code>[out:csv(::type, ::id, name, admin_level, parent_id)];
rel(148838)-&gt;.c;
.c map_to_area;
rel(area)[admin_level=&quot;2&quot;][boundary=administrative][type!=multilinestring];
foreach(
  out ids;
  rel(r); //children
  out;
);</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Jul '18, 22:43</strong></p>
<img src="https://secure.gravatar.com/avatar/7dcc267e54465a74eea1ce059e3432f9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andrefrsilva&#39;s gravatar image" />
<p><span>andrefrsilva</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andrefrsilva has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-65034" class="comments-container">
&#10;</div>
<div id="comment-tools-65034" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65034-form-container" class="comment-form-container">
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

<span id="65038"></span>

<div id="answer-container-65038" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-65038-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65038-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65038-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I guess that not all admin_level=4 relations added as children to the admin_level=2 relation. Juust being mapped as nested boundary relations is not enough. The admin_level=4 boundaries should be explicitly added to the admin_level=2 relation.</p>
<p>AFAIK, it is not common practice to do this. I even thought that the wiki adviced against it, but I cannot find a reference for that now.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Jul '18, 04:13</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-65038" class="comments-container">
<span id="65039"></span>
<div id="comment-65039" class="comment">
<div id="post-65039-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>So what should I do instead to get the children relations of each relation?</p>
</div>
<div id="comment-65039-info" class="comment-info">
<span class="comment-age">(31 Jul '18, 11:55)</span> <span class="comment-user userinfo">andrefrsilva</span>
</div>
</div>
</div>
<div id="comment-tools-65038" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65038-form-container" class="comment-form-container">
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

