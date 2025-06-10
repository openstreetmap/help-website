+++
type = "question"
title = "Configuration apache2 webserver nominatim"
description = '''Hello, I have a question about where this instruction is placed in which directory or file? Webserver setup The website/ directory in the build directory contains the configured website. Include the directory into your webbrowser to serve php files from there. Configure for use with Apache Make sure...'''
date = "2020-05-15T19:54:00Z"
lastmod = "2020-05-16T00:54:00Z"
weight = 74839
keywords = [ "website", "webserver", "nominatim", "apache2" ]
aliases = [ "/questions/74839" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Configuration apache2 webserver nominatim](/questions/74839/configuration-apache2-webserver-nominatim)

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
<span id="post-74839-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74839-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74839-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, I have a question about where this instruction is placed in which directory or file? Webserver setup The website/ directory in the build directory contains the configured website. Include the directory into your webbrowser to serve php files from there.</p>
<p>Configure for use with Apache Make sure your Apache configuration contains the required permissions for the directory and create an alias:</p>
<p><img src="https://help.openstreetmap.org/upfiles/website.png" alt="alt text" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-website" rel="tag" title="see questions tagged &#39;website&#39;">website</span> <span class="post-tag tag-link-webserver" rel="tag" title="see questions tagged &#39;webserver&#39;">webserver</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-apache2" rel="tag" title="see questions tagged &#39;apache2&#39;">apache2</span>
</div>
<div id="question-controls" class="post-controls">
<div class="community-wiki">
This question is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 May '20, 19:54</strong></p>
<img src="https://secure.gravatar.com/avatar/224322734ba5aec7f8c1b96e32946ca1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="edderantonio&#39;s gravatar image" />
<p><span>edderantonio</span><br />
<span class="score" title="11 reputation points">11</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="edderantonio has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-74839" class="comments-container">
&#10;</div>
<div id="comment-tools-74839" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74839-form-container" class="comment-form-container">
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

<span id="74840"></span>

<div id="answer-container-74840" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74840-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74840-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-74840-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This kind of depends on your Apache setup. On Ubuntu or Debian machines, you will typically have a directory <code>/etc/apache2/sites-available</code> and in it files for every virtual host (or if you're not using any virtual hosts, you could use the 000-default file). Place the code from the Nominatim docs inside the <code>&lt;Virtualhost&gt;</code> block.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 May '20, 20:17</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 May '20, 20:17</strong> </span></p>
</div>
</div>
<div id="comments-container-74840" class="comments-container">
<span id="74842"></span>
<div id="comment-74842" class="comment">
<div id="post-74842-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I appreciate the answer, but these two instructions come in the nomination documentation:</p>
<p>1.- Configure Apache web server You must create an alias for the website directory in your apache configuration. Add a separate nominatim configuration to your web server: sudo tee /etc/apache2/conf-available/nominatim.conf &lt;&lt; EOFAPACHECONF &lt;directory "$userhome="" nominatim="" build="" website"=""&gt; Options FollowSymLinks MultiViews AddType text/html .php DirectoryIndex search.php Require all granted &lt;/directory&gt;</p>
<p>Alias /nominatim $USERHOME/Nominatim/build/website EOFAPACHECONF</p>
<p>2.- Web server configuration The website / directory in the build directory contains the configured website. Include the directory in your web browser to serve php files from there.</p>
<p>Configure for use with Apache Make sure your Apache configuration contains the necessary permissions for the directory and create an alias:</p>
<p>&lt;directory "="" srv="" nominatim="" build="" website"=""&gt; Options FollowSymLinks MultiViews AddType text/html .php DirectoryIndex search.php Require all granted &lt;/directory&gt; Alias /nominatim /srv/nominatim/build/website</p>
<p>the second instruction is the one I don't know where it is placed</p>
</div>
<div id="comment-74842-info" class="comment-info">
<span class="comment-age">(15 May '20, 20:41)</span> <span class="comment-user userinfo">edderantonio</span>
</div>
</div>
</div>
<div id="comment-tools-74840" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74840-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="74841"></span>

<div id="answer-container-74841" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74841-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74841-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74841-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I appreciate the answer, but these two instructions come in the nomination documentation:</p>
<p>1.- Configure Apache web server You must create an alias for the website directory in your apache configuration. Add a separate nominatim configuration to your web server:</p>
<p><img src="https://help.openstreetmap.org/upfiles/settings.png" alt="alt text" /></p>
<p>2.- Web server configuration The website / directory in the build directory contains the configured website. Include the directory in your web browser to serve php files from there.</p>
<p>Configure for use with Apache Make sure your Apache configuration contains the necessary permissions for the directory and create an alias:</p>
<p><img src="https://help.openstreetmap.org/upfiles/webserver.png" alt="alt text" /></p>
<p>the second instruction is the one I don't know where it is placed</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 May '20, 20:39</strong></p>
<img src="https://secure.gravatar.com/avatar/224322734ba5aec7f8c1b96e32946ca1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="edderantonio&#39;s gravatar image" />
<p><span>edderantonio</span><br />
<span class="score" title="11 reputation points">11</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="edderantonio has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-74841" class="comments-container">
<span id="74848"></span>
<div id="comment-74848" class="comment">
<div id="post-74848-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The second configuration goes into the file <code>/etc/apache2/conf-available/nominatim.conf</code>. It's the same as the first only $USERNAME is replaced by '/src/nominatim'. Then run the command <code>sudo a2enconf nominatim</code>. This will create a symlink with the same filename into the directory <code>/etc/apache2/conf-enabled/</code>. Next run <code>sudo systemctl restart apache2</code>. This will start the Apache webserver. Now you should see the website on 'http://localhost/nominatim/search.php'. Check the Apache logfile, usually <code>/var/log/apache2/error.log</code> for errors. If the file '/etc/apache2/ports.conf' lists a different port, e.g. 9999, then the URL would be 'http://localhost:9999/nominatim/search.php' Replace 'localhost' by the IP address of the server when accessing from a browser.</p>
</div>
<div id="comment-74848-info" class="comment-info">
<span class="comment-age">(16 May '20, 00:54)</span> <span class="comment-user userinfo">mtmail</span>
</div>
</div>
</div>
<div id="comment-tools-74841" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74841-form-container" class="comment-form-container">
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

