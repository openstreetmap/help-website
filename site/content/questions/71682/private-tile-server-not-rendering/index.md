+++
type = "question"
title = "Private Tile Server not rendering"
description = '''I searched other topics but didn&#x27;t found a post that used this version of Ubuntu (18.04), so I think it would be a good idea to don&#x27;t merge this with other topics, despite similar problem. I followed the tutorial available at https://switch2osm.org/manually-building-a-tile-server-18-04-lts/ to setup...'''
date = "2019-11-17T01:45:00Z"
lastmod = "2019-11-19T16:57:00Z"
weight = 71682
keywords = [ "rendering", "mod_tile", "osm", "tileserver" ]
aliases = [ "/questions/71682" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Private Tile Server not rendering](/questions/71682/private-tile-server-not-rendering)

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
<span id="post-71682-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71682-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-71682-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I searched other topics but didn't found a post that used this version of Ubuntu (18.04), so I think it would be a good idea to don't merge this with other topics, despite similar problem.</p>
<p>I followed the tutorial available at <a href="https://switch2osm.org/manually-building-a-tile-server-18-04-lts/">https://switch2osm.org/manually-building-a-tile-server-18-04-lts/</a> to setup my own tile server. I'm building the server in my computer and everything went fine. The <a href="http://localhost/hot/0/0/0.png">http://localhost/hot/0/0/0.png</a> showed the world map correctly, but <a href="http://localhost/hot/1/0/0.png">http://localhost/hot/1/0/0.png</a> gives Not Found error.</p>
<p>In the last step, where I should view the tiles, they aren't shown, but for some reason, when I put the zoom lv 0 it shows the map.</p>
<p>I'm opening the "sample_leaflet.html" file inside folder /src/mod_tile/extra/ using Firefox Browser.</p>
<p>Thanks in advance. Please ask me to post any other useful info that would help to debug this problem.</p>
<p><img src="https://i.imgur.com/o9T3yGZ.png" width="800" /></p>
<p><img src="https://i.imgur.com/ct5klJC.png" width="800" /></p>
<p>UPDATE #1:</p>
<p>The Browser Console shows the following errors.</p>
<p><img src="https://i.imgur.com/vabUeYR.png" width="800" /></p>
<p>This is my leaflet file</p>
<p><img src="https://i.imgur.com/JXVUMzX.png" width="800" /></p>
<p><code>systemctl status renderd</code> give the following:</p>
<p><img src="https://i.imgur.com/wkS9JA6.png" width="800" /></p>
<p>This is the result from <code>tail -f /var/log/syslog | grep " TILE "</code></p>
<p><img src="https://i.imgur.com/IbnLrrt.png" width="800" /></p>
<p>UPDATE #3: I checked folder "/var/lib/mod_tile/ajt/", where its supposed to store the tiles and it is occupying a total of 60.9 Kb, so clearly the tiles aren't being stored there.</p>
<p><img src="https://i.imgur.com/DEFQBB8.png" width="800" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-mod_tile" rel="tag" title="see questions tagged &#39;mod_tile&#39;">mod_tile</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Nov '19, 01:45</strong></p>
<img src="https://secure.gravatar.com/avatar/5f1f061e7e81f0e885227d27d95752f6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="carlosguedes&#39;s gravatar image" />
<p><span>carlosguedes</span><br />
<span class="score" title="91 reputation points">91</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="carlosguedes has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Nov '19, 16:09</strong> </span></p>
</div>
</div>
<div id="comments-container-71682" class="comments-container">
&#10;</div>
<div id="comment-tools-71682" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71682-form-container" class="comment-form-container">
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

<span id="71728"></span>

<div id="answer-container-71728" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71728-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71728-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-71728-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="carlosguedes has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You have a "failed to write metafile to file" error, so you need to check:</p>
<ul>
<li>What account you are running the command that is trying to write to that directory</li>
<li>What access rights are needed to write to that directory.</li>
</ul>
<p>Here's what it looks like on a server of mine:</p>
<pre><code>renderaccount@myserver:~$ cd /var/lib/mod_tile/ajt
renderaccount@myserver:/var/lib/mod_tile/ajt$ ls -ald .
drwxrwxr-x 27 renderaccount renderaccount 4096 Oct 23  2018 .
renderaccount@myserver:/var/lib/mod_tile/ajt$</code></pre>
<p>The process that renders tiles runs as a user called "renderaccount" and that account has write access to that directory.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Nov '19, 15:08</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Nov '19, 15:08</strong> </span></p>
</div>
</div>
<div id="comments-container-71728" class="comments-container">
<span id="71736"></span>
<div id="comment-71736" class="comment">
<div id="post-71736-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'm logging in OS using my root account, but in Terminal I do <code>su renderaccount</code> to run commands as the user renderaccount, is that correct?</p>
<p>I did the following commands:</p>
<p>sudo chown renderaccount /var/lib/mod_tile/</p>
<p>sudo chmod u+w /var/lib/mod_tile/</p>
<p>Isn't that enough to give write permisions for renderaccount?</p>
</div>
<div id="comment-71736-info" class="comment-info">
<span class="comment-age">(19 Nov '19, 16:08)</span> <span class="comment-user userinfo">carlosguedes</span>
</div>
</div>
<span id="71739"></span>
<div id="comment-71739" class="comment">
<div id="post-71739-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Now it worked! But I don't know exactly what solved it, because I did 2 things.</p>
<p>1) I did the chown command with : after the username, like this sudo chown renderaccount: /var/lib/mod_tile/ but I don't know if the : is needed (the switch2osm tutorial dont use it)</p>
<p>2) I did chown and chmod commands both in /var/lib/mod_tile/ and /var/lib/mod_tile/ajt/ but I'm not sure if an user having permision to write in a folder is enough to write in its subfolder.</p>
</div>
<div id="comment-71739-info" class="comment-info">
<span class="comment-age">(19 Nov '19, 16:43)</span> <span class="comment-user userinfo">carlosguedes</span>
</div>
</div>
<span id="71740"></span>
<div id="comment-71740" class="comment">
<div id="post-71740-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Looking at the "drwxrwxr-x" in my comment above, the first "rwx" means that the owner of the directory has the right to read files, write files and cd into that directory. The owner of the directory is "renderaccount". The second "rwx" means that anyone in the group "renderaccount" can read, write, and enter into that directory. The "r-x" at the end means that everyone else can read that directory and cd into it but not write files there.</p>
<p>The level of detail in the "switch2osm" guide is a compromise - it tries to assume no prior knowledge so that if you follow the instructions you'll get something working at the other end, but it doesn't go into so much detail about the various Unix concepts that you encounter on the way through. If it did it'd be an awful lot longer, and all of that stuff is available elsewhere.</p>
</div>
<div id="comment-71740-info" class="comment-info">
<span class="comment-age">(19 Nov '19, 16:57)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-71728" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71728-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="71684"></span>

<div id="answer-container-71684" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71684-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71684-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-71684-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>First of all:</p>
<p>have you prerendered any tiles? Those metatiles on e.g. on zoom 6 can take up to 2 CPU-Hours to render for the first time, but you should at least see renderd showing up in the syslog, so there is sth. else not working between leaflet and your apache/renderd toolchain.</p>
<p>Do you see any errors in the js console of the firefox developer tab?</p>
<p>And please use grep renderd on your syslog to watch renderds work, not grep " TILE ".</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Nov '19, 09:26</strong></p>
<img src="https://secure.gravatar.com/avatar/e06ed329df6032df14b5639de4d64782?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Spiekerooger&#39;s gravatar image" />
<p><span>Spiekerooger</span><br />
<span class="score" title="3148 reputation points"><span>3.1k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Spiekerooger has 18 accepted answers">16%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Nov '19, 14:03</strong> </span></p>
</div>
</div>
<div id="comments-container-71684" class="comments-container">
<span id="71687"></span>
<div id="comment-71687" class="comment">
<div id="post-71687-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It's my first time rendering tiles. I left my laptop on for all night long to check if its rendering but nothing appeared. Its specs are 16 GB RAM, i7-8550U, MX150 2 GB and all running in SSD, should it take that long? Geofabrik don't have OSM data of smaller parts of Brazil, like states or cities, that's why I used the whole country. I updated my question with the screenshot of the Browser Console, is that the right console? I did grep renderd also but didn't got any message.</p>
</div>
<div id="comment-71687-info" class="comment-info">
<span class="comment-age">(17 Nov '19, 16:33)</span> <span class="comment-user userinfo">carlosguedes</span>
</div>
</div>
<span id="71706"></span>
<div id="comment-71706" class="comment">
<div id="post-71706-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>After reinstalling everything with the right account now it shows the tile messages in console, despite now showing the tiles itself. I updated my question.</p>
</div>
<div id="comment-71706-info" class="comment-info">
<span class="comment-age">(19 Nov '19, 02:48)</span> <span class="comment-user userinfo">carlosguedes</span>
</div>
</div>
<span id="71708"></span>
<div id="comment-71708" class="comment">
<div id="post-71708-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>So it does look as if you don't have permission to write the metatiles into the file structure. Check the owner and rights or your ajt directory in a terminal and check renderd.conf settings for the internal tile path.</p>
</div>
<div id="comment-71708-info" class="comment-info">
<span class="comment-age">(19 Nov '19, 05:42)</span> <span class="comment-user userinfo">Spiekerooger</span>
</div>
</div>
<span id="71727"></span>
<div id="comment-71727" class="comment">
<div id="post-71727-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Correcting my last comment: After reinstalling everything with the right account now it shows the tile messages in console, despite not showing the tiles itself. I updated my question.</p>
</div>
<div id="comment-71727-info" class="comment-info">
<span class="comment-age">(19 Nov '19, 15:00)</span> <span class="comment-user userinfo">carlosguedes</span>
</div>
</div>
<span id="71729"></span>
<div id="comment-71729" class="comment">
<div id="post-71729-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>But you syslog tells us that renderd is not able to write the metatiles to a file. Sou check (e.g. via top) the linux user that is running renderd and than check file permissions at the ajt directory.</p>
</div>
<div id="comment-71729-info" class="comment-info">
<span class="comment-age">(19 Nov '19, 15:09)</span> <span class="comment-user userinfo">Spiekerooger</span>
</div>
</div>
<span id="71738"></span>
<div id="comment-71738" class="comment not_top_scorer">
<div id="post-71738-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>the command top -U renderaccount shows that renderaccount is indeed running renderd.</p>
</div>
<div id="comment-71738-info" class="comment-info">
<span class="comment-age">(19 Nov '19, 16:24)</span> <span class="comment-user userinfo">carlosguedes</span>
</div>
</div>
</div>
<div id="comment-tools-71684" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-71684-form-container" class="comment-form-container">
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

