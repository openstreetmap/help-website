+++
type = "question"
title = "BigMap Image Download Perl Script"
description = '''I am trying to use the BigMaps to download an image of the entire state of Arkansas at zoom 16. If I am lucky enough to get it to actually not crash my browser, I click the &quot;Perl&quot; link which downloads a &quot;mkmap.pl&quot; file. When I run it in CMD with Perl, I get this:  - GD Warning: product of memory all...'''
date = "2017-08-14T10:57:00Z"
lastmod = "2017-08-16T08:20:00Z"
weight = 58299
keywords = [ "download", "map", "image", "bigmap", "perl" ]
aliases = [ "/questions/58299" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [BigMap Image Download Perl Script](/questions/58299/bigmap-image-download-perl-script)

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
<span id="post-58299-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-58299-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-58299-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am trying to use the BigMaps to download an image of the entire state of Arkansas at zoom 16. If I am lucky enough to get it to actually not crash my browser, I click the "Perl" link which downloads a "mkmap.pl" file. When I run it in CMD with Perl, I get this: - GD Warning: product of memory allocation multiplication would exceed INT_MAX, failing operation - gracefully - Can't call method "colorAllocate" on an undefined value at /perl_tests/arkansas.pl line 11. Line 11 in that file reads: - my $white = $img-&gt;colorAllocate(248,248,248); Why is this causing an error? I would think that with this file being directly from BigMaps, it would work immediately. Am I doing something wrong, or is the file causing the error?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-download" rel="tag" title="see questions tagged &#39;download&#39;">download</span> <span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span> <span class="post-tag tag-link-image" rel="tag" title="see questions tagged &#39;image&#39;">image</span> <span class="post-tag tag-link-bigmap" rel="tag" title="see questions tagged &#39;bigmap&#39;">bigmap</span> <span class="post-tag tag-link-perl" rel="tag" title="see questions tagged &#39;perl&#39;">perl</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Aug '17, 10:57</strong></p>
<img src="https://secure.gravatar.com/avatar/37dad3ff646c63f1eb94bcb2302c4915?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BobGrey&#39;s gravatar image" />
<p><span>BobGrey</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BobGrey has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-58299" class="comments-container">
&#10;</div>
<div id="comment-tools-58299" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-58299-form-container" class="comment-form-container">
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

<span id="58300"></span>

<div id="answer-container-58300" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-58300-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-58300-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-58300-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The bounding box for Arkansas is roughly from longitude -94.61787 to -89.64224 and latitude 33.00412 to 36.49951. According to <a href="https://wiki.openstreetmap.org/wiki/Slippy_map_tilenames">slippy map tilenames</a> and <a href="http://oms.wff.ch/calc.htm">Tilesname Webcalc</a> this would lead to about 906*774 = 701244 tiles for zoom level 16. Each tile is 256x256 large. The resulting image would have a size of 179518464 x 179518464 pixels. I doubt this is what you really want.</p>
<p>Also, BigMap and BigMap2 are essentially performing a bulk download and thus violating the <a href="https://operations.osmfoundation.org/policies/tiles/">tile usage policy</a>.</p>
<p>Maybe you want to tell us what you are trying to achieve. There might be better solutions, for example rendering your own tiles.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Aug '17, 13:32</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-58300" class="comments-container">
<span id="58314"></span>
<div id="comment-58314" class="comment">
<div id="post-58314-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I am trying to recreate Arkansas on a 1:1 scale. I want to find an image that is can show EVERY road and street in Arkansas, which is only possible on high zoom levels (I found Zoom 15 to be the lowest zoom that still shows the desired detail, but it causes roads close to each other to merge together, such as roads with medians or freeways and their service roads...) If there is a better way to do this, please let me know! How do I go about rendering my own tiles? This seems like it will be a good idea, I just don't know what it actually is or how it works... Thank you for the reply and pointing out the tile usage policy issue with it. Perhaps downloading 700,000 tiles is actually not a good idea! Sorry about that...</p>
</div>
<div id="comment-58314-info" class="comment-info">
<span class="comment-age">(15 Aug '17, 10:22)</span> <span class="comment-user userinfo">BobGrey</span>
</div>
</div>
<span id="58316"></span>
<div id="comment-58316" class="comment">
<div id="post-58316-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You can take a look at <a href="https://switch2osm.org/serving-tiles/">https://switch2osm.org/serving-tiles/</a> and <a href="https://wiki.openstreetmap.org/wiki/Rendering.">https://wiki.openstreetmap.org/wiki/Rendering.</a> However it depends on what you want to achieve with this image. Do you want to print it? Do you just want to view it on your desktop computer or on a smartphone?</p>
</div>
<div id="comment-58316-info" class="comment-info">
<span class="comment-age">(15 Aug '17, 11:33)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="58320"></span>
<div id="comment-58320" class="comment">
<div id="post-58320-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I certainly hope they aren't planning on printing it out. A 1:1 scale map of Arkansas would take up an area the size of... well... Arkansas! :D <a href="http://blogs.ubc.ca/clanki/files/2007/04/on-the-impossibility.pdf">http://blogs.ubc.ca/clanki/files/2007/04/on-the-impossibility.pdf</a></p>
</div>
<div id="comment-58320-info" class="comment-info">
<span class="comment-age">(15 Aug '17, 16:47)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
<span id="58321"></span>
<div id="comment-58321" class="comment">
<div id="post-58321-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>No problem - just print it on the inside of an appropriate <a href="https://en.wikipedia.org/wiki/Menger_sponge">fractal shape</a> and everything will be fine!</p>
</div>
<div id="comment-58321-info" class="comment-info">
<span class="comment-age">(15 Aug '17, 17:05)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="58322"></span>
<div id="comment-58322" class="comment">
<div id="post-58322-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I just want to download it for viewing. I have no intentions on printing.</p>
</div>
<div id="comment-58322-info" class="comment-info">
<span class="comment-age">(16 Aug '17, 01:57)</span> <span class="comment-user userinfo">BobGrey</span>
</div>
</div>
<span id="58323"></span>
<div id="comment-58323" class="comment not_top_scorer">
<div id="post-58323-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Are you trying to download the rendered map, or the satellite photos?</p>
</div>
<div id="comment-58323-info" class="comment-info">
<span class="comment-age">(16 Aug '17, 07:34)</span> <span class="comment-user userinfo">dsh4</span>
</div>
</div>
<span id="58324"></span>
<div id="comment-58324" class="comment not_top_scorer">
<div id="post-58324-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Downloading/viewing such a single big image isn't really useful. You won't be able to orientate yourself, you won't be able to zoom (because everything will just get blurry when zooming out), you won't be able to search for addresses, calculate routes etc. If you are looking for a desktop software for OSM then take a look at <a href="https://marble.kde.org/">Marble</a>. However it requires an Internet connection (except for some cached tiles, or if you have your own tile server). Unfortunately I can't suggest a good desktop software with offline OSM maps.</p>
</div>
<div id="comment-58324-info" class="comment-info">
<span class="comment-age">(16 Aug '17, 07:52)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="58325"></span>
<div id="comment-58325" class="comment not_top_scorer">
<div id="post-58325-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I don't need maps as of being able to find places, that is what I use Google Maps for. I want a single, large image that can cover ALL of Arkansas on zoom 16. I use such image as a reference base for a project I am working on to re-create the entire state in a virtual environment on a 1:1 scale...</p>
</div>
<div id="comment-58325-info" class="comment-info">
<span class="comment-age">(16 Aug '17, 08:20)</span> <span class="comment-user userinfo">BobGrey</span>
</div>
</div>
</div>
<div id="comment-tools-58300" class="comment-tools">
<span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-58300-form-container" class="comment-form-container">
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

