+++
type = "question"
title = "Import My Maps from my Google account to OSMAnd app?"
description = '''Is it possible to import the maps I have made in Google Maps/My Places into the Android app for OSM? Since recently Google have disabled the possibility to view my personal maps in the Google Maps Android app.'''
date = "2013-08-23T12:31:00Z"
lastmod = "2015-06-11T23:54:00Z"
weight = 25683
keywords = [ "import", "osmand", "google_maps" ]
aliases = [ "/questions/25683" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [Import My Maps from my Google account to OSMAnd app?](/questions/25683/import-my-maps-from-my-google-account-to-osmand-app)

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
<span id="post-25683-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25683-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-25683-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is it possible to import the maps I have made in Google Maps/My Places into the Android app for OSM?</p>
<p>Since recently Google have disabled the possibility to view my personal maps in the Google Maps Android app.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span> <span class="post-tag tag-link-osmand" rel="tag" title="see questions tagged &#39;osmand&#39;">osmand</span> <span class="post-tag tag-link-google_maps" rel="tag" title="see questions tagged &#39;google_maps&#39;">google_maps</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Aug '13, 12:31</strong></p>
<img src="https://secure.gravatar.com/avatar/9002dfafe881735c449b8c288728d72b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lagerstrom&#39;s gravatar image" />
<p><span>Lagerstrom</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lagerstrom has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Aug '13, 02:13</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-25683" class="comments-container">
&#10;</div>
<div id="comment-tools-25683" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-25683-form-container" class="comment-form-container">
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

<span id="25691"></span>

<div id="answer-container-25691" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-25691-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25691-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-25691-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Google My Maps does have an option to export as a KML file. If you are using the "classic My Maps", then it is in the left hand sidebar, just underneath the title. There is a link for "KML". If you are using the new "Maps Engine", then look in the top left box, underneath the title there is a folder icon. Click on that folder, then choose "Export to KML".</p>
<p>For using the KML file in OsmAnd, and I'm not sure if it is possible to load it directly. If you want to show lines on the map, then you can convert it to a GPX track, eg using GPSBabel. Then copy it to the osmand/tracks directory, and enable it in OsmAnd by going to menu &gt; Define view &gt; GPX track. See <a href="http://code.google.com/p/osmand/wiki/HowToViewGPXTracks">How to view GPX tracks</a></p>
<p>For a more advanced map, you could convert from KML to .osm format. Then use OsmAndMapCreator to create a map in OsmAnd obf format. Some more details: <a href="http://code.google.com/p/osmand/wiki/CreatingKMLFile">Using KML files</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Aug '13, 16:16</strong></p>
<img src="https://secure.gravatar.com/avatar/aa505c046b1c010e997a7849c6f3dbbe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vclaw&#39;s gravatar image" />
<p><span>Vclaw</span><br />
<span class="score" title="9217 reputation points"><span>9.2k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="95 badges"><span class="silver">●</span><span class="badgecount">95</span></span><span title="141 badges"><span class="bronze">●</span><span class="badgecount">141</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vclaw has 41 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-25691" class="comments-container">
&#10;</div>
<div id="comment-tools-25691" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-25691-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="43541"></span>

<div id="answer-container-43541" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43541-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43541-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-43541-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It's possible with a few steps. Ashraf Fouad has written a <a href="http://ashraffouad.blogspot.com/2013/08/moving-favorites-from-google-maps-to.html">thorough blog post with detailed steps on how to do this</a>.</p>
<p>I've exported my own starred locations using the method noted as 1-a in the blog post using the online tool at <a href="http://gexport.somee.com/">http://gexport.somee.com/</a> . Ashraf noted that it didn't work for him but didn't note why. I (too) needed to do some tweaking to get the conversion tool working. This was likely because I had so many Google Bookmarks that it seemed to choke the tool.</p>
<p>What I did was I edit your exported Google Bookmarks file so that it only contained rows that had a location, the starred locations (and a few other locations that were in the bookmarks, IIRC). The way I did that was by first (after making a copy of the original bookmarks export file) opening the bookmarks file in a text editor, them cut-pasting all the bookmarks to my favorite spreadsheet application, then filtering all rows without the location identifier (.. can't remember what it is but you'll see it when you open it). Then marking those rows and deleting them leaving me with only rows with locations and copy-pasting those rows back to the bookmarks file. After this I was able to get the gexport.somee.com tool to convert my bookmarks into a KML file. And then converted to GPX and imported to OsmAnd.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Jun '15, 23:54</strong></p>
<img src="https://secure.gravatar.com/avatar/280f61ca58a2e8c3d7bc877ed8a3def2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jaakkoh&#39;s gravatar image" />
<p><span>jaakkoh</span><br />
<span class="score" title="548 reputation points">548</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jaakkoh has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-43541" class="comments-container">
&#10;</div>
<div id="comment-tools-43541" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43541-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="25686"></span>

<div id="answer-container-25686" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-25686-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25686-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-25686-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>No, OSMand does not have that feature, as far as I know.</p>
<p>I also think it unlikely that any other app will have the feature if Google has decided that their official app should not have it. It is their data (not yours) and their API, so they are free to decide whether to give access on Android.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Aug '13, 13:08</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-25686" class="comments-container">
&#10;</div>
<div id="comment-tools-25686" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-25686-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="36039"></span>

<div id="answer-container-36039" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-36039-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-36039-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-36039-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Seems that the recent version 1.8.3 converts/imports from KML, but after many searches I still unable to do it. The clue is that feature would be in My Places.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Aug '14, 09:39</strong></p>
<img src="https://secure.gravatar.com/avatar/8fd5a2d84e0e6df37ae05e16440c035f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jener&#39;s gravatar image" />
<p><span>Jener</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jener has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-36039" class="comments-container">
&#10;</div>
<div id="comment-tools-36039" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-36039-form-container" class="comment-form-container">
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

