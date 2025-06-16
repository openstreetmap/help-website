+++
type = "question"
title = "Maps to Static Image to be stored on a &quot;mobile&quot; application"
description = '''Hi, I have to develop an application that will find the map, from an address/postcode, and create a static image of the map. The reason being because that image will be stored on a &quot;mobile&quot; application that has limited internet access and indeed very limited bandwidth (and will be used by public - s...'''
date = "2013-06-05T16:41:00Z"
lastmod = "2013-06-06T09:50:00Z"
weight = 23034
keywords = [ "map", "image", "static" ]
aliases = [ "/questions/23034" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Maps to Static Image to be stored on a "mobile" application](/questions/23034/maps-to-static-image-to-be-stored-on-a-mobile-application)

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
<span id="post-23034-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23034-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-23034-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I have to develop an application that will find the map, from an address/postcode, and create a static image of the map. The reason being because that image will be stored on a "mobile" application that has limited internet access and indeed very limited bandwidth (and will be used by public - so lots of people).</p>
<p>Obviously the solution has to be cheap (ideally free) and quick so I'm wondering if OpenStreetMap could be used for this? (BTW the application is in .Net)</p>
<p>I would greatly appreciate if you could point me in the right direction for this issue and if OpenStreetMap can't be used if you know of any other providers that could be used for this?</p>
<p>Kind regards Sidharth</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span> <span class="post-tag tag-link-image" rel="tag" title="see questions tagged &#39;image&#39;">image</span> <span class="post-tag tag-link-static" rel="tag" title="see questions tagged &#39;static&#39;">static</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Jun '13, 16:41</strong></p>
<img src="https://secure.gravatar.com/avatar/612176c228033ecb5963e58a006cbda4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sid&#39;s gravatar image" />
<p><span>Sid</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sid has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Nov '13, 13:29</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-23034" class="comments-container">
&#10;</div>
<div id="comment-tools-23034" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23034-form-container" class="comment-form-container">
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

<span id="23048"></span>

<div id="answer-container-23048" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-23048-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23048-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-23048-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Your question is largely a rendering question and many of the responses you will see if you enter "render map" into the search box will likely be applicable.</p>
<p>The standard way to render map images is setting up a server with PostGIS and Mapnik, import data with osm2pgsql, and then you can use various tools e.g. nik2img.py to create PNG images of any size, in any projection, for any area of the world. You could then write a batch job that generates all the static images you need. If the images are all in one area, e.g. all in India, then importing the data is relatively quick. If the images are across the world then you have to import a world-wide data set which is slower.</p>
<p>There are many other methods to achieve what you want; one of them would consist of using a "static map" script to download ready-made map tiles from someone else's server, or even use a complete "static map" service offered by someone else. Such use is bound by the usage policies of the service in question, so before you download a large number of tiles or images you should check whether you're not violating their terms. Some static map options are listed on the wiki: <a href="https://wiki.openstreetmap.org/wiki/Static_map_images">https://wiki.openstreetmap.org/wiki/Static_map_images</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Jun '13, 09:50</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-23048" class="comments-container">
&#10;</div>
<div id="comment-tools-23048" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23048-form-container" class="comment-form-container">
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

