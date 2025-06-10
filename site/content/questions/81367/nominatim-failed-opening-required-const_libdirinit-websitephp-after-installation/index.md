+++
type = "question"
title = "nominatim: Failed opening required &#x27;CONST_LibDir/init-website.php&#x27; after installation"
description = '''Hi. I followed the installation instructions with a fresh debian 11. php version is 7.4.21. Here is my apache configuration: &amp;lt;VirtualHost *:80&amp;gt;  ServerName geo.domain.tld   &amp;lt;Directory &quot;/usr/local/lib/nominatim/lib-php/website/&quot;&amp;gt;  Options FollowSymLinks MultiViews  AddType text/html .php ...'''
date = "2021-08-19T13:37:00Z"
lastmod = "2021-08-19T17:56:00Z"
weight = 81367
keywords = [ "nominatim", "php" ]
aliases = [ "/questions/81367" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [nominatim: Failed opening required 'CONST_LibDir/init-website.php' after installation](/questions/81367/nominatim-failed-opening-required-const_libdirinit-websitephp-after-installation)

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
<span id="post-81367-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81367-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81367-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi. I followed <a href="https://nominatim.org/release-docs/latest/admin/Installation/">the installation instructions</a> with a fresh debian 11. php version is 7.4.21. Here is my apache configuration:</p>
<pre><code>&lt;VirtualHost *:80&gt;
    ServerName geo.domain.tld
&#10;    &lt;Directory &quot;/usr/local/lib/nominatim/lib-php/website/&quot;&gt;
        Options FollowSymLinks MultiViews
        AddType text/html   .php
        DirectoryIndex search.php
        Require all granted
    &lt;/Directory&gt;
&#10;    DocumentRoot /usr/local/lib/nominatim/lib-php/website/
&lt;/VirtualHost&gt;</code></pre>
<p>Here is the error log generated when trying to access the domain:</p>
<pre><code>[Thu Aug 19 14:26:42.482410 2021] [php7:warn] [pid 438204] [client ::1:34376] PHP Warning:  Use of undefined constant CONST_LibDir - assumed &#39;CONST_LibDir&#39; (this will throw an Error in a future version of PHP) in /usr/local/lib/nominatim/lib-php/website/search.php on line 3
[Thu Aug 19 14:26:42.482778 2021] [php7:warn] [pid 438204] [client ::1:34376] PHP Warning:  require_once(CONST_LibDir/init-website.php): failed to open stream: No such file or directory in /usr/local/lib/nominatim/lib-php/website/search.php on line 3
[Thu Aug 19 14:26:42.482792 2021] [php7:error] [pid 438204] [client ::1:34376] PHP Fatal error:  require_once(): Failed opening required &#39;CONST_LibDir/init-website.php&#39; (include_path=&#39;.:/usr/share/php&#39;) in /usr/local/lib/nominatim/lib-php/website/search.php on line 3</code></pre>
<p>Is there something wrong with my installation?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-php" rel="tag" title="see questions tagged &#39;php&#39;">php</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Aug '21, 13:37</strong></p>
<img src="https://secure.gravatar.com/avatar/55a66e99c10fe46b1cac78c236483c8c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="azmeuk&#39;s gravatar image" />
<p><span>azmeuk</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="azmeuk has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-81367" class="comments-container">
&#10;</div>
<div id="comment-tools-81367" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81367-form-container" class="comment-form-container">
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

<span id="81371"></span>

<div id="answer-container-81371" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-81371-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81371-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81371-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In the Apache configuration you need to use your project directory, e.g. <code>/srv/nominatim</code> (see <a href="https://www.nominatim.org/release-docs/3.7.2/admin/Deployment/#nominatim-with-apache).">https://www.nominatim.org/release-docs/3.7.2/admin/Deployment/#nominatim-with-apache).</a> In previous Nominatim versions that was called the "build" directory. It was created during the Nominatim setup already.</p>
<p>If you can't find <code>website/*.php</code> files in the project directory try running</p>
<p><code>nominatim refresh --website</code></p>
<p>in the project directory.</p>
<p>The <code>website/*.php</code> files in the project directory have various <code>@define('CONST_...</code> lines near the top, the files in <code>/usr/local/lib/nominatim/lib-php/website/</code> don't and the nominatim refresh adds those lines.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Aug '21, 17:56</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-81371" class="comments-container">
&#10;</div>
<div id="comment-tools-81371" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81371-form-container" class="comment-form-container">
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

