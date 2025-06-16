+++
type = "question"
title = "Newbie question about hiding elements"
description = '''Hi I am trying to make some 2 types of location map (in SVG format) for our club showing where to find various sporting venues. The first is a large scale map showing only major roads, railways, rivers etc plus some landmarks such as pubs, shops etc. The second is a smaller scale map showing the imm...'''
date = "2011-06-13T18:13:00Z"
lastmod = "2012-05-29T11:45:00Z"
weight = 5737
keywords = [ "rendering", "newbie" ]
aliases = [ "/questions/5737" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Newbie question about hiding elements](/questions/5737/newbie-question-about-hiding-elements)

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
<span id="post-5737-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-5737-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-5737-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi</p>
<p>I am trying to make some 2 types of location map (in SVG format) for our club showing where to find various sporting venues. The first is a large scale map showing only major roads, railways, rivers etc plus some landmarks such as pubs, shops etc. The second is a smaller scale map showing the immediate area.</p>
<p>There is a wealth of data in the OSM map file which I need to hide but not sure how to do this. I can see two ways:</p>
<ol>
<li>edit the downloaded data and delete the elements I don't need using (eg) JOSM;</li>
<li>use a renderer to only display the items of interest.</li>
</ol>
<p>Slightly worried that if I do (1) I will accidentally upload the data back to OSM and wipe out someone's hard work. Also, not sure how to see what I have deleted using JOSM - I only get an edit view rather than a rendered view.</p>
<p>(2) sounds safer but looking through the XML file I am not sure how to find the data I need to display - it would be great if I could do this graphically. I understand that I need to render the maps in both cases to produce the SVG file using (eg) Osmarender. Presumably I can run this from a DOS prompt (running Windows)?<br />
</p>
<p>Sorry for so many questions but the whole process seems a bit daunting. Thanks in advance</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-newbie" rel="tag" title="see questions tagged &#39;newbie&#39;">newbie</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Jun '11, 18:13</strong></p>
<img src="https://secure.gravatar.com/avatar/5c8a8d9bc2a7379d8f129b696e2623ef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pet_griffin&#39;s gravatar image" />
<p><span>pet_griffin</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pet_griffin has no accepted answers">0%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Jun '11, 13:29</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span></p>
</div>
</div>
<div id="comments-container-5737" class="comments-container">
&#10;</div>
<div id="comment-tools-5737" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-5737-form-container" class="comment-form-container">
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

<span id="5740"></span>

<div id="answer-container-5740" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-5740-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-5740-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-5740-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Use <a href="http://maperitive.net">Maperitive</a>. Load the unmodified OSM file and start rendering using the default (OSM Mapnik-like) stylesheet. Then remove rules from the stylesheet for anything you don't want on your map.</p>
<p>Once you're done, you can export the map to SVG.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Jun '11, 20:57</strong></p>
<img src="https://secure.gravatar.com/avatar/591340f954c00c8208d5ffe668f50a05?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Breki&#39;s gravatar image" />
<p><span>Breki</span><br />
<span class="score" title="2040 reputation points"><span>2.0k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="18 badges"><span class="silver">●</span><span class="badgecount">18</span></span><span title="43 badges"><span class="bronze">●</span><span class="badgecount">43</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Breki has 5 accepted answers">10%</span></p>
</div>
</div>
<div id="comments-container-5740" class="comments-container">
<span id="6022"></span>
<div id="comment-6022" class="comment">
<div id="post-6022-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The OSM editor "Merkaartor" (<a href="http://www.merkaartor.be">http://www.merkaartor.be</a>) is also able to produce SVG output of OSM data.</p>
</div>
<div id="comment-6022-info" class="comment-info">
<span class="comment-age">(27 Jun '11, 12:12)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
<span id="13059"></span>
<div id="comment-13059" class="comment">
<div id="post-13059-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You can also generate your own tiles with Maperitive if you wanted to upload those to your site. You'd need some HTML to display them, perhaps based on my example here: <a href="https://wiki.openstreetmap.org/wiki/User:EdLoach#Using_Maperitive_Tiles">https://wiki.openstreetmap.org/wiki/User:EdLoach#Using_Maperitive_Tiles</a></p>
</div>
<div id="comment-13059-info" class="comment-info">
<span class="comment-age">(29 May '12, 11:45)</span> <span class="comment-user userinfo">EdLoach ♦</span>
</div>
</div>
</div>
<div id="comment-tools-5740" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-5740-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="5739"></span>

<div id="answer-container-5739" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-5739-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-5739-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-5739-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The simplest way is to export the map as an SVG file and using your favorite SVG editor remove the items you do not want and change the colors/icons to your liking. No need to install a renderer.</p>
<p>If you want complete control over how the map is going to look like you should make your own rule file that only displays the elements that you want and using the icons and style you want. On one-of maps there is often manual postprocessing on the svg file to fine tune the details and make the map look perfect.</p>
<p>If you are afraid that you will upload data with JOSM you can delete your token in the settings. JOSM will then ask you for your username and password before uploading anything.</p>
<p>The easiest way for you is just try and install osmarender and try to render a few maps. Maybe try and change a few rendering rules or editing the map using an SVG editor.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Jun '11, 19:29</strong></p>
<img src="https://secure.gravatar.com/avatar/44a4438f0146dfd898e24c221fd28b58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gnonthgol&#39;s gravatar image" />
<p><span>Gnonthgol ♦</span><br />
<span class="score" title="13750 reputation points"><span>13.8k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="103 badges"><span class="silver">●</span><span class="badgecount">103</span></span><span title="198 badges"><span class="bronze">●</span><span class="badgecount">198</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gnonthgol has 57 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Jun '11, 01:56</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span></p>
</div>
</div>
<div id="comments-container-5739" class="comments-container">
&#10;</div>
<div id="comment-tools-5739" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-5739-form-container" class="comment-form-container">
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

