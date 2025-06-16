+++
type = "question"
title = "How do I export map images of larger areas?"
description = '''I want to print a big citymap that I can take with me. How do I get the images of a large area?'''
date = "2010-07-07T11:40:00Z"
lastmod = "2015-04-15T21:10:00Z"
weight = 22
keywords = [ "download", "map", "export" ]
aliases = [ "/questions/22" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [How do I export map images of larger areas?](/questions/22/how-do-i-export-map-images-of-larger-areas)

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
<span id="post-22-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22-score" class="post-score" title="current number of votes">
10
</div>
<span id="post-22-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
5
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to print a big citymap that I can take with me. How do I get the images of a large area?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-download" rel="tag" title="see questions tagged &#39;download&#39;">download</span> <span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span> <span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Jul '10, 11:40</strong></p>
<img src="https://secure.gravatar.com/avatar/278e1af65e82993efd0ba7bbbacf6435?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="spaetz&#39;s gravatar image" />
<p><span>spaetz</span><br />
<span class="score" title="853 reputation points">853</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="22 badges"><span class="bronze">●</span><span class="badgecount">22</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="spaetz has 2 accepted answers">28%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Jul '10, 05:11</strong> </span></p>
</div>
</div>
<div id="comments-container-22" class="comments-container">
&#10;</div>
<div id="comment-tools-22" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22-form-container" class="comment-form-container">
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

<span id="23"></span>

<div id="answer-container-23" class="answer accepted-answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-23-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23-score" class="post-score" title="current number of votes">
19
</div>
<span id="post-23-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="spaetz has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<ul>
<li><strong><a href="https://www.openstreetmap.org/export">Export tab</a></strong>: This is probably the easiest solution but only works for small areas. Select one of the options that is suitable: Raw OpenStreetMap XML Data, Mapnik Image, Osmarender Image, Embeddable HTML</li>
<li><strong><a href="http://maposmatic.org/">Maposmatic</a></strong>: Is a service that lets you create pretty city maps in any size in pdf and svg format. They also come with a street index.</li>
<li><strong><a href="https://wiki.openstreetmap.org/wiki/Bigmap">bigmap.cgi</a></strong>: This lets you select an area and download a small perl script that, when run, outputs the requested area in one big .png file. It stitches the grphic together from the single 256x256 pixel tile images.</li>
<li><strong><a href="http://walking-papers.org">Walking papers</a></strong>: Lets you easily select an area and print the map on a A4 (or letter) page. This is incredibly handy if you need a city map when exploring a new city, or to print a map and (with a real pen!) want to make notes, additions and corrections before fixing the map. Walking papers also offers a cool scan service where you can upload those annotated maps.</li>
<li><strong><a href="http://maperitive.net/">Maperitive</a></strong>: Desktopp app, written in mono, can produce both bitmaps, SVGs and web tiles from OSM XML files.</li>
</ul>
<p>Render on your own. Only do if you know what you are doing and need e.g. to customize your maps.</p>
<ul>
<li><strong>osmarender</strong>: <a href="https://wiki.openstreetmap.org/wiki/Osmarender">https://wiki.openstreetmap.org/wiki/Osmarender</a></li>
<li><strong>or/p</strong>: is an osmarender drop-in replacement that is faster (written in perl). See <a href="https://wiki.openstreetmap.org/wiki/Orp">https://wiki.openstreetmap.org/wiki/Orp</a></li>
<li><strong>mapnik</strong>: Full blown mapnik install is probably NOT what you want to do when all you need is some nice maps. But hey, <a href="https://wiki.openstreetmap.org/wiki/Mapnik">here is information about the mapnik renderer</a>.</li>
</ul>
<p>If you decide you want to customize or render things on your own, also have a look at the related question "<a href="/questions/136/how-do-i-render-my-own-maps-for-my-website">How do I render Maps for my own website</a>".</p>
</div>
<div class="answer-controls post-controls">
<div class="community-wiki">
This answer is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Jul '10, 12:03</strong></p>
<img src="https://secure.gravatar.com/avatar/278e1af65e82993efd0ba7bbbacf6435?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="spaetz&#39;s gravatar image" />
<p><span>spaetz</span><br />
<span class="score" title="853 reputation points">853</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="22 badges"><span class="bronze">●</span><span class="badgecount">22</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="spaetz has 2 accepted answers">28%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Jun '11, 08:10</strong> </span></p>
</div>
</div>
<div id="comments-container-23" class="comments-container">
<span id="18420"></span>
<div id="comment-18420" class="comment">
<div id="post-18420-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>map2image is another great option <a href="http://maps.stamen.com/m2i/#toner/768:512/12/37.7749/-122.4347">http://maps.stamen.com/m2i/#toner/768:512/12/37.7749/-122.4347</a></p>
</div>
<div id="comment-18420-info" class="comment-info">
<span class="comment-age">(13 Dec '12, 15:37)</span> <span class="comment-user userinfo">mcw</span>
</div>
</div>
</div>
<div id="comment-tools-23" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="676"></span>

<div id="answer-container-676" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-676-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-676-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-676-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>One other option: <a href="http://maperitive.net/">Maperitive</a></p>
<p>It can produce both <strong>bitmaps</strong>, <strong>SVG</strong>s and <strong>web tiles</strong> from OSM XML files (and/or web tiles, for that matter).</p>
<p>An example of Berlin rendered using simple wireframe rules: <img src="http://farm3.static.flickr.com/2783/4446075390_6f8222d420.jpg" alt="alt text" /></p>
<p>Click here for a larger images: <a href="http://www.flickr.com/photos/breki74/4446075390/sizes/l/in/photostream/"></a><a href="http://www.flickr.com/photos/breki74/4446075390/sizes/l/in/photostream/"></a><a href="http://www.flickr.com/photos/breki74/4446075390/sizes/l/in/photostream/">http://www.flickr.com/photos/breki74/4446075390/sizes/l/in/photostream/</a></p>
<p>More on exporting:</p>
<ul>
<li><a href="http://maperitive.net/docs/manual/Commands/ExportBitmap.html">export-bitmap command</a></li>
<li><a href="http://maperitive.net/docs/manual/Commands/ExportSvg.html">export-svg command</a></li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Aug '10, 17:08</strong></p>
<img src="https://secure.gravatar.com/avatar/591340f954c00c8208d5ffe668f50a05?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Breki&#39;s gravatar image" />
<p><span>Breki</span><br />
<span class="score" title="2040 reputation points"><span>2.0k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="18 badges"><span class="silver">●</span><span class="badgecount">18</span></span><span title="43 badges"><span class="bronze">●</span><span class="badgecount">43</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Breki has 5 accepted answers">10%</span></p>
</img>
</div>
</div>
<div id="comments-container-676" class="comments-container">
&#10;</div>
<div id="comment-tools-676" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-676-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="42364"></span>

<div id="answer-container-42364" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-42364-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42364-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-42364-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>See <span>"OSM on Paper" in our wiki</span></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Apr '15, 21:10</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-42364" class="comments-container">
&#10;</div>
<div id="comment-tools-42364" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42364-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="18407"></span>

<div id="answer-container-18407" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-18407-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18407-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-18407-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There's also Static map images. It lets you pick a location, image size, and place markers on the map. Then export it as a single image. Works great for making desktop wallpapers.</p>
<p>See <a href="https://wiki.openstreetmap.org/wiki/Static_map_images">https://wiki.openstreetmap.org/wiki/Static_map_images</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Dec '12, 01:20</strong></p>
<img src="https://secure.gravatar.com/avatar/639adad99d23636aba25de2606691408?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="OpenBrian&#39;s gravatar image" />
<p><span>OpenBrian</span><br />
<span class="score" title="56 reputation points">56</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="OpenBrian has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-18407" class="comments-container">
&#10;</div>
<div id="comment-tools-18407" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18407-form-container" class="comment-form-container">
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

