+++
type = "question"
title = "Mapnik installation issue on centos 7"
description = '''Hi All,  I have been trying to setup osm on centos 7. I have been following this site https://github.com/lijenpan/osm/blob/master/osm-centos7.md. Most of the steps like installing postgres, boost c++ library I did had issue I managed to resolve them too.   I am stucked at here git clone git://github...'''
date = "2017-06-05T19:30:00Z"
lastmod = "2017-06-06T21:00:00Z"
weight = 56456
keywords = [ "mapnik" ]
aliases = [ "/questions/56456" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Mapnik installation issue on centos 7](/questions/56456/mapnik-installation-issue-on-centos-7)

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
<span id="post-56456-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56456-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-56456-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi All, I have been trying to setup osm on centos 7. I have been following this site <a href="https://github.com/lijenpan/osm/blob/master/osm-centos7.md.">https://github.com/lijenpan/osm/blob/master/osm-centos7.md.</a> Most of the steps like installing postgres, boost c++ library I did had issue I managed to resolve them too. I am stucked at here git clone <span>git://github.com/mapnik/mapnik</span></p>
<pre><code>&gt; cd maplink ./configure I got the
&gt; following errors. ./configure scons:
&gt; Reading SConscript files ...
&#10;Welcome to Mapnik...
&#10;Configuring build environment...
Configuring on Linux in *release mode*...
CXX c++ (GCC) 4.8.5 20150623 (Red Hat 4.8.5-11)
Copyright (C) 2015 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
Checking for freetype-config... yes
Checking for dlfcn.h support ... no
Checking if compiler (c++) supports -std=c++14 flag... (cached) no
C++ compiler does not support C++14 standard (-std=c++14), which is required. Please upgrade your compiler
[root@localhost mapnik]# gcc --version
gcc (GCC) 4.8.5 20150623 (Red Hat 4.8.5-11)
Copyright (C) 2015 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</code></pre>
<p>Then I google and manually download the latest release candidate and ran the ./configure command but I end up with different set of errors.</p>
<p>Could not find required header files for boost python Checking for pkg-config... yes Checking for pycairo... yes</p>
<p>Exiting... the following required dependencies were not found: - ltdl (GNU Libtool | more info: <a href="http://www.gnu.org/software/libtool)">http://www.gnu.org/software/libtool)</a> - boost version &gt;=1.47 (more info see: <a href="https://github.com/mapnik/mapnik/wiki//MapnikInstallation">https://github.com/mapnik/mapnik/wiki//MapnikInstallation</a> &amp; <a href="http://www.boost.org">http://www.boost.org</a>) - boost system (more info see: <a href="https://github.com/mapnik/mapnik/wiki//MapnikInstallation">https://github.com/mapnik/mapnik/wiki//MapnikInstallation</a> &amp; <a href="http://www.boost.org">http://www.boost.org</a>) - boost filesystem (more info see: <a href="https://github.com/mapnik/mapnik/wiki//MapnikInstallation">https://github.com/mapnik/mapnik/wiki//MapnikInstallation</a> &amp; <a href="http://www.boost.org">http://www.boost.org</a>) - boost regex (more info see: <a href="https://github.com/mapnik/mapnik/wiki//MapnikInstallation">https://github.com/mapnik/mapnik/wiki//MapnikInstallation</a> &amp; <a href="http://www.boost.org">http://www.boost.org</a>) - boost thread (more info see: <a href="https://github.com/mapnik/mapnik/wiki//MapnikInstallation">https://github.com/mapnik/mapnik/wiki//MapnikInstallation</a> &amp; <a href="http://www.boost.org">http://www.boost.org</a>) - boost python (more info see: <a href="https://github.com/mapnik/mapnik/wiki//MapnikInstallation">https://github.com/mapnik/mapnik/wiki//MapnikInstallation</a> &amp; <a href="http://www.boost.org">http://www.boost.org</a>)</p>
<p>See '/usr/local/mapnik-v2.1.0rc2/config.log' for details on possible problems.</p>
<p>I tried to run yum install libtool-ltdl but it says already installed.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Jun '17, 19:30</strong></p>
<img src="https://secure.gravatar.com/avatar/26750873415fcbe30ebf2fdeab499d99?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="newbie14&#39;s gravatar image" />
<p><span>newbie14</span><br />
<span class="score" title="31 reputation points">31</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="newbie14 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-56456" class="comments-container">
<span id="56463"></span>
<div id="comment-56463" class="comment">
<div id="post-56463-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Similar issue: <a href="https://github.com/mapnik/mapnik/issues/3591">https://github.com/mapnik/mapnik/issues/3591</a> . You need to update your compiler. Maybe there are third-party gcc packages with newer versions for CentOS available?</p>
</div>
<div id="comment-56463-info" class="comment-info">
<span class="comment-age">(06 Jun '17, 09:00)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="56464"></span>
<div id="comment-56464" class="comment">
<div id="post-56464-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>See also this forum thread: <a href="https://forum.openstreetmap.org/viewtopic.php?id=58594">https://forum.openstreetmap.org/viewtopic.php?id=58594</a></p>
</div>
<div id="comment-56464-info" class="comment-info">
<span class="comment-age">(06 Jun '17, 09:08)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="56467"></span>
<div id="comment-56467" class="comment">
<div id="post-56467-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/158/scai">@scai</a> I have run yum update yet the same what else should I do with the gcc?</p>
</div>
<div id="comment-56467-info" class="comment-info">
<span class="comment-age">(06 Jun '17, 15:18)</span> <span class="comment-user userinfo">newbie14</span>
</div>
</div>
</div>
<div id="comment-tools-56456" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56456-form-container" class="comment-form-container">
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

<span id="56469"></span>

<div id="answer-container-56469" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56469-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56469-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-56469-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="newbie14 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It sounds like you have a couple of options on Centos:</p>
<ol>
<li>Ask someone who's familiar with Centos how to install gcc 6 (and manually set clang if necessary, as per <a href="https://github.com/mapnik/mapnik/issues/3591#issuecomment-299469997">https://github.com/mapnik/mapnik/issues/3591#issuecomment-299469997</a> ) and try that.</li>
<li>Try an earlier version of mapnik, and use a map style that doesn't depend on very recent mapnik features. "OSM Bright" in the "lijenpan" instructions will likely work with an earlier mapnik.</li>
</ol>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Jun '17, 15:42</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-56469" class="comments-container">
<span id="56480"></span>
<div id="comment-56480" class="comment">
<div id="post-56480-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I found a better link as most steps in here works <a href="http://qiita.com/nkmrtkhd/items/642ae1b8a996cc46d85c">http://qiita.com/nkmrtkhd/items/642ae1b8a996cc46d85c</a></p>
</div>
<div id="comment-56480-info" class="comment-info">
<span class="comment-age">(06 Jun '17, 20:38)</span> <span class="comment-user userinfo">newbie14</span>
</div>
</div>
<span id="56481"></span>
<div id="comment-56481" class="comment">
<div id="post-56481-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>OK, so that's using the 2.3 branch of Mapnik and osm-bright.</p>
</div>
<div id="comment-56481-info" class="comment-info">
<span class="comment-age">(06 Jun '17, 21:00)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-56469" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56469-form-container" class="comment-form-container">
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

