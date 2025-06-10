+++
type = "question"
title = "Step by step installing Osmosis"
description = '''Hi there, sorry if my questions is so newbie and lame but i really need some help. I am using FreeBSD 9.1 and really want to install open street map. Osmosis. So this is my step :   1. installing PostgreeSQL   2. Installing OSM2PgSQL  3. Installing Mapnik  4. installing postgis everything run ok in ...'''
date = "2013-05-13T08:33:00Z"
lastmod = "2013-05-13T12:11:00Z"
weight = 22357
keywords = [ "osmosis" ]
aliases = [ "/questions/22357" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Step by step installing Osmosis](/questions/22357/step-by-step-installing-osmosis)

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
<span id="post-22357-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22357-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-22357-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi there, sorry if my questions is so newbie and lame but i really need some help. I am using FreeBSD 9.1 and really want to install open street map. Osmosis.</p>
<p>So this is my step : 1. installing PostgreeSQL 2. Installing OSM2PgSQL 3. Installing Mapnik 4. installing postgis</p>
<p>everything run ok in four step above. but when i tried to installing Mod Tile, i have so many error to compiling and make install. So many tutorial i've found but average the tutorial explain in Linux OS.</p>
<p>Really i need some help. The step by step installing Osmosis on FreeBSD (Unix) i really dont know how, because i am new in Open Street Map.</p>
<p>Thank You and I apologize for bad word.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 May '13, 08:33</strong></p>
<img src="https://secure.gravatar.com/avatar/7eac8f615876dfeca9c571aab03cf40f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rizvi&#39;s gravatar image" />
<p><span>Rizvi</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rizvi has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-22357" class="comments-container">
<span id="22359"></span>
<div id="comment-22359" class="comment">
<div id="post-22359-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You could try to show us your <em>first</em> error when running make.</p>
</div>
<div id="comment-22359-info" class="comment-info">
<span class="comment-age">(13 May '13, 09:43)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="22361"></span>
<div id="comment-22361" class="comment">
<div id="post-22361-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>when i try to "make" in mod_tile directory for installing, then a message appear: "Make : no target to make" Here, i just dunno what target, must i used to installing mod_tile. i am just already run "sh autogen.sh" in mod tile dir. but after that, i dunno what to do ?</p>
<p>Thank you for response scai.</p>
</div>
<div id="comment-22361-info" class="comment-info">
<span class="comment-age">(13 May '13, 10:09)</span> <span class="comment-user userinfo">Rizvi</span>
</div>
</div>
<span id="22362"></span>
<div id="comment-22362" class="comment not_top_scorer">
<div id="post-22362-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>According to your error message there is no file <em>Makefile</em> in your current directory. Did you run <em>autogen.sh</em> and <em>configure</em> as explained <a href="http://switch2osm.org/serving-tiles/manually-building-a-tile-server/">here</a>? If both commands succeed without problem then they should have generated a Makefile.</p>
</div>
<div id="comment-22362-info" class="comment-info">
<span class="comment-age">(13 May '13, 10:41)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="22363"></span>
<div id="comment-22363" class="comment">
<div id="post-22363-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks again scai. everything done in compiling but in the ends, the instalation got error. here is the message</p>
<pre><code>Stop in /usr/home/rizvi/mod_tile.
*** [all-recursive] Error code 1
&#10;Stop in /usr/home/rizvi/mod_tile.
*** [all] Error code 1
&#10;Stop in /usr/home/rizvi/mod_tile.</code></pre>
</div>
<div id="comment-22363-info" class="comment-info">
<span class="comment-age">(13 May '13, 10:54)</span> <span class="comment-user userinfo">Rizvi</span>
</div>
</div>
<span id="22365"></span>
<div id="comment-22365" class="comment">
<div id="post-22365-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>There must be at least one other error before. Always try to find and fix the first error. Subsequent errors are often just a consequence of the first error.</p>
</div>
<div id="comment-22365-info" class="comment-info">
<span class="comment-age">(13 May '13, 11:14)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="22367"></span>
<div id="comment-22367" class="comment not_top_scorer">
<div id="post-22367-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<pre><code>sudo apt-get install apache2 apache2-threaded-dev apache2-mpm-prefork apache2-utils libagg-dev</code></pre>
<p>are those mean, i need to install apache2, apache2-threaded-dev, apache2-mpm-prefork etc, before i installing mod tile. i guess, FreeBSD don't have a think like that.</p>
<p>i take that from the site you gave to me. thanks again, scai</p>
</div>
<div id="comment-22367-info" class="comment-info">
<span class="comment-age">(13 May '13, 12:02)</span> <span class="comment-user userinfo">Rizvi</span>
</div>
</div>
<span id="22369"></span>
<div id="comment-22369" class="comment">
<div id="post-22369-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Yes, <code>apt-get</code> is a Debian/Ubuntu command to install packages. Try to find the corresponding packages for FreeBSD. The names might be slightly different and some of those might be included in other packages etc.</p>
</div>
<div id="comment-22369-info" class="comment-info">
<span class="comment-age">(13 May '13, 12:11)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-22357" class="comment-tools">
<span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-22357-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

