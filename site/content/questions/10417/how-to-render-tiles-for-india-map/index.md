+++
type = "question"
title = "How to render tiles for India Map"
description = '''Dear Sir, I want to render tiles for India only. I tried India coordinates in generate_tiles.py. But it does not generate tiles. Currently, generate_tiles.py contains following lines. What should I change if I need tiles for India only. bbox = (-180.0,-90.0, 180.0,90.0) render_tiles(bbox, mapfile, t...'''
date = "2012-02-05T06:08:00Z"
lastmod = "2012-02-06T11:19:00Z"
weight = 10417
keywords = [ "tiles", "india", "mapnik" ]
aliases = [ "/questions/10417" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to render tiles for India Map](/questions/10417/how-to-render-tiles-for-india-map)

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
<span id="post-10417-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10417-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-10417-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Dear Sir, I want to render tiles for India only. I tried India coordinates in <a href="http://generate_tiles.py">generate_tiles.py</a>. But it does not generate tiles. Currently, <a href="http://generate_tiles.py">generate_tiles.py</a> contains following lines. What should I change if I need tiles for India only.</p>
<p>bbox = (-180.0,-90.0, 180.0,90.0) render_tiles(bbox, mapfile, tile_dir, 0, 15, "India")</p>
<p>should required anything more to generate India Tiles ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-india" rel="tag" title="see questions tagged &#39;india&#39;">india</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Feb '12, 06:08</strong></p>
<img src="https://secure.gravatar.com/avatar/6415fd7bc63406c5ab1bc64cc29bb52a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="baban&#39;s gravatar image" />
<p><span>baban</span><br />
<span class="score" title="41 reputation points">41</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="baban has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Feb '12, 08:19</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/a2839f25c5f2da24f6ffd25de1641684?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NicolasDumoulin&#39;s gravatar image" />
<p><span>NicolasDumoulin</span><br />
<span class="score" title="3327 reputation points"><span>3.3k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span></p>
</div>
</div>
<div id="comments-container-10417" class="comments-container">
&#10;</div>
<div id="comment-tools-10417" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10417-form-container" class="comment-form-container">
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

<span id="10440"></span>

<div id="answer-container-10440" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-10440-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10440-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-10440-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>First, a correct bbox for India should be (66.4,5.2,90.5,36.2).</p>
<p>Then, which procedure have you followed for your attempt? Have you installed mapnik? Have you downloaded OSM data, and imported it into pgsql? If not, you must read the <a href="http://wiki.openstreetmap.org/wiki/Mapnik">mapnik documentation on the wiki</a>. If you're aware of that, do you have any message output by the python script that can give us some hint for helping you?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Feb '12, 08:18</strong></p>
<img src="https://secure.gravatar.com/avatar/a2839f25c5f2da24f6ffd25de1641684?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NicolasDumoulin&#39;s gravatar image" />
<p><span>NicolasDumoulin</span><br />
<span class="score" title="3327 reputation points"><span>3.3k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NicolasDumoulin has 15 accepted answers">13%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Feb '12, 11:16</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-10440" class="comments-container">
<span id="10445"></span>
<div id="comment-10445" class="comment">
<div id="post-10445-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>To add to what NicolasDumoulin said, you might find that the "serving tiles" instructions at <a href="http://switch2osm.org/">switch2osm</a> might be a little easier to follow than the various wiki pages (which might not have been written with each other in mind).</p>
</div>
<div id="comment-10445-info" class="comment-info">
<span class="comment-age">(06 Feb '12, 11:19)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-10440" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10440-form-container" class="comment-form-container">
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

