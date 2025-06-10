+++
type = "question"
title = "Extremely slow Nominatim install with Docker"
description = '''I am trying to install Nominatim based off of a dockerized version of the tool found here: https://github.com/mediagis/nominatim-docker. I was successful with installing dockerised Nominatim with a smaller country locally. And the process ran pretty fast. Then, I got an EC2 instance with, 64GB memor...'''
date = "2019-12-22T03:34:00Z"
lastmod = "2019-12-22T17:09:00Z"
weight = 72200
keywords = [ "nominatim", "osm", "osm2pgsql" ]
aliases = [ "/questions/72200" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Extremely slow Nominatim install with Docker](/questions/72200/extremely-slow-nominatim-install-with-docker)

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
<span id="post-72200-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72200-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-72200-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am trying to install Nominatim based off of a dockerized version of the tool found here: <a href="https://github.com/mediagis/nominatim-docker.">https://github.com/mediagis/nominatim-docker.</a> I was successful with installing dockerised Nominatim with a smaller country locally. And the process ran pretty fast.</p>
<p>Then, I got an EC2 instance with, 64GB memory, 1TB SSD, and 6 core processors to do an install with the entire planet (48GB). The most of the planet file got processed fast, in about 6hours and when processing the relations gave an error and failed. When I ran the planet file based on the same docker image, the object parsing (specially ways) were extremely slow. About 100 times slower than the initial run. This is the error I got when the planet ran faster:</p>
<pre><code>Processing: Node(5640116k 412.0k/s) Way(625947k 118.89k/s) Relation(628790 712.11/s)2019-12-18 22:48:23.270 UTC [210] LOG:  incomplete message from client
2019-12-18 22:48:23.270 UTC [210] CONTEXT:  COPY place, line 233940695
2019-12-18 22:48:23.270 UTC [210] STATEMENT:  COPY place FROM STDIN
2019-12-18 22:48:23.270 UTC [207] LOG:  incomplete message from client
2019-12-18 22:48:23.270 UTC [207] CONTEXT:  COPY planet_osm_rels, line 598784
2019-12-18 22:48:23.270 UTC [207] STATEMENT:  COPY planet_osm_rels FROM STDIN
Killed
2019-12-18 22:48:23.275 UTC [210] ERROR:  unexpected EOF on client connection with an open transaction
2019-12-18 22:48:23.275 UTC [210] CONTEXT:  COPY place, line 233940695
2019-12-18 22:48:23.275 UTC [210] STATEMENT:  COPY place FROM STDIN
2019-12-18 22:48:23.275 UTC [207] ERROR:  unexpected EOF on client connection with an open transaction
2019-12-18 22:48:23.275 UTC [207] CONTEXT:  COPY planet_osm_rels, line 598784
2019-12-18 22:48:23.275 UTC [207] STATEMENT:  COPY planet_osm_rels FROM STDIN
2019-12-18 22:48:23.275 UTC [207] LOG:  could not send data to client: Broken pipe
2019-12-18 22:48:23.275 UTC [207] STATEMENT:  COPY planet_osm_rels FROM STDIN
2019-12-18 22:48:23.275 UTC [210] LOG:  could not send data to client: Broken pipe
2019-12-18 22:48:23.275 UTC [210] STATEMENT:  COPY place FROM STDIN
2019-12-18 22:48:23.275 UTC [207] FATAL:  terminating connection because protocol synchronization was lost
2019-12-18 22:48:23.325 UTC [210] FATAL:  terminating connection because protocol synchronization was lost
ERROR: No Data
string(7) &quot;No Data&quot;</code></pre>
<p>Finally, I just took a pbf of North America (8GB) and tried the install. Object parsing related to North America went relatively fast, but it is still working on rankings and indexes. The install is going on for over 16 hours.</p>
<p>I didn't do any PostgreSQL optimizations before running the install. When the object parsing is slow, I see the container is only using about 1% of the available memory.</p>
<p>In Nominatim install instructions (here: <a href="https://nominatim.org/release-docs/latest/admin/Installation/)">https://nominatim.org/release-docs/latest/admin/Installation/)</a> I see that with less config (32 GB RAM) a planet install is taking only 2 days. What am I doing wrong and how can I optimize the process?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Dec '19, 03:34</strong></p>
<img src="https://secure.gravatar.com/avatar/3fa98831cef96f8b9fb7530160338da7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="picmate&#39;s gravatar image" />
<p><span>picmate</span><br />
<span class="score" title="71 reputation points">71</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="picmate has one accepted answer">50%</span></p>
</div>
</div>
<div id="comments-container-72200" class="comments-container">
&#10;</div>
<div id="comment-tools-72200" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72200-form-container" class="comment-form-container">
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

<span id="72207"></span>

<div id="answer-container-72207" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72207-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72207-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-72207-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="picmate has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The mediagis docker image is not particularly well suited for large size imports like North America or the planet. Read the original Nominatim installation instructions to get an idea about tuning and here in particular the section on <a href="http://nominatim.org/release-docs/develop/admin/Installation/#postgresql-tuning">PostgreSQL tuning</a>, <a href="http://nominatim.org/release-docs/develop/admin/Import-and-Update/#flatnode-files">using flatnode files</a> and <a href="http://nominatim.org/release-docs/develop/admin/Import-and-Update/#initial-import-of-the-data">notes on time and memory use during import</a>.</p>
<p>A machine of your size should manage a planet import in 2-3 days but only if you use flatnode files and a tuned postgres configuration.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Dec '19, 16:39</strong></p>
<img src="https://secure.gravatar.com/avatar/d888b712d85dee0aa304297f2dc697c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lonvia&#39;s gravatar image" />
<p><span>lonvia</span><br />
<span class="score" title="6213 reputation points"><span>6.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lonvia has 43 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-72207" class="comments-container">
&#10;</div>
<div id="comment-tools-72207" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72207-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="72201"></span>

<div id="answer-container-72201" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72201-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72201-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-72201-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In the Docker file I don't see "--osm2pgsql-cache" set for the setup.php (<a href="https://nominatim.org/release-docs/latest/admin/Import-and-Update/#initial-import-of-the-data)">https://nominatim.org/release-docs/latest/admin/Import-and-Update/#initial-import-of-the-data)</a> That will give osm2pgsql more RAM to work with.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Dec '19, 04:17</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-72201" class="comments-container">
<span id="72205"></span>
<div id="comment-72205" class="comment">
<div id="post-72205-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks. Can I know whether 20 ways/sec parsing time is what I should expect for way parsing when working with this type of instance configuration?</p>
</div>
<div id="comment-72205-info" class="comment-info">
<span class="comment-age">(22 Dec '19, 13:27)</span> <span class="comment-user userinfo">picmate</span>
</div>
</div>
<span id="72208"></span>
<div id="comment-72208" class="comment">
<div id="post-72208-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I had around 6000k/s (node), 60k/s (way), 1000/s (relation) on the last planet import.</p>
</div>
<div id="comment-72208-info" class="comment-info">
<span class="comment-age">(22 Dec '19, 17:09)</span> <span class="comment-user userinfo">mtmail</span>
</div>
</div>
</div>
<div id="comment-tools-72201" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72201-form-container" class="comment-form-container">
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

