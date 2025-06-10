+++
type = "question"
title = "Openstreetmap sends point instead relation for city district"
description = '''Hi everyone! Openstreetmap sends &quot;node&quot; instead &quot;relation&quot; for Shayxontoxur District (which is in Tashkent, Uzbekistan). For other districts (for example, Chilanzar District) everything works pretty well.  How to solve it? Thanks for your help and time.'''
date = "2019-09-17T09:46:00Z"
lastmod = "2019-09-17T12:03:00Z"
weight = 70817
keywords = [ "nodes", "relations" ]
aliases = [ "/questions/70817" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Openstreetmap sends point instead relation for city district](/questions/70817/openstreetmap-sends-point-instead-relation-for-city-district)

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
<span id="post-70817-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70817-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-70817-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi everyone!</p>
<p>Openstreetmap sends "node" instead "relation" for Shayxontoxur District (which is in Tashkent, Uzbekistan). For other districts (for example, Chilanzar District) everything works pretty well.</p>
<p>How to solve it?</p>
<p>Thanks for your help and time.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Sep '19, 09:46</strong></p>
<img src="https://secure.gravatar.com/avatar/8f363113aa3ef62ca702fd58c4e8d85c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mountain_view&#39;s gravatar image" />
<p><span>mountain_view</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mountain_view has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-70817" class="comments-container">
&#10;</div>
<div id="comment-tools-70817" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70817-form-container" class="comment-form-container">
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

<span id="70819"></span>

<div id="answer-container-70819" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-70819-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70819-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-70819-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="mountain_view has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The issue seems to be that <a href="https://www.openstreetmap.org/relation/2439529#map=13/41.3248/69.2174&amp;layers=D">https://www.openstreetmap.org/relation/2439529#map=13/41.3248/69.2174&amp;layers=D</a></p>
<p>"only" has a name in Cyrillic script and the same for the label node that is linked <a href="https://www.openstreetmap.org/node/3957807636">https://www.openstreetmap.org/node/3957807636</a> in the boundary relation.</p>
<p>The best way to fix the issue is likely to add the <a href="https://www.openstreetmap.org/node/309372663#map=9/41.3180/69.2372">https://www.openstreetmap.org/node/309372663#map=9/41.3180/69.2372</a> node as admin_centre (adding different language versions of the name as needed) and do away with the label node.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Sep '19, 12:03</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-70819" class="comments-container">
&#10;</div>
<div id="comment-tools-70819" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70819-form-container" class="comment-form-container">
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

