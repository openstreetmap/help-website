+++
type = "question"
title = "Planet File GIS Import Fails in Processing: Way"
description = '''Hi, I’ve been attempting to import the planet.bz2 file into my GIS database but the import fails when my VM aborts during the Processing: Way stage of the import. Details:  Machine Windows 7 32 GB RAM Intel i7-3740QM 2.70 GHZ processor 236 GB of disk space 64-bit VirtualBox Version 4.3.4 Linux 2.6 (...'''
date = "2013-12-06T18:01:00Z"
lastmod = "2013-12-07T22:45:00Z"
weight = 28857
keywords = [ "planet", "gis", "osm", "failure" ]
aliases = [ "/questions/28857" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Planet File GIS Import Fails in Processing: Way](/questions/28857/planet-file-gis-import-fails-in-processing-way)

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
<span id="post-28857-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-28857-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-28857-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I’ve been attempting to import the planet.bz2 file into my GIS database but the import fails when my VM aborts during the Processing: Way stage of the import. Details:</p>
<ul>
<li><strong>Machine</strong></li>
<li>Windows 7</li>
<li>32 GB RAM</li>
<li>Intel i7-3740QM 2.70 GHZ processor</li>
<li>236 GB of disk space</li>
<li>64-bit</li>
<li><strong>VirtualBox</strong></li>
<li>Version 4.3.4</li>
<li>Linux 2.6 (64-bit) running CentOS 6.3</li>
<li>PostgreSQL 8.4</li>
<li>27 (of 32) GB RAM</li>
<li>620 GB of disk space (external drive)</li>
<li><strong>After</strong> several aborts I also edited the Postgresql.conf file using these <a href="http://www.geofabrik.de/media/2010-07-10-rendering-toolchain-performance.pdf">recommendations</a> (slide 8).</li>
<li><strong>osm2pgsql Commands</strong></li>
<li>osm2pgsql --username ptosm --password --slim -d gis -C 2048 --style /usr/share/osm2pgsql/default.style /pgsql/planet_tile_file.osm.bz2</li>
<li>osm2pgsql --username ptosm --password --slim -d gis -C 12000 --style /usr/share/osm2pgsql/default.style /pgsql/planet_tile_file.osm.bz2</li>
<li><strong>Log</strong>: Not included because the import runs normally until aborting around (estimate) Processing Node: (2,050,000kb; 36.9 kb/s) Processing: Way (650kb; .07kb/s).</li>
</ul>
<p>Is my machine capable of completing the planet file import? I’ve also asked about this on the VirtualBox forum but I’m asking here in case it’s an OSM-related issue. Any help or advice would be greatly appreciated!</p>
<p>Thanks,</p>
<p>Alpha</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-planet" rel="tag" title="see questions tagged &#39;planet&#39;">planet</span> <span class="post-tag tag-link-gis" rel="tag" title="see questions tagged &#39;gis&#39;">gis</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-failure" rel="tag" title="see questions tagged &#39;failure&#39;">failure</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Dec '13, 18:01</strong></p>
<img src="https://secure.gravatar.com/avatar/7ee1136c8ef2d8dc1e88bedbd50f6db2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Alpha47&#39;s gravatar image" />
<p><span>Alpha47</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Alpha47 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Dec '13, 18:02</strong> </span></p>
</div>
</div>
<div id="comments-container-28857" class="comments-container">
<span id="28864"></span>
<div id="comment-28864" class="comment">
<div id="post-28864-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>How fast is access to the external drive? When you ran with extracts did it appear to be IO-bound?</p>
</div>
<div id="comment-28864-info" class="comment-info">
<span class="comment-age">(06 Dec '13, 21:58)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="28895"></span>
<div id="comment-28895" class="comment">
<div id="post-28895-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>At the time it didn't seem to be but I may not have noticed because these were smaller files that I was able to import much more rapidly than the planet file. I'll update this ticket when I have more information.</p>
<p>Thanks for the response!</p>
</div>
<div id="comment-28895-info" class="comment-info">
<span class="comment-age">(07 Dec '13, 22:45)</span> <span class="comment-user userinfo">Alpha47</span>
</div>
</div>
</div>
<div id="comment-tools-28857" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-28857-form-container" class="comment-form-container">
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

<span id="28858"></span>

<div id="answer-container-28858" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-28858-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-28858-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-28858-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>At least on paper you should be able to import a full planet (no claims about how fast/slow it will be). It would however seem to be rather unlikely that the machine will actually continue to run if the VM starts using the 32GB of memory.</p>
<p>You are using both an old postgresql version and command line options that might have been appropriate 3 years ago, but are more than outdated today (three years ago the planet file contained less than half the nodes it has today). You will need to specify at least -C 18000 and likely it would make sense to use the flat file node store. See for example switch2osm.org for updated information.</p>
<p>Without further information on any errors displayed during the abort it will be difficult to help you with the specific problem.</p>
<p>In general it is a good idea to import a small extract first to check that everything works before embarking on a full planet import.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Dec '13, 20:29</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Dec '13, 22:23</strong> </span></p>
</div>
</div>
<div id="comments-container-28858" class="comments-container">
<span id="28861"></span>
<div id="comment-28861" class="comment">
<div id="post-28861-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the response!</p>
<p>Smaller files (a world extract and a couple continent files) all worked successfully, which is nice in light of the inferior commands and postgres database I was using.</p>
<p>I'll upgrade and adjust my command line options and update this ticket when I have more information.</p>
</div>
<div id="comment-28861-info" class="comment-info">
<span class="comment-age">(06 Dec '13, 21:01)</span> <span class="comment-user userinfo">Alpha47</span>
</div>
</div>
<span id="28867"></span>
<div id="comment-28867" class="comment">
<div id="post-28867-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>BTW you should be importing the data in PBF format, it is quite a bit faster.</p>
</div>
<div id="comment-28867-info" class="comment-info">
<span class="comment-age">(06 Dec '13, 23:05)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-28858" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-28858-form-container" class="comment-form-container">
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

