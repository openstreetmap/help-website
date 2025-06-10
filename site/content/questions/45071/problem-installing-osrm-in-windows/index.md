+++
type = "question"
title = "Problem installing OSRM in Windows"
description = '''Hi, I have downloaded windows build from http://build.project-osrm.org/. The release folder looks like below 05/09/2015 01:33 &amp;lt;DIR&amp;gt; . 05/09/2015 01:33 &amp;lt;DIR&amp;gt; .. 04/09/2015 13:42 35 .stxxl.txt 04/09/2015 13:39 825,856 algorithm-tests.exe 04/09/2015 13:26 14,011 bicycle.lua 04/09/2015 13:26...'''
date = "2015-09-05T10:29:00Z"
lastmod = "2015-09-07T01:24:00Z"
weight = 45071
keywords = [ "windows", "osrm", "installation" ]
aliases = [ "/questions/45071" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Problem installing OSRM in Windows](/questions/45071/problem-installing-osrm-in-windows)

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
<span id="post-45071-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45071-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-45071-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I have downloaded windows build from <a href="http://build.project-osrm.org/.">http://build.project-osrm.org/.</a> The release folder looks like below</p>
<pre><code>05/09/2015  01:33    &lt;DIR&gt;          .
05/09/2015  01:33    &lt;DIR&gt;          ..
04/09/2015  13:42                35 .stxxl.txt
04/09/2015  13:39           825,856 algorithm-tests.exe
04/09/2015  13:26            14,011 bicycle.lua
04/09/2015  13:26            13,458 car.lua
04/09/2015  13:37           944,128 datastructure-tests.exe
05/09/2015  01:25       633,726,109 england-latest.osm.pbf
04/09/2015  13:26    &lt;DIR&gt;          examples
04/09/2015  13:26             6,969 foot.lua
04/09/2015  13:26    &lt;DIR&gt;          lib
27/08/2015  16:45           487,936 libexpat.dll
27/08/2015  16:45           242,176 lua.dll
04/09/2015  13:36           471,040 osrm-datastore.exe
04/09/2015  13:41         1,795,584 osrm-extract.exe
04/09/2015  13:37           888,832 osrm-prepare.exe
04/09/2015  13:42         1,238,016 osrm-routed.exe
05/09/2015  01:32            53,502 profile.lua
04/09/2015  13:26             1,290 rasterbot-interp.lua
04/09/2015  13:26             1,278 rasterbot.lua
04/09/2015  13:32           126,464 rtree-bench.exe
05/09/2015  01:33                 0 stxxl.errlog
05/09/2015  01:33               233 stxxl.log
27/08/2015  16:49           188,928 tbb.dll
27/08/2015  16:49            89,088 tbbmalloc.dll
27/08/2015  16:49            31,232 tbbmalloc_proxy.dll
04/09/2015  13:26             3,442 testbot.lua
04/09/2015  13:26               167 turnbot.lua</code></pre>
<p>profile.lua was not there. I manually downloaded and copied it there. When I run osrm-extract, there is no error but nothing happens</p>
<pre><code>\osrm_Release&gt;osrm-extract england-latest.osm.pbf
[info] Input file: england-latest.osm.pbf[0m
[info] Profile: profile.lua[0m
[info] Threads: 4[0m
[info] Using script profile.lua[0m
[STXXL-MSG] STXXL v1.4.99 (prerelease/Release) (git f7389c79e946430f5e3f7efc15e5bcc29183d200) 
+ gnu     parallel(__GLIBCXX__)
[STXXL-MSG] Disk &#39;c:\temp\stxxl&#39; is allocated, space: 10000 MiB, I/O implementation: wincall 
queue=0    devid=0
[info] Parsing in progress..[0m</code></pre>
<p>I left it for a day. The temp folder looks like</p>
<pre><code>Directory of C:\temp
&#10;05/09/2015  01:33    &lt;DIR&gt;          .
05/09/2015  01:33    &lt;DIR&gt;          ..
03/04/2015  23:37    &lt;DIR&gt;          nwb
04/04/2015  00:22       660,036,518 nwb.routing.flatfile
05/09/2015  01:33    10,485,760,000 stxxl
           2 File(s) 11,145,796,518 bytes
           3 Dir(s)  89,474,977,792 bytes free
&#10;Directory of C:\temp\nwb
&#10;03/04/2015  23:37    &lt;DIR&gt;          .
03/04/2015  23:37    &lt;DIR&gt;          ..
03/04/2015  09:29                 6 roads.cpg
03/04/2015  09:35       310,237,909 roads.dbf
03/04/2015  09:29               144 roads.prj
03/04/2015  09:35       574,407,012 roads.shp
03/04/2015  09:35        25,325,620 roads.shx
03/04/2015  23:37    &lt;DIR&gt;          Wegvakken
           5 File(s)    909,970,691 bytes
           3 Dir(s)  89,474,977,792 bytes free</code></pre>
<p>Any help would be greatly appreciated.</p>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-osrm" rel="tag" title="see questions tagged &#39;osrm&#39;">osrm</span> <span class="post-tag tag-link-installation" rel="tag" title="see questions tagged &#39;installation&#39;">installation</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Sep '15, 10:29</strong></p>
<img src="https://secure.gravatar.com/avatar/543b438feb510e40268215991d88f2d5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="a6datta&#39;s gravatar image" />
<p><span>a6datta</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="a6datta has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Sep '15, 01:25</strong> </span></p>
</div>
</div>
<div id="comments-container-45071" class="comments-container">
<span id="45072"></span>
<div id="comment-45072" class="comment">
<div id="post-45072-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>What's the spec of your machine?</p>
</div>
<div id="comment-45072-info" class="comment-info">
<span class="comment-age">(05 Sep '15, 10:57)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
<span id="45075"></span>
<div id="comment-45075" class="comment">
<div id="post-45075-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I don't think it's working. If I look at task manager it's silent. It occupied the diskspace but not writing anything. The file name in temp is 'Wegvakken' but I am extracting england map. My machine is i5, 16GB RAM and SSD with writing speed 550MB.</p>
</div>
<div id="comment-45075-info" class="comment-info">
<span class="comment-age">(05 Sep '15, 13:18)</span> <span class="comment-user userinfo">a6datta</span>
</div>
</div>
<span id="45077"></span>
<div id="comment-45077" class="comment">
<div id="post-45077-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I managed it get it worked.</p>
</div>
<div id="comment-45077-info" class="comment-info">
<span class="comment-age">(05 Sep '15, 17:55)</span> <span class="comment-user userinfo">a6datta</span>
</div>
</div>
<span id="45078"></span>
<div id="comment-45078" class="comment">
<div id="post-45078-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/11438/a6datta"></a><a href="http://help.openstreetmap.org/users/11438/a6datta">@a6datta</a>: could you please write about the problem and solution here - for other people with the same issue.</p>
</div>
<div id="comment-45078-info" class="comment-info">
<span class="comment-age">(06 Sep '15, 01:34)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="45087"></span>
<div id="comment-45087" class="comment">
<div id="post-45087-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>The windows build does not contain profile.lua file. I manually created the file. The contents of the file is require("lib/access") require("profiles/car")</p>
</div>
<div id="comment-45087-info" class="comment-info">
<span class="comment-age">(07 Sep '15, 01:24)</span> <span class="comment-user userinfo">a6datta</span>
</div>
</div>
</div>
<div id="comment-tools-45071" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45071-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

