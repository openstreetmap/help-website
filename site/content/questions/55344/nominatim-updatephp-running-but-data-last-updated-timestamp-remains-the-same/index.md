+++
type = "question"
title = "Nominatim update.php running but &#x27;Data last updated&#x27; timestamp remains the same"
description = '''I have freshly installed Nominatim on a brand new server and went through all the instructions to import the full planet osm data. All worked well and I have a Nominatim installation working now, capable of doing search and reverse search. I downloaded the full planet file on the 5th of March 2017, ...'''
date = "2017-03-29T22:30:00Z"
lastmod = "2017-04-04T21:50:00Z"
weight = 55344
keywords = [ "nominatim", "update", "osmosis" ]
aliases = [ "/questions/55344" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Nominatim update.php running but 'Data last updated' timestamp remains the same](/questions/55344/nominatim-updatephp-running-but-data-last-updated-timestamp-remains-the-same)

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
<span id="post-55344-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55344-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-55344-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have freshly installed Nominatim on a brand new server and went through all the instructions to import the full planet osm data. All worked well and I have a Nominatim installation working now, capable of doing search and reverse search. I downloaded the full planet file on the 5th of March 2017, and it took a bit less than a couple of weeks to index, and now it is running fine. The home page displays:</p>
<p>Data last updated: 2017/02/28 23:58GMT.</p>
<p>I suppose this is the date the OSM file was generated.</p>
<p>I have now tried to set up the updater and after installing osmosis I updated the settings in local.php as follows:</p>
<pre><code>@define(&#39;CONST_Osmosis_Binary&#39;, &#39;/usr/bin/osmosis&#39;);    
@define(&#39;CONST_Replication_Url&#39;, &#39;http://planet.openstreetmap.org/replication/day&#39;);
@define(&#39;CONST_Replication_MaxInterval&#39;, &#39;3600&#39;);
@define(&#39;CONST_Replication_Update_Interval&#39;, &#39;60&#39;);  // How often upstream publishes diffs
@define(&#39;CONST_Replication_Recheck_Interval&#39;, &#39;60&#39;); // How long to sleep if no update found yet</code></pre>
<p>I changed to use day replication because I wanted to recover 3 weeks of updates or so, and updating every day is enough for me. Then I did:</p>
<pre><code>./utils/setup.php --osmosis-init
./utils/setup.php --create-functions --enable-diff-updates</code></pre>
<p>And finally ran this:</p>
<pre><code>nohup ./utils/update.php --import-osmosis-all &amp;</code></pre>
<p>It seemed to be doing a lot of stuff and took quite a number of hours to stop outputing logs. It seems to be running periodically too.</p>
<p>However, Nominatim's web page is still showing that the Data last updated: 2017/02/28 23:58GMT.</p>
<p>How to I check if osmosis is really updating correctly?</p>
<p>My configuration.txt has the following:</p>
<pre><code># The URL of the directory containing change files.
baseUrl=http://planet.openstreetmap.org/replication/day
&#10;# Defines the maximum time interval in seconds to download in a single invocation.
# Setting to 0 disables this feature.
maxInterval = 3600</code></pre>
<p>I have this in my state.txt:</p>
<pre><code>#Wed Mar 29 20:46:08 CEST 2017
sequenceNumber=1659
timestamp=2017-03-29T00\:00\:00Z</code></pre>
<p>I've tried to change the maxInterval to 0, in case that was affecting it. Did it 4 hours ago, but still the data last updated time is the same.</p>
<p>The output of update.php is showing lines like:</p>
<pre><code>  Done 75495 in 11397 @ 6.624112 per second - Rank 26 ETA (seconds): 17284.882812
  Done 75498 in 11398 @ 6.623794 per second - Rank 26 ETA (seconds): 17285.261719
  Done 75506 in 11398 @ 6.624496 per second - Rank 26 ETA (seconds): 17282.222656
  Done 75515 in 11399 @ 6.624704 per second - Rank 26 ETA (seconds): 17280.320312</code></pre>
<p>What could be the reason the data is not updating properly?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-update" rel="tag" title="see questions tagged &#39;update&#39;">update</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Mar '17, 22:30</strong></p>
<img src="https://secure.gravatar.com/avatar/e01618347bd158e35c34cce5bc006a92?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jbx1&#39;s gravatar image" />
<p><span>jbx1</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jbx1 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Mar '17, 22:31</strong> </span></p>
</div>
</div>
<div id="comments-container-55344" class="comments-container">
<span id="55362"></span>
<div id="comment-55362" class="comment">
<div id="post-55362-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Did the update script finish? It starts with rank 2 and goes to rank 30. Rank 30 (buildings) usually takes twice as long as rank 28. When I see ETA 17000 seconds that's 5 further just for rank 28 to finish, then a new ETA for rank 30 will be shown.</p>
</div>
<div id="comment-55362-info" class="comment-info">
<span class="comment-age">(30 Mar '17, 10:13)</span> <span class="comment-user userinfo">mtmail</span>
</div>
</div>
<span id="55367"></span>
<div id="comment-55367" class="comment">
<div id="post-55367-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Well I restarted yesterday with that change in setting of MaxInterval to 0 in configuration.txt and local.php. It is still in Rank 26 it seems! Is it normal to take so long to update? I have this now: Done 185023 in 77387 @ 2.390880 per second - Rank 26 ETA (seconds): 2078.314697 Done 185023 in 77388 @ 2.390849 per second - Rank 26 ETA (seconds): 2078.341553</p>
</div>
<div id="comment-55367-info" class="comment-info">
<span class="comment-age">(30 Mar '17, 16:50)</span> <span class="comment-user userinfo">jbx1</span>
</div>
</div>
<span id="55475"></span>
<div id="comment-55475" class="comment">
<div id="post-55475-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It is still running (after the restart of the 30th of March) and still the Data last updated date is the same. At some point it was doing Rank 27, now it is again doing Rank 19.<br />
<code>Done 19201 in 1745 @ 11.003438 per second - Interpolation lines ETA (seconds): 3569.702393 Done 13022 in 5464 @ 2.383236 per second - Rank 19 ETA (seconds): 19723.605469</code></p>
<p>Should I restart it? Will it resume if I stop it? Can I do something about it?</p>
</div>
<div id="comment-55475-info" class="comment-info">
<span class="comment-age">(04 Apr '17, 21:50)</span> <span class="comment-user userinfo">jbx1</span>
</div>
</div>
</div>
<div id="comment-tools-55344" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55344-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

