+++
type = "question"
title = "Error using renderd"
description = '''Hey guys I was following this guide to setup my own tile server. Today I finished my import of europe. After starting renderd I got the following messages:  renderd[19189]: Loading parameterization function for renderd[19189]: Loading parameterization function for renderd[19189]: Loading parameteriz...'''
date = "2017-09-14T13:59:00Z"
lastmod = "2017-09-14T16:51:00Z"
weight = 59629
keywords = [ "rendering", "renderd", "mapnik", "mod_tile" ]
aliases = [ "/questions/59629" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Error using renderd](/questions/59629/error-using-renderd)

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
<span id="post-59629-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-59629-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-59629-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hey guys I was following <a href="https://switch2osm.org/manually-building-a-tile-server-16-04-2-lts/">this</a> guide to setup my own tile server.</p>
<p>Today I finished my import of europe. After starting renderd I got the following messages:</p>
<pre><code>renderd[19189]: Loading parameterization function for
renderd[19189]: Loading parameterization function for renderd[19189]: Loading parameterization function for
&#10;renderd[19189]: An error occurred while loading the map layer &#39;default&#39;: failed to parse image-filters: &#39;scale-hsla(0,1,0,1,0.6,0.95,0                                                                                                                                         ,1)&#39; in style &#39;landcover-low-zoom-low-zoom&#39; in Style at line 376 of &#39;/opt/openstreetmap-carto/mapnik.xml&#39;
renderd[19189]: An error occurred while loading the map layer &#39;default&#39;: failed to parse image-filters: &#39;scale-hsla(0,1,0,1,0.6,0.95,0                                                                                                                                         ,1)&#39; in style &#39;landcover-low-zoom-low-zoom&#39; in Style at line 376 of &#39;/opt/openstreetmap-carto/mapnik.xml&#39;
renderd[19189]: An error occurred while loading the map layer &#39;default&#39;: failed to parse image-filters: &#39;scale-hsla(0,1,0,1,0.6,0.95,0                                                                                                                                         ,1)&#39; in style &#39;landcover-low-zoom-low-zoom&#39; in Style at line 376 of &#39;/opt/openstreetmap-carto/mapnik.xml&#39;
renderd[19189]: An error occurred while loading the map layer &#39;default&#39;: failed to parse image-filters: &#39;scale-hsla(0,1,0,1,0.6,0.95,0                                                                                                                                         ,1)&#39; in style &#39;landcover-low-zoom-low-zoom&#39; in Style at line 376 of &#39;/opt/openstreetmap-carto/mapnik.xml&#39;</code></pre>
<p>If I hit my URL I get this messages:</p>
<pre><code>renderd[19189]: DEBUG: Got incoming connection, fd 8, number 1
renderd[19189]: DEBUG: Got incoming request with protocol version 2
renderd[19189]: DEBUG: Got command RenderPrio fd(8) xml(default), z(0), x(0), y(0), mime(image/png), options()
renderd[19189]: Received request for map layer &#39;default&#39; which failed to load
renderd[19189]: DEBUG: Sending render cmd(4 default 0/0/0) with protocol version 2 to fd 8
renderd[19189]: DEBUG: Failed to read cmd on fd 8
renderd[19189]: DEBUG: Connection 0, fd 8 closed, now 0 left</code></pre>
<p>For now I have no Idea what the error could be. Or if the errors are related. Hopefully someone can help me here.</p>
<p>Thanks in advance Dominic</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-mod_tile" rel="tag" title="see questions tagged &#39;mod_tile&#39;">mod_tile</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Sep '17, 13:59</strong></p>
<img src="https://secure.gravatar.com/avatar/f2ff5fbe76b699a58bc64acd0ccb8cb6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nevyen&#39;s gravatar image" />
<p><span>Nevyen</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nevyen has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-59629" class="comments-container">
<span id="59630"></span>
<div id="comment-59630" class="comment">
<div id="post-59630-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Obviously "failed to parse image-filters" isn't "normal" - it suggests that mapnik is confused. What OS and version are you using, and did mapnik come via "apt-get" or some other method?</p>
</div>
<div id="comment-59630-info" class="comment-info">
<span class="comment-age">(14 Sep '17, 14:23)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="59632"></span>
<div id="comment-59632" class="comment">
<div id="post-59632-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>OS is Debian 8. We installed Mapnik 2.2 via apt-get.</p>
</div>
<div id="comment-59632-info" class="comment-info">
<span class="comment-age">(14 Sep '17, 16:24)</span> <span class="comment-user userinfo">Nevyen</span>
</div>
</div>
</div>
<div id="comment-tools-59629" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-59629-form-container" class="comment-form-container">
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

<span id="59634"></span>

<div id="answer-container-59634" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-59634-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-59634-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-59634-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you're using Mapnik 2.2, you'll need to use a map style that supports it, or an old version of a current map style that supported Mapnik 2.2 at some time in the past.</p>
<p>Back before various node.js stuff was fixed to work, the switch2osm instructions used to say something like:</p>
<pre><code>git checkout `git rev-list -n 1 --before=&quot;2016-11-28 00:00&quot; master`</code></pre>
<p>that gets a version of the style from late November 2016, and I think that's the latest date that you don't need a bleeding edge carto for, and with a bit of luck it might work on Mapnik 2.2. Never tried it on Debian 8 myself, though.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Sep '17, 16:48</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-59634" class="comments-container">
<span id="59635"></span>
<div id="comment-59635" class="comment">
<div id="post-59635-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I will check this out tomorrow when I have access to the server. Thanks for this hint.</p>
</div>
<div id="comment-59635-info" class="comment-info">
<span class="comment-age">(14 Sep '17, 16:51)</span> <span class="comment-user userinfo">Nevyen</span>
</div>
</div>
</div>
<div id="comment-tools-59634" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-59634-form-container" class="comment-form-container">
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

