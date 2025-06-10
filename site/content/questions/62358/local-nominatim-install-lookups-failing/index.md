+++
type = "question"
title = "Local Nominatim install lookups failing"
description = '''This is my second shot at posting - first went away when I validated my email. I&#x27;m trying to get a local instance of nominatim 3.1.0 running on FreeBSD 11.1 and PG 9.5. I followed the instructions published here: https://nominatim.org/release-docs/latest/admin/Installation/. I did not encounter any ...'''
date = "2018-02-24T09:16:00Z"
lastmod = "2018-03-02T19:53:00Z"
weight = 62358
keywords = [ "nominatim", "local" ]
aliases = [ "/questions/62358" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Local Nominatim install lookups failing](/questions/62358/local-nominatim-install-lookups-failing)

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
<span id="post-62358-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62358-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-62358-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>This is my second shot at posting - first went away when I validated my email.</p>
<p>I'm trying to get a local instance of nominatim 3.1.0 running on FreeBSD 11.1 and PG 9.5. I followed the instructions published here: <a href="https://nominatim.org/release-docs/latest/admin/Installation/.">https://nominatim.org/release-docs/latest/admin/Installation/.</a> I did not encounter any errors during the install and the apache/php side of things seems to be working nicely. I installed no additional components (no TIGER, wikipedia, etc.). I installed New Jersey from here: <a href="http://download.geofabrik.de/north-america.html">http://download.geofabrik.de/north-america.html</a></p>
<p>However I can only query by zipcode. Entering a street name, city, town or place name gives no results. Zipcodes return a result, but clicking on the "details" link gives me an error. This example is zip "07960" and the URL that produces the below error is <a href="http://myinstall/details.php?place_id=430312">http://myinstall/details.php?place_id=430312</a></p>
<pre><code>Bad Request 
Nominatim has encountered an error with your request. Details:
Unknown place id.</code></pre>
<p>Poking around in the database, some seemingly important tables are empty:</p>
<pre><code>nominatim=# select count(*) from location_area;
 count
-------
     0
(1 row)
&#10;nominatim=# select count(*) from search_name;
 count
-------
     0
(1 row)</code></pre>
<p>Places seem populated:</p>
<pre><code>nominatim=# select count(*) from place;
 count
--------
 329248
(1 row)
&#10;nominatim=# select count(*) from placex;
 count
--------
 325948
(1 row)</code></pre>
<p>I'm stumped. I went through the install a second time to make sure I was doing things correctly and to gather logs of the whole process. The gist below contains the cmake output, (g)make output, setup.php output and the pgsql log. Nothing stands out as an error in the setup log, but this is my first try at anything GIS-related so I have no idea what I'm looking at.</p>
<p><a href="https://gist.github.com/sporkman/969be026d7048eda54d1060312f8fedb">https://gist.github.com/sporkman/969be026d7048eda54d1060312f8fedb</a></p>
<p>Any ideas? The empty tables seem like a big hint, not sure what populates them though.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-local" rel="tag" title="see questions tagged &#39;local&#39;">local</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Feb '18, 09:16</strong></p>
<img src="https://secure.gravatar.com/avatar/8d055a5c91585c6899a51494d0b6c8e4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="spork123&#39;s gravatar image" />
<p><span>spork123</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="spork123 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-62358" class="comments-container">
<span id="62366"></span>
<div id="comment-62366" class="comment">
<div id="post-62366-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Could you please add the contents of your local settings file(build/settings/local.php)?</p>
</div>
<div id="comment-62366-info" class="comment-info">
<span class="comment-age">(24 Feb '18, 12:03)</span> <span class="comment-user userinfo">lonvia</span>
</div>
</div>
<span id="62369"></span>
<div id="comment-62369" class="comment">
<div id="post-62369-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, both installation and output of the setup.php look fine. And placex being filled is a good sign. The 'Create Search indices' step taking only 3 second could be suspicious. Best next good step is to try the installation with a small full country, e.g. Luxembourg or Monaco, so we can rule out the input file new-jersey causes this.</p>
</div>
<div id="comment-62369-info" class="comment-info">
<span class="comment-age">(24 Feb '18, 13:35)</span> <span class="comment-user userinfo">mtmail</span>
</div>
</div>
<span id="62374"></span>
<div id="comment-62374" class="comment">
<div id="post-62374-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>OK, here's more info... local overrides are minimal:</p>
<pre><code>[spork@nominatim /home/nominatim/Nominatim-3.1.0]$ cat build/settings/local.php
&lt;?php
&#10; @define(&#39;CONST_Database_Web_User&#39;, &#39;www&#39;);
 @define(&#39;CONST_Website_BaseURL&#39;, &#39;/&#39;);
&#10;?&gt;</code></pre>
<p>Also php version just in case there's an issue there:</p>
<pre><code>[nominatim@nominatim /usr/home/nominatim/Nominatim-3.1.0]$ php -v
PHP 5.6.32 (cli) (built: Jan  2 2018 01:29:52)
Copyright (c) 1997-2016 The PHP Group
Zend Engine v2.6.0, Copyright (c) 1998-2016 Zend Technologies</code></pre>
<p>Postgresql/related Versions:</p>
<pre><code>postgis24-2.4.2                Geographic objects support for PostgreSQL databases
postgresql95-client-9.5.10     PostgreSQL database (client)
postgresql95-contrib-9.5.10    The contrib utilities from the PostgreSQL distribution
postgresql95-server-9.5.10     PostgreSQL is the most advanced open-source database available anywhere</code></pre>
<p>Also, for reference, the entire nominatim source and build directories are owned by a "nominatim" user, and this user was also used to perform all database operations. I manually "dropdb nominatim" between tests.</p>
<p>I grabbed Luxembourg and verified the checksum is OK:</p>
<pre><code>[nominatim@nominatim /usr/home/nominatim/Nominatim-3.1.0]$ fetch http://download.geofabrik.de/europe/luxembourg-latest.osm.pbf
luxembourg-latest.osm.pbf                     100% of   22 MB  728 kBps 00m32s
[nominatim@nominatim /usr/home/nominatim/Nominatim-3.1.0]$ md5 luxembourg-latest.osm.pbf
MD5 (luxembourg-latest.osm.pbf) = 4042514b653f6732342ae4bc0a4763ad</code></pre>
<p>I searched for a number of towns listed here (<a href="https://en.wikipedia.org/wiki/List_of_towns_in_Luxembourg)">https://en.wikipedia.org/wiki/List_of_towns_in_Luxembourg)</a> and came up with no results. I searched on a postcode and after trying a few got a hit on "8070". And like the New Jersey data, the details link lead to the same error (partial URL: details.php?place_id=210598). Like NJ, "location_area" is empty, "place" and "placex" are populated. Not sure what other tables are important. Of note, a dump of this db, uncompressed is about 304MB. There's something in there. :)</p>
<p>I'm attaching the debug output for the successful and unsuccessful searches as screenshots. The setup.php log is here: <a href="https://gist.github.com/sporkman/6829ef07576678c884119bb2ee4f3c01">https://gist.github.com/sporkman/6829ef07576678c884119bb2ee4f3c01</a></p>
<p>Scanning the log, things that look weird to me:</p>
<ul>
<li>Line 11 NOTICE: table "place" does not exist, skipping (very early in the process)</li>
<li>As you noted, lots of things are taking just seconds to complete. That said this is a VM with SSD storage and lots of CPU.</li>
<li>Lines 55-80 note that a function and a bunch of tables don't exist, but I assume they get created</li>
<li>All the "indexing ranks" lines state that nothing was done ("Done 0 in 0 @ 0.000000 per second - FINISHED") - this "Done 0" repeats on lines 109-214, so whatever that indexing is supposed to be doing, it doesn't seem to be actually doing any work</li>
<li>Is there a way to get verbose output on what queries are being run here?</li>
</ul>
</div>
<div id="comment-62374-info" class="comment-info">
<span class="comment-age">(24 Feb '18, 20:04)</span> <span class="comment-user userinfo">spork123</span>
</div>
</div>
<span id="62375"></span>
<div id="comment-62375" class="comment">
<div id="post-62375-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>ps - sorry for "answering", this is too big for a comment and there's no formatting in comments.</p>
</div>
<div id="comment-62375-info" class="comment-info">
<span class="comment-age">(24 Feb '18, 20:05)</span> <span class="comment-user userinfo">spork123</span>
</div>
</div>
<span id="62377"></span>
<div id="comment-62377" class="comment not_top_scorer">
<div id="post-62377-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>300MB is still reasonable. The country_grid.sql.gz is already 100MB uncompressed and imported for partitioning data regardless. The "NOTICE: table "place" does not exist, skipping" are fine, postgresql doesn't have a silent "create this table if it doesnt exist yet" afaik so this goes to the output. Have you applied any of the <a href="http://www.nominatim.org/release-docs/latest/admin/Installation/#postgresql-tuning">http://www.nominatim.org/release-docs/latest/admin/Installation/#postgresql-tuning</a> changes? For such a small import tuning makes no difference, I'm just wondering if there were any Postgresql config changes. Lastly can we rule out the harddrive is full (though usually Postgresql will print an error). I think it's the first time we see this kind of error, or rather lack of error message while looping through 0 places.</p>
</div>
<div id="comment-62377-info" class="comment-info">
<span class="comment-age">(24 Feb '18, 21:22)</span> <span class="comment-user userinfo">mtmail</span>
</div>
</div>
<span id="62378"></span>
<div id="comment-62378" class="comment not_top_scorer">
<div id="post-62378-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>meta <a href="https://help.openstreetmap.org/users/14796/spork123">@spork123</a>: there is formatting in comments - just no preview. You can use the preview of the answer or use <a href="https://daringfireball.net/projects/markdown/dingus">https://daringfireball.net/projects/markdown/dingus</a> for previewing which is more accurate anyway. (note: I have converted your "answer" to a "comment".)</p>
</div>
<div id="comment-62378-info" class="comment-info">
<span class="comment-age">(24 Feb '18, 22:18)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="62380"></span>
<div id="comment-62380" class="comment not_top_scorer">
<div id="post-62380-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I think I lost a reply, but the short version just that drive space is fine.</p>
<p>PG changes: shared_buffers = 1500MB, work_mem = 50MB, maintenance_work_mem = 512MB, synchronous_commit = off (for import), checkpoint_timeout = 10min, checkpoint_completion_target = 0.9 and the rest is stock.</p>
<p>PHP modules/PEAR: json, openssl, pgsql, xml, zlib and pear-1.10.5, pear-DB-1.9.2</p>
<p>I've been stepping through setup.php to see what it does, and now I see that the indexing step is handled by an executable: build/nominatim/nominatim - I'm going to assume that's where the issue is. Any thoughts on debugging that? It's not doing an instant segfault or anything, so that's good. But does it make any interesting assumptions about what OS it's running on?</p>
</div>
<div id="comment-62380-info" class="comment-info">
<span class="comment-age">(24 Feb '18, 23:24)</span> <span class="comment-user userinfo">spork123</span>
</div>
</div>
<span id="62381"></span>
<div id="comment-62381" class="comment not_top_scorer">
<div id="post-62381-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>btw, thanks <a href="https://help.openstreetmap.org/users/5179/aseerel4c26"></a><a href="https://help.openstreetmap.org/users/5179/aseerel4c26">@aseerel4c26</a>, I had no idea.</p>
<p>So this indexer. Either it's silently failing or it's not seeing whatever input data it wants. Can anyone elaborate on what it's looking for so I can verify the input data exists?</p>
<p>Manual run:</p>
<pre><code>[nominatim@nominatim /usr/home/nominatim/Nominatim-3.1.0/build]$ nominatim/nominatim -i -d nominatim -P 5432 -t  1 -R 4
nominatim version 3.1.0
&#10;Starting indexing rank (0 to 4) using 1 threads
Starting rank 0
  Done 0 in 0 @ 0.000000 per second - FINISHED
&#10;Starting rank 1
  Done 0 in 0 @ 0.000000 per second - FINISHED
(etc.)</code></pre>
</div>
<div id="comment-62381-info" class="comment-info">
<span class="comment-age">(24 Feb '18, 23:38)</span> <span class="comment-user userinfo">spork123</span>
</div>
</div>
<span id="62383"></span>
<div id="comment-62383" class="comment not_top_scorer">
<div id="post-62383-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Even more data. Installed using the same process on Ubuntu 16.04 LTS. Same dataset and all, biggest difference was that I saw the index process actually generate quite a bit of output. And it worked as well.</p>
<p>Experiments to narrow this down to the index process that calls the "nominatim" binary:</p>
<ul>
<li>Copy "broken"/not properly indexed database dump to working ubuntu server, load it up, use "setup.php --create-functions" to create missing functions and note that the previously working Ubuntu setup stopped working with the same results as the FreeBSD install I've been working on</li>
<li>Manually run "setup.php --index" on this "broken" data on the Ubuntu server, and after that process completes, everything is working normally again</li>
<li>Dump this "good" database, copy it to FreeBSD server. As above, manually create functions. This install now works normally.</li>
</ul>
<p>What does this show? Given a properly indexed db, the FreeBSD version works, which means the frontend is OK, osm2pgsql works, the nominatim.so module for PG works. It also shows that the data the indexer needs to function is present (proven when copying "bad" db to ubuntu and indexing it). So something is up with the indexer, no?</p>
</div>
<div id="comment-62383-info" class="comment-info">
<span class="comment-age">(25 Feb '18, 05:45)</span> <span class="comment-user userinfo">spork123</span>
</div>
</div>
<span id="62480"></span>
<div id="comment-62480" class="comment not_top_scorer">
<div id="post-62480-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hey all, is this better handled in a github ticket?</p>
</div>
<div id="comment-62480-info" class="comment-info">
<span class="comment-age">(28 Feb '18, 01:00)</span> <span class="comment-user userinfo">spork123</span>
</div>
</div>
<span id="62492"></span>
<div id="comment-62492" class="comment">
<div id="post-62492-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>This looks like a compatibility bug in nominatim.index,c and will require some debugging on your side. Please open a new bug on github.</p>
</div>
<div id="comment-62492-info" class="comment-info">
<span class="comment-age">(02 Mar '18, 09:38)</span> <span class="comment-user userinfo">lonvia</span>
</div>
</div>
<span id="62499"></span>
<div id="comment-62499" class="comment not_top_scorer">
<div id="post-62499-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/14796/spork123">@spork123</a>: please link the issue here once you have created it.</p>
</div>
<div id="comment-62499-info" class="comment-info">
<span class="comment-age">(02 Mar '18, 19:53)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-62358" class="comment-tools">
<span class="comments-showing"> showing 5 of 12 </span> <a href="#" class="show-all-comments-link">show 7 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-62358-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

