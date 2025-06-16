+++
type = "question"
title = "Java slippy map API"
description = '''Hi,  I am currently creating a slippy map for Java. Not Javascript, Java. The tile usage policy appears to be geared more towards using a browser, which I am not. Can somebody clarify it for me?  Valid User-Agent identifying application. Faking another app&#x27;s User-Agent WILL get you blocked.  What do...'''
date = "2011-08-04T18:24:00Z"
lastmod = "2011-08-05T22:41:00Z"
weight = 6888
keywords = [ "usage", "api", "java", "slippy" ]
aliases = [ "/questions/6888" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Java slippy map API](/questions/6888/java-slippy-map-api)

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
<span id="post-6888-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-6888-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-6888-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I am currently creating a slippy map for Java. Not Javascript, Java. The tile usage policy appears to be geared more towards using a browser, which I am not. Can somebody clarify it for me?</p>
<blockquote>
<p>Valid User-Agent identifying application. Faking another app's User-Agent WILL get you blocked.</p>
</blockquote>
<p>What do i use for a user-agent identifier?</p>
<blockquote>
<p>Maximum of 2 download threads. (Unmodified web browsers' download thread limits are acceptable.) Note: modern web browsers in standard configuration generally pass all the above technical requirements.</p>
</blockquote>
<p>So I can only request one thread to http://[abc].<a href="http://tile.openstreetmap.org/zoom/x/y.png">tile.openstreetmap.org/zoom/x/y.png</a><br />
</p>
<p>eg.</p>
<p>my api requests: <a href="http://a.tile.opentstreetmap.org/8/2323/5465.png">http://a.tile.opentstreetmap.org/8/2323/5465.png</a> and <a href="http://b.tile.opentstreetmap.org/8/4542/7657.png">http://b.tile.opentstreetmap.org/8/4542/7657.png</a> but it can't make another request like this: <a href="http://c.tile.opentstreetmap.org/8/56565/7867.png">http://c.tile.opentstreetmap.org/8/56565/7867.png</a> until a and b are finished loading?</p>
<p>Also can I send two requests to the same server? so i send two requests to a and b?</p>
<p>thank you!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-usage" rel="tag" title="see questions tagged &#39;usage&#39;">usage</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-java" rel="tag" title="see questions tagged &#39;java&#39;">java</span> <span class="post-tag tag-link-slippy" rel="tag" title="see questions tagged &#39;slippy&#39;">slippy</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Aug '11, 18:24</strong></p>
<img src="https://secure.gravatar.com/avatar/bb1529902fcb9f95fece81cc067b862e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="meerkat_aicml&#39;s gravatar image" />
<p><span>meerkat_aicml</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="meerkat_aicml has no accepted answers">0%</span> </br></p>
</div>
</div>
<div id="comments-container-6888" class="comments-container">
<span id="6889"></span>
<div id="comment-6889" class="comment">
<div id="post-6889-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>You may want to take a look at: <a href="https://wiki.openstreetmap.org/wiki/LiveMapViewer">https://wiki.openstreetmap.org/wiki/LiveMapViewer</a> It is written in java, it uses "slippy map" and it's source code is available.</p>
</div>
<div id="comment-6889-info" class="comment-info">
<span class="comment-age">(04 Aug '11, 19:26)</span> <span class="comment-user userinfo">RM87</span>
</div>
</div>
<span id="6921"></span>
<div id="comment-6921" class="comment">
<div id="post-6921-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Have a look at JMapViewer ( <a href="http://trac.openstreetmap.org/browser/applications/viewer/jmapviewer">http://trac.openstreetmap.org/browser/applications/viewer/jmapviewer</a> )</p>
<p>JMapViewer is a Java Swing component for integrating OSM maps in to your Java application.</p>
<p>LiveEditMapViewer mentioned in the comment above uses jmapviewer as its slippy map component.</p>
</div>
<div id="comment-6921-info" class="comment-info">
<span class="comment-age">(05 Aug '11, 22:18)</span> <span class="comment-user userinfo">apmon</span>
</div>
</div>
</div>
<div id="comment-tools-6888" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-6888-form-container" class="comment-form-container">
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

<span id="6890"></span>

<div id="answer-container-6890" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-6890-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-6890-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-6890-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="meerkat_aicml has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The User-Agent is the name of your program. It is important for identifying what application is violating the terms and can be used to block those versions of the program.</p>
<p>There are currently only two servers that are serving tiles. The [abc].<a href="http://tile.openstreetmap.org">tile.openstreetmap.org</a> and <a href="http://tile.openstreetmap.org">tile.openstreetmap.org</a> each map to one of theese two servers. The most important is that you do not send to many requests to the servers at once. The problem is people that are downloading a lot of tiles for offload use where most tiles are not displayed to any users.</p>
<p>If you are woried that you may download too many tiles too fast you can always set up your own tile server.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Aug '11, 19:30</strong></p>
<img src="https://secure.gravatar.com/avatar/44a4438f0146dfd898e24c221fd28b58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gnonthgol&#39;s gravatar image" />
<p><span>Gnonthgol ♦</span><br />
<span class="score" title="13750 reputation points"><span>13.8k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="103 badges"><span class="silver">●</span><span class="badgecount">103</span></span><span title="198 badges"><span class="bronze">●</span><span class="badgecount">198</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gnonthgol has 57 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Aug '11, 14:14</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/f09c0b7a655fed386e070e036e2da248?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dieterdreist&#39;s gravatar image" />
<p><span>dieterdreist</span><br />
<span class="score" title="3677 reputation points"><span>3.7k</span></span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="67 badges"><span class="bronze">●</span><span class="badgecount">67</span></span></p>
</div>
</div>
<div id="comments-container-6890" class="comments-container">
<span id="6891"></span>
<div id="comment-6891" class="comment">
<div id="post-6891-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for clarifying. Out of curiosity how many requests is too many?</p>
</div>
<div id="comment-6891-info" class="comment-info">
<span class="comment-age">(04 Aug '11, 20:29)</span> <span class="comment-user userinfo">meerkat_aicml</span>
</div>
</div>
<span id="6900"></span>
<div id="comment-6900" class="comment">
<div id="post-6900-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>The statement about the two servers is incorrect - all addresses map to the same cache server, and there is another server generating tiles behind that.</p>
<p>In any case, the "2 threads" limit are to any and all addresses combined. So if you wanted to use two addresses, you could only download 1 tile at a time from each.</p>
</div>
<div id="comment-6900-info" class="comment-info">
<span class="comment-age">(05 Aug '11, 09:17)</span> <span class="comment-user userinfo">Andy Allan</span>
</div>
</div>
<span id="6916"></span>
<div id="comment-6916" class="comment">
<div id="post-6916-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Okay so would it be any faster to use two addresses than one? Or would the server treat both requests the same?</p>
</div>
<div id="comment-6916-info" class="comment-info">
<span class="comment-age">(05 Aug '11, 16:37)</span> <span class="comment-user userinfo">meerkat_aicml</span>
</div>
</div>
<span id="6922"></span>
<div id="comment-6922" class="comment">
<div id="post-6922-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Just for the record, [abc].tile do currently map onto two caching servers (konqi,albi), which are front ends to a single server.</p>
<p>Funnily enough, the aliases [abc] are actually there explicitly to violate this policy of two threads. By default browsers only open n simultanoius connections per domain. In order to get the browser to open more simultanious connections and reduce latency, aliases are introduced which each get n connections.</p>
<p>So in Java it doesn't really matter to which server you connect and you might as well only use <a href="http://tile.osm.org">tile.osm.org</a>, although in future that might change.</p>
</div>
<div id="comment-6922-info" class="comment-info">
<span class="comment-age">(05 Aug '11, 22:34)</span> <span class="comment-user userinfo">apmon</span>
</div>
</div>
<span id="6923"></span>
<div id="comment-6923" class="comment">
<div id="post-6923-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>The policies are generally written to prevent server overload from massive automated downloads, that can quickly rack up 10.000s of tiles.</p>
<p>The policy kind of works as "if it causes troubles to the servers" it is "illegal". If the load is low and no admin notices it is fine. So what is allowed and what not is kind of fuzzy.</p>
<p>To get an indication of what gets noticed: <a href="https://wiki.openstreetmap.org/wiki/Talk:Tile_usage_policy#Usage_stats_for_Monday_1st_March_2010">https://wiki.openstreetmap.org/wiki/Talk:Tile_usage_policy#Usage_stats_for_Monday_1st_March_2010</a> <a href="http://munin.openstreetmap.org/openstreetmap/yevaud.openstreetmap/index.html#mod_tile">http://munin.openstreetmap.org/openstreetmap/yevaud.openstreetmap/index.html#mod_tile</a></p>
</div>
<div id="comment-6923-info" class="comment-info">
<span class="comment-age">(05 Aug '11, 22:41)</span> <span class="comment-user userinfo">apmon</span>
</div>
</div>
</div>
<div id="comment-tools-6890" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-6890-form-container" class="comment-form-container">
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

