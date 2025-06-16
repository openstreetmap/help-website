+++
type = "question"
title = "Not getting output from tileserver when I reduce the AWS RDS memory size to 16GB"
description = '''Hi all, I was using RDS instance db.r4.xlarge (RAM - 32GB CPU-4 ) to store the database and do the SQL queries for tileserver. It was working perfectly and getting output. However, when I tried to downgrade the RDS instance to db.r4.large (RAM-16GB and CPU-2vCPU), it is showing the following error. ...'''
date = "2018-02-15T10:17:00Z"
lastmod = "2018-03-08T10:49:00Z"
weight = 62113
keywords = [ "rendering", "tileserver", "aws", "database", "memory" ]
aliases = [ "/questions/62113" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Not getting output from tileserver when I reduce the AWS RDS memory size to 16GB](/questions/62113/not-getting-output-from-tileserver-when-i-reduce-the-aws-rds-memory-size-to-16gb)

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
<span id="post-62113-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62113-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-62113-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all, I was using RDS instance db.r4.xlarge (RAM - 32GB CPU-4 ) to store the database and do the SQL queries for tileserver. It was working perfectly and getting output. However, when I tried to downgrade the RDS instance to db.r4.large (RAM-16GB and CPU-2vCPU), it is showing the following error.</p>
<p>DEBUG: START TILE ajt 0 0-0 0-0, new metatile renderd[14721]: Rendering projected coordinates 0 0 0 -&gt; -20037508.342800|-20037508.342800 20037508.342800|20037508.342800 to a 1 x 1 tile renderd[14721]: DEBUG: Connection 0, fd 6 closed, now 0 left</p>
<p>Please let me know if someone has any idea about this error.</p>
<p>Thanks Subin</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span> <span class="post-tag tag-link-aws" rel="tag" title="see questions tagged &#39;aws&#39;">aws</span> <span class="post-tag tag-link-database" rel="tag" title="see questions tagged &#39;database&#39;">database</span> <span class="post-tag tag-link-memory" rel="tag" title="see questions tagged &#39;memory&#39;">memory</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Feb '18, 10:17</strong></p>
<img src="https://secure.gravatar.com/avatar/95e9674b7a67d58ada813e0c6bc38d84?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="subinjp7&#39;s gravatar image" />
<p><span>subinjp7</span><br />
<span class="score" title="16 reputation points">16</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="subinjp7 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Feb '18, 17:11</strong> </span></p>
</div>
</div>
<div id="comments-container-62113" class="comments-container">
<span id="62114"></span>
<div id="comment-62114" class="comment">
<div id="post-62114-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>This is not an error message. Can you check if your postgresql log file or your syslog show any messages when you try to access the tile?</p>
</div>
<div id="comment-62114-info" class="comment-info">
<span class="comment-age">(15 Feb '18, 10:40)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="62117"></span>
<div id="comment-62117" class="comment">
<div id="post-62117-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I checked the sylog, but could not find anything specific. But in RDS instance, it shows that, connection to the client lost. But I am not sure, what is the reason behind losing the connection..Please help me.</p>
<p>Actually I used EC2 instance:m4.xlarge with 32 GB RAM and RDS instance: db.r4.xlarge with 32GB RAM to run osm2pgsql to convert openstreetmap data in to postgres database. I am currently using the following configuration for accessing full planet database for tileserver. EC2 instance:t2.medium with 4GB RAM for rendering purpose (front end) and RDS instance: db.r4.large with 16GB RAM to store database and run SQL queries.</p>
<p>Please let me know if it is enough to run tileserver for full planet or should I upgrade the configurations?</p>
</div>
<div id="comment-62117-info" class="comment-info">
<span class="comment-age">(15 Feb '18, 19:18)</span> <span class="comment-user userinfo">subinjp7</span>
</div>
</div>
<span id="62126"></span>
<div id="comment-62126" class="comment">
<div id="post-62126-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Without any error information it's difficult to comment further...</p>
</div>
<div id="comment-62126-info" class="comment-info">
<span class="comment-age">(15 Feb '18, 21:26)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="62128"></span>
<div id="comment-62128" class="comment">
<div id="post-62128-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Sometimes it shows the tiles when requesting the tiles for multiple times. I am not sure what is the reason behind this.</p>
<p>In the RDS instance, the following errors are showing while requesting tiles,</p>
<p>:LOG: could not send data to client: Connection timed out or LOG: could not receive data from client: Connection reset by peer</p>
</div>
<div id="comment-62128-info" class="comment-info">
<span class="comment-age">(15 Feb '18, 21:48)</span> <span class="comment-user userinfo">subinjp7</span>
</div>
</div>
<span id="62150"></span>
<div id="comment-62150" class="comment">
<div id="post-62150-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Does <code>dmesg</code> show "Out of memory" messages?</p>
</div>
<div id="comment-62150-info" class="comment-info">
<span class="comment-age">(16 Feb '18, 14:09)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="62151"></span>
<div id="comment-62151" class="comment not_top_scorer">
<div id="post-62151-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>No such messages...But while uploading the database, I have got many warning messages such as</p>
<p>NOTICE: Self-intersection at or near point 0.68302757542791204 46.349042878781603.</p>
<p>Does it have any relation to the current situation.</p>
</div>
<div id="comment-62151-info" class="comment-info">
<span class="comment-age">(16 Feb '18, 14:42)</span> <span class="comment-user userinfo">subinjp7</span>
</div>
</div>
</div>
<div id="comment-tools-62113" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-62113-form-container" class="comment-form-container">
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

<span id="62132"></span>

<div id="answer-container-62132" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-62132-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62132-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-62132-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="subinjp7 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It sounds to me as if your system is working normally, but very slow. This means when you access a tile that has not been pre-rendered, renderd will attempt to render the tile on the fly, and that takes too long, then someone along the way gives up and closes the connection. For a world-wide database you must have your database on SSD, and ideally the database should be local to the rendering machine and not connected to over the network. Otherwise you incur too many latencies.</p>
<p>On a very slow system you can still make it work "a little" by pre-rendering lots of tiles (see render_list), however you cannot pre-render the world on all zoom levels.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Feb '18, 00:23</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-62132" class="comments-container">
<span id="62141"></span>
<div id="comment-62141" class="comment">
<div id="post-62141-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your answer. But I would like to ask one more question. I upgraded my EC2 instance and tried to render it. When I tried to render following tiles with zoom level 10, it failed. example.com/10/536/378.png</p>
<p>But when I tried again to render the same tiles with zoom level 12 it worked and then I could render the tiles with zoom level 10 also. I am not sure what is the problem with this.Do you have any idea about this?</p>
</div>
<div id="comment-62141-info" class="comment-info">
<span class="comment-age">(16 Feb '18, 09:48)</span> <span class="comment-user userinfo">subinjp7</span>
</div>
</div>
<span id="62142"></span>
<div id="comment-62142" class="comment">
<div id="post-62142-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You've said "it failed", but haven't said what messages occurred in the syslog of the tile server related to tile generation between the "TILE START" and "TILE DONE" messages.</p>
</div>
<div id="comment-62142-info" class="comment-info">
<span class="comment-age">(16 Feb '18, 10:00)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="62146"></span>
<div id="comment-62146" class="comment">
<div id="post-62146-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I am not getting TILE DONE message when it is getting failed.</p>
</div>
<div id="comment-62146-info" class="comment-info">
<span class="comment-age">(16 Feb '18, 11:12)</span> <span class="comment-user userinfo">subinjp7</span>
</div>
</div>
</div>
<div id="comment-tools-62132" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62132-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="62144"></span>

<div id="answer-container-62144" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-62144-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62144-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-62144-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><img src="/upfiles/tiles000.PNG" alt="alt text" /></p>
<p>Please find the attached image here with. This is the error message showing file rendering a world map(example.com/0/0/0.png).</p>
<p>Does it have anything to do with database upload? Database has been uploaded successfully.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Feb '18, 10:50</strong></p>
<img src="https://secure.gravatar.com/avatar/95e9674b7a67d58ada813e0c6bc38d84?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="subinjp7&#39;s gravatar image" />
<p><span>subinjp7</span><br />
<span class="score" title="16 reputation points">16</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="subinjp7 has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Feb '18, 10:52</strong> </span></p>
</div>
</div>
<div id="comments-container-62144" class="comments-container">
<span id="62145"></span>
<div id="comment-62145" class="comment">
<div id="post-62145-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Moreover I would like to add some more points. While uploading the database, I have got many warning messages such as NOTICE: Self-intersection at or near point 0.68302757542791204 46.349042878781603.</p>
<p>Does it have any relation to the current situation.</p>
</div>
<div id="comment-62145-info" class="comment-info">
<span class="comment-age">(16 Feb '18, 11:10)</span> <span class="comment-user userinfo">subinjp7</span>
</div>
</div>
<span id="62147"></span>
<div id="comment-62147" class="comment">
<div id="post-62147-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Depending on the speed of the system the "DONE TILE" might be minutes or hours later.</p>
</div>
<div id="comment-62147-info" class="comment-info">
<span class="comment-age">(16 Feb '18, 13:11)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="62149"></span>
<div id="comment-62149" class="comment">
<div id="post-62149-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for your answer.</p>
<p>How can I make sure that, connection is not getting closed in a short period of time? If I change the ModTileMissingRequestTimeout to a large value, can I avoid that situation?</p>
<p>Do you have any idea about the reason behind failing happens at some zoom levels(most of the time, low zoom levels)?</p>
</div>
<div id="comment-62149-info" class="comment-info">
<span class="comment-age">(16 Feb '18, 13:38)</span> <span class="comment-user userinfo">subinjp7</span>
</div>
</div>
<span id="62574"></span>
<div id="comment-62574" class="comment">
<div id="post-62574-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, see Frederik's answer above. You're trying to use a hammer as a screwdriver and are wondering why none of the screws are going in properly.</p>
<p>Get it working on a local server or VPS first, then look for cloud services that actually meet the requirements.</p>
</div>
<div id="comment-62574-info" class="comment-info">
<span class="comment-age">(08 Mar '18, 10:49)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-62144" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62144-form-container" class="comment-form-container">
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

