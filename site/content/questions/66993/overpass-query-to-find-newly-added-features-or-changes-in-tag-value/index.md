+++
type = "question"
title = "Overpass query to find newly added features or changes in tag value"
description = '''Hi Everyone,  I am curious if Overpass is able to query features that were added or have changes in tag value.  For example, I wanna see how many oneway tags were added for a given month. Likewise seeing also if there are any changes in the tag value.  This is the current code i am using. [diff: &quot;20...'''
date = "2018-11-30T01:02:00Z"
lastmod = "2018-12-02T13:41:00Z"
weight = 66993
keywords = [ "overpass", "overpass-turbo" ]
aliases = [ "/questions/66993" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Overpass query to find newly added features or changes in tag value](/questions/66993/overpass-query-to-find-newly-added-features-or-changes-in-tag-value)

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
<span id="post-66993-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66993-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-66993-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi Everyone,</p>
<p>I am curious if Overpass is able to query features that were added or have changes in tag value.</p>
<p>For example, I wanna see how many oneway tags were added for a given month. Likewise seeing also if there are any changes in the tag value.</p>
<p>This is the current code i am using. [diff: "2018-05-30T15:00:00Z","2018-06-30T15:00:00Z"][out:xml][timeout:25];(way<a href="%7B%7Bbbox%7D%7D">"oneway"</a>;);out body;&gt;;out skel qt;</p>
<p>This query gives anything that is touched but does not always pertain to added oneway tag. it can be any change to the segment tagged oneway.</p>
<p>Any thoughts about this?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Nov '18, 01:02</strong></p>
<img src="https://secure.gravatar.com/avatar/3aff6e35f2fe591cfa7e3f779064d363?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mapsbyjujubee&#39;s gravatar image" />
<p><span>mapsbyjujubee</span><br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mapsbyjujubee has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-66993" class="comments-container">
&#10;</div>
<div id="comment-tools-66993" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66993-form-container" class="comment-form-container">
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

<span id="67014"></span>

<div id="answer-container-67014" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-67014-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67014-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-67014-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can further filter the results of your query to only those with actual changes of the "oneway" tag with the <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#The_block_statement_compare">compare</a> statement, see also blog post section <a href="https://dev.overpass-api.de/blog/sliced_time_and_space.html#compare">Sliced Time and Space - Comparing Diffs</a>:</p>
<pre><code>[adiff:&quot;2018-05-30T15:00:00Z&quot;,&quot;2018-06-30T15:00:00Z&quot;];
way[&quot;oneway&quot;]({{bbox}});
compare(delta:t[&quot;oneway&quot;]);
out meta geom;</code></pre>
<p><em><a href="http://overpass-turbo.eu/s/Eai">Overpass Turbo</a></em></p>
<p>adiff results in the <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Augmented_Diffs#Contained_data">Augmented Diff</a> format can also be visualized in achavi (better shows create/modify/delete) by exporting the data into a file with "Export" &gt; "download raw OSM data" and drag&amp;drop onto the map at <a href="https://overpass-api.de/achavi/">https://overpass-api.de/achavi/</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Nov '18, 18:16</strong></p>
<img src="https://secure.gravatar.com/avatar/f92748c8fa508a936bcf2169b30cabf6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ikonor&#39;s gravatar image" />
<p><span>ikonor</span><br />
<span class="score" title="1286 reputation points"><span>1.3k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ikonor has 4 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-67014" class="comments-container">
<span id="67030"></span>
<div id="comment-67030" class="comment">
<div id="post-67030-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/2012/ikonor"></a><a href="https://help.openstreetmap.org/users/2012/ikonor">@ikonor</a> This is awesome thank you!<br />
Just a follow-up question will be possible to add USER here as well to this query? I tried running the code below but it's giving me false positives. Now that I answer the time question I wanna see if I can associate it with USER and see what changes a USER or a group of user has done to a specific tag. is that possible?</p>
<p>[adiff:"2018-05-30T15:00:00Z","2018-06-30T15:00:00Z"]; way<span>"oneway"</span>({{bbox}}); compare(delta:t["oneway"]); out meta geom;</p>
</div>
<div id="comment-67030-info" class="comment-info">
<span class="comment-age">(01 Dec '18, 20:43)</span> <span class="comment-user userinfo">mapsbyjujubee</span>
</div>
</div>
<span id="67040"></span>
<div id="comment-67040" class="comment">
<div id="post-67040-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I fear there is no proper way to filter adiff results by user. There is a user/uid filter [1], but that's weird and does not do what you would expect in an adiff query (e.g. misses deletes/tag removals), because what you would want is to filter the "new" objects in the adiff output, not the data in each timestamp query.</p>
<p>[1] <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#By_user_.28user.2C_uid.29">https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#By_user_.28user.2C_uid.29</a></p>
</div>
<div id="comment-67040-info" class="comment-info">
<span class="comment-age">(02 Dec '18, 13:41)</span> <span class="comment-user userinfo">ikonor</span>
</div>
</div>
</div>
<div id="comment-tools-67014" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67014-form-container" class="comment-form-container">
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

