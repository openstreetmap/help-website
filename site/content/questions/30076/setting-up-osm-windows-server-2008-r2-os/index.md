+++
type = "question"
title = "Setting up OSM Windows Server 2008 R2 (OS)"
description = '''Hello List, I have installed PostGRES 9.2 and PostGIS on windows server OS and I am having issues using the import tools to import OSM data to PostGRES.  Just to start, I do not have an option of running any flavor of linux at all, virtual or not.  I wanted to use osm2pgsql to import the pbf files o...'''
date = "2014-01-22T13:31:00Z"
lastmod = "2014-01-24T12:59:00Z"
weight = 30076
keywords = [ "osm", "postgres", "osmosis", "osm2pgsql" ]
aliases = [ "/questions/30076" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Setting up OSM Windows Server 2008 R2 (OS)](/questions/30076/setting-up-osm-windows-server-2008-r2-os)

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
<span id="post-30076-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30076-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-30076-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello List,</p>
<p>I have installed PostGRES 9.2 and PostGIS on windows server OS and I am having issues using the import tools to import OSM data to PostGRES.<br />
</p>
<p>Just to start, I do not have an option of running any flavor of linux at all, virtual or not.<br />
</p>
<p>I wanted to use osm2pgsql to import the pbf files of the whole planet into the PostGRES database, but the program keeps crashing in slim mode '--slim'.</p>
<p>When I switch to osmosis, I just can't get it to setup correctly at all. When I call the program from the .bat file, it say C:\program isn't a valid path, which it isn't. So I moved the program to the root and placed it in c:\osmosis\bin. I still cannot get the osmosis to work.</p>
<p>Are there database tuning options I need to set in PostGRES?<br />
Are there additional commands I need to set on the import of osm2pgsql to help with the program crashing? Is there a setup guide for windows for osmosis?</p>
<p>Thank you</p>
<p>A</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-postgres" rel="tag" title="see questions tagged &#39;postgres&#39;">postgres</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Jan '14, 13:31</strong></p>
<img src="https://secure.gravatar.com/avatar/1df0b0daef7049f4aa8561e4c29fd7de?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Fisherman12i&#39;s gravatar image" />
<p><span>Fisherman12i</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Fisherman12i has no accepted answers">0%</span> </br></br></p>
</div>
</div>
<div id="comments-container-30076" class="comments-container">
<span id="30077"></span>
<div id="comment-30077" class="comment">
<div id="post-30077-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Can you please post the crash log os osm2pgsql?</p>
</div>
<div id="comment-30077-info" class="comment-info">
<span class="comment-age">(22 Jan '14, 13:34)</span> <span class="comment-user userinfo">iii</span>
</div>
</div>
<span id="30078"></span>
<div id="comment-30078" class="comment">
<div id="post-30078-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>where is the crash report located?</p>
</div>
<div id="comment-30078-info" class="comment-info">
<span class="comment-age">(22 Jan '14, 13:39)</span> <span class="comment-user userinfo">Fisherman12i</span>
</div>
</div>
<span id="30081"></span>
<div id="comment-30081" class="comment">
<div id="post-30081-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>When iii says "post the crash log", he means "post it to a text sharing site like Pastebin and post the URL here".</p>
</div>
<div id="comment-30081-info" class="comment-info">
<span class="comment-age">(22 Jan '14, 13:50)</span> <span class="comment-user userinfo">Jonathan Ben...</span>
</div>
</div>
<span id="30084"></span>
<div id="comment-30084" class="comment">
<div id="post-30084-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I was asking where the log file lives on the system so I can post it. I looked in the osm2pgsql folders and didn't find it. So i was wondering if it's placed in the appdata folders etc... To be clear on the crashing, the process crashed on windows server, so there might not be a log file.</p>
</div>
<div id="comment-30084-info" class="comment-info">
<span class="comment-age">(22 Jan '14, 14:10)</span> <span class="comment-user userinfo">Fisherman12i</span>
</div>
</div>
<span id="30092"></span>
<div id="comment-30092" class="comment">
<div id="post-30092-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Unless anyone has tried this on W2K8R2 (which I doubt) it's quite possible that no-one knows where the log's going to end up. It's also possible (given that it's Windows) that the program might be failing because it can't open a logfile (or any other output file). To try and work around that, try installing away from root and away from "program files" etc. (which it sounds like your're doing) and run from a command prompt so that you can see any errors written to stdout.</p>
<p>You say that it's "crashing", but what error message do you see that tells you that?</p>
</div>
<div id="comment-30092-info" class="comment-info">
<span class="comment-age">(22 Jan '14, 15:45)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="30095"></span>
<div id="comment-30095" class="comment not_top_scorer">
<div id="post-30095-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Not an answer, but may contain some hints - it might be worth trying to hunt down video / slides for <a href="http://lanyrd.com/2013/sotm/scpkgp/">this SOTM presentation</a>?</p>
</div>
<div id="comment-30095-info" class="comment-info">
<span class="comment-age">(22 Jan '14, 16:06)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="30151"></span>
<div id="comment-30151" class="comment not_top_scorer">
<div id="post-30151-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Crash log is here: <a href="http://pastebin.com/RZLa8cgE">http://pastebin.com/RZLa8cgE</a></p>
</div>
<div id="comment-30151-info" class="comment-info">
<span class="comment-age">(23 Jan '14, 13:53)</span> <span class="comment-user userinfo">Fisherman12i</span>
</div>
</div>
<span id="30152"></span>
<div id="comment-30152" class="comment not_top_scorer">
<div id="post-30152-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That's not a log from osm2pgsql as such, just Windows saying that it failed. Try running from a command prompt to see if you can get anything more meaningful out of it.</p>
</div>
<div id="comment-30152-info" class="comment-info">
<span class="comment-age">(23 Jan '14, 14:05)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="30153"></span>
<div id="comment-30153" class="comment not_top_scorer">
<div id="post-30153-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>No error message was spit out from osm2pgsql</p>
</div>
<div id="comment-30153-info" class="comment-info">
<span class="comment-age">(23 Jan '14, 14:39)</span> <span class="comment-user userinfo">Fisherman12i</span>
</div>
</div>
<span id="30154"></span>
<div id="comment-30154" class="comment not_top_scorer">
<div id="post-30154-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>So what is the actual problem? Can you please provide us the command line you use to invoke the import?</p>
</div>
<div id="comment-30154-info" class="comment-info">
<span class="comment-age">(23 Jan '14, 15:11)</span> <span class="comment-user userinfo">iii</span>
</div>
</div>
<span id="30155"></span>
<div id="comment-30155" class="comment not_top_scorer">
<div id="post-30155-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Normally postgres log files are put in the data subdirectory of the postgres installation. I generally install postgres in a location with no spaces in directory names. You may wish to change the degree of logging for postgres, which you can do through an option in PgAdmin 3.</p>
<p>However, before doing any of these things, it is important to know which version of each piece of software you are using and basic info about the configuration of your box (amount of RAM..).</p>
<p>Try importing Liechtenstein, if it works come back here, else read the docs more closely.</p>
</div>
<div id="comment-30155-info" class="comment-info">
<span class="comment-age">(23 Jan '14, 15:12)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="30156"></span>
<div id="comment-30156" class="comment not_top_scorer">
<div id="post-30156-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>OK, so I was wrong - <a href="https://github.com/openstreetmap/osm2pgsql/issues/117">at least one other person</a> uses osm2pgsl on Windows :-)</p>
</div>
<div id="comment-30156-info" class="comment-info">
<span class="comment-age">(23 Jan '14, 15:17)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-30076" class="comment-tools">
<span class="comments-showing"> showing 5 of 12 </span> <a href="#" class="show-all-comments-link">show 7 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-30076-form-container" class="comment-form-container">
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

<span id="30179"></span>

<div id="answer-container-30179" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-30179-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30179-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-30179-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I was able to setup PostgreSQL (APIDB and PostGIS) loaded PostgreSQL (APIDB) it with the full planet file, and set it up to be updated from the hourly diffs. Using <strong>Windows Professional 7</strong> x64. Not Windows Server 2008R2, but not too different...</p>
<p>To be able to run osmosis, the PATH variable must contain the directory for the <strong>Java runtime</strong> (JRE). In my case it is "C:\Program Files (x86)\Java\jre7\bin" (was able to run it using the 64-bit JRE, but this is another history). It'll be different for you, likely.</p>
<p>The command I used to load the planet file was:</p>
<pre><code>osmosis -v --fast-read-xml file=[location of planet file] --buffer bufferCapacity=100000 --log-progress --write-apidb host=[server] database=[database] user=[user] password=[password]</code></pre>
<p>Most likely you'll want to change the --fast-read-xml to --read-pbf. That "xml" speaks for itself, it was done when the main form of the planet file was XML...</p>
<p>Also, you may try to add a --tee and the appropriate command to save it to the PostGIS database <em>at the same time</em>.</p>
<p>If you try to load the full planet file, osmosis (and very likely osmtopgsql as well) will fail with an <strong>PostgreSQL error</strong> stating that it cannot process transactions with more than 2^32 commands in it. For this problem the only workaround I found was to (temporarily!) disable transaction support of osmosis, altering its source code directly. More details about the changes can be found <a href="http://addictedtoosm.wordpress.com/2013/01/03/carga-do-planet-osm-possivel/">here</a> (Note: In portuguese)</p>
<p>As far as I could find, this is a limitation of PostgreSQL, and may be fixed in the future. It arose about September/2012 when the planet file grew too large.</p>
<p>For updating from the hourly diffs, I use the following osmosis command:</p>
<pre><code>osmosis -v --rri workingDirectory=[path_of_osmosis_work_dir] --write-apidb-change host=[your_server] password=[password] database=[database] user=[user] validateSchemaVersion=yes allowIncorrectSchemaVersion=no populateCurrentTables=yes</code></pre>
<p>In this case you also can use --tee to save changes to PostGIS at the same time.</p>
<p>Anyway, the process took (i7 3770, 32GB RAM, PostgreSQL 9.2 64-bit, tables and index spread over 6 tablespaces on 7 physical disks) <strong>about 1.5 weeks</strong>.</p>
<p>Make sure you have plenty of free disk space (the APIDB is now 1.5TB, PostGIS probably will grow to about 800GB). The temp files also grow very large, I prefer to unpack the planet file before loading it.</p>
<p>Please contact me again if your trouble persists.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Jan '14, 12:59</strong></p>
<img src="https://secure.gravatar.com/avatar/94b019f273c04cd88bc1c8dd0a8f2161?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MCPicoli&#39;s gravatar image" />
<p><span>MCPicoli</span><br />
<span class="score" title="2172 reputation points"><span>2.2k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MCPicoli has 10 accepted answers">24%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Jan '14, 15:21</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/49a7d0e0408e9cf2f698faac0f4d837a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iii&#39;s gravatar image" />
<p><span>iii</span><br />
<span class="score" title="4892 reputation points"><span>4.9k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="40 badges"><span class="silver">●</span><span class="badgecount">40</span></span><span title="82 badges"><span class="bronze">●</span><span class="badgecount">82</span></span></p>
</div>
</div>
<div id="comments-container-30179" class="comments-container">
&#10;</div>
<div id="comment-tools-30179" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30179-form-container" class="comment-form-container">
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

