+++
type = "question"
title = "What does &quot;unordered&quot; mean in visibility option for GPS traces?"
description = ''' On the OSM Upload GPS Trace page the public option is described as &quot;shown in trace list and as anonymous, unordered points&quot;. However, the public properties described on this wiki page says &quot;points are chronologically ordered&quot;. So which is it?  This is a question on talk page of Visibility of GPS tr...'''
date = "2018-11-06T10:37:00Z"
lastmod = "2018-11-08T20:35:00Z"
weight = 66689
keywords = [ "website", "traces", "visibility" ]
aliases = [ "/questions/66689" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [What does "unordered" mean in visibility option for GPS traces?](/questions/66689/what-does-unordered-mean-in-visibility-option-for-gps-traces)

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
<span id="post-66689-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66689-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-66689-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<blockquote>
<p>On the OSM Upload GPS Trace page the public option is described as "shown in trace list and as anonymous, unordered points". However, the public properties described on this wiki page says "points are chronologically ordered". So which is it?</p>
</blockquote>
<p>This is a question on talk page of <a href="https://wiki.openstreetmap.org/wiki/Visibility_of_GPS_traces">Visibility of GPS traces</a>.</p>
<p>This is a question for me too. Is it a mistake or it has a meaning I'm not aware of that?</p>
<p><img src="/upfiles/Untitled_5ZOiQVq.png" alt="visibility option for uploading GPS trace" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-website" rel="tag" title="see questions tagged &#39;website&#39;">website</span> <span class="post-tag tag-link-traces" rel="tag" title="see questions tagged &#39;traces&#39;">traces</span> <span class="post-tag tag-link-visibility" rel="tag" title="see questions tagged &#39;visibility&#39;">visibility</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Nov '18, 10:37</strong></p>
<img src="https://secure.gravatar.com/avatar/5b2d680cd0c22a32517db07ed16eeaf2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iriman&#39;s gravatar image" />
<p><span>iriman</span><br />
<span class="score" title="297 reputation points">297</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="iriman has one accepted answer">33%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Nov '18, 16:47</strong> </span></p>
</div>
</div>
<div id="comments-container-66689" class="comments-container">
&#10;</div>
<div id="comment-tools-66689" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66689-form-container" class="comment-form-container">
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

<span id="66729"></span>

<div id="answer-container-66729" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-66729-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66729-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-66729-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="iriman has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="https://github.com/tomhughes/openstreetmap-website/commit/cdb42d2a6ce539be3f3e50edebb88240dfd16e04">Since 7th November 2018</a> (background: see my other, older "answer" here) "unordered" means more less what it says: your uploaded points are available via the <a href="https://wiki.openstreetmap.org/wiki/API_v0.6#Retrieving_GPS_points"><code>trackpoints</code> API call</a> lumped together with all other "unordered" points and returned <em>in latitude-longitude-timestamp order</em> (that is: sorted by coordinates). These "unordered" points are useful for point-cloud or heatmap-style presentation, but hardly for showing them as lines.</p>
<p>Privacy notes: If there are multiple such unordered traces in an area then it is not easy (of not impossible) to reconstruct a single trace. However, be aware: if there is only a single trace uploaded in a specific area, then it may be obvious that all the few points in that area belong together (like breadcrumbs on a path).</p>
<p>Further note that although the points are available only unordered they <em>are</em> available publicly - in contrast to what one may interpret into the label "private". Hence, it is no good idea to upload traces of secret places - see <a href="https://web.archive.org/web/20181027135414/https://www.theguardian.com/world/2018/jan/28/fitness-tracking-app-gives-away-location-of-secret-us-army-bases">strava's issues</a> with this in January 2018.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Nov '18, 18:04</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-66729" class="comments-container">
&#10;</div>
<div id="comment-tools-66729" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66729-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="66705"></span>

<div id="answer-container-66705" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-66705-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66705-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-66705-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I think that is just a text mistake and it should be "ordered" points on the website. We likely all agree that with the few traces which we have a point cloud (which unordered would mean) is of not much sense (this is different for e.g. <a href="https://wiki.openstreetmap.org/wiki/Strava">Strava</a> who have many many points and can produce a heatmeap/pointcloud from that).</p>
<p><strong>I simply tested it:</strong></p>
<p>In 2014 I uploaded<code>*</code> a trace with "Visibility: Private (only shared as anonymous, unordered points)". If I now start a JOSM (which does <em>not</em> have my OSM credentials/Oauth to be sure) and download traces from the server (JOSM issues a API call to /api/0.6/trackpoints ) then I see the trace as a line - which is clearly showing that the points are in the right order.</p>
<p>Screenshot of the downloaded trace (thin, green) and the original trace (thick, darkred) opened from a local gpx file for comparison and a default map in the background. <img src="/upfiles/trace_map_redisfile_greenisdownloaded.png" alt="screenshot1" /></p>
<p>Screenshot of the downloaded traces list in JOSM showing no info about my "private" trace. In fact the "length" given is fully wrong because that is apparently the summarized length of all private traces in that download area together. <img src="/upfiles/tracelist,_mine_is_selected.png" alt="screenshot2" /></p>
<p><code>*</code><span class="small">usually I upload with "TRACKABLE" as this conveys the speed which is useful to distinguish walking from cycling or motor_vehicles.</span></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Nov '18, 16:25</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Nov '18, 16:33</strong> </span></p>
</div>
</div>
<div id="comments-container-66705" class="comments-container">
<span id="66706"></span>
<div id="comment-66706" class="comment">
<div id="post-66706-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I think the devs like to get requests at <a href="https://github.com/openstreetmap/openstreetmap-website/issues">github</a> instead of trac, anybody using github willing to request a change of the wording?</p>
</div>
<div id="comment-66706-info" class="comment-info">
<span class="comment-age">(06 Nov '18, 16:29)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="66707"></span>
<div id="comment-66707" class="comment">
<div id="post-66707-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>I opened an issue on <a href="https://github.com/openstreetmap/openstreetmap-website/issues/2046">github</a></p>
</div>
<div id="comment-66707-info" class="comment-info">
<span class="comment-age">(06 Nov '18, 19:18)</span> <span class="comment-user userinfo">iriman</span>
</div>
</div>
<span id="66714"></span>
<div id="comment-66714" class="comment">
<div id="post-66714-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>… API behaviour has now been changed to adhere to the descriptions (NOT the wiki descriptions!). As we could guess, there is now a JOSM issue with GPS point downloading: <a href="https://josm.openstreetmap.de/ticket/16963">JOSM ticket</a>. (Update:) I created a <a href="https://trac.openstreetmap.org/ticket/5503">Potlatch2 ticket</a>, too.</p>
</div>
<div id="comment-66714-info" class="comment-info">
<span class="comment-age">(07 Nov '18, 14:57)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="66720"></span>
<div id="comment-66720" class="comment">
<div id="post-66720-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>I have uploaded nearly 500 gpx 'Public' traces on the basis that they were displayed with lines joining the points on JOSM and the Standard lay of OpenStreetMap.org with'Public GPS Traces'selected. Will this still be the case or will I need to upload nearly 500 traces again as 'Trackable' to get a sensible display of the traces.</p>
</div>
<div id="comment-66720-info" class="comment-info">
<span class="comment-age">(08 Nov '18, 06:56)</span> <span class="comment-user userinfo">nevw</span>
</div>
</div>
<span id="66721"></span>
<div id="comment-66721" class="comment not_top_scorer">
<div id="post-66721-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/7380/nevw"></a><a href="https://help.openstreetmap.org/users/7380/nevw">@nevw</a>: I agree, that it is quite unfortunate that the API behaved a very long time in the way it did and that it is changed all of a sudden now.</p>
<p>At least re-uploading is not needed; you could change the visibility setting for each of your traces: Go to your uploaded traces list, click on the trace (not click "edit"!), then click "Edit this trace", then change the visibility and save.</p>
<p>However, note that the "trackable" option is publishing more details (exact timestamps!) than the "old private" did. Maybe another visibility option providing that "old private" behaviour would be good to have. Or a complete revamp of the visibility options... I would love to have trackable with masked timestamps: all original timestamps shifted by a random about in order to hide the original time, but to still convey the real speed info.</p>
</div>
<div id="comment-66721-info" class="comment-info">
<span class="comment-age">(08 Nov '18, 08:29)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="66723"></span>
<div id="comment-66723" class="comment">
<div id="post-66723-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>If a revamp of the visibility options was done it would also be helpful to be able to alter our trace option choice in bulk.</p>
</div>
<div id="comment-66723-info" class="comment-info">
<span class="comment-age">(08 Nov '18, 10:20)</span> <span class="comment-user userinfo">nevw</span>
</div>
</div>
<span id="66730"></span>
<div id="comment-66730" class="comment not_top_scorer">
<div id="post-66730-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/7380/nevw"></a><a href="https://help.openstreetmap.org/users/7380/nevw">@nevw</a> agreed. I have created <a href="https://github.com/openstreetmap/openstreetmap-website/issues/2054">this ticket</a> for bulk mode.</p>
</div>
<div id="comment-66730-info" class="comment-info">
<span class="comment-age">(08 Nov '18, 20:35)</span> <span class="comment-user userinfo">don-vip</span>
</div>
</div>
</div>
<div id="comment-tools-66705" class="comment-tools">
<span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-66705-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="66691"></span>

<div id="answer-container-66691" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-66691-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66691-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-66691-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Given that the last 2 options say "with timestamps", I always assumed that the points in the first 2 do not have timestamps. Without timestamps, one probably looses the ordering of the points, as there is no other construct in the GPX file that guarantees an order.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Nov '18, 11:27</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</img>
</div>
</div>
<div id="comments-container-66691" class="comments-container">
<span id="66693"></span>
<div id="comment-66693" class="comment">
<div id="post-66693-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>but we can be sure that the order is correct, otherwise it doesn't represent the same gps trace which is uploaded.</p>
</div>
<div id="comment-66693-info" class="comment-info">
<span class="comment-age">(06 Nov '18, 11:53)</span> <span class="comment-user userinfo">iriman</span>
</div>
</div>
<span id="66695"></span>
<div id="comment-66695" class="comment">
<div id="post-66695-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>It will be just a collection of points, not a real trace. At least that's my understanding of this option.</p>
</div>
<div id="comment-66695-info" class="comment-info">
<span class="comment-age">(06 Nov '18, 12:19)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-66691" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66691-form-container" class="comment-form-container">
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

