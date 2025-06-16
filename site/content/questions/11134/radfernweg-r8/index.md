+++
type = "question"
title = "Radfernweg R8"
description = '''hallo, ich habe begonnen im Bereich Vockenhausen die aktualisierte Route des R8 einzupflegen. Nach den ersten Änderungen (Änderungssatz 10947005) steht mir aber der R8 zum anbinden an den aktualisierten Weg nicht mehr zur Verfügung. Irgend etwas habe ich falsch gemacht und bräuchte Unterstützung. Mf...'''
date = "2012-03-12T12:57:00Z"
lastmod = "2012-03-12T16:52:00Z"
weight = 11134
keywords = [ "radfernweg" ]
aliases = [ "/questions/11134" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Radfernweg R8](/questions/11134/radfernweg-r8)

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
<span id="post-11134-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11134-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-11134-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>hallo, ich habe begonnen im Bereich Vockenhausen die aktualisierte Route des R8 einzupflegen. Nach den ersten Änderungen (Änderungssatz 10947005) steht mir aber der R8 zum anbinden an den aktualisierten Weg nicht mehr zur Verfügung. Irgend etwas habe ich falsch gemacht und bräuchte Unterstützung. MfG Klaus_C</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-radfernweg" rel="tag" title="see questions tagged &#39;radfernweg&#39;">radfernweg</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Mar '12, 12:57</strong></p>
<img src="https://secure.gravatar.com/avatar/47496c5c895de03b7675cf7f852c1eb7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Klaus_C&#39;s gravatar image" />
<p><span>Klaus_C</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Klaus_C has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-11134" class="comments-container">
<span id="11138"></span>
<div id="comment-11138" class="comment">
<div id="post-11138-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Roughly:</p>
<p>Hi, I started in Vockenhausen uploading the updated route of the R8. After the first change (change set 10,947,005) available to me but the R8 to connect to the upgraded road is no longer available. Something I've done wrong and needed support. Best regards Klaus_C</p>
</div>
<div id="comment-11138-info" class="comment-info">
<span class="comment-age">(12 Mar '12, 16:47)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-11134" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11134-form-container" class="comment-form-container">
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

<span id="11139"></span>

<div id="answer-container-11139" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-11139-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11139-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-11139-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi - <a href="https://www.openstreetmap.org/browse/changeset/10947005">this</a> is the changeset. It adds a new footpath but somehow the R8 relation got deleted. I've reverted the original changeset and manually made the other change again.</p>
<p>Relation <a href="https://www.openstreetmap.org/browse/relation/18379">18379</a> is back, but it's too big to get through the "browse" interface. If you do something like:</p>
<p>wget <a href="http://api.openstreetmap.org/api/0.6/relation/18379">http://api.openstreetmap.org/api/0.6/relation/18379</a></p>
<p>it will retrieve OK. "wget", if you're not familiar with it, is a command-line program to get stuff from the Internet.</p>
<p>The footway looks like <a href="https://www.openstreetmap.org/browse/way/79024281/history">this</a> now, which should be back how you left it.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Mar '12, 16:52</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Mar '12, 17:23</strong> </span></p>
</div>
</div>
<div id="comments-container-11139" class="comments-container">
&#10;</div>
<div id="comment-tools-11139" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11139-form-container" class="comment-form-container">
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

