+++
type = "question"
title = "Carto CSS &#x27;hasOwnProperty&#x27; of undefined"
description = '''Following the tutorials at https://switch2osm.org/serving-tiles/manually-building-a-tile-server-14-04/ on Ubuntu 15.04, I am getting a error at the step where I build the OSMBright.xml style sheet.  Not sure why - I have made sure node and all dependencies in the process are set up and mapnik, rende...'''
date = "2015-05-02T23:20:00Z"
lastmod = "2015-05-08T03:53:00Z"
weight = 42816
keywords = [ "tileserver", "error", "carto", "15.04", "ubuntu" ]
aliases = [ "/questions/42816" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Carto CSS 'hasOwnProperty' of undefined](/questions/42816/carto-css-hasownproperty-of-undefined)

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
<span id="post-42816-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42816-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-42816-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Following the tutorials at <a href="https://switch2osm.org/serving-tiles/manually-building-a-tile-server-14-04/">https://switch2osm.org/serving-tiles/manually-building-a-tile-server-14-04/</a> on Ubuntu 15.04, I am getting a error at the step where I build the OSMBright.xml style sheet.</p>
<p>Not sure why - I have made sure node and all dependencies in the process are set up and mapnik, renderd, mod_tile, osm2pgsql are all installed as well (server is running the pbf import right now in fact.)</p>
<p>(I still have the old "XML" based format running at this time which works fine.)</p>
<p>At the end of the process to creating the stylesheet I am getting this error. I have went through the steps for this 6 times and get the same error.</p>
<p>I chown'd the /usr/local/share/maps/style directory to my username. I also attempted to do all this as root via sudo su but got the same results.</p>
<p>carto project.mml &gt; OSMBright.xml</p>
<pre><code>/usr/lib/nodejs/carto/lib/carto/tree/reference.js:19
if (mapnik_reference.version.hasOwnProperty(version)) {
                             ^
TypeError: Cannot call method &#39;hasOwnProperty&#39; of undefined
at Object.ref.setVersion (/usr/lib/nodejs/carto/lib/carto/tree/reference.js:19:34)
at /usr/lib/nodejs/carto/lib/carto/tree/reference.js:209:5
at Object.&lt;anonymous&gt; (/usr/lib/nodejs/carto/lib/carto/tree/reference.js:213:3)
at Module._compile (module.js:456:26)
at Object.Module._extensions..js (module.js:474:10)
at Module.load (module.js:356:32)
at Function.Module._load (module.js:312:12)
at Module.require (module.js:364:17)
at require (module.js:380:17)
at exports.(anonymous function) (/usr/lib/nodejs/carto/lib/carto/index.js:73:5)</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span> <span class="post-tag tag-link-carto" rel="tag" title="see questions tagged &#39;carto&#39;">carto</span> <span class="post-tag tag-link-15.04" rel="tag" title="see questions tagged &#39;15.04&#39;">15.04</span> <span class="post-tag tag-link-ubuntu" rel="tag" title="see questions tagged &#39;ubuntu&#39;">ubuntu</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 May '15, 23:20</strong></p>
<img src="https://secure.gravatar.com/avatar/1afe4bf83008befdcf7bdf5c6abfa195?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="f00dl3a&#39;s gravatar image" />
<p><span>f00dl3a</span><br />
<span class="score" title="171 reputation points">171</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="f00dl3a has one accepted answer">25%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 May '15, 23:34</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-42816" class="comments-container">
<span id="42836"></span>
<div id="comment-42836" class="comment">
<div id="post-42836-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>(when anything goes wrong, suspect node.js)</p>
<p>What does "node -v" return? For info I'm seeing v0.10.37 on an Ubuntu 14.04 box with a PPA for node (see <a href="http://wiki.openstreetmap.org/wiki/User:SomeoneElse/Ubuntu_1404_tileserver#Things_that_need_nodejs">http://wiki.openstreetmap.org/wiki/User:SomeoneElse/Ubuntu_1404_tileserver#Things_that_need_nodejs</a> )</p>
</div>
<div id="comment-42836-info" class="comment-info">
<span class="comment-age">(03 May '15, 13:33)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="42838"></span>
<div id="comment-42838" class="comment">
<div id="post-42838-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Node -v (and node alone) does not return anything, justexits back to term, had to use nodejs -v -- returns 0.10.28</p>
</div>
<div id="comment-42838-info" class="comment-info">
<span class="comment-age">(03 May '15, 14:20)</span> <span class="comment-user userinfo">f00dl3a</span>
</div>
</div>
<span id="42856"></span>
<div id="comment-42856" class="comment">
<div id="post-42856-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Do you have the fix for the conflicting names for node(js) on Ubuntu installed?</p>
<p>sudo apt-get install nodejs-legacy</p>
<p>WHile I think it is very unlikely that it is causing the issue, who knows with node.js :-)</p>
</div>
<div id="comment-42856-info" class="comment-info">
<span class="comment-age">(03 May '15, 17:08)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="42857"></span>
<div id="comment-42857" class="comment">
<div id="post-42857-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That fixed the node problem but not the error.</p>
<p>v0.10.28 astump@astump-EX58-UD4P:~$ cd /usr/local/share/maps/style/OSMBright/ astump@astump-EX58-UD4P:/usr/local/share/maps/style/OSMBright$ carto project.mml &gt; OSMBright.xml</p>
<p>/usr/lib/nodejs/carto/lib/carto/tree/reference.js:19 if (mapnik_reference.version.hasOwnProperty(version)) { ^ TypeError: Cannot call method 'hasOwnProperty' of undefined at Object.ref.setVersion (/usr/lib/nodejs/carto/lib/carto/tree/reference.js:19 34) at /usr/lib/nodejs/carto/lib/carto/tree/reference.js:209:5 at Object.&lt;anonymous&gt; (/usr/lib/nodejs/carto/lib/carto/tree/reference.js:213:3 at Module._compile (module.js:456:26) at Object.Module._extensions..js (module.js:474:10) at Module.load (module.js:356:32) at Function.Module._load (module.js:312:12) at Module.require (module.js:364:17) at require (module.js:380:17) at exports.(anonymous function) (/usr/lib/nodejs/carto/lib/carto/index.js:73:5 Astump@astump-EX58-UD4P:/usr/local/share/maps/style/OSMBright$</p>
</div>
<div id="comment-42857-info" class="comment-info">
<span class="comment-age">(03 May '15, 17:39)</span> <span class="comment-user userinfo">f00dl3a</span>
</div>
</div>
<span id="42874"></span>
<div id="comment-42874" class="comment">
<div id="post-42874-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I thought maybe node didn't have mapnik installed so I did npm install -g carto and npm install -g mapnik, but that did not resolve the problem either. Still getting the same error message. I downloaded the 3.x version via npm install -g mapnik@3.x but still the same message. (mapnik_reference.version.hasOwnProperty(version))</p>
</div>
<div id="comment-42874-info" class="comment-info">
<span class="comment-age">(04 May '15, 16:43)</span> <span class="comment-user userinfo">f00dl3a</span>
</div>
</div>
</div>
<div id="comment-tools-42816" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42816-form-container" class="comment-form-container">
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

<span id="42948"></span>

<div id="answer-container-42948" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-42948-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42948-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-42948-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Fixed. Corrupt OS installation due to a failing SATA chip on the motherboard. Totally failed yesterday, and on the new system this error is no longer present.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 May '15, 03:53</strong></p>
<img src="https://secure.gravatar.com/avatar/1afe4bf83008befdcf7bdf5c6abfa195?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="f00dl3a&#39;s gravatar image" />
<p><span>f00dl3a</span><br />
<span class="score" title="171 reputation points">171</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="f00dl3a has one accepted answer">25%</span></p>
</div>
</div>
<div id="comments-container-42948" class="comments-container">
&#10;</div>
<div id="comment-tools-42948" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42948-form-container" class="comment-form-container">
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

