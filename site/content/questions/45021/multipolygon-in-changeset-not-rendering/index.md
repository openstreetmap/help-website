+++
type = "question"
title = "multipolygon in changeset not rendering"
description = '''I added this changeset over a day ago (a natural reserve boundary). The ways are definitely in the database and tagged correctly: boundary=national_park. However, the natural reserve is not rendering on the OSM slippy map. The changeset was created from an ESRI Shapefile imported using JOSM, as desc...'''
date = "2015-09-02T07:12:00Z"
lastmod = "2015-09-02T11:56:00Z"
weight = 45021
keywords = [ "shapefile", "changeset", "multipolygon", "josm", "rendering" ]
aliases = [ "/questions/45021" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [multipolygon in changeset not rendering](/questions/45021/multipolygon-in-changeset-not-rendering)

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
<span id="post-45021-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45021-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-45021-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I added this <a href="https://www.openstreetmap.org/changeset/33709791" title="changeset">changeset</a> over a day ago (a natural reserve boundary). The ways are definitely in the database and tagged correctly: <code>boundary=national_park</code>. However, the natural reserve is not rendering on the OSM slippy map.</p>
<p>The changeset was created from an ESRI Shapefile imported using JOSM, as described in the wiki. Is the multipolygon constructed incorrectly? What am I doing wrong here? I'd like to add many unmapped conservation areas like this.</p>
<p><strong>EDIT:</strong> After <a href="https://www.openstreetmap.org/changeset/33741738">these changes</a> by another user, it's starting to render at some zoom levels. I still don't understand what I did wrong, though. What was broken in my initial changeset?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-shapefile" rel="tag" title="see questions tagged &#39;shapefile&#39;">shapefile</span> <span class="post-tag tag-link-changeset" rel="tag" title="see questions tagged &#39;changeset&#39;">changeset</span> <span class="post-tag tag-link-multipolygon" rel="tag" title="see questions tagged &#39;multipolygon&#39;">multipolygon</span> <span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Sep '15, 07:12</strong></p>
<img src="https://secure.gravatar.com/avatar/e12e88db04b2b596c6bc53c8d18e817e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="inkatlas&#39;s gravatar image" />
<p><span>inkatlas</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="inkatlas has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Sep '15, 09:03</strong> </span></p>
</div>
</div>
<div id="comments-container-45021" class="comments-container">
&#10;</div>
<div id="comment-tools-45021" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45021-form-container" class="comment-form-container">
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

<span id="45022"></span>

<div id="answer-container-45022" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-45022-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45022-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-45022-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It looks like it was <a href="https://www.openstreetmap.org/changeset/33741738#map=14/44.9226/136.4977">edited to version 2</a> about 6 hours ago and renders now, however I suspect the role for <a href="https://www.openstreetmap.org/way/368492375">this way</a> should be inner, rather than outer. Edit: I'm half asleep. Clearly it does have role "inner" already.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Sep '15, 08:38</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Sep '15, 08:41</strong> </span></p>
</div>
</div>
<div id="comments-container-45022" class="comments-container">
<span id="45024"></span>
<div id="comment-45024" class="comment">
<div id="post-45024-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, it's starting to render at some zoom levels. What problem did the edit resolve though? How can I avoid this in the future?</p>
</div>
<div id="comment-45024-info" class="comment-info">
<span class="comment-age">(02 Sep '15, 09:04)</span> <span class="comment-user userinfo">inkatlas</span>
</div>
</div>
<span id="45026"></span>
<div id="comment-45026" class="comment">
<div id="post-45026-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I looked at the history of the relation and couldn't see anything obviously wrong. The edit seems to have been to use existing ways where possible rather than just reusing their nodes. It may be you had old tiles cached locally so just weren't seeing the render maybe?</p>
</div>
<div id="comment-45026-info" class="comment-info">
<span class="comment-age">(02 Sep '15, 09:55)</span> <span class="comment-user userinfo">EdLoach ♦</span>
</div>
</div>
</div>
<div id="comment-tools-45022" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45022-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="45023"></span>

<div id="answer-container-45023" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-45023-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45023-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-45023-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>At least at zoom level 13 it renders for me <a href="http://www.openstreetmap.org/#map=13/45.3521/136.5127">http://www.openstreetmap.org/#map=13/45.3521/136.5127</a></p>
<p>You may need to reload.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Sep '15, 08:52</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-45023" class="comments-container">
<span id="45025"></span>
<div id="comment-45025" class="comment">
<div id="post-45025-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It's starting to render at some zoom levels after a fix by another user (updated question). Not sure what they did and still want to understand what my mistake was.</p>
</div>
<div id="comment-45025-info" class="comment-info">
<span class="comment-age">(02 Sep '15, 09:05)</span> <span class="comment-user userinfo">inkatlas</span>
</div>
</div>
<span id="45027"></span>
<div id="comment-45027" class="comment">
<div id="post-45027-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>See <a href="http://nrenner.github.io/achavi/?changeset=33741738">http://nrenner.github.io/achavi/?changeset=33741738</a> for the changes.</p>
</div>
<div id="comment-45027-info" class="comment-info">
<span class="comment-age">(02 Sep '15, 11:43)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="45028"></span>
<div id="comment-45028" class="comment">
<div id="post-45028-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>If you were to have similar problems in the future, this website <a href="http://analyser.openstreetmap.fr/">http://analyser.openstreetmap.fr/</a> will analyse a multipolygon (or any relation) for you and tell you if there are any obvious errors, like openings ("ouvertures") or self-intersections.</p>
</div>
<div id="comment-45028-info" class="comment-info">
<span class="comment-age">(02 Sep '15, 11:56)</span> <span class="comment-user userinfo">joost schouppe</span>
</div>
</div>
</div>
<div id="comment-tools-45023" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45023-form-container" class="comment-form-container">
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

