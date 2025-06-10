+++
type = "question"
title = "Help in understanding which suburbs get returned in Nominatim search"
description = '''Hello, I need to understand why this happen. City of Arona in Italy has three suburbs, and one of the three is called Mercurago. I am searching in OSM: Via Piave, Arona  and Nominatim always returns: Residential Via Piave, Mercurago, Arona, Novara, Piemonte, Italy Mercurago is actually a suburb of A...'''
date = "2014-08-25T19:06:00Z"
lastmod = "2018-09-01T08:11:00Z"
weight = 36156
keywords = [ "suburb", "nominatim" ]
aliases = [ "/questions/36156" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Help in understanding which suburbs get returned in Nominatim search](/questions/36156/help-in-understanding-which-suburbs-get-returned-in-nominatim-search)

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
<span id="post-36156-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-36156-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-36156-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I need to understand why this happen.</p>
<p>City of Arona in Italy has three suburbs, and one of the three is called Mercurago.</p>
<p>I am searching in OSM: <strong>Via Piave, Arona</strong></p>
<p>and Nominatim always returns: <strong>Residential Via Piave, Mercurago, Arona, Novara, Piemonte, Italy</strong></p>
<p>Mercurago is actually a suburb of Arona, but Via Piave is in Arona and not in Mercurago.</p>
<p>Can you please help me in understanding why the suburb of Mercurago is always returned in all the search for Arona's roads, regardelss they are in Mercurago or not ?</p>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-suburb" rel="tag" title="see questions tagged &#39;suburb&#39;">suburb</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Aug '14, 19:06</strong></p>
<img src="https://secure.gravatar.com/avatar/081ae1820f5b4f18b8ad79c68a193b63?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxicampa&#39;s gravatar image" />
<p><span>maxicampa</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxicampa has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Aug '14, 15:59</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/cebf8499a8a3009705e261cfd224e8c0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="neuhausr&#39;s gravatar image" />
<p><span>neuhausr</span><br />
<span class="score" title="7460 reputation points"><span>7.5k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="70 badges"><span class="silver">●</span><span class="badgecount">70</span></span><span title="121 badges"><span class="bronze">●</span><span class="badgecount">121</span></span></p>
</div>
</div>
<div id="comments-container-36156" class="comments-container">
&#10;</div>
<div id="comment-tools-36156" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-36156-form-container" class="comment-form-container">
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

<span id="36218"></span>

<div id="answer-container-36218" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-36218-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-36218-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-36218-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="maxicampa has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Nominatim always composes the address based on the nodes that are the nearest. So probably the node representing Mercurago is so close to Via Piave that Nominatim assumes that is the suburb to take.</p>
<p>The only way to solve this is to replace the suburb node with a boundary relation representing the suburb. I would contact the Italian community to find out how this is normally done in Italy. E.g. are there sources from which the boundaries can be copied ?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Aug '14, 15:01</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-36218" class="comments-container">
<span id="65666"></span>
<div id="comment-65666" class="comment">
<div id="post-65666-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Would using "is_in=Arona" on the suburbs help Nominatim to get it right?</p>
</div>
<div id="comment-65666-info" class="comment-info">
<span class="comment-age">(01 Sep '18, 08:11)</span> <span class="comment-user userinfo">Joseph E</span>
</div>
</div>
</div>
<div id="comment-tools-36218" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-36218-form-container" class="comment-form-container">
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

