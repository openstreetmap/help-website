+++
type = "question"
title = "OSRM-extract crashes when ran"
description = '''I&#x27;ve used git clone to get the latest version of OSRM, built it through build-local.bat and then downloaded great-britain-latest.osm.pbf from GeoFabrik. When I try and run osrm-extract great-britain-latest.osm.pbf it crashes via a win32 process (below) and I can&#x27;t seem to find any info online about ...'''
date = "2016-08-02T15:49:00Z"
lastmod = "2016-08-15T15:17:00Z"
weight = 51211
keywords = [ "osrm" ]
aliases = [ "/questions/51211" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [OSRM-extract crashes when ran](/questions/51211/osrm-extract-crashes-when-ran)

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
<span id="post-51211-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51211-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-51211-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've used <code>git clone</code> to get the latest version of OSRM, built it through <code>build-local.bat</code> and then downloaded <code>great-britain-latest.osm.pbf</code> from <code>GeoFabrik</code>.</p>
<p>When I try and run <code>osrm-extract great-britain-latest.osm.pbf</code> it crashes via a win32 process (below) and I can't seem to find any info online about it. Here's m full console output:</p>
<p><code>C:\Users\james\osrm-backend\osrm_Release&gt;osrm-extract great-britain-latest.osm.pbf [info] Using script profile.lua [info] Input file: great-britain-latest.osm.pbf [info] Profile: profile.lua [info] Threads: 8 [STXXL-MSG] STXXL v1.4.99 (prerelease/Release) (git 1babe452214b4613a2a488d80073f4185c05a0b3) + gnu parallel(__GLIBCXX__) [STXXL-MSG] Disk 'c:\temp\stxxl' is allocated, space: 10000 MiB, I/O implementation: wincall queue=0 devid=0 [info] Parsing in progress..</code></p>
<p>I then get <code>Unhandled exception at 0x00007FFE7DCA98FE (ucrtbase.dll) in osrm-extract.exe: Fatal program exit requested.</code> which I can't figure out.</p>
<p>Can anyone offer any advice please?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osrm" rel="tag" title="see questions tagged &#39;osrm&#39;">osrm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Aug '16, 15:49</strong></p>
<img src="https://secure.gravatar.com/avatar/a7cb490555f288a4bc1232439157dc1c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JamesGould&#39;s gravatar image" />
<p><span>JamesGould</span><br />
<span class="score" title="196 reputation points">196</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JamesGould has one accepted answer">33%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Aug '16, 15:49</strong> </span></p>
</div>
</div>
<div id="comments-container-51211" class="comments-container">
<span id="51212"></span>
<div id="comment-51212" class="comment">
<div id="post-51212-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>The file might be corrupt. Did you compare the checksum?</p>
</div>
<div id="comment-51212-info" class="comment-info">
<span class="comment-age">(02 Aug '16, 16:28)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="51233"></span>
<div id="comment-51233" class="comment">
<div id="post-51233-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You can try asking in the #osrm channel on IRC (<a href="http://irc.osm.org">http://irc.osm.org</a>). My two guesses would be (a) not enough memory or (b) Windows incompatibility with current code.</p>
</div>
<div id="comment-51233-info" class="comment-info">
<span class="comment-age">(03 Aug '16, 15:16)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
</div>
<div id="comment-tools-51211" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51211-form-container" class="comment-form-container">
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

<span id="51424"></span>

<div id="answer-container-51424" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-51424-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51424-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-51424-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>For anyone that stumbles across this post in the future, this error was due to .stxxl being in the wrong directory. Here is a copy of the file contents: <code>disk=c:\temp\stxxl,10000,wincall</code> which is stored in the <code>osrm_Release</code> folder. Ensure <code>C:/temp</code> has enough memory access and it's a writeable folder.</p>
<p>Part of the issue was correcting with <code>Cannot write with no DIRECT mode</code> error that I got when trying to run the extraction tool, which led me to appending <code>direct=on</code> onto the end of the <code>.stxxl</code> file. <strong>Don't do this</strong>. Just do the above checks and it'll work.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Aug '16, 15:17</strong></p>
<img src="https://secure.gravatar.com/avatar/a7cb490555f288a4bc1232439157dc1c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JamesGould&#39;s gravatar image" />
<p><span>JamesGould</span><br />
<span class="score" title="196 reputation points">196</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JamesGould has one accepted answer">33%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Aug '16, 15:19</strong> </span></p>
</div>
</div>
<div id="comments-container-51424" class="comments-container">
&#10;</div>
<div id="comment-tools-51424" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51424-form-container" class="comment-form-container">
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

