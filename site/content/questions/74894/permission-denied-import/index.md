+++
type = "question"
title = "permission denied import"
description = '''Hello, The following happens to me, mark permission denied and I tried with sudo and without sudo also with sudo -u username ./utils / ..., but nothing /srv/nominatim/build/Nominatim$ ./utils/setup.php --osm-file /home/ubuntu/Descargas/mexico-latest.osm.pbf --all --osm2pgsql-cache 28000 2&amp;gt;&amp;amp;1 ...'''
date = "2020-05-18T22:02:00Z"
lastmod = "2020-05-18T22:10:00Z"
weight = 74894
keywords = [ "import", "nominatim", "data_import" ]
aliases = [ "/questions/74894" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [permission denied import](/questions/74894/permission-denied-import)

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
<span id="post-74894-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74894-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74894-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, The following happens to me, mark permission denied and I tried with sudo and without sudo also with sudo -u username ./utils / ..., but nothing</p>
<p>/srv/nominatim/build/Nominatim$ ./utils/setup.php --osm-file /home/ubuntu/Descargas/mexico-latest.osm.pbf --all --osm2pgsql-cache 28000 2&gt;&amp;1 | tee setup.log bash: ./utils/setup.php: Permiso denegado</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-data_import" rel="tag" title="see questions tagged &#39;data_import&#39;">data_import</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 May '20, 22:02</strong></p>
<img src="https://secure.gravatar.com/avatar/224322734ba5aec7f8c1b96e32946ca1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="edderantonio&#39;s gravatar image" />
<p><span>edderantonio</span><br />
<span class="score" title="11 reputation points">11</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="edderantonio has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-74894" class="comments-container">
&#10;</div>
<div id="comment-tools-74894" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74894-form-container" class="comment-form-container">
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

<span id="74896"></span>

<div id="answer-container-74896" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74896-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74896-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-74896-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you have a 'Nominatim' directory inside a 'build' directory, then I'm confused. No part of the installation instructions create this directory structure. It should've been <code>/srv/nominatim/Nominatim/build</code></p>
<p>Try logging in as user nominatim: 'sudo su nominatim' and then executing the script. And delete the file <code>setup.log</code>, maybe the file already exists and is write-protected (or owned by another user).</p>
<p>At some point helping from the other side of the world will no longer be possible, "permission denied" is a kind of error message a system administrator needs to be able to debug themselves, at least a bit. It's possible the software is too complex for your needs.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 May '20, 22:10</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-74896" class="comments-container">
&#10;</div>
<div id="comment-tools-74896" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74896-form-container" class="comment-form-container">
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

