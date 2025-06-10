+++
type = "question"
title = "nominatim.openstreetmap.org/reverse returns wrong address in special case"
description = '''example: http://nominatim.openstreetmap.org/reverse?format=xml&amp;amp;lat=45.3283699&amp;amp;lon=40.71868&amp;amp;accept-language=en returns &quot;Maykop, .... Adygea, South federal district, Russian Federation&quot; but http://nominatim.openstreetmap.org/ in bounds 40.34,45.56,41.1,45.13 shows Gulkevichi (Гулькевичи), ...'''
date = "2015-05-29T10:33:00Z"
lastmod = "2015-06-01T13:36:00Z"
weight = 43300
keywords = [ "wrong", "reverse" ]
aliases = [ "/questions/43300" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [nominatim.openstreetmap.org/reverse returns wrong address in special case](/questions/43300/nominatimopenstreetmaporgreverse-returns-wrong-address-in-special-case)

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
<span id="post-43300-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43300-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-43300-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>example: <a href="http://nominatim.openstreetmap.org/reverse?format=xml&amp;lat=45.3283699&amp;lon=40.71868&amp;accept-language=en">http://nominatim.openstreetmap.org/reverse?format=xml&amp;lat=45.3283699&amp;lon=40.71868&amp;accept-language=en</a> returns "Maykop, .... Adygea, South federal district, Russian Federation"</p>
<p>but <a href="http://nominatim.openstreetmap.org/">http://nominatim.openstreetmap.org/</a> in bounds 40.34,45.56,41.1,45.13 shows Gulkevichi (Гулькевичи), which belongs not to Adygea, but to Krasnodar Krai area</p>
<p>it seems that problem is actual to region S45.31, W40.35, N45.34, E40.74</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-wrong" rel="tag" title="see questions tagged &#39;wrong&#39;">wrong</span> <span class="post-tag tag-link-reverse" rel="tag" title="see questions tagged &#39;reverse&#39;">reverse</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 May '15, 10:33</strong></p>
<img src="https://secure.gravatar.com/avatar/a7c1929d0f03b2f22417d6b1e87397ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dmitrijk&#39;s gravatar image" />
<p><span>dmitrijk</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dmitrijk has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-43300" class="comments-container">
<span id="43314"></span>
<div id="comment-43314" class="comment">
<div id="post-43314-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Your second example doesn't seem to be complete. What are you searching for within those bounds?</p>
<p>It might help if you describe what you're trying to do and what you would like to happen.</p>
</div>
<div id="comment-43314-info" class="comment-info">
<span class="comment-age">(29 May '15, 16:31)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
</div>
<div id="comment-tools-43300" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43300-form-container" class="comment-form-container">
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

<span id="43350"></span>

<div id="answer-container-43350" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43350-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43350-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-43350-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>i use second example only to show that first example is not valid. Gulkevichi is situated near N45.32, E40.71: <a href="http://nominatim.openstreetmap.org/search.php?q=%D0%93%D1%83%D0%BB%D1%8C%D0%BA%D0%B5%D0%B2%D0%B8%D1%87%D0%B8&amp;viewbox=40%2C44.66%2C40.21%2C44.55">http://nominatim.openstreetmap.org/search.php?q=%D0%93%D1%83%D0%BB%D1%8C%D0%BA%D0%B5%D0%B2%D0%B8%D1%87%D0%B8&amp;viewbox=40%2C44.66%2C40.21%2C44.55</a></p>
<p>The Maykop is situated to South - N44.6 40.1, Here: <a href="http://nominatim.openstreetmap.org/search.php?q=%D0%BC%D0%B0%D0%B9%D0%BA%D0%BE%D0%BF&amp;viewbox=40.64%2C45.39%2C40.75%2C45.33">http://nominatim.openstreetmap.org/search.php?q=%D0%BC%D0%B0%D0%B9%D0%BA%D0%BE%D0%BF&amp;viewbox=40.64%2C45.39%2C40.75%2C45.33</a></p>
<p>but reverse query to N45.32, E40.71 returns Maykop instead of Gulkevichi. It is an error</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Jun '15, 13:36</strong></p>
<img src="https://secure.gravatar.com/avatar/a7c1929d0f03b2f22417d6b1e87397ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dmitrijk&#39;s gravatar image" />
<p><span>dmitrijk</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dmitrijk has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-43350" class="comments-container">
&#10;</div>
<div id="comment-tools-43350" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43350-form-container" class="comment-form-container">
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

