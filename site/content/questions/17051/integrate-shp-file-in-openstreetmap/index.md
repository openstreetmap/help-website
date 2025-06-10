+++
type = "question"
title = "integrate shp file in openstreetmap"
description = '''Hello,  I downloaded datas from Openstreetmap about train stations in France (RER network around Paris). I used http://download.geofabrik.de/openstreetmap in order to do it. I discovered that those datas wasn&#x27;t filled up. Some train stations was missing. Then, I completed those datas with the ArcGis...'''
date = "2012-10-20T12:46:00Z"
lastmod = "2020-06-05T20:24:00Z"
weight = 17051
keywords = [ "shp" ]
aliases = [ "/questions/17051" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [integrate shp file in openstreetmap](/questions/17051/integrate-shp-file-in-openstreetmap)

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
<span id="post-17051-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17051-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-17051-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I downloaded datas from Openstreetmap about train stations in France (RER network around Paris). I used <a href="http://download.geofabrik.de/openstreetmap">http://download.geofabrik.de/openstreetmap</a> in order to do it. I discovered that those datas wasn't filled up. Some train stations was missing.</p>
<p>Then, I completed those datas with the ArcGis software.</p>
<p>Now I have a shp file with the name of each RER station and the name of the train line corresponding (RER A, RER B, RER C, RER D, RER E).</p>
<p>I would like to update the datas on openstreetmap. Is that possible to integrate datas in shp format from arcgis to Openstreetmap in one time?</p>
<p>Thanks everybody</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-shp" rel="tag" title="see questions tagged &#39;shp&#39;">shp</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Oct '12, 12:46</strong></p>
<img src="https://secure.gravatar.com/avatar/b82d78194e3ddb26b4ac32de31046aaa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dizzy84&#39;s gravatar image" />
<p><span>Dizzy84</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dizzy84 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-17051" class="comments-container">
<span id="17053"></span>
<div id="comment-17053" class="comment">
<div id="post-17053-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>When you say "Then, I completed those datas with the ArcGis software" where did you get the information about the location about the missing stations from? Did you go out and survey them, or get the information from some other source? See <a href="http://wiki.openstreetmap.org/wiki/FAQ#Why_don.27t_you_just_use_Google_Maps.2Fwhoever_for_your_data.3F">the wiki</a> for more info.</p>
</div>
<div id="comment-17053-info" class="comment-info">
<span class="comment-age">(20 Oct '12, 13:43)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-17051" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17051-form-container" class="comment-form-container">
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

<span id="17052"></span>

<div id="answer-container-17052" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17052-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17052-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-17052-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can use the <a href="http://esriosmeditor.codeplex.com/">ArcGIS Editor for OpenStreetMap</a> plugin for working with osm data in ArcGIS.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Oct '12, 13:35</strong></p>
<img src="https://secure.gravatar.com/avatar/f7f8127223bd00c9e8f569ce2e9ddf22?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RM87&#39;s gravatar image" />
<p><span>RM87</span><br />
<span class="score" title="3346 reputation points"><span>3.3k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="37 badges"><span class="silver">●</span><span class="badgecount">37</span></span><span title="53 badges"><span class="bronze">●</span><span class="badgecount">53</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RM87 has 20 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-17052" class="comments-container">
&#10;</div>
<div id="comment-tools-17052" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17052-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="75154"></span>

<div id="answer-container-75154" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-75154-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75154-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-75154-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>SE PUEDE HACER LO MISMO USANDO QGIS?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Jun '20, 20:24</strong></p>
<img src="https://secure.gravatar.com/avatar/a8198d9ed75a5f120d4702e616ca4ed0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H%C3%A9ctor%20Eudes%20Almeida%20Mac%C3%ADas&#39;s gravatar image" />
<p><span>Héctor Eudes...</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Héctor Eudes Almeida Macías has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-75154" class="comments-container">
&#10;</div>
<div id="comment-tools-75154" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75154-form-container" class="comment-form-container">
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

