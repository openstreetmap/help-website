+++
type = "question"
title = "Understanding Scale"
description = '''I&#x27;m interesting in generating URL&#x27;s to get a single map PNG for a given latitude/longitude range. Experimenting with the &quot;Export&quot; tab at openstreetmap.org, I&#x27;ve found that you must pass the latitude/longitude range, as well as a scale value. I haven&#x27;t been able to figure out exactly how to calculate...'''
date = "2011-12-14T00:07:00Z"
lastmod = "2014-02-14T11:55:00Z"
weight = 9510
keywords = [ "scale" ]
aliases = [ "/questions/9510" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Understanding Scale](/questions/9510/understanding-scale)

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
<span id="post-9510-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9510-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-9510-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm interesting in generating URL's to get a single map PNG for a given latitude/longitude range. Experimenting with the "Export" tab at <a href="http://openstreetmap.org">openstreetmap.org</a>, I've found that you must pass the latitude/longitude range, as well as a scale value. I haven't been able to figure out exactly how to calculate the scale that gives me the number of pixels I want.</p>
<p>I working from the information here: <a href="https://wiki.openstreetmap.org/wiki/FAQ#What_is_the_map_scale_for_a_particular_zoom_level_of_the_map.3F">https://wiki.openstreetmap.org/wiki/FAQ#What_is_the_map_scale_for_a_particular_zoom_level_of_the_map.3F</a></p>
<p>It appears that scale means the ratio of the map size shown on the screen, assuming a DPI of 72, to the actual size of the geographic area included. The page indicates that that is only true at the equator, however, and the scale number is interpreted differently at other latitudes, but let's skip that for now and look at the equator.</p>
<p>A single degree of longitude at the equator is 111320.0 meters across. As a silly example to keep the math simple, if I use the export web page interface to set the rectangle to a 1 degree square centered on the equator, and the scale to 1:1, it reports an image size of 397569610 pixels wide (don't worry I didn't try to download this image!). Assuming 72dpi, and with 39.37 inches in a meter, that works out to 397569610 / (72*39.37) = 140,254 meters, rather than the expected 111,320. (It's not just an artifact of using that absurd scale, it works out the same at other scales with another multiplication step).</p>
<p>Any idea of what's wrong with my assumptions/math?</p>
<p>Thanks!</p>
<p>Jesse</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-scale" rel="tag" title="see questions tagged &#39;scale&#39;">scale</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Dec '11, 00:07</strong></p>
<img src="https://secure.gravatar.com/avatar/d9e7f5b208631ce463d69c64a1af9eea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jesse2&#39;s gravatar image" />
<p><span>Jesse2</span><br />
<span class="score" title="61 reputation points">61</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jesse2 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-9510" class="comments-container">
&#10;</div>
<div id="comment-tools-9510" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9510-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="9513"></span>

<div id="answer-container-9513" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-9513-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9513-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-9513-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Well your math seems sane and I don't really have an answer on that part... but if you are looking to get static map images, another good place to look is the MapQuest Open API. They have a static map function that serves up OSM data but also has all kinds of bells and whistles. Their blog post about it with a link to the documentation can be found here:</p>
<p><a href="http://devblog.mapquest.com/2011/05/11/get-creative-with-the-open-static-maps-api/">http://devblog.mapquest.com/2011/05/11/get-creative-with-the-open-static-maps-api/</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Dec '11, 05:11</strong></p>
<img src="https://secure.gravatar.com/avatar/43ae79d3345e19f30ea5f2ea64a9f7bc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ToeBee&#39;s gravatar image" />
<p><span>ToeBee</span><br />
<span class="score" title="976 reputation points">976</span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ToeBee has 6 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-9513" class="comments-container">
<span id="9551"></span>
<div id="comment-9551" class="comment">
<div id="post-9551-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the info, I hadn't seen that, I'll check out their API/terms!</p>
</div>
<div id="comment-9551-info" class="comment-info">
<span class="comment-age">(16 Dec '11, 00:23)</span> <span class="comment-user userinfo">Jesse2</span>
</div>
</div>
<span id="9552"></span>
<div id="comment-9552" class="comment">
<div id="post-9552-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>They are in general pretty liberal with their terms, especially for the "open" stuff. A general page about their open products can be found here: <a href="http://developer.mapquest.com/web/products/open/">http://developer.mapquest.com/web/products/open/</a></p>
</div>
<div id="comment-9552-info" class="comment-info">
<span class="comment-age">(16 Dec '11, 07:21)</span> <span class="comment-user userinfo">ToeBee</span>
</div>
</div>
</div>
<div id="comment-tools-9513" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9513-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="9511"></span>

<div id="answer-container-9511" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-9511-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9511-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-9511-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>My suspicion is that something is wrong because you even start to wonder. Pixels and real world units don't go well together and the whole concept of "map scale" is worth little when every medium has a different resolution. For the sake of argument, let's just say our web interface assumes 90 dpi and not 72, then your computation works out fine!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Dec '11, 00:36</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-9511" class="comments-container">
<span id="9550"></span>
<div id="comment-9550" class="comment">
<div id="post-9550-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the response, the math works out well at 90 dpi! I'm now able to generate a scale value that generates ~1 megapixel maps for a given lat/lon range. But, maybe I'm thinking about this wrong - is there a better way to specify desired image size, other than through scale?</p>
</div>
<div id="comment-9550-info" class="comment-info">
<span class="comment-age">(16 Dec '11, 00:17)</span> <span class="comment-user userinfo">Jesse2</span>
</div>
</div>
</div>
<div id="comment-tools-9511" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9511-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="30742"></span>

<div id="answer-container-30742" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-30742-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30742-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-30742-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>To calculate it, use these formulas:</p>
<pre><code>resolution = 156543.034 meters/pixel * cos(latitude) / (2 ^ zoomlevel)</code></pre>
<p>The resolution means how many meters per pixel you get.</p>
<pre><code>scale = 1 : (dpi * 39.37 in/m * resolution)</code></pre>
<p>The scale means, how many cm in reality is 1 cm on the paper (or on the screen).</p>
<p>So if you have a screen with 96 dpi, you get that one pixel is 1.1943 meters. And you get a scale of 1 : 4 231 which means that 1 cm on your screen is 42.3 m in reality.</p>
<p>If you have a printer which prints 300 dpi … (now do the calculations yourself).</p>
<hr />
<p>There is a <a href="https://wiki.openstreetmap.org/wiki/Slippy_map_tilenames#Resolution_and_Scale">wiki page about scaling</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Feb '14, 11:55</strong></p>
<img src="https://secure.gravatar.com/avatar/793c9f0cfb9f3cc6001d73f127644c67?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="erik&#39;s gravatar image" />
<p><span>erik</span><br />
<span class="score" title="558 reputation points">558</span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="34 badges"><span class="bronze">●</span><span class="badgecount">34</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="erik has one accepted answer">9%</span></p>
</div>
</div>
<div id="comments-container-30742" class="comments-container">
&#10;</div>
<div id="comment-tools-30742" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30742-form-container" class="comment-form-container">
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

