+++
type = "question"
title = "Underground feature representation"
description = '''I just mapped two superposed features. A large public place (highway=pedestrian; area=yes) and an underlying parking (location=underground) with its ways (highway=service; service=parking_aisle; location=underground).  I am rather disappointed to see the result on the map (mapnik) because the underg...'''
date = "2020-05-13T14:20:00Z"
lastmod = "2020-05-14T14:54:00Z"
weight = 74790
keywords = [ "underground", "parking_aisle", "multi-storey", "mapnik" ]
aliases = [ "/questions/74790" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Underground feature representation](/questions/74790/underground-feature-representation)

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
<span id="post-74790-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74790-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74790-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I just mapped two superposed features. A large public place (highway=pedestrian; area=yes) and an underlying parking (location=underground) with its ways (highway=service; service=parking_aisle; location=underground).</p>
<p>I am rather disappointed to see the result on the map (mapnik) because the underground parking aisles appear on the public place on the surface. I have tried level and layer tags to potentially change their representation without success. Any idea on how to manage this issue or is it the expected result?</p>
<p>Here is the case: <a href="https://www.openstreetmap.org/#map=19/45.39973/-71.89598">https://www.openstreetmap.org/#map=19/45.39973/-71.89598</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-underground" rel="tag" title="see questions tagged &#39;underground&#39;">underground</span> <span class="post-tag tag-link-parking_aisle" rel="tag" title="see questions tagged &#39;parking_aisle&#39;">parking_aisle</span> <span class="post-tag tag-link-multi-storey" rel="tag" title="see questions tagged &#39;multi-storey&#39;">multi-storey</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 May '20, 14:20</strong></p>
<img src="https://secure.gravatar.com/avatar/a504353df13461ace2c733906a99ce16?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jfd553&#39;s gravatar image" />
<p><span>jfd553</span><br />
<span class="score" title="389 reputation points">389</span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jfd553 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 May '20, 14:37</strong> </span></p>
</div>
</div>
<div id="comments-container-74790" class="comments-container">
&#10;</div>
<div id="comment-tools-74790" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74790-form-container" class="comment-form-container">
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

<span id="74792"></span>

<div id="answer-container-74792" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74792-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74792-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-74792-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="jfd553 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There's actually a recently <a href="https://github.com/gravitystorm/openstreetmap-carto/issues/4118">filed issue</a> which relates to part of this question.</p>
<p>However, how to render underground facilities is a more broadly-based question and there is currently no good answer, see <a href="https://www.openstreetmap.org/#map=18/53.40820/-2.97929">for instance</a> passages to access an underground metro station. The CartoCSS styles get more and more complex with additional layers, and most of these underground features are currently edge cases which probably don't justify the major work required to resolve the rendering in a small number of areas. This is especially so as the tagging may evolve as there are more people mapping them.</p>
<p>It is quite likely that for the kind of map output you expect that additional post-processing over-and-above the current architecture of the Carto CSS style which is constrained by needing to stay close to OSM because it is refreshed continually. There are probably cases where underground service roads should be shown as well as those where it would be preferred that they are not.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 May '20, 15:27</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-74792" class="comments-container">
<span id="74793"></span>
<div id="comment-74793" class="comment">
<div id="post-74793-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Well, I then understand why I initially did not find any satisfying answer. Thank.</p>
</div>
<div id="comment-74793-info" class="comment-info">
<span class="comment-age">(13 May '20, 15:37)</span> <span class="comment-user userinfo">jfd553</span>
</div>
</div>
</div>
<div id="comment-tools-74792" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74792-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="74806"></span>

<div id="answer-container-74806" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74806-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74806-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74806-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi jfd553,</p>
<p>Have a look here, <a href="https://www.openstreetmap.org/#map=19/51.92319/4.46459">https://www.openstreetmap.org/#map=19/51.92319/4.46459</a> Otherwise I would use layers or levels the last is more 3D mapping IMHO or enlighthen the object with underground=yes. In case of a park simple covered=yes.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 May '20, 14:54</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
</div>
<div id="comments-container-74806" class="comments-container">
&#10;</div>
<div id="comment-tools-74806" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74806-form-container" class="comment-form-container">
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

