+++
type = "question"
title = "How to restrict access to the tile server?"
description = '''This question has been asked before and was answered with (paraphrasing): &quot;This is not a OSM specific matter. This is an Apache issue. Restrict access in the way you would normally do for Apache.&quot; Fair enough, tried that. I can restrict access to files on the server but I can&#x27;t restrict access to th...'''
date = "2014-05-31T14:59:00Z"
lastmod = "2014-06-02T00:32:00Z"
weight = 33582
keywords = [ "apache", "access", "mod_tile", "tileserver" ]
aliases = [ "/questions/33582" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to restrict access to the tile server?](/questions/33582/how-to-restrict-access-to-the-tile-server)

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
<span id="post-33582-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33582-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-33582-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>This question has been asked before and was answered with (paraphrasing): "This is not a OSM specific matter. This is an Apache issue. Restrict access in the way you would normally do for Apache."</p>
<p>Fair enough, tried that. I can restrict access to files on the server but I can't restrict access to the map tiles (e.g. <a href="http://example.com/osm/10/503/344.png).">http://example.com/osm/10/503/344.png).</a></p>
<p>I have a dynamic tile server with mapnik, mod_tile and renderd.</p>
<p>I think this might be a mod_tile specific issue, hence asking here.</p>
<p>Initially I wanted to restrict access by only allowing requests where a referer was set and was from the site I have the map on. Using normal Apache allow/deny rules it didn't work. From a different site I could still access the tile server and display the tiles (these were freshly rendered tiles on areas and zooms on the map I hadn't been to before and confirmed this by running "top" in a SSH window and could see renderd and postgres running every time I went to a new area of the map).</p>
<p>For testing (and out of frustration) I simplified it and tried to block <em>all</em> access to the tile files. In /etc/apache2/sites-available/tileserver_site tried this:</p>
<p>&lt;Directory /var/www/&gt;<br />
AllowOverride None<br />
Order deny,allow<br />
Deny from all<br />
&lt;/Directory&gt;</p>
<p>Worked great for any files that were in /var/www/ got "Forbidden" as expected, but was still able to access the tiles.</p>
<p>Okay, so the tiles aren't actually in /var/www/ they are in /var/lib/mod_tile/, so tried this:</p>
<p>&lt;Directory /var/lib/mod_tile/&gt;<br />
AllowOverride None<br />
Order deny,allow<br />
Deny from all<br />
&lt;/Directory&gt;</p>
<p>...could still access the tiles.</p>
<p>Even tried:</p>
<p>&lt;Directory /&gt;<br />
AllowOverride None<br />
Order deny,allow<br />
Deny from all<br />
&lt;/Directory&gt;</p>
<p>...could still access the tiles! Apache and mod_tile apparently working away merrily, regardless of the access rules!</p>
<p>Anyone know how to restrict access to the tiles?</p>
<p>Thank you.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-apache" rel="tag" title="see questions tagged &#39;apache&#39;">apache</span> <span class="post-tag tag-link-access" rel="tag" title="see questions tagged &#39;access&#39;">access</span> <span class="post-tag tag-link-mod_tile" rel="tag" title="see questions tagged &#39;mod_tile&#39;">mod_tile</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 May '14, 14:59</strong></p>
<img src="https://secure.gravatar.com/avatar/11e6e819b91b4d177c249c5123d2fa15?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Charles%20Sweeney&#39;s gravatar image" />
<p><span>Charles Sweeney</span><br />
<span class="score" title="101 reputation points">101</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Charles Sweeney has no accepted answers">0%</span> </br></br></p>
</div>
</div>
<div id="comments-container-33582" class="comments-container">
&#10;</div>
<div id="comment-tools-33582" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33582-form-container" class="comment-form-container">
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

<span id="33609"></span>

<div id="answer-container-33609" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-33609-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33609-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-33609-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Fixed it.</p>
<p>To restrict access to your tile server from sites other than your own, put this in your Apache config file:</p>
<p>&lt;Location /&gt;<br />
SetEnvIf Referer example\.com localreferer<br />
Order deny,allow<br />
Deny from all<br />
Allow from env=localreferer<br />
&lt;/Location&gt;</p>
<p>--</p>
<p>&lt;Location&gt; is the key. You can't use &lt;Directory&gt; because the directory where the tiles are kept (/var/lib/mod_tile/) is outside the document root for the virtualhost that is the tileserver so any rules in your Apache config won't apply there. &lt;Location&gt; on the other hand doesn't apply to the filesystem it applies to the URL. So in the above example &lt;Location /&gt; applies to any URL requested on the tile server.</p>
<p>Replace example\.com with the name of your website. Remember to escape dots with a backslash.</p>
<p>The above code will probably work in any of the many Apache config files used in Apache2. I tried it in the master /etc/apache2/apache2.conf and it worked sweetly there, so left it as it was. I put it in before any of the includes were called.</p>
<p>The code works by checking the referer of the request. If it matches your site, access is granted, otherwise it's denied. If a referer isn't set, access will be denied. Every browser by default sends the referer so in practice this shouldn't give any problems.</p>
<p>Remember to restart Apache after editing the config file:</p>
<p>/etc/init.d/apache2 restart</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Jun '14, 00:32</strong></p>
<img src="https://secure.gravatar.com/avatar/11e6e819b91b4d177c249c5123d2fa15?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Charles%20Sweeney&#39;s gravatar image" />
<p><span>Charles Sweeney</span><br />
<span class="score" title="101 reputation points">101</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Charles Sweeney has no accepted answers">0%</span> </br></br></p>
</div>
</div>
<div id="comments-container-33609" class="comments-container">
&#10;</div>
<div id="comment-tools-33609" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33609-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="33583"></span>

<div id="answer-container-33583" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-33583-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33583-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-33583-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You should really ask this question in a place with Apache experts; it really is not an OpenStreetMap specific question, and the solution might depend on a couple of factors like for example your Apache version.</p>
<p>I am a bit curious how you used allow/deny rules to restrict requests to a specific referer.</p>
<p>A common way to deal with the problem is to rewrite requests that do not match a condition, for example with rules like this:</p>
<pre><code>RewriteCond %{HTTP_REFERER} !^http://mypage.com/myurl.html$
RewriteRule ^/.*png$ /somewhere/on/disk/notallowed.png</code></pre>
<p>This will of course require mod_rewrite and <code>RewriteEngine On</code>.</p>
<p>I have seen setups where the order of loading modules actually had an impact on whether and how this worked. But really, even though mod_tile is involved, nothing about this is OSM specific; from Apache's view, mod_tile is just like any other content-serving module.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 May '14, 15:26</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span> </br></br></p>
</div>
</div>
<div id="comments-container-33583" class="comments-container">
<span id="33585"></span>
<div id="comment-33585" class="comment">
<div id="post-33585-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Thanks Frederik.</p>
<p>I figured OSM people would know more about mod_tile/renderd than Apache people. If I ask Apache people the first thing they will ask is "What is mod_tile?", "What is renderd?". You would need to know how they worked and how they were set up to know why the normal Apache rules weren't applying to them.</p>
<p>I was going to post some code for restricting based on referer but I'm new to this board and can't preview it in the "comment" section and feared it might come out goofy as it does in the main text box unless I use HTML entities on it. Plus was limited on characters.</p>
</div>
<div id="comment-33585-info" class="comment-info">
<span class="comment-age">(31 May '14, 15:58)</span> <span class="comment-user userinfo">Charles Sweeney</span>
</div>
</div>
</div>
<div id="comment-tools-33583" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33583-form-container" class="comment-form-container">
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

