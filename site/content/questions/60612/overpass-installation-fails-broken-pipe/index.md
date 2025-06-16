+++
type = "question"
title = "Overpass Installation fails: broken pipe"
description = '''Hello, I would like to setup a small private OSM Server in the cloud for testing an application. To achieve this, I&#x27;ve launched an AWS EC2 t2.micro instance and followed the installation steps from the Official OSM Install Guide. In general the installation worked fine, at least for very small count...'''
date = "2017-11-14T13:13:00Z"
lastmod = "2017-11-16T10:04:00Z"
weight = 60612
keywords = [ "overpass", "fails", "aws", "installation", "broken-pipe" ]
aliases = [ "/questions/60612" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Overpass Installation fails: broken pipe](/questions/60612/overpass-installation-fails-broken-pipe)

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
<span id="post-60612-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60612-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-60612-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I would like to setup a small private OSM Server in the cloud for testing an application. To achieve this, I've launched an AWS EC2 t2.micro instance and followed the installation steps from the <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Installation">Official OSM Install Guide</a>.</p>
<p>In general the installation worked fine, at least for very small countries. I've successfully installed Andorra (<a href="http://download.geofabrik.de/europe/andorra-latest.osm.bz2">Geofabrik-Link</a>) and Faroe Islands (<a href="http://download.geofabrik.de/europe/faroe-islands-latest.osm.bz2">Geofabrik-Link</a>) and was able to run queries on the instance.</p>
<p>When trying to do same with a little bit larger country, in this case Austria (<a href="http://download.geofabrik.de/europe/austria-latest.osm.bz2">Geofabrik-Link</a>), i receive a "<strong>broken pipe</strong>" error:</p>
<blockquote>
<p>Reading XML file ...terminate called after throwing an instance of 'std::bad_alloc' what(): std::bad_alloc src/bin/init_osm3s.sh: line 44: 29086 Broken pipe bunzip2 &lt; $PLANET_FILE 29087 Aborted (core dumped) | $EXEC_DIR/bin/update_database --db-dir=$DB_DIR/ $META $COMPRESSION</p>
</blockquote>
<p>Can someone help me to get this fixed?</p>
<p>The resources of my EC2 instance currently are the following: - Ubuntu Server 16.04 LTS (HVM) - 1 GB RAM - ~25-30GB of free disk space (using AWS EBS)</p>
<p>My simple guess is that the resources are too low, especially the Memory of 1GB. Before I upgrade to more resources (I want to avoid costs as much as possible) and test again, I would like to how likely this would fix my problem? Also, can anybody tell me how much RAM and Disk Space I approximately need for a ~900MB OSM-file like Austria?</p>
<p><strong>Update 1:</strong> In the meantime I've upgraded my machine and now have the following resources:</p>
<ul>
<li>Ubuntu 16.04 LTS</li>
<li>2vCPUs</li>
<li>7.5 GB RAM</li>
<li>~50 GB of free SSD disk space</li>
</ul>
<p>I tried to run the Austria Import again. Unfortunately it failed again (shortly after starting the import) with a slightly different error:</p>
<blockquote>
<p>Reading XML file ... elapsed node 1559520430. ./exec/bin/init_osm3s.sh: line 44: 18530 Broken pipe $ 18531 Killed | $EXEC_DIR/bin/update_database --db-dir=$DB_DIR/ $META $COMPRESSION</p>
</blockquote>
<p>Again, I was able to import the very small country export Faroe-Island. I also tried importing a "medium" large country in terms of file size: Belgium. Running the import with Belgium showed no errors. (I manually canceled the import after around 5-10mins).</p>
<p>Is 7.5GB RAM still not enough? Or can it be another problem?</p>
<p><strong>Update 2:</strong> Now I also tested importing a larger country, Czech Republic with a file size of ~1.1GB. Interestingly, the import again seemed to run without problems and I saw the import progress without any errors (i.e. many lines with "Reading XM L file...elapsed node xxxx. Flushing to databse ... done.) I cancelled after around 10min.</p>
<p>To summarize my import approaches:</p>
<ul>
<li>country | filesize | status</li>
<li>austria | ~900MB | failed (both on 1GB RAM and 7.5GB RAM)</li>
<li>faroe | ~3MB | worked (both)</li>
<li>belgium | ~500MB | worked (on 7.5GB RAM)</li>
<li>czechrep | ~1.1GB | worked (on 7.5GB RAM)</li>
</ul>
<p>I can only guess, but since importing all countries (even larger one's) except for Austria seemed to work, I suspect there might be something wrong with the export hosted at Geofabrik? Anyone had similar problems before? Someone knows another server that hosts country files, or is there a way how I can find out if the file is "OK"?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-fails" rel="tag" title="see questions tagged &#39;fails&#39;">fails</span> <span class="post-tag tag-link-aws" rel="tag" title="see questions tagged &#39;aws&#39;">aws</span> <span class="post-tag tag-link-installation" rel="tag" title="see questions tagged &#39;installation&#39;">installation</span> <span class="post-tag tag-link-broken-pipe" rel="tag" title="see questions tagged &#39;broken-pipe&#39;">broken-pipe</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Nov '17, 13:13</strong></p>
<img src="https://secure.gravatar.com/avatar/b2429b48885174828e926ec537ce8f41?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hiasel&#39;s gravatar image" />
<p><span>hiasel</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hiasel has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Nov '17, 10:21</strong> </span></p>
</div>
</div>
<div id="comments-container-60612" class="comments-container">
<span id="60613"></span>
<div id="comment-60613" class="comment">
<div id="post-60613-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>1 GB RAM sounds pretty low. Check <code>dmesg</code> for out of memory (OOM) messages.</p>
</div>
<div id="comment-60613-info" class="comment-info">
<span class="comment-age">(14 Nov '17, 13:18)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="60614"></span>
<div id="comment-60614" class="comment">
<div id="post-60614-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for quick response. Could you help me how exactly i shall use the dmesg command? I've just executed it and simply searched for "OOM", but can't find anything. Or shall I run this command (in parallel) while I do the database import?</p>
</div>
<div id="comment-60614-info" class="comment-info">
<span class="comment-age">(14 Nov '17, 13:24)</span> <span class="comment-user userinfo">hiasel</span>
</div>
</div>
<span id="60615"></span>
<div id="comment-60615" class="comment not_top_scorer">
<div id="post-60615-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Run it afterwards: <code>dmesg | grep -i "out of memory"</code>. If there is no output then too few memory is not your issue.</p>
</div>
<div id="comment-60615-info" class="comment-info">
<span class="comment-age">(14 Nov '17, 13:43)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="60617"></span>
<div id="comment-60617" class="comment not_top_scorer">
<div id="post-60617-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>hm. just executed dmesg | grep -i "out of memory" right after calling init_osm3s.sh and there is indeed no output. The error remains. The full error message btw. starts with "Reading XML file ...terminate called after throwing an instance of 'std::bad_alloc' what(): std::bad_alloc" (i've updated that in the question).</p>
</div>
<div id="comment-60617-info" class="comment-info">
<span class="comment-age">(14 Nov '17, 14:31)</span> <span class="comment-user userinfo">hiasel</span>
</div>
</div>
<span id="60618"></span>
<div id="comment-60618" class="comment">
<div id="post-60618-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><code>std::bad_alloc</code> definitely sounds like having too few memory. The program doesn't get killed by the kernel but terminates itself since it can't allocate enough memory. Get more RAM or try a smaller map extract.</p>
</div>
<div id="comment-60618-info" class="comment-info">
<span class="comment-age">(14 Nov '17, 15:32)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="60619"></span>
<div id="comment-60619" class="comment not_top_scorer">
<div id="post-60619-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>allright, then I will upgrade my machine and post the result as soon as I got it running. Thanks a lot already for your help :)</p>
</div>
<div id="comment-60619-info" class="comment-info">
<span class="comment-age">(14 Nov '17, 15:36)</span> <span class="comment-user userinfo">hiasel</span>
</div>
</div>
<span id="60628"></span>
<div id="comment-60628" class="comment not_top_scorer">
<div id="post-60628-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I just tried running the import again with an upgrade machine (See my updated question). Still no success. I wonder if 7.5GB is still not enough? According to the Install Guide "1 GB of RAM and sufficient swap space for a small extract or a development system." To me, austria still seems like a "small" extract compared to others, so I thought with ~8GB i'm on the safe side. Is it possible that there is something wrong with the file-extract of austria at geofabrik? (I've downloaded a fresh copy each time i tried running the import, so it shouldnt be my fault)</p>
</div>
<div id="comment-60628-info" class="comment-info">
<span class="comment-age">(15 Nov '17, 09:39)</span> <span class="comment-user userinfo">hiasel</span>
</div>
</div>
<span id="60629"></span>
<div id="comment-60629" class="comment">
<div id="post-60629-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You could try one of the <a href="https://wiki.openstreetmap.org/wiki/Planet.osm#Country_and_area_extracts">other extracts</a>.</p>
</div>
<div id="comment-60629-info" class="comment-info">
<span class="comment-age">(15 Nov '17, 10:29)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="60642"></span>
<div id="comment-60642" class="comment">
<div id="post-60642-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks for pointing me to the list of extracts. In the end I used a custom extract from: <a href="http://extract.bbbike.org/.">http://extract.bbbike.org/.</a> For my project I only need a part of Austria, i.e. my custom extract file size now is only ~150MB. Importing this custom extract worked without problems and I can perform queries on my cloud instance :)</p>
</div>
<div id="comment-60642-info" class="comment-info">
<span class="comment-age">(16 Nov '17, 10:04)</span> <span class="comment-user userinfo">hiasel</span>
</div>
</div>
</div>
<div id="comment-tools-60612" class="comment-tools">
<span class="comments-showing"> showing 5 of 9 </span> <a href="#" class="show-all-comments-link">show 4 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-60612-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

