+++
type = "question"
title = "Osmosis - No Output File"
description = '''Hi all - Mis-posted this last time, so trying again. Brand new to OSM and Osmosis. I&#x27;m running Windows 10 in Bootcamp on a MacBook Pro (if that matters).  I ran through the instructions here, and everything worked as it should. https://wiki.openstreetmap.org/wiki/Osmosis/Quick_Install_(Windows) When...'''
date = "2018-03-21T13:19:00Z"
lastmod = "2018-03-21T13:39:00Z"
weight = 62761
keywords = [ "osmosis" ]
aliases = [ "/questions/62761" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Osmosis - No Output File](/questions/62761/osmosis-no-output-file)

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
<span id="post-62761-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62761-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-62761-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all -</p>
<p>Mis-posted this last time, so trying again. Brand new to OSM and Osmosis. I'm running Windows 10 in Bootcamp on a MacBook Pro (if that matters).</p>
<p>I ran through the instructions here, and everything worked as it should.</p>
<p><a href="https://wiki.openstreetmap.org/wiki/Osmosis/Quick_Install_(Windows)">https://wiki.openstreetmap.org/wiki/Osmosis/Quick_Install_(Windows)</a></p>
<p>When I try to run a test from the command line however, I'm not seeing any output file. I've tried using a map of Chicago I saved as well as some sample data I found on an Osmium walkthrough, and have tried extracting a list of schools and speed cameras. I've triple-checked for typos in the command, but no matter what I try, there's no output file.</p>
<p>Any insight or feedback on what I might be doing wrong would be greatly appreciated.</p>
<p>Cheers!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Mar '18, 13:19</strong></p>
<img src="https://secure.gravatar.com/avatar/10edbcbc6198c726545ec674d240efc6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yatta3&#39;s gravatar image" />
<p><span>yatta3</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yatta3 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-62761" class="comments-container">
<span id="62762"></span>
<div id="comment-62762" class="comment">
<div id="post-62762-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Please tell use the command(s) you have tried.</p>
</div>
<div id="comment-62762-info" class="comment-info">
<span class="comment-age">(21 Mar '18, 13:36)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="62764"></span>
<div id="comment-62764" class="comment">
<div id="post-62764-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>osmosis --read-pbf chicago_test.osm.pbf --node-key-value keyValueList="highway.speed_camera" --write-xml radar.osm</p>
<p>osmosis --rbf chicago_test.osm.pbf --nkv keyValueList="amenity.school" --wx schools.osm</p>
<p>osmosis --rbf sample_osmosis.osm.pbf --nkv keyValueList="amenity.school" --wx schools.osm</p>
</div>
<div id="comment-62764-info" class="comment-info">
<span class="comment-age">(21 Mar '18, 13:39)</span> <span class="comment-user userinfo">yatta3</span>
</div>
</div>
</div>
<div id="comment-tools-62761" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62761-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

