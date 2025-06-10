+++
type = "question"
title = "Shell tools or scripts to split GPX files based on time"
description = '''I am using my GPX files in photo and video processing, and at times need to back track to older archives. I have currently blended all my GPX files into a combined archive, but this is now too big, so that many of the tools I am using are unable to find the data. I am therefor looking for a tool or ...'''
date = "2016-01-09T22:10:00Z"
lastmod = "2016-01-10T23:33:00Z"
weight = 47433
keywords = [ "date", "gpx", "post_process_gpx" ]
aliases = [ "/questions/47433" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Shell tools or scripts to split GPX files based on time](/questions/47433/shell-tools-or-scripts-to-split-gpx-files-based-on-time)

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
<span id="post-47433-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47433-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-47433-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am using my GPX files in photo and video processing, and at times need to back track to older archives. I have currently blended all my GPX files into a combined archive, but this is now too big, so that many of the tools I am using are unable to find the data.</p>
<p>I am therefor looking for a tool or shell commands I can use to split the combined archive into monthly files (or if that is still too big, daily files) That way I don't have to look through my entire database in order to find the correct traces.</p>
<p>gpsbabel might be possible, but filtering is still confusing for me.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-date" rel="tag" title="see questions tagged &#39;date&#39;">date</span> <span class="post-tag tag-link-gpx" rel="tag" title="see questions tagged &#39;gpx&#39;">gpx</span> <span class="post-tag tag-link-post_process_gpx" rel="tag" title="see questions tagged &#39;post_process_gpx&#39;">post_process_gpx</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Jan '16, 22:10</strong></p>
<img src="https://secure.gravatar.com/avatar/9e78e86dbaee163b57f19b777d194a12?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Skippern&#39;s gravatar image" />
<p><span>Skippern</span><br />
<span class="score" title="166 reputation points">166</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Skippern has one accepted answer">33%</span></p>
</div>
</div>
<div id="comments-container-47433" class="comments-container">
&#10;</div>
<div id="comment-tools-47433" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47433-form-container" class="comment-form-container">
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

<span id="47440"></span>

<div id="answer-container-47440" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-47440-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47440-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-47440-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Skippern has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>gpsbabel can do the low-level filtering for you, but it is a bit awkward, especially if your GPX file has more than one data type (route, track, or waypoint). You would then have to wrap this in a script to process by month or day or whatever.</p>
<p>Here are some examples.</p>
<p>If you have a GPX file of only tracks, and you want only tracks from the year 2014 (2014-01-01 to 2015-01-01), you could use something like this:</p>
<pre><code>gpsbabel -i gpx -f in.gpx \
   -x track,start=20140101,stop=20150101 \
   -o gpx -F out.gpx</code></pre>
<p>Make sure none of your tracks crosses the start or stop date/times, because gpsbabel filters the trackpoints (not the tracks) by trackpoint date/time, and you will end up with partial tracks.</p>
<p>If your GPX file has only waypoints, you have to transform them to use the filter:</p>
<pre><code>gpsbabel -i gpx -f in.gpx \
    -x transform,trk=wpt,del \
    -x track,start=20140101,stop=20150101 \
    -x transform,wpt=trk,del \
    -o gpx -F out.gpx</code></pre>
<p>If your GPX file has both waypoints and tracks, you have to run 2 passes, once per type. Then merge the results (if desired).</p>
<pre><code>gpsbabel -i gpx -f in.gpx \
    -x nuketypes,tracks,routes \
    -x transform,trk=wpt,del \
    -x track,start=20140101,stop=20150101 \
    -x transform,wpt=trk,del \
    -o gpx -F out_w.gpx
gpsbabel -i gpx -f in.gpx \
    -x nuketypes,waypoints,routes \
    -x track,start=20140101,stop=20150101 \
    -o gpx -F out_t.gpx
gpsbabel -i gpx -f out_w.gpx -f out_t.gpx -o gpx -F out.gpx</code></pre>
<p>Doing this for routes 'is left as an exercise for the reader'.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Jan '16, 23:33</strong></p>
<img src="https://secure.gravatar.com/avatar/c1e98ded2982cd352d4c77075aa0cd74?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ljb_nj&#39;s gravatar image" />
<p><span>ljb_nj</span><br />
<span class="score" title="659 reputation points">659</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ljb_nj has one accepted answer">12%</span></p>
</div>
</div>
<div id="comments-container-47440" class="comments-container">
&#10;</div>
<div id="comment-tools-47440" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47440-form-container" class="comment-form-container">
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

