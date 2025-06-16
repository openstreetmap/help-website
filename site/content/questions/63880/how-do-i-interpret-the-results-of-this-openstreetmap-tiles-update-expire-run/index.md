+++
type = "question"
title = "How do I interpret the results of this openstreetmap-tiles-update-expire run?"
description = '''With my tile server up and running, I went to experiment with updating the data.  My original data covered the US state California (2018-05-28T20:00:02Z). In openstreetmap-tiles-update-expire my changes included -b -124.0 30.0 -113.0 42.0 which, unless I goofed something, should encompass the geogra...'''
date = "2018-05-30T18:46:00Z"
lastmod = "2018-05-30T20:09:00Z"
weight = 63880
keywords = [ "state.txt", "update", "osmosis" ]
aliases = [ "/questions/63880" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How do I interpret the results of this openstreetmap-tiles-update-expire run?](/questions/63880/how-do-i-interpret-the-results-of-this-openstreetmap-tiles-update-expire-run)

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
<span id="post-63880-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63880-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-63880-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>With my tile server up and running, I went to experiment with updating the data.</p>
<p>My original data covered the US state California (2018-05-28T20:00:02Z). In <code>openstreetmap-tiles-update-expire</code> my changes included <code>-b -124.0 30.0 -113.0 42.0</code> which, unless I goofed something, should encompass the geographic mass desired.</p>
<p>Here was my command: <code>sudo ~/src/mod_tile/openstreetmap-tiles-update-expire 2018-05-28T20:00:02Z</code></p>
<p><img src="/upfiles/OSM_Update_Results_9AUnsuP.png" alt="alt text" /></p>
<p>And the content of <code>state.txt</code>:</p>
<pre><code>#original-source: http://planet.openstreetmap.org/replication/minute/002/990/717.state.txt
#generated-by: https://replicate-sequences.osm.mazdermind.de/?2018-05-28T20:00:02ZT00:00:00Z
#Mon May 28 19:59:04 UTC 2018
txnMaxQueried=1631231293
sequenceNumber=2990717
timestamp=2018-05-28T19\:59\:02Z
txnReadyList=
txnMax=1631231293
txnActiveList=1631231235,1631231290</code></pre>
<p>Please help me understand how to interpret these results. The <code>run.log</code> only stated that the Osmosis replication system was initializing, and so I'm assuming nothing was imported or update. Does this mean there were no updates found? Or, is something not configured right so the process failed silently?</p>
<p>Thanks!</p>
<p>Tim</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-state.txt" rel="tag" title="see questions tagged &#39;state.txt&#39;">state.txt</span> <span class="post-tag tag-link-update" rel="tag" title="see questions tagged &#39;update&#39;">update</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 May '18, 18:46</strong></p>
<img src="https://secure.gravatar.com/avatar/9d2fa479c7f7984fd8fd435b2badbc4d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tim_rohrer&#39;s gravatar image" />
<p><span>tim_rohrer</span><br />
<span class="score" title="81 reputation points">81</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tim_rohrer has one accepted answer">100%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 May '18, 18:48</strong> </span></p>
</div>
</div>
<div id="comments-container-63880" class="comments-container">
<span id="63881"></span>
<div id="comment-63881" class="comment">
<div id="post-63881-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>sudo ~/src/mod_tile/openstreetmap-tiles-update-expire 2018-05-28T20:00:02Z has initialised the replication system to that date; run it without the date to update.</p>
<p>Actually I wouldn't tend to do it through sudo but through a normal user account, but the principle is the same.</p>
</div>
<div id="comment-63881-info" class="comment-info">
<span class="comment-age">(30 May '18, 18:55)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="63882"></span>
<div id="comment-63882" class="comment">
<div id="post-63882-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Running without the date gave me: rm: cannot remove '/var/lib/mod_tile/changes.osc.gz': No such file or directory rm: cannot remove '/var/lib/mod_tile/dirty_tiles.29567': No such file or directory</p>
<p>Now I'm researching that.</p>
<p>The reason for sudo is that I did most of my compiling with my regular account but had created a <code>tileserver</code> user for running things. I'm now learning it would have been easier to create the <code>tileserver</code> user first, then install/build everything under that. Or, maybe there is a better way?</p>
</div>
<div id="comment-63882-info" class="comment-info">
<span class="comment-age">(30 May '18, 19:11)</span> <span class="comment-user userinfo">tim_rohrer</span>
</div>
</div>
<span id="63884"></span>
<div id="comment-63884" class="comment">
<div id="post-63884-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'd pick one user and use that throughout.</p>
<p>The "cannot remove" error might mean it failed to dowbload it in the first place - edit the script to not remove the temporary files that it creates (or rename them to "something.$$" so that you can look at the files afterwards). Check you're using https, not http, throughout. If you're using openstreetmap's version of openstreetmap-tiles-update-expire rather than the switch2osm version, you'll need to change it for https.</p>
</div>
<div id="comment-63884-info" class="comment-info">
<span class="comment-age">(30 May '18, 19:19)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="63885"></span>
<div id="comment-63885" class="comment">
<div id="post-63885-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'm using switch2osm, but I'll double check the https when I go through the file.</p>
<p>To be clear, the script should do the download, right?</p>
</div>
<div id="comment-63885-info" class="comment-info">
<span class="comment-age">(30 May '18, 19:36)</span> <span class="comment-user userinfo">tim_rohrer</span>
</div>
</div>
<span id="63886"></span>
<div id="comment-63886" class="comment">
<div id="post-63886-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, the script should download and import the file.</p>
</div>
<div id="comment-63886-info" class="comment-info">
<span class="comment-age">(30 May '18, 19:38)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="63889"></span>
<div id="comment-63889" class="comment not_top_scorer">
<div id="post-63889-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Turns out my <code>tail</code> had died and froze the terminal. Not sure why but the additional notices I now see in the log indicate <code>Osmosis</code> isn't happy about something. I <em>think</em> I've address the permissions issues; my tileserver account owns everything other /var/lib/mod_tile.</p>
<p>I had installed osmosis from Ubuntu repo, and it is failing for what appear to be java errors.</p>
<p>I'm off to troubleshoot that now. I might be back soon with a new post :-)</p>
</div>
<div id="comment-63889-info" class="comment-info">
<span class="comment-age">(30 May '18, 20:09)</span> <span class="comment-user userinfo">tim_rohrer</span>
</div>
</div>
</div>
<div id="comment-tools-63880" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-63880-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

