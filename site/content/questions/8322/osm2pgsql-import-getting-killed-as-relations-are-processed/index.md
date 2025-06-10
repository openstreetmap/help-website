+++
type = "question"
title = "osm2pgsql import getting killed as relations are processed"
description = '''Whenever I try to import the planet.osm.bz2 or california.osm.bz2, I get this: bash-4.2$ ./osm2pgsql -S ./default.style ../california.osm osm2pgsql SVN version 0.80.0 (32bit id space) Using projection SRS 900913 (Spherical Mercator) Setting up table: planet_osm_point NOTICE: table &quot;planet_osm_point_...'''
date = "2011-10-05T18:08:00Z"
lastmod = "2015-08-28T17:50:00Z"
weight = 8322
keywords = [ "import", "osm2pgsql" ]
aliases = [ "/questions/8322" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [osm2pgsql import getting killed as relations are processed](/questions/8322/osm2pgsql-import-getting-killed-as-relations-are-processed)

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
<span id="post-8322-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8322-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-8322-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Whenever I try to import the <strong>planet.osm.bz2</strong> or <strong>california.osm.bz2</strong>, I get this:</p>
<p>bash-4.2$ ./osm2pgsql -S ./default.style ../california.osm<br />
osm2pgsql SVN version 0.80.0 (32bit id space)</p>
<p>Using projection SRS 900913 (Spherical Mercator)<br />
Setting up table: planet_osm_point<br />
NOTICE: table "planet_osm_point_tmp" does not exist, skipping<br />
Setting up table: planet_osm_line<br />
NOTICE: table "planet_osm_line_tmp" does not exist, skipping<br />
Setting up table: planet_osm_polygon<br />
NOTICE: table "planet_osm_polygon_tmp" does not exist, skipping<br />
Setting up table: planet_osm_roads<br />
NOTICE: table "planet_osm_roads_tmp" does not exist, skipping<br />
Mid: Ram, scale=100</p>
<p>Reading in file: ../california.osm<br />
Processing: Node(41300k 56.5k/s) Way(0k 0.00k/s) Relation(0 0.00/s)Killed</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Oct '11, 18:08</strong></p>
<img src="https://secure.gravatar.com/avatar/48980c72ff56a285d3689c40bc272e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NDFobia1158&#39;s gravatar image" />
<p><span>NDFobia1158</span><br />
<span class="score" title="61 reputation points">61</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NDFobia1158 has no accepted answers">0%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Oct '12, 10:40</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></br></p>
</div>
</div>
<div id="comments-container-8322" class="comments-container">
&#10;</div>
<div id="comment-tools-8322" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8322-form-container" class="comment-form-container">
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

<span id="8323"></span>

<div id="answer-container-8323" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8323-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8323-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-8323-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="NDFobia1158 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I would guess this is the "out of memory killer" shooting your process; type <code>dmesg</code> after the incident to see the latest system messages that would corrobate this. I am surprised that you should run out of memory on a file as small as the California one but maybe other processes are eating memory too? Try the <code>--slim</code> option on osm2pgsql which will slow down things but use less memory.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Oct '11, 18:20</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span> </br></br></p>
</div>
</div>
<div id="comments-container-8323" class="comments-container">
<span id="16795"></span>
<div id="comment-16795" class="comment">
<div id="post-16795-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I run into the same error by using the --slim option. There are any other solutions?</p>
</div>
<div id="comment-16795-info" class="comment-info">
<span class="comment-age">(10 Oct '12, 09:25)</span> <span class="comment-user userinfo">marco-2012</span>
</div>
</div>
<span id="16796"></span>
<div id="comment-16796" class="comment">
<div id="post-16796-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Have you looked at the switch2osm.org site? While for smaller extracts you can use quite a small machine, you should take the systems requirements for a full planet import seriously.</p>
</div>
<div id="comment-16796-info" class="comment-info">
<span class="comment-age">(10 Oct '12, 09:41)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="16797"></span>
<div id="comment-16797" class="comment">
<div id="post-16797-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, I used switch2osm.org/serving-tiles/manually-building-a-tile-server-12-04/ to set up a tile server on a virtual machine. I can import download.geofabrik.de/openstreetmap/europe/germany/hamburg.osm.pbf successfully and everything works fine. But if I try to import download.geofabrik.de/openstreetmap/europe/germany.osm.pbf I get the "out of memory killer". The virtual machine has 1 GB RAM. Is it to small?</p>
</div>
<div id="comment-16797-info" class="comment-info">
<span class="comment-age">(10 Oct '12, 09:57)</span> <span class="comment-user userinfo">marco-2012</span>
</div>
</div>
<span id="16798"></span>
<div id="comment-16798" class="comment">
<div id="post-16798-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I suspect yes, Germany is something over 5% of all data. Very roughly I would suspect that you need at least 1GB just for the import process.</p>
</div>
<div id="comment-16798-info" class="comment-info">
<span class="comment-age">(10 Oct '12, 10:13)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="16800"></span>
<div id="comment-16800" class="comment not_top_scorer">
<div id="post-16800-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Just another data point / anecdote - I struggled to load england (1/6 the size of germany) on a VM allocated 2Gb without fiddling with settings, so I'd have thought that 1Gb was too small.</p>
<p>If buying more memory isn't an option, perhaps experiment with VM memory settings - monitor what's being used, try larger or smaller -C values, and try either swap within the VM or a larger memory usage (relying on swap on the host) to see what works best.</p>
</div>
<div id="comment-16800-info" class="comment-info">
<span class="comment-age">(10 Oct '12, 10:39)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="16808"></span>
<div id="comment-16808" class="comment">
<div id="post-16808-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I increased the RAM to 2 GB and tried to increase and decrease the -C value, but I still got an error (not sure what, but no out of memory error). After I leaved the -C value (I don't know what the default -C value is) it works without any errors. Thanks for your help.</p>
</div>
<div id="comment-16808-info" class="comment-info">
<span class="comment-age">(10 Oct '12, 13:49)</span> <span class="comment-user userinfo">marco-2012</span>
</div>
</div>
</div>
<div id="comment-tools-8323" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-8323-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="44954"></span>

<div id="answer-container-44954" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-44954-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44954-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-44954-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I had the same problem with canada-latest.pbf. (2gb file size) Using ksysguard I watched the osm2pgsql process consume first memory (4gb) and then swap (4gb) until all was gone and the process killed. To fix: su dd if=/dev/zero of=/home/RB/temp/extraswap bs=1M count=16384 add 16gb swap file mkswap /home/RB/temp/extraswap swapon /home/RB/temp/extraswap swapon -s and see added swap</p>
<p>The pgsql data file was in /usr/share in the root directory (50gb). That was overdosed also so I moved /usr/share/pgsql to /home/RB/proj/Maps where mucho disk space is available. Good to go after that.</p>
<p>The 2gb canada-latest required nearly 14gb of memory to process so there is a memory leak or poor architecture someplace in the osm2pgsql program -Rick Brown in Reno, NV</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Aug '15, 17:44</strong></p>
<img src="https://secure.gravatar.com/avatar/a9c1024e705bd06284f4555b0593db23?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RickBrown&#39;s gravatar image" />
<p><span>RickBrown</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RickBrown has no accepted answers">0%</span> </br></br></p>
</div>
</div>
<div id="comments-container-44954" class="comments-container">
<span id="44955"></span>
<div id="comment-44955" class="comment">
<div id="post-44955-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The github for osm2pgsql is here:</p>
<p><a href="https://github.com/openstreetmap/osm2pgsql/issues">https://github.com/openstreetmap/osm2pgsql/issues</a></p>
<p>I'd suggest explaining the problem there, and include details of the full command line and version that you used (since what osm2pgsql does depends very much on what you ask it to do - whether you ask it to create an updatable database, for example).</p>
<p>If you can identify a "memory leak or poor architecture" in the code (or even better, suggest a fix) I'd describe that too.</p>
</div>
<div id="comment-44955-info" class="comment-info">
<span class="comment-age">(28 Aug '15, 17:50)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-44954" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44954-form-container" class="comment-form-container">
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

