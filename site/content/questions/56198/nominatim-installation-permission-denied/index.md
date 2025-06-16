+++
type = "question"
title = "Nominatim installation - Permission denied"
description = '''I get the following error when I try to import pdf file: ERROR: could not access file &quot;/srv/nominatim/Nominatim/build/module/nominatim.so&quot;: Permission denied ERROR: pgsql returned with error code (3) pgsql returned with error code (3) I have already checked other threads regarding this issue and non...'''
date = "2017-05-16T10:34:00Z"
lastmod = "2017-05-16T12:46:00Z"
weight = 56198
keywords = [ "nominatim.so", "nominatim", "permission" ]
aliases = [ "/questions/56198" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Nominatim installation - Permission denied](/questions/56198/nominatim-installation-permission-denied)

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
<span id="post-56198-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56198-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-56198-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I get the following error when I try to import pdf file:</p>
<p>ERROR: could not access file "/srv/nominatim/Nominatim/build/module/nominatim.so": Permission denied ERROR: pgsql returned with error code (3) pgsql returned with error code (3)</p>
<p>I have already checked other threads regarding this issue and non of them could help me to fix the problem. I don't use root for installation and have given all permissions to postgres user. I can even edit the file with postgres user. Postgres has access to all parent directories as well.</p>
<p>I use Fedora 24.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim.so" rel="tag" title="see questions tagged &#39;nominatim.so&#39;">nominatim.so</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-permission" rel="tag" title="see questions tagged &#39;permission&#39;">permission</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 May '17, 10:34</strong></p>
<img src="https://secure.gravatar.com/avatar/ca009706fa6df2b33eb931f781ff57f4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="khamooshi&#39;s gravatar image" />
<p><span>khamooshi</span><br />
<span class="score" title="146 reputation points">146</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="khamooshi has one accepted answer">50%</span></p>
</div>
</div>
<div id="comments-container-56198" class="comments-container">
<span id="56199"></span>
<div id="comment-56199" class="comment">
<div id="post-56199-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>There has been a similar problem here: <a href="/questions/13825/permission-issue-of-so-file-in-nominatim-osm-postgres-db">https://help.openstreetmap.org/questions/13825/permission-issue-of-so-file-in-nominatim-osm-postgres-db</a> Please re-check that the file and <em>each</em> directory in the path has read and execute permissions for the user or group your pgsql process is running with. If in doubt login as root, switch to the psql user and then try to access the file yourself.</p>
</div>
<div id="comment-56199-info" class="comment-info">
<span class="comment-age">(16 May '17, 12:33)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-56198" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56198-form-container" class="comment-form-container">
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

<span id="56200"></span>

<div id="answer-container-56200" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56200-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56200-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-56200-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="khamooshi has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Check if you have SELinux on, and if yes, switch it off before retrying. If that fixes the problem, you can work on defining a more fine-grained permission for SELinux to allow PostgreSQL to load the .so file. See <a href="https://docs.fedoraproject.org/en-US/Fedora/12/html/Security-Enhanced_Linux/sect-Security-Enhanced_Linux-Working_with_SELinux-Enabling_and_Disabling_SELinux.html">https://docs.fedoraproject.org/en-US/Fedora/12/html/Security-Enhanced_Linux/sect-Security-Enhanced_Linux-Working_with_SELinux-Enabling_and_Disabling_SELinux.html</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 May '17, 12:46</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-56200" class="comments-container">
&#10;</div>
<div id="comment-tools-56200" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56200-form-container" class="comment-form-container">
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

