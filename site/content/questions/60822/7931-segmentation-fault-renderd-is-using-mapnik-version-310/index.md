+++
type = "question"
title = "7931 segmentation fault (Renderd is using mapnik version 3.1.0)"
description = '''How this error could be explained? It was about a week for me to try to install mapnik. I finally found the manual bellow.  It brought me as far as installing apache on one of the two boxes were I am trying to set it up.  Second box could not even get mod-tiles built.  But here I am stuck when tryin...'''
date = "2017-11-27T23:08:00Z"
lastmod = "2017-11-29T03:29:00Z"
weight = 60822
keywords = [ "renderd", "mapnik" ]
aliases = [ "/questions/60822" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [7931 segmentation fault (Renderd is using mapnik version 3.1.0)](/questions/60822/7931-segmentation-fault-renderd-is-using-mapnik-version-310)

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
<span id="post-60822-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60822-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-60822-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How this error could be explained? It was about a week for me to try to install mapnik. I finally found the manual bellow.</p>
<p>It brought me as far as installing apache on one of the two boxes were I am trying to set it up.</p>
<p>Second box could not even get mod-tiles built.</p>
<p>But here I am stuck when trying to call renderd from a command line (does not work from httpd either). This box is relatively weak. Has 512MB ram and I use it as it is easy to respawn it clean. Second box I have is very powerful (16GB of RAM) but there I stuck with (mapnik/box2d.hpp: No such file or directory error when building mod-tiles).</p>
<p><a href="https://switch2osm.org/manually-building-a-tile-server-16-04-2-lts/">https://switch2osm.org/manually-building-a-tile-server-16-04-2-lts/</a></p>
<pre><code>renderd -f -c /usr/local/etc/renderd.conf
&#10;renderd[7931]: Rendering daemon started
renderd[7931]: Initiating request_queue
renderd[7931]: Parsing section renderd
renderd[7931]: Parsing render section 0
renderd[7931]: Parsing section mapnik
renderd[7931]: Parsing section ajt
renderd[7931]: config renderd: unix socketname=/var/run/renderd/renderd.sock
renderd[7931]: config renderd: num_threads=4
renderd[7931]: config renderd: num_slaves=0
renderd[7931]: config renderd: tile_dir=/mapnik/mod_tile
renderd[7931]: config renderd: stats_file=/var/run/renderd/renderd.stats
renderd[7931]: config mapnik:  plugins_dir=/usr/lib/mapnik/3.0/input
renderd[7931]: config mapnik:  font_dir=/usr/share/fonts/truetype
renderd[7931]: config mapnik:  font_dir_recurse=1
renderd[7931]: config renderd(0): Active
renderd[7931]: config renderd(0): unix socketname=/var/run/renderd/renderd.sock
renderd[7931]: config renderd(0): num_threads=4
renderd[7931]: config renderd(0): tile_dir=/mapnik/mod_tile
renderd[7931]: config renderd(0): stats_file=/var/run/renderd/renderd.stats
renderd[7931]: config map 0:   name(ajt) file(/mapnik/mapnik.xml) uri(/hot/) htcp() host(localhost)
renderd[7931]: Initialising unix server socket on /var/run/renderd/renderd.sock
renderd[7931]: Created server socket 5
renderd[7931]: Renderd is using mapnik version 3.1.0
[1]    7931 segmentation fault (core dumped)  renderd -f -c /usr/local/etc/renderd.con</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Nov '17, 23:08</strong></p>
<img src="https://secure.gravatar.com/avatar/0af3a91d5ddde7174bf4031d70564f8e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Oblomingo&#39;s gravatar image" />
<p><span>Oblomingo</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Oblomingo has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-60822" class="comments-container">
<span id="60826"></span>
<div id="comment-60826" class="comment">
<div id="post-60826-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>"segmentation fault (core dumped)" just means "something went wrong". Without more information about how you got to that position it's difficult to say anything more helpful.</p>
<p>What OS and what version are you running on each box?</p>
<p>What did you install on each and in what order?</p>
<p>In particular, what comments did you type in what order to get the "mapnik/box2d.hpp: No such file or directory error" error?</p>
</div>
<div id="comment-60826-info" class="comment-info">
<span class="comment-age">(28 Nov '17, 00:04)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="60827"></span>
<div id="comment-60827" class="comment">
<div id="post-60827-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>May I ask to ignore "mapnik/box2d.hpp". This is related to a different server. Here I am getting only one error 7931 segmentation fault</p>
<p>It happens when I run the following command</p>
<p>renderd -f -c /usr/local/etc/renderd.conf</p>
<p>Content of the file</p>
<p>[renderd] num_threads=1 tile_dir=/mapnik/mod_tile stats_file=/mapnik/renderd.stats</p>
<p>[mapnik] plugins_dir=/usr/lib/mapnik/3.0/input font_dir=/usr/share/fonts/truetype font_dir_recurse=1</p>
<p>[ajt] URI=/hot/ TILEDIR=/mapnik/mod_tile XML=/home/stan/src/openstreetmap-carto/mapnik.xml HOST=localhost TILESIZE=256 MAXZOOM=20</p>
<p>Running it on Ubuntu 16.04.3 LTS</p>
<p>Does this renderd has any kind of traditional log where it reports details of what it is doing. I can see something is printed to console but as you noticed it is not enough to get to the root of the problem.</p>
<p>Thank you btw for looking into it.</p>
</div>
<div id="comment-60827-info" class="comment-info">
<span class="comment-age">(28 Nov '17, 01:02)</span> <span class="comment-user userinfo">Oblomingo</span>
</div>
</div>
<span id="60828"></span>
<div id="comment-60828" class="comment">
<div id="post-60828-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<blockquote>
<p>Does this renderd has any kind of traditional log where it reports details of what it is doing.</p>
</blockquote>
<p>Yes, when run that way it should output to stdout, but it's falling over before it got a chance.</p>
<p>It seems odd that (for example) you've got things pointing at "/mapnik/" rather than "/var/lib"? Also it's odd that you're telling it "num_threads=1" yet it starts 4, and uses a different stats file.</p>
<p>It's a long time since I've tried to render tiles on something with as little memory as 512Mb, but I have done it in the past (albeit with older versions of everything).</p>
<p>Where did the mapnik you're using come from? <a href="https://switch2osm.org/manually-building-a-tile-server-16-04-2-lts/">https://switch2osm.org/manually-building-a-tile-server-16-04-2-lts/</a> fetches it via apt-get, and when I restart renderd here I see "Renderd is using mapnik version 3.0.9" rather than 3.1.0. Are you perhaps trying to use a self-built mapnik version?</p>
<p>I've never had a lot of success with that: <a href="https://github.com/mapnik/mapnik/issues/3462">https://github.com/mapnik/mapnik/issues/3462</a> :)</p>
</div>
<div id="comment-60828-info" class="comment-info">
<span class="comment-age">(28 Nov '17, 01:21)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="60829"></span>
<div id="comment-60829" class="comment not_top_scorer">
<div id="post-60829-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<blockquote>
<blockquote>
<p>pointing at "/mapnik/" rather than "/var/lib I tried to change path because I thought issue might be related to permissions. So I moved all stuff to one folder and give all permissions.</p>
<p>Where did the mapnik you're using come from? Yes, I tried to follow these steps.</p>
<p>Are you perhaps trying to use a self-built mapnik version First I tried to build mapnik myself semi/successfully as I never was able to get a test cases passed. There might be a bug in mapnik that when it inits posgres test databases it does not add extension postgis_topology because it expects it would be added with postgis when it should be another way around for the latest versions of postgres. Long story short my self build version of mapnik could not be tested because test database did not have raster types (could only be added by postgis_topology extension that is not in mapnik test init script). So I stopped building source and switched to binaries. However you might be right and there is somewhere a collision between self build and binary packages. Not sure how could it be checked.</p>
</blockquote>
</blockquote>
</div>
<div id="comment-60829-info" class="comment-info">
<span class="comment-age">(28 Nov '17, 01:39)</span> <span class="comment-user userinfo">Oblomingo</span>
</div>
</div>
<span id="60830"></span>
<div id="comment-60830" class="comment not_top_scorer">
<div id="post-60830-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You can try to use "locate libmapnik" - your self built version would be probably somewhere in the /usr/local.</p>
</div>
<div id="comment-60830-info" class="comment-info">
<span class="comment-age">(28 Nov '17, 02:20)</span> <span class="comment-user userinfo">kocio</span>
</div>
</div>
<span id="60840"></span>
<div id="comment-60840" class="comment not_top_scorer">
<div id="post-60840-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I traced libmapnik down and uninstalled it. So now version 3.0.9 is reported in the log file. However result is the same - segmentation fails.</p>
<p>BOX 512MB renderd[26381]: Renderd is using mapnik version 3.0.9 [1] 26380 segmentation fault (core dumped) sudo -u renderaccount renderd -f -c /usr/local/etc/renderd.conf</p>
<p>I tried doing the same on the more powerful box where mapnik was built from source and error is the same. Problem seems to be not related to hardware available as box with 512MB memory is failing the same way as box with 16GB</p>
<p>BOX 16GB renderd[22083]: Initialising unix server socket on /var/run/renderd/renderd.sock renderd[22083]: Created server socket 5 renderd[22083]: Renderd is using mapnik version 3.1.0 [1] 22083 segmentation fault (core dumped) renderd -f -c /usr/local/etc/renderd.conf</p>
</div>
<div id="comment-60840-info" class="comment-info">
<span class="comment-age">(28 Nov '17, 15:41)</span> <span class="comment-user userinfo">Oblomingo</span>
</div>
</div>
<span id="60841"></span>
<div id="comment-60841" class="comment not_top_scorer">
<div id="post-60841-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It seems to fail because of this line</p>
<p>plugins_dir=/usr/lib/mapnik/3.0/input</p>
<p>without this line it starts but later complain that plugin dir is not set. However there is no segmentation error. Content of the folder seems to be correct</p>
<p>-rwxrwxrwx 1 renderaccount renderaccount 619K Dec 3 2015 topojson.input -rwxrwxrwx 1 renderaccount renderaccount 148K Dec 3 2015 sqlite.input -rwxrwxrwx 1 renderaccount renderaccount 171K Dec 3 2015 shape.input -rwxrwxrwx 1 renderaccount renderaccount 159K Dec 3 2015 raster.input -rwxrwxrwx 1 renderaccount renderaccount 248K Dec 3 2015 postgis.input -rwxrwxrwx 1 renderaccount renderaccount 191K Dec 3 2015 pgraster.input -rwxrwxrwx 1 renderaccount renderaccount 135K Dec 3 2015 ogr.input -rwxrwxrwx 1 renderaccount renderaccount 755K Dec 3 2015 geojson.input -rwxrwxrwx 1 renderaccount renderaccount 71K Dec 3 2015 gdal.input -rwxrwxrwx 1 renderaccount renderaccount 664K Dec 3 2015 csv.input</p>
</div>
<div id="comment-60841-info" class="comment-info">
<span class="comment-age">(28 Nov '17, 15:57)</span> <span class="comment-user userinfo">Oblomingo</span>
</div>
</div>
<span id="60842"></span>
<div id="comment-60842" class="comment not_top_scorer">
<div id="post-60842-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If you can reproduce the problem (perhaps in a virtual machine installed under VirtualBox running on the larger machine) using an "off the shelf" copy of 16.04 LTS then people will have a chance of being able to investigate it. Until then all we can say that there's something different about your systems that's causing the problems, and only you have access there.</p>
<p>I last ran through the "switch2osm" page on 22/10/2017 and at that time "it just worked". Obviously new versions of software come out all the time and something might have broken, but I'm guessing that it's actually related to your previous self-build of mapnik and python-mapnik.</p>
</div>
<div id="comment-60842-info" class="comment-info">
<span class="comment-age">(28 Nov '17, 16:00)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="60843"></span>
<div id="comment-60843" class="comment">
<div id="post-60843-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I run command mapnik-config --input-plugins It gave me a different directory /usr/local/lib/mapnik/input I changed renderd.conf plugins_dir=/usr/local/lib/mapnik/input and it started working</p>
<p>At least fixed one box. Second box (the one with 512MB memory does not work no matter how renderd.conf looks like - but ok. at least something works)</p>
</div>
<div id="comment-60843-info" class="comment-info">
<span class="comment-age">(28 Nov '17, 16:29)</span> <span class="comment-user userinfo">Oblomingo</span>
</div>
</div>
<span id="60846"></span>
<div id="comment-60846" class="comment not_top_scorer">
<div id="post-60846-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Finally I got a second box running.</p>
<p>Solution was</p>
<ol>
<li><p>Increased memory to 1GB</p></li>
<li><p>Built mapnik 3.1 (and python bindings) from source (map available in ubuntu repo (version 3.0.9) did not work on neither boxes I tried)</p></li>
<li><p>Was very hard to build mod_tiles with mapnik version 3.1. It was trying to use some artifacts left after mapnik build and build was failing with bizarre messages as it was not what it expexted. So I had to delete some of the mapnik build artifacts in order to make mod_tiles succeed.</p></li>
</ol>
<p>At the end got everything working. May be if I tried from a clean slate then "switch2osm" way would also work but I give it a serious doubt. Both boxes I have only worked on mapnik build from source</p>
</div>
<div id="comment-60846-info" class="comment-info">
<span class="comment-age">(29 Nov '17, 00:50)</span> <span class="comment-user userinfo">Oblomingo</span>
</div>
</div>
<span id="60847"></span>
<div id="comment-60847" class="comment">
<div id="post-60847-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Good that you got it working, but in both cases you'd half-built-from source first, so you likely had a mixture of stuff lying around.</p>
<p>It might be useful if you could explain what you actually did rather than just say e.g. "So I had to delete some of the mapnik build artifacts" - that doesn't help anyone who's trying to do it in the future.</p>
</div>
<div id="comment-60847-info" class="comment-info">
<span class="comment-age">(29 Nov '17, 01:14)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="60851"></span>
<div id="comment-60851" class="comment not_top_scorer">
<div id="post-60851-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>May be. But in one case I have deleted (uninstall) source build mapnik alltogether and made sure I had only ubuntu supplied version left (3.0.9) and it did not work (segmentation error)</p>
<p>when I was trying to build mod_tiles it was complaining that it could not find jpeg turbo lib referring some unusual path /home/travis/.. (travis is not a user on this server)</p>
<p>mod_tile libtool: error: cannot find the library '/home/travis/build/mapbox/mason/mason_packages/linux-x86_64/jpeg_turbo/1.5.1/lib/libjpeg.la'</p>
<p>It also was giving warning that some libs were moved. I could not reproduce it anymore.</p>
<p>I decided to delete mason_packages folder and as strange it was - it helped</p>
<p>rm -rf /home/myuser/src/mapnik/mason_packages/</p>
<p>After I deleted it mod_tiles was successfully built and rendering starts working</p>
</div>
<div id="comment-60851-info" class="comment-info">
<span class="comment-age">(29 Nov '17, 03:29)</span> <span class="comment-user userinfo">Oblomingo</span>
</div>
</div>
</div>
<div id="comment-tools-60822" class="comment-tools">
<span class="comments-showing"> showing 5 of 12 </span> <a href="#" class="show-all-comments-link">show 7 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-60822-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

