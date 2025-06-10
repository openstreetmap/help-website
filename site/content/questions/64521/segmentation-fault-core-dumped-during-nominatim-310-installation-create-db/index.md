+++
type = "question"
title = "Segmentation fault (core dumped) during Nominatim 3.1.0 installation Create DB"
description = '''Hello, I am attempting to install Nominatim on Ubuntu 14.04 with php5. During the attempt to run setup.php it fails on this line: https://github.com/openstreetmap/Nominatim/blob/master/utils/setup.php#L88 With output: 2018-07-04 06:31:38 == Create DB Segmentation fault (core dumped)  My version of P...'''
date = "2018-07-04T07:56:00Z"
lastmod = "2018-07-04T07:56:00Z"
weight = 64521
keywords = [ "segfault", "nominatim", "installation" ]
aliases = [ "/questions/64521" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Segmentation fault (core dumped) during Nominatim 3.1.0 installation Create DB](/questions/64521/segmentation-fault-core-dumped-during-nominatim-310-installation-create-db)

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
<span id="post-64521-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64521-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-64521-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I am attempting to install Nominatim on Ubuntu 14.04 with php5. During the attempt to run setup.php it fails on this line: <a href="https://github.com/openstreetmap/Nominatim/blob/master/utils/setup.php#L88">https://github.com/openstreetmap/Nominatim/blob/master/utils/setup.php#L88</a></p>
<p>With output:</p>
<pre><code>2018-07-04 06:31:38 == Create DB
Segmentation fault (core dumped)</code></pre>
<p>My version of PEAR::DB is 1.9.2.</p>
<p>If I deliberately break the connection string, it will return a 'DB not available' error without throwing a segfault. The command I ran was:</p>
<pre><code>./utils/setup.php --osm-file /srv/nominatim/australia-latest.osm.pbf --all 2&gt;&amp;1</code></pre>
<p>I get the same results if I run with root (I know that the setup instructions warn against installing as root).</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-segfault" rel="tag" title="see questions tagged &#39;segfault&#39;">segfault</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-installation" rel="tag" title="see questions tagged &#39;installation&#39;">installation</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Jul '18, 07:56</strong></p>
<img src="https://secure.gravatar.com/avatar/f76c1f20a04c0e8b3e33afc521274f63?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jordanglue&#39;s gravatar image" />
<p><span>jordanglue</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jordanglue has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-64521" class="comments-container">
&#10;</div>
<div id="comment-tools-64521" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64521-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

