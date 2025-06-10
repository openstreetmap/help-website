+++
type = "question"
title = "How to tag christmas trees plantations?"
description = '''Hi,  Quite off season but well. I&#x27;m tagging a lot of christmas trees plantation around my place. I always used:  1) landuse=farmland + produce=christmas_trees (+ leaf_type=needleleaved + leaf_cycle=evergreen + landcover=trees). See http://overpass-turbo.eu/s/yYt (you can run it at the world scale sa...'''
date = "2018-05-21T13:47:00Z"
lastmod = "2018-05-30T20:59:00Z"
weight = 63597
keywords = [ "trees", "tagging" ]
aliases = [ "/questions/63597" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How to tag christmas trees plantations?](/questions/63597/how-to-tag-christmas-trees-plantations)

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
<span id="post-63597-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63597-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-63597-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>Quite off season but well. I'm tagging a lot of christmas trees plantation around my place. I always used:</p>
<p>1) <code>landuse=farmland + produce=christmas_trees</code> (+ leaf_type=needleleaved + leaf_cycle=evergreen + landcover=trees). See <a href="http://overpass-turbo.eu/s/yYt">http://overpass-turbo.eu/s/yYt</a> (you can run it at the world scale safely)</p>
<p>The rational is that in my country christmas trees must be grown in a farmland: legally you cannot cut a forest to grow christmas trees instead. In addition, they will be always cut before getting more than 2 m height, and they are grown in places that can be far from forested areas. So I exclude the tagging scheme <code>landuse=forest+produce=christmas_trees</code></p>
<p>But recently, I came across:</p>
<p>2) <code>landuse=plant_nursery + trees=christmas_trees</code>. See <a href="http://overpass-turbo.eu/s/yYs">http://overpass-turbo.eu/s/yYs</a></p>
<p>What do you think?</p>
<p>Merry Christmas,</p>
<p>juminet</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-trees" rel="tag" title="see questions tagged &#39;trees&#39;">trees</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 May '18, 13:47</strong></p>
<img src="https://secure.gravatar.com/avatar/7841360034567cd045edd29245f4d5e4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="juminet&#39;s gravatar image" />
<p><span>juminet</span><br />
<span class="score" title="61 reputation points">61</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="juminet has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-63597" class="comments-container">
<span id="63892"></span>
<div id="comment-63892" class="comment">
<div id="post-63892-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Similar <a href="https://help.openstreetmap.org/questions/50624/are-knee-high-trees-a-forest">https://help.openstreetmap.org/questions/50624/are-knee-high-trees-a-forest</a></p>
</div>
<div id="comment-63892-info" class="comment-info">
<span class="comment-age">(30 May '18, 20:59)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
</div>
<div id="comment-tools-63597" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63597-form-container" class="comment-form-container">
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

<span id="63600"></span>

<div id="answer-container-63600" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-63600-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63600-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-63600-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="juminet has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I would not use landuse=farmland and rely on the produce tag. This in general violates the principle of least surprise.</p>
<p>I think that landuse=plant_nursery is the most widely used tag for this purpose. See the <a href="https://wiki.openstreetmap.org/wiki/Tag%3Alanduse%3Dplant_nursery#Christmas_tree_plantation.">wiki</a>.</p>
<p>Note that christmas trees may be one of several species of conifer.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 May '18, 17:26</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 May '18, 17:28</strong> </span></p>
</div>
</div>
<div id="comments-container-63600" class="comments-container">
<span id="63623"></span>
<div id="comment-63623" class="comment">
<div id="post-63623-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Indeed, I think that's the most adequate tagging scheme. I'll start replacing "my" christmas trees fields.</p>
</div>
<div id="comment-63623-info" class="comment-info">
<span class="comment-age">(22 May '18, 19:47)</span> <span class="comment-user userinfo">juminet</span>
</div>
</div>
</div>
<div id="comment-tools-63600" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63600-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="63598"></span>

<div id="answer-container-63598" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-63598-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63598-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-63598-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I think all of those tagging methods are correct, including sectioning off a portion of farmland as a forested area of the entereprise if preferred. Depending on the individual situation any one of those methods would be correct for a particular case. Merry Xmas</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 May '18, 14:31</strong></p>
<img src="https://secure.gravatar.com/avatar/e5674dd96938593e0af5130dfffe0f90?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nevw&#39;s gravatar image" />
<p><span>nevw</span><br />
<span class="score" title="9843 reputation points"><span>9.8k</span></span><span title="26 badges"><span class="badge1">●</span><span class="badgecount">26</span></span><span title="90 badges"><span class="silver">●</span><span class="badgecount">90</span></span><span title="178 badges"><span class="bronze">●</span><span class="badgecount">178</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nevw has 32 accepted answers">9%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 May '18, 14:32</strong> </span></p>
</div>
</div>
<div id="comments-container-63598" class="comments-container">
&#10;</div>
<div id="comment-tools-63598" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63598-form-container" class="comment-form-container">
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

