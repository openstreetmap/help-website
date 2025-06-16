+++
type = "question"
title = "Retrieved Bing imagery differs between computers in JOSM"
description = '''The title really explains it all- I use JOSM on both my desktop and laptop, and noticed recently that the high-resolution (and more current) imagery that is being retrieved is differing between the two. On my laptop, I can load the available z19 imagery from 2014 in my area of interest, and that ima...'''
date = "2014-11-28T18:51:00Z"
lastmod = "2014-12-11T09:36:00Z"
weight = 38898
keywords = [ "josm", "bing", "imagery", "zoom" ]
aliases = [ "/questions/38898" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Retrieved Bing imagery differs between computers in JOSM](/questions/38898/retrieved-bing-imagery-differs-between-computers-in-josm)

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
<span id="post-38898-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-38898-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-38898-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>The title really explains it all- I use JOSM on both my desktop and laptop, and noticed recently that the high-resolution (and more current) imagery that is being retrieved is differing between the two. On my laptop, I can load the available z19 imagery from 2014 in my area of interest, and that imagery is what is reported via the imagery analyzer. On the other hand, my desktop is still loading the first batch of imagery from an unknown date: it doesn't report any imagery data on the tile. I've tried fresh "installs" of JOSM on both tries by dumping the imagery cache and the JOSM install data location in AppData, to no avail.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-bing" rel="tag" title="see questions tagged &#39;bing&#39;">bing</span> <span class="post-tag tag-link-imagery" rel="tag" title="see questions tagged &#39;imagery&#39;">imagery</span> <span class="post-tag tag-link-zoom" rel="tag" title="see questions tagged &#39;zoom&#39;">zoom</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Nov '14, 18:51</strong></p>
<img src="https://secure.gravatar.com/avatar/96c800bb494c1a15777fcdfa5a062467?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="YamaOfParadise&#39;s gravatar image" />
<p><span>YamaOfParadise</span><br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="YamaOfParadise has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-38898" class="comments-container">
<span id="38899"></span>
<div id="comment-38899" class="comment">
<div id="post-38899-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Could you please compare the "Imagery providers" (Preferences-&gt;Imagery Preferences, Imagery providers tab-&gt; Selected entries) from both JOSM installs? In my JOSM installation, the Imagery URL is tms[19]:https://{switch:a,b,c}.tile.openstreetmap.org/{zoom}/{x}/{y}.png</p>
<p>You might also want to clear the "Tile Cache Directory" specified in preferences : Preferences-&gt;Imagery Preferences, Settings tab, Tile cache directory.</p>
</div>
<div id="comment-38899-info" class="comment-info">
<span class="comment-age">(28 Nov '14, 19:24)</span> <span class="comment-user userinfo">BlueTiger</span>
</div>
</div>
<span id="38911"></span>
<div id="comment-38911" class="comment">
<div id="post-38911-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Well, I'm talking about the Bing imagery; the url is bing[22]:<a href="http://www.bing.com/maps/">http://www.bing.com/maps/</a> . That's the same URL on both installations. I've dumped the Cache a number of times as well.</p>
</div>
<div id="comment-38911-info" class="comment-info">
<span class="comment-age">(29 Nov '14, 00:53)</span> <span class="comment-user userinfo">YamaOfParadise</span>
</div>
</div>
<span id="38913"></span>
<div id="comment-38913" class="comment">
<div id="post-38913-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/10071/yamaofparadise">@YamaOfParadise</a>, that is strange. In my JOSM installation, the Bing imagery URL is same as you specified and I can go to zoom level 19 without problems.</p>
</div>
<div id="comment-38913-info" class="comment-info">
<span class="comment-age">(29 Nov '14, 04:43)</span> <span class="comment-user userinfo">BlueTiger</span>
</div>
</div>
<span id="39211"></span>
<div id="comment-39211" class="comment">
<div id="post-39211-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I don't remember the details but I think that JOSM used two different locations for the images cache. Perhaps you are still using one old location. The best would be to test your new "fresh" install with a new preference settings file.</p>
</div>
<div id="comment-39211-info" class="comment-info">
<span class="comment-age">(11 Dec '14, 09:36)</span> <span class="comment-user userinfo">Pieren</span>
</div>
</div>
</div>
<div id="comment-tools-38898" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-38898-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

