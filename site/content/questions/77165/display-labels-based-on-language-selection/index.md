+++
type = "question"
title = "Display labels based on language selection"
description = '''Hi team, While using OSM background tiles, can we make the display of tiles based on the language selection like all labels in French, Russian etc. Also is it possible to display labels only in English ignoring localization. Regards, Pavan'''
date = "2020-10-20T05:43:00Z"
lastmod = "2020-10-20T08:58:00Z"
weight = 77165
keywords = [ "tiles", "labels", "localization", "english" ]
aliases = [ "/questions/77165" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Display labels based on language selection](/questions/77165/display-labels-based-on-language-selection)

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
<span id="post-77165-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77165-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-77165-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi team, While using OSM background tiles, can we make the display of tiles based on the language selection like all labels in French, Russian etc. Also is it possible to display labels only in English ignoring localization. Regards, Pavan</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-labels" rel="tag" title="see questions tagged &#39;labels&#39;">labels</span> <span class="post-tag tag-link-localization" rel="tag" title="see questions tagged &#39;localization&#39;">localization</span> <span class="post-tag tag-link-english" rel="tag" title="see questions tagged &#39;english&#39;">english</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Oct '20, 05:43</strong></p>
<img src="https://secure.gravatar.com/avatar/544b35794331e70f878f253e86f1a432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pavan%20Kumar%20J&#39;s gravatar image" />
<p><span>Pavan Kumar J</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pavan Kumar J has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-77165" class="comments-container">
&#10;</div>
<div id="comment-tools-77165" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77165-form-container" class="comment-form-container">
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

<span id="77167"></span>

<div id="answer-container-77167" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-77167-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77167-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-77167-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you are using pre-rendered raster tiles, you are stuck with whatever your provider chose to show.</p>
<p>If you are using <a href="https://wiki.openstreetmap.org/wiki/Vector_tiles">vector tiles</a> then it may be possible to configure them to display another label depending on who has produced them.</p>
<p>In terms of raw data if you're creating your own tiles, the name of an object is normally recorded in the <a href="https://wiki.openstreetmap.org/wiki/Key:name"><code>name</code></a> tag in the local language or according to local convention if there are multiple local languages. Names in specific languages are recorded in separate tags identified by the ISO language code e.g. <code>name:en</code>. These tags are not always present so you will need some form of fallback in case the English name is not recorded anywhere. See the <a href="https://wiki.openstreetmap.org/wiki/Multilingual_names">multilingual names</a> page on the wiki for more information.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Oct '20, 08:39</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-77167" class="comments-container">
&#10;</div>
<div id="comment-tools-77167" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77167-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="77168"></span>

<div id="answer-container-77168" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-77168-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77168-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-77168-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are several projects that use not the local language for a region, but display all labels (if existent) in English, French, etc. Some of them also use transcribing of local names. I don't know of an example showing only Russian labels worldwide, but for a selection of European languages you'll find examples through <a href="https://www.osmap.info"></a><a href="https://www.osmap.info">https://www.osmap.info</a> for raster tiles.</p>
<p>See <a href="https://wiki.openstreetmap.org/wiki/Map_internationalization">https://wiki.openstreetmap.org/wiki/Map_internationalization</a> for more info and a list of vector and raster tiles with non-local labeling.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Oct '20, 08:58</strong></p>
<img src="https://secure.gravatar.com/avatar/e06ed329df6032df14b5639de4d64782?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Spiekerooger&#39;s gravatar image" />
<p><span>Spiekerooger</span><br />
<span class="score" title="3148 reputation points"><span>3.1k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Spiekerooger has 18 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Oct '20, 09:10</strong> </span></p>
</div>
</div>
<div id="comments-container-77168" class="comments-container">
&#10;</div>
<div id="comment-tools-77168" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77168-form-container" class="comment-form-container">
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

