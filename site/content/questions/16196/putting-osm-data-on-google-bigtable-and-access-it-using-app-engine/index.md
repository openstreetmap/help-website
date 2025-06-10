+++
type = "question"
title = "putting OSm data on Google bigtable and access it using app engine"
description = '''Hiya, Does anyone know of any tools for converting (and ideally uploading) OSM data to google app engine/big table? Thanks PS I have fooled around with postgres etc offline but I was looking for an online server.'''
date = "2012-09-18T03:32:00Z"
lastmod = "2012-09-18T04:19:00Z"
weight = 16196
keywords = [ "engine", "app", "datastore", "bigtable" ]
aliases = [ "/questions/16196" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [putting OSm data on Google bigtable and access it using app engine](/questions/16196/putting-osm-data-on-google-bigtable-and-access-it-using-app-engine)

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
<span id="post-16196-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16196-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-16196-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hiya,</p>
<p>Does anyone know of any tools for converting (and ideally uploading) OSM data to google app engine/big table?</p>
<p>Thanks</p>
<p>PS I have fooled around with postgres etc offline but I was looking for an online server.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-engine" rel="tag" title="see questions tagged &#39;engine&#39;">engine</span> <span class="post-tag tag-link-app" rel="tag" title="see questions tagged &#39;app&#39;">app</span> <span class="post-tag tag-link-datastore" rel="tag" title="see questions tagged &#39;datastore&#39;">datastore</span> <span class="post-tag tag-link-bigtable" rel="tag" title="see questions tagged &#39;bigtable&#39;">bigtable</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Sep '12, 03:32</strong></p>
<img src="https://secure.gravatar.com/avatar/4d1b1af15ea6b9401536117739666981?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jake%20cimirlo&#39;s gravatar image" />
<p><span>jake cimirlo</span><br />
<span class="score" title="101 reputation points">101</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jake cimirlo has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-16196" class="comments-container">
&#10;</div>
<div id="comment-tools-16196" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16196-form-container" class="comment-form-container">
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

<span id="16198"></span>

<div id="answer-container-16198" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-16198-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16198-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-16198-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I guess the easy answer is OSM -&gt; KML -&gt; datastore. Could it really be that simple?</p>
<p>In case anyone is interested, the project is to do agent based modeling using real world data. I've done the OSM to Netlogo to play around in, got the agents doing A* and TS with multimodal criteria. But Netlogo is slower than the horse you bet your rent on on my computer. So I thought I'd take a stab at online computing using Google or Amazon to host the data (or something else if anyone has any suggestions), python or java (probably python) for the programming and then exporting to Google Earth for the vizualizing. It is probably well beyond my capabilities but my little experience in programming suggests i learn better trying a project than farting around trying to actually learn something.</p>
<p>Anyway, if anyone has any suggestions or sources, I would welcome them.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Sep '12, 04:19</strong></p>
<img src="https://secure.gravatar.com/avatar/4d1b1af15ea6b9401536117739666981?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jake%20cimirlo&#39;s gravatar image" />
<p><span>jake cimirlo</span><br />
<span class="score" title="101 reputation points">101</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jake cimirlo has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-16198" class="comments-container">
&#10;</div>
<div id="comment-tools-16198" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16198-form-container" class="comment-form-container">
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

