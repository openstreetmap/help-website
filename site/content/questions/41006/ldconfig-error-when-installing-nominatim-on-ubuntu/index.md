+++
type = "question"
title = "ldconfig error when installing nominatim on Ubuntu"
description = '''Due to a large amount of geocoding tasks (around 1,3 million queries only for Germany) I want to install Nominatim on my laptop for which I followed the official manual. I installed the required software without problems, however when installing Nominatim itself as follows ./configure make  I encoun...'''
date = "2015-02-14T10:44:00Z"
lastmod = "2015-02-14T10:44:00Z"
weight = 41006
keywords = [ "nominatim", "ubuntu" ]
aliases = [ "/questions/41006" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [ldconfig error when installing nominatim on Ubuntu](/questions/41006/ldconfig-error-when-installing-nominatim-on-ubuntu)

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
<span id="post-41006-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41006-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-41006-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Due to a large amount of geocoding tasks (around 1,3 million queries only for Germany) I want to install Nominatim on my laptop for which I followed the <a href="http://wiki.openstreetmap.org/wiki/Nominatim/Installation">official manual</a>. I installed the required software without problems, however when installing Nominatim itself as follows</p>
<pre><code>./configure
make</code></pre>
<p>I encounter the following error</p>
<pre><code>middle-pgsql.c:1660:39: error: format specifies type &#39;long&#39; but the argument has
  type &#39;unsigned int&#39; [-Werror,-Wformat]
                        size * 8, sizeof(osmid_t) * 8);
                                  ^~~~~~~~~~~~~~~~~~~
1 error generated.
make[2]: *** [middle-pgsql.o] Error 1
make[2]: Leaving directory `/home/jharvard/Nominatim/osm2pgsql&#39;
make[1]: *** [all] Error 2
make[1]: Leaving directory `/home/jharvard/Nominatim/osm2pgsql&#39;
make: *** [all-recursive] Error 1</code></pre>
<p>Though the configuration file runs smoothly, it shows the following warning that I don't know how to deal with. Can anybody help? Is that likely to be the cause?</p>
<pre><code>checking for libxml - version &gt;= 2.0.0... no
*** Could not run libxml test program, checking why...
*** The test program compiled, but did not run. This usually means
*** that the run-time linker is not finding LIBXML or finding the wrong
*** version of LIBXML. If it is not finding LIBXML, you&#39;ll need to set your
*** LD_LIBRARY_PATH environment variable, or edit /etc/ld.so.conf to point
*** to the installed location  Also, make sure you have run ldconfig if that
*** is required on your system
***
*** If you have an old version installed, it is best to remove it, although
*** you may also be able to get things to work by modifying LD_LIBRARY_PATH</code></pre>
<p>I am not sure how to deal with the path problem. Because I have properly installed the libxml2-dev package I do not suspect that this is causing the trouble. However, ldconfig seems not to be working. When running it using <code>sudo ldconfig</code> I get the error</p>
<pre><code>/sbin/ldconfig.real: /usr/lib/i386-linux-gnu/libzeitgeist-2.0.so.0 is not an ELF file - it has the wrong mahig bytes
/sbin/ldconfig.real: /usr/lib/i386-linux-gnu/libzeitgeist-2.0.so.0.0.0 is not an ELF file - it has the wrong mahig bytes</code></pre>
<p>I have a Mac (5 GB RAM) with Mac OS 10.10.2 Yosemite on which I am running Ubuntu 14.04.1 LTS (Release 14.04) using Virtual Box 4.3.22 (the Ubuntu distribution I am using is distributed for an edx course).</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-ubuntu" rel="tag" title="see questions tagged &#39;ubuntu&#39;">ubuntu</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Feb '15, 10:44</strong></p>
<img src="https://secure.gravatar.com/avatar/f1ac39ece091aedaeb2d8b0a48351daf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scoopert&#39;s gravatar image" />
<p><span>scoopert</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scoopert has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Feb '15, 10:49</strong> </span></p>
</div>
</div>
<div id="comments-container-41006" class="comments-container">
&#10;</div>
<div id="comment-tools-41006" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41006-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

