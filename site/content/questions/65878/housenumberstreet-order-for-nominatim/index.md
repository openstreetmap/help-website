+++
type = "question"
title = "Housenumber/Street order for Nominatim?"
description = '''House numbers are used after the street name in Norway. Then why will that order often fail in providing the correct location from Nominatim, while the reverse order (house number before street) will succeed (in Norway)? Is there perhaps a wrong or missing parameter for Norway in Nominatim? Example:...'''
date = "2018-09-13T08:48:00Z"
lastmod = "2018-09-13T15:05:00Z"
weight = 65878
keywords = [ "nominatim" ]
aliases = [ "/questions/65878" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Housenumber/Street order for Nominatim?](/questions/65878/housenumberstreet-order-for-nominatim)

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
<span id="post-65878-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65878-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-65878-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>House numbers are used <em>after</em> the street name in Norway. Then why will that order often fail in providing the correct location from Nominatim, while the reverse order (house number before street) will succeed (in Norway)?</p>
<p>Is there perhaps a wrong or missing parameter for Norway in Nominatim?</p>
<p>Example:</p>
<ul>
<li>Works: "1, Motzfeldtsgate, Oslo" - <a href="https://nominatim.openstreetmap.org/search.php?q=1%2C+Motzfeldtsgate%2C+Oslo">https://nominatim.openstreetmap.org/search.php?q=1%2C+Motzfeldtsgate%2C+Oslo</a></li>
<li>Fails: "Motzfeldtsgate 1, Oslo" -<br />
<a href="https://nominatim.openstreetmap.org/search.php?q=Motzfeldtsgate+1%2C+Oslo">https://nominatim.openstreetmap.org/search.php?q=Motzfeldtsgate+1%2C+Oslo</a></li>
</ul>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Sep '18, 08:48</strong></p>
<img src="https://secure.gravatar.com/avatar/5f7aab1c5c071949b643713d26f4ee76?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NKA&#39;s gravatar image" />
<p><span>NKA</span><br />
<span class="score" title="126 reputation points">126</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NKA has no accepted answers">0%</span> </br></p>
</div>
</div>
<div id="comments-container-65878" class="comments-container">
&#10;</div>
<div id="comment-tools-65878" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65878-form-container" class="comment-form-container">
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

<span id="65884"></span>

<div id="answer-container-65884" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-65884-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65884-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-65884-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Nominatim supports both equally, it has no logic based on country here. It's actually a side-effect on how addresses are returned, again without logic based on country (<a href="https://github.com/openstreetmap/Nominatim/issues/213).">https://github.com/openstreetmap/Nominatim/issues/213).</a> The returned address is "1, Motzfeldts gate, Arctanderbyen, Grønland, Gamle Oslo, Oslo, 0187, Norway" and "Motzfeldtsgate 1" gets an ordering penalty score for not having the house number in first position.</p>
<p><a href="https://nominatim.openstreetmap.org/search.php?q=Motzfeldtsgate+1%2C+Oslo&amp;debug=1">https://nominatim.openstreetmap.org/search.php?q=Motzfeldtsgate+1%2C+Oslo&amp;debug=1</a> is very detailed, check <code>foundorder</code> near the botton of the page.</p>
<p>It's a good example where that doesn't give the intended result. Can you add it to <a href="https://github.com/openstreetmap/Nominatim/issues">https://github.com/openstreetmap/Nominatim/issues</a> ?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Sep '18, 15:05</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-65884" class="comments-container">
&#10;</div>
<div id="comment-tools-65884" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65884-form-container" class="comment-form-container">
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

