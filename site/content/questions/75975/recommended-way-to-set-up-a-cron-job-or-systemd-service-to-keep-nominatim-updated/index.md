+++
type = "question"
title = "Recommended way to set up a Cron job or Systemd service to keep Nominatim updated?"
description = '''Subject says it all. The update method mentioned in the docs, ./utils/update.php --import-osmosis-all seems to be designed to be a forked process as it will keep running after an update until the sleep timeout then do it again. How can I convert this into a Systemd service? Similarly, if I&#x27;m using C...'''
date = "2020-08-01T02:02:00Z"
lastmod = "2020-08-01T02:45:00Z"
weight = 75975
keywords = [ "nominatim", "update", "updates" ]
aliases = [ "/questions/75975" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Recommended way to set up a Cron job or Systemd service to keep Nominatim updated?](/questions/75975/recommended-way-to-set-up-a-cron-job-or-systemd-service-to-keep-nominatim-updated)

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
<span id="post-75975-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75975-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-75975-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Subject says it all. The update method mentioned in the docs, <code>./utils/update.php --import-osmosis-all</code> seems to be designed to be a forked process as it will keep running after an update until the sleep timeout then do it again. How can I convert this into a Systemd service?</p>
<p>Similarly, if I'm using Cron, do I just have it run <code>./utils/update.php --import-osmosis</code> no more often than the update interval specified in settings/local.php? Is there a way to disable its built-in sleep so it just checks immediately? (This is how cron jobs seem to be intended to work, as cron handles the sleeping/scheduling.)</p>
<p><code>--check-for-updates</code> returns immediately, but does it only do a check or will it download updates if there are any?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-update" rel="tag" title="see questions tagged &#39;update&#39;">update</span> <span class="post-tag tag-link-updates" rel="tag" title="see questions tagged &#39;updates&#39;">updates</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Aug '20, 02:02</strong></p>
<img src="https://secure.gravatar.com/avatar/9d09f8dc09cc4e4e2b72019fb0c1fefc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RenegadeTech&#39;s gravatar image" />
<p><span>RenegadeTech</span><br />
<span class="score" title="46 reputation points">46</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RenegadeTech has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Aug '20, 01:36</strong> </span></p>
</div>
</div>
<div id="comments-container-75975" class="comments-container">
<span id="75976"></span>
<div id="comment-75976" class="comment">
<div id="post-75976-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'm guessing you're talking about nominatim here?</p>
</div>
<div id="comment-75976-info" class="comment-info">
<span class="comment-age">(01 Aug '20, 02:07)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="75977"></span>
<div id="comment-75977" class="comment">
<div id="post-75977-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Oops, yes, sorry. Fixed.</p>
</div>
<div id="comment-75977-info" class="comment-info">
<span class="comment-age">(01 Aug '20, 02:45)</span> <span class="comment-user userinfo">RenegadeTech</span>
</div>
</div>
</div>
<div id="comment-tools-75975" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75975-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

