+++
type = "question"
title = "Getting Error While Installing Nominatim &quot;configure.ac:20: required file `config.h.in&#x27; not found&quot;"
description = '''Hi, I followed the instruction on the URL &quot;http://wiki.openstreetmap.org/wiki/Nominatim/Installation&quot; but while running ./autogen.sh I am getting the below mentioned error : autoreconf2.50: running: /usr/bin/autoconf --force autoreconf2.50: running: /usr/bin/autoheader --force autoreconf2.50: runnin...'''
date = "2012-09-18T16:36:00Z"
lastmod = "2012-09-24T09:38:00Z"
weight = 16223
keywords = [ "osm" ]
aliases = [ "/questions/16223" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Getting Error While Installing Nominatim "configure.ac:20: required file \`config.h.in' not found"](/questions/16223/getting-error-while-installing-nominatim-configureac20-required-file-confighin-not-found)

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
<span id="post-16223-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16223-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-16223-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I followed the instruction on the URL "http://wiki.openstreetmap.org/wiki/Nominatim/Installation" but while running ./autogen.sh I am getting the below mentioned error :</p>
<pre><code>autoreconf2.50: running: /usr/bin/autoconf --force
autoreconf2.50: running: /usr/bin/autoheader --force
autoreconf2.50: running: automake --add-missing --copy --force-missing
configure.ac:20: required file `config.h.in&#39; not found
autoreconf2.50: automake failed with exit status: 1</code></pre>
<p>Not sure what is the reason.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Sep '12, 16:36</strong></p>
<img src="https://secure.gravatar.com/avatar/92a98ebc8319176cebf47da5adb5c838?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pratap&#39;s gravatar image" />
<p><span>Pratap</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pratap has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-16223" class="comments-container">
<span id="16227"></span>
<div id="comment-16227" class="comment">
<div id="post-16227-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>What OS and version did this happen on?</p>
</div>
<div id="comment-16227-info" class="comment-info">
<span class="comment-age">(18 Sep '12, 19:01)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="16228"></span>
<div id="comment-16228" class="comment">
<div id="post-16228-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>root@localhost:/Nominatim# cat /etc/issue Debian GNU/Linux 6.0 \n \l</p>
<p>root@localhost:/Nominatim# uname -a Linux localhost 2.6.32-5-686 #1 SMP Sat May 5 01:33:08 UTC 2012 i686 GNU/Linux</p>
</div>
<div id="comment-16228-info" class="comment-info">
<span class="comment-age">(18 Sep '12, 19:17)</span> <span class="comment-user userinfo">Pratap</span>
</div>
</div>
<span id="16231"></span>
<div id="comment-16231" class="comment">
<div id="post-16231-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>there should be a config.h.in in the nominatim and in the osm2pgsql subdirectory. Are they there?</p>
</div>
<div id="comment-16231-info" class="comment-info">
<span class="comment-age">(18 Sep '12, 20:49)</span> <span class="comment-user userinfo">datendelphin</span>
</div>
</div>
<span id="16250"></span>
<div id="comment-16250" class="comment">
<div id="post-16250-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>No I do not see "config.h.in" under Nominatim and in the OSM2pgsql subdir too.</p>
<p>root@localhost:/var/www/Nominatim# find ./* -name config.h.in root@localhost:/var/www/Nominatim# locate config.h.in /usr/local/src/protobuf-2.4.1/config.h.in /usr/local/src/protobuf-2.4.1/gtest/build-aux/config.h.in</p>
</div>
<div id="comment-16250-info" class="comment-info">
<span class="comment-age">(19 Sep '12, 06:19)</span> <span class="comment-user userinfo">Pratap</span>
</div>
</div>
<span id="16407"></span>
<div id="comment-16407" class="comment">
<div id="post-16407-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>There seems to be no clue available for this issue. Also I tried copying the file config.h.in from the URL "https://trac.openstreetmap.org/browser/applications/utils/nominatim/nominatim/config.h.in" into my directory "/var/www/Nominatim/nominatim" but still getting the same error.</p>
</div>
<div id="comment-16407-info" class="comment-info">
<span class="comment-age">(24 Sep '12, 09:38)</span> <span class="comment-user userinfo">Pratap</span>
</div>
</div>
</div>
<div id="comment-tools-16223" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16223-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

