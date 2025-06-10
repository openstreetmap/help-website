+++
type = "question"
title = "How to find tracks at a location"
description = '''Is there a way to search all tracks at a certain location or in a certasin area'''
date = "2014-05-09T07:49:00Z"
lastmod = "2014-05-11T12:15:00Z"
weight = 33020
keywords = [ "tracks", "find" ]
aliases = [ "/questions/33020" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [How to find tracks at a location](/questions/33020/how-to-find-tracks-at-a-location)

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
<span id="post-33020-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33020-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-33020-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is there a way to search all tracks at a certain location or in a certasin area</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tracks" rel="tag" title="see questions tagged &#39;tracks&#39;">tracks</span> <span class="post-tag tag-link-find" rel="tag" title="see questions tagged &#39;find&#39;">find</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 May '14, 07:49</strong></p>
<img src="https://secure.gravatar.com/avatar/bb9dfa1612b0a11c4f1ed9d1ebde3d62?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Argo5&#39;s gravatar image" />
<p><span>Argo5</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Argo5 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-33020" class="comments-container">
<span id="33021"></span>
<div id="comment-33021" class="comment">
<div id="post-33021-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Please explain what <em>tracks</em> you are looking for and what you intend to do with them.</p>
</div>
<div id="comment-33021-info" class="comment-info">
<span class="comment-age">(09 May '14, 07:57)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="33043"></span>
<div id="comment-33043" class="comment">
<div id="post-33043-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Also describe your usecase. Are you a mapper? Are you a data user? A programmer?</p>
</div>
<div id="comment-33043-info" class="comment-info">
<span class="comment-age">(09 May '14, 14:00)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-33020" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33020-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="33082"></span>

<div id="answer-container-33082" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-33082-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33082-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-33082-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Assuming that you speak of GPX tracks which we call "traces" - no, this is not possible.</p>
<p>The OpenStreetMap backend stores uploaded traces in two forms. It keeps the original files, but also processes them and inserts all points found in the traces into the database. The original files cannot be queries by location - the only <a href="http://wiki.openstreetmap.org/wiki/API_v0.6#Downloading_trace_metadata">API calls available for accessing the original files</a> are "all traces for the logged in user", and "trace with id X". The database <em>can</em> be queried by location (there is an <a href="http://wiki.openstreetmap.org/wiki/API_v0.6#Retrieving_GPS_points">API call that gives you all trackpoints in a given area)</a> but that access mode will not tell you which track a point is from so you cannot reconstruct the full track. The same is true for the <a href="http://planet.openstreetmap.org/gps/">full GPX planet dump</a> - it contains all trackpoints but not the track IDs.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 May '14, 12:15</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-33082" class="comments-container">
&#10;</div>
<div id="comment-tools-33082" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33082-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="33029"></span>

<div id="answer-container-33029" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-33029-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33029-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-33029-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you mean all GPS traces uploaded to OSM, read <a href="https://www.mapbox.com/blog/openstreetmap-gps-layer/">https://www.mapbox.com/blog/openstreetmap-gps-layer/</a> on how you can see them in iD. The same layer is available for JOSM users</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 May '14, 09:18</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-33029" class="comments-container">
&#10;</div>
<div id="comment-tools-33029" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33029-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="33060"></span>

<div id="answer-container-33060" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-33060-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33060-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-33060-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you edit with Potlatch2 click GPS dropdown and GPS Data<img src="/upfiles/aa_potlatch2_GPs_traces_1.JPG" alt="alt text" /></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 May '14, 23:47</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 May '14, 01:33</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-33060" class="comments-container">
&#10;</div>
<div id="comment-tools-33060" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33060-form-container" class="comment-form-container">
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

