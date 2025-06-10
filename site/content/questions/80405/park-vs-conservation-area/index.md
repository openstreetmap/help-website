+++
type = "question"
title = "Park vs conservation area"
description = '''We have a private, no-access conservation area showing as a Park on the map and tagged as private in the description. Having it attributed as a park is leading to trespassing/damage issues. Should I change it to an &quot;Area&quot; leaving the name alone (as it is referred to elsewhere on the web) or remove i...'''
date = "2021-06-03T17:53:00Z"
lastmod = "2021-06-04T03:40:00Z"
weight = 80405
keywords = [ "tresspass", "conservation", "park" ]
aliases = [ "/questions/80405" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Park vs conservation area](/questions/80405/park-vs-conservation-area)

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
<span id="post-80405-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80405-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-80405-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>We have a private, no-access conservation area showing as a Park on the map and tagged as private in the description. Having it attributed as a park is leading to trespassing/damage issues. Should I change it to an "Area" leaving the name alone (as it is referred to elsewhere on the web) or remove it? I think the main issue is people automatically see a green area as public access. Thanks,</p>
<p>Tycho</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tresspass" rel="tag" title="see questions tagged &#39;tresspass&#39;">tresspass</span> <span class="post-tag tag-link-conservation" rel="tag" title="see questions tagged &#39;conservation&#39;">conservation</span> <span class="post-tag tag-link-park" rel="tag" title="see questions tagged &#39;park&#39;">park</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Jun '21, 17:53</strong></p>
<img src="https://secure.gravatar.com/avatar/9f13529b344e02cefc5d99d25eda4b29?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Wasco%20County%20GIS&#39;s gravatar image" />
<p><span>Wasco County...</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Wasco County GIS has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-80405" class="comments-container">
<span id="80415"></span>
<div id="comment-80415" class="comment">
<div id="post-80415-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>(Same question <a href="https://forum.openstreetmap.org/viewtopic.php?pid=831427#p831427)">https://forum.openstreetmap.org/viewtopic.php?pid=831427#p831427)</a></p>
</div>
<div id="comment-80415-info" class="comment-info">
<span class="comment-age">(04 Jun '21, 03:40)</span> <span class="comment-user userinfo">Kovoschiz</span>
</div>
</div>
</div>
<div id="comment-tools-80405" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80405-form-container" class="comment-form-container">
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

<span id="80412"></span>

<div id="answer-container-80412" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-80412-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80412-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-80412-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Wasco County GIS has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The <code>area=yes</code>/<code>no</code> tags are supplementary tags for ambiguous situations, and not meant to be used as main tags.</p>
<p>For tagging of protected areas the wiki article for their <a href="https://wiki.openstreetmap.org/wiki/Tag:boundary%3Dprotected_area">boundaries</a> and the rather opaque <a href="https://wiki.openstreetmap.org/wiki/Key:protect_class">protect class</a> tags are probably a good starting point.</p>
<p><a href="https://wiki.openstreetmap.org/wiki/Tag:leisure%3Dnature_reserve"><code>leisure=nature_reserve</code></a> may be appropriate if there is some degree of access allowed by the public.</p>
<p>Mistagging specifically so that the area doesn't render as green is <a href="https://wiki.openstreetmap.org/wiki/Tagging_for_the_renderer">generally discouraged</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Jun '21, 02:50</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Jun '21, 02:51</strong> </span></p>
</div>
</div>
<div id="comments-container-80412" class="comments-container">
&#10;</div>
<div id="comment-tools-80412" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80412-form-container" class="comment-form-container">
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

