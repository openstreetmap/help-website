+++
type = "question"
title = "Nominatim installation problem: proj projection"
description = '''This is my first time to install Nominatim. Testing on centos6.5 parallels in mac. I have tried the earlier questions https://help.openstreetmap.org/questions/20326/nominatim-installation-not-finding-proj-headers, but this did not worked as its already installed.   [root@localhost Nominatim]# ./conf...'''
date = "2015-07-18T19:03:00Z"
lastmod = "2015-07-18T22:02:00Z"
weight = 44258
keywords = [ "projection" ]
aliases = [ "/questions/44258" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Nominatim installation problem: proj projection](/questions/44258/nominatim-installation-problem-proj-projection)

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
<span id="post-44258-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44258-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-44258-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>This is my first time to install Nominatim. Testing on centos6.5 parallels in mac. I have tried the earlier questions <a href="/questions/20326/nominatim-installation-not-finding-proj-headers,">https://help.openstreetmap.org/questions/20326/nominatim-installation-not-finding-proj-headers,</a> but this did not worked as its already installed.</p>
<hr />
<pre><code>    [root@localhost Nominatim]# ./configure
checking for a BSD-compatible install... /usr/bin/install -c
checking whether build environment is sane... yes
checking for a thread-safe mkdir -p... /bin/mkdir -p
checking for gawk... gawk
checking whether make sets $(MAKE)... yes
checking whether make supports nested variables... yes
checking for gcc... gcc
checking whether the C compiler works... yes
checking for C compiler default output file name... a.out
checking for suffix of executables... 
checking whether we are cross compiling... no
checking for suffix of object files... o
checking whether we are using the GNU C compiler... yes
checking whether gcc accepts -g... yes
checking for gcc option to accept ISO C89... none needed
checking whether gcc understands -c and -o together... yes
checking for style of include used by make... GNU
checking dependency style of gcc... gcc3
checking for g++... g++
checking whether we are using the GNU C++ compiler... yes
checking whether g++ accepts -g... yes
checking dependency style of g++... gcc3
checking build system type... x86_64-unknown-linux-gnu
checking host system type... x86_64-unknown-linux-gnu
checking for the pthreads library -lpthreads... no
checking whether pthreads work without any flags... no
checking whether pthreads work with -Kthread... no
checking whether pthreads work with -kthread... no
checking for the pthreads library -llthread... no
checking whether pthreads work with -pthread... yes
checking for joinable pthread attribute... PTHREAD_CREATE_JOINABLE
checking if more special flags are required for pthreads... no
checking how to run the C preprocessor... gcc -E
checking for grep that handles long lines and -e... /bin/grep
checking for egrep... /bin/grep -E
checking for ANSI C header files... yes
checking for sys/types.h... yes
checking for sys/stat.h... yes
checking for stdlib.h... yes
checking for string.h... yes
checking for memory.h... yes
checking for strings.h... yes
checking for inttypes.h... yes
checking for stdint.h... yes
checking for unistd.h... yes
checking for geos-config... /usr/bin/geos-config
checking for geos libraries... checking geos/version.h usability... yes
checking geos/version.h presence... yes
checking for geos/version.h... yes
yes
checking for proj projection library... no
configure: error: required library not found
[root@localhost Nominatim]#</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-projection" rel="tag" title="see questions tagged &#39;projection&#39;">projection</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Jul '15, 19:03</strong></p>
<img src="https://secure.gravatar.com/avatar/2463811d231d70c616bd07bdc0067395?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="arj123&#39;s gravatar image" />
<p><span>arj123</span><br />
<span class="score" title="46 reputation points">46</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="arj123 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Jul '15, 19:08</strong> </span></p>
</div>
</div>
<div id="comments-container-44258" class="comments-container">
<span id="44262"></span>
<div id="comment-44262" class="comment">
<div id="post-44262-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>What kind of Unix is this?</p>
</div>
<div id="comment-44262-info" class="comment-info">
<span class="comment-age">(18 Jul '15, 20:04)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="44264"></span>
<div id="comment-44264" class="comment">
<div id="post-44264-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>cent os 6.5</p>
</div>
<div id="comment-44264-info" class="comment-info">
<span class="comment-age">(18 Jul '15, 22:02)</span> <span class="comment-user userinfo">arj123</span>
</div>
</div>
</div>
<div id="comment-tools-44258" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44258-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

