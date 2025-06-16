+++
type = "question"
title = "How can I export svg files with layers editable in inkscape ?"
description = '''Hello everybody, as far as I understood, the OSM data stock is organized in layers, attributed to various contens, such as water, roads, forest, buildings etc. Up to now I didnt find a possibility to export these layers in a manner inkscape can distinguish them - so they can be switched on and off e...'''
date = "2010-09-15T20:46:00Z"
lastmod = "2015-02-16T20:14:00Z"
weight = 813
keywords = [ "layers", "svg", "inkscape" ]
aliases = [ "/questions/813" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [How can I export svg files with layers editable in inkscape ?](/questions/813/how-can-i-export-svg-files-with-layers-editable-in-inkscape)

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
<span id="post-813-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-813-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-813-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello everybody,</p>
<p>as far as I understood, the OSM data stock is organized in layers, attributed to various contens, such as water, roads, forest, buildings etc.</p>
<p>Up to now I didnt find a possibility to export these layers in a manner inkscape can distinguish them - so they can be switched on and off etc.</p>
<p>Thanks and greetings,</p>
<p>Wolf</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-layers" rel="tag" title="see questions tagged &#39;layers&#39;">layers</span> <span class="post-tag tag-link-svg" rel="tag" title="see questions tagged &#39;svg&#39;">svg</span> <span class="post-tag tag-link-inkscape" rel="tag" title="see questions tagged &#39;inkscape&#39;">inkscape</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Sep '10, 20:46</strong></p>
<img src="https://secure.gravatar.com/avatar/270c2954f0ef833b01ab36cd27c742d2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="herrdeh&#39;s gravatar image" />
<p><span>herrdeh</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="herrdeh has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-813" class="comments-container">
&#10;</div>
<div id="comment-tools-813" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-813-form-container" class="comment-form-container">
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

<span id="818"></span>

<div id="answer-container-818" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-818-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-818-score" class="post-score" title="current number of votes">
7
</div>
<span id="post-818-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Simple one. Follow these steps:</p>
<ol>
<li>Download Maperitive (<a href="http://maperitive.net/"></a><a href="http://maperitive.net/"></a><a href="http://maperitive.net/">http://maperitive.net/</a>) and run it</li>
<li>Load your OSM file using the <code>load-source path_to_my_osm_file</code> command</li>
<li>Export it to SVG using either the menu option or by the <a href="http://maperitive.net/docs/manual/Commands/ExportSvg.html"><code>export-svg</code> command</a></li>
</ol>
<p>The exported SVG groups map features into SVG/Inkscape layers, so you'll be able to edit or hide them separately.</p>
<p>Here's how it looks in Adobe Illustrator (Inkscape shows it pretty much the same): <img src="https://wiki.openstreetmap.org/w/images/7/7e/MaperitiveSvgIllustrator.png" alt="alt text" /></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Sep '10, 04:23</strong></p>
<img src="https://secure.gravatar.com/avatar/591340f954c00c8208d5ffe668f50a05?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Breki&#39;s gravatar image" />
<p><span>Breki</span><br />
<span class="score" title="2040 reputation points"><span>2.0k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="18 badges"><span class="silver">●</span><span class="badgecount">18</span></span><span title="43 badges"><span class="bronze">●</span><span class="badgecount">43</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Breki has 5 accepted answers">10%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Nov '10, 19:23</strong> </span></p>
</div>
</div>
<div id="comments-container-818" class="comments-container">
&#10;</div>
<div id="comment-tools-818" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-818-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="847"></span>

<div id="answer-container-847" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-847-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-847-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-847-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Inkscape allows you to select elements based on their style (for example fill color: fill:#ff0000;) using Edit-&gt;Find (Ctrl+F).</p>
<p>To get the style of an object, select the object and look in Edit-&gt;XML editor...</p>
<p>I used this trick to get the coastline out of the SVG map exported from the OpenStreetMap home page.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Sep '10, 22:16</strong></p>
<img src="https://secure.gravatar.com/avatar/bc7753dbf85a3cac5cb7b0f6e1f8362a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ponchietto&#39;s gravatar image" />
<p><span>ponchietto</span><br />
<span class="score" title="61 reputation points">61</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ponchietto has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-847" class="comments-container">
&#10;</div>
<div id="comment-tools-847" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-847-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="814"></span>

<div id="answer-container-814" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-814-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-814-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-814-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>OSM data is not organized in layers. Contrary to how usual GIS software works, with OSM it is not the data creator's job to decide which layer something is on ("this is a tree; add it to the <em>natural</em> layer"), but instead the data user's job ("give me all objects tagged as trees and combine them in a layer I'll call <em>natural</em>").</p>
<p>There is no existing software or service that will neatly arrange objects on SVG layers for you. Your best bet is probably to look at installing one of the renderers capable of generating SVG output (Mapnik, Osmarender, or Mapgen.pl - all on the Wiki) and then try to generate individual SVG files for each layer which you later combine. This will require some work.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Sep '10, 20:58</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-814" class="comments-container">
&#10;</div>
<div id="comment-tools-814" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-814-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="41064"></span>

<div id="answer-container-41064" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-41064-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41064-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-41064-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Guys thank you so much for the attention to my issue! :) I think I found the solution to my issue through the use of mapaperitive, super useful tool! I imported as source an "opencyclemap" map of the area in the program (using the EXPORT function in osm) and simply exported the map as SVG for Illustrator. Until now I managed to get fairly decent topographic map of the area to use as reference in my project. Still opened to even better solution!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Feb '15, 20:14</strong></p>
<img src="https://secure.gravatar.com/avatar/e4ebf9e89553c72153b7b0bbcca24c85?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Alberto1989&#39;s gravatar image" />
<p><span>Alberto1989</span><br />
<span class="score" title="56 reputation points">56</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Alberto1989 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-41064" class="comments-container">
&#10;</div>
<div id="comment-tools-41064" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41064-form-container" class="comment-form-container">
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

