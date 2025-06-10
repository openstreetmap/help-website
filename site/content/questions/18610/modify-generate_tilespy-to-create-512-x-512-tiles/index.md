+++
type = "question"
title = "modify generate_tiles.py to create 512 x 512 tiles?"
description = '''Hey folks, I&#x27;m wanting to mod generate_tiles.py to create 512 x 512 tiles. Googling around, I found this lonesome question, unanswered on a forum, but I share that poster&#x27;s concern about blinding changing all 256&#x27;s to 512&#x27;s. Afterall, I see 256&#x27;s in places throughout the file that seem unrelated to ...'''
date = "2012-12-19T14:56:00Z"
lastmod = "2013-01-30T14:17:00Z"
weight = 18610
keywords = [ "python", "generate_tiles", "mapnik" ]
aliases = [ "/questions/18610" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [modify generate_tiles.py to create 512 x 512 tiles?](/questions/18610/modify-generate_tilespy-to-create-512-x-512-tiles)

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
<span id="post-18610-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18610-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-18610-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hey folks, I'm wanting to mod <code>generate_tiles.py</code> to create 512 x 512 tiles. Googling around, I <a href="http://forum.openstreetmap.org/viewtopic.php?id=13799">found this lonesome question</a>, unanswered on a forum, but I share that poster's concern about blinding changing all 256's to 512's. Afterall, I see 256's in places throughout the file that <em>seem</em> unrelated to the tile size---like in the projection values and in the image type.</p>
<p>I could start a round of trial-an-error, changing 256's to 512's based on relatively-educated guesses, but I thought I'd poll the community first. Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-python" rel="tag" title="see questions tagged &#39;python&#39;">python</span> <span class="post-tag tag-link-generate_tiles" rel="tag" title="see questions tagged &#39;generate_tiles&#39;">generate_tiles</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Dec '12, 14:56</strong></p>
<img src="https://secure.gravatar.com/avatar/0bda1cf1a41b6d91ad2f3c5a88d059a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="elrobis&#39;s gravatar image" />
<p><span>elrobis</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="elrobis has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-18610" class="comments-container">
<span id="19440"></span>
<div id="comment-19440" class="comment">
<div id="post-19440-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>(as you've probably done the "trial and error" by now)</p>
<p>Did it work?</p>
</div>
<div id="comment-19440-info" class="comment-info">
<span class="comment-age">(30 Jan '13, 12:25)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="19445"></span>
<div id="comment-19445" class="comment">
<div id="post-19445-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Here is the url btw: <a href="http://svn.openstreetmap.org/applications/rendering/mapnik/generate_tiles.py">http://svn.openstreetmap.org/applications/rendering/mapnik/generate_tiles.py</a></p>
<p>I managed to get it working way back, but if it's hard you can have a look at generate_image.py in the same directory to see how to render images of arbitrary size. (I guess someone(else) should update that code to use render_size globaly)</p>
</div>
<div id="comment-19445-info" class="comment-info">
<span class="comment-age">(30 Jan '13, 14:17)</span> <span class="comment-user userinfo">emj</span>
</div>
</div>
</div>
<div id="comment-tools-18610" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18610-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

