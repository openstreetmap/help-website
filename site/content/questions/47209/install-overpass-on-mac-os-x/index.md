+++
type = "question"
title = "Install Overpass on Mac OS X"
description = '''For testing purposes (before putting it on a Linux server), I would like to install the Overpass API on Mac OS X (El Capitan). According to the changelog it should also build on a Mac. However, the installation guide is only given for Ubuntu. I would follow these instructions, however homebrew canno...'''
date = "2015-12-18T12:44:00Z"
lastmod = "2021-12-18T21:01:00Z"
weight = 47209
keywords = [ "overpass", "macosx" ]
aliases = [ "/questions/47209" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Install Overpass on Mac OS X](/questions/47209/install-overpass-on-mac-os-x)

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
<span id="post-47209-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47209-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-47209-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>For testing purposes (before putting it on a Linux server), I would like to install the Overpass API on Mac OS X (El Capitan). According to the <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/versions#Other_changes_3">changelog</a> it should also build on a Mac. However, the <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Installation#Installation">installation guide</a> is only given for Ubuntu. I would follow these instructions, however homebrew cannot find the packages libexpat1-dev and zlib1g-dev. What can I do?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-macosx" rel="tag" title="see questions tagged &#39;macosx&#39;">macosx</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Dec '15, 12:44</strong></p>
<img src="https://secure.gravatar.com/avatar/382c1236163ab7156d672328538ba11e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Arik&#39;s gravatar image" />
<p><span>Arik</span><br />
<span class="score" title="51 reputation points">51</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Arik has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-47209" class="comments-container">
&#10;</div>
<div id="comment-tools-47209" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47209-form-container" class="comment-form-container">
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

<span id="47217"></span>

<div id="answer-container-47217" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-47217-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47217-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-47217-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Arik has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you follow the instructions at: overpass-api.de/no_frills.html, "Software Installation" this will work on a Mac provided you build with: make CXXFLAGS="-O3" CPPFLAGS="-DNATIVE_LARGE_FILES"</p>
<p><em>Error: I still get an error saying "ld: library not found for -lrt" though. Is there a way to get around this?</em></p>
<p>Oh! I forgot that problem. This will happen about 6 times in the build. The way I worked around it is each time that make stops with this error, copy &amp; paste the last gcc command line (these spread over more than one line) and delete the "-lrt", then hit return. When it finishes, re-type "make CXXFLAGS="-O3" CPPFLAGS="-DNATIVE_LARGE_FILES"</p>
<p>BTW: We have an issue for this. Please follow up here: <a href="https://github.com/drolbr/Overpass-API/issues/216">https://github.com/drolbr/Overpass-API/issues/216</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Dec '15, 16:12</strong></p>
<img src="https://secure.gravatar.com/avatar/73a79b941319efb1c455368f7dcd2703?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="malcolmh&#39;s gravatar image" />
<p><span>malcolmh</span><br />
<span class="score" title="96 reputation points">96</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="malcolmh has one accepted answer">50%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Dec '15, 16:31</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/264d84ab05b942224b05960903eba7a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmd&#39;s gravatar image" />
<p><span>mmd</span><br />
<span class="score" title="5682 reputation points"><span>5.7k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="53 badges"><span class="silver">●</span><span class="badgecount">53</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span></p>
</div>
</div>
<div id="comments-container-47217" class="comments-container">
<span id="47231"></span>
<div id="comment-47231" class="comment">
<div id="post-47231-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Well, that's really only a workaround. Better would be to address this in <a href="https://github.com/drolbr/Overpass-API/blob/master/src/configure.ac#L21">https://github.com/drolbr/Overpass-API/blob/master/src/configure.ac#L21</a> and recreate the build environment. Result: no more manual fiddling. Anyone with a mac here who is brave enough to test this and update the github issue i mentioned? A patch could be similar to this one: <a href="http://lists.freedesktop.org/archives/mesa-commit/2013-February/041707.html">http://lists.freedesktop.org/archives/mesa-commit/2013-February/041707.html</a></p>
</div>
<div id="comment-47231-info" class="comment-info">
<span class="comment-age">(19 Dec '15, 09:58)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
<span id="47232"></span>
<div id="comment-47232" class="comment">
<div id="post-47232-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Tried it, same failure:</p>
<p>ld: library not found for -lrt clang: error: linker command failed with exit code 1 (use -v to see invocation) make[2]: <strong><em>[bin/osm3s_query] Error 1 make[1]:</em></strong> [all-recursive] Error 1 make: *** [all] Error 2</p>
</div>
<div id="comment-47232-info" class="comment-info">
<span class="comment-age">(19 Dec '15, 10:16)</span> <span class="comment-user userinfo">malcolmh</span>
</div>
</div>
<span id="47233"></span>
<div id="comment-47233" class="comment">
<div id="post-47233-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Did you also run autoscan, aclocal, autoheader, libtoolize, automake --add-missing, autoconf (see <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Installation#Installation">Installation option 2</a>) before running configure and make again?</p>
</div>
<div id="comment-47233-info" class="comment-info">
<span class="comment-age">(19 Dec '15, 10:54)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
<span id="47234"></span>
<div id="comment-47234" class="comment">
<div id="post-47234-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>No. These steps are not mentioned in the Installation page. I tried this (BTW, no libtoolize, but ran glibtoolize). Same failure.</p>
</div>
<div id="comment-47234-info" class="comment-info">
<span class="comment-age">(19 Dec '15, 11:32)</span> <span class="comment-user userinfo">malcolmh</span>
</div>
</div>
<span id="47240"></span>
<div id="comment-47240" class="comment">
<div id="post-47240-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>no_frills.html is targetting more the official releases. I recommend to check this <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Installation">Wiki page</a> as well.</p>
<p>Thanks to Travis CI I now have a working build on Mac OS X without any manual tweaks: <a href="https://travis-ci.org/mmd-osm/Overpass-API/builds/97856095">https://travis-ci.org/mmd-osm/Overpass-API/builds/97856095</a></p>
<p>Please retest with the changes described <a href="https://github.com/mmd-osm/Overpass-API/commit/bd091c081f3777dc42e4ad892e513afec03a8b09">here</a> - except for the .travis.yml maybe, which is only in <a href="https://github.com/mmd-osm/Overpass-API/tree/test754_osx">my branch</a>.</p>
</div>
<div id="comment-47240-info" class="comment-info">
<span class="comment-age">(19 Dec '15, 16:25)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
</div>
<div id="comment-tools-47217" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47217-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="82874"></span>

<div id="answer-container-82874" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82874-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82874-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82874-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hello, I found these links:<br />
<a href="https://github.com/sodascience/osmenrich_docker">https://github.com/sodascience/osmenrich_docker</a><br />
<a href="https://github.com/wiktorn/Overpass-API">https://github.com/wiktorn/Overpass-API</a></p>
<p>Hope this helps someone in the future.</p>
<p>Cheers</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Dec '21, 21:01</strong></p>
<img src="https://secure.gravatar.com/avatar/5bfcb2e9d3cd4816c85c6521762caabf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wobi&#39;s gravatar image" />
<p><span>wobi</span><br />
<span class="score" title="116 reputation points">116</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wobi has no accepted answers">0%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Dec '21, 21:02</strong> </span></p>
</div>
</div>
<div id="comments-container-82874" class="comments-container">
&#10;</div>
<div id="comment-tools-82874" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82874-form-container" class="comment-form-container">
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

