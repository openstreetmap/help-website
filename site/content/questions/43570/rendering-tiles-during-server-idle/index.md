+++
type = "question"
title = "Rendering tiles during server idle"
description = '''Rendering tiles during server idle I haven&#x27;t found any related question so far, so I am now going to ask in this QA. I have a tile server configured using mapnik / renderd / mod_tile / apache and postgresql and most of the time the machine remains idle. But when a user requests a not cached tile or ...'''
date = "2015-06-15T13:19:00Z"
lastmod = "2015-06-17T17:05:00Z"
weight = 43570
keywords = [ "rendering" ]
aliases = [ "/questions/43570" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Rendering tiles during server idle](/questions/43570/rendering-tiles-during-server-idle)

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
<span id="post-43570-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43570-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-43570-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Rendering tiles during server idle</p>
<p>I haven't found any related question so far, so I am now going to ask in this QA.</p>
<p>I have a tile server configured using mapnik / renderd / mod_tile / apache and postgresql and most of the time the machine remains idle. But when a user requests a not cached tile or more likely a bunch of new tiles it takes the machine a couple of seconds to render them. As I intend to not update my osm database that often, I think it would be a performance gain if the server spawns a process that renders and caches some tiles during the idle time. As I don't need to update my database that often and I just have a single country in my database, the cachesize would certainly stay in a small gigabyte range. Does any of the programs I use (e.g. mod_tile) provide such a function or is there any other way the idle rendering task could be done?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Jun '15, 13:19</strong></p>
<img src="https://secure.gravatar.com/avatar/1d65bc251f62664c2af0a1b6cd0f2170?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ltsstar&#39;s gravatar image" />
<p><span>ltsstar</span><br />
<span class="score" title="66 reputation points">66</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ltsstar has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-43570" class="comments-container">
&#10;</div>
<div id="comment-tools-43570" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43570-form-container" class="comment-form-container">
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

<span id="43598"></span>

<div id="answer-container-43598" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43598-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43598-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-43598-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="ltsstar has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you were to change from <code>renderd</code> to <code>tirex</code>, then you can use <code>tirex-batch</code> to batch render tiles even when no-one is looking at them. This means that while your server is idle, it'll be rendering and saving tiles, and if someone requests a tile later, that prerendered tile will be returned, rather than on-the-fly calculation.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Jun '15, 17:05</strong></p>
<img src="https://secure.gravatar.com/avatar/16e12e337f6edc3750681492656097ed?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rorym&#39;s gravatar image" />
<p><span>rorym</span><br />
<span class="score" title="5358 reputation points"><span>5.4k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="49 badges"><span class="silver">●</span><span class="badgecount">49</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rorym has 18 accepted answers">11%</span></p>
</div>
</div>
<div id="comments-container-43598" class="comments-container">
&#10;</div>
<div id="comment-tools-43598" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43598-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="43574"></span>

<div id="answer-container-43574" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43574-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43574-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-43574-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I couldn't find renderd instructions on the wiki, but the alternative <a href="https://wiki.openstreetmap.org/wiki/Tirex">tirex</a> backend performs the same task of handling rendering jobs queues. In principle, all you need to do is start a <a href="https://wiki.openstreetmap.org/wiki/Tirex/Commands/tirex-batch">batch-rendering</a> of the tiles you want, using a low priority so that it doesn't interfere with live browser requests. See also <a href="https://wiki.openstreetmap.org/wiki/Tirex/Tile_Update_Strategies">update strategies</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Jun '15, 17:47</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Jun '15, 17:08</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-43574" class="comments-container">
&#10;</div>
<div id="comment-tools-43574" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43574-form-container" class="comment-form-container">
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

