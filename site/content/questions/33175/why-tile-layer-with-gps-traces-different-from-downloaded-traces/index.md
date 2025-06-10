+++
type = "question"
title = "Why tile layer with gps-traces different from downloaded traces?"
description = '''In JOSM you can turn on a tms-layer that shows gps-traces from OpenStreetMap (tms[20]:https://gps-{switch:a,b,c}.tile.openstreetmap.org/lines/{zoom}/{x}/{y}.png). I did that, being happy that there is an option to show relatively easy uploaded gps-traces. After some time I realised me that there are...'''
date = "2014-05-14T15:38:00Z"
lastmod = "2014-05-23T10:49:00Z"
weight = 33175
keywords = [ "tiles", "traces", "gps" ]
aliases = [ "/questions/33175" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Why tile layer with gps-traces different from downloaded traces?](/questions/33175/why-tile-layer-with-gps-traces-different-from-downloaded-traces)

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
<span id="post-33175-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33175-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-33175-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>In JOSM you can turn on a tms-layer that shows gps-traces from OpenStreetMap (tms[20]:<a href="https://gps">https://gps</a>-{switch:a,b,c}.tile.openstreetmap.org/lines/{zoom}/{x}/{y}.png). I did that, being happy that there is an option to show relatively easy uploaded gps-traces. After some time I realised me that there are much less traces shown then when I download them directly from the OSM-server. So my question is, why there are differences between this tile-layer and the downloaded gps-traces? Maybe these tiles have not been refreshed since a long time?</p>
<p>Under what license are the uploaded gps-traces actually?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-traces" rel="tag" title="see questions tagged &#39;traces&#39;">traces</span> <span class="post-tag tag-link-gps" rel="tag" title="see questions tagged &#39;gps&#39;">gps</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 May '14, 15:38</strong></p>
<img src="https://secure.gravatar.com/avatar/448e9915cff2cfa46e47e1c7921d9779?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BAGgeraar&#39;s gravatar image" />
<p><span>BAGgeraar</span><br />
<span class="score" title="316 reputation points">316</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BAGgeraar has 2 accepted answers">33%</span></p>
</div>
</div>
<div id="comments-container-33175" class="comments-container">
&#10;</div>
<div id="comment-tools-33175" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33175-form-container" class="comment-form-container">
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

<span id="33234"></span>

<div id="answer-container-33234" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-33234-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33234-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-33234-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It's a service provided by Mapbox. According to <a href="https://www.mapbox.com/blog/openstreetmap-gps-layer/,">https://www.mapbox.com/blog/openstreetmap-gps-layer/,</a> it's all public available GPS traces. Further on they describe in more detail</p>
<blockquote>
<p>Every 60 seconds, the GPS layer is updated with the latest tracks that have been uploaded to OpenStreetMap. Any GPS track uploaded and marked as “Identifiable” or “Public” is included in the layer.</p>
</blockquote>
<p>If this is not what you are looking for, I suggest you ask them for more details.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 May '14, 13:47</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-33234" class="comments-container">
<span id="33236"></span>
<div id="comment-33236" class="comment">
<div id="post-33236-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>For a bit more info on this see <a href="https://github.com/openstreetmap/iD/issues/1930">here</a> and <a href="https://github.com/ericfischer/gpx-updater/issues/1">here</a>.</p>
</div>
<div id="comment-33236-info" class="comment-info">
<span class="comment-age">(16 May '14, 14:08)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-33234" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33234-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="33405"></span>

<div id="answer-container-33405" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-33405-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33405-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-33405-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I asked Mapbox and this is what they answered: "Updates to the GPX traces are not as frequent as desired and it takes time to reflect changes such as deletions or change of permissions. The original data are being import from the bulk GPX track data: <a href="https://blog.openstreetmap.org/2013/04/12/bulk-gpx-track-data/.">https://blog.openstreetmap.org/2013/04/12/bulk-gpx-track-data/."</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 May '14, 10:49</strong></p>
<img src="https://secure.gravatar.com/avatar/448e9915cff2cfa46e47e1c7921d9779?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BAGgeraar&#39;s gravatar image" />
<p><span>BAGgeraar</span><br />
<span class="score" title="316 reputation points">316</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BAGgeraar has 2 accepted answers">33%</span></p>
</div>
</div>
<div id="comments-container-33405" class="comments-container">
&#10;</div>
<div id="comment-tools-33405" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33405-form-container" class="comment-form-container">
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

