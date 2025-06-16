+++
type = "question"
title = "Need help for editing after having done a survey!"
description = '''Dear OSM experts, I just did a survey outside in Bali, Indonesia to record new GPS traces with the Android application OSMAnd. Once I get back I uploaded the gps traces and everything was going well. The problem that I have and would appreciate to have your suggestions is when I was doing my survey ...'''
date = "2015-08-12T12:00:00Z"
lastmod = "2015-08-14T10:16:00Z"
weight = 44730
keywords = [ "notes", "editing", "osmand" ]
aliases = [ "/questions/44730" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Need help for editing after having done a survey!](/questions/44730/need-help-for-editing-after-having-done-a-survey)

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
<span id="post-44730-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44730-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-44730-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Dear OSM experts,</p>
<p>I just did a survey outside in Bali, Indonesia to record new GPS traces with the Android application OSMAnd. Once I get back I uploaded the gps traces and everything was going well.</p>
<p>The problem that I have and would appreciate to have your suggestions is when I was doing my survey I created an audio or picture note with OSMAnd before recording a new street so I could remember the street's name and the kind of surface and edit it properly in OSM.</p>
<p>I just realized when I try to edit my uploaded traces via the traces list on <a href="https://www.openstreetmap.org/">https://www.openstreetmap.org/</a> , the audio/picture notes are not included. I have my audio/picture notes on my OSMAnd and with the timestamps I can try to connect the dots I mean I try to see which gps trace goes with the good audio based on the timestamps.</p>
<p>For me it's very tedious and difficult to do, furthermore I'm afraid to do mistakes. Is someone has a pattern or know how to workaround to fix that problem ?</p>
<p>Thank you very much</p>
<p>Xavier</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-notes" rel="tag" title="see questions tagged &#39;notes&#39;">notes</span> <span class="post-tag tag-link-editing" rel="tag" title="see questions tagged &#39;editing&#39;">editing</span> <span class="post-tag tag-link-osmand" rel="tag" title="see questions tagged &#39;osmand&#39;">osmand</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Aug '15, 12:00</strong></p>
<img src="https://secure.gravatar.com/avatar/a8bf73e8d74ccbf4e233108b4cb6ccb1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ZoomBali&#39;s gravatar image" />
<p><span>ZoomBali</span><br />
<span class="score" title="110 reputation points">110</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ZoomBali has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-44730" class="comments-container">
&#10;</div>
<div id="comment-tools-44730" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44730-form-container" class="comment-form-container">
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

<span id="44754"></span>

<div id="answer-container-44754" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-44754-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44754-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-44754-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="ZoomBali has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I havent used OSMand in the way you mentioned, but it sounds very similar to how OSMtracker works.</p>
<p>In OSMtracker, everytime you do a survey, for that survey, the gpx trace, photos and voice notes are all put into a single folder. If you start another survey, a new folder is created and everything for that survey goes into that second folder and so on.</p>
<p>If OSMand does something similar, the following should work for you</p>
<ol>
<li>Hook your phone up to your PC and navigate to the OSMtracker folder in the file directory</li>
<li>Create a folder on the desktop and copy everything in the OSMtracker folder to that. There will likely be several folders if you've done several surveys</li>
<li>Open JOSM</li>
<li>In JOSM, go to File &gt; Open &gt; Navigate to the folder on your desktop &gt; Open it &gt; Open a survey folder &gt; Select the .gpx file (there should only be one) and load that into JOSM</li>
<li>Now you should see a GPS trace and icons for both your images and voice notes in JOSM. To view an image, click on the appropriate icon, to listen to a voice note do the same for those</li>
<li>Now just download data from OSM, make your edits and upload</li>
<li>Once you're done, if you havent already, upload the gpx file to OSM website</li>
</ol>
<p>I hope that helps. Sorry I can't give OSMand specific advice</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Aug '15, 21:48</strong></p>
<img src="https://secure.gravatar.com/avatar/9f0faef4659de616c82f448ff3f4e8e2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaCor&#39;s gravatar image" />
<p><span>DaCor</span><br />
<span class="score" title="1339 reputation points"><span>1.3k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="29 badges"><span class="bronze">●</span><span class="badgecount">29</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaCor has one accepted answer">2%</span></p>
</div>
</div>
<div id="comments-container-44754" class="comments-container">
&#10;</div>
<div id="comment-tools-44754" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44754-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="44731"></span>

<div id="answer-container-44731" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-44731-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44731-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-44731-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="https://wiki.openstreetmap.org/wiki/JOSM">JOSM</a> supports both <a href="https://wiki.openstreetmap.org/wiki/JOSM/Photomapping">photo mapping</a> as well as <a href="https://josm.openstreetmap.de/wiki/Help/AudioMapping">audio mapping</a>. There are also two more generic <a href="https://wiki.openstreetmap.org/wiki/Photo_mapping">photo mapping</a> and <a href="https://wiki.openstreetmap.org/wiki/Audio_mapping">audio mapping</a> pages in the OSM wiki. I haven't tried audio mapping myself yet so maybe someone else can write a more detailed answer.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Aug '15, 12:36</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Aug '15, 12:38</strong> </span></p>
</div>
</div>
<div id="comments-container-44731" class="comments-container">
<span id="44734"></span>
<div id="comment-44734" class="comment">
<div id="post-44734-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I just copy the photo's from my Smartphone onto the disk of the computer where I do the editing with JOSM. JOSM can open the photo's and place them correctly "on the map" without need for the track.</p>
<p>As for the audit files, it seems that some people had problems to open them in JOSM, see this <a href="https://josm.openstreetmap.de/ticket/8765">ticket</a>. I don't use audiofiles, so I don't know whether it is still a problem.</p>
</div>
<div id="comment-44734-info" class="comment-info">
<span class="comment-age">(12 Aug '15, 13:38)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="44735"></span>
<div id="comment-44735" class="comment">
<div id="post-44735-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>is this explanation on the <a href="https://groups.google.com/forum/#!searchin/osmand/josm/osmand/l3Z2rDSvQ6g/EXSkodv97ZgJ">OsmAnd forum</a> of any help ?</p>
</div>
<div id="comment-44735-info" class="comment-info">
<span class="comment-age">(12 Aug '15, 13:44)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="44737"></span>
<div id="comment-44737" class="comment">
<div id="post-44737-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>If your photo has location in the EXIF data it should be placed properly without the associated track.</p>
<p>But even if you have turned that off, JOSM can use waypoint data in the GPX file to properly locate the photo (and, I think, the sound file).</p>
<p>Unfortunately, when you upload the GPX file to OSM the waypoints are stripped off so the photos and sound files cannot be located properly. I do my edits with my GPX files locally with JOSM before uploading to OSM for that reason.</p>
</div>
<div id="comment-44737-info" class="comment-info">
<span class="comment-age">(12 Aug '15, 15:36)</span> <span class="comment-user userinfo">n76</span>
</div>
</div>
</div>
<div id="comment-tools-44731" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44731-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="44768"></span>

<div id="answer-container-44768" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-44768-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44768-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-44768-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Thank you DaCor and scai for helping me,</p>
<p>I have an alternative to suggest but before let me explain what I tried.</p>
<p>Dacor I tried your way because you gave me simple steps to follow otherwise when I try to read the wiki documentations links it's difficult to follow and you need to open a new tab about other OSM Terminologies and spend hours to read and try to understand.</p>
<p>With Android OSMtracker when I upload a GPX file, I see the audio file (in format .3gpp) in my JOSM editor but when I try to open it apparently JOSM cannot open this king of file. I found this support ticket about the issue but again (I'm not a programmer) I couldn't follow properly the answers. <a href="https://josm.openstreetmap.de/ticket/5805">https://josm.openstreetmap.de/ticket/5805</a></p>
<p>They proposed to download an older version of JOSM which I tried (version 3376 on Windows). Now I can open the audio notes on JOSM but there's no sound, I tried different media players (VLC, SPlayer) but it doesn't work.</p>
<p>Instead of an audio notes with OSMtracker you can take “Text note” for instance ( Street Paradise, Paved road). For us it's enough for the tags (street name and kind of street) but you can add what you want. This note is then displayed next to the GPS trace on JOSM so it's easy after that to Edit the new GPS trace without being confused with many audio files and trying to match the time stamps of the audio files with the GPX files.</p>
<p>Here's a simple step-by-step guide (For Dummies) to go outside for a survey (recording GPS trace) with a smartphone and editing the GPS traces in JOSM and upload them in OSM server.</p>
<ol>
<li>Open the application “OSMTracker for Android” (first download it :) )</li>
<li>Click on the “+” sign to start a new GPS trace.</li>
<li>Wait few seconds for GPS fix.</li>
<li>Click on “Text note” and write the name of the street and the state of the street (ex: Paved, Street Uluwatu).</li>
<li>To finish a GPS trace click on the casette icon at the upper right side to save the GPS trace.</li>
<li>Redo the steps 1 to 6 for adding more GPS traces.</li>
<li>Once back home for each GPS traces recorded on OSMTracker, click and hold on the GPS trace and click on “Export as GPX”.</li>
<li>Hook your phone up to your PC and on your PC navigate to the OSMtracker folder in the file directory.</li>
<li>Create a folder on the desktop and copy everything in the OSMtracker folder to that. There will likely be several folders if you've done several GPS trace.</li>
<li>Open JOSM (first download it :) )</li>
<li>In JOSM, go to File &gt; Open &gt; Navigate to the folder on your desktop &gt; Open it &gt; Open a GPS trace folder &gt; Select the .gpx file (there should only be one) and load that into JOSM</li>
<li>Next to the GPS trace you should see the “text note” (ex: Paved, Street Uluwatu).</li>
<li>Click on the download icon, the arrow down “Download Map data from the OSM server”.</li>
<li>Add the new street by selecting the icon “Draw nodes” and draw the street above the GPS trace.</li>
<li>For adding the tags, click on “Presets” and select the appropriate element (ex; highways, shops etc)</li>
<li>Fill the empty input boxes and click “Apply Preset”</li>
<li>Redo the steps 11 to 16 for the other GPS traces.</li>
<li>When you are done upload the GPS traces to OSM server by clicking on the icon with the green arrow up “Upload all changes in the active data layer to the OSM server”</li>
<li>Follow the instructions on the pop-up window (enter your OSM credentials)</li>
</ol>
<p>Voilà, it's done!</p>
<p>Xavier</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Aug '15, 10:16</strong></p>
<img src="https://secure.gravatar.com/avatar/a8bf73e8d74ccbf4e233108b4cb6ccb1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ZoomBali&#39;s gravatar image" />
<p><span>ZoomBali</span><br />
<span class="score" title="110 reputation points">110</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ZoomBali has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Aug '15, 10:17</strong> </span></p>
</div>
</div>
<div id="comments-container-44768" class="comments-container">
&#10;</div>
<div id="comment-tools-44768" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44768-form-container" class="comment-form-container">
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

