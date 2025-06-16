+++
type = "question"
title = "[closed] Cut Labels with Mapnik"
description = '''I&#x27;m getting cut labels on my maps. Same thing is happening on the main map here: https://www.openstreetmap.org/#map=11/52.3303/-1.3774 (look between Coventry and Rugby) Anyone know how to fix them? I made a dynamic tileserver with Mapnik, renderd and Apache mod-tile. Also made a static one with Mapni...'''
date = "2014-05-26T18:20:00Z"
lastmod = "2014-05-26T18:20:00Z"
weight = 33486
keywords = [ "labels", "osm.xml", "cut", "mapnik" ]
aliases = [ "/questions/33486" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] Cut Labels with Mapnik](/questions/33486/cut-labels-with-mapnik)

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
<span id="post-33486-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33486-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-33486-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm getting cut labels on my maps. Same thing is happening on the main map here:</p>
<p><a href="https://www.openstreetmap.org/#map=11/52.3303/-1.3774">https://www.openstreetmap.org/#map=11/52.3303/-1.3774</a></p>
<p>(look between Coventry and Rugby)</p>
<p>Anyone know how to fix them?</p>
<p>I made a dynamic tileserver with Mapnik, renderd and Apache mod-tile. Also made a static one with Mapnik and generate_tiles.py to make the tiles. Same thing is happening in both cases.</p>
<p>Did some research and discovered that the problem is caused by not having a buffer around the rendered tiles. So I stated a buffer size in my main xml style file (osm.xml):</p>
<p>&lt;Map background-color="#b5d0d0" buffer-size="128" srs="&amp;srs900913;" minimum-version="2.0.0"&gt;</p>
<p>Did so for the dynamic and the static servers. Made no difference. Tried different sizes for the buffer: 256, 1024, made no difference. I know osm.xml is being loaded because every time I edit it I change the background colour and I can see the new colour in newly rendered tiles.</p>
<p>So Mapnik is reading osm.xml but apparently ignoring the buffer size. Why so?</p>
<p>Thank you.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-labels" rel="tag" title="see questions tagged &#39;labels&#39;">labels</span> <span class="post-tag tag-link-osm.xml" rel="tag" title="see questions tagged &#39;osm.xml&#39;">osm.xml</span> <span class="post-tag tag-link-cut" rel="tag" title="see questions tagged &#39;cut&#39;">cut</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 May '14, 18:20</strong></p>
<img src="https://secure.gravatar.com/avatar/11e6e819b91b4d177c249c5123d2fa15?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Charles%20Sweeney&#39;s gravatar image" />
<p><span>Charles Sweeney</span><br />
<span class="score" title="101 reputation points">101</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Charles Sweeney has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>26 May '14, 18:49</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-33486" class="comments-container">
&#10;</div>
<div id="comment-tools-33486" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33486-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Duplicate Question (https://help.openstreetmap.org/questions/33485/cut-labels-with-mapnik)" by scai 26 May '14, 18:49

</div>

</div>

</div>

