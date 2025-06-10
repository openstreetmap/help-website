+++
type = "question"
title = "Export administrative boundaries of a country for use with an external application"
description = '''Hey Guys,  I am trying to create a image of Germany with the borders (of admin_level=6) filled with colour, depending on different (statistical) indicators. Is it possible to export a map with this borders and load it in to my Map-Explorer? thanks a lot! Dole edit: i have to say i am not used to do ...'''
date = "2011-03-24T10:58:00Z"
lastmod = "2012-10-02T12:43:00Z"
weight = 4036
keywords = [ "map", "borders", "export", "colour", "fill" ]
aliases = [ "/questions/4036" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Export administrative boundaries of a country for use with an external application](/questions/4036/export-administrative-boundaries-of-a-country-for-use-with-an-external-application)

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
<span id="post-4036-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4036-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-4036-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hey Guys,</p>
<p>I am trying to create a image of Germany with the borders (of admin_level=6) filled with colour, depending on different (statistical) indicators. Is it possible to export a map with this borders and load it in to my Map-Explorer?</p>
<p>thanks a lot! Dole</p>
<p>edit: i have to say i am not used to do stuff with geographic-tool cause i am a "socialstudies guy"... OSM is to detailed, but i need the lvl6 borders, so i can colour them. i guess there are about 400 of areas in Ger. would be much work to fill them by hand.</p>
<p>hope my Prob got a bit clearer :)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span> <span class="post-tag tag-link-borders" rel="tag" title="see questions tagged &#39;borders&#39;">borders</span> <span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span> <span class="post-tag tag-link-colour" rel="tag" title="see questions tagged &#39;colour&#39;">colour</span> <span class="post-tag tag-link-fill" rel="tag" title="see questions tagged &#39;fill&#39;">fill</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Mar '11, 10:58</strong></p>
<img src="https://secure.gravatar.com/avatar/9fd76bbf29d7dc9eddb9d39a78b7c174?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dole&#39;s gravatar image" />
<p><span>Dole</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dole has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Mar '11, 14:32</strong> </span></p>
</div>
</div>
<div id="comments-container-4036" class="comments-container">
&#10;</div>
<div id="comment-tools-4036" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4036-form-container" class="comment-form-container">
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

<span id="4039"></span>

<div id="answer-container-4039" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-4039-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4039-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-4039-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can get all administrative boundaries in several ways:</p>
<ol>
<li>You could make a call at one of the <a href="http://wiki.openstreetmap.org/wiki/Xapi">Xapi</a> filtering by location (bounding box) and tag (admin_level). Note that the Xapi is mostly overloaded these days, <a href="http://wiki.openstreetmap.org/wiki/Platform_Status">check current status here</a>.</li>
<li>You could take a germany extract, for instance from geofabrik, and extract the boundaries with <a href="http://wiki.openstreetmap.org/wiki/Osmosis">Osmosis</a></li>
<li>If I recall right, <a href="http://www.geofabrik.de/en/data/shapefiles.html">geofabrik</a> offers shapefiles from OSM-Data, and there might be a boundaries file for Germany in their download section , <a href="http://download.geofabrik.de/osm/">see here</a>.</li>
<li>If you wanted only admin_level=4 and 2 you could download them with josm, but for admin_level=6 this might be too much effort.</li>
</ol>
<p>I don't know which formats are supported by Map-Explorer, but if it doesn't support osm-xml directly you could load the osm-file into Josm and export it as GPX, which most geo-applications are able to read. There are also tools available to convert osm to shapefile. More help on this topic and alternative programs can be found <a href="http://wiki.openstreetmap.org/wiki/Shapefiles">in the wiki</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Mar '11, 11:44</strong></p>
<img src="https://secure.gravatar.com/avatar/f09c0b7a655fed386e070e036e2da248?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dieterdreist&#39;s gravatar image" />
<p><span>dieterdreist</span><br />
<span class="score" title="3677 reputation points"><span>3.7k</span></span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="67 badges"><span class="bronze">●</span><span class="badgecount">67</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dieterdreist has 4 accepted answers">3%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Mar '11, 21:05</strong> </span></p>
</div>
</div>
<div id="comments-container-4039" class="comments-container">
&#10;</div>
<div id="comment-tools-4039" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4039-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="16544"></span>

<div id="answer-container-16544" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-16544-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16544-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-16544-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It <strong>can</strong> be done with JOSM, but it sohohoh difficult too explain that I won't. It so dangerous too. A novice could erase nation wide data with a single click. Always experiment such things with (J)OSM without a password and best on an alternate server. I've done it with Belgium, but it wouldn't work with Switzerland. CH don't put subareas in boundary relations (believe me as I say it :-)).</p>
<p>As Frederik said, your best bet is a ready made map of some kind. Look up Google with searcher like "Germany map administrative svg", best in German. SVG is important. It's a vector format that will scale very well and allow you to change the picture easily with a program like Inkscape, or change it to another format. This is my third hit, just to show you the kind of things: <a href="http://en.wikipedia.org/wiki/File:Map_Germany_L%C3%A4nder-de.svg">http://en.wikipedia.org/wiki/File:Map_Germany_L%C3%A4nder-de.svg</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Sep '12, 00:56</strong></p>
<img src="https://secure.gravatar.com/avatar/22d0547d929d81aa90014a6f0aef484a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GentilPapou&#39;s gravatar image" />
<p><span>GentilPapou</span><br />
<span class="score" title="160 reputation points">160</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GentilPapou has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-16544" class="comments-container">
&#10;</div>
<div id="comment-tools-16544" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16544-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="16604"></span>

<div id="answer-container-16604" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-16604-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16604-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-16604-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Use the VG2500 dataset of the Bundesamt für Kartografie and Geodäsie: <a href="http://www.bkg.bund.de/nn_149566/EN/News/01News/N2011/2011">http://www.bkg.bund.de/nn_149566/EN/News/01News/N2011/2011</a><strong>09</strong>15-VG2500__04-09-2011.html</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Oct '12, 12:36</strong></p>
<img src="https://secure.gravatar.com/avatar/806d5a652505590a9eba797ad5bea8db?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gormo&#39;s gravatar image" />
<p><span>gormo</span><br />
<span class="score" title="2928 reputation points"><span>2.9k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="26 badges"><span class="silver">●</span><span class="badgecount">26</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gormo has 13 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-16604" class="comments-container">
<span id="16605"></span>
<div id="comment-16605" class="comment">
<div id="post-16605-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The download link is <a href="http://www.geodatenzentrum.de/geodaten/gdz_rahmen.gdz_div?gdz_spr=eng&amp;gdz_akt_zeile=5&amp;gdz_anz_zeile=4&amp;gdz_unt_zeile=17&amp;gdz_user_id=0">http://www.geodatenzentrum.de/geodaten/gdz_rahmen.gdz_div?gdz_spr=eng&amp;gdz_akt_zeile=5&amp;gdz_anz_zeile=4&amp;gdz_unt_zeile=17&amp;gdz_user_id=0</a></p>
</div>
<div id="comment-16605-info" class="comment-info">
<span class="comment-age">(02 Oct '12, 12:37)</span> <span class="comment-user userinfo">gormo</span>
</div>
</div>
<span id="16606"></span>
<div id="comment-16606" class="comment">
<div id="post-16606-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>...and if you just want a SVG you could get it from <a href="http://www.geodatenzentrum.de/geodaten/gdz_rahmen.gdz_div?gdz_spr=eng&amp;gdz_akt_zeile=5&amp;gdz_anz_zeile=5&amp;gdz_user_id=0">http://www.geodatenzentrum.de/geodaten/gdz_rahmen.gdz_div?gdz_spr=eng&amp;gdz_akt_zeile=5&amp;gdz_anz_zeile=5&amp;gdz_user_id=0</a></p>
</div>
<div id="comment-16606-info" class="comment-info">
<span class="comment-age">(02 Oct '12, 12:43)</span> <span class="comment-user userinfo">gormo</span>
</div>
</div>
</div>
<div id="comment-tools-16604" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16604-form-container" class="comment-form-container">
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

