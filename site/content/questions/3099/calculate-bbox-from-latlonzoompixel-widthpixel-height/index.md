+++
type = "question"
title = "calculate bbox from lat+lon+zoom+pixel width+pixel height"
description = '''How do you calculate a bounding box (that can be used where ever a bbox query parameter is required) using the center longitude and latitude, the zoom factor and the displayed width and height in pixels? Basically I need this to calculate the embedding and mapnik image export URLs from a permalink.'''
date = "2011-02-16T03:59:00Z"
lastmod = "2013-06-10T18:08:00Z"
weight = 3099
keywords = [ "lat", "embed", "lon", "bbox" ]
aliases = [ "/questions/3099" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [calculate bbox from lat+lon+zoom+pixel width+pixel height](/questions/3099/calculate-bbox-from-latlonzoompixel-widthpixel-height)

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
<span id="post-3099-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3099-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-3099-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How do you calculate a bounding box (that can be used where ever a <code>bbox</code> query parameter is required) using the center longitude and latitude, the zoom factor and the displayed width and height in pixels? Basically I need this to calculate the embedding and mapnik image export URLs from a permalink.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-lat" rel="tag" title="see questions tagged &#39;lat&#39;">lat</span> <span class="post-tag tag-link-embed" rel="tag" title="see questions tagged &#39;embed&#39;">embed</span> <span class="post-tag tag-link-lon" rel="tag" title="see questions tagged &#39;lon&#39;">lon</span> <span class="post-tag tag-link-bbox" rel="tag" title="see questions tagged &#39;bbox&#39;">bbox</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Feb '11, 03:59</strong></p>
<img src="https://secure.gravatar.com/avatar/d264e9dd3768e50e27aa3364cdfe3b6d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="panzi&#39;s gravatar image" />
<p><span>panzi</span><br />
<span class="score" title="66 reputation points">66</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="panzi has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-3099" class="comments-container">
&#10;</div>
<div id="comment-tools-3099" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3099-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="3100"></span>

<div id="answer-container-3100" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-3100-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3100-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-3100-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="panzi has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Convert the longitude and latitude of the map center to tile coordinates using the alogrithm described in <a href="http://wiki.openstreetmap.org/wiki/Slippy_map_tilenames">the Slippy Map Tilenames article on the wiki</a>, keeping the fractional part. Add / substract half of the width from tileX and half of the height from tileY to generate the coordinates of the four corners of the bbox. Convert them back to longitude and latitude using the description from the same wiki page. All you are now left to do is to create the string describing the bbox from the coordinates of the four corners. For mapnik this should be minlong,minlat,maxlong,maxlat.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Feb '11, 07:31</strong></p>
<img src="https://secure.gravatar.com/avatar/465f344e31e8ba1be0e0401414815db0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="petschge&#39;s gravatar image" />
<p><span>petschge</span><br />
<span class="score" title="8279 reputation points"><span>8.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="73 badges"><span class="silver">●</span><span class="badgecount">73</span></span><span title="98 badges"><span class="bronze">●</span><span class="badgecount">98</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="petschge has 29 accepted answers">21%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Feb '11, 07:38</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span></p>
</div>
</div>
<div id="comments-container-3100" class="comments-container">
<span id="14673"></span>
<div id="comment-14673" class="comment">
<div id="post-14673-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://pastebin.com/mMKrhA4D">http://pastebin.com/mMKrhA4D</a> is what I did with what you wrote. But the calculated values are too large. Why is that?</p>
</div>
<div id="comment-14673-info" class="comment-info">
<span class="comment-age">(27 Jul '12, 22:19)</span> <span class="comment-user userinfo">Richart</span>
</div>
</div>
</div>
<div id="comment-tools-3100" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3100-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="23195"></span>

<div id="answer-container-23195" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-23195-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23195-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-23195-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You probably need to take in account pixel size of each tile... I've needed this myself so this is what I've come up with and documented at <a href="http://wiki.openstreetmap.org/wiki/Slippy_map_tilenames#Lon..2Flat._to_bbox">OSM Wiki</a>:</p>
<pre><code>use Math::Trig;
&#10;sub getLonLat {
    my ($xtile, $ytile, $zoom) = @_;
    my $n = 2 ** $zoom;
    my $lon_deg = $xtile / $n * 360.0 - 180.0;
    my $lat_deg = rad2deg(atan(sinh(pi * (1 - 2 * $ytile / $n))));
    return ($lon_deg, $lat_deg);
}
&#10;# convert from permalink OSM format like:
# http://www.openstreetmap.org/?lat=43.731049999999996&amp;lon=15.79375&amp;zoom=13&amp;layers=M
# to OSM &quot;Export&quot; iframe embedded bbox format like:
# http://www.openstreetmap.org/export/embed.html?bbox=15.7444,43.708,15.8431,43.7541&amp;layer=mapnik
&#10;sub LonLat_to_bbox {
    my ($lat, $lon, $zoom) = @_;
&#10;    my $width = 425; my $height = 350;  # note: must modify this to match your embed map width/height in pixels
    my $tile_size = 256;
&#10;    my ($xtile, $ytile) = getTileNumber ($lat, $lon, $zoom);
&#10;    my $xtile_s = ($xtile * $tile_size - $width/2) / $tile_size;
    my $ytile_s = ($ytile * $tile_size - $height/2) / $tile_size;
    my $xtile_e = ($xtile * $tile_size + $width/2) / $tile_size;
    my $ytile_e = ($ytile * $tile_size + $height/2) / $tile_size;
&#10;    my ($lon_s, $lat_s) = getLonLat($xtile_s, $ytile_s, $zoom);
    my ($lon_e, $lat_e) = getLonLat($xtile_e, $ytile_e, $zoom);
&#10;    my $bbox = &quot;$lon_s,$lat_s,$lon_e,$lat_e&quot;;
    return $bbox;
}</code></pre>
<p>You can see code in action <a href="http://biciklijade.com/detail/57">here</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Jun '13, 18:08</strong></p>
<img src="https://secure.gravatar.com/avatar/666391973130e371bf8092f70c43df28?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Matija%20Nalis&#39;s gravatar image" />
<p><span>Matija Nalis</span><br />
<span class="score" title="750 reputation points">750</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Matija Nalis has 2 accepted answers">11%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Jun '13, 15:53</strong> </span></p>
</div>
</div>
<div id="comments-container-23195" class="comments-container">
&#10;</div>
<div id="comment-tools-23195" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23195-form-container" class="comment-form-container">
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

