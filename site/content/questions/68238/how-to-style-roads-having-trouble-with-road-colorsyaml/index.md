+++
type = "question"
title = "How to style roads?  Having trouble with road-colors.yaml"
description = '''I am using the basic openstreetmap-carto styling for my map. I am trying to re-color the roads so that all roads are white. To make this change, I came across the file named road-colors.yaml. The color syntax is nothing I have seen before. I found no instructions online as to how I can edit this fil...'''
date = "2019-03-04T02:05:00Z"
lastmod = "2021-03-22T08:27:00Z"
weight = 68238
keywords = [ "openstreetmap-carto", "style", "carto", "mapnik" ]
aliases = [ "/questions/68238" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to style roads? Having trouble with road-colors.yaml](/questions/68238/how-to-style-roads-having-trouble-with-road-colorsyaml)

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
<span id="post-68238-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68238-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-68238-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am using the basic openstreetmap-carto styling for my map. I am trying to re-color the roads so that all roads are white.</p>
<p>To make this change, I came across the file named <code>road-colors.yaml</code>.</p>
<p>The color syntax is nothing I have seen before. I found no instructions online as to how I can edit this file.</p>
<p>I simply want all roads to be white. How do I do that?</p>
<p>Default file contents:</p>
<pre><code># This is the input for scripts/generate_road_colours.py
&#10;# All road classes colours will be generated for, in order of importance
# (biggest first).
roads:
  - motorway
  - trunk
  - primary
  - secondary
&#10;# The starting and ending hue. The range goes from 0 to 360, with 0 and 360
# representing red.
hue: [10, 106]
&#10;# The lightness and chroma (also known as saturation) for each type of colour.
# Lightness ranges from 0 to 100; dark to bright.
# Chroma ranges from 0 to 100 too; unsaturated to fully saturated.
classes:
  # Colours for output into the MSS file
  mss:
    fill:
      lightness: [70, 97]
      chroma: [35, 29]
    casing:
      lightness: [50, 50]
      chroma: [70, 55]
    low-zoom:
      lightness: [62, 92]
      chroma: [50, 40]
    low-zoom-casing:
      lightness: [50, 70]
      chroma: [50, 65]
    shield:
      lightness: [20, 25]
      chroma: [40, 42]
  # Colours used by the road shields script
  shield:
    fill:
      lightness: [85, 95]
      chroma: [12, 14]
    stroke_fill:
      lightness: [70, 80]
      chroma: [22, 24]</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap-carto" rel="tag" title="see questions tagged &#39;openstreetmap-carto&#39;">openstreetmap-carto</span> <span class="post-tag tag-link-style" rel="tag" title="see questions tagged &#39;style&#39;">style</span> <span class="post-tag tag-link-carto" rel="tag" title="see questions tagged &#39;carto&#39;">carto</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Mar '19, 02:05</strong></p>
<img src="https://secure.gravatar.com/avatar/b1e3fbb6f31c5e0144e7b18fcd7d5d33?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="valachio&#39;s gravatar image" />
<p><span>valachio</span><br />
<span class="score" title="41 reputation points">41</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="valachio has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-68238" class="comments-container">
&#10;</div>
<div id="comment-tools-68238" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68238-form-container" class="comment-form-container">
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

<span id="79279"></span>

<div id="answer-container-79279" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-79279-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79279-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-79279-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can always override colors in <code>style.mms</code>. Just copy the bunch of definitions you want to modify, change the colors and voilà!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Mar '21, 20:39</strong></p>
<img src="https://secure.gravatar.com/avatar/e4587465b2b1b94834e5e625b80a29dd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Marcos%20Dione&#39;s gravatar image" />
<p><span>Marcos Dione</span><br />
<span class="score" title="71 reputation points">71</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Marcos Dione has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-79279" class="comments-container">
&#10;</div>
<div id="comment-tools-79279" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79279-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="79353"></span>

<div id="answer-container-79353" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-79353-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79353-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-79353-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I know it's not preferable way by documentation but in my case I changed color hash codes in <code>style/road-colors-generated.mss</code> and during later updates it works fine. It's about colours of road. But not all 'line items' definitions you can find there. There is also file <code>style/roads.mss</code> where rest of colours are defined for that group (i.e. <code>living-street</code>, <code>residential</code>, <code>footway</code>, <code>taxiway</code>, <code>railway</code> etc.). Here you can customize every tag by ZOOM level including road width and object casing.</p>
<p>What (I think) is worth to be mentioned is that road definition is divided into 2 parts. One part is responsible for road itself (colour, width, casing), and in the same file but in lated parts you can find definition how street names are generated (font colour, spacing between next labels, linings etc.). The same file structure is in <code>style/amenity-points.mss</code></p>
<p>I think it might be valuable knowledge especially for beginnners. It wasn't so clear for me couple days ago when I started to customize my own style.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Mar '21, 08:27</strong></p>
<img src="https://secure.gravatar.com/avatar/735ed8c1abf1a1f7b907b78d9594303c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="engopy&#39;s gravatar image" />
<p><span>engopy</span><br />
<span class="score" title="126 reputation points">126</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="engopy has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Mar '21, 08:27</strong> </span></p>
</div>
</div>
<div id="comments-container-79353" class="comments-container">
&#10;</div>
<div id="comment-tools-79353" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79353-form-container" class="comment-form-container">
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

