+++
type = "question"
title = "create a simple, minimalist black and white map"
description = '''Hi, I am new to the mapping world (an architecture student) and trying to create a simple map of New York City. I would like ideally to have a map of just the streets as single black lines on a black background, with the option of underlaying a faded satellite image. I can&#x27;t seem to figure out how t...'''
date = "2011-04-06T23:24:00Z"
lastmod = "2011-04-07T00:43:00Z"
weight = 4313
keywords = [ "rendering", "style", "custom", "minimal", "map" ]
aliases = [ "/questions/4313" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [create a simple, minimalist black and white map](/questions/4313/create-a-simple-minimalist-black-and-white-map)

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
<span id="post-4313-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4313-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-4313-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I am new to the mapping world (an architecture student) and trying to create a simple map of New York City. I would like ideally to have a map of just the streets as single black lines on a black background, with the option of underlaying a faded satellite image. I can't seem to figure out how to edit a map to get this. If I can't get it that simple, at least a gray-scale map with streets (or block outlines) without showing street names or the names of anything else - no extra lines for public transit, etc. Thanks in advance!!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-style" rel="tag" title="see questions tagged &#39;style&#39;">style</span> <span class="post-tag tag-link-custom" rel="tag" title="see questions tagged &#39;custom&#39;">custom</span> <span class="post-tag tag-link-minimal" rel="tag" title="see questions tagged &#39;minimal&#39;">minimal</span> <span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Apr '11, 23:24</strong></p>
<img src="https://secure.gravatar.com/avatar/b1e27dc0d85dc6e3881c4321e5271255?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="the%20coop%20guy&#39;s gravatar image" />
<p><span>the coop guy</span><br />
<span class="score" title="46 reputation points">46</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="the coop guy has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Apr '15, 14:43</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-4313" class="comments-container">
&#10;</div>
<div id="comment-tools-4313" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4313-form-container" class="comment-form-container">
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

<span id="4314"></span>

<div id="answer-container-4314" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-4314-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4314-score" class="post-score" title="current number of votes">
10
</div>
<span id="post-4314-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You will need to install rendering software, then download the area of interest, create a suitable rendering style, and run your data through the rendering engine to arrive at a PNG file or something.</p>
<p>If you choose to use the renderer <a href="http://www.maperitive.net">Maperitive</a> (reasonably simple to install and suitable for beginners), a style sheet that just draws a thin line for every road could look like this:</p>
<hr />
<pre><code>features
    lines
        street : highway
&#10;properties
    map-background-color : #EEEEEE
&#10;rules
    target: street
        define
           line-color : black
           line-width : 1
        draw : line</code></pre>
<hr />
<p>If you choose to install the renderer <a href="https://wiki.openstreetmap.org/wiki/Mapnik">Mapnik</a> - which requires some other programs to be installed as well, is more difficult, but can process larger amounts of data -, then you'll find a very simple style example on the web site for an OSM book I've co-authored, <a href="http://openstreetmap.info/examples/index.html">here.</a> (The "Mapnik waterways example")</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Apr '11, 23:36</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Apr '11, 21:55</strong> </span></p>
</div>
</div>
<div id="comments-container-4314" class="comments-container">
<span id="4316"></span>
<div id="comment-4316" class="comment">
<div id="post-4316-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Great thanks for the help! I was deciding between the two and went with Mapnik - it seems to be the most powerful, and the most useful especially as I plan to do more of this in the future and in grad school. I ended up downloading Python and PROJ_Framework to get everything fully installed. I have never used Python and never really coded/programmed anything, so this will be an adventure for me! I also found a program called TileMill which seems to have some pretty amazing graphics capabilities.</p>
<p>P</p>
</div>
<div id="comment-4316-info" class="comment-info">
<span class="comment-age">(07 Apr '11, 00:43)</span> <span class="comment-user userinfo">the coop guy</span>
</div>
</div>
</div>
<div id="comment-tools-4314" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4314-form-container" class="comment-form-container">
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

