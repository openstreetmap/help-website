+++
type = "question"
title = "Nominatim - how to apply weekly OSM changesets?"
description = '''With Nominatim, how should I apply weekly changesets? Should I use any Nominatim command or osmosis command? Thanks!'''
date = "2013-05-06T05:02:00Z"
lastmod = "2013-05-07T13:06:00Z"
weight = 22124
keywords = [ "changesets", "weekly" ]
aliases = [ "/questions/22124" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Nominatim - how to apply weekly OSM changesets?](/questions/22124/nominatim-how-to-apply-weekly-osm-changesets)

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
<span id="post-22124-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22124-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-22124-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>With Nominatim, how should I apply weekly changesets?</p>
<p>Should I use any Nominatim command or osmosis command?</p>
<p>Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-changesets" rel="tag" title="see questions tagged &#39;changesets&#39;">changesets</span> <span class="post-tag tag-link-weekly" rel="tag" title="see questions tagged &#39;weekly&#39;">weekly</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 May '13, 05:02</strong></p>
<img src="https://secure.gravatar.com/avatar/e1d21bf0156f12ba67fcb192c5667790?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sa9496&#39;s gravatar image" />
<p><span>sa9496</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sa9496 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-22124" class="comments-container">
&#10;</div>
<div id="comment-tools-22124" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22124-form-container" class="comment-form-container">
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

<span id="22136"></span>

<div id="answer-container-22136" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-22136-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22136-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-22136-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Please tell us if you have read this page already:</p>
<p><a href="https://wiki.openstreetmap.org/wiki/Nominatim/Installation">https://wiki.openstreetmap.org/wiki/Nominatim/Installation</a></p>
<p>There are some hints about updating Nominatim's database.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 May '13, 16:59</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-22136" class="comments-container">
<span id="22163"></span>
<div id="comment-22163" class="comment">
<div id="post-22163-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Oh yes, of course I read it before I could set it up.<br />
</p>
<p>I also tried to run "./utils/update.php --import-osmosis-all --no-npi" to update the database after installation. However, what I'm aware is it will download multiple "hourly update" files and apply them one by one, which takes too long. In fact, on my computer with full planet file imported, it cannot even process 24 x "hourly update" file in a day. That means it can never catch up the "most recently" version of database....</p>
<p>That's why I would like to download the "weekly update" file and run it on my computer, I believe it's easier to handle...</p>
<p>Please let me know if I didn't anything wrongly. Thanks</p>
</div>
<div id="comment-22163-info" class="comment-info">
<span class="comment-age">(07 May '13, 13:06)</span> <span class="comment-user userinfo">sa9496</span>
</div>
</div>
</div>
<div id="comment-tools-22136" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22136-form-container" class="comment-form-container">
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

