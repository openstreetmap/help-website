+++
type = "question"
title = "Whats wrong with this roundabout ?"
description = '''Im adding man_made=embankments, http://www.openstreetmap.org/#map=18/52.47369/4.77315 The roads (ways) are nicely figured in OSM,s slippy map, but the roundabout tagged highway=trunk is turned into a black line when added man_made=embankment.  Whats the reason for this exception ? Or just being impa...'''
date = "2014-09-02T16:11:00Z"
lastmod = "2014-09-02T22:09:00Z"
weight = 36514
keywords = [ "roundabout", "embankment", "trunk" ]
aliases = [ "/questions/36514" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Whats wrong with this roundabout ?](/questions/36514/whats-wrong-with-this-roundabout)

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
<span id="post-36514-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-36514-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-36514-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Im adding man_made=embankments, <a href="http://www.openstreetmap.org/#map=18/52.47369/4.77315">http://www.openstreetmap.org/#map=18/52.47369/4.77315</a> The roads (ways) are nicely figured in OSM,s slippy map, but the roundabout tagged highway=trunk is turned into a black line when added man_made=embankment. Whats the reason for this exception ? Or just being impatient ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-roundabout" rel="tag" title="see questions tagged &#39;roundabout&#39;">roundabout</span> <span class="post-tag tag-link-embankment" rel="tag" title="see questions tagged &#39;embankment&#39;">embankment</span> <span class="post-tag tag-link-trunk" rel="tag" title="see questions tagged &#39;trunk&#39;">trunk</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Sep '14, 16:11</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
</div>
<div id="comments-container-36514" class="comments-container">
&#10;</div>
<div id="comment-tools-36514" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-36514-form-container" class="comment-form-container">
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

<span id="36516"></span>

<div id="answer-container-36516" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-36516-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-36516-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-36516-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Hendrikklaas has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>When I check right now the data, the tag "man_made=embankment" is <a href="http://www.openstreetmap.org/way/6606647/history">removed</a>. But I would guess that could be a rendering issue. Combining these two attributs is a bit dangerous for a roundabout since both of them are depending on the direction of the way (the transport flow for the roundabout and the high/low side for the embankment). What I could advice is :</p>
<p>- read the wiki about <a href="http://wiki.openstreetmap.org/wiki/Tag:man%20made=embankment?uselang=en">embankment</a>. It says that "embankment=yes" is much more popular in OSM (something I verified with taginfo). The direction of the way is important : cf "Add man_made=embankment to a way with the left-hand side of the way being the high side and the right-hand side being the low side"<br />
- It also says that you can micro-map the embankment by tracing separate ways (detached from the highway)<br />
- in general, you don't need a "oneway=yes" on "junction=roundabout". This is probably the only case in OSM where oneway is clearly implied (it's more controversial for motorways).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Sep '14, 16:42</strong></p>
<img src="https://secure.gravatar.com/avatar/0e92f2d89853fd4e04c4b40a921e519b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pieren&#39;s gravatar image" />
<p><span>Pieren</span><br />
<span class="score" title="9847 reputation points"><span>9.8k</span></span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="157 badges"><span class="bronze">●</span><span class="badgecount">157</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pieren has 34 accepted answers">15%</span> </br></br></p>
</div>
</div>
<div id="comments-container-36516" class="comments-container">
<span id="36528"></span>
<div id="comment-36528" class="comment">
<div id="post-36528-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi Pieren thanks, I removed it, because the effect surprised me. I’ll have to survey embankments too and stop adding man_made=embankment to an existing way. The easiest solution.</p>
</div>
<div id="comment-36528-info" class="comment-info">
<span class="comment-age">(02 Sep '14, 22:09)</span> <span class="comment-user userinfo">Hendrikklaas</span>
</div>
</div>
</div>
<div id="comment-tools-36516" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-36516-form-container" class="comment-form-container">
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

