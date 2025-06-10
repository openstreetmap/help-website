+++
type = "question"
title = "Exporting a relatively large map"
description = '''Is it possible for someone who is NOT a programmer, to export a large map (such as the map of Orange County in California) in SVG format in order for it to be used in vector-based applications such as InkScape? Is OSM for programmers only? I can get around, however, I am not a web or C++ programmer.'''
date = "2010-12-12T22:58:00Z"
lastmod = "2013-10-17T21:20:00Z"
weight = 1792
keywords = [ "svg", "export" ]
aliases = [ "/questions/1792" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Exporting a relatively large map](/questions/1792/exporting-a-relatively-large-map)

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
<span id="post-1792-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1792-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-1792-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is it possible for someone who is NOT a programmer, to export a large map (such as the map of Orange County in California) in SVG format in order for it to be used in vector-based applications such as InkScape? Is OSM for programmers only? I can get around, however, I am not a web or C++ programmer.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-svg" rel="tag" title="see questions tagged &#39;svg&#39;">svg</span> <span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Dec '10, 22:58</strong></p>
<img src="https://secure.gravatar.com/avatar/e0b92c051cf1bd4648859efbf141acb3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mattmos&#39;s gravatar image" />
<p><span>mattmos</span><br />
<span class="score" title="46 reputation points">46</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mattmos has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> retagged <strong>13 Dec '10, 07:48</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/591340f954c00c8208d5ffe668f50a05?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Breki&#39;s gravatar image" />
<p><span>Breki</span><br />
<span class="score" title="2040 reputation points"><span>2.0k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="18 badges"><span class="silver">●</span><span class="badgecount">18</span></span><span title="43 badges"><span class="bronze">●</span><span class="badgecount">43</span></span></p>
</div>
</div>
<div id="comments-container-1792" class="comments-container">
&#10;</div>
<div id="comment-tools-1792" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1792-form-container" class="comment-form-container">
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

<span id="1796"></span>

<div id="answer-container-1796" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-1796-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1796-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-1796-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The export tab(*) on <a href="http://www.openstreetmap.org">the project's main page</a> can be used to export any area in SVG format. Exporting custom maps in SVG is a CPU intensive task; that's why the "normal" map consists of standardised, pre-rendered bitmap tiles which are easier to produce and, crucially, the same for every viewer.</p>
<p>There are three limits to the free export service on the main page:</p>
<ul>
<li>It is not available during high-load times. Sometimes you will see a message that says, in effect, that you should try again later.</li>
<li>You cannot request an arbitrary resolution; e.g. if you request a map the size of Orange County, you will not get a level of detail that shows individual houses. But you can get a more detailed map than the one you see on screen by entering a smaller scale number down to the allowed minimum.</li>
<li>The resulting SVG is awful for post-processing (takes ages to load in Inkscape, lettering done as vectors, etc.)</li>
</ul>
<p>If you want more then you will have to install some rendering software on your own computer and run it. You could use e.g. <a href="http://wiki.openstreetmap.org/wiki/Maperitive">Maperitive</a>, <a href="http://wiki.openstreetmap.org/wiki/Osmarender">Osmarender</a>, or a local <a href="http://wiki.openstreetmap.org/wiki/Mapnik">Mapnik</a> installation. Mapnik is the only one that will give you the same look as the main map, but is more difficult to set up and will also produce the same kind of SVG. Maperitive and Osmarender produce SVG that is better suited for post-processing but the maps will also look different. For Maperitive, also see <a href="http://help.openstreetmap.org/questions/813/how-can-i-export-svg-files-with-layers-editable-in-inkscape">this other answer</a>.</p>
<p>If you lack the time or ability to do this, you can also <a href="http://wiki.openstreetmap.org/wiki/List_of_Companies_offering_OSM_Consulting">pay someone to do the work.</a></p>
<p>OpenStreetMap is a community effort, not a service provider. OpenStreetMap is "for" whomever community members want it to be for! If you choose one of the above methods for your work, or if you end up doing something completely different, consider contributing to OpenStreetMap by documenting your work in our Wiki so that others who have the same background and the same demands as yourself will have it easier to find the answers they are looking for.</p>
<p>(*) In August 2013 the export tab has been removed, and replaced by an "export" link on the left hand side that lets you export the raw data for an area, and a "share" button on the right hand side that lets you export images.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Dec '10, 08:00</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Aug '13, 00:36</strong> </span></p>
</div>
</div>
<div id="comments-container-1796" class="comments-container">
&#10;</div>
<div id="comment-tools-1796" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1796-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="1795"></span>

<div id="answer-container-1795" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-1795-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1795-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-1795-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Yes: use Maperitive. See my answer on <a href="http://help.openstreetmap.org/questions/813/how-can-i-export-svg-files-with-layers-editable-in-inkscape"></a><a href="http://help.openstreetmap.org/questions/813/how-can-i-export-svg-files-with-layers-editable-in-inkscape"></a><a href="http://help.openstreetmap.org/questions/813/how-can-i-export-svg-files-with-layers-editable-in-inkscape">http://help.openstreetmap.org/questions/813/how-can-i-export-svg-files-with-layers-editable-in-inkscape</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Dec '10, 07:52</strong></p>
<img src="https://secure.gravatar.com/avatar/591340f954c00c8208d5ffe668f50a05?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Breki&#39;s gravatar image" />
<p><span>Breki</span><br />
<span class="score" title="2040 reputation points"><span>2.0k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="18 badges"><span class="silver">●</span><span class="badgecount">18</span></span><span title="43 badges"><span class="bronze">●</span><span class="badgecount">43</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Breki has 5 accepted answers">10%</span></p>
</div>
</div>
<div id="comments-container-1795" class="comments-container">
&#10;</div>
<div id="comment-tools-1795" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1795-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="2066"></span>

<div id="answer-container-2066" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-2066-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2066-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-2066-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="http://wiki.openstreetmap.org/wiki/Bigmap">http://wiki.openstreetmap.org/wiki/Bigmap</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Jan '11, 14:44</strong></p>
<img src="https://secure.gravatar.com/avatar/cb9e3487765b1e13e3fd6ebb00fdcac7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kartograefin&#39;s gravatar image" />
<p><span>Kartograefin</span><br />
<span class="score" title="592 reputation points">592</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kartograefin has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-2066" class="comments-container">
<span id="27277"></span>
<div id="comment-27277" class="comment">
<div id="post-27277-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Bigmap creates rasterized (pixel) images. Not vector (SVG) graphics.</p>
</div>
<div id="comment-27277-info" class="comment-info">
<span class="comment-age">(17 Oct '13, 21:20)</span> <span class="comment-user userinfo">erik</span>
</div>
</div>
</div>
<div id="comment-tools-2066" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2066-form-container" class="comment-form-container">
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

