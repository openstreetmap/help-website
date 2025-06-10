+++
type = "question"
title = "Error in mod_tile compile with centos 6.3 gcc 4.4.6"
description = '''I tried compiling the last version of mod_tile from svn (rev 28723) and I got this message: gen_tile.cpp: In function ‘void render_init(const char*, const char*, int)’: gen_tile.cpp:506: error: base operand of ‘-&amp;gt;’ has non-pointer type ‘mapnik::datasource_cache’  So I evidently changed the code t...'''
date = "2012-09-22T07:37:00Z"
lastmod = "2012-12-07T16:49:00Z"
weight = 16334
keywords = [ "compile", "gcc", "error", "mod_tile" ]
aliases = [ "/questions/16334" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Error in mod_tile compile with centos 6.3 gcc 4.4.6](/questions/16334/error-in-mod_tile-compile-with-centos-63-gcc-446)

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
<span id="post-16334-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16334-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-16334-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I tried compiling the last version of mod_tile from svn (rev 28723) and I got this message:</p>
<pre><code>gen_tile.cpp: In function ‘void render_init(const char*, const char*, int)’:
gen_tile.cpp:506: error: base operand of ‘-&gt;’ has non-pointer type ‘mapnik::datasource_cache’</code></pre>
<p>So I evidently changed the code to fix this, and I'm pretty sure I compiled the same version on a fedroa 17 box yesterday without any error. (May be a problem with gcc)</p>
<pre><code>Index: gen_tile.cpp
===================================================================
--- gen_tile.cpp    (revision 28723)
+++ gen_tile.cpp    (working copy)
@@ -503,7 +503,7 @@
 void render_init(const char *plugins_dir, const char* font_dir, int font_dir_recurse)
 {
     syslog(LOG_INFO, &quot;Renderd is using mapnik version %i.%i.%i&quot;, (MAPNIK_VERSION / 100000), ((MAPNIK_VERSION / 100) % 1000), (MAPNIK_VERSION % 100));
-    mapnik::datasource_cache::instance()-&gt;register_datasources(plugins_dir);
+    mapnik::datasource_cache::instance().register_datasources(plugins_dir);
     load_fonts(font_dir, font_dir_recurse);
 }</code></pre>
<p>I'm currently using Centos 6.3 kernel 2.6.32-279.5.2.el6.x86_64 with :</p>
<ul>
<li>gcc-gfortran-4.4.6-4.el6.x86_64</li>
<li>libgcc-4.4.6-4.el6.x86_64</li>
<li>gcc-c++-4.4.6-4.el6.x86_64</li>
<li>gcc-4.4.6-4.el6.x86_64</li>
</ul>
<p>I don't even know if it qualify as a problem ??</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-compile" rel="tag" title="see questions tagged &#39;compile&#39;">compile</span> <span class="post-tag tag-link-gcc" rel="tag" title="see questions tagged &#39;gcc&#39;">gcc</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span> <span class="post-tag tag-link-mod_tile" rel="tag" title="see questions tagged &#39;mod_tile&#39;">mod_tile</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Sep '12, 07:37</strong></p>
<img src="https://secure.gravatar.com/avatar/1ab55adc52980c7b0481e3bd89cd364f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chedi&#39;s gravatar image" />
<p><span>chedi</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chedi has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-16334" class="comments-container">
&#10;</div>
<div id="comment-tools-16334" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16334-form-container" class="comment-form-container">
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

<span id="16345"></span>

<div id="answer-container-16345" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-16345-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16345-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-16345-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It is not a problem with gcc, it depends on which version of Mapnik you're compiling with. Mapnik trunk (as of ~ 15 days ago) seems to require the above change, whereas older Mapnik versions don't.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Sep '12, 10:47</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-16345" class="comments-container">
<span id="18276"></span>
<div id="comment-18276" class="comment">
<div id="post-18276-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This has now been fixed in mod_tile svn revision 29051</p>
</div>
<div id="comment-18276-info" class="comment-info">
<span class="comment-age">(07 Dec '12, 16:49)</span> <span class="comment-user userinfo">apmon</span>
</div>
</div>
</div>
<div id="comment-tools-16345" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16345-form-container" class="comment-form-container">
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

