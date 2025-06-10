+++
type = "question"
title = "Adding data to OSM file before processing with mkgmap"
description = '''I generate my own garmin map files using mkgmap. I want to be able to search for addresses using postcodes in the uk. This data isn&#x27;t widely entered on OSM and its not going to be until we get a paf file. However the office of national statistics publishes a postcode dump which would be sufficient f...'''
date = "2014-06-05T08:32:00Z"
lastmod = "2017-07-09T12:48:00Z"
weight = 33698
keywords = [ "mkgmap", "postcode", "uk" ]
aliases = [ "/questions/33698" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Adding data to OSM file before processing with mkgmap](/questions/33698/adding-data-to-osm-file-before-processing-with-mkgmap)

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
<span id="post-33698-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33698-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-33698-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I generate my own garmin map files using mkgmap. I want to be able to search for addresses using postcodes in the uk. This data isn't widely entered on OSM and its not going to be until we get a paf file. However the office of national statistics publishes a postcode dump which would be sufficient for my purposes. Essentially I want to download the latest OSM data for the uk and the latest ons postcode file and combine them before putting through mkgmap. What is the best way to achieve this?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-mkgmap" rel="tag" title="see questions tagged &#39;mkgmap&#39;">mkgmap</span> <span class="post-tag tag-link-postcode" rel="tag" title="see questions tagged &#39;postcode&#39;">postcode</span> <span class="post-tag tag-link-uk" rel="tag" title="see questions tagged &#39;uk&#39;">uk</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Jun '14, 08:32</strong></p>
<img src="https://secure.gravatar.com/avatar/b53da6e71be71966b21548ed7e92a57f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mcgin&#39;s gravatar image" />
<p><span>mcgin</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mcgin has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-33698" class="comments-container">
&#10;</div>
<div id="comment-tools-33698" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33698-form-container" class="comment-form-container">
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

<span id="33859"></span>

<div id="answer-container-33859" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-33859-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33859-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-33859-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I would simply create two separate layers: one for the OSM data, the other for the ONS or CodePoint Open data. You can then merge these using the --gmapsupp flag of mkgmap.</p>
<p>The more difficult problem is exactly how to transform the Code Point Open data so as to be usable with a Garmin device. Simply ensuring every postcode is tagged in this way "addr:postcode=SW1A 1AA" may not be adequate for your purposes (I presume using postcodes as a geolocation code, as used in commercial satnavs is one use case).</p>
<p>I am not familiar with the status of the address branch of the mkgmap code.</p>
<p>Extending the postcode data to produce approximate locations for actual addresses is theoretically possible (use the 12 million addresses from Land Registry Prices Paid and those from the National Register of Social Housing: both are Open Data sets licensed under OGL), but there are problems in identifying how house numbers increment on particular road segments. Note that most of this latter aspect could be done with OpenData sets without having to use OSM. In the next few months it is likely that some of these data sets will be made available in a modified, and more useful form, on <a href="http://openaddresses.io/">openaddresses.io</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Jun '14, 19:06</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-33859" class="comments-container">
<span id="33862"></span>
<div id="comment-33862" class="comment">
<div id="post-33862-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>So it's the creation of that second layer that I'm after, is it simply another IMG file or what format does it need to be in?</p>
</div>
<div id="comment-33862-info" class="comment-info">
<span class="comment-age">(10 Jun '14, 20:52)</span> <span class="comment-user userinfo">mcgin</span>
</div>
</div>
<span id="33863"></span>
<div id="comment-33863" class="comment">
<div id="post-33863-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Yes just another img file, probably also created with the gmapsupp option (necessary if your source needs to be split into several files)</p>
<p>something like mkgmap --gmapsupp gb_osm_gmapsupp.img ons_gmapsupp.img</p>
</div>
<div id="comment-33863-info" class="comment-info">
<span class="comment-age">(10 Jun '14, 21:17)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="33864"></span>
<div id="comment-33864" class="comment">
<div id="post-33864-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>So the next question is how to convert the postcode file to an IMG file. I haven't seen any tools that do this, and I'm not sure what the format of the IMG file is in order to do it manually.</p>
</div>
<div id="comment-33864-info" class="comment-info">
<span class="comment-age">(10 Jun '14, 21:47)</span> <span class="comment-user userinfo">mcgin</span>
</div>
</div>
<span id="33869"></span>
<div id="comment-33869" class="comment">
<div id="post-33869-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You need it as an OSM XML file, so options might be ogr2ogr, QGIS (delimited text layer, save as an OGR compatible layer) &amp; JOSM, or load into PostGIS and use SQL to transform to the snapshot schema format &amp; Osmosis to read it into an OSM file. This may be best as a separate question.</p>
</div>
<div id="comment-33869-info" class="comment-info">
<span class="comment-age">(11 Jun '14, 07:54)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="33898"></span>
<div id="comment-33898" class="comment">
<div id="post-33898-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Won't that result in negative ids in the OSM file as its not synced with the main OSM... Are negative ids even a problem?</p>
</div>
<div id="comment-33898-info" class="comment-info">
<span class="comment-age">(12 Jun '14, 06:26)</span> <span class="comment-user userinfo">mcgin</span>
</div>
</div>
<span id="56965"></span>
<div id="comment-56965" class="comment not_top_scorer">
<div id="post-56965-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>So anyway, 3 years ago someone asked a valid question. Pity there was no reply, as I'm in the same boat with no experience how to paddle.</p>
<p>I actually have a comma delimited file: lat, long, postcode, over 2.5 million entries.</p>
<p>I would reckon 85% are negative numbers, being UK postcodes. So if I subtracted these numbers from 360 degrees, would that work?</p>
<p>After that, then what would I do?</p>
</div>
<div id="comment-56965-info" class="comment-info">
<span class="comment-age">(08 Jul '17, 21:17)</span> <span class="comment-user userinfo">Me Again</span>
</div>
</div>
<span id="56972"></span>
<div id="comment-56972" class="comment not_top_scorer">
<div id="post-56972-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>No longitude is a negative number. And the reply I gave then is still valid now. Convert your file into a suitable OSM form &amp; run mkgmap over the output.</p>
</div>
<div id="comment-56972-info" class="comment-info">
<span class="comment-age">(09 Jul '17, 12:48)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-33859" class="comment-tools">
<span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-33859-form-container" class="comment-form-container">
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

