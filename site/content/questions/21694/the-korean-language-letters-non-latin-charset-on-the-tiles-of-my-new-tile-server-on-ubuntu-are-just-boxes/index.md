+++
type = "question"
title = "The Korean language letters (non-latin charset) on the tiles of my new tile server on ubuntu are just boxes"
description = '''hello   I installed osm on my Ubuntu server, as shown in the photo below. The Korean language, Hangul, however, retrieve broken. I faithfully as a guide, but many times, even if you tried any of these symptoms appear. The procedure below.(Very simple)  sudo add-apt-repository ppa:kakrueger/openstree...'''
date = "2013-04-22T03:40:00Z"
lastmod = "2013-04-30T02:30:00Z"
weight = 21694
keywords = [ "charset", "tile-server", "ubuntu" ]
aliases = [ "/questions/21694" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [The Korean language letters (non-latin charset) on the tiles of my new tile server on ubuntu are just boxes](/questions/21694/the-korean-language-letters-non-latin-charset-on-the-tiles-of-my-new-tile-server-on-ubuntu-are-just-boxes)

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
<span id="post-21694-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21694-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-21694-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>hello</p>
<p><img src="http://ruby.pe.kr/1.png" alt="alt text" /></p>
<p>I installed osm on my Ubuntu server, as shown in the photo below. The Korean language, Hangul, however, retrieve broken.</p>
<p>I faithfully as a guide, but many times, even if you tried any of these symptoms appear.</p>
<h2 id="the-procedure-below.very-simple">The procedure below.(Very simple)</h2>
<ol>
<li>sudo add-apt-repository ppa:kakrueger/openstreetmap</li>
<li>sudo apt-get update</li>
<li>sudo apt-get install libapache2-mod-tile</li>
<li>wget <a href="http://download.geofabrik.de/openstreetmap/europe/ireland.osm.pbf">http://download.geofabrik.de/openstreetmap/europe/ireland.osm.pbf</a></li>
</ol>
<p>·</p>
<ul>
<li>sudo su - postgres</li>
<li>createdb osm</li>
<li>createlang plpgsql osm</li>
<li>createuser &lt;username&gt;</li>
</ul>
<p>·5. osm2pgsql --slim -C 1500 ireland.osm.pbf</p>
<p>·6. restart …</p>
<hr />
<h2 id="below-is-the-result-of-my-test.">Below is the result of my test.</h2>
<ol>
<li>create test.php -&gt; &lt;? echo("대한민국"); ?&gt; OK</li>
<li>login psql -&gt; show clinet encoding? OK - UTF-8</li>
<li>PHP-CHARSET : line comment -&gt; UTF-8<br />
</li>
<li>using josm, open the character map check OK</li>
</ol>
<hr />
<p>What is the problem?....... bohoo....</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-charset" rel="tag" title="see questions tagged &#39;charset&#39;">charset</span> <span class="post-tag tag-link-tile-server" rel="tag" title="see questions tagged &#39;tile-server&#39;">tile-server</span> <span class="post-tag tag-link-ubuntu" rel="tag" title="see questions tagged &#39;ubuntu&#39;">ubuntu</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Apr '13, 03:40</strong></p>
<img src="https://secure.gravatar.com/avatar/d6e5f1c6e6f0ffac4430f3fe7d2fd1a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sgGold&#39;s gravatar image" />
<p><span>sgGold</span><br />
<span class="score" title="15 reputation points">15</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sgGold has no accepted answers">0%</span> </br></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Apr '13, 01:05</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-21694" class="comments-container">
&#10;</div>
<div id="comment-tools-21694" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21694-form-container" class="comment-form-container">
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

<span id="21704"></span>

<div id="answer-container-21704" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-21704-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21704-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-21704-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Make sure that you have the "unifont" font installed (<code>sudo apt-get install ttf-unifont</code>) and that your fontset-settings.inc file correctly references the "unifont Medium" font.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Apr '13, 09:58</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-21704" class="comments-container">
<span id="21709"></span>
<div id="comment-21709" class="comment">
<div id="post-21709-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thank you for answer. I as directed, using the command "sudo apt-get install ttf-unifont" The installation finished successfully, reboot.</p>
<p>Sadly, the result was the same. , "Fontset-settings.xml" I open the file but it was in the set. You, the font is installed correctly, there should not?</p>
<hr />
<p>mtis @ ubuntu: ~ $ sudo find /-name unifont * / usr / share / fonts / truetype / unifont / usr / share / fonts / truetype / unifont / unifont.ttf</p>
<hr />
</div>
<div id="comment-21709-info" class="comment-info">
<span class="comment-age">(22 Apr '13, 10:27)</span> <span class="comment-user userinfo">sgGold</span>
</div>
</div>
<span id="21710"></span>
<div id="comment-21710" class="comment">
<div id="post-21710-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<pre><code>mtis @ ubuntu: ~ $ tail / etc / mapnik-osm-data / inc / fontset-settings.xml.inc
  &lt;! - Font face-name = &quot;unifont Medium&quot; / -&gt;
&lt;/ FontSet
&lt;FontSet Name=&quot;bold-fonts&quot;&gt;
  The &lt;font face-name=&quot;DejaVu The Sans Bold&quot; /&gt;
  &lt;! - Font face-name = &quot;unifont Medium&quot; / -&gt;
&lt;/ FontSet
&lt;FontSet Name=&quot;oblique-fonts&quot;&gt;
  The &lt;font face-name=&quot;DejaVu The Sans Oblique&quot; /&gt;
  &lt;! - Font face-name = &quot;unifont Medium&quot; / -&gt;
&lt;/ FontSet</code></pre>
</div>
<div id="comment-21710-info" class="comment-info">
<span class="comment-age">(22 Apr '13, 10:28)</span> <span class="comment-user userinfo">sgGold</span>
</div>
</div>
<span id="21773"></span>
<div id="comment-21773" class="comment">
<div id="post-21773-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Your comment comes out a bit garbled, but notice that the character combination "less than" "exlamation mark" "minus" "minus" is the beginning of a comment in XML ("minus" "minus" "greater than" is the end of a comment) so it looks like the unifont might be commented out in your fontset-settings.inc?</p>
</div>
<div id="comment-21773-info" class="comment-info">
<span class="comment-age">(23 Apr '13, 18:55)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="21778"></span>
<div id="comment-21778" class="comment">
<div id="post-21778-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>(meta <span>@Frederik Ramm</span>: fixed the code formatting)</p>
</div>
<div id="comment-21778-info" class="comment-info">
<span class="comment-age">(23 Apr '13, 23:38)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="21961"></span>
<div id="comment-21961" class="comment">
<div id="post-21961-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you.I did not know that it is there, the line block. However, on the DejaVu font, erase Leaving Unifont only Does not generate tiles ...</p>
<p>I think, to get back to after the following procedure to install the font. What do you think?</p>
<p>I'm confused. Boohoo</p>
</div>
<div id="comment-21961-info" class="comment-info">
<span class="comment-age">(29 Apr '13, 03:26)</span> <span class="comment-user userinfo">sgGold</span>
</div>
</div>
</div>
<div id="comment-tools-21704" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21704-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="21964"></span>

<div id="answer-container-21964" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-21964-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21964-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-21964-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Not all fonts are able to display all UTF-8 characters. The DejaVu font for example doesn't appear to be able to display Korean characters, which is what leads to your problem.</p>
<p>Mapnik, the rendering library used to generate the tiles, has the ability to use alternative fonts for those characters that aren't supported by the default font. This alternative font is specified (as you have now done) in the style sheet in font-settings.xml.inc.</p>
<p>In addition, however, you need to tell mapnik where to find this alternative font. As you are using renderd as your driver for mapnik, the way you tell mapnik where to look for the fonts is in /etc/renderd.conf</p>
<p>In that file, there is a configuration parameter font_dir ( <a href="https://github.com/openstreetmap/mod_tile/blob/master/debian/renderd.conf#L9">https://github.com/openstreetmap/mod_tile/blob/master/debian/renderd.conf#L9</a> ) and font_dir_recurse. In the default /etc/renderd.conf these parameters are set wrong, as they point directly to the dejavu font, rather than the generic font dir and then recurse in to load all fonts.</p>
<p>So if you set font_dir_recurse to true and then change font_dir to the generic /usr/share/fonts/truetype/ you should hopefully get mapnik to load the unifont, which should then render the Korean characters correctly.</p>
<p>The Ubuntu 13.04 packages I uploaded a couple of days ago should have this fixed, but I haven't uploaded corrected packages yet for the older versions of Ubuntu.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Apr '13, 10:26</strong></p>
<img src="https://secure.gravatar.com/avatar/32c974c4ca8b246698c2b82c64924da5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="apmon&#39;s gravatar image" />
<p><span>apmon</span><br />
<span class="score" title="6527 reputation points"><span>6.5k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="44 badges"><span class="silver">●</span><span class="badgecount">44</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="apmon has 9 accepted answers">20%</span></p>
</div>
</div>
<div id="comments-container-21964" class="comments-container">
<span id="21981"></span>
<div id="comment-21981" class="comment">
<div id="post-21981-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thank you. Has been resolved. I'm very happy.</p>
<p>Thank you</p>
</div>
<div id="comment-21981-info" class="comment-info">
<span class="comment-age">(30 Apr '13, 02:30)</span> <span class="comment-user userinfo">sgGold</span>
</div>
</div>
</div>
<div id="comment-tools-21964" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21964-form-container" class="comment-form-container">
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

</hr>

</div>

</div>

