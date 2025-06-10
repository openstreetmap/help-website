+++
type = "question"
title = "[closed] Overpass API 403 Error in Apache"
description = '''I&#x27;m trying to install the overpass api as a web server with apache but I cannot access the interpreter from an http request.  Overpass API Install Here is my 000-default.conf &amp;lt;VirtualHost *:80&amp;gt; ServerAdmin webmaster@localhost ExtFilterDefine gzip mode=output cmd=/bin/gzip DocumentRoot /root/os...'''
date = "2014-05-27T22:05:00Z"
lastmod = "2015-07-24T19:21:00Z"
weight = 33517
keywords = [ "apache", "overpass", "api", "error" ]
aliases = [ "/questions/33517" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] Overpass API 403 Error in Apache](/questions/33517/overpass-api-403-error-in-apache)

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
<span id="post-33517-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33517-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-33517-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm trying to install the overpass api as a web server with apache but I cannot access the interpreter from an http request. <a href="http://wiki.openstreetmap.org/wiki/Overpass_API/install">Overpass API Install</a></p>
<p>Here is my 000-default.conf</p>
<pre><code>&lt;VirtualHost *:80&gt;
ServerAdmin webmaster@localhost
ExtFilterDefine gzip mode=output cmd=/bin/gzip
DocumentRoot /root/osm-3s_v0.7.4/html
&#10;# This directive indicates that whenever someone types http://www.mydomain.com/api/ 
# Apache2 should refer to what is in the local directory [YOUR_EXEC_DIR]/cgi-bin/
ScriptAlias /api/ /srv/osm3s/cgi-bin/
&#10;# This specifies some directives specific to the directory: [YOUR_EXEC_DIR]/cgi-bin/
&lt;Directory &quot;/srv/osm3s/cgi-bin/&quot;&gt;
            AllowOverride None
            Options +ExecCGI -MultiViews +SymLinksIfOwnerMatch
            Order allow,deny
            Allow from all
            #SetOutputFilter gzip
            #Header set Content-Encoding gzip
&lt;/Directory&gt;
&#10;ErrorLog /var/log/apache2/error.log
&#10;# Possible values include: debug, info, notice, warn, error, crit, alert, emerg
LogLevel warn
&#10;CustomLog /var/log/apache2/access.log combined</code></pre>
<p>However when I try to run the command:</p>
<pre><code>http://175.33.148.57/api/interpreter?data=%3Cprint%20mode=%22body%22/%3E</code></pre>
<p>I get the 403 Forbidden error.</p>
<p>I have already done</p>
<pre><code>chmod 777 /srv/osm3s/cgi-bin/</code></pre>
<p>But nothing seems to work.</p>
<p>Please help, Ive been stuck on this for 3 days now! Thanks in advance.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-apache" rel="tag" title="see questions tagged &#39;apache&#39;">apache</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 May '14, 22:05</strong></p>
<img src="https://secure.gravatar.com/avatar/5abb2932327bb97ee8a2abc3c14caa8c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gmeister4&#39;s gravatar image" />
<p><span>gmeister4</span><br />
<span class="score" title="60 reputation points">60</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gmeister4 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>24 Jul '15, 19:22</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/264d84ab05b942224b05960903eba7a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmd&#39;s gravatar image" />
<p><span>mmd</span><br />
<span class="score" title="5682 reputation points"><span>5.7k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="53 badges"><span class="silver">●</span><span class="badgecount">53</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span></p>
</div>
</div>
<div id="comments-container-33517" class="comments-container">
<span id="44199"></span>
<div id="comment-44199" class="comment">
<div id="post-44199-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Is there a solution for this? I've also found this post at <a href="http://stackoverflow.com/questions/23898866/apache-2-4-7-403-forbidden-error">stackoverflow</a> but none of the answers fixed it for me.</p>
<p>(I'm using CentOS, Apache/2.2.15 and I tried all possible solutions from this answers including moving installation to /var/www/osm/)</p>
</div>
<div id="comment-44199-info" class="comment-info">
<span class="comment-age">(15 Jul '15, 11:52)</span> <span class="comment-user userinfo">PhilHamm</span>
</div>
</div>
<span id="44415"></span>
<div id="comment-44415" class="comment">
<div id="post-44415-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Follow-up is here: <a href="http://gis.19327.n5.nabble.com/Apache-Permission-Error-tc5850534.html">http://gis.19327.n5.nabble.com/Apache-Permission-Error-tc5850534.html</a> - I close this one.</p>
</div>
<div id="comment-44415-info" class="comment-info">
<span class="comment-age">(24 Jul '15, 19:21)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
</div>
<div id="comment-tools-33517" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33517-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Issue is now handled on Overpass API development list." by mmd 24 Jul '15, 19:22

</div>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44249"></span>

<div id="answer-container-44249" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-44249-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44249-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-44249-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>meanwhile we have a mailinglist for overpassAPI:</p>
<p><a href="http://gis.19327.n5.nabble.com/Overpass-API-Development-f5839267.html">http://gis.19327.n5.nabble.com/Overpass-API-Development-f5839267.html</a></p>
<p>try to ask there.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Jul '15, 10:17</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-44249" class="comments-container">
&#10;</div>
<div id="comment-tools-44249" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44249-form-container" class="comment-form-container">
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

