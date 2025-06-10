+++
type = "question"
title = "Osm2pgsql  very slow way processing"
description = '''When I do pbf dile import with Osm2pgsql it always gets stuck at ways processing. Id populates database with nodes rather quickly (the speed increaded when used &quot;--drop&quot; and &quot;--disable-parallel-indexing&quot; options, but ways are still processed at 0.16 kb/s. Now the server runs on a virtual machine wit...'''
date = "2020-03-02T09:11:00Z"
lastmod = "2020-03-02T09:11:00Z"
weight = 73305
keywords = [ "ways", "slow", "osm2pgsql" ]
aliases = [ "/questions/73305" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Osm2pgsql very slow way processing](/questions/73305/osm2pgsql-very-slow-way-processing)

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
<span id="post-73305-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73305-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-73305-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>When I do pbf dile import with Osm2pgsql it always gets stuck at ways processing. Id populates database with nodes rather quickly (the speed increaded when used "--drop" and "--disable-parallel-indexing" options, but ways are still processed at 0.16 kb/s. Now the server runs on a virtual machine with a fixed sized disk space. And the host system (windows 10) shows that there is a 50% disk usage while the ways are processed. What exactly is happening when ways are processed? Can using a normal mode (instead of slim) fix the issue? Would a normal mode map export be enough if I am not planning to frequently update database using --append (not gonna use it anyway, since it's slow to the point of being useless). Thank you.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ways" rel="tag" title="see questions tagged &#39;ways&#39;">ways</span> <span class="post-tag tag-link-slow" rel="tag" title="see questions tagged &#39;slow&#39;">slow</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Mar '20, 09:11</strong></p>
<img src="https://secure.gravatar.com/avatar/7d9dea8db6c9981b45d28f28bb29f49d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kartman1&#39;s gravatar image" />
<p><span>kartman1</span><br />
<span class="score" title="38 reputation points">38</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kartman1 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Mar '20, 09:22</strong> </span></p>
</div>
</div>
<div id="comments-container-73305" class="comments-container">
&#10;</div>
<div id="comment-tools-73305" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73305-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

