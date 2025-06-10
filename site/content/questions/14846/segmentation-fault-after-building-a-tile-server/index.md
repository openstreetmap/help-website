+++
type = "question"
title = "segmentation fault after building a tile server"
description = '''I followed exactly the following tutorial, and everything worked without problems. http://switch2osm.org/serving-tiles/manually-building-a-tile-server/ In the end, at the end of the sequence: sudo mkdir /var/run/renderd sudo chown myuser /var/run/renderd renderd -f -c /usr/local/etc/renderd.conf  I ...'''
date = "2012-08-05T13:02:00Z"
lastmod = "2012-09-22T19:06:00Z"
weight = 14846
keywords = [ "tile", "segfault", "installation", "server" ]
aliases = [ "/questions/14846" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [segmentation fault after building a tile server](/questions/14846/segmentation-fault-after-building-a-tile-server)

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
<span id="post-14846-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14846-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-14846-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I followed exactly the following tutorial, and everything worked without problems. <a href="http://switch2osm.org/serving-tiles/manually-building-a-tile-server/">http://switch2osm.org/serving-tiles/manually-building-a-tile-server/</a></p>
<p>In the end, at the end of the sequence:</p>
<pre><code>sudo mkdir /var/run/renderd
sudo chown myuser /var/run/renderd
renderd -f -c /usr/local/etc/renderd.conf</code></pre>
<p>I am receiving a segmentation fault message:</p>
<pre><code>myuser@gis:~$ renderd -f -c /usr/local/etc/renderd.conf
renderd[9707]: Rendering daemon started
renderd[9707]: Parsing section renderd
renderd[9707]: Parsing render section 0
renderd[9707]: Parsing section mapnik
renderd[9707]: Parsing section default
renderd[9707]: config renderd: unix socketname=/var/run/renderd/renderd.sock
renderd[9707]: config renderd: num_threads=4
renderd[9707]: config renderd: num_slaves=0
renderd[9707]: config renderd: tile_dir=/var/lib/mod_tile
renderd[9707]: config renderd: stats_file=/var/run/renderd/renderd.stats
renderd[9707]: config mapnik:  plugins_dir=/usr/local/lib/mapnik/input
renderd[9707]: config mapnik:  font_dir=/usr/share/fonts/truetype/ttf-dejavu
renderd[9707]: config mapnik:  font_dir_recurse=1
renderd[9707]: config renderd(0): Active
renderd[9707]: config renderd(0): unix socketname=/var/run/renderd/renderd.sock
renderd[9707]: config renderd(0): num_threads=4
renderd[9707]: config renderd(0): tile_dir=/var/lib/mod_tile
renderd[9707]: config renderd(0): stats_file=/var/run/renderd/renderd.stats
renderd[9707]: config map 0:   name(default) file(/home/myuser/src/mapnik-style/osm.xml) uri(/osm_tiles2/) htcp() host(localhost)
renderd[9707]: Initialising unix server socket on /var/run/renderd/renderd.sock
renderd[9707]: Created server socket 4
renderd[9707]: Renderd is using mapnik version 0.7.2
renderd[9707]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSans-ExtraLight.ttf
renderd[9707]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSans-Oblique.ttf
renderd[9707]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSerif.ttf
renderd[9707]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSansMono-Bold.ttf
renderd[9707]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSansMono-Oblique.ttf
renderd[9707]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSerif-BoldItalic.ttf
renderd[9707]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSerifCondensed.ttf
renderd[9707]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSans-BoldOblique.ttf
renderd[9707]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSerif-Italic.ttf
renderd[9707]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSansCondensed-Oblique.ttf
renderd[9707]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSerifCondensed-Italic.ttf
renderd[9707]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSans-Bold.ttf
renderd[9707]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSansCondensed-Bold.ttf
renderd[9707]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSansCondensed.ttf
renderd[9707]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSans.ttf
renderd[9707]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSansMono-BoldOblique.ttf
renderd[9707]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSansCondensed-BoldOblique.ttf
renderd[9707]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSerifCondensed-Bold.ttf
renderd[9707]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSansMono.ttf
renderd[9707]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSerifCondensed-BoldItalic.ttf
renderd[9707]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSerif-Bold.ttf
Running in foreground mode...
renderd[9707]: Starting stats thread
Segmentation fault</code></pre>
<p>Running dmesg, the following error appears:</p>
<pre><code>[ 5132.442678] renderd[9713]: **segfault** at 1a ip 00007f4c3c448b12 sp 00007f4c2ef397a0 error 4 in **libxml2.so.2.7.6**[7f4c3c3ef000+146000]</code></pre>
<p>or</p>
<pre><code>[ 5423.308084] renderd[10245] **general protection** ip:7fe4d82ec2a2 sp:7fe4c9264748 error:0 in **libc-2.11.1.so**[7fe4d8269000+17a000]</code></pre>
<p>Trying to restart manually the httpd server, another error appears:</p>
<pre><code>myuser@gis:~$ sudo /etc/init.d/apache2 restart
 * Restarting web server apache2    [Sun Aug 05 14:28:51 2012] [notice] Committing tile config default
Segmentation fault    [fail]</code></pre>
<p>Looking in dmesg (the segfault with libc appears twice):</p>
<pre><code>[ 5491.172508] apache2[10319]: **segfault** at 0 ip 00007f3a4c5803e4 sp 00007fff5444fa88 error 4 in **libc-2.11.1.so**[7f3a4c4fd000+17a000]
[ 5491.231489] apache2[10327]: **segfault** at 0 ip 00007f8fc8fa03e4 sp 00007fffd2798c38 error 4 in **libc-2.11.1.so**[7f8fc8f1d000+17a000]</code></pre>
<p>So, where is the problem ? I can't figure out. Should I downgrade some packages ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tile" rel="tag" title="see questions tagged &#39;tile&#39;">tile</span> <span class="post-tag tag-link-segfault" rel="tag" title="see questions tagged &#39;segfault&#39;">segfault</span> <span class="post-tag tag-link-installation" rel="tag" title="see questions tagged &#39;installation&#39;">installation</span> <span class="post-tag tag-link-server" rel="tag" title="see questions tagged &#39;server&#39;">server</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Aug '12, 13:02</strong></p>
<img src="https://secure.gravatar.com/avatar/5598e066f7d11f2179682c98f66b60bc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aes693&#39;s gravatar image" />
<p><span>aes693</span><br />
<span class="score" title="56 reputation points">56</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aes693 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Aug '12, 15:58</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-14846" class="comments-container">
<span id="14848"></span>
<div id="comment-14848" class="comment">
<div id="post-14848-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Are you using the original OSM map styles or have you made any changes to the XML file?</p>
</div>
<div id="comment-14848-info" class="comment-info">
<span class="comment-age">(05 Aug '12, 13:41)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="14851"></span>
<div id="comment-14851" class="comment">
<div id="post-14851-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I downloaded a map for one country. I didn't change anything.</p>
</div>
<div id="comment-14851-info" class="comment-info">
<span class="comment-age">(05 Aug '12, 15:39)</span> <span class="comment-user userinfo">aes693</span>
</div>
</div>
<span id="14883"></span>
<div id="comment-14883" class="comment">
<div id="post-14883-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I just installed this morning Ubuntu 12.04 LTS (x86_64). The machine has 4GB ram and 3Ghz cpu (AMD). Following the tutorial, I installed the packages (some updated). At the end I am confronted with the same issue. It's not the mod_tile.so. It's renderd that what gaves me errors. Now the segfault errors are related to: libxml2.so.2.7.8 and libc-2.15.so. So, could be a compiling problem ?</p>
<p>I am newbie using gdb, but if I'll find the issue (hopefully), I'll report it.</p>
</div>
<div id="comment-14883-info" class="comment-info">
<span class="comment-age">(07 Aug '12, 12:30)</span> <span class="comment-user userinfo">aes693</span>
</div>
</div>
<span id="15054"></span>
<div id="comment-15054" class="comment">
<div id="post-15054-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Same problem here. Have you found a solution? I have tried the same instructions on three Ubuntu 12.04. Can anyone help?</p>
</div>
<div id="comment-15054-info" class="comment-info">
<span class="comment-age">(14 Aug '12, 09:44)</span> <span class="comment-user userinfo">bluescreen</span>
</div>
</div>
<span id="15079"></span>
<div id="comment-15079" class="comment not_top_scorer">
<div id="post-15079-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The segfault in apache might be solved after you do an svn update.</p>
<p>Not sure about the issue in renderd yet though. A more informative stack trace would hopefully be helpful tracking this down.</p>
</div>
<div id="comment-15079-info" class="comment-info">
<span class="comment-age">(14 Aug '12, 16:37)</span> <span class="comment-user userinfo">apmon</span>
</div>
</div>
<span id="16266"></span>
<div id="comment-16266" class="comment not_top_scorer">
<div id="post-16266-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Just another data point, but when I ran through the more recent version <a href="http://switch2osm.org/serving-tiles/manually-building-a-tile-server-12-04/">http://switch2osm.org/serving-tiles/manually-building-a-tile-server-12-04/</a> a couple of days ago there were no segfault issues.</p>
</div>
<div id="comment-16266-info" class="comment-info">
<span class="comment-age">(20 Sep '12, 09:29)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="16267"></span>
<div id="comment-16267" class="comment not_top_scorer">
<div id="post-16267-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@SomeoneElse</span>: thanks for information; I will double check asap if there are changes and if it's working here too.</p>
</div>
<div id="comment-16267-info" class="comment-info">
<span class="comment-age">(20 Sep '12, 09:45)</span> <span class="comment-user userinfo">aes693</span>
</div>
</div>
<span id="16315"></span>
<div id="comment-16315" class="comment not_top_scorer">
<div id="post-16315-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@SomeoneElse</span>: thank you very much, now I see, that how-to web page was modified on the top, in the software installation section: now, there are 29 packages to be installed (18 previous). Postgresql server is 9.1 (I added myself manually before this modification anyway; previous was 8.4 @ Ubuntu 10.04). At "Install Mapnik library" section, that downloading and compiling the source of ... 'sudo apt-get install libltdl3-dev libpng12-dev libtiff4-dev libicu-dev [...]' disappeared. I hope it will work now; I will install it from zero again.</p>
</div>
<div id="comment-16315-info" class="comment-info">
<span class="comment-age">(21 Sep '12, 17:46)</span> <span class="comment-user userinfo">aes693</span>
</div>
</div>
<span id="16316"></span>
<div id="comment-16316" class="comment not_top_scorer">
<div id="post-16316-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I will repeat another question now, so please, be patient with me: my problem can be related to my wish of using a map for only one country instead the whole planet ? Do I have to open a new topic / search (more) for an answer ? Sorry for bothering with newbie questions and thank you all who answered for your effort &amp; help.</p>
</div>
<div id="comment-16316-info" class="comment-info">
<span class="comment-age">(21 Sep '12, 17:50)</span> <span class="comment-user userinfo">aes693</span>
</div>
</div>
<span id="16318"></span>
<div id="comment-16318" class="comment">
<div id="post-16318-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Generally you'd ask one question per question, because it gets confusing otherwise, but no - the fact that you've imported only one country rather than the whole planet wouldn't cause the issue that you're seeing; the only difference it would make would be that the data import would happen faster and require less memory.</p>
</div>
<div id="comment-16318-info" class="comment-info">
<span class="comment-age">(21 Sep '12, 17:57)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="16319"></span>
<div id="comment-16319" class="comment not_top_scorer">
<div id="post-16319-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I know and I'm sorry. I should write in the title of the topic from the beggining/or in the body of the question: '(working with only a country map)' and express my worry because I didn't follow 100% the tutorial (because of the hardware and also the uselessness of using the map of the whole planet). Thank you for your answer !</p>
</div>
<div id="comment-16319-info" class="comment-info">
<span class="comment-age">(21 Sep '12, 18:03)</span> <span class="comment-user userinfo">aes693</span>
</div>
</div>
</div>
<div id="comment-tools-14846" class="comment-tools">
<span class="comments-showing"> showing 5 of 11 </span> <a href="#" class="show-all-comments-link">show 6 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-14846-form-container" class="comment-form-container">
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

4 Answers:

</div>

</div>

<span id="15538"></span>

<div id="answer-container-15538" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-15538-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15538-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-15538-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The segmentation fault in renderd appears to be triggered by a long standing bug in libxml[1,2] and therefore outside of the control of mod_tile/renderd</p>
<p>One can also trigger the segmentation fault with "xmllint --noent /etc/mapnik-osm-data/osm.xml" (or whereever the path of your osm style sheet)</p>
<p>The problem seems to be a missing external entity in your osm style sheet. Try running "xmllint /etc/mapnik-osm-data/osm.xml" and see if it tells you which entity is missing, or not correctly configured. Once the style sheet is correctly configured, renderd should no longer segfault.</p>
<p>The segmentation fault in apache / mod_tile should be fixed in the latest code. So recompiling and re-installing mod_tile after an svn update should fix the problem.</p>
<p>[1] <a href="https://github.com/mapnik/mapnik/issues/566">https://github.com/mapnik/mapnik/issues/566</a> [2] <a href="https://bugs.launchpad.net/lxml/+bug/502959">https://bugs.launchpad.net/lxml/+bug/502959</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Aug '12, 04:48</strong></p>
<img src="https://secure.gravatar.com/avatar/32c974c4ca8b246698c2b82c64924da5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="apmon&#39;s gravatar image" />
<p><span>apmon</span><br />
<span class="score" title="6527 reputation points"><span>6.5k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="44 badges"><span class="silver">●</span><span class="badgecount">44</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="apmon has 9 accepted answers">20%</span></p>
</div>
</div>
<div id="comments-container-15538" class="comments-container">
<span id="16264"></span>
<div id="comment-16264" class="comment">
<div id="post-16264-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Sorry for delay and thank you for answer. I'm looking forward to find a solution to display the country's tiles. Btw: is it possible to put all of these to work under CentOS ? Thanks.</p>
</div>
<div id="comment-16264-info" class="comment-info">
<span class="comment-age">(19 Sep '12, 23:05)</span> <span class="comment-user userinfo">aes693</span>
</div>
</div>
</div>
<div id="comment-tools-15538" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15538-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="15055"></span>

<div id="answer-container-15055" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-15055-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15055-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-15055-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Try using the ready-made packages from <a href="http://switch2osm.org/serving-tiles/building-a-tile-server-from-packages/">http://switch2osm.org/serving-tiles/building-a-tile-server-from-packages/</a> instead of compiling your own.</p>
<p>Segmentation faults in Apache (likely from mod_tile) and in renderd are unlikely to have the same root cause; both components access the tile directories and the renderd.conf file but that's about all they have in common.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Aug '12, 09:55</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-15055" class="comments-container">
<span id="15064"></span>
<div id="comment-15064" class="comment">
<div id="post-15064-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@Frederik Ramm</span></p>
<p>Thank you for your response. Well, I tried to eliminate the possible causes, one by one. I commented the following lines from the file /etc/apache2/sites-available/default</p>
<h1 id="loadtileconfigfile-usrlocaletcrenderd.conf">LoadTileConfigFile /usr/local/etc/renderd.conf</h1>
<h1 id="modtilerenderdsocketname-varrunrenderdrenderd.sock">ModTileRenderdSocketName /var/run/renderd/renderd.sock</h1>
<h1 id="modtilerequesttimeout-0">ModTileRequestTimeout 0</h1>
<h1 id="modtilemissingrequesttimeout-30">ModTileMissingRequestTimeout 30</h1>
<p>Then, I restarted the Apache:</p>
<p>myuser@gis:~$ sudo /etc/init.d/apache2 restart</p>
<ul>
<li>Restarting web server apache2</li>
</ul>
<p>apache2: Could not reliably determine the server's fully qualified domain name, using 127.0.1.1 for ServerName [...etc..] [ OK ]</p>
</div>
<div id="comment-15064-info" class="comment-info">
<span class="comment-age">(14 Aug '12, 11:28)</span> <span class="comment-user userinfo">aes693</span>
</div>
</div>
<span id="15065"></span>
<div id="comment-15065" class="comment">
<div id="post-15065-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Then, I wanted to see if the modules (also mod_tile) were loaded:</p>
<p>myuser@gis:/var/log/apache2$ apachectl -t -D DUMP_MODULES /usr/sbin/apachectl: 87: ulimit: error setting limit (Operation not permitted) apache2: Could not reliably determine the server's fully qualified domain name, using 127.0.1.1 for ServerName Loaded Modules:</p>
<p>core_module (static) [...other 23 modules...] tile_module (shared) Syntax OK</p>
<p>So, the next question: if the module [tile_module] was corrupted, shouldn't appeared at the startup at least a warning ?</p>
<p>Thank you very much for your hint. I will dig deeper in parallel.</p>
</div>
<div id="comment-15065-info" class="comment-info">
<span class="comment-age">(14 Aug '12, 11:29)</span> <span class="comment-user userinfo">aes693</span>
</div>
</div>
<span id="15226"></span>
<div id="comment-15226" class="comment not_top_scorer">
<div id="post-15226-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ok, following ready-made packages from <a href="http://switch2osm.org/serving-tiles/building-a-tile-server-from-packages/">http://switch2osm.org/serving-tiles/building-a-tile-server-from-packages/</a> I have a new situation:</p>
<p>I downloaded <a href="http://ppa.launchpad.net/kakrueger/openstreetmap/ubuntu/pool/main/liba/libapache2-mod-tile/libapache2-mod-tile_0.4-11~precise2.tar.gz">http://ppa.launchpad.net/kakrueger/openstreetmap/ubuntu/pool/main/liba/libapache2-mod-tile/libapache2-mod-tile_0.4-11~precise2.tar.gz</a></p>
<p>and I compiled. Then I unmarked those 4 lines above. I restarted the apache2 service.</p>
<p>Restarting web server apache2 [...] [Fri Aug 17 22:15:23 2012] [notice] Loading tile config default at /osm_tiles2/ for zooms 0 - 18 from tile directory /var/lib/mod_tile with extension .png and mime type image/png [ OK ]</p>
</div>
<div id="comment-15226-info" class="comment-info">
<span class="comment-age">(17 Aug '12, 20:21)</span> <span class="comment-user userinfo">aes693</span>
</div>
</div>
<span id="15227"></span>
<div id="comment-15227" class="comment">
<div id="post-15227-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Then I typed as in the guide: sudo mkdir /var/run/renderd sudo chown myuser /var/run/renderd renderd -f -c /usr/local/etc/renderd.conf</p>
<p>but the result it's the same:</p>
<p>renderd[10342]: Rendering daemon started [...etc...] Running in foreground mode... renderd[10342]: Starting stats thread Segmentation fault (core dumped)</p>
<p>myuser@gis:~$ dmesg</p>
<p>... [ 1702.604071] renderd[9561]: segfault at 1b ip 00007f0fcc8cb600 sp 00007f0fbe1723b0 error 4 in libxml2.so.2.7.8[7f0fcc874000+151000]</p>
</div>
<div id="comment-15227-info" class="comment-info">
<span class="comment-age">(17 Aug '12, 20:25)</span> <span class="comment-user userinfo">aes693</span>
</div>
</div>
<span id="15236"></span>
<div id="comment-15236" class="comment not_top_scorer">
<div id="post-15236-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>by the way: I used also the .deb packages, but without success:</p>
<p>libapache2-mod-tile_0.4-11~precise2_amd64.deb and renderd_0.4-11~precise2_amd64.deb from <a href="http://ppa.launchpad.net/kakrueger/openstreetmap/ubuntu/pool/main/liba/libapache2-mod-tile/">http://ppa.launchpad.net/kakrueger/openstreetmap/ubuntu/pool/main/liba/libapache2-mod-tile/</a></p>
</div>
<div id="comment-15236-info" class="comment-info">
<span class="comment-age">(18 Aug '12, 07:13)</span> <span class="comment-user userinfo">aes693</span>
</div>
</div>
<span id="15240"></span>
<div id="comment-15240" class="comment">
<div id="post-15240-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>So far I haven't been able to reproduce this segfault. I just followed the instructions in a fresh (fully up-to-date) Ubuntu 12.04 (64bit) VM and did not have any issues. It is correctly rendering and I can view the tiles in the browser via mod_tile.</p>
<p>Can you give any additional information that might help track these issues down?</p>
</div>
<div id="comment-15240-info" class="comment-info">
<span class="comment-age">(18 Aug '12, 09:19)</span> <span class="comment-user userinfo">apmon</span>
</div>
</div>
<span id="15254"></span>
<div id="comment-15254" class="comment not_top_scorer">
<div id="post-15254-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@apmon</span>: sure. Please, give me details how can I provide a fully accurate report.</p>
</div>
<div id="comment-15254-info" class="comment-info">
<span class="comment-age">(18 Aug '12, 18:11)</span> <span class="comment-user userinfo">aes693</span>
</div>
</div>
<span id="15346"></span>
<div id="comment-15346" class="comment not_top_scorer">
<div id="post-15346-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ok, I installed the old 10.04.4 LTS onto an old 32bit single core AMD 2ghz machine<br />
with 3GB Ram (VMware), (gaving 1GB Ram to Ubuntu).<br />
I installed and configured all packages using SSH, using putty, saving all the<br />
printable output (session log), and I noticed that there are no errors.<br />
Running apache, renderd, I also noticed the lack of errors.<br />
<br />
The differences between this and previous installations:<br />
- at the beggining of the installation I gave an<br />
sudo apt-get install update &amp;&amp; sudo apt-get upgrade<br />
- the file ~/src/mapnik-style/inc/settings.xml.inc shouldn't have<br />
uncommented those to be replaced lines (as the one below) ?<br />
<strong>&lt;ENTITY osm2pgsql_projection "&amp;srs900913;"&gt;</strong><br />
- at the building of the Mapnik library's from source,<br />
git checkout 0.7<br />
... apears: falling to 0.7.2;<br />
- having only one GB Ram, I used the values:<br />
sudo sysctl -w kernel.shmmax=536870912 ; 512 MB<br />
sudo sysctl -w kernel.shmall=131072 ; shmmax / 4096<br />
<br />
Tomorrow I will go back to the machine with Ubuntu 12.04 LTS (x86_64) and I will try to:<br />
a) make the modifications to the ~/src/mapnik-style/inc/settings.xml.inc file, or<br />
b) reinstall all from zero and log everything at installations &amp; configurations.<br />
<br />
I have one more question: if (because the hardware) I can't (because I don't need to)<br />
use the whole planet [file] and I want to use just a country (package), the procedure it's<br />
similar, mean e.g. using the file wget <a href="http://192.168.1.1/countryX.osm.bz2">http://192.168.1.1/countryX.osm.bz2</a> and run a<br />
osm2pgsql --slim -d gis -C 2048 ~/planet/countryX.osm.bz2 ?<br />
<br />
I tried to see if there are generated tiles of that country, using a slippymap e.g.<br />
<a href="http://192.168.1.2/osm/slippymap.html,">http://192.168.1.2/osm/slippymap.html,</a> but when I switched from Mapnik to Local Tiles,<br />
(over the countryX), the tiles turned from standard, colored to pink with no content.<br />
Using Firedebug I could see that the server returned 404 errors e.g. couldn't find the<br />
following resources (tiles supposed to be generated): e.g. <a href="http://192.168.1.2/osm/0/12/34.png">http://192.168.1.2/osm/0/12/34.png</a><br />
</p>
</div>
<div id="comment-15346-info" class="comment-info">
<span class="comment-age">(21 Aug '12, 22:35)</span> <span class="comment-user userinfo">aes693</span>
</div>
</div>
<span id="15415"></span>
<div id="comment-15415" class="comment">
<div id="post-15415-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Partially solved, some questions remains.<br />
There are two causes what generated those errors:<br />
<br />
1) The old/default <strong>mod_tile.so</strong> and <strong>renderd</strong> have some (yet) unidentified issues,<br />
so, following Mr. Frederik Ramm advice, I am using <strong>mod_tile.so</strong>and <strong>renderd</strong><br />
from Mr. Kai Kruger (see above); results: no problems with apache httpd/renderd;<br />
<br />
2) I logged on the machine with Ubuntu 12.04 LTS (x86_64) and I just edited<br />
<strong>/home/myuser/src/mapnik-style/inc/settings.xml.inc</strong>.<br />
I <strong>commented</strong> (!--) and <strong>uncommented</strong> (!) one by one the following lines:<br />
<br />
&lt;!ENTITY symbols "symbols"&gt;<br />
&lt;!ENTITY osm2pgsql_projection "&amp;srs900913;"&gt;<br />
&lt;!ENTITY dwithin_node_way "&amp;dwithin_900913;"&gt;<br />
&lt;!ENTITY world_boundaries "/usr/local/share/world_boundaries"&gt;<br />
&lt;!ENTITY prefix "planet_osm"&gt;<br />
<br />
Letting <strong>uncommented</strong> the last line (ENTITY prefix "planet_osm) will generates <strong>segmentation fault</strong><br />
(in renderd), while letting <strong>commented</strong>, will generates the follwing output:<br />
<br />
myuser@gis:~$ renderd -f -c /usr/local/etc/renderd.conf<br />
renderd[9730]: Rendering daemon started<br />
renderd[9730]: Parsing section renderd<br />
renderd[9730]: Parsing render section 0<br />
renderd[9730]: Parsing section mapnik<br />
renderd[9730]: Parsing section default<br />
renderd[9730]: config renderd: unix socketname=/var/run/renderd/renderd.sock<br />
renderd[9730]: config renderd: num_threads=2<br />
renderd[9730]: config renderd: num_slaves=0<br />
renderd[9730]: config renderd: tile_dir=/var/lib/mod_tile<br />
renderd[9730]: config renderd: stats_file=/var/run/renderd/renderd.stats<br />
renderd[9730]: config mapnik: plugins_dir=/usr/local/lib/mapnik/input<br />
renderd[9730]: config mapnik: font_dir=/usr/share/fonts/truetype/ttf-dejavu<br />
renderd[9730]: config mapnik: font_dir_recurse=1<br />
renderd[9730]: config renderd(0): Active<br />
renderd[9730]: config renderd(0): unix socketname=/var/run/renderd/renderd.sock<br />
renderd[9730]: config renderd(0): num_threads=2<br />
renderd[9730]: config renderd(0): tile_dir=/var/lib/mod_tile<br />
renderd[9730]: config renderd(0): stats_file=/var/run/renderd/renderd.stats<br />
renderd[9730]: config map 0: name(default) file(/home/myuser/src/mapnik-style/osm.xml) uri(/osm_tiles2/) htcp() host(localhost)<br />
renderd[9730]: Initialising unix server socket on /var/run/renderd/renderd.sock<br />
renderd[9730]: Created server socket 5<br />
renderd[9730]: Renderd is using mapnik version 0.7.2<br />
renderd[9730]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSerifCondensed.ttf<br />
renderd[9730]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSerif-Italic.ttf<br />
renderd[9730]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSerif.ttf<br />
renderd[9730]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSansCondensed.ttf<br />
renderd[9730]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSerifCondensed-Bold.ttf<br />
renderd[9730]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSansCondensed-Bold.ttf<br />
renderd[9730]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSansMono-Bold.ttf<br />
renderd[9730]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSansCondensed-BoldOblique.ttf<br />
renderd[9730]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSansMono-Oblique.ttf<br />
renderd[9730]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSans-Oblique.ttf<br />
renderd[9730]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSansMono.ttf<br />
renderd[9730]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSansCondensed-Oblique.ttf<br />
renderd[9730]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSerif-BoldItalic.ttf<br />
renderd[9730]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSerif-Bold.ttf<br />
renderd[9730]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSans-BoldOblique.ttf<br />
renderd[9730]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSerifCondensed-BoldItalic.ttf<br />
renderd[9730]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSerifCondensed-Italic.ttf<br />
renderd[9730]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSans-Bold.ttf<br />
renderd[9730]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSans-ExtraLight.ttf<br />
renderd[9730]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSans.ttf<br />
renderd[9730]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSansMono-BoldOblique.ttf<br />
Running in foreground mode...<br />
renderd[9730]: Starting stats thread<br />
renderd[9730]: An error occurred while loading the map layer 'default': XML document not well formed:<br />
Start tag expected, '&lt;' not found (encountered in file '/home/myuser/src/mapnik-style/osm.xml' at line 9)renderd[9730]: An error occurred while loading the map layer 'default': XML document not well formed:<br />
Start tag expected, '&lt;' not found (encountered in file '/home/myuser/src/mapnik-style/osm.xml' at line 9)<br />
<br />
mean the line:<br />
<br />
<strong>&lt;Map bgcolor="#b5d0d0" srs="&amp;srs900913;" minimum_version="0.7.1"&gt;</strong><br />
<br />
Now, the last questions: this output is because I am not using the planet file (and just one country),<br />
and if so, how can I correct set up the config files to work with only one country, so the<br />
tiles to be generated ?<br />
Thank you very much and sorry for bothering you with my questions.</p>
</div>
<div id="comment-15415-info" class="comment-info">
<span class="comment-age">(22 Aug '12, 22:42)</span> <span class="comment-user userinfo">aes693</span>
</div>
</div>
</div>
<div id="comment-tools-15055" class="comment-tools">
<span class="comments-showing"> showing 5 of 9 </span> <a href="#" class="show-all-comments-link">show 4 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-15055-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="16352"></span>

<div id="answer-container-16352" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-16352-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16352-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-16352-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><span><span>@SomeoneElse</span></span>, Frederik Ramm, apmon: I <strong>solved</strong> finally.<br />
It's working even with the map for one country instead the whole planet.<br />
My worries that wouldn't work and will require a special procedure were unjustified.<br />
<br />
It was a mix of various issues like external (libxml, libc) and internal<br />
(typing, missing [un]commented lines), also forget to modify slippymap.html.<br />
I guess besides those external, those internal are newbies' errors.<br />
<br />
My newbie advices (after I dig into the config files) are:<br />
<br />
<strong>a)</strong> be careful when editing renderd.conf<br />
I filled it up with appropriate values for paths, and I used alternatively <strong>numthreads=1</strong> (I will tune after),<br />
then I took care to use the same path (/osm_tiles2/) with that from slippymap.html<br />
e.g. <a href="http://192.168.0.1/osm_tiles2/$%7Bz%7D/$%7Bx%7D/$%7By%7D.png">http://192.168.0.1/osm_tiles2/${z}/${x}/${y}.png</a><br />
(in the javascript part); then I used an IP value for HOST instead "<strong>host=localhost</strong>";<br />
<br />
<strong>b)</strong> don't forget to check into /etc/apache2/sites-available/default for order allow, deny<br />
and allow from all at the beginning to get rid of initial troubles.<br />
<br />
<strong>c)</strong> osm.xml can provide further informations if you missed something in the config files<br />
(see the usage of "xmllint /home/myuser/src/mapnik-style/osm.xml" above)<br />
<br />
<strong>d)</strong> now, the last part: in the ~/src/mapnik-style/inc/ folder, only two files are<br />
editable (as in the tutorial): <strong>settings.xml.inc</strong> and <strong>datasource-settings.xml.inc</strong> ;<br />
users must be very carefully when (un)commenting:<br />
in datasource-settings.inc the lines with password, host, port, user should be commented as:<br />
&lt;!-- Parameter name ="password"&gt;%(password)s&lt;/Parameter --&gt;<br />
it's important to pay attention to the sintax (the first 4 and the last 3 characters) !<br />
Then, in the settings.xml.inc, you should keep 7 lines (take care at the sintax),<br />
those with: "symbols", "osm2pgsql_projection", "dwithin_900913", "dwithin_4326",<br />
dwithin_node_way, world_boundaries (take care at the path), and the line with prefix.<br />
These seven lines begin and terminate in the same manner: (first two and the last chr$ are important)<br />
&lt;!ENTITY symbols "symbols"&gt;<br />
<br />
OK, at last, at the installation point, if you don't have plenty RAM memory and an old CPU, instead of using<br />
osm2pgsql --slim -d gis -C 16000 --number-processes 3 ~/planet/planet-latest.osm.pbf (or ...Xcountry.pbf),<br />
you can use: osm2pgsql --slim -d gis -C 2048 ~/planet/countryX.osm.bz2<br />
<br />
I think that was all. Thank you very much for your support and for the patience.<br />
See you next time ! :)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Sep '12, 19:06</strong></p>
<img src="https://secure.gravatar.com/avatar/5598e066f7d11f2179682c98f66b60bc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aes693&#39;s gravatar image" />
<p><span>aes693</span><br />
<span class="score" title="56 reputation points">56</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aes693 has no accepted answers">0%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Sep '12, 19:22</strong> </span></p>
</div>
</div>
<div id="comments-container-16352" class="comments-container">
&#10;</div>
<div id="comment-tools-16352" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16352-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="16313"></span>

<div id="answer-container-16313" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-16313-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16313-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-16313-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><span>@apmon</span>:<br />
<br />
Hi,<br />
<br />
'xmllint /home/myuser/src/mapnik-style/osm.xml'<br />
or<br />
'xmllint --noent /home/myuser/src/mapnik-style/osm.xml'<br />
have the same result:<br />
<br />
myuser@gis:/$ xmllint /home/myuser/src/mapnik-style/osm.xml<br />
/home/myuser/src/mapnik-style/osm.xml:4: parser error : Char 0x0 out of allowed range<br />
%entities;<br />
              ^<br />
Entity: line 1:<br />
 %entities;<br />
                ^<br />
/home/myuser/src/mapnik-style/osm.xml:6: parser error : Comment must not contain '--' (double-hyphen)<br />
&lt;!-- This stylesheet uses features only available in mapnik builds with<br />
     ^<br />
/home/myuser/src/mapnik-style/osm.xml:8: parser error : Comment doesn't start and stop in the same entity<br />
      and behaviour that necessitate an upgrade to mapnik 0.7.1 --&gt;<br />
                                                                                              ^<br />
/home/myuser/src/mapnik-style/osm.xml:9: parser error : internal error<br />
&lt;Map bgcolor="#b5d0d0" srs="&amp;srs900913;" minimum_version="0.7.1"&gt;<br />
^<br />
/home/myuser/src/mapnik-style/osm.xml:9: parser error : DOCTYPE improperly terminated<br />
&lt;Map bgcolor="#b5d0d0" srs="&amp;srs900913;" minimum_version="0.7.1"&gt;<br />
^<br />
/home/myuser/src/mapnik-style/osm.xml:9: parser error : Start tag expected, '&lt;' not found<br />
&lt;Map bgcolor="#b5d0d0" srs="&amp;srs900913;" minimum_version="0.7.1"&gt;<br />
  ^<br />
</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Sep '12, 16:30</strong></p>
<img src="https://secure.gravatar.com/avatar/5598e066f7d11f2179682c98f66b60bc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aes693&#39;s gravatar image" />
<p><span>aes693</span><br />
<span class="score" title="56 reputation points">56</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aes693 has no accepted answers">0%</span> </br></br></p>
</div>
</div>
<div id="comments-container-16313" class="comments-container">
&#10;</div>
<div id="comment-tools-16313" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16313-form-container" class="comment-form-container">
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

