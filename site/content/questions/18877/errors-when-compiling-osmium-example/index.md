+++
type = "question"
title = "Errors when compiling Osmium example"
description = '''I&#x27;m trying to compile the examples from Osmium, but I get an error. $:~/osmium/examples$ make  g++ -g -Wall -Wextra -Wdisabled-optimization -pedantic -Wctor-dtor-privacy -Wnon-virtual-dtor -Woverloaded-virtual -Wsign-promo -Wno-long-long -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -I../include -DOSMI...'''
date = "2013-01-05T16:45:00Z"
lastmod = "2013-01-16T18:11:00Z"
weight = 18877
keywords = [ "osmium" ]
aliases = [ "/questions/18877" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Errors when compiling Osmium example](/questions/18877/errors-when-compiling-osmium-example)

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
<span id="post-18877-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18877-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-18877-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm trying to compile the examples from Osmium, but I get an error.</p>
<pre><code>$:~/osmium/examples$ make
&#10;g++ -g -Wall -Wextra -Wdisabled-optimization -pedantic -Wctor-dtor-privacy -Wnon-virtual-dtor -Woverloaded-virtual -Wsign-promo -Wno-long-long -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -I../include -DOSMIUM_WITH_DEBUG -I/usr/include/libxml2 -o osmium_convert osmium_convert.cpp -lexpat -lz -lpthread -lprotobuf-lite -losmpbf -lxml2
In file included from ../include/osmium/handler.hpp:33:0,
                 from ../include/osmium/input.hpp:29,
                 from ../include/osmium/input/pbf.hpp:35,
                 from ../include/osmium.hpp:26,
                 from osmium_convert.cpp:33:
../include/osmium/osm/area.hpp:27:36: fatal error: geos/geom/MultiPolygon.h: No such file or directory
compilation terminated.
make: *** [osmium_convert] Error 1
&#10;$:~/osmium/examples$</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmium" rel="tag" title="see questions tagged &#39;osmium&#39;">osmium</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Jan '13, 16:45</strong></p>
<img src="https://secure.gravatar.com/avatar/407d8e57e3058ea1969d515f44547556?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rub21&#39;s gravatar image" />
<p><span>Rub21</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rub21 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Jan '13, 08:42</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/2d4dfcdcde73aa5e2ffa4a9b3a7cb51d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jochen%20Topf&#39;s gravatar image" />
<p><span>Jochen Topf</span><br />
<span class="score" title="5244 reputation points"><span>5.2k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span></p>
</div>
</div>
<div id="comments-container-18877" class="comments-container">
&#10;</div>
<div id="comment-tools-18877" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18877-form-container" class="comment-form-container">
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

<span id="18893"></span>

<div id="answer-container-18893" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-18893-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18893-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-18893-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You have to install all the prerequisites mentioned in the README. In this case you are missing the GEOS library (or have a version that's too old). This wiki page may also help you: <a href="http://wiki.openstreetmap.org/wiki/Osmium/Quick_Start">http://wiki.openstreetmap.org/wiki/Osmium/Quick_Start</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Jan '13, 08:39</strong></p>
<img src="https://secure.gravatar.com/avatar/2d4dfcdcde73aa5e2ffa4a9b3a7cb51d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jochen%20Topf&#39;s gravatar image" />
<p><span>Jochen Topf</span><br />
<span class="score" title="5244 reputation points"><span>5.2k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jochen Topf has 32 accepted answers">31%</span></p>
</div>
</div>
<div id="comments-container-18893" class="comments-container">
&#10;</div>
<div id="comment-tools-18893" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18893-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="19146"></span>

<div id="answer-container-19146" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-19146-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19146-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-19146-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>On my ubuntu, i had to install <strong><a href="http://packages.ubuntu.com/search?searchon=contents&amp;keywords=MultiPolygon.h&amp;mode=exactfilename&amp;suite=quantal&amp;arch=any">libgeos++-dev</a></strong> from the ubuntu repository with success</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Jan '13, 18:11</strong></p>
<img src="https://secure.gravatar.com/avatar/c551898078227f2dafa97154b722b805?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BrunoC&#39;s gravatar image" />
<p><span>BrunoC</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BrunoC has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Jan '13, 07:23</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-19146" class="comments-container">
&#10;</div>
<div id="comment-tools-19146" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19146-form-container" class="comment-form-container">
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

