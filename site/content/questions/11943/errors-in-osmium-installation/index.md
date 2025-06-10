+++
type = "question"
title = "Errors in osmium installation"
description = '''I am trying to get osmium examples running as per instructions (http://wiki.openstreetmap.org/wiki/Osmium/Quick_Start), but compilation of the examples fails with errors: g++ -g -Wall -Wextra -Wredundant-decls -Wdisabled-optimization -pedantic -Wctor-dtor-privacy -Wnon-virtual-dtor -Woverloaded-virt...'''
date = "2012-04-12T15:37:00Z"
lastmod = "2012-04-16T13:16:00Z"
weight = 11943
keywords = [ "osmium", "installation", "linux" ]
aliases = [ "/questions/11943" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Errors in osmium installation](/questions/11943/errors-in-osmium-installation)

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
<span id="post-11943-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11943-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-11943-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am trying to get osmium examples running as per instructions (<a href="http://wiki.openstreetmap.org/wiki/Osmium/Quick_Start),">http://wiki.openstreetmap.org/wiki/Osmium/Quick_Start),</a> but compilation of the examples fails with errors:</p>
<pre><code>g++ -g -Wall -Wextra -Wredundant-decls -Wdisabled-optimization -pedantic -Wctor-dtor-privacy -Wnon-virtual-dtor -Woverloaded-virtual -Wsign-promo -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -I../include -DOSMIUM_WITH_OUTPUT_OSM_XML -I/usr/include/libxml2 -o osmium_convert osmium_convert.cpp -L/usr/local/lib -lexpat -lpthread -lz -lprotobuf-lite -losmpbf -lxml2
g++ -g -Wall -Wextra -Wredundant-decls -Wdisabled-optimization -pedantic -Wctor-dtor-privacy -Wnon-virtual-dtor -Woverloaded-virtual -Wsign-promo -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -I../include -o osmium_debug osmium_debug.cpp -L/usr/local/lib -lexpat -lpthread -lz -lprotobuf-lite -losmpbf
g++ -g -Wall -Wextra -Wredundant-decls -Wdisabled-optimization -pedantic -Wctor-dtor-privacy -Wnon-virtual-dtor -Woverloaded-virtual -Wsign-promo -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -I../include -o osmium_store_and_debug osmium_store_and_debug.cpp -L/usr/local/lib -lexpat -lpthread -lz -lprotobuf-lite -losmpbf
g++ -g -Wall -Wextra -Wredundant-decls -Wdisabled-optimization -pedantic -Wctor-dtor-privacy -Wnon-virtual-dtor -Woverloaded-virtual -Wsign-promo -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -I../include -o osmium_find_bbox osmium_find_bbox.cpp -L/usr/local/lib -lexpat -lpthread -lz -lprotobuf-lite -losmpbf
g++ -g -Wall -Wextra -Wredundant-decls -Wdisabled-optimization -pedantic -Wctor-dtor-privacy -Wnon-virtual-dtor -Woverloaded-virtual -Wsign-promo -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -I../include -o osmium_progress osmium_progress.cpp -L/usr/local/lib -lexpat -lpthread -lz -lprotobuf-lite -losmpbf
g++ -g -Wall -Wextra -Wredundant-decls -Wdisabled-optimization -pedantic -Wctor-dtor-privacy -Wnon-virtual-dtor -Woverloaded-virtual -Wsign-promo -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -I../include -o osmium_range_from_history osmium_range_from_history.cpp -L/usr/local/lib -lexpat -lpthread -lz -lprotobuf-lite -losmpbf
g++ -g -Wall -Wextra -Wredundant-decls -Wdisabled-optimization -pedantic -Wctor-dtor-privacy -Wnon-virtual-dtor -Woverloaded-virtual -Wsign-promo -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -I../include -DOSMIUM_WITH_OUTPUT_OSM_XML -I/usr/include/libxml2 -o osmium_sizeof osmium_sizeof.cpp -L/usr/local/lib -lexpat -lpthread -lz -lprotobuf-lite -losmpbf -lxml2
g++ -g -Wall -Wextra -Wredundant-decls -Wdisabled-optimization -pedantic -Wctor-dtor-privacy -Wnon-virtual-dtor -Woverloaded-virtual -Wsign-promo -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -I../include -o osmium_stats osmium_stats.cpp -L/usr/local/lib -lexpat -lpthread -lz -lprotobuf-lite -losmpbf -lsqlite3
g++ -g -Wall -Wextra -Wredundant-decls -Wdisabled-optimization -pedantic -Wctor-dtor-privacy -Wnon-virtual-dtor -Woverloaded-virtual -Wsign-promo -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -I../include -o osmium_time osmium_time.cpp -L/usr/local/lib -lexpat -lpthread -lz -lprotobuf-lite -losmpbf
make: gdal-config: Command not found
make: gdal-config: Command not found
g++ -g -Wall -Wextra -Wredundant-decls -Wdisabled-optimization -pedantic -Wctor-dtor-privacy -Wnon-virtual-dtor -Woverloaded-virtual -Wsign-promo -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -I../include -DOSMIUM_WITH_OGR  -o osmium_toogr osmium_toogr.cpp -L/usr/local/lib -lexpat -lpthread -lz -lprotobuf-lite -losmpbf 
osmium_toogr.cpp:31:25: fatal error: ogrsf_frmts.h: No such file or directory
compilation terminated.
make: *** [osmium_toogr] Error 1</code></pre>
<p>System is Ubuntu Oneiric (but I can switch to any other Debian or Ubuntu version if recommended). Is someone able to help me figure out what is going wrong?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmium" rel="tag" title="see questions tagged &#39;osmium&#39;">osmium</span> <span class="post-tag tag-link-installation" rel="tag" title="see questions tagged &#39;installation&#39;">installation</span> <span class="post-tag tag-link-linux" rel="tag" title="see questions tagged &#39;linux&#39;">linux</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Apr '12, 15:37</strong></p>
<img src="https://secure.gravatar.com/avatar/8f930f94e9f607180db8da1cfcfc432e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="g0ldfish&#39;s gravatar image" />
<p><span>g0ldfish</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="g0ldfish has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-11943" class="comments-container">
&#10;</div>
<div id="comment-tools-11943" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11943-form-container" class="comment-form-container">
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

<span id="11947"></span>

<div id="answer-container-11947" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-11947-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11947-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-11947-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As it says in the README you need gdal installed for OGR support:</p>
<p>GDAL (for OGR support) <a href="http://gdal.org/">http://gdal.org/</a> Debian/Ubuntu: libgdal1-dev</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Apr '12, 16:45</strong></p>
<img src="https://secure.gravatar.com/avatar/2d4dfcdcde73aa5e2ffa4a9b3a7cb51d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jochen%20Topf&#39;s gravatar image" />
<p><span>Jochen Topf</span><br />
<span class="score" title="5244 reputation points"><span>5.2k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jochen Topf has 32 accepted answers">31%</span></p>
</div>
</div>
<div id="comments-container-11947" class="comments-container">
<span id="12059"></span>
<div id="comment-12059" class="comment">
<div id="post-12059-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I actually found out last week (searching for "gdal-config: Command not found"), but my comment obviously had not been processed.</p>
<p>May I add the package to debian/ubuntu example command on the wiki page about quick start?</p>
</div>
<div id="comment-12059-info" class="comment-info">
<span class="comment-age">(16 Apr '12, 13:16)</span> <span class="comment-user userinfo">g0ldfish</span>
</div>
</div>
</div>
<div id="comment-tools-11947" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11947-form-container" class="comment-form-container">
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

