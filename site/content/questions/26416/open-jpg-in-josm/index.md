+++
type = "question"
title = "Open JPG in JOSM"
description = '''In JOSM I would like to open a geo tagged jpg file I took with my phone. It seems to require a GPX file to do this, which I do not have. (I took the photo as a visual note to change a particular OSM object). How do I do this? thanks'''
date = "2013-09-17T04:54:00Z"
lastmod = "2013-09-19T13:06:00Z"
weight = 26416
keywords = [ "josm", "photomapping", "jpg" ]
aliases = [ "/questions/26416" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Open JPG in JOSM](/questions/26416/open-jpg-in-josm)

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
<span id="post-26416-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26416-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-26416-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>In JOSM I would like to open a geo tagged jpg file I took with my phone. It seems to require a GPX file to do this, which I do not have. (I took the photo as a visual note to change a particular OSM object).</p>
<p>How do I do this?</p>
<p>thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-photomapping" rel="tag" title="see questions tagged &#39;photomapping&#39;">photomapping</span> <span class="post-tag tag-link-jpg" rel="tag" title="see questions tagged &#39;jpg&#39;">jpg</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Sep '13, 04:54</strong></p>
<img src="https://secure.gravatar.com/avatar/c386bfc33fe5fc783e26c89ed54a85b4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GavinX&#39;s gravatar image" />
<p><span>GavinX</span><br />
<span class="score" title="56 reputation points">56</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GavinX has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Sep '13, 23:42</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/aa505c046b1c010e997a7849c6f3dbbe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vclaw&#39;s gravatar image" />
<p><span>Vclaw</span><br />
<span class="score" title="9217 reputation points"><span>9.2k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="95 badges"><span class="silver">●</span><span class="badgecount">95</span></span><span title="141 badges"><span class="bronze">●</span><span class="badgecount">141</span></span></p>
</div>
</div>
<div id="comments-container-26416" class="comments-container">
&#10;</div>
<div id="comment-tools-26416" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26416-form-container" class="comment-form-container">
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

<span id="26484"></span>

<div id="answer-container-26484" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-26484-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26484-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-26484-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>For opening JPG photos in JOSM, you can just go to File menu -&gt; Open, and select the photos. Or drag and drop the files onto the JOSM window. Then if the photos are geotagged, JOSM will show them on the map. This is part of the core JOSM program, no need for any plugins.</p>
<p>If JOSM prompts for "Correlate image with GPX track", that means the photos are not geotagged. Or they are not geotagged in a way that JOSM understands.</p>
<p>You could use other software to check if the images are geotagged. eg if using a recent version of Windows, right click on the JPG, then select "Properties", then select the "Details" tab. There should be several GPS tags for latitude/longitude. Or you can try IrfanView, or Geosetter, they can also show any GPS tags.</p>
<p>If none of this software shows tags for coordinates, it suggests your phone is not actually geotagging the photos. Or it is doing it in some non-standard way. So check the settings on your phone and camera app, or try another app. Note that even if geotagging is enabled, it might take a while for the phone to get a GPS fix. So you might have to start the camera app, then wait for it to get the location, before taking any photos.</p>
<p>If other software shows your photos are tagged, then it could be a bug with JOSM. So first try out the latest development version of JOSM, it may have been fixed recently. If that doesn't work, you can report a bug it on the <a href="http://josm.openstreetmap.de/">JOSM trac</a>, preferably with a link to an example JPG.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Sep '13, 23:38</strong></p>
<img src="https://secure.gravatar.com/avatar/aa505c046b1c010e997a7849c6f3dbbe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vclaw&#39;s gravatar image" />
<p><span>Vclaw</span><br />
<span class="score" title="9217 reputation points"><span>9.2k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="95 badges"><span class="silver">●</span><span class="badgecount">95</span></span><span title="141 badges"><span class="bronze">●</span><span class="badgecount">141</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vclaw has 41 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-26484" class="comments-container">
&#10;</div>
<div id="comment-tools-26484" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26484-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="26424"></span>

<div id="answer-container-26424" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-26424-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26424-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-26424-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Check the JOSM plugins list:</p>
<p><a href="http://josm.openstreetmap.de/wiki/Plugins">http://josm.openstreetmap.de/wiki/Plugins</a></p>
<p>especially the <a href="http://wiki.openstreetmap.org/wiki/JOSM/Plugins/ImportImagePlugin">ImportImagePlugin</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Sep '13, 10:31</strong></p>
<img src="https://secure.gravatar.com/avatar/0e92f2d89853fd4e04c4b40a921e519b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pieren&#39;s gravatar image" />
<p><span>Pieren</span><br />
<span class="score" title="9847 reputation points"><span>9.8k</span></span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="157 badges"><span class="bronze">●</span><span class="badgecount">157</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pieren has 34 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-26424" class="comments-container">
<span id="26500"></span>
<div id="comment-26500" class="comment">
<div id="post-26500-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>The PicLayer and ImportImage plugins are for loading background images as a layer. eg aerial imagery, or a scanned map.</p>
<p>They are not necessary (and won't work) for a normal 'on the ground' photo.</p>
</div>
<div id="comment-26500-info" class="comment-info">
<span class="comment-age">(19 Sep '13, 13:06)</span> <span class="comment-user userinfo">Vclaw</span>
</div>
</div>
</div>
<div id="comment-tools-26424" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26424-form-container" class="comment-form-container">
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

