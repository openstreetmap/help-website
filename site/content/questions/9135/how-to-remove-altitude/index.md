+++
type = "question"
title = "How to remove altitude"
description = '''I used symbian and sports tracker to trace the jogging path. Then export to kml and used free kml2svg.fr tool to convert it to svg. How ever, when I check this trace each time there is a elevation difference, the trace gets longer than real path on a map should be. Is there any tools to remove or cl...'''
date = "2011-11-20T13:02:00Z"
lastmod = "2011-11-23T11:05:00Z"
weight = 9135
keywords = [ "data", "kml", "elevation" ]
aliases = [ "/questions/9135" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to remove altitude](/questions/9135/how-to-remove-altitude)

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
<span id="post-9135-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9135-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-9135-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I used symbian and sports tracker to trace the jogging path. Then export to kml and used free <a href="http://kml2svg.fr">kml2svg.fr</a> tool to convert it to svg.</p>
<p>How ever, when I check this trace each time there is a elevation difference, the trace gets longer than real path on a map should be.</p>
<p>Is there any tools to remove or clamp the data to starting altitude or 0m meters ? Tried the sports tracker "clamp to ground" / "relative to ground" / "Absolute" but all of them gave exactly the same trace which was wrong.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span> <span class="post-tag tag-link-kml" rel="tag" title="see questions tagged &#39;kml&#39;">kml</span> <span class="post-tag tag-link-elevation" rel="tag" title="see questions tagged &#39;elevation&#39;">elevation</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Nov '11, 13:02</strong></p>
<img src="https://secure.gravatar.com/avatar/88017063eed6267bdabd96d2c4c06bfb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="testrai&#39;s gravatar image" />
<p><span>testrai</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="testrai has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-9135" class="comments-container">
<span id="9156"></span>
<div id="comment-9156" class="comment">
<div id="post-9156-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Perhaps you could upload an example KML somewhere and then someone could suggest how to remove the altitude from it (if that's what you need; I'm not convinced I understand your problem though).</p>
<p>A random KML file on my PC has something like:</p>
<p>&lt;coordinates&gt;-1.1665988,54.1558052,0&lt;/coordinates&gt;</p>
<p>in it, of which the ",0" at the end is the altitude. I'd have thought that it might be possible to change the altitude to 0 using a half-decent text editor?</p>
</div>
<div id="comment-9156-info" class="comment-info">
<span class="comment-age">(21 Nov '11, 14:39)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="9165"></span>
<div id="comment-9165" class="comment">
<div id="post-9165-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Your question is about "altitude", but from the context it is apparent that you mean "elevation". The word "altitude" means height above ground. "Elevation" means height above mean sea level.</p>
</div>
<div id="comment-9165-info" class="comment-info">
<span class="comment-age">(21 Nov '11, 19:30)</span> <span class="comment-user userinfo">user8192</span>
</div>
</div>
<span id="9190"></span>
<div id="comment-9190" class="comment">
<div id="post-9190-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You all have right topics - thank you</p>
<p>This hasn't yet got nothing to do with osm, because the trace gathered with sportstr seems to be wrong. Of course if you are jogging uphill and downhill, want the real run length, and not the flattened(altitude removed)+not so long trace.</p>
<p>Or am i stupid here - are maps drawn like that or on a flattened surface ?</p>
<p>I'm happy if i can flatten the file either kml or in gpx format. But how ?</p>
</div>
<div id="comment-9190-info" class="comment-info">
<span class="comment-age">(22 Nov '11, 20:20)</span> <span class="comment-user userinfo">testrai</span>
</div>
</div>
<span id="9191"></span>
<div id="comment-9191" class="comment">
<div id="post-9191-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>ok, i made a picture to be more clear. is there a way to make the bottom result? (with nokia+sports tracker, or do i have to buy android)</p>
<p><a href="http://bayimg.com/pAlihaaDA">http://bayimg.com/pAlihaaDA</a></p>
</div>
<div id="comment-9191-info" class="comment-info">
<span class="comment-age">(22 Nov '11, 20:40)</span> <span class="comment-user userinfo">testrai</span>
</div>
</div>
</div>
<div id="comment-tools-9135" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9135-form-container" class="comment-form-container">
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

<span id="9138"></span>

<div id="answer-container-9138" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-9138-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9138-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-9138-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Sports Tracker only uses OpenStreetMap map images as a backdrop to your trace. The altitude data you're seeing has been gathered from your GPS receiver, and has nothing to do with OpenStreetMap, which doesn't actually store any altitude data for any features.</p>
<p>There are some <a href="http://wiki.openstreetmap.org/wiki/Recording_GPS_tracks">tips for improving GPS accuracy</a> on our wiki, but other than that you should contact either the manufacturer of your GPS receiver (or phone if you're using its built-in GPS), or Sports Tracking Technologies, the publishers of your App.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Nov '11, 17:16</strong></p>
<img src="https://secure.gravatar.com/avatar/9fe361843971cf8b23dc93517f00b996?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jonathan%20Bennett&#39;s gravatar image" />
<p><span>Jonathan Ben...</span><br />
<span class="score" title="8261 reputation points"><span>8.3k</span></span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="85 badges"><span class="silver">●</span><span class="badgecount">85</span></span><span title="108 badges"><span class="bronze">●</span><span class="badgecount">108</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jonathan Bennett has 21 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Nov '11, 17:17</strong> </span></p>
</div>
</div>
<div id="comments-container-9138" class="comments-container">
<span id="9150"></span>
<div id="comment-9150" class="comment">
<div id="post-9150-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I don't think you'll find a solution with the device itself. But there definitely are tools to modify a trace file after the fact, and zero-ing the altitude should be a easy and common operation.</p>
<p>I don't know which tools those would be though. gdal is one, but that may be too programing-oriented for the OP. Some programs, like googleearth, have a "ignore altitude" option, but I think they only do the modification in memory, and do not update the trace file.</p>
</div>
<div id="comment-9150-info" class="comment-info">
<span class="comment-age">(21 Nov '11, 09:27)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
</div>
<div id="comment-tools-9138" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9138-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="9192"></span>

<div id="answer-container-9192" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-9192-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9192-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-9192-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As SomeoneElse hinted, both KML and GPX files are just XML files. That means that you can open them with a simple text editor, see how they are structured, and make some edits. Check wikipedia for an xml primer if you need it.</p>
<p>Opening one of my gpx file, and the same one converted to kml (using ogr2ogr), you quickly spot the &lt;ele&gt; tag (for gpx) and the &lt;SimpleData name="ele"&gt; tag (for kml). Check your own files in case they are structured differently. Deleting those should achieve what you want.</p>
<p>There are many ways to delete those, it depends on what you're comfortable with. You can use your text editor to search+replace, if the search field accepts regexps. You can use 'sed' if you are using a unix-derived OS (including Linux or MacOSX) : "sed 's@&lt;ele&gt;[0-9.-]*&lt;/ele&gt;@<span>@g</span>' myfile.gpx &gt; newfile.gpx". There are some xml-specific editors out there too if they feel better for you.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Nov '11, 22:28</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-9192" class="comments-container">
<span id="9202"></span>
<div id="comment-9202" class="comment">
<div id="post-9202-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you</p>
<p>This must be that i'm stupid. Because i removed the last col from coords in the klm file - the altitude</p>
<p>and after that using the <a href="http://kml2svg.fr">kml2svg.fr</a> tool and still got the same trace widht what was too long.</p>
<p>So perhaps the sports tracker already makes some calculations into those coordinates and that's why they are wrong.</p>
</div>
<div id="comment-9202-info" class="comment-info">
<span class="comment-age">(23 Nov '11, 11:05)</span> <span class="comment-user userinfo">testrai</span>
</div>
</div>
</div>
<div id="comment-tools-9192" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9192-form-container" class="comment-form-container">
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

