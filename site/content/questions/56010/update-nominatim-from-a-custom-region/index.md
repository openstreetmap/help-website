+++
type = "question"
title = "Update Nominatim from a custom region"
description = '''Hi to all! I succeeded install Nomiatim with a custom extract region that is not exist en geofabrik, then I buit it from Bbbike. Now I want to update the database, but all instructions refers to a diff from geofabrik. How I can update de database with a fresh data of the custom region, an not from a...'''
date = "2017-05-03T13:32:00Z"
lastmod = "2017-05-03T14:23:00Z"
weight = 56010
keywords = [ "region", "nominatim", "update", "custom" ]
aliases = [ "/questions/56010" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Update Nominatim from a custom region](/questions/56010/update-nominatim-from-a-custom-region)

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
<span id="post-56010-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56010-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-56010-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi to all!</p>
<p>I succeeded install Nomiatim with a custom extract region that is not exist en geofabrik, then I buit it from Bbbike.</p>
<p>Now I want to update the database, but all instructions refers to a diff from geofabrik.</p>
<p>How I can update de database with a fresh data of the custom region, an not from a whole country ?</p>
<p>Thank you</p>
<p>Best regards, Carlos</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-region" rel="tag" title="see questions tagged &#39;region&#39;">region</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-update" rel="tag" title="see questions tagged &#39;update&#39;">update</span> <span class="post-tag tag-link-custom" rel="tag" title="see questions tagged &#39;custom&#39;">custom</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 May '17, 13:32</strong></p>
<img src="https://secure.gravatar.com/avatar/46f203350f96ab645a0a04ed99cfa0d2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Carlos%20Brys&#39;s gravatar image" />
<p><span>Carlos Brys</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Carlos Brys has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 May '17, 13:34</strong> </span></p>
</div>
</div>
<div id="comments-container-56010" class="comments-container">
&#10;</div>
<div id="comment-tools-56010" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56010-form-container" class="comment-form-container">
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

<span id="56017"></span>

<div id="answer-container-56017" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56017-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56017-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-56017-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You first have to download an updated extract for the same region from bbbike. Then you have two options:</p>
<ol>
<li>do a full new import. If you are concerned about the interruption of service, you can import into a new database and then drop the old database and rename the new one once you are done.</li>
<li>use "osmium" or "osmosis" to compute the difference between the new file and the old file (which you have to keep lying around for this purpose). Then load the resulting update file into your live database (using <code>php utils/update.php --import-diff</code>).</li>
</ol>
<p>Option 2 is only suitable if you are doing this frequently and the number of changes is therefore small; once the number of changed objects is in the 5% to 10% range (i.e. if you do an update and 5% of all things are new or changed) then option 1 is probably more efficient.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 May '17, 14:23</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-56017" class="comments-container">
&#10;</div>
<div id="comment-tools-56017" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56017-form-container" class="comment-form-container">
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

