+++
type = "question"
title = "Adding more states to nominatim installation: what are the additional steps"
description = '''I have completed a local Nominatim installation with California (USA) added and the entire tiger database already parsed as per the documentation. Now I want to add the rest of North America as well. My questions are:  Can I just add the north-american pbf to osm2pgsql using the command in the docum...'''
date = "2016-07-25T03:20:00Z"
lastmod = "2016-07-25T04:49:00Z"
weight = 51080
keywords = [ "nominatim", "osm2pgsql" ]
aliases = [ "/questions/51080" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Adding more states to nominatim installation: what are the additional steps](/questions/51080/adding-more-states-to-nominatim-installation-what-are-the-additional-steps)

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
<span id="post-51080-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51080-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-51080-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have completed a local Nominatim installation with California (USA) added and the entire tiger database already parsed as per the <a href="http://wiki.openstreetmap.org/wiki/Nominatim/Installation">documentation</a>. Now I want to add the rest of North America as well. My questions are:</p>
<ol>
<li>Can I just add the north-american pbf to osm2pgsql using the command in the documentation and assume that California will be ignored ? The command I am talking about is: <code>./utils/setup.php --osm-file north-america-latest.osm.pbf --all [--osm2pgsql-cache 18000] 2&gt;&amp;1 | tee setup.log</code>.</li>
<li>Can I assume that the tiger and wiki bins mentioned in the same <a href="http://wiki.openstreetmap.org/wiki/Nominatim/Installation">documentation</a> will not need to be processed again as they are independent of the state ?</li>
<li>Is there anything else I need to do apart from the osm upload mentioned in (1) for the nominatim install ?</li>
</ol>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Jul '16, 03:20</strong></p>
<img src="https://secure.gravatar.com/avatar/cd15d38fd1e508e6c2bcad9e153e789d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="arunmk&#39;s gravatar image" />
<p><span>arunmk</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="arunmk has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-51080" class="comments-container">
&#10;</div>
<div id="comment-tools-51080" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51080-form-container" class="comment-form-container">
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

<span id="51081"></span>

<div id="answer-container-51081" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-51081-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51081-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-51081-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Answering it myself after doing a bit more research on the site: it seems like the above is not advisable though it is possible.</p>
<p>The relevant answers are over <a href="https://help.openstreetmap.org/questions/30492/updating-n-america-data-to-planet-data">here</a> and over <a href="https://help.openstreetmap.org/questions/15505/import-more-osm-files-in-to-nominatim">here</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Jul '16, 04:49</strong></p>
<img src="https://secure.gravatar.com/avatar/cd15d38fd1e508e6c2bcad9e153e789d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="arunmk&#39;s gravatar image" />
<p><span>arunmk</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="arunmk has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-51081" class="comments-container">
&#10;</div>
<div id="comment-tools-51081" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51081-form-container" class="comment-form-container">
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

