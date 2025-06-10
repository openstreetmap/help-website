+++
type = "question"
title = "Nominatim Setup with latest Planet PBF always fails"
description = '''Hi, in the last few days I have made several attempts to set up Nominatim with the latest planet pbf but the import always failed after it already ran for quite some time. Attempts were made with AWS Ubuntu 18.04 AMI, 1TB of Storage and both a m5.2xlarge (32GB memory + 32GB swapfile) as well as a m5...'''
date = "2019-03-03T00:04:00Z"
lastmod = "2019-03-03T16:59:00Z"
weight = 68221
keywords = [ "planet", "nominatim", "installation", "pbf" ]
aliases = [ "/questions/68221" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Nominatim Setup with latest Planet PBF always fails](/questions/68221/nominatim-setup-with-latest-planet-pbf-always-fails)

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
<span id="post-68221-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68221-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-68221-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, in the last few days I have made several attempts to set up Nominatim with the latest planet pbf but the import always failed after it already ran for quite some time. Attempts were made with AWS Ubuntu 18.04 AMI, 1TB of Storage and both a m5.2xlarge (32GB memory + 32GB swapfile) as well as a m5.4xlarge (64GB memory, no swapfile). Using smaller pbf's like germany works fine.</p>
<p>I am always following the installation guide on <a href="http://nominatim.org/release-docs/latest/appendix/Install-on-Ubuntu-18/">nominatim.org</a> with the exception that I am using a different user and directory: <code> export USERNAME=ubuntu export USERHOME=/home/ubuntu/nominatim </code></p>
<p>For my latest try (32GB memory + 32GB swapfile) I used this command: <code> ./utils/setup.php --osm-file planet-latest.osm.pbf --all --osm2pgsql-cache 24000 2&gt;&amp;1 | tee setup.log </code></p>
<p>and it failed with this message: <code> Processing: Node(5054999k 477.8k/s) Way(564535k 25.40k/s) Relation(3376050 729.64/s) ERROR: 1 select * from place limit 1 [nativecode=ERROR: relation "place" does not exist LINE 1: select * from place limit 1 ^] </code></p>
<p>There are no errors in /var/log/syslog.</p>
<p>PostgreSQL config: <code> shared_buffers = 2GB maintenance_work_mem = 10GB work_mem = 50MB effective_cache_size = 24GB synchronous_commit = off checkpoint_timeout = 10min checkpoint_completion_target = 0.9 </code></p>
<p>Excerpt from the postgresql log: <code> 2019-03-02 21:07:12.612 UTC [20827] LOG: checkpoints are occurring too frequently (23 seconds apart) 2019-03-02 21:07:12.612 UTC [20827] HINT: Consider increasing the configuration parameter "max_wal_size". 2019-03-02 21:07:41.033 UTC [20827] LOG: checkpoints are occurring too frequently (29 seconds apart) 2019-03-02 21:07:41.033 UTC [20827] HINT: Consider increasing the configuration parameter "max_wal_size". 2019-03-02 21:09:53.090 UTC [20827] LOG: checkpoints are occurring too frequently (29 seconds apart) 2019-03-02 21:09:53.090 UTC [20827] HINT: Consider increasing the configuration parameter "max_wal_size". 2019-03-02 22:32:11.844 UTC [21697] ubuntu@nominatim ERROR: relation "place" does not exist at character 15 2019-03-02 22:32:11.844 UTC [21697] ubuntu@nominatim STATEMENT: select * from place limit 1 2019-03-02 22:32:14.486 UTC [21805] ubuntu@nominatim LOG: incomplete message from client 2019-03-02 22:32:14.486 UTC [21805] ubuntu@nominatim CONTEXT: COPY place, line 212096963 2019-03-02 22:32:14.486 UTC [21805] ubuntu@nominatim STATEMENT: COPY place (osm_type, osm_id, class, type, name, admin_level, address, extratags, geometry) FROM STDIN 2019-03-02 22:32:14.486 UTC [21805] ubuntu@nominatim ERROR: unexpected EOF on client connection with an open transaction 2019-03-02 22:32:14.486 UTC [21805] ubuntu@nominatim CONTEXT: COPY place, line 212096963 2019-03-02 22:32:14.486 UTC [21805] ubuntu@nominatim STATEMENT: COPY place (osm_type, osm_id, class, type, name, admin_level, address, extratags, geometry) FROM STDIN 2019-03-02 22:32:14.486 UTC [21805] ubuntu@nominatim LOG: could not send data to client: Broken pipe 2019-03-02 22:32:14.486 UTC [21805] ubuntu@nominatim STATEMENT: COPY place (osm_type, osm_id, class, type, name, admin_level, address, extratags, geometry) FROM STDIN 2019-03-02 22:32:14.487 UTC [21808] ubuntu@nominatim LOG: incomplete message from client 2019-03-02 22:32:14.487 UTC [21808] ubuntu@nominatim CONTEXT: COPY planet_osm_rels, line 3376543 2019-03-02 22:32:14.487 UTC [21808] ubuntu@nominatim STATEMENT: COPY planet_osm_rels FROM STDIN;</code></p>
<code> </code>
<p>2019-03-02 22:32:14.487 UTC [21808] ubuntu@nominatim ERROR: unexpected EOF on client connection with an open transaction 2019-03-02 22:32:14.487 UTC [21808] ubuntu@nominatim CONTEXT: COPY planet_osm_rels, line 3376543 2019-03-02 22:32:14.487 UTC [21808] ubuntu@nominatim STATEMENT: COPY planet_osm_rels FROM STDIN;</p>
<p>2019-03-02 22:32:14.487 UTC [21808] ubuntu@nominatim LOG: could not send data to client: Broken pipe 2019-03-02 22:32:14.487 UTC [21808] ubuntu@nominatim STATEMENT: COPY planet_osm_rels FROM STDIN;</p>
</code>
<p><code>2019-03-02 22:32:14.487 UTC [21806] ubuntu@nominatim LOG: unexpected EOF on client connection with an open transaction 2019-03-02 22:32:14.487 UTC [21807] ubuntu@nominatim LOG: unexpected EOF on client connection with an open transaction 2019-03-02 22:32:14.520 UTC [21808] ubuntu@nominatim FATAL: terminating connection because protocol synchronization was lost 2019-03-02 22:32:14.607 UTC [21805] ubuntu@nominatim FATAL: terminating connection because protocol synchronization was lost </code></p>
<p>Is there any obvious error I am making?</p>
<p>Edit: I tried using a flatnode file a suggested by mtmail, but got the same result as before. The last two runs exited with the same error but already failed while still processing the nodes.</p>
<p>Here is the full setup script I am using: <a href="https://pastebin.com/mVWsbkWY">setup.sh</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-planet" rel="tag" title="see questions tagged &#39;planet&#39;">planet</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-installation" rel="tag" title="see questions tagged &#39;installation&#39;">installation</span> <span class="post-tag tag-link-pbf" rel="tag" title="see questions tagged &#39;pbf&#39;">pbf</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Mar '19, 00:04</strong></p>
<img src="https://secure.gravatar.com/avatar/1a203d985cdf6ea40d39c20131df7842?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Greenish%20Purple&#39;s gravatar image" />
<p><span>Greenish Purple</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Greenish Purple has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Mar '19, 08:47</strong> </span></p>
</div>
</div>
<div id="comments-container-68221" class="comments-container">
&#10;</div>
<div id="comment-tools-68221" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68221-form-container" class="comment-form-container">
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

<span id="68222"></span>

<div id="answer-container-68222" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68222-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68222-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-68222-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The processing line for whole planet would go to 6, possible 7 million relations (OpenStreetMap data keeps growing every month).</p>
<p>The setup steps and setting you posted look alright. 32GB should work, or rather the failure would look differently if you ran out of memory in that step of the setup. My last import used a cache size of 28000.</p>
<p>To me it all points to the client (osm2pgsql)-server connection crashing hard. Those machines have network-mounted drives. Which <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html">https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html</a> do you use? Is it possible you hit a IOPs burst limit? Any AWS Cloudwatch metrics that would show drive throughput or IOPs used? I've seen the postgresql server die and missing network connection (if installed on a separate server) but those have different log lines in the postgresql log.</p>
<p>Apart from trying again, or again with higher spec drives, I suggest using the flatnode file. Maybe you already do, the output posted here is to short to tell. It's explained on <a href="https://nominatim.org/release-docs/latest/admin/Import-and-Update/">https://nominatim.org/release-docs/latest/admin/Import-and-Update/</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Mar '19, 01:10</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-68222" class="comments-container">
<span id="68223"></span>
<div id="comment-68223" class="comment">
<div id="post-68223-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for taking the time to help me out. I am using a general purpose SSD that has a performance of 3000 IOPS and about all of it is used during the db import.</p>
<p>Does using the flatnode file mean a hit to performance? I am mostly interested in the reverse geocode lookup.</p>
<p>Edit: I'm currently trying both just running it again as well as using flatnode and will look at how both servers fared tomorrow.</p>
</div>
<div id="comment-68223-info" class="comment-info">
<span class="comment-age">(03 Mar '19, 01:34)</span> <span class="comment-user userinfo">Greenish Purple</span>
</div>
</div>
<span id="68227"></span>
<div id="comment-68227" class="comment">
<div id="post-68227-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Both setups failed quite early this time, using a flatnodes file made no difference. I added my full installation script to the question, maybe there is an error in there I don't see.</p>
</div>
<div id="comment-68227-info" class="comment-info">
<span class="comment-age">(03 Mar '19, 08:51)</span> <span class="comment-user userinfo">Greenish Purple</span>
</div>
</div>
<span id="68230"></span>
<div id="comment-68230" class="comment">
<div id="post-68230-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I found something in the osm2pgsql issue list <a href="https://github.com/openstreetmap/osm2pgsql/issues/159">https://github.com/openstreetmap/osm2pgsql/issues/159</a> which points to database looses connection and a user reports more RAM helped. Here <a href="https://github.com/openstreetmap/osm2pgsql/issues/855">https://github.com/openstreetmap/osm2pgsql/issues/855</a> connecting to the database via unix socket instead of port was recommended. Lastly just today another user reported the same issue just hours ago <a href="https://github.com/openstreetmap/Nominatim/issues/1320">https://github.com/openstreetmap/Nominatim/issues/1320</a></p>
</div>
<div id="comment-68230-info" class="comment-info">
<span class="comment-age">(03 Mar '19, 12:37)</span> <span class="comment-user userinfo">mtmail</span>
</div>
</div>
<span id="68231"></span>
<div id="comment-68231" class="comment">
<div id="post-68231-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Okay, I am going to modify the setup script to omit the port, which should mean that the connection is established via socket instead. I will also spin up an even bigger server with 192GB memory and try that with the unmodified setup script.</p>
<p>Thank you for spending the time to dig out possible solutions :)</p>
</div>
<div id="comment-68231-info" class="comment-info">
<span class="comment-age">(03 Mar '19, 14:37)</span> <span class="comment-user userinfo">Greenish Purple</span>
</div>
</div>
<span id="68233"></span>
<div id="comment-68233" class="comment">
<div id="post-68233-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Result: both 32GB memory + 32GB swapfile with socket connection to postgres and the 192GB memory server failed with the same error message as above, logfiles also look the same :(</p>
<p>Are there any logs I can dig through to maybe get a better error message besides the postgres log?</p>
</div>
<div id="comment-68233-info" class="comment-info">
<span class="comment-age">(03 Mar '19, 16:59)</span> <span class="comment-user userinfo">Greenish Purple</span>
</div>
</div>
</div>
<div id="comment-tools-68222" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68222-form-container" class="comment-form-container">
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

