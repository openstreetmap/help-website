+++
type = "question"
title = "scale and units question???"
description = '''I&#x27;ve exported the map region to jpg in 1:1000000, the resolution, shown to me was 2019 x 1866; area сoordinates was so: N 56.9583; E 40.3617; S 54.3107; W 35.2828 (it is the Moscow oblast) so my question is: what should be the DPI factor (in photoshop for example) to print that image in 1:1000000 ??...'''
date = "2012-04-12T23:24:00Z"
lastmod = "2014-02-14T12:00:00Z"
weight = 11955
keywords = [ "scale" ]
aliases = [ "/questions/11955" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [scale and units question???](/questions/11955/scale-and-units-question)

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
<span id="post-11955-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11955-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-11955-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've exported the map region to jpg in 1:1000000, the resolution, shown to me was 2019 x 1866; area сoordinates was so: N 56.9583; E 40.3617; S 54.3107; W 35.2828 (it is the Moscow oblast) so my question is: what should be the DPI factor (in photoshop for example) to print that image in 1:1000000 ???? because DPI factor by default is 72 and printed picture doesn't match to the scale 1:1000000. The same problem appeared in archicad, when I made import of the drawing (I tried it with JPG and Pdf format)the scale was also wrong. I'm working in metric system and I thought the problem is in that? but I tried different convertation and nothing helped??</p>
<p>I tryed to describe my question in link below</p>
<p><a href="http://help.openstreetmap.org/upfiles/scale_factor.jpg">http://help.openstreetmap.org/upfiles/scale_factor.jpg</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-scale" rel="tag" title="see questions tagged &#39;scale&#39;">scale</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Apr '12, 23:24</strong></p>
<img src="https://secure.gravatar.com/avatar/3d1b8fd37f50ae93cfae1a8eadf91604?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sergpomelov&#39;s gravatar image" />
<p><span>sergpomelov</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sergpomelov has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Apr '12, 14:26</strong> </span></p>
</div>
</div>
<div id="comments-container-11955" class="comments-container">
&#10;</div>
<div id="comment-tools-11955" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11955-form-container" class="comment-form-container">
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

4 Answers:

</div>

</div>

<span id="11984"></span>

<div id="answer-container-11984" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-11984-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11984-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-11984-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>That's what I did:</p>
<ol>
<li>Get an image of a known distance, at a given scale (say: 100m at 1:5000)</li>
<li>Get map size it should have: <code>100m / 5000 = 0.02m = 2cm</code></li>
<li>Measure that distance in pixels of obtained image: 100px so far <em>surprise!</em></li>
<li>Calculate: <code>100px / 2cm = 50 px/cm</code>. That's the resolution</li>
<li>Want it in inches? <code>50px/cm * 2,54cm/in = 127px/in</code></li>
</ol>
<p>As this measures are quite inaccurate, maybe you should try with different distances and map scales. I made it twice, and the second time I got <code>112.27 px/in</code>, so I think it should go around 120dpi.</p>
<p>Note: dpi is "dots per inch", and, as screen 'dots' are pixels, I used dpi and pixels/inch as the same unit.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Apr '12, 16:03</strong></p>
<img src="https://secure.gravatar.com/avatar/060ea25dc906b6f0e6c0744cd15d3fc1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="samel&#39;s gravatar image" />
<p><span>samel</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="samel has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-11984" class="comments-container">
<span id="12000"></span>
<div id="comment-12000" class="comment">
<div id="post-12000-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'm not so small, dady ))) But thanks a lot, Now i'm doing that with latitudinal way' I tape direct nombers in zone coordinates (not N 56.9583, but 57 not S 54.3107, but 54 not... and so on) the distance of 1_o of meredian is approx 111 km and it is quite all right for me.. for now... but I think that OSM steel needs to improve some resolution and unit parametr in export menu (for not to spand a time for that)</p>
</div>
<div id="comment-12000-info" class="comment-info">
<span class="comment-age">(14 Apr '12, 01:41)</span> <span class="comment-user userinfo">sergpomelov</span>
</div>
</div>
</div>
<div id="comment-tools-11984" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11984-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="12022"></span>

<div id="answer-container-12022" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-12022-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12022-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-12022-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>also found good decision with Maperitive. here <a href="http://help.openstreetmap.org/questions/840/problem-with-map-scale-when-generating-maps-with-osmarender">http://help.openstreetmap.org/questions/840/problem-with-map-scale-when-generating-maps-with-osmarender</a> (thanks to Breki)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Apr '12, 21:35</strong></p>
<img src="https://secure.gravatar.com/avatar/3d1b8fd37f50ae93cfae1a8eadf91604?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sergpomelov&#39;s gravatar image" />
<p><span>sergpomelov</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sergpomelov has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-12022" class="comments-container">
<span id="12031"></span>
<div id="comment-12031" class="comment">
<div id="post-12031-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>may be that coment is not for OSM system, but for supporting products... SO, using Maperitive (now I began to work with vector :) )I tried to export OSM data to illustrator and Inkscape at the same time )) so... for my great wondering, after export that data to dxf format I found that in Archicad they came with different size... after a fiew hours of interest I understood some primitive thing ! attention ! INKSCAPE EXPORT DATA IN 90 DPI AND ILLUSTRATOR EXPORT IT IN 72 DPI ! attention ! at the same time the resolution of my monitor is <a href="http://members.ping.de/~sven/dpi.html">http://members.ping.de/~sven/dpi.html</a> see next coment</p>
</div>
<div id="comment-12031-info" class="comment-info">
<span class="comment-age">(15 Apr '12, 11:42)</span> <span class="comment-user userinfo">sergpomelov</span>
</div>
</div>
<span id="12032"></span>
<div id="comment-12032" class="comment">
<div id="post-12032-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>1366 X 768 with 15.6" diagonal... (100.45 PPI/points per inch/)that<code>s why imported data was a bit bigger. So I scale it down to my real monitor size. In my case it was 381,56mm to 341,86 (that is the exported box size not the monitor / my monitor size is 34.54cm × 19.42cm //see link, in previous coment by the way I found it in Maperitive</code>s help///and I exported it from INKSCAPE /90 DPI//PPI for monitor///)</p>
</div>
<div id="comment-12032-info" class="comment-info">
<span class="comment-age">(15 Apr '12, 11:55)</span> <span class="comment-user userinfo">sergpomelov</span>
</div>
</div>
<span id="12033"></span>
<div id="comment-12033" class="comment">
<div id="post-12033-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>And as for OSM... Actualy I wouldn`t ever do all that if I onley had real 100mm leng virtual line (exportable to PDF) in the left down corner, close to the scale line (also exportable). But now I know everything about map scaling. Thanks for your attention.</p>
</div>
<div id="comment-12033-info" class="comment-info">
<span class="comment-age">(15 Apr '12, 12:13)</span> <span class="comment-user userinfo">sergpomelov</span>
</div>
</div>
</div>
<div id="comment-tools-12022" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12022-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="30743"></span>

<div id="answer-container-30743" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-30743-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30743-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-30743-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>From that <a href="http://wiki.openstreetmap.org/wiki/Slippy_map_tilenames#Resolution_and_Scale">wiki page</a> you get these basic formulas:</p>
<pre><code>resolution = 156543.034 meters/pixel * cos(latitude) / (2 ^ zoomlevel)</code></pre>
<p>The resolution means how many meters per pixel you get.</p>
<pre><code>scale = 1 : (dpi * 39.37 in/m * resolution)</code></pre>
<p>The scale means, how many cm in reality is 1 cm on the paper (or on the screen).</p>
<p>So if you have a screen with 96 dpi, you get that one pixel is 1.1943 meters. And you get a scale of 1 : 4 231 which means that 1 cm on your screen is 42.3 m in reality.</p>
<p>If you have a printer which prints 300 dpi … (now do the calculations yourself).</p>
<p>I hope this helps you getting the right size of your image.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Feb '14, 12:00</strong></p>
<img src="https://secure.gravatar.com/avatar/793c9f0cfb9f3cc6001d73f127644c67?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="erik&#39;s gravatar image" />
<p><span>erik</span><br />
<span class="score" title="558 reputation points">558</span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="34 badges"><span class="bronze">●</span><span class="badgecount">34</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="erik has one accepted answer">9%</span></p>
</div>
</div>
<div id="comments-container-30743" class="comments-container">
&#10;</div>
<div id="comment-tools-30743" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30743-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="11957"></span>

<div id="answer-container-11957" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-11957-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11957-score" class="post-score" title="current number of votes">
-2
</div>
<span id="post-11957-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The exported image is using mercator projection. This projection does not preserve scale. The exported image is scale 1:1000000 if you export an area near the equator, but this becomes a bigger scale the longer north or south you get. When you are comparing this map with a map in a projection that preserves scale better like utm you will see that they do not match. You will also notice other differences in the projections.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Apr '12, 01:28</strong></p>
<img src="https://secure.gravatar.com/avatar/44a4438f0146dfd898e24c221fd28b58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gnonthgol&#39;s gravatar image" />
<p><span>Gnonthgol ♦</span><br />
<span class="score" title="13750 reputation points"><span>13.8k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="103 badges"><span class="silver">●</span><span class="badgecount">103</span></span><span title="198 badges"><span class="bronze">●</span><span class="badgecount">198</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gnonthgol has 57 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-11957" class="comments-container">
<span id="11969"></span>
<div id="comment-11969" class="comment">
<div id="post-11969-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I dont think that answers the question. The problem is that the export tab lets you specify a 1:X scale, but that number is meaningless without an associated DPI (since the export is in pixels, it doesn't make sense to say "map is 1/Xth the size of reality" if you do not know the physical size of your printed/displayed pixel). The export tab should either say what DPI is used, or allow to set the DPI.</p>
<p>Concerning projection deformations: 1) zoom in sufficiently 2) let the export tab adjust the scale from the latitude.</p>
</div>
<div id="comment-11969-info" class="comment-info">
<span class="comment-age">(13 Apr '12, 10:53)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
<span id="11970"></span>
<div id="comment-11970" class="comment">
<div id="post-11970-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>M ) I see, but the scale is smaller??</p>
</div>
<div id="comment-11970-info" class="comment-info">
<span class="comment-age">(13 Apr '12, 11:11)</span> <span class="comment-user userinfo">sergpomelov</span>
</div>
</div>
<span id="11977"></span>
<div id="comment-11977" class="comment">
<div id="post-11977-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>zoom distanse does not matter, picture details depends on a scale factor you tape... as I understand... (and you always have maximum limit of a scale factor) and by the way, small scale line in low left corner is correct I checked it</p>
</div>
<div id="comment-11977-info" class="comment-info">
<span class="comment-age">(13 Apr '12, 12:55)</span> <span class="comment-user userinfo">sergpomelov</span>
</div>
</div>
<span id="11982"></span>
<div id="comment-11982" class="comment">
<div id="post-11982-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>made the way you toled me using latitude !!! greate !!! I think somehow OSM arrange that problem later ) thanks a lof for hi light decision (hard to find it sometimes)</p>
</div>
<div id="comment-11982-info" class="comment-info">
<span class="comment-age">(13 Apr '12, 14:22)</span> <span class="comment-user userinfo">sergpomelov</span>
</div>
</div>
</div>
<div id="comment-tools-11957" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11957-form-container" class="comment-form-container">
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

