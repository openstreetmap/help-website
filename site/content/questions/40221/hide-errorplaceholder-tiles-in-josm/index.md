+++
type = "question"
title = "Hide Error/Placeholder Tiles in JOSM"
description = '''When using aerial imagery to trace detail it is often useful to &quot;overzoom&quot; past the highest resolution they offer in order to place points more precisely etc. Some sources such as Bing simply return an error message when they don&#x27;t have a zoom level allowing the previous (now blurry) zoom level to s...'''
date = "2015-01-11T16:59:00Z"
lastmod = "2017-10-01T04:13:00Z"
weight = 40221
keywords = [ "mapquest", "josm", "bing", "background", "mapbox" ]
aliases = [ "/questions/40221" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Hide Error/Placeholder Tiles in JOSM](/questions/40221/hide-errorplaceholder-tiles-in-josm)

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
<span id="post-40221-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40221-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-40221-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>When using aerial imagery to trace detail it is often useful to "overzoom" past the highest resolution they offer in order to place points more precisely etc. Some sources such as Bing simply return an error message when they don't have a zoom level allowing the previous (now blurry) zoom level to stay on the screen. Others, such as Mapbox and MapQuest show row after row, column after column of the same useless placeholder image.</p>
<p>Is there a setting or Plugin for JOSM that allows me to specify a image that should be ignored and never rendered in the background?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-mapquest" rel="tag" title="see questions tagged &#39;mapquest&#39;">mapquest</span> <span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-bing" rel="tag" title="see questions tagged &#39;bing&#39;">bing</span> <span class="post-tag tag-link-background" rel="tag" title="see questions tagged &#39;background&#39;">background</span> <span class="post-tag tag-link-mapbox" rel="tag" title="see questions tagged &#39;mapbox&#39;">mapbox</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Jan '15, 16:59</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-40221" class="comments-container">
&#10;</div>
<div id="comment-tools-40221" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40221-form-container" class="comment-form-container">
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

<span id="40224"></span>

<div id="answer-container-40224" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-40224-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40224-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-40224-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>A <em>workaround</em>: you can specify/edit the max zoom level of each imagery source in your <a href="https://josm.openstreetmap.de/wiki/Help/Preferences/Imagery">imagery preferences</a>: the number in <code>[ ]</code>. I guess you will need to re-add (to your layers list) a imagery layer to activate this setting, in case you already had bing in your <a href="https://josm.openstreetmap.de/wiki/Help/Dialog/LayerList">current layers</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Jan '15, 19:17</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Jan '15, 19:28</strong> </span></p>
</div>
</div>
<div id="comments-container-40224" class="comments-container">
<span id="40459"></span>
<div id="comment-40459" class="comment">
<div id="post-40459-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Unfortunately the max zoom for the imagery I'm most interested in varies from place to place. Time for a feature request I think.</p>
</div>
<div id="comment-40459-info" class="comment-info">
<span class="comment-age">(18 Jan '15, 11:12)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
</div>
<div id="comment-tools-40224" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40224-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="59903"></span>

<div id="answer-container-59903" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-59903-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-59903-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-59903-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Another workaround: once the highest-resolution zoom level you need is loaded, if you right-click the layer in the Layers pane and uncheck "Auto zoom" it will overzoom beyond that zoom level instead of trying to request any other tiles.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Oct '17, 04:13</strong></p>
<img src="https://secure.gravatar.com/avatar/cc964a1d9f156b67400e204cf1d0e4bf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="meetar&#39;s gravatar image" />
<p><span>meetar</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="meetar has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-59903" class="comments-container">
&#10;</div>
<div id="comment-tools-59903" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-59903-form-container" class="comment-form-container">
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

