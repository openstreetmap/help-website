+++
type = "question"
title = "wget can&#x27;t download requested file"
description = '''Hi, I am trying get map from openstreetmaps, but having problems. (debian system) $ wget -O patagonie.osm &quot;http://api.openstreetmap.org/api/0.6/map?bbox=-75.64,-56.17,-64.70,-50.00&quot; --2011-10-20 23:07:43-- http://api.openstreetmap.org/api/0.6/map?bbox=-75.64,-56.17,-64.70,-50.00 Resolving api.openst...'''
date = "2011-10-20T22:21:00Z"
lastmod = "2011-10-21T00:56:00Z"
weight = 8543
keywords = [ "wget" ]
aliases = [ "/questions/8543" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [wget can't download requested file](/questions/8543/wget-cant-download-requested-file)

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
<span id="post-8543-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8543-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-8543-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I am trying get map from openstreetmaps, but having problems. (debian system) $ wget -O patagonie.osm "http://api.openstreetmap.org/api/0.6/map?bbox=-75.64,-56.17,-64.70,-50.00" --2011-10-20 23:07:43-- <a href="http://api.openstreetmap.org/api/0.6/map?bbox=-75.64,-56.17,-64.70,-50.00">http://api.openstreetmap.org/api/0.6/map?bbox=-75.64,-56.17,-64.70,-50.00</a> Resolving <a href="http://api.openstreetmap.org">api.openstreetmap.org</a> (<a href="http://api.openstreetmap.org">api.openstreetmap.org</a>)... 193.63.75.100, 193.63.75.99 Connecting to <a href="http://api.openstreetmap.org">api.openstreetmap.org</a> (<a href="http://api.openstreetmap.org">api.openstreetmap.org</a>)|193.63.75.100|:80... connected. HTTP request sent, awaiting response... 400 Bad Request 2011-10-20 23:07:43 ERROR 400: Bad Request.</p>
<p>Is this data too big?</p>
<p>regards</p>
<p>mira</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-wget" rel="tag" title="see questions tagged &#39;wget&#39;">wget</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Oct '11, 22:21</strong></p>
<img src="https://secure.gravatar.com/avatar/cc698b57a5363f253ef29a95753ae24c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="miramikes&#39;s gravatar image" />
<p><span>miramikes</span><br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="miramikes has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-8543" class="comments-container">
&#10;</div>
<div id="comment-tools-8543" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8543-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="8544"></span>

<div id="answer-container-8544" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8544-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8544-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-8544-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Yes, it's apparently too big.</p>
<p>When I open <a href="http://api.openstreetmap.org/api/0.6/map?bbox=-75.64,-56.17,-64.70,-50.00">http://api.openstreetmap.org/api/0.6/map?bbox=-75.64,-56.17,-64.70,-50.00</a> in Firefox I get:</p>
<p><strong>The maximum bbox size is 0.25, and your request was too large. Either request a smaller area, or use planet.osm</strong></p>
<p>You will see the same error message if you add the <code>-S</code> switch to your <code>wget</code> command (i.e. <code>wget -SO patagonie.osm ...</code>).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Oct '11, 22:36</strong></p>
<img src="https://secure.gravatar.com/avatar/c2a980da3fdfa1ee2659ad70d1e21f31?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gnurk&#39;s gravatar image" />
<p><span>gnurk</span><br />
<span class="score" title="6114 reputation points"><span>6.1k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="silver">●</span><span class="badgecount">60</span></span><span title="96 badges"><span class="bronze">●</span><span class="badgecount">96</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gnurk has 18 accepted answers">15%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Oct '11, 00:13</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span></p>
</div>
</div>
<div id="comments-container-8544" class="comments-container">
<span id="8549"></span>
<div id="comment-8549" class="comment">
<div id="post-8549-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for clarifying</p>
</div>
<div id="comment-8549-info" class="comment-info">
<span class="comment-age">(21 Oct '11, 00:56)</span> <span class="comment-user userinfo">miramikes</span>
</div>
</div>
</div>
<div id="comment-tools-8544" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8544-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="8547"></span>

<div id="answer-container-8547" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8547-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8547-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-8547-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The main OpenStreetMap API is provided for editing the map, not for downloading large extracts for other projects. So it limits how large an area you can download. See the <a href="http://wiki.openstreetmap.org/wiki/API_usage_policy">API usage policy</a>.</p>
<p>If you want a larger extract, eg a whole country, then it is probably best to use a Planet extract. These are available from a number of different providers, covering different parts of the world, see <a href="http://wiki.openstreetmap.org/wiki/Planet#Country_and_area_extracts">Planet.osm extracts</a>. Geofabrik and Cloudmade provide extracts for Argentina and Chile, or for the whole of South America, which would cover the area of your bounding box request.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Oct '11, 00:01</strong></p>
<img src="https://secure.gravatar.com/avatar/aa505c046b1c010e997a7849c6f3dbbe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vclaw&#39;s gravatar image" />
<p><span>Vclaw</span><br />
<span class="score" title="9217 reputation points"><span>9.2k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="95 badges"><span class="silver">●</span><span class="badgecount">95</span></span><span title="141 badges"><span class="bronze">●</span><span class="badgecount">141</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vclaw has 41 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-8547" class="comments-container">
<span id="8548"></span>
<div id="comment-8548" class="comment">
<div id="post-8548-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ok, thank you.</p>
</div>
<div id="comment-8548-info" class="comment-info">
<span class="comment-age">(21 Oct '11, 00:55)</span> <span class="comment-user userinfo">miramikes</span>
</div>
</div>
</div>
<div id="comment-tools-8547" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8547-form-container" class="comment-form-container">
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

