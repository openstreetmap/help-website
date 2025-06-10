+++
type = "question"
title = "Simple houses mapped as multipolygons... What to do?"
description = '''Hi, some houses in my neighborhood are mapped as multipolygons while it&#x27;s only simple shapes that could be represented as only one surface... Do you have any idea of what to do? Thanks in advance for your help! :) Here is an example: '''
date = "2017-02-04T09:40:00Z"
lastmod = "2017-02-04T10:39:00Z"
weight = 54451
keywords = [ "house", "multipolygon", "houses" ]
aliases = [ "/questions/54451" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Simple houses mapped as multipolygons... What to do?](/questions/54451/simple-houses-mapped-as-multipolygons-what-to-do)

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
<span id="post-54451-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54451-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-54451-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, some houses in my neighborhood are mapped as multipolygons while it's only simple shapes that could be represented as only one surface...</p>
<p>Do you have any idea of what to do? Thanks in advance for your help! :)</p>
<p>Here is an example:</p>
<p><img src="http://help.openstreetmap.org/upfiles/Capture_du_2017-02-04_10-36-29.png" alt="house mapped as multipolygon" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-house" rel="tag" title="see questions tagged &#39;house&#39;">house</span> <span class="post-tag tag-link-multipolygon" rel="tag" title="see questions tagged &#39;multipolygon&#39;">multipolygon</span> <span class="post-tag tag-link-houses" rel="tag" title="see questions tagged &#39;houses&#39;">houses</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Feb '17, 09:40</strong></p>
<img src="https://secure.gravatar.com/avatar/a6f6dfca2347a0e7effd848ba6af84c0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="thomaskuntzz&#39;s gravatar image" />
<p><span>thomaskuntzz</span><br />
<span class="score" title="71 reputation points">71</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="thomaskuntzz has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-54451" class="comments-container">
&#10;</div>
<div id="comment-tools-54451" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54451-form-container" class="comment-form-container">
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

<span id="54452"></span>

<div id="answer-container-54452" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-54452-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54452-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-54452-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>These houses are not mapped as multipolygons in the OSM sense (i.e. they don't have a relation combining the parts) - or at least they didn't until you added one! I would not recommend doing that, since multipolygon relations with touching outer rings are considered invalid.</p>
<p>Instead, use the JOSM editor's "join overlapping areas" function to combine the various rings into one.</p>
<p>It appears that the data you are looking at is the result of an import of Cadastre data in 2010 (<a href="https://www.openstreetmap.org/changeset/5056952)">https://www.openstreetmap.org/changeset/5056952)</a> that was improperly reviewed and hence these issues were not detected ahead of the import. If you should find that there are too many problems to handle manually, there's also the option of deleting the faulty import altogether.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Feb '17, 10:07</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-54452" class="comments-container">
<span id="54454"></span>
<div id="comment-54454" class="comment">
<div id="post-54454-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, the house was made up of several areas so I merged them together...</p>
<p>There is a large number of houses that are the result of this Cadastre data import (by the way, your link seem to be broken) and that are mapped the same way as this one, that is as multiple surfaces instead of one.</p>
<p>So I'd like to clean up all this a bit and I don't know what to do...</p>
</div>
<div id="comment-54454-info" class="comment-info">
<span class="comment-age">(04 Feb '17, 10:36)</span> <span class="comment-user userinfo">thomaskuntzz</span>
</div>
</div>
<span id="54455"></span>
<div id="comment-54455" class="comment">
<div id="post-54455-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Remove the ) after the link for it to work. Install the JOSM editor and learn how to use it; while the ID editor you are using is fine for everyday mapping activities, JOSM has a broader set of tools for more complicated operations like cleaning up a botched import.</p>
</div>
<div id="comment-54455-info" class="comment-info">
<span class="comment-age">(04 Feb '17, 10:39)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-54452" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54452-form-container" class="comment-form-container">
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

