+++
type = "question"
title = "Bus stop on a street light"
description = '''Can anyone help me with how to tag a bus stop that is indicated by a sign fixed on a street light? Eg, here  (That one also has a shelter, but that&#x27;s not always the case.) The problem arises at the note here: https://www.openstreetmap.org/note/1656360 The problem seems to be that iD doesn&#x27;t like hig...'''
date = "2020-09-25T08:52:00Z"
lastmod = "2020-09-26T13:31:00Z"
weight = 76808
keywords = [ "busstops", "streetlamp" ]
aliases = [ "/questions/76808" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Bus stop on a street light](/questions/76808/bus-stop-on-a-street-light)

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
<span id="post-76808-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76808-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-76808-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Can anyone help me with how to tag a bus stop that is indicated by a sign fixed on a street light?</p>
<p>Eg, <a href="https://drive.google.com/file/d/1gwsvbBXIegYfHlIoBHunf0b8zY4aSBup/view?usp=sharing">here</a> (That one also has a shelter, but that's not always the case.)</p>
<p>The problem arises at the note here: <a href="https://www.openstreetmap.org/note/1656360">https://www.openstreetmap.org/note/1656360</a> The problem seems to be that iD doesn't like highway=bus_stop and highway=street_light on the same node.</p>
<p>My solution has been to duplicate the node and tag each separately, but it's not very parsimonious.</p>
<p>Thank you.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-busstops" rel="tag" title="see questions tagged &#39;busstops&#39;">busstops</span> <span class="post-tag tag-link-streetlamp" rel="tag" title="see questions tagged &#39;streetlamp&#39;">streetlamp</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Sep '20, 08:52</strong></p>
<img src="https://secure.gravatar.com/avatar/4f273f48fd8756729fc15f4fcf4aae2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="eteb3&#39;s gravatar image" />
<p><span>eteb3</span><br />
<span class="score" title="295 reputation points">295</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="eteb3 has one accepted answer">6%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Sep '20, 08:57</strong> </span></p>
</div>
</div>
<div id="comments-container-76808" class="comments-container">
&#10;</div>
<div id="comment-tools-76808" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76808-form-container" class="comment-form-container">
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

<span id="76810"></span>

<div id="answer-container-76810" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76810-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76810-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-76810-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="eteb3 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You cannot add the same key to one object twice. Adding <code>highway=street_lamp</code> and <code>highway=bus_stop</code> simply does not work from the data model behind OSM. Technically, you could tag something like <code>highway=street_lamp;bus_stop</code> but such construct adding multiple values to one key is difficult to interpret for data consumers and generally frowned upon.</p>
<p>Using two nodes for the two separat features street lamp and bus stop is the right way to do it.</p>
<p>Please also have a look at the Wiki for <a href="https://wiki.openstreetmap.org/wiki/One_feature,_one_OSM_element">some other aspects</a> in this question.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Sep '20, 10:51</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-76810" class="comments-container">
&#10;</div>
<div id="comment-tools-76810" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76810-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="76812"></span>

<div id="answer-container-76812" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76812-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76812-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-76812-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Two separate nodes is the way to go. If you want to express that some object is attached to another object, you can use the key <a href="https://wiki.openstreetmap.org/wiki/Key:support"><code>support</code></a>.</p>
<p>(Although I find it arguable whether the bus stop <em>sign</em> being supported by a street light means that the bus stop <em>as a whole</em> is supported by a street light.)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Sep '20, 11:17</strong></p>
<img src="https://secure.gravatar.com/avatar/0626be5f46f32fce501353e8a5ec399c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tordanik&#39;s gravatar image" />
<p><span>Tordanik</span><br />
<span class="score" title="11998 reputation points"><span>12.0k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="106 badges"><span class="silver">●</span><span class="badgecount">106</span></span><span title="147 badges"><span class="bronze">●</span><span class="badgecount">147</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tordanik has 58 accepted answers">35%</span></p>
</div>
</div>
<div id="comments-container-76812" class="comments-container">
<span id="76828"></span>
<div id="comment-76828" class="comment">
<div id="post-76828-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Position of the street light and pole features would be a good question.</p>
</div>
<div id="comment-76828-info" class="comment-info">
<span class="comment-age">(26 Sep '20, 08:14)</span> <span class="comment-user userinfo">Kovoschiz</span>
</div>
</div>
<span id="76832"></span>
<div id="comment-76832" class="comment">
<div id="post-76832-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Presumably they can be exactly contiguous?</p>
</div>
<div id="comment-76832-info" class="comment-info">
<span class="comment-age">(26 Sep '20, 13:31)</span> <span class="comment-user userinfo">eteb3</span>
</div>
</div>
</div>
<div id="comment-tools-76812" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76812-form-container" class="comment-form-container">
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

