+++
type = "question"
title = "Bug? Zooms 12 and below not marked dirty, so never re-rendered."
description = '''I added significant detail to a section of our city over the last couple of weeks, enough that it is visible at many zoom levels. Everything has been fully rendered at zoom levels 13 and up. Nothing re-rendered at zoom levels 12 and below. I examined the specific tile status for zoom levels 9 throug...'''
date = "2017-04-01T22:26:00Z"
lastmod = "2017-04-02T17:07:00Z"
weight = 55425
keywords = [ "rendering", "zoom", "bug" ]
aliases = [ "/questions/55425" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Bug? Zooms 12 and below not marked dirty, so never re-rendered.](/questions/55425/bug-zooms-12-and-below-not-marked-dirty-so-never-re-rendered)

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
<span id="post-55425-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55425-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-55425-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I added significant detail to a section of our city over the last couple of weeks, enough that it is visible at many zoom levels. Everything has been fully rendered at zoom levels 13 and up. Nothing re-rendered at zoom levels 12 and below. I examined the specific tile status for zoom levels 9 through 12. In all cases:</p>
<ul>
<li>The status was clean. The system doesn't believe anything has changed.</li>
<li>The last re-render was January 30th</li>
<li>If I force the tile to be dirty, it does properly re-render</li>
</ul>
<p>By any chance:</p>
<ul>
<li><p>Are zooms 0-12 done in an entirely different manner, that ignores clean/dirty status?</p></li>
<li><p>If not, I believe I've found a bug.</p></li>
</ul>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-zoom" rel="tag" title="see questions tagged &#39;zoom&#39;">zoom</span> <span class="post-tag tag-link-bug" rel="tag" title="see questions tagged &#39;bug&#39;">bug</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Apr '17, 22:26</strong></p>
<img src="https://secure.gravatar.com/avatar/5b0dc19c17a667754ccfa936bb4de2f8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MrPete&#39;s gravatar image" />
<p><span>MrPete</span><br />
<span class="score" title="56 reputation points">56</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MrPete has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Apr '17, 22:29</strong> </span></p>
</div>
</div>
<div id="comments-container-55425" class="comments-container">
&#10;</div>
<div id="comment-tools-55425" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55425-form-container" class="comment-form-container">
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

<span id="55428"></span>

<div id="answer-container-55428" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55428-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55428-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-55428-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Lower zooms are more expensive to render (there's more data per tile to consider) and are typically only (re)rendered as a batch job when the rendering style gets updated, to cut down on frequent expensive renders.</p>
<p>Can't find the reference to your specific question right now, but <a href="https://wiki.openstreetmap.org/wiki/Featured_tile_layers/Updates">Featured_tile_layers/Updates</a> and <a href="/questions/178/how-often-does-the-main-mapnik-map-get-updated">how-often-does-the-main-mapnik-map-get-updated</a> have plenty of info.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Apr '17, 23:59</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-55428" class="comments-container">
<span id="55449"></span>
<div id="comment-55449" class="comment">
<div id="post-55449-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Wow. Since render style is stable that means this really only happens manually.</p>
</div>
<div id="comment-55449-info" class="comment-info">
<span class="comment-age">(02 Apr '17, 15:13)</span> <span class="comment-user userinfo">MrPete</span>
</div>
</div>
<span id="55453"></span>
<div id="comment-55453" class="comment">
<div id="post-55453-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="https://github.com/gravitystorm/openstreetmap-carto/releases">https://github.com/gravitystorm/openstreetmap-carto/releases</a> the rendering style does get regular updates. Some releases might get skiped by openstreetmap.org's renderer but in general they're pretty close.</p>
</div>
<div id="comment-55453-info" class="comment-info">
<span class="comment-age">(02 Apr '17, 17:07)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
</div>
<div id="comment-tools-55428" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55428-form-container" class="comment-form-container">
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

