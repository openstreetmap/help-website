+++
type = "question"
title = "How to adjust compass angle exif tag on photos to follow a gpx track?"
description = '''I&#x27;ve been taking photos with a sports camera (a Replay XD1080, like a GoPro) on my bike and recording a GPX track with my phone. This is a great set up, because the camera is designed to be mounted on a bicycle&#x27;s handlebars, is waterproof, and has a mode where it takes one photo every 3 seconds.  I ...'''
date = "2017-05-17T19:32:00Z"
lastmod = "2017-05-19T11:46:00Z"
weight = 56215
keywords = [ "photos", "photomapping", "mapillary", "exif", "josm" ]
aliases = [ "/questions/56215" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [How to adjust compass angle exif tag on photos to follow a gpx track?](/questions/56215/how-to-adjust-compass-angle-exif-tag-on-photos-to-follow-a-gpx-track)

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
<span id="post-56215-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56215-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-56215-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've been taking photos with a sports camera (a Replay XD1080, like a GoPro) on my bike and recording a GPX track with my phone. This is a great set up, because the camera is designed to be mounted on a bicycle's handlebars, is waterproof, and has a mode where it takes one photo every 3 seconds.</p>
<p>I can correlate the pictures with the gpx track in JOSM using the Photo_geotagging (and photoadjust, if needed) plugins, but it does not set the compass angle in the image's exif tag, and mapillary goes ahead and assumes all images w/o a compass angle specified are facing north....</p>
<p>I thought I had seen an option somewhere to set the compass angle to follow the travel of the gpx track, which is a sensible feature, but can not find it anywhere now. I may have seen it somewhere other than JOSM, but if not JOSM it would have been in gottengeography or on the mappillary website itself, and have checked there too.</p>
<p>How do I set the compass angle to follow the gpx track?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-photos" rel="tag" title="see questions tagged &#39;photos&#39;">photos</span> <span class="post-tag tag-link-photomapping" rel="tag" title="see questions tagged &#39;photomapping&#39;">photomapping</span> <span class="post-tag tag-link-mapillary" rel="tag" title="see questions tagged &#39;mapillary&#39;">mapillary</span> <span class="post-tag tag-link-exif" rel="tag" title="see questions tagged &#39;exif&#39;">exif</span> <span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 May '17, 19:32</strong></p>
<img src="https://secure.gravatar.com/avatar/f88a467aa884aeb760041004f62448ee?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="keithonearth&#39;s gravatar image" />
<p><span>keithonearth</span><br />
<span class="score" title="2939 reputation points"><span>2.9k</span></span><span title="56 badges"><span class="badge1">●</span><span class="badgecount">56</span></span><span title="76 badges"><span class="silver">●</span><span class="badgecount">76</span></span><span title="108 badges"><span class="bronze">●</span><span class="badgecount">108</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="keithonearth has 3 accepted answers">13%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 May '17, 18:16</strong> </span></p>
</div>
</div>
<div id="comments-container-56215" class="comments-container">
&#10;</div>
<div id="comment-tools-56215" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56215-form-container" class="comment-form-container">
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

<span id="56216"></span>

<div id="answer-container-56216" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56216-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56216-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-56216-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I use a similar setup with the <a href="https://github.com/mapillary/mapillary_tools">mapillary_tools</a> scripts.</p>
<p>For setting the compass angle only, specify <code>--overwrite_EXIF_direction_tag</code> in the image processing step below but don't specify <code>--overwrite_EXIF_gps_tag</code>.</p>
<p>My work flow for geo-tagging photos and uploading them to mapillary is processing and uploading is usually the following (on Linux):</p>
<h1 id="current-version-of-mapillary_tools">Current version of mapillary_tools</h1>
<h2 id="installation">Installation</h2>
<p>Run the following commands for installing mapillary_tools:</p>
<ul>
<li><code>sudo apt install python-pip</code></li>
<li><code>pip install git+</code><a href="https://github.com/mapillary/Piexif"><code>https://github.com/mapillary/Piexif</code></a></li>
<li><code>pip install --upgrade git+</code><a href="https://github.com/mapillary/mapillary_tools"><code>https://github.com/mapillary/mapillary_tools</code></a></li>
</ul>
<h2 id="image-processing">Image Processing</h2>
<p>Run the following command for adding GPS information to your photo's EXIF tags:</p>
<p><code>~/.local/bin/mapillary_tools process --verbose --advanced --rerun --user_name mapillary_user --interpolate_directions --overwrite_EXIF_gps_tag --overwrite_EXIF_direction_tag --duplicate_angle 360 --offset_time 1 --import_path "~/media/cam/" --geotag_source "gpx" --geotag_source_path "~/gpx/today.gpx"</code></p>
<p>Some explanations:</p>
<ul>
<li>Replace <code>mapillary_user</code> with your mapillary user name</li>
<li>Replace <code>~/media/cam/</code> and <code>~/gpx/today.gpx</code> with your photo and GPX path</li>
<li><code>--interpolate_directions</code> tells it to interpolate the photo direction based on the GPX track</li>
<li><code>--duplicate_angle 360</code> tells it to ignore the angle when searching for duplicates, usefule since without GPS support your camera won't set a meaningful angle</li>
<li><code>--offset_time 1</code> specifies the offset to add to your GPX time stamps to synchronize with the photo timestamp from your camera clock</li>
</ul>
<p>You can run <code>mapillary_tools process --advanced -h</code> to see all options and their description.</p>
<h2 id="upload">Upload</h2>
<p>Run the following command to upload your photos:</p>
<p>~/.local/bin/mapillary_tools upload --verbose --advanced --skip_subfolders --number_threads 10 --max_attempts 10 --import_path "~/media/cam/"</p>
<h1 id="old-answer-for-old-version-of-mapillary_tools-before-release-v0.0.0">Old answer for old version of mapillary_tools (before release v0.0.0)</h1>
<pre><code>export MAPILLARY_USERNAME=myname
export MAPILLARY_EMAIL=myaddress@domain.com
export MAPILLARY_PASSWORD=asdf1234
&#10;python geotag_from_gpx.py --time-offset 0 /path/to/images/ /path/to/track.gpx
python add_mapillary_tag_from_exif.py /path/to/images/
python remove_duplicates.py -p 360 /path/to/images/
python upload.py /path/to/images/</code></pre>
<ul>
<li><code>geotag_from_gpx.py</code> adds the coordinates for each photo and also the heading based on the next photo. This is the most interesting script. You can use the <code>--time-offset</code> parameter if your camera's clock is out of sync with your GPS logger's clock. Ideally use JOSM afterwards to open a few photos and validate the geotagging.</li>
<li><code>add_mapillary_tag_from_exif.py</code> adds a special tag to identify the photo sequence.</li>
<li><code>remove_duplicates.py</code> removes duplicated photos taken at the same location. (Parameter <code>-p 360</code> is important for <em>ignoring</em> the heading when searching for duplicates. This is because the script tries to keep photos at the same location if the heading changes significantly. But due to the previously executed <code>geotag_from_gpx.py</code> the heading for photos taken at the <em>same</em> location is almost random, leading to large heading variations and thus many duplicates being erroneously kept).</li>
<li><code>upload.py</code> will simply upload the result to mapillary.</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 May '17, 21:07</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Jul '19, 12:48</strong> </span></p>
</div>
</div>
<div id="comments-container-56216" class="comments-container">
<span id="56219"></span>
<div id="comment-56219" class="comment">
<div id="post-56219-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This looks like just what I was after! The only issue I can see is that the clock on the camera and the clock on the GPS may differ by as much as a couple of minuets. This places the images in the wrong place if I do not adjust the time on the photos. The JOSM plugins make this easy enough, and I get good geolocation tags in the image's exif tags. I think that a fully automated process would not allow me to adjust the time on the images.</p>
</div>
<div id="comment-56219-info" class="comment-info">
<span class="comment-age">(17 May '17, 22:30)</span> <span class="comment-user userinfo">keithonearth</span>
</div>
</div>
<span id="56220"></span>
<div id="comment-56220" class="comment">
<div id="post-56220-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/9027/keithonearth">@keithonearth</a>: The difference in clock can be corrected with the time-offset parameter of the first script. You can determine the difference by making a picture of the clock of your GPS (if that includes seconds), otherwise, make a waypoint at the same time you make a picture. I explain this in more detail in <a href="http://www.osm.be/2017/04/21/en-post-survey.html">http://www.osm.be/2017/04/21/en-post-survey.html</a></p>
</div>
<div id="comment-56220-info" class="comment-info">
<span class="comment-age">(18 May '17, 04:19)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="56223"></span>
<div id="comment-56223" class="comment">
<div id="post-56223-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It also helps to start the time lapse and the GPS recording at the same time. I also use JOSM to validate the geotagging of the photos after running <code>geotag_from_gpx.py</code>.</p>
</div>
<div id="comment-56223-info" class="comment-info">
<span class="comment-age">(18 May '17, 07:38)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-56216" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56216-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="56217"></span>

<div id="answer-container-56217" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56217-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56217-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-56217-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I set it with the python script <a href="https://github.com/mapillary/mapillary_tools/blob/master/python/interpolate_direction.py">interpolate_direction.py</a> from Mapillary. You can also use Javawa's <a href="http://www.javawa.nl/fotogeotag_en.html">fotogeotag</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 May '17, 21:40</strong></p>
<img src="https://secure.gravatar.com/avatar/0f5ffc3756c4662b9dfad80b7665ac6c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ligfietser&#39;s gravatar image" />
<p><span>ligfietser</span><br />
<span class="score" title="2894 reputation points"><span>2.9k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="27 badges"><span class="silver">●</span><span class="badgecount">27</span></span><span title="57 badges"><span class="bronze">●</span><span class="badgecount">57</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ligfietser has 8 accepted answers">11%</span></p>
</div>
</div>
<div id="comments-container-56217" class="comments-container">
<span id="56232"></span>
<div id="comment-56232" class="comment">
<div id="post-56232-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks! I found this script <em>very</em> helpful. especially as it works well with JOSM, which allows me to correlate with the gpx and tweak the locations in a program I'm familiar with.</p>
</div>
<div id="comment-56232-info" class="comment-info">
<span class="comment-age">(19 May '17, 07:24)</span> <span class="comment-user userinfo">keithonearth</span>
</div>
</div>
</div>
<div id="comment-tools-56217" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56217-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="56239"></span>

<div id="answer-container-56239" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56239-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56239-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-56239-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>After uploading your sequence, once you get the notification it's available on Mapillary, edit sequence and click on NORMALIZE (it will adjust the bearing of the photo in relation to the next one). No script needed.</p>
<p>Also for geotag I recommend GeoSetter, you can adjust timestamp with positive and negative values (which is extremely useful as you cannot sync HH:MM:SS between yours GPS/smartphone and the action camera (unless it's adjustable by the action cam app, as in GoPro Hero 5 or GoPro Session 5).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 May '17, 11:46</strong></p>
<img src="https://secure.gravatar.com/avatar/fca0301c1cc27de002f7fd6bdaceaecb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lfttp&#39;s gravatar image" />
<p><span>lfttp</span><br />
<span class="score" title="56 reputation points">56</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lfttp has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-56239" class="comments-container">
&#10;</div>
<div id="comment-tools-56239" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56239-form-container" class="comment-form-container">
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

