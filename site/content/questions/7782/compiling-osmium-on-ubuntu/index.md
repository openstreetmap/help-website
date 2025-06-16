+++
type = "question"
title = "Compiling osmium on Ubuntu"
description = '''Following https://wiki.openstreetmap.org/wiki/Osmium/Quick_Start on Ubuntu 10.04 LTS with libprotobuf-dev installed gives lots of &quot;/usr/bin/ld: cannot find -lprotobuf-lite&quot; errors. OSM-binary can be compiled using the non-Debian/Ubuntu instructions (e.g. make instead of debuild), but make osmium/exam...'''
date = "2011-09-11T13:33:00Z"
lastmod = "2011-09-11T15:41:00Z"
weight = 7782
keywords = [ "osmium", "c++" ]
aliases = [ "/questions/7782" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Compiling osmium on Ubuntu](/questions/7782/compiling-osmium-on-ubuntu)

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
<span id="post-7782-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7782-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-7782-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Following <a href="https://wiki.openstreetmap.org/wiki/Osmium/Quick_Start">https://wiki.openstreetmap.org/wiki/Osmium/Quick_Start</a> on Ubuntu 10.04 LTS with libprotobuf-dev installed gives lots of "/usr/bin/ld: cannot find -lprotobuf-lite" errors.</p>
<p>OSM-binary can be compiled using the non-Debian/Ubuntu instructions (e.g. make instead of debuild), but make osmium/examples still fails looking for -lprotobuf-lite</p>
<p>Changing LDFLAGS on line 26 of Makefile to /usr/lib doesn't seem to help</p>
<pre><code>user@ireem:~$ ls  /usr/lib/libprotobuf*
/usr/lib/libprotobuf-c.a         /usr/lib/libprotobuf-lite.so.5
/usr/lib/libprotobuf-c.so        /usr/lib/libprotobuf-lite.so.5.0.0
/usr/lib/libprotobuf-c.so.0      /usr/lib/libprotobuf.so
/usr/lib/libprotobuf-c.so.0.0.0  /usr/lib/libprotobuf.so.5
/usr/lib/libprotobuf.la          /usr/lib/libprotobuf.so.5.0.0
&#10;user@ireem:~/osm/osmium/libosmpbf/osmium/examples$ make clean
rm -f *.o core osmium_sizeof osmium_debug osmium_stats osmium_find_bbox osmium_time osmium_progress osmium_convert osmium_toogr osmium_toshape nodedensity
user@ireem:~/osm/osmium/libosmpbf/osmium/examples$ make
g++ -g -Wall -Wextra -Wredundant-decls -Wdisabled-optimization -pedantic -Wctor-dtor-privacy -Wnon-virtual-dtor -Woverloaded-virtual -Wsign-promo -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -I../include -DOSMIUM_WITH_OUTPUT_OSM_XML -I/usr/include/libxml2 -o osmium_sizeof osmium_sizeof.cpp -L/usr/lib -lexpat -lpthread -lz -lprotobuf-lite -losmpbf -lxml2
/usr/bin/ld: cannot find -lprotobuf-lite
collect2: ld returned 1 exit status
make: *** [osmium_sizeof] Error 1</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmium" rel="tag" title="see questions tagged &#39;osmium&#39;">osmium</span> <span class="post-tag tag-link-c++" rel="tag" title="see questions tagged &#39;c++&#39;">c++</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Sep '11, 13:33</strong></p>
<img src="https://secure.gravatar.com/avatar/3e44debd67415e7aa7759c83b829be6a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="OJW&#39;s gravatar image" />
<p><span>OJW</span><br />
<span class="score" title="151 reputation points">151</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="OJW has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Sep '11, 13:42</strong> </span></p>
</div>
</div>
<div id="comments-container-7782" class="comments-container">
&#10;</div>
<div id="comment-tools-7782" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7782-form-container" class="comment-form-container">
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

<span id="7783"></span>

<div id="answer-container-7783" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-7783-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7783-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-7783-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="OJW has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You seem to be missing <code>/usr/lib/</code><a href="http://libprotobuf-lite.so"><code>libprotobuf-lite.so</code></a>. Do this:</p>
<p><code>cd /usr/lib</code></p>
<p><code>ln -s libprotobuf-lite.so.5 </code><a href="http://libprotobuf-lite.so"><code>libprotobuf-lite.so</code></a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Sep '11, 13:46</strong></p>
<img src="https://secure.gravatar.com/avatar/4837c9b51f52c9a5accf528cd9729812?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Derick%20Rethans&#39;s gravatar image" />
<p><span>Derick Rethans</span><br />
<span class="score" title="247 reputation points">247</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Derick Rethans has one accepted answer">50%</span></p>
</div>
</div>
<div id="comments-container-7783" class="comments-container">
<span id="7785"></span>
<div id="comment-7785" class="comment">
<div id="post-7785-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Note that this seems to be a bug in the Ubuntu libprotobuf-dev package as it should contain that link but doesn't - this should really be reported to the maintainer of that package.</p>
</div>
<div id="comment-7785-info" class="comment-info">
<span class="comment-age">(11 Sep '11, 14:50)</span> <span class="comment-user userinfo">TomH ♦♦</span>
</div>
</div>
<span id="7786"></span>
<div id="comment-7786" class="comment">
<div id="post-7786-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>TomH: OK, <a href="https://bugs.launchpad.net/ubuntu/+source/protobuf-c/+bug/847065">https://bugs.launchpad.net/ubuntu/+source/protobuf-c/+bug/847065</a></p>
</div>
<div id="comment-7786-info" class="comment-info">
<span class="comment-age">(11 Sep '11, 15:41)</span> <span class="comment-user userinfo">OJW</span>
</div>
</div>
</div>
<div id="comment-tools-7783" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7783-form-container" class="comment-form-container">
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

