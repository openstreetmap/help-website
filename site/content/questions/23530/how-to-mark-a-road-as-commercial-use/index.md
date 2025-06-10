+++
type = "question"
title = "How to mark a road as commercial use?"
description = '''Hi the Palisades Interstate Parkway that runs through New York and New Jersey does not allow commercial vehicles. So how do I add that to the system?'''
date = "2013-06-19T20:06:00Z"
lastmod = "2013-06-19T21:49:00Z"
weight = 23530
keywords = [ "trailers", "restrictions", "commercial", "tractor", "trucks" ]
aliases = [ "/questions/23530" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to mark a road as commercial use?](/questions/23530/how-to-mark-a-road-as-commercial-use)

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
<span id="post-23530-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23530-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-23530-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi the Palisades Interstate Parkway that runs through New York and New Jersey does not allow commercial vehicles. So how do I add that to the system?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-trailers" rel="tag" title="see questions tagged &#39;trailers&#39;">trailers</span> <span class="post-tag tag-link-restrictions" rel="tag" title="see questions tagged &#39;restrictions&#39;">restrictions</span> <span class="post-tag tag-link-commercial" rel="tag" title="see questions tagged &#39;commercial&#39;">commercial</span> <span class="post-tag tag-link-tractor" rel="tag" title="see questions tagged &#39;tractor&#39;">tractor</span> <span class="post-tag tag-link-trucks" rel="tag" title="see questions tagged &#39;trucks&#39;">trucks</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Jun '13, 20:06</strong></p>
<img src="https://secure.gravatar.com/avatar/aea7596681eea0b3d53293aedfee44a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tomljr&#39;s gravatar image" />
<p><span>tomljr</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tomljr has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-23530" class="comments-container">
<span id="23531"></span>
<div id="comment-23531" class="comment">
<div id="post-23531-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>what kind of vehicle is commercial, rather unclear IMHO ? A bus or hgv, delivery service or just a cab, which vehicles are excluded ? Otherwise just use the value no.</p>
</div>
<div id="comment-23531-info" class="comment-info">
<span class="comment-age">(19 Jun '13, 20:26)</span> <span class="comment-user userinfo">Hendrikklaas</span>
</div>
</div>
</div>
<div id="comment-tools-23530" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23530-form-container" class="comment-form-container">
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

<span id="23532"></span>

<div id="answer-container-23532" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-23532-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23532-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-23532-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Bearing in mind the comment by Hendrikklaas, but assuming you are referring to trucks, <strong>the standard tagging is <code>hgv=no</code></strong> (hgv is British legal english for Heavy Goods Vehicle).</p>
<p>If other types of vehicles are also included in this restriction add each of these in the same way. The most widely used examples are documented <a href="http://wiki.openstreetmap.org/wiki/Key:access#Land-based_transportation">here</a> on the wiki. <a href="http://taginfo.openstreetmap.org/keys/?key=access">taginfo</a> for the key <code>access</code> may also provide inspiration, as many values are also used as keys with values of <code>no|yes|permissive</code>.</p>
<p>I would expect <code>hgv=no</code> to generate the right behaviour by most routers.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Jun '13, 21:49</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-23532" class="comments-container">
&#10;</div>
<div id="comment-tools-23532" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23532-form-container" class="comment-form-container">
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

