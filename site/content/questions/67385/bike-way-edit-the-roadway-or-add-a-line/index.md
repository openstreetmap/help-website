+++
type = "question"
title = "Bike Way - edit the roadway or add a line?"
description = '''Newbie here. I am trying to update the bikeways near me. I am an ArcGIS user, so Potlatch2 is new to me but I get the jist of it. I am still kinda confused on how to go about adding the bikeways. If I want to update a roadway to show a recent installation of a bike lane, do I draw a new line over it...'''
date = "2018-12-29T00:09:00Z"
lastmod = "2018-12-29T06:59:00Z"
weight = 67385
keywords = [ "opencyclemap", "bike", "bicycle" ]
aliases = [ "/questions/67385" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Bike Way - edit the roadway or add a line?](/questions/67385/bike-way-edit-the-roadway-or-add-a-line)

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
<span id="post-67385-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67385-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-67385-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Newbie here. I am trying to update the bikeways near me. I am an ArcGIS user, so Potlatch2 is new to me but I get the jist of it.</p>
<p>I am still kinda confused on how to go about adding the bikeways. If I want to update a roadway to show a recent installation of a bike lane, do I draw a new line over it and assign cycle path tag? Or do I click the existing roadway, go to the bicycle tab and edit the necessary pulldowns, and if necessary assign a bicycle local cycle route number? What is the best approach?</p>
<p>Thank you all for your input!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-opencyclemap" rel="tag" title="see questions tagged &#39;opencyclemap&#39;">opencyclemap</span> <span class="post-tag tag-link-bike" rel="tag" title="see questions tagged &#39;bike&#39;">bike</span> <span class="post-tag tag-link-bicycle" rel="tag" title="see questions tagged &#39;bicycle&#39;">bicycle</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Dec '18, 00:09</strong></p>
<img src="https://secure.gravatar.com/avatar/018fa3f246ef5b39b40bcdb64d88fb18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mh0205&#39;s gravatar image" />
<p><span>mh0205</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mh0205 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-67385" class="comments-container">
&#10;</div>
<div id="comment-tools-67385" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67385-form-container" class="comment-form-container">
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

<span id="67386"></span>

<div id="answer-container-67386" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-67386-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67386-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-67386-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I don't think either is wrong, but if the "bikeway" is an integral part of the road, with only a line of paint, or a minimal barrier separating the lane from motor vehicle traffic then I'd suggest that adding tags to the existing roadway would more accurately reflect reality, and if the "bikeway" is separated from the roadway then adding a new "way" (what we call "lines" here) would be preferable. If adding tags to the roadway take a look at <a href="https://wiki.openstreetmap.org/wiki/Key:cycleway">OSM's Wiki article on cycleways</a>. When you call it a bike lane, it sounds like you are looking for the <code>cycleway=lane</code> tag added to the existing roadway.</p>
<p>If adding a new way be sure it connects with existing ones, to allow accurate routing.</p>
<p>OSM does have extremely flexible data types, and there's often more than one way to do things.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Dec '18, 03:13</strong></p>
<img src="https://secure.gravatar.com/avatar/f88a467aa884aeb760041004f62448ee?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="keithonearth&#39;s gravatar image" />
<p><span>keithonearth</span><br />
<span class="score" title="2939 reputation points"><span>2.9k</span></span><span title="56 badges"><span class="badge1">●</span><span class="badgecount">56</span></span><span title="76 badges"><span class="silver">●</span><span class="badgecount">76</span></span><span title="108 badges"><span class="bronze">●</span><span class="badgecount">108</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="keithonearth has 3 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-67386" class="comments-container">
<span id="67387"></span>
<div id="comment-67387" class="comment">
<div id="post-67387-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>There is also a <a href="https://wiki.openstreetmap.org/wiki/Bicycle">wiki page on bicycle infrastructure</a> with a lot of different situations with pictures and the preferred tagging methods.</p>
<p>To the OP: Please note that we never map cycleways by "drawing a new line over" the existing OSM way. we either add tags to the way or draw a line parallel to it.</p>
</div>
<div id="comment-67387-info" class="comment-info">
<span class="comment-age">(29 Dec '18, 06:59)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
</div>
<div id="comment-tools-67386" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67386-form-container" class="comment-form-container">
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

