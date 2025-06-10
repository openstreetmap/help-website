+++
type = "question"
title = "How can I make sense of munin.openstreetmap.org?"
description = '''There are so many servers and graphs on munin.openstreetmap.org - what do they tell me about the project? What can I, as a non-sysadmin, learn from these graphs? Which are the important ones? (relayed from talk-de)'''
date = "2010-08-01T10:11:00Z"
lastmod = "2010-08-01T18:27:00Z"
weight = 527
keywords = [ "munin", "server" ]
aliases = [ "/questions/527" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How can I make sense of munin.openstreetmap.org?](/questions/527/how-can-i-make-sense-of-muninopenstreetmaporg)

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
<span id="post-527-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-527-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-527-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
2
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>There are so many servers and graphs on <a href="http://munin.openstreetmap.org">munin.openstreetmap.org</a> - what do they tell me about the project? What can I, as a non-sysadmin, learn from these graphs? Which are the important ones?</p>
<p>(relayed from talk-de)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-munin" rel="tag" title="see questions tagged &#39;munin&#39;">munin</span> <span class="post-tag tag-link-server" rel="tag" title="see questions tagged &#39;server&#39;">server</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Aug '10, 10:11</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-527" class="comments-container">
&#10;</div>
<div id="comment-tools-527" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-527-form-container" class="comment-form-container">
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

<span id="529"></span>

<div id="answer-container-529" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-529-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-529-score" class="post-score" title="current number of votes">
8
</div>
<span id="post-529-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Frederik Ramm has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The first thing to remember about munin graphs is that they only tell you what's happening on the servers and it's extremely difficult to figure out <em>why</em> it might be happening from the graphs alone. For example, if editing seems slow and munin says the load is unusually high on the database server, this doesn't by itself say what the cause is, or what the solution might be.</p>
<p>On the other hand, the munin graphs can be very interesting and provide useful information to anyone interested in the technical side of OSM.</p>
<p>The first thing to look at is the <a href="http://wiki.openstreetmap.org/wiki/Servers">servers page on the wiki</a>. These do change from time to time, so it's best to look there for whatever the current state is. It is impossible to say which are the important ones, as this entirely depends on which of the OSM services you consider important. For example, if you're looking at the maps then the mapnik tile server might be the most important. If you're editing, then the rails front-end, back-end and database servers are all important.</p>
<p>Each of the servers on the wiki page has a direct link to munin. Following this will bring you to the summary page of munin, which shows the daily and weekly graphs for each of the monitors. There are many of these monitors, and while each is important in its own right, there are some which give a better overall understanding. One of these is "<a href="http://en.wikipedia.org/wiki/Load_Average">load average</a>" in the system section. To get an idea of the historical values of any graph, click on it to be taken to a page which additionally shows monthly and yearly graphs. If the current load average is much higher than historical values I know that this server is working much harder than usual.</p>
<p>Other useful graphs are the memory and CPU usage (in the system section) and disk I/O (in the disk section), which can help shed some light on why load might be high.</p>
<p>Some servers are running services which provide more detail. For example, the database server currently uses <a href="http://www.postgresql.org/">PostgreSQL</a> as the main database and this has it's own plugins in the "postgresql" section. An interesting one to look at is the "database size" graph which, although it changes slowly, shows the total amount of data in OSM. Another is the number of transactions, which roughly equates to the number of operations being executed on the database and has a distinctive daily cycle, caused by people using OSM across the world in varying amounts.</p>
<p>Another, on the mapnik tile server, is the "mod_tile" section. If, at some point in the future, the mapnik tiles aren't being served with mod_tile this will go away, perhaps replaced with something else. In the meantime, it is interesting to look at the "freshness of served tiles" graph, which shows the count of how many tiles were served to clients in which state. It's also worth looking at the network traffic graphs, as sometimes slow tile-serving can be a result of many other clients attempting to access the server.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Aug '10, 15:35</strong></p>
<img src="https://secure.gravatar.com/avatar/d53ec2d1ec832fdf10f72222db4fa710?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Matt&#39;s gravatar image" />
<p><span>Matt</span><br />
<span class="score" title="1161 reputation points"><span>1.2k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="18 badges"><span class="silver">●</span><span class="badgecount">18</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Matt has one accepted answer">33%</span></p>
</div>
</div>
<div id="comments-container-529" class="comments-container">
&#10;</div>
<div id="comment-tools-529" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-529-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="528"></span>

<div id="answer-container-528" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-528-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-528-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-528-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>That is an interesting question, but one that is difficult to answer in that generality, as it will depend on what exactly you would want to see. Furthermore, the graphs are mainly meant for sysadmins, so many of the graphs are rather uninteresting for "normal users".</p>
<p>However, there are a couple of graphs, that can help the general users understand the status of the OpenStreetMap servers and if they are experiencing a load that makes it likely that the users will see detrimental effects.</p>
<p>The answer probably splits into three categories:</p>
<p>1) The map tile server: This machine is called yevaud and thus its munin graphs are <a href="http://munin.openstreetmap.org/openstreetmap/yevaud.openstreetmap/">here</a> Here, the most interesting graphs are probably in the "renderd" section.</p>
<p>The first of the graphs, show the <a href="http://munin.openstreetmap.org/openstreetmap/yevaud.openstreetmap/replication_delay2.html">database lag</a>. I.e. the time the rendering is behind the main database and thus the minimum amount of time it takes before edits made in OSM can possibly show up on the map. Typical lags are in the range of 1 - 10 minutes.</p>
<p>The second graph shows the rendering <a href="http://munin.openstreetmap.org/openstreetmap/yevaud.openstreetmap/renderd_queue.html">queue lengths</a>. I.e. how many tiles are currently waiting to be rerendered. The priority queue is filled with requests whos tiles don't yet exists and thus if not rendered on time will result in a "more OSM coming soon" tile. The render queue is used for tiles that are out of date and which the server tries to render "on the fly" to ensure that users always see the most up to date tiles. However, if tiles can't be rendered quickly enough, they get rendered in the background and get added to the overflow queue, the "dirty queue". The "dirty queue" shows you how long you can expect it to take for your tiles to get rerendered and show up to date information.</p>
<p>The third graph, shows how many tiles are currently being <a href="http://munin.openstreetmap.org/openstreetmap/yevaud.openstreetmap/renderd_processed.html">rendered</a>. Here, perhaps the most interesting part is the "dropped" value, which shows how many requests for updating tiles get dropped as the "dirty queue" is full. If requests get dropped, then the next time you visit the tiles, they may still not have updated and means that you may see more out of date tiles, or odd artefacts with parts of the map having been updated and other adjacent parts not. Otherwise, the graphs show if the rendering is working at all.</p>
<p>The other major graph that is of interest, is perhaps the <a href="http://munin.openstreetmap.org/openstreetmap/yevaud.openstreetmap/if_eth1.html">Network graph</a> which shows how much data the server is handing out. Given that the network of the hoster is only a 100Mbit/s, in extreme traffic spikes, you might see that the tile server is limited by the network and thus can't hand out tiles fast enough.</p>
<p>2) Editing and the rails servers <a href="http://munin.openstreetmap.org/openstreetmap/puff.openstreetmap/#passenger">Puff</a>, <a href="http://munin.openstreetmap.org/openstreetmap/norbert.openstreetmap/index.html#passenger">Norbert</a></p>
<p>TODO: needs to be covered in an update</p>
<p>3) Other services like <a href="http://munin.openstreetmap.org/openstreetmap/katie.openstreetmap/#nominatim">Nominatim</a>, <a href="http://%5Bwiki%5Dhttp://munin.openstreetmap.org">[wiki]http://munin.openstreetmap.org</a>/openstreetmap/konqi.openstreetmap/index.html</p>
<p>TODO: needs explanation of the graphs</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Aug '10, 15:33</strong></p>
<img src="https://secure.gravatar.com/avatar/32c974c4ca8b246698c2b82c64924da5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="apmon&#39;s gravatar image" />
<p><span>apmon</span><br />
<span class="score" title="6527 reputation points"><span>6.5k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="44 badges"><span class="silver">●</span><span class="badgecount">44</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="apmon has 9 accepted answers">20%</span></p>
</div>
</div>
<div id="comments-container-528" class="comments-container">
<span id="531"></span>
<div id="comment-531" class="comment">
<div id="post-531-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Great answer as well, Matt's and yours should really be merged into one! Voted both up but can "accept" only one...</p>
</div>
<div id="comment-531-info" class="comment-info">
<span class="comment-age">(01 Aug '10, 18:27)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-528" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-528-form-container" class="comment-form-container">
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

