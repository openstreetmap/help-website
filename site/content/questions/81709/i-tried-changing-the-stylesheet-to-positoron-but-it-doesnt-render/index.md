+++
type = "question"
title = "I tried changing the stylesheet to Positoron, but it doesn&#x27;t render."
description = '''I have done all the steps as described in this guide and confirmed that it works fine. Note that since naciscdn.org is down, I have replaced the relevant part of external-data.yml with the following description. https://naturalearth.s3.amazonaws.com/110m_cultural/ne_110m_admin_0_boundary_lines_land....'''
date = "2021-09-10T09:39:00Z"
lastmod = "2021-09-10T10:50:00Z"
weight = 81709
keywords = [ "rendering", "stylesheet", "render" ]
aliases = [ "/questions/81709" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [I tried changing the stylesheet to Positoron, but it doesn't render.](/questions/81709/i-tried-changing-the-stylesheet-to-positoron-but-it-doesnt-render)

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
<span id="post-81709-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81709-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81709-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have done all the steps as described in <a href="https://switch2osm.org/serving-tiles/manually-building-a-tile-server-20-04-lts/">this guide</a> and confirmed that it works fine.<br />
Note that since naciscdn.org is down, I have replaced the relevant part of external-data.yml with the following description.<br />
<a href="https://naturalearth.s3.amazonaws.com/110m_cultural/ne_110m_admin_0_boundary_lines_land.zip.">https://naturalearth.s3.amazonaws.com/110m_cultural/ne_110m_admin_0_boundary_lines_land.zip.</a></p>
<p>I would like to use the Positoron style for my basemap. I downloaded the style sheet from <a href="https://github.com/CartoDB/basemap-styles">here</a> and rewrote /usr/local/etc/renderd.conf.</p>
<blockquote>
<p>[renderd]<br />
num_threads=8<br />
tile_dir=/var/lib/mod_tile<br />
stats_file=/var/run/renderd/renderd.stats</p>
<p>[mapnik]<br />
plugins_dir=/usr/lib/mapnik/3.0/input<br />
font_dir=/usr/share/fonts/truetype<br />
font_dir_recurse=1</p>
<p>[ajt]<br />
URI=/hot/<br />
TILEDIR=/var/lib/mod_tile<br />
XML=/home/ubuntu/basemap-styles/cartocss/web-styles/positron.tm2/project.xml<br />
HOST=localhost<br />
TILESIZE=256</p>
</blockquote>
<p>When I start the renderd daemon and try to access <a href="http://myhost/hot/0/0/0.png,">http://myhost/hot/0/0/0.png,</a> I just get a gray image and it does not render correctly.<br />
When I try to access the site again after some time has passed, I just get a gray image.<br />
There are no errors in the renderd daemon log.<br />
In the /var/lib/mod_tile/ajt/ directory, a .meta file has been created.</p>
<blockquote>
<p>renderd[58068]: DEBUG: Got incoming connection, fd 5, number 1<br />
renderd[58068]: DEBUG: Got incoming request with protocol version 2<br />
renderd[58068]: DEBUG: Got command RenderPrio fd(5) xml(ajt), z(0), x(0), y(0), mime(image/png), options()<br />
renderd[58068]: DEBUG: START TILE ajt 0 0-0 0-0, new metatile<br />
renderd[58068]: Rendering projected coordinates 0 0 0 -&gt; -20037508.342800|-20037508.342800 20037508.342800|20037508.342800 to a 1 x 1 tile<br />
renderd[58068]: DEBUG: DONE TILE ajt 0 0-0 0-0 in 0.005 seconds<br />
debug: Creating and writing a metatile to /var/lib/mod_tile/ajt/0/0/0/0/0/0.meta</p>
<p>renderd[58068]: DEBUG: Sending render cmd(3 ajt 0/0/0) with protocol version 2 to fd 5<br />
renderd[58068]: DEBUG: Connection 0, fd 5 closed, now 0 left</p>
</blockquote>
<p>Please let me know what action I have to take in order to use Positoron style.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-stylesheet" rel="tag" title="see questions tagged &#39;stylesheet&#39;">stylesheet</span> <span class="post-tag tag-link-render" rel="tag" title="see questions tagged &#39;render&#39;">render</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Sep '21, 09:39</strong></p>
<img src="https://secure.gravatar.com/avatar/38c93e5f0209e15ecc928b62b7da9ba9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="m-itabashi&#39;s gravatar image" />
<p><span>m-itabashi</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="m-itabashi has no accepted answers">0%</span> </br></br></p>
</div>
</div>
<div id="comments-container-81709" class="comments-container">
<span id="81711"></span>
<div id="comment-81711" class="comment">
<div id="post-81711-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'd be surprised if you can use that as a "drop in replacement" like that. Someone did ask about it over at <a href="https://github.com/CartoDB/basemap-styles/issues/22">https://github.com/CartoDB/basemap-styles/issues/22</a> a while back but didn't get an answer.</p>
</div>
<div id="comment-81711-info" class="comment-info">
<span class="comment-age">(10 Sep '21, 10:50)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-81709" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81709-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

