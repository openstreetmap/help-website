+++
type = "question"
title = "How can I download a subset of the data for a large area?"
description = '''I want to download a big area as an .osm file using filters. For example, I want to download France without roads because I don&#x27;t need them, and I want a smaller file. Is it possible?'''
date = "2011-10-30T10:28:00Z"
lastmod = "2011-10-31T13:29:00Z"
weight = 8700
keywords = [ "download", "filtering" ]
aliases = [ "/questions/8700" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How can I download a subset of the data for a large area?](/questions/8700/how-can-i-download-a-subset-of-the-data-for-a-large-area)

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
<span id="post-8700-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8700-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-8700-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to download a big area as an .osm file using filters. For example, I want to download France without roads because I don't need them, and I want a smaller file. Is it possible?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-download" rel="tag" title="see questions tagged &#39;download&#39;">download</span> <span class="post-tag tag-link-filtering" rel="tag" title="see questions tagged &#39;filtering&#39;">filtering</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Oct '11, 10:28</strong></p>
<img src="https://secure.gravatar.com/avatar/aa8b71d1269f59a9abff7956903a240c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Corentin&#39;s gravatar image" />
<p><span>Corentin</span><br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Corentin has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Oct '11, 13:24</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/9fe361843971cf8b23dc93517f00b996?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jonathan%20Bennett&#39;s gravatar image" />
<p><span>Jonathan Ben...</span><br />
<span class="score" title="8261 reputation points"><span>8.3k</span></span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="85 badges"><span class="silver">●</span><span class="badgecount">85</span></span><span title="108 badges"><span class="bronze">●</span><span class="badgecount">108</span></span></p>
</div>
</div>
<div id="comments-container-8700" class="comments-container">
&#10;</div>
<div id="comment-tools-8700" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8700-form-container" class="comment-form-container">
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

<span id="8701"></span>

<div id="answer-container-8701" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8701-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8701-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-8701-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You probably want to use somthing like <a href="https://wiki.openstreetmap.org/wiki/Xapi">XAPI</a> or <a href="https://wiki.openstreetmap.org/wiki/Overpass_API">Overpass</a>. However for big conuntry extracts you have <a href="http://download.geofabrik.de/osm/">GeoFabrik</a> and <a href="http://downloads.cloudmade.com/">CloudMade</a> that uses the <a href="https://wiki.openstreetmap.org/wiki/Pbf">PBF</a> binary format that is smaller then crompressed XML files.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Oct '11, 11:42</strong></p>
<img src="https://secure.gravatar.com/avatar/44a4438f0146dfd898e24c221fd28b58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gnonthgol&#39;s gravatar image" />
<p><span>Gnonthgol ♦</span><br />
<span class="score" title="13750 reputation points"><span>13.8k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="103 badges"><span class="silver">●</span><span class="badgecount">103</span></span><span title="198 badges"><span class="bronze">●</span><span class="badgecount">198</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gnonthgol has 57 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-8701" class="comments-container">
<span id="8718"></span>
<div id="comment-8718" class="comment">
<div id="post-8718-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>... and once you've got data from e.g. GeoFabrik you can then use something like <a href="https://wiki.openstreetmap.org/wiki/Osmfilter">https://wiki.openstreetmap.org/wiki/Osmfilter</a> to either extract what you want or delete what you don't want.</p>
<p>France is quite large, so maybe a smaller area might be what you're looking for - <a href="http://download.geofabrik.de/osm/europe/france/">http://download.geofabrik.de/osm/europe/france/</a> ?</p>
</div>
<div id="comment-8718-info" class="comment-info">
<span class="comment-age">(31 Oct '11, 13:29)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-8701" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8701-form-container" class="comment-form-container">
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

