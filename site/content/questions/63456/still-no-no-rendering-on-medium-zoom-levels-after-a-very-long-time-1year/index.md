+++
type = "question"
title = "Still no no rendering on medium zoom levels after a very long time (&gt;1year)?"
description = '''Hi, I have a question about the rendering of a piece of forest in Sweden https://www.openstreetmap.org/#map=13/57.0787/13.0526 At zoom level 11 there are large white patches, at level 12 one patch is filled with forest, at level 13 the rest is filled-in. Apparently the forest data is available, but ...'''
date = "2018-05-14T08:58:00Z"
lastmod = "2018-05-15T17:00:00Z"
weight = 63456
keywords = [ "zoomlevel", "rendering" ]
aliases = [ "/questions/63456" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Still no no rendering on medium zoom levels after a very long time (\>1year)?](/questions/63456/still-no-no-rendering-on-medium-zoom-levels-after-a-very-long-time-1year)

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
<span id="post-63456-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63456-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-63456-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I have a question about the rendering of a piece of forest in Sweden <a href="https://www.openstreetmap.org/#map=13/57.0787/13.0526">https://www.openstreetmap.org/#map=13/57.0787/13.0526</a> At zoom level 11 there are large white patches, at level 12 one patch is filled with forest, at level 13 the rest is filled-in. Apparently the forest data is available, but has not surfaced to zoom levels 12 and lower. As I understand, zoom levels 12 and less are rendered less often. However, I have observed this phenomenon for as long as I can remember (at least 2 years), and tile.openstreetmap.org says the tile was rendered last week. (<a href="https://a.tile.openstreetmap.org/12/2196/1253.png/status)">https://a.tile.openstreetmap.org/12/2196/1253.png/status)</a> "Tile is clean. Last rendered at Sun May 06 21:12:08 2018. Last accessed at Sun May 13 07:58:00 2018. Stored in file:///srv/tile.openstreetmap.org/tiles/default/12/0/0/132/158/0.meta (Dates might not be accurate. Rendering time might be reset to an old date for tile expiry. Access times might not be updated on all file systems)" This does not seem to be correct since the forest visible on higher zoom levels was already there then.</p>
<p>When I request the status of the tile, it says the tile is clean. When I force the tile dirty, it is still reported clean.</p>
<p>Why is the data not rendered at the lower zoom levels after more than a year and how do I successfully force a re-render of a tile? Or is there a parameter which limits the rendering of an item to specified higher zoom levels? Please enlighten me.</p>
<p>Best regards, Paul van der Hulst</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-zoomlevel" rel="tag" title="see questions tagged &#39;zoomlevel&#39;">zoomlevel</span> <span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 May '18, 08:58</strong></p>
<img src="https://secure.gravatar.com/avatar/7da043110f398d01e59c0ac245446d77?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Paultjevdh&#39;s gravatar image" />
<p><span>Paultjevdh</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Paultjevdh has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 May '18, 18:20</strong> </span></p>
</div>
</div>
<div id="comments-container-63456" class="comments-container">
<span id="63477"></span>
<div id="comment-63477" class="comment">
<div id="post-63477-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I cannot answer with any certainty, but I note that</p>
<ul>
<li><p>The forest multipolygons in the area have been edited quite recently.</p></li>
<li><p>In a database import I did some weeks ago, using my own import tool which is rather picky about multipolygon correctness, those relations have no geometry (i.e, the importer choked on them).</p></li>
<li><p>In a DB import from today, they have geometry.</p></li>
</ul>
<p>So maybe there was a problem with the geometry which has very recently been fixed, and not yet picked up by the renderer for lower zoom levels.</p>
</div>
<div id="comment-63477-info" class="comment-info">
<span class="comment-age">(14 May '18, 20:29)</span> <span class="comment-user userinfo">turepalsson</span>
</div>
</div>
<span id="63486"></span>
<div id="comment-63486" class="comment">
<div id="post-63486-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>(Actually, on a closer look it turns out that the two multipolygons I checked (relations 8286925 and 8286775) were only created five days ago.)</p>
</div>
<div id="comment-63486-info" class="comment-info">
<span class="comment-age">(15 May '18, 08:57)</span> <span class="comment-user userinfo">turepalsson</span>
</div>
</div>
<span id="63488"></span>
<div id="comment-63488" class="comment">
<div id="post-63488-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi Ture, Thanks for your info. Do you also understand why I cannot mark tiles dirty? Best regards, Paul</p>
</div>
<div id="comment-63488-info" class="comment-info">
<span class="comment-age">(15 May '18, 14:02)</span> <span class="comment-user userinfo">Paultjevdh</span>
</div>
</div>
<span id="63490"></span>
<div id="comment-63490" class="comment">
<div id="post-63490-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>No, on that I have no clue.</p>
</div>
<div id="comment-63490-info" class="comment-info">
<span class="comment-age">(15 May '18, 17:00)</span> <span class="comment-user userinfo">turepalsson</span>
</div>
</div>
</div>
<div id="comment-tools-63456" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63456-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

