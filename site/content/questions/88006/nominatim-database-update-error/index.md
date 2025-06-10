+++
type = "question"
title = "Nominatim database update error"
description = '''Periodicly i update the Nominatim database with the command: nominatim replication. And untill now that always worked correctly. But last time i did the process exited with this error (see image). psycopg2.errors.InternalError_: line_substring: 1st arg isn&#x27;t a line CONTEXT: PL/pgSQL function osmline...'''
date = "2023-11-16T01:09:00Z"
lastmod = "2024-01-23T08:32:00Z"
weight = 88006
keywords = [ "nominatim" ]
aliases = [ "/questions/88006" ]
osqa_answers = 7
osqa_accepted = false
+++

<div class="headNormal">

# [Nominatim database update error](/questions/88006/nominatim-database-update-error)

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
<span id="post-88006-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-88006-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-88006-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Periodicly i update the Nominatim database with the command: nominatim replication.</p>
<p>And untill now that always worked correctly. But last time i did the process exited with this error (see image).</p>
<p>psycopg2.errors.InternalError_: line_substring: 1st arg isn't a line CONTEXT: PL/pgSQL function osmline_update() line 113 at assignment</p>
<p><a href="https://www.imgpaste.net/image/KUowAY">https://www.imgpaste.net/image/KUowAY</a></p>
<p>When i restart the update process it will start the process again and apperently stop again at the same point.</p>
<p>Is there a way to update the database past this date or any other suggestion how to fix this ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Nov '23, 01:09</strong></p>
<img src="https://secure.gravatar.com/avatar/83ec59f9a0f82dc7c8ff3393a7586e32?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TrackTrace&#39;s gravatar image" />
<p><span>TrackTrace</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TrackTrace has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Nov '23, 01:20</strong> </span></p>
</div>
</div>
<div id="comments-container-88006" class="comments-container">
<span id="88139"></span>
<div id="comment-88139" class="comment">
<div id="post-88139-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi Ole,</p>
<p>Actually i did not find a solution. If no one can come up with a solution here i will rebuild the complete database.</p>
</div>
<div id="comment-88139-info" class="comment-info">
<span class="comment-age">(11 Jan '24, 00:01)</span> <span class="comment-user userinfo">TrackTrace</span>
</div>
</div>
</div>
<div id="comment-tools-88006" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-88006-form-container" class="comment-form-container">
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

7 Answers:

</div>

</div>

<span id="88124"></span>

<div id="answer-container-88124" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-88124-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-88124-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-88124-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I have exactly the same problem. Did you manage to get it running again? Thanks! Ole.</p>
<p>Setup: nominatim 4.2 with docker-compose</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Jan '24, 12:30</strong></p>
<img src="https://secure.gravatar.com/avatar/13820df4f4f1e48fa7f5fa1190e5af80?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="o_gardiner&#39;s gravatar image" />
<p><span>o_gardiner</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="o_gardiner has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-88124" class="comments-container">
&#10;</div>
<div id="comment-tools-88124" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-88124-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="88141"></span>

<div id="answer-container-88141" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-88141-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-88141-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-88141-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi TrackTrace,</p>
<p>Thanks for your response. Before rebuilding the complete database I wanted to check if an update to a newer version of Nominatim might help. Which version are you using?</p>
<p>Thanks, Ole.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Jan '24, 09:58</strong></p>
<img src="https://secure.gravatar.com/avatar/13820df4f4f1e48fa7f5fa1190e5af80?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="o_gardiner&#39;s gravatar image" />
<p><span>o_gardiner</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="o_gardiner has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-88141" class="comments-container">
&#10;</div>
<div id="comment-tools-88141" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-88141-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="88142"></span>

<div id="answer-container-88142" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-88142-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-88142-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-88142-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi Ole,</p>
<p>Im on 4.2.2</p>
<p>I see that there have been five major updates since then 4.2.2 <a href="https://nominatim.org/release-history/">https://nominatim.org/release-history/</a></p>
<p>Actually till now i did not really bother to much since the nominatim server kept working (without the updated database). By the way i have build the Europe database and You ?</p>
<p>Since the database update process seemed rather slow in the past i was still wondering if updating the database periodicly was really the best option. But now that you also have the same issue i will spend some time on it to see if updating nominatim can solve the problem.</p>
<p>Since i run nominatim on a virtualbox ubuntu server i will clone (server is about 650 GB) and then update it to see if it works (so that even if updating nominatim breaks the server i would still have the working original server).</p>
<p>P.s. Meaby you are interested to get in touch since we seem to have the same interest.</p>
<p>Follow up:</p>
<p>Did clone the server. When i now try to update nominatim it states.</p>
<p>nominatim admin --migrate</p>
<p>2024-01-11 12:07:22: Using project directory: /var/lib/postgresql</p>
<p>2024-01-11 12:07:22: Checking for necessary database migrations</p>
<p>2024-01-11 12:07:22: Database already at latest version (4.2.2-0)</p>
<p>I did download the latest update and put it in the /srv/nominatim directory where i originally installed 4.2.2 from.</p>
<p>I now have in this directory: /srv/nominatim Build Nominatim-4.2.2<br />
Nominatim-4.2.2.tar.bz2<br />
Nominatim-4.3.2.tar.bz2 (should i unpack this ?)</p>
<p>I did run the command: nominatim admin --migrate From both /srv/nominatim and /srv/nominatim/build</p>
<p>From both i get the same result:</p>
<p>2024-01-11 12:07:22: Using project directory: /var/lib/postgresql</p>
<p>2024-01-11 12:07:22: Checking for necessary database migrations</p>
<p>2024-01-11 12:07:22: Database already at latest version (4.2.2-0)</p>
<p>Did unpack: tar xf Nominatim-4.3.2.tar.bz2 Did Run the command nominatim admin --migrate from: /srv/nominatim/Nominatim-4.3.2directory with same result</p>
<p>Using project directory: /srv/nominatim/Nominatim-4.3.2</p>
<p>Checking for necessary database migrations</p>
<p>Database already at latest version (4.2.2-0)</p>
<p>Anyone has tips ?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Jan '24, 10:40</strong></p>
<img src="https://secure.gravatar.com/avatar/83ec59f9a0f82dc7c8ff3393a7586e32?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TrackTrace&#39;s gravatar image" />
<p><span>TrackTrace</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TrackTrace has no accepted answers">0%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Jan '24, 11:32</strong> </span></p>
</div>
</div>
<div id="comments-container-88142" class="comments-container">
&#10;</div>
<div id="comment-tools-88142" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-88142-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="88152"></span>

<div id="answer-container-88152" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-88152-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-88152-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-88152-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Meaby we can get a reply here:</p>
<p><a href="https://github.com/osm-search/Nominatim/issues/3299">https://github.com/osm-search/Nominatim/issues/3299</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Jan '24, 02:32</strong></p>
<img src="https://secure.gravatar.com/avatar/83ec59f9a0f82dc7c8ff3393a7586e32?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TrackTrace&#39;s gravatar image" />
<p><span>TrackTrace</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TrackTrace has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Jan '24, 02:36</strong> </span></p>
</div>
</div>
<div id="comments-container-88152" class="comments-container">
&#10;</div>
<div id="comment-tools-88152" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-88152-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="88154"></span>

<div id="answer-container-88154" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-88154-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-88154-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-88154-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi TrackTrace,</p>
<p>Thanks for your detailed answer! I'm using nominatim in a docker context, so updating should not be too difficult. The only thing that makes me hesitate is that we are running a custom dataset (Germany, Netherlands, Denmark, Austria) which I would prefer not to have to manually setup again. Did I understand your latest follow-up correctly in that an update did not help? Or ist the database update issue resolved now?</p>
<p>Btw, we are using nominatim to extract hierarchical geo information for a database of addresses which are being displayed on a map.</p>
<p>Cheers, Ole.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Jan '24, 08:29</strong></p>
<img src="https://secure.gravatar.com/avatar/13820df4f4f1e48fa7f5fa1190e5af80?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="o_gardiner&#39;s gravatar image" />
<p><span>o_gardiner</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="o_gardiner has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-88154" class="comments-container">
&#10;</div>
<div id="comment-tools-88154" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-88154-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="88178"></span>

<div id="answer-container-88178" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-88178-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-88178-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-88178-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi Ole,</p>
<p>Actually i used this suggestion.</p>
<p>Downloading and unpacking the *.tar.bz2 isn't enough. You need to build and install Nominatim (<a href="https://nominatim.org/release-docs/latest/admin/Installation/#building-nominatim).">https://nominatim.org/release-docs/latest/admin/Installation/#building-nominatim).</a> Then nominatim --version should print the new version. With the new version you can run nominatim admin --migrate</p>
<p>After that it gave me issues where the user had not enough write acces. So still was not able to try it with an updated version. Did you try anything ?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Jan '24, 23:50</strong></p>
<img src="https://secure.gravatar.com/avatar/83ec59f9a0f82dc7c8ff3393a7586e32?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TrackTrace&#39;s gravatar image" />
<p><span>TrackTrace</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TrackTrace has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-88178" class="comments-container">
&#10;</div>
<div id="comment-tools-88178" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-88178-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="88187"></span>

<div id="answer-container-88187" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-88187-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-88187-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-88187-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi TrackTrace,</p>
<p>Sorry for not getting back to you earlier. I plan to update nominatim within the next days or so and check if this solves the issue. I will keep you updated :)</p>
<p>Best, Ole</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Jan '24, 08:32</strong></p>
<img src="https://secure.gravatar.com/avatar/13820df4f4f1e48fa7f5fa1190e5af80?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="o_gardiner&#39;s gravatar image" />
<p><span>o_gardiner</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="o_gardiner has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-88187" class="comments-container">
&#10;</div>
<div id="comment-tools-88187" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-88187-form-container" class="comment-form-container">
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

