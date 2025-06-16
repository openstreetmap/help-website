+++
type = "question"
title = "Is it possible to make sure Mapnik (2.2) allways render complete tiles?"
description = '''Hi I have imported whole europe into database.  When I select a bounding box that covers whole norway, and start pre-rendering the tiles, I see that last tile(s) vertically within the bounding box only get the map renderd in it&#x27;s upper part.  It looks like this:  I would like to be able to render ma...'''
date = "2018-08-09T15:15:00Z"
lastmod = "2018-08-22T22:33:00Z"
weight = 65238
keywords = [ "tiles", "render", "mapnik" ]
aliases = [ "/questions/65238" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Is it possible to make sure Mapnik (2.2) allways render complete tiles?](/questions/65238/is-it-possible-to-make-sure-mapnik-22-allways-render-complete-tiles)

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
<span id="post-65238-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65238-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65238-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi</p>
<p>I have imported whole europe into database. When I select a bounding box that covers whole norway, and start pre-rendering the tiles, I see that last tile(s) vertically within the bounding box only get the map renderd in it's upper part.</p>
<p>It looks like this:</p>
<p><img src="/upfiles/620.png" alt="alt text" /></p>
<p>I would like to be able to render map on the whole tile - the data for the map is in the database. If no map data in the database, then this partly rendered tile would be okay though.</p>
<p>This has probably to do with my values for bbox in generate_tiles.py (and extent in the xml file), which currently is like this:</p>
<p>in generate_tiles.py: <code> bbox = (3.98,57.69,32.23,71.46) </code></p>
<p>in xml file: <code> &lt;parameter name="extent"&gt;443052,7902476,3587827,11561422&lt;/parameter&gt; </code></p>
<p>So, is it possible to make sure values used for bbox and extent are such that I allways get renderd complete tiles? If so, how do I do this? If not possible to control using bbox and extent, is there any other way to handle this in Mapnik (2.2)?</p>
<p>Or perhaps there is a way to tell Mapnik to render complete tiles, as long as there is data available i database to do so?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-render" rel="tag" title="see questions tagged &#39;render&#39;">render</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Aug '18, 15:15</strong></p>
<img src="https://secure.gravatar.com/avatar/0da1f043b943c87172fb4dc60f017440?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MapViking&#39;s gravatar image" />
<p><span>MapViking</span><br />
<span class="score" title="56 reputation points">56</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MapViking has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Aug '18, 11:10</strong> </span></p>
</div>
</div>
<div id="comments-container-65238" class="comments-container">
<span id="65390"></span>
<div id="comment-65390" class="comment">
<div id="post-65390-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If someone know if there is a solution to the above question, please tell me.</p>
</div>
<div id="comment-65390-info" class="comment-info">
<span class="comment-age">(16 Aug '18, 22:58)</span> <span class="comment-user userinfo">MapViking</span>
</div>
</div>
</div>
<div id="comment-tools-65238" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65238-form-container" class="comment-form-container">
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

<span id="65519"></span>

<div id="answer-container-65519" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-65519-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65519-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65519-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I guess you will have to indicate the boundaries of your extent and bbox aligned with the tile boundaries (i.e. add some buffer to fill up the tile).</p>
<p>Update: try to be generous with the extent and add some buffer. IIRR, mapnik will render any tile that is even just partly within your bounding box (i.e. it will render usually slightly more than what you ask for), but might clip the content to the extent you provide.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Aug '18, 22:33</strong></p>
<img src="https://secure.gravatar.com/avatar/f09c0b7a655fed386e070e036e2da248?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dieterdreist&#39;s gravatar image" />
<p><span>dieterdreist</span><br />
<span class="score" title="3677 reputation points"><span>3.7k</span></span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="67 badges"><span class="bronze">●</span><span class="badgecount">67</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dieterdreist has 4 accepted answers">3%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Aug '18, 22:44</strong> </span></p>
</div>
</div>
<div id="comments-container-65519" class="comments-container">
&#10;</div>
<div id="comment-tools-65519" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65519-form-container" class="comment-form-container">
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

