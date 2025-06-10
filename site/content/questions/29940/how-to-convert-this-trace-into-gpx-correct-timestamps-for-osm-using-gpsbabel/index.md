+++
type = "question"
title = "How to convert this trace into GPX (correct timestamps) for OSM using gpsbabel?"
description = '''Hi there. What is this format? pastebin.com link  What input and output file format should I use in gpsbabel so I can convert and upload this GPS trace in OpenStreetMap?  Thanks. '''
date = "2014-01-18T16:02:00Z"
lastmod = "2014-01-18T18:42:00Z"
weight = 29940
keywords = [ "gpslogmee", "gpsbabel", "convert", "gpx", "timestamps" ]
aliases = [ "/questions/29940" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to convert this trace into GPX (correct timestamps) for OSM using gpsbabel?](/questions/29940/how-to-convert-this-trace-into-gpx-correct-timestamps-for-osm-using-gpsbabel)

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
<span id="post-29940-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29940-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-29940-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi there.</p>
<p>What is this format? <a href="http://pastebin.com/HhpEfV6L">pastebin.com link</a><br />
</p>
<p>What input and output file format should I use in <a href="http://www.gpsbabel.org/">gpsbabel</a> so I can convert and upload this GPS trace in OpenStreetMap?<br />
</p>
<p>Thanks.<br />
</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-gpslogmee" rel="tag" title="see questions tagged &#39;gpslogmee&#39;">gpslogmee</span> <span class="post-tag tag-link-gpsbabel" rel="tag" title="see questions tagged &#39;gpsbabel&#39;">gpsbabel</span> <span class="post-tag tag-link-convert" rel="tag" title="see questions tagged &#39;convert&#39;">convert</span> <span class="post-tag tag-link-gpx" rel="tag" title="see questions tagged &#39;gpx&#39;">gpx</span> <span class="post-tag tag-link-timestamps" rel="tag" title="see questions tagged &#39;timestamps&#39;">timestamps</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Jan '14, 16:02</strong></p>
<img src="https://secure.gravatar.com/avatar/3b09c80bc2f346ff49cf0d8eb22260b5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dobri_z&#39;s gravatar image" />
<p><span>dobri_z</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dobri_z has no accepted answers">0%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Jan '14, 19:07</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></br></p>
</div>
</div>
<div id="comments-container-29940" class="comments-container">
&#10;</div>
<div id="comment-tools-29940" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29940-form-container" class="comment-form-container">
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

<span id="29942"></span>

<div id="answer-container-29942" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-29942-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29942-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-29942-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This seems to be already in <span>GPX format</span>, in principle. Does the upload to OSM not work? I guess it may be due to the timestamps not being in ISO 8601 date-time format (they are e.g. "Sat Jan 18 2014 14:01:32 GMT+0200 (EET)"). If possible you should configure your app to record the time stamps in the correct format, tell the app author or use another one.<br />
</p>
<p>I <em>do not know how to use gpsbabel</em> to convert the time stamps. However, I see two alternative options:</p>
<ol>
<li>As an ugly workaround you could replace the timestamps in wrong format by new ones in the correct format. On upload please select the "private" privacy option which hides the time/speed info to other users as it is faked.
<ol>
<li>You can use gbsbabel to add fake timestamps (see also <a href="/questions/1260/how-to-create-fake-timestamps-with-gpsbabel">1</a> and <a href="http://www.gpsbabel.org/htmldoc-1.4.4/filter_track.html">2</a>):<br />
<code>gpsbabel -i gpx -f gps_logmee.gpx -x track,faketime=f19700101000000+1 -o gpx -F outputfilename.gpx</code></li>
<li>You could use a <span>regexp</span>-capable text editor and search<br />
<code>&lt;time&gt;[^&lt;]*&lt;/time&gt;</code><br />
and replace all by<br />
<code>&lt;time&gt;1970-01-01T00:00:00Z&lt;/time&gt;</code></li>
</ol></li>
<li>Alternatively you could use the gpx file directly (without uploading) in most editors (iD, JOSM, Potlatch2). That works even without correct time stamps. Of course that "no upload method" looses the benefit to other mappers.</li>
</ol>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Jan '14, 16:46</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Jan '14, 18:06</strong> </span></p>
</div>
</div>
<div id="comments-container-29942" class="comments-container">
<span id="29945"></span>
<div id="comment-29945" class="comment">
<div id="post-29945-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Thank you for your quick response.<br />
Problem solved.<br />
All three methods work fine.<br />
Have a nice day.</p>
</div>
<div id="comment-29945-info" class="comment-info">
<span class="comment-age">(18 Jan '14, 18:42)</span> <span class="comment-user userinfo">dobri_z</span>
</div>
</div>
</div>
<div id="comment-tools-29942" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29942-form-container" class="comment-form-container">
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

