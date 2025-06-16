+++
type = "question"
title = "Overpass turbo: extract all relation members with specific tags"
description = '''How to extract, from a bicycle route relation, all way-type members that are roads of type unclassified and higher and that do not have maxspeed tags '''
date = "2021-09-11T13:41:00Z"
lastmod = "2021-09-30T16:31:00Z"
weight = 81718
keywords = [ "member", "overpass", "relations" ]
aliases = [ "/questions/81718" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Overpass turbo: extract all relation members with specific tags](/questions/81718/overpass-turbo-extract-all-relation-members-with-specific-tags)

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
<span id="post-81718-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81718-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81718-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How to extract, from a bicycle route relation, all way-type members that are roads of type unclassified and higher and that do not have maxspeed tags</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-member" rel="tag" title="see questions tagged &#39;member&#39;">member</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Sep '21, 13:41</strong></p>
<img src="https://secure.gravatar.com/avatar/0a45ba8bcc4b69a12b3e817afff187e7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="voschix&#39;s gravatar image" />
<p><span>voschix</span><br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="voschix has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-81718" class="comments-container">
<span id="81719"></span>
<div id="comment-81719" class="comment">
<div id="post-81719-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Show us your routine as it is at the moment.</p>
</div>
<div id="comment-81719-info" class="comment-info">
<span class="comment-age">(11 Sep '21, 15:32)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
<span id="81720"></span>
<div id="comment-81720" class="comment">
<div id="post-81720-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have no routine at the moment. I would like to create a new one. I would like to complete the maxspeed information on cycle routes were these run on public roads.</p>
</div>
<div id="comment-81720-info" class="comment-info">
<span class="comment-age">(11 Sep '21, 21:15)</span> <span class="comment-user userinfo">voschix</span>
</div>
</div>
<span id="81723"></span>
<div id="comment-81723" class="comment">
<div id="post-81723-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Why not have an attempt? Expecting others to do the /whole/ job for you is a bit selfish.</p>
</div>
<div id="comment-81723-info" class="comment-info">
<span class="comment-age">(13 Sep '21, 14:35)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
</div>
<div id="comment-tools-81718" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81718-form-container" class="comment-form-container">
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

<span id="81722"></span>

<div id="answer-container-81722" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-81722-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81722-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-81722-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="scai has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Let's assume your bicycle route relation is within a set called "bike". Then, overpass turbo will provide you with all way-type members if you query for "way(r.bike)". Here, you can apply any filters you want, e.g. "way(r.bike)[highway=unclassified][!maxspeed]".</p>
<p>Here, an example which has one additional step to only search in the displayed area ("bbox"): <a href="https://overpass-turbo.eu/s/1b88">https://overpass-turbo.eu/s/1b88</a></p>
<p>Good luck!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Sep '21, 14:18</strong></p>
<img src="https://secure.gravatar.com/avatar/ffb12f7c2548687764b2de9e4562d2d9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="G%C3%A5seborg&#39;s gravatar image" />
<p><span>Gåseborg</span><br />
<span class="score" title="311 reputation points">311</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gåseborg has 4 accepted answers">50%</span></p>
</div>
</div>
<div id="comments-container-81722" class="comments-container">
<span id="81782"></span>
<div id="comment-81782" class="comment">
<div id="post-81782-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks. This is precisely what I needed.</p>
</div>
<div id="comment-81782-info" class="comment-info">
<span class="comment-age">(16 Sep '21, 16:57)</span> <span class="comment-user userinfo">voschix</span>
</div>
</div>
<span id="82007"></span>
<div id="comment-82007" class="comment">
<div id="post-82007-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/277/voschix">@voschix</a>: Good! Then, you could mark this question as answered, by "accepting" the answer (<a href="/questions/34318/how-to-mark-an-answer-as-accepted-and-mark-my-question-as-answered/34319)">https://help.openstreetmap.org/questions/34318/how-to-mark-an-answer-as-accepted-and-mark-my-question-as-answered/34319)</a> in order to avoid other people to check whether it still needs to be answered.</p>
</div>
<div id="comment-82007-info" class="comment-info">
<span class="comment-age">(30 Sep '21, 12:51)</span> <span class="comment-user userinfo">Gåseborg</span>
</div>
</div>
<span id="82009"></span>
<div id="comment-82009" class="comment">
<div id="post-82009-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have marked it as accepted.</p>
</div>
<div id="comment-82009-info" class="comment-info">
<span class="comment-age">(30 Sep '21, 13:26)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-81722" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81722-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="82011"></span>

<div id="answer-container-82011" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82011-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82011-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-82011-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Taking <a href="https://help.openstreetmap.org/users/20300/gaseborg">@Gåseborg</a> answer &amp; shrinking it to save on the typing:</p>
<pre><code>rel[route=bicycle]({{bbox}});
way(r)[highway~&quot;unclassified|tertiary|secondary|primary|trunk|motorway&quot;][!maxspeed];
out geom;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Sep '21, 16:31</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-82011" class="comments-container">
&#10;</div>
<div id="comment-tools-82011" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82011-form-container" class="comment-form-container">
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

