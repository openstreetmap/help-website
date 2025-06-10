+++
type = "question"
title = "rendering performance very slow with zoomlevel &gt; 9"
description = '''Hi there @all I tried to setup an experimental tile server hosting only Germany using the following instructions: https://switch2osm.org/serving-tiles/manually-building-a-tile-server-ubuntu-22-04-lts/ Everything works fine in general, but when I try to access a tile with zoomlevel &amp;gt; 9 (10/0/0 e.g...'''
date = "2022-10-31T08:06:00Z"
lastmod = "2022-10-31T08:06:00Z"
weight = 86029
keywords = [ "performance", "renderd", "mod_tile" ]
aliases = [ "/questions/86029" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [rendering performance very slow with zoomlevel \> 9](/questions/86029/rendering-performance-very-slow-with-zoomlevel-9)

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
<span id="post-86029-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86029-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86029-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi there <a href="https://help.openstreetmap.org/users/16165/allain117">@all</a></p>
<p>I tried to setup an experimental tile server hosting only Germany using the following instructions: <a href="https://switch2osm.org/serving-tiles/manually-building-a-tile-server-ubuntu-22-04-lts/">https://switch2osm.org/serving-tiles/manually-building-a-tile-server-ubuntu-22-04-lts/</a></p>
<p>Everything works fine in general, but when I try to access a tile with zoomlevel &gt; 9 (10/0/0 e.g.), the rendering time increases from around 0.5s up to &gt; 100s.</p>
<p><img src="https://help.openstreetmap.org/upfiles/RenderD_Logs_fFu6KYx.PNG" alt="alt text" /></p>
<p>My server specs are</p>
<ol>
<li>6 vCore Processor</li>
<li>12GB RAM, Swapping enabled with 2GB</li>
<li>240GB SSD, currently ~42% in use with data for whole Germany</li>
</ol>
<p>Compared to the minimum requirements mentioned to host data for the whole world, I thought this could be enough for having only a few users around the day.</p>
<p>Does anyone have an idea for the cause of this huge performance step? Or is it simply far too much load for this server spec?</p>
<p>Currently, I consider pre-rendering tiles up to zoomlevel 15 for Germany using render_tiles_geo.pl script.</p>
<p>Best Sebastian</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-performance" rel="tag" title="see questions tagged &#39;performance&#39;">performance</span> <span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span> <span class="post-tag tag-link-mod_tile" rel="tag" title="see questions tagged &#39;mod_tile&#39;">mod_tile</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 Oct '22, 08:06</strong></p>
<img src="https://secure.gravatar.com/avatar/f3d9da942a1ac078cdc4167d359ff9a5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sebastianknopf&#39;s gravatar image" />
<p><span>sebastianknopf</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sebastianknopf has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-86029" class="comments-container">
&#10;</div>
<div id="comment-tools-86029" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86029-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

