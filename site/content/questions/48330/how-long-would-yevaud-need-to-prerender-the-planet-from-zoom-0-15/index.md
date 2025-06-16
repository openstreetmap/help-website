+++
type = "question"
title = "How long would yevaud need to prerender the planet from zoom 0-15?"
description = '''I&#x27;m about to setup a tile server or find some alternatives.  One of the alternatives would be prerendering the tiles and downloading the images. Therefore it would be helpful to know how long (approx.) a server like yevaud would need to prerender the planets Tiles via render_list from zoom 0 to zoom...'''
date = "2016-02-24T15:07:00Z"
lastmod = "2016-03-03T14:09:00Z"
weight = 48330
keywords = [ "render_list", "rendering", "yevaud" ]
aliases = [ "/questions/48330" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How long would yevaud need to prerender the planet from zoom 0-15?](/questions/48330/how-long-would-yevaud-need-to-prerender-the-planet-from-zoom-0-15)

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
<span id="post-48330-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48330-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-48330-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm about to setup a tile server or find some alternatives.</p>
<p>One of the alternatives would be prerendering the tiles and downloading the images. Therefore it would be helpful to know how long (approx.) a server like yevaud would need to prerender the planets Tiles via render_list from zoom 0 to zoom 15?</p>
<p>Also: In my estimations, I would need a large amount of disk space (4TB?). True?</p>
<p>I once prerendered the planet from 0-10 on a really low-performance system and it took nearly 3 weeks. I was wondering if this is normal or if my hardware was just too limited (low memory, no ssd)</p>
<p><a href="https://hardware.openstreetmap.org/servers/yevaud.openstreetmap.org/">https://hardware.openstreetmap.org/servers/yevaud.openstreetmap.org/</a></p>
<p>Thanks in advance! :)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-render_list" rel="tag" title="see questions tagged &#39;render_list&#39;">render_list</span> <span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-yevaud" rel="tag" title="see questions tagged &#39;yevaud&#39;">yevaud</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Feb '16, 15:07</strong></p>
<img src="https://secure.gravatar.com/avatar/e6ebf8e9d8721aa0d3a7ec0f3dc60c44?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ChrizMas&#39;s gravatar image" />
<p><span>ChrizMas</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ChrizMas has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-48330" class="comments-container">
<span id="48417"></span>
<div id="comment-48417" class="comment">
<div id="post-48417-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Well, there's <a href="https://wiki.openstreetmap.org/wiki/Tile_disk_usage">https://wiki.openstreetmap.org/wiki/Tile_disk_usage</a> , which also includes tile counts - note that at zoom 15, only about a quarter of those tiles has ever been requested (what with most of planet surface being an ocean etc.). Three weeks on a toaster sounds reasonable.</p>
</div>
<div id="comment-48417-info" class="comment-info">
<span class="comment-age">(29 Feb '16, 16:06)</span> <span class="comment-user userinfo">Piskvor</span>
</div>
</div>
<span id="48483"></span>
<div id="comment-48483" class="comment">
<div id="post-48483-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for you response!</p>
<p>Yeah, I used these numbers for my disk space estimation. An alternative would be a "Pre-rendering-Server" in the cloud. But I really don't know how long the pre-rendering would take on a really strong EC2 instance (e.g. i2). Therefore I can't really estimate costs, etc.</p>
<p>Guess I just have to try it once.</p>
</div>
<div id="comment-48483-info" class="comment-info">
<span class="comment-age">(03 Mar '16, 14:09)</span> <span class="comment-user userinfo">ChrizMas</span>
</div>
</div>
</div>
<div id="comment-tools-48330" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48330-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

