+++
type = "question"
title = "osm2pgsql with --flat-nodes question (closed)"
description = '''when import the pbf file with : osm2pgsql --create --slim --flat-nodes /mnt/resource/nodes.cache /opt/osm/planet-190805.osm.pbf then, the file /mnt/resource/nodes.cache must been keep for osm2pgsql --append ? and will the osm2pgsql --append update the file /mnt/resource/nodes.cache for next running ...'''
date = "2019-08-30T02:35:00Z"
lastmod = "2019-08-30T09:41:00Z"
weight = 70565
keywords = [ "flat-nodes", "osm2pgsql" ]
aliases = [ "/questions/70565" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [osm2pgsql with --flat-nodes question (closed)](/questions/70565/osm2pgsql-with-flat-nodes-question-closed)

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
<span id="post-70565-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70565-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-70565-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>when import the pbf file with : osm2pgsql --create --slim --flat-nodes /mnt/resource/nodes.cache /opt/osm/planet-190805.osm.pbf</p>
<p>then, the file /mnt/resource/nodes.cache must been keep for osm2pgsql --append ?</p>
<p>and will the osm2pgsql --append update the file /mnt/resource/nodes.cache for next running time?</p>
<p>and is the file /mnt/resource/nodes.cache need for mapnik etc.?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-flat-nodes" rel="tag" title="see questions tagged &#39;flat-nodes&#39;">flat-nodes</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Aug '19, 02:35</strong></p>
<img src="https://secure.gravatar.com/avatar/5d7bbd96dde7f9bc6a9e599a925f9a76?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nationals&#39;s gravatar image" />
<p><span>Nationals</span><br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nationals has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Sep '19, 01:22</strong> </span></p>
</div>
</div>
<div id="comments-container-70565" class="comments-container">
<span id="70566"></span>
<div id="comment-70566" class="comment">
<div id="post-70566-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>how about the performance different using --flat-nodes or not while osm2pgsql --create?</p>
</div>
<div id="comment-70566-info" class="comment-info">
<span class="comment-age">(30 Aug '19, 03:13)</span> <span class="comment-user userinfo">Nationals</span>
</div>
</div>
</div>
<div id="comment-tools-70565" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70565-form-container" class="comment-form-container">
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

<span id="70567"></span>

<div id="answer-container-70567" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-70567-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70567-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-70567-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you want to do updates with <code>--append</code> then you need to keep the flatnodes file, and specify it again with <code>--flat-nodes</code> when doing the update. If you do not want to do updates then you can delete the file.</p>
<p>The performance on the initial import is better with <code>--flat-nodes</code> if you have a large data set; for very small data sets (small country, or just a state or so) it can be faster without.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Aug '19, 09:01</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-70567" class="comments-container">
<span id="70568"></span>
<div id="comment-70568" class="comment">
<div id="post-70568-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>thanks for your reply.</p>
<p>and is the file /mnt/resource/nodes.cache need for mapnik etc. ?</p>
</div>
<div id="comment-70568-info" class="comment-info">
<span class="comment-age">(30 Aug '19, 09:11)</span> <span class="comment-user userinfo">Nationals</span>
</div>
</div>
<span id="70569"></span>
<div id="comment-70569" class="comment">
<div id="post-70569-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>No, it is only accessed by osm2pgsql.</p>
</div>
<div id="comment-70569-info" class="comment-info">
<span class="comment-age">(30 Aug '19, 09:41)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-70567" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70567-form-container" class="comment-form-container">
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

