+++
type = "question"
title = "Nominatim Setup.php : ERROR: Scripts must be run from build directory"
description = '''i&#x27;m trying to setup my own nominatim server in a CentOS 7 VirtualMachine. I&#x27;m using this guide which is followed here for data import. This line gives me trouble when trying to import data: ./utils/setup.php --osm-file &amp;lt;_data_file_&amp;gt; --all  When executing the above command, the output says &quot;ERR...'''
date = "2018-02-21T13:44:00Z"
lastmod = "2018-02-21T14:18:00Z"
weight = 62251
keywords = [ "setup.php", "nominatim", "centos", "php" ]
aliases = [ "/questions/62251" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Nominatim Setup.php : ERROR: Scripts must be run from build directory](/questions/62251/nominatim-setupphp-error-scripts-must-be-run-from-build-directory)

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
<span id="post-62251-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62251-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-62251-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>i'm trying to setup my own nominatim server in a CentOS 7 VirtualMachine. I'm using <a href="https://nominatim.org/release-docs/latest/appendix/Install-on-Centos-7/">this guide</a> which is followed <a href="https://nominatim.org/release-docs/latest/admin/Import-and-Update/">here</a> for data import.</p>
<p>This line gives me trouble when trying to import data:</p>
<pre><code>./utils/setup.php --osm-file &lt;_data_file_&gt; --all</code></pre>
<p>When executing the above command, the output says "ERROR: Scripts must be run from build directory.".</p>
<p>Which one would be the build directory?</p>
<p>I tried running from nominatim root directory, utils, and data, but no luck.</p>
<p>Best regards, Federico.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-setup.php" rel="tag" title="see questions tagged &#39;setup.php&#39;">setup.php</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-centos" rel="tag" title="see questions tagged &#39;centos&#39;">centos</span> <span class="post-tag tag-link-php" rel="tag" title="see questions tagged &#39;php&#39;">php</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Feb '18, 13:44</strong></p>
<img src="https://secure.gravatar.com/avatar/a18f136faf7c1903109a9dda85ecdffb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Federico%20Alvarez%20UY&#39;s gravatar image" />
<p><span>Federico Alv...</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Federico Alvarez UY has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Feb '18, 14:03</strong> </span></p>
</div>
</div>
<div id="comments-container-62251" class="comments-container">
&#10;</div>
<div id="comment-tools-62251" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62251-form-container" class="comment-form-container">
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

<span id="62254"></span>

<div id="answer-container-62254" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-62254-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62254-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-62254-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Federico Alvarez UY has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The guide has a couple of lines <code>mkdir build; cd build; cmake ..; make</code>. While the <code>build</code> directory could be anywhere in the filesystem, it's usually a subdirectory of the <code>Nominatim</code> directory, so a <code>cd build</code>, then <code>./utils/setup.php...</code></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Feb '18, 14:12</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-62254" class="comments-container">
<span id="62255"></span>
<div id="comment-62255" class="comment">
<div id="post-62255-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks a lot mtmail. That was it!</p>
<p>Will continue installation now.</p>
<p>Thanks again.</p>
<p>Best regards, Federico.</p>
</div>
<div id="comment-62255-info" class="comment-info">
<span class="comment-age">(21 Feb '18, 14:18)</span> <span class="comment-user userinfo">Federico Alv...</span>
</div>
</div>
</div>
<div id="comment-tools-62254" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62254-form-container" class="comment-form-container">
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

