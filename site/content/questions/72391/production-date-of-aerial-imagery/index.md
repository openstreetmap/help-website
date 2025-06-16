+++
type = "question"
title = "production date of aerial imagery"
description = '''Is there a possibility to see the date of production of aerial imagery? Where I am interested, the images of Bing and Esri are very different.'''
date = "2020-01-07T07:45:00Z"
lastmod = "2020-01-14T14:56:00Z"
weight = 72391
keywords = [ "imagery", "mapping" ]
aliases = [ "/questions/72391" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [production date of aerial imagery](/questions/72391/production-date-of-aerial-imagery)

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
<span id="post-72391-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72391-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-72391-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is there a possibility to see the date of production of aerial imagery? Where I am interested, the images of Bing and Esri are <strong>very</strong> different.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-imagery" rel="tag" title="see questions tagged &#39;imagery&#39;">imagery</span> <span class="post-tag tag-link-mapping" rel="tag" title="see questions tagged &#39;mapping&#39;">mapping</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Jan '20, 07:45</strong></p>
<img src="https://secure.gravatar.com/avatar/93249e7a7a52d8d1d08cc69e60b0106a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="derFred&#39;s gravatar image" />
<p><span>derFred</span><br />
<span class="score" title="66 reputation points">66</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="derFred has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-72391" class="comments-container">
&#10;</div>
<div id="comment-tools-72391" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72391-form-container" class="comment-form-container">
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

<span id="72500"></span>

<div id="answer-container-72500" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72500-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72500-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-72500-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi derFred -- the background imagery providers are capable of tagging their tiles with metadata that indicates the image capture date or production date. And some map editing software is capable of showing that information. But the details are a little complicated.</p>
<ul>
<li><p>To see tile information in iD, go into Edit mode and zoom into the map, then hit Ctrl-Shift-B to bring up the "Background" info window. It will display a "Vintage" date (or date range) for the current imagery -- or "Unknown" if the imagery date is not known. You can also click the "Show Tiles" button at the bottom of the Background box to see info for individual tiles, in case you're in an area where some tiles are newer than others. <em>(Note that some browsers use the Ctrl-Shift-B shortcut for their own purposes! iD should be able to "steal" this key combo from the browser but it only seems to work if you're zoomed in close. It might take a few tries.)</em></p></li>
<li><p>To see the tile information in JOSM, you can load various imagery layers, zoom in, right-click the map, select the name of one of the loaded imagery layers, and select "Show tile info" for the tile at that map position. Various info fields will be shown, and may include the imagery date. (Ignore the lastModification and expirationTime fields -- those refer to the current download of the tile, not the imagery itself.)</p></li>
</ul>
<p>But here's where things get weird: In my area I have imagery available from Bing, ESRI, and Mapbox. To see the Bing date info, I have to use JOSM -- it shows "Vintage Unknown" in iD. To see the ESRI date info, I have to use iD -- no production date shows up in the JOSM tile info dialog. So it seems like both the publishing of these data fields and the software support are not exactly standardized. (Mapbox doesn't appear to publish any tile date metadata at all.)</p>
<p>See also this similar question: <a href="/questions/72212/how-to-ascertain-the-age-of-the-aerial-imagery-at-a-particular-location">https://help.openstreetmap.org/questions/72212/how-to-ascertain-the-age-of-the-aerial-imagery-at-a-particular-location</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Jan '20, 14:56</strong></p>
<img src="https://secure.gravatar.com/avatar/977d95e2184a885d9a01fb3297225872?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jmapb&#39;s gravatar image" />
<p><span>jmapb</span><br />
<span class="score" title="3387 reputation points"><span>3.4k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="61 badges"><span class="bronze">●</span><span class="badgecount">61</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jmapb has 22 accepted answers">22%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Jan '20, 16:51</strong> </span></p>
</div>
</div>
<div id="comments-container-72500" class="comments-container">
&#10;</div>
<div id="comment-tools-72500" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72500-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="72484"></span>

<div id="answer-container-72484" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72484-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72484-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-72484-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I don't think it could be possible to see the date of production of aerial imagery. The way around it is using Show historical imagery tool in Google Earth to determine how your study area looked like in the past, and then to see whether you will be able to tell where Bing imagery fits on the timeline - it's easy to do with areas with some sort of development undertaken recently. I don't think that credits are good indication of imagery date.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Jan '20, 08:28</strong></p>
<img src="https://secure.gravatar.com/avatar/4af421ee150ee53344589a9c1d896884?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gaurav%20Parajuli&#39;s gravatar image" />
<p><span>Gaurav Parajuli</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gaurav Parajuli has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-72484" class="comments-container">
&#10;</div>
<div id="comment-tools-72484" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72484-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="72494"></span>

<div id="answer-container-72494" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72494-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72494-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-72494-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi not a direct answer but use full maybe, use JOSM or any editor which offers a range of areal views. And have a look to find the most recent background and use that one.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Jan '20, 09:24</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
</div>
<div id="comments-container-72494" class="comments-container">
&#10;</div>
<div id="comment-tools-72494" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72494-form-container" class="comment-form-container">
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

