+++
type = "question"
title = "Is there a list with the colors used in the default Openstreetmap style?"
description = '''Hello everyone. I&#x27;m writing a small android application with osmdroid that shows the map and uses the landcover information of the current position for some features. Since the tiles are being stored on the filesystem of the device either way by osmdroid, i had the idea to analyse them instead of us...'''
date = "2015-10-31T22:40:00Z"
lastmod = "2015-11-04T16:12:00Z"
weight = 46280
keywords = [ "rendering", "tiles", "style", "mapnik" ]
aliases = [ "/questions/46280" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Is there a list with the colors used in the default Openstreetmap style?](/questions/46280/is-there-a-list-with-the-colors-used-in-the-default-openstreetmap-style)

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
<span id="post-46280-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46280-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-46280-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello everyone.</p>
<p>I'm writing a small android application with osmdroid that shows the map and uses the landcover information of the current position for some features. Since the tiles are being stored on the filesystem of the device either way by osmdroid, i had the idea to analyse them instead of using another service like overpass api, to reduce the traffic caused by my application and to allow usage in areas with bad or no internet.</p>
<p>On <a href="http://wiki.openstreetmap.org/wiki/Mapnik">http://wiki.openstreetmap.org/wiki/Mapnik</a> it says that <a href="https://github.com/gravitystorm/openstreetmap-carto">https://github.com/gravitystorm/openstreetmap-carto</a> is the official style of openstreetmap. Distributed over the relevant .mss files i can find a lot of color hex codes.</p>
<p>But for example the green <a href="http://www.color-hex.com/color/c8f9cc">#c8f9cc</a> which is used in the park at <a href="http://a.tile.openstreetmap.org/16/34126/21791.png">http://a.tile.openstreetmap.org/16/34126/21791.png</a> can't be found anywhere, neither by manual search (going into the files and strg+f) nor with the github search function. looking into the mss file it should be <a href="http://www.color-hex.com/color/c8facc">#c8facc</a></p>
<p>Another example would be the yellow <a href="http://www.color-hex.com/color/fef0ba">#fef0ba</a> which is used in this tile: <a href="http://c.tile.openstreetmap.org/19/274603/166642.png">http://c.tile.openstreetmap.org/19/274603/166642.png</a> where the beach is marked with natural=beach, so it should be <a href="http://www.color-hex.com/color/fff1ba">#fff1ba</a>.</p>
<p>Should be values are based on <a href="https://github.com/gravitystorm/openstreetmap-carto/blob/master/landcover.mss">https://github.com/gravitystorm/openstreetmap-carto/blob/master/landcover.mss</a></p>
<p>I suspect that the gamma adjustments for zoom level and number of nodes are the cause of this, for example:</p>
<pre><code>[feature = &#39;leisure_park&#39;],
[feature = &#39;leisure_recreation_ground&#39;] {
[zoom &gt;= 10] {
  polygon-fill: @park;
  [way_pixels &gt;= 4]  { **polygon-gamma: 0.75**; }
  [way_pixels &gt;= 64] { **polygon-gamma: 0.3**;  }
}
}</code></pre>
<p>So i tried playing around with the original colors and the gamma adjustment tool of paint.net, but i was unable to reproduce the used colorcodes.</p>
<p>Is this really the right github project, or am i looking at the wrong one? If it is the wrong one, could you please point me into the right direction?</p>
<p>If it is the right one, what operation gets executed that produces the final colorcodes? Is there maybe somewhere a full list of them?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-style" rel="tag" title="see questions tagged &#39;style&#39;">style</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 Oct '15, 22:40</strong></p>
<img src="https://secure.gravatar.com/avatar/991a1daf7de47d3dcc3d94933c70ce2d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EinFreierNick&#39;s gravatar image" />
<p><span>EinFreierNick</span><br />
<span class="score" title="121 reputation points">121</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EinFreierNick has one accepted answer">50%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Nov '15, 19:37</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-46280" class="comments-container">
<span id="46281"></span>
<div id="comment-46281" class="comment">
<div id="post-46281-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>just a quick drop in (no time to think about your question in deep), maybe it is related: <a href="https://blog.openstreetmap.org/2015/10/30/openstreetmap-org-map-changing/">https://blog.openstreetmap.org/2015/10/30/openstreetmap-org-map-changing/</a></p>
</div>
<div id="comment-46281-info" class="comment-info">
<span class="comment-age">(31 Oct '15, 23:48)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="46283"></span>
<div id="comment-46283" class="comment">
<div id="post-46283-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/5179/aseerel4c26">@aseerel4c26</a> that might be possible. At the green area ~1/4th directly below the the New York label the dark green changes from #AACAAE to #AACBAF</p>
</div>
<div id="comment-46283-info" class="comment-info">
<span class="comment-age">(01 Nov '15, 08:32)</span> <span class="comment-user userinfo">EinFreierNick</span>
</div>
</div>
<span id="46285"></span>
<div id="comment-46285" class="comment">
<div id="post-46285-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>meta: Welcome to OSM, <a href="http://help.openstreetmap.org/users/11637/einfreiernick"></a><a href="http://help.openstreetmap.org/users/11637/einfreiernick">@EinFreierNick</a>!</p>
</div>
<div id="comment-46285-info" class="comment-info">
<span class="comment-age">(01 Nov '15, 09:07)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-46280" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46280-form-container" class="comment-form-container">
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

<span id="46296"></span>

<div id="answer-container-46296" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-46296-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46296-score" class="post-score" title="current number of votes">
7
</div>
<span id="post-46296-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="EinFreierNick has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You are looking at the correct code for where the colours are defined.</p>
<p>The piece you are missing is how the stylesheet is converted into rendered tiles. The OSMF tileservers use <code>mod_tile</code> and renderd to generate the images. <code>renderd</code> has a <a href="https://github.com/openstreetmap/mod_tile/blob/6b9611aaf763f4f776d1fd363433aac7e25cb34b/src/gen_tile.cpp#L277">hard-coded mapnik image format of "png256"</a> which means that it uses a 256 colour palette with the default settings for calculating the palette. Any differences between the colours set in the stylesheet and those found in the tiles are almost certainly due to the palette creation process.</p>
<p>You can read more details on the <a href="https://github.com/mapnik/mapnik/wiki/OutputFormats">available mapnik image formats</a> on the mapnik wiki.</p>
<p>If you use other software to create the images, such as Tilemill, then you might find the colours are slightly different, either by using full 32bit non-paletted images, or paletted images created with different settings.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Nov '15, 11:07</strong></p>
<img src="https://secure.gravatar.com/avatar/c3743b1b368f5e209eb8aad30164acc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andy%20Allan&#39;s gravatar image" />
<p><span>Andy Allan</span><br />
<span class="score" title="12456 reputation points"><span>12.5k</span></span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="128 badges"><span class="silver">●</span><span class="badgecount">128</span></span><span title="153 badges"><span class="bronze">●</span><span class="badgecount">153</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andy Allan has 46 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-46296" class="comments-container">
<span id="46370"></span>
<div id="comment-46370" class="comment">
<div id="post-46370-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>And see <a href="https://github.com/gravitystorm/openstreetmap-carto/issues/1940">https://github.com/gravitystorm/openstreetmap-carto/issues/1940</a> for a related github discussion.</p>
</div>
<div id="comment-46370-info" class="comment-info">
<span class="comment-age">(03 Nov '15, 16:43)</span> <span class="comment-user userinfo">gormo</span>
</div>
</div>
<span id="46388"></span>
<div id="comment-46388" class="comment">
<div id="post-46388-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>uf, i think i'll have to drop this. there are too many unknowns and even phenomenons in the "creation of the colors". But still, thank you for your help.</p>
</div>
<div id="comment-46388-info" class="comment-info">
<span class="comment-age">(04 Nov '15, 16:12)</span> <span class="comment-user userinfo">EinFreierNick</span>
</div>
</div>
</div>
<div id="comment-tools-46296" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46296-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="46282"></span>

<div id="answer-container-46282" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-46282-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46282-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-46282-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You are looking at the right code. Why the color code #c8facc defined in the style sheet ends up as #c8f9cc in the PNG I have no idea - I'd expect some alpha/antialiasing artifacts along the outline of the area but not in the centre.</p>
<p>There's a couple steps from the style sheet to the ready-made image. Some stylesheet instructions that deal with colours (lighten, darken, saturate etc.) are processed by the "carto" compiler that creates a Mapnik XML style description from the CSS files. But the actual drawing (during which the alpha values come into play) is handled by the Mapnik renderer, and more precisely by the AGG library it uses to do the drawing. If you can boil this down to a small test case - Mapnik instructed to render color A but instead rendered color B - then you could perhaps open a ticket on the Mapnik Github repository.</p>
<p>Having said that, trying to deduct geodata from tiles by color codes, and especially with a tolerance so small that a small change like c8facc-&gt;c8f9cc trips up the logic, sounds extremely brittle to me. Remember, the map style might change at any time.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Nov '15, 00:29</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-46282" class="comments-container">
<span id="46284"></span>
<div id="comment-46284" class="comment">
<div id="post-46284-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>yes ofcause building in a tolerance probably wouldn't hurt. But when i have no clue why (and how) things are like they are, this is going to be rather wearsome. In this case the difference is 1-3 per color, but what if it is somewhere 15 and not 1-3?</p>
</div>
<div id="comment-46284-info" class="comment-info">
<span class="comment-age">(01 Nov '15, 08:33)</span> <span class="comment-user userinfo">EinFreierNick</span>
</div>
</div>
<span id="46286"></span>
<div id="comment-46286" class="comment">
<div id="post-46286-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Like it is happening with #FFF1BA -&gt; #FFF0A9 (see the edit of the start post). The difference in blue is 17.</p>
</div>
<div id="comment-46286-info" class="comment-info">
<span class="comment-age">(01 Nov '15, 12:50)</span> <span class="comment-user userinfo">EinFreierNick</span>
</div>
</div>
</div>
<div id="comment-tools-46282" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46282-form-container" class="comment-form-container">
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

