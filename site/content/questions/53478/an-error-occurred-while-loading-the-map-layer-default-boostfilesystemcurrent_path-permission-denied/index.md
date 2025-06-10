+++
type = "question"
title = ": An error occurred while loading the map layer &#x27;default&#x27;: boost::filesystem::current_path: Permission denied"
description = '''I have been trying to get renderd to run but I can&#x27;t get past this error: Dec 11 10:05:27 renderd[22885] &amp;lt;Debug&amp;gt;: DEBUG: Loading font: /opt/local/lib/mapnik/fonts/DejaVuSerifCondensed.ttf Dec 11 10:05:27 renderd[22885] &amp;lt;Debug&amp;gt;: DEBUG: Loading font: /opt/local/lib/mapnik/fonts/unifont-8.0...'''
date = "2016-12-11T12:25:00Z"
lastmod = "2016-12-13T14:51:00Z"
weight = 53478
keywords = [ "mac", "renderd" ]
aliases = [ "/questions/53478" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [: An error occurred while loading the map layer 'default': boost::filesystem::current_path: Permission denied](/questions/53478/an-error-occurred-while-loading-the-map-layer-default-boostfilesystemcurrent_path-permission-denied)

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
<span id="post-53478-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53478-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-53478-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have been trying to get renderd to run but I can't get past this error:</p>
<pre><code>Dec 11 10:05:27  renderd[22885] &lt;Debug&gt;: DEBUG: Loading font: /opt/local/lib/mapnik/fonts/DejaVuSerifCondensed.ttf
Dec 11 10:05:27  renderd[22885] &lt;Debug&gt;: DEBUG: Loading font: /opt/local/lib/mapnik/fonts/unifont-8.0.01.ttf
Running in foreground mode...
debug: init_storage_backend: initialising file storage backend at: /var/lib/mod_tile
Dec 11 10:05:27  renderd[22885] &lt;Debug&gt;: Starting stats thread
Dec 11 10:05:27  renderd[22885] &lt;Info&gt;: Loading parameterization function for 
debug: init_storage_backend: initialising file storage backend at: /var/lib/mod_tile
debug: init_storage_backend: initialising file storage backend at: /var/lib/mod_tile
Dec 11 10:05:27  renderd[22885] &lt;Info&gt;: Loading parameterization function for 
Dec 11 10:05:27  renderd[22885] &lt;Info&gt;: Loading parameterization function for 
debug: init_storage_backend: initialising file storage backend at: /var/lib/mod_tile
Dec 11 10:05:27  renderd[22885] &lt;Info&gt;: Loading parameterization function for 
Dec 11 10:05:27  renderd[22885] &lt;Error&gt;: An error occurred while loading the map layer &#39;default&#39;: boost::filesystem::current_path: Permission denied
Dec 11 10:05:27  renderd[22885] &lt;Error&gt;: An error occurred while loading the map layer &#39;default&#39;: boost::filesystem::current_path: Permission denied
Dec 11 10:05:27  renderd[22885] &lt;Error&gt;: An error occurred while loading the map layer &#39;default&#39;: boost::filesystem::current_path: Permission denied
Dec 11 10:05:27  renderd[22885] &lt;Error&gt;: An error occurred while loading the map layer &#39;default&#39;: boost::filesystem::current_path: Permission denied</code></pre>
<p>I have even tried to create the folder /var/lib/mod_tile/default, but no luck.</p>
<p>Any ideas?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-mac" rel="tag" title="see questions tagged &#39;mac&#39;">mac</span> <span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Dec '16, 12:25</strong></p>
<img src="https://secure.gravatar.com/avatar/085f049ba18dc20e7476dfba11554735?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Luke16&#39;s gravatar image" />
<p><span>Luke16</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Luke16 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Dec '16, 16:03</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-53478" class="comments-container">
<span id="53479"></span>
<div id="comment-53479" class="comment">
<div id="post-53479-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>What file permissions does /var/lib/mod_tile have currently and what user are you running the above as?</p>
</div>
<div id="comment-53479-info" class="comment-info">
<span class="comment-age">(11 Dec '16, 12:44)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="53483"></span>
<div id="comment-53483" class="comment">
<div id="post-53483-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>The folder and its underlying files and folders are owned by user postgres:</p>
<p>drwxr-xr-x 4 postgres wheel 136 Dec 11 10:04 mod_tile</p>
<p>drwxr-xr-x 2 postgres wheel 68 Dec 11 10:04 default</p>
<p>and the command is run as:</p>
<p>sudo -u postgres renderd -f -c /usr/local/etc/renderd.conf</p>
</div>
<div id="comment-53483-info" class="comment-info">
<span class="comment-age">(11 Dec '16, 16:55)</span> <span class="comment-user userinfo">Luke16</span>
</div>
</div>
</div>
<div id="comment-tools-53478" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53478-form-container" class="comment-form-container">
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

<span id="53492"></span>

<div id="answer-container-53492" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53492-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53492-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-53492-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Apparently some file or directory that renderd wants to access is not readable for the user you're running it under (the user "postgres", I gather from your comment above).</p>
<p>You can debug this further by installing (if not already present) the "strace" utility and then running</p>
<pre><code>sudo -u postgres
strace -o /tmp/strace.out -f renderd -f -c /usr/local/etc/renderd.conf</code></pre>
<p>this will log all system calls the program makes; before it aborts with the error message, you will likely see something that looks a bit like</p>
<pre><code>[12345] open(&quot;/some/file&quot;, O_WRONLY|O_CREAT|O_NOCTTY|O_NONBLOCK, 0666) = -1 EACCES (Permission denied)</code></pre>
<p>which then tells you which file or directory renderd tried to open and couldn't. Then fix permissions or ownership accordingly.</p>
<p>Note that not <em>all</em> errors in a <code>strace</code> output are necessarily a problem; in many situations a program might try to open one file and when that doesn't work, try something else.</p>
<p>A general comment on your running renderd under the "postgres" user: it would be better to create a new Unix user (eg "osm" or "renderd") to run renderd under and ensure that that user has access to the PostgreSQL database (eg <code>sudo -u postgres createuser -s renderd</code>).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Dec '16, 23:53</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-53492" class="comments-container">
<span id="53506"></span>
<div id="comment-53506" class="comment">
<div id="post-53506-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>It seems to be a problem with the database actually. This is a snippet of the dtruss (since strace is not available on macOS):</p>
<p>Dec 12 12:21:54 renderd[55477] &lt;error&gt;: An error occurred while loading the map layer 'default': Postgis Plugin: timeout expired Connection string: ' dbname=gis connect_timeout=4' encountered during parsing of layer 'landuse_gen0' in Layer of '/usr/local/share/maps/style/OSMBright/OSMBright.xml'</p>
<p>But I have no idea how to make sure if the script is able to access the database and/or check its DB connection configuration.</p>
<p>PS: I am aware that I should have created a user the task, but, for now, I want it to work first.</p>
</div>
<div id="comment-53506-info" class="comment-info">
<span class="comment-age">(12 Dec '16, 14:33)</span> <span class="comment-user userinfo">Luke16</span>
</div>
</div>
<span id="53528"></span>
<div id="comment-53528" class="comment">
<div id="post-53528-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>After a system restart it seems to have worked but now I can't get Apache2 to run the mod_tile module. It crashes.</p>
<p>When I built it from source I saw that it was pointing to the wrong installation of Apache2. It was using the /usr/libexec/apache2 and /usr/include/apache2. I thought that it would not interfere since I could just copy the mod_tile.so library to the correct running location of apache2.</p>
<p>How does it solve the path for the apache2 installation? How can I change it?</p>
<p>I have tried changing the order in the configure.ac file:</p>
<p>AC_CHECK_PROGS(APXS, /opt/local/apache2/bin/apxs , reject)</p>
<p>but then the ./configure won't complete.</p>
<p>checking for /opt/local/apache2/bin/apxs... no</p>
<p>even though it exists, is readable and executable by everyone.</p>
</div>
<div id="comment-53528-info" class="comment-info">
<span class="comment-age">(13 Dec '16, 10:02)</span> <span class="comment-user userinfo">Luke16</span>
</div>
</div>
<span id="53537"></span>
<div id="comment-53537" class="comment">
<div id="post-53537-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Finally!</p>
<p>The problem was really at the configure.ac file where the function AC_CHECK_PROGS just could not actually find the existing /opt/local/apache2/bin/apxs. Since /opt/local/bin is the first one on the $PATH, I had to pass ../apache2/bin/apxs as a parameter. Because, later on ../apache2/bin/apxs does not mean anything I also changed to the AC_CHECK_PROG function, which only accepts one parameter, but allows to return a different one as a result:</p>
<p>AC_CHECK_PROG(APXS, [../apache2/bin/apxs], [/opt/local/apache2/bin/apxs], reject)</p>
</div>
<div id="comment-53537-info" class="comment-info">
<span class="comment-age">(13 Dec '16, 14:51)</span> <span class="comment-user userinfo">Luke16</span>
</div>
</div>
</div>
<div id="comment-tools-53492" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53492-form-container" class="comment-form-container">
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

