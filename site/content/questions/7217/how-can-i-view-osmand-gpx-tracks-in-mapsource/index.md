+++
type = "question"
title = "How can I view OSMAnd GPX tracks in Mapsource?"
description = '''I have generated a number of .GPX tracks using OSMAnd on my Samsung Galaxy. Mapsource cannot read them! Question 1 Is there a programme available to convert them to a Mapsource compatible format? Question 2 Where can I view these OSMAnd generated .gpx files?'''
date = "2011-08-20T17:28:00Z"
lastmod = "2019-10-24T19:35:00Z"
weight = 7217
keywords = [ "mapsource", "gpx", "osmand" ]
aliases = [ "/questions/7217" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [How can I view OSMAnd GPX tracks in Mapsource?](/questions/7217/how-can-i-view-osmand-gpx-tracks-in-mapsource)

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
<span id="post-7217-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7217-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-7217-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have generated a number of <em>.GPX tracks using OSMAnd on my Samsung Galaxy. Mapsource cannot read them! Question 1 Is there a programme available to convert them to a Mapsource compatible format? Question 2 Where can I view these OSMAnd generated</em> .gpx files?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-mapsource" rel="tag" title="see questions tagged &#39;mapsource&#39;">mapsource</span> <span class="post-tag tag-link-gpx" rel="tag" title="see questions tagged &#39;gpx&#39;">gpx</span> <span class="post-tag tag-link-osmand" rel="tag" title="see questions tagged &#39;osmand&#39;">osmand</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Aug '11, 17:28</strong></p>
<img src="https://secure.gravatar.com/avatar/cd4569f9fa1aac11eb6b19d6de309ea6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dcp&#39;s gravatar image" />
<p><span>dcp</span><br />
<span class="score" title="721 reputation points">721</span><span title="37 badges"><span class="badge1">●</span><span class="badgecount">37</span></span><span title="44 badges"><span class="silver">●</span><span class="badgecount">44</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dcp has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-7217" class="comments-container">
<span id="7220"></span>
<div id="comment-7220" class="comment">
<div id="post-7220-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the advice. I have posted the same question on the Samsung smartphone forum as well. I have loaded the gpx-file into JOSM: It works!</p>
</div>
<div id="comment-7220-info" class="comment-info">
<span class="comment-age">(20 Aug '11, 19:33)</span> <span class="comment-user userinfo">dcp</span>
</div>
</div>
<span id="7221"></span>
<div id="comment-7221" class="comment">
<div id="post-7221-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Upload them to osm (assuming that it'll let you, of course) as tracks that we can download and we can have a look!</p>
</div>
<div id="comment-7221-info" class="comment-info">
<span class="comment-age">(20 Aug '11, 19:39)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-7217" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7217-form-container" class="comment-form-container">
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

<span id="7225"></span>

<div id="answer-container-7225" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-7225-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7225-score" class="post-score" title="current number of votes">
7
</div>
<span id="post-7225-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>MapSource can be a bit fussy about what GPX files it will read. If the GPX file is not valid for some reason, it will usually just refuse to import it (with an unhelpful error message).</p>
<p>One way around this is to process the GPX file with <a href="http://www.gpsbabel.org/">GPS Babel</a>. Just set the input and output formats to GPX, and tick the box to process tracks. This usually produces a GPX file that MapSource can open.</p>
<p>It could be worth checking if you GPX file is valid, or what is wrong with it. See the instructions here: <a href="http://www.topografix.com/gpx_validation.asp">Validating GPX files</a>. Or upload your GPX file somewhere, and I will check it. If OsmAnd is not producing valid GPX files, it could be worth reporting it, to see if it can be fixed. I found a previous report (and suggested fix) here <a href="http://code.google.com/p/osmand/issues/detail?id=431">Issue 431 - osmand</a>, though I'm not sure if it has been implemented. Worth making sure you are using the latest version of OsmAnd, to check if it is fixed.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Aug '11, 20:51</strong></p>
<img src="https://secure.gravatar.com/avatar/aa505c046b1c010e997a7849c6f3dbbe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vclaw&#39;s gravatar image" />
<p><span>Vclaw</span><br />
<span class="score" title="9217 reputation points"><span>9.2k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="95 badges"><span class="silver">●</span><span class="badgecount">95</span></span><span title="141 badges"><span class="bronze">●</span><span class="badgecount">141</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vclaw has 41 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-7225" class="comments-container">
&#10;</div>
<div id="comment-tools-7225" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7225-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="7218"></span>

<div id="answer-container-7218" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-7218-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7218-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-7218-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can take the gpx files and <a href="http://wiki.openstreetmap.org/wiki/Upload">upload them to OpenStreetMap</a>. There you can use them for reference when editing.</p>
<p>As for Mapsource, this forum is about OpenStreetMap specific issues, so your best bet is to go to a Garmin forum. There's lots of documentation on the OSM wiki about <a href="http://wiki.openstreetmap.org/wiki/Garmin">using Garmin devices and software with OpenStreetMap</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Aug '11, 17:53</strong></p>
<img src="https://secure.gravatar.com/avatar/5f2082b86cc50d63c05f33f55166df2d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="emacsen&#39;s gravatar image" />
<p><span>emacsen</span><br />
<span class="score" title="1191 reputation points"><span>1.2k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="emacsen has 4 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-7218" class="comments-container">
<span id="15736"></span>
<div id="comment-15736" class="comment">
<div id="post-15736-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I had a trace that needed repair see this <a href="http://help.openstreetmap.org/questions/5993/repairing-a-gpx-trace">http://help.openstreetmap.org/questions/5993/repairing-a-gpx-trace</a></p>
</div>
<div id="comment-15736-info" class="comment-info">
<span class="comment-age">(31 Aug '12, 22:49)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
</div>
<div id="comment-tools-7218" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7218-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="71319"></span>

<div id="answer-container-71319" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71319-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71319-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-71319-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I have found that I can upload the OsmAnd gpx file to GPX Trackmaker, which is free to download and use. It will convert the file to xxx.gtm. Save this as a GPX exchange file. You can now open it in BaseCamp. Mapsource is an old app.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Oct '19, 16:42</strong></p>
<img src="https://secure.gravatar.com/avatar/1d97144a8a2bfece714383217e04f512?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Linbbo&#39;s gravatar image" />
<p><span>Linbbo</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Linbbo has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Oct '19, 16:43</strong> </span></p>
</div>
</div>
<div id="comments-container-71319" class="comments-container">
&#10;</div>
<div id="comment-tools-71319" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71319-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="71320"></span>

<div id="answer-container-71320" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71320-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71320-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-71320-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><img src="https://help.openstreetmap.org/upfiles/gps_track_editor_screen.JPG" alt="alt text" /></p>
<p>I sometime use Garmin Basecamp, but i think this program is simpler to use and OSM map background displays as well so try GPX Track Editor, see <a href="http://www.gpstrackeditor.com/">http://www.gpstrackeditor.com/</a> it's also on google play i think, so android as well as Windows, and it's free on windows.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Oct '19, 19:35</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Oct '19, 14:36</strong> </span></p>
</div>
</div>
<div id="comments-container-71320" class="comments-container">
&#10;</div>
<div id="comment-tools-71320" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71320-form-container" class="comment-form-container">
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

