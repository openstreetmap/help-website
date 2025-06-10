+++
type = "question"
title = "OpenStreetCam images in JOSM without upload"
description = '''I have some OpenStreetCam mp4 sequences that I would like to use for some local editing without first unloading them to OpenStreetCam.  Is there a way to get these into JOSM without sending them all the way up to a remote server and bringing them back down again? Ripping the images from the mp4s sho...'''
date = "2019-12-11T19:20:00Z"
lastmod = "2019-12-12T18:33:00Z"
weight = 72072
keywords = [ "josm", "osc", "openstreetcam" ]
aliases = [ "/questions/72072" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [OpenStreetCam images in JOSM without upload](/questions/72072/openstreetcam-images-in-josm-without-upload)

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
<span id="post-72072-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72072-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-72072-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have some OpenStreetCam mp4 sequences that I would like to use for some local editing without first unloading them to OpenStreetCam.</p>
<p>Is there a way to get these into JOSM <em>without</em> sending them all the way up to a remote server and bringing them back down again?</p>
<p>Ripping the images from the mp4s shouldn't be too difficult, but while NMEA-like, JOSM thinks the metadata files aren't valid NMEA files. There seem to be some scripts <a href="https://github.com/openstreetcam/upload-scripts">here</a> but they're a little light on documentation for someone who lives in GUI land and while they'll generate exif, it's not clear if they will extract images first.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-osc" rel="tag" title="see questions tagged &#39;osc&#39;">osc</span> <span class="post-tag tag-link-openstreetcam" rel="tag" title="see questions tagged &#39;openstreetcam&#39;">openstreetcam</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Dec '19, 19:20</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-72072" class="comments-container">
<span id="72078"></span>
<div id="comment-72078" class="comment">
<div id="post-72078-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I'm not clear what you are trying to achieve and what issue you have. Do you want to show the images with the street cam plugin? Do you want to show the locations where the images have been taken? Did you try to open an image file with the standard open command and failed?</p>
</div>
<div id="comment-72078-info" class="comment-info">
<span class="comment-age">(12 Dec '19, 08:09)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
<span id="72082"></span>
<div id="comment-72082" class="comment">
<div id="post-72082-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'm after any method of getting them into JOSM without upload.</p>
<p>I don't really mind whether that is:</p>
<ul>
<li>a hidden setting in the OSC plugin that lets you use local files or</li>
<li>a way of ripping images from the videos and a track from the metadata file to manually synchronize them in JOSM, or</li>
<li>some way of extracting images and writing coordinates to the exif data (thought osc_tools.py might do this, but it just seems to say it's "finished" without changing any files).</li>
</ul>
<p>I realize that uploading would be easier, but with no apparent way to trim sequences I'm not really comfortable uploading this set of images.</p>
</div>
<div id="comment-72082-info" class="comment-info">
<span class="comment-age">(12 Dec '19, 14:58)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
</div>
<div id="comment-tools-72072" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72072-form-container" class="comment-form-container">
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

<span id="72085"></span>

<div id="answer-container-72085" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72085-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72085-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-72085-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I am not aware of a plug-in for JOSM that can deal with mp4 files. You can extract the images from a "normal" MP4 file using ffmpeg but those images will not be geo-referenced. There are some tools that allow you to add gps exif data to photos but you'll need to get that somehow from the MP4 file. But, again, I don't think there is a standard for how GPX data can be encoded in a MP4 file. And it is not clear to me that OpenStreetCam's MP4 file adheres to standards.</p>
<p>For what its worth, I was dealing with a similar issue when setting up my "dash cam mapping" methodology. Fortunately for me I found some code on the Internet that was able to extract the proprietary format GPX information from my dash cam's video. I used that along with ffmpeg and exiftool to create my dashcam2josm script.</p>
<p>In my case, I happen to use the scripts your link points to up upload the still georeferenced images from my dashcam2josm script to OpenStreetCam. I do that because I figure there are things that I am not worried about mapping (fire hydrants, bus stops, etc.) that others might want to have imagery for.</p>
<p>Getting back to your issue, it looks like the generate_exif script in the <a href="https://github.com/openstreetcam/upload-scripts">https://github.com/openstreetcam/upload-scripts</a> repository may be what you need. But it has been so long since I gave up trying to use the OpenStreetCam app that I am not sure what files it generates and don't really know what the script help message means about "Folder PATH with OSC metadata file and images". Can you extract the images from the file using ffmpeg? If so then maybe the generate_exif script would then add the GPS data to them. . . Just a guess though.</p>
<pre><code>upload-scripts$ python osc_tools.py generate_exif -h
usage: python osc_tools.py generate_exif [-h] -p PATH [-l {d,i,w}]
&#10;optional arguments:
  -h, --help            show this help message and exit
  -p PATH, --path PATH  Folder PATH with OSC metadata file and images
  -l {d,i,w}, --log_level {d,i,w}
                        Level of logging to console:
                          d level (debug) will log every event to the console
                          i level (info) will log every event more severe than debug level to the console
                          w level (warning) will log every event more severe than info level to the console</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Dec '19, 16:17</strong></p>
<img src="https://secure.gravatar.com/avatar/f60af53a4eba0c21f25c22674fb4a8cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="n76&#39;s gravatar image" />
<p><span>n76</span><br />
<span class="score" title="10839 reputation points"><span>10.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="82 badges"><span class="silver">●</span><span class="badgecount">82</span></span><span title="172 badges"><span class="bronze">●</span><span class="badgecount">172</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="n76 has 48 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-72085" class="comments-container">
<span id="72087"></span>
<div id="comment-72087" class="comment">
<div id="post-72087-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I think the PATH is just the folder location. The script seems to do nothing except claim to be 'finished'.</p>
<p>From the app I get a '<code>track.txt.gz</code>' file and several videos '<code>0.mp4</code>', '<code>1.mp4</code>' etc. I assume the compressed text file is what is called the 'metadata file' in the documentation. It seems to be a semicolon delimited file with each line starting with a unix time stamp and one or more columns that contain what appear to be coordinates and other data. Column 15 and 16 look like video file and (overall) picture number?</p>
<p>Oddly, the script fails to recognize the metadata unless I manually uncompressed it first. I think the script is silently failing to run gzip when run from powershell. (WSL-bash has it but I'm having trouble with other dependancies.) I wonder if there are other things failing that aren't making it to the console.</p>
</div>
<div id="comment-72087-info" class="comment-info">
<span class="comment-age">(12 Dec '19, 18:33)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
</div>
<div id="comment-tools-72085" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72085-form-container" class="comment-form-container">
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

