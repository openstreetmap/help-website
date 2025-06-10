+++
type = "question"
title = "freaking mapnik! (error renderd, no datasource for type: &#x27;postgis&#x27; )"
description = '''Recently I was assigned with a task of setting up a portable offline OSM tile server.  So naturally I went there:  https://switch2osm.org/serving-tiles/manually-building-a-tile-server-18-04-lts/ And tried to follow all the instructions on a virtual machine. (a VDI image with Ubuntu 19.10) And there ...'''
date = "2020-02-21T13:27:00Z"
lastmod = "2020-02-21T16:52:00Z"
weight = 73178
keywords = [ "renderd", "postgis", "mapnik" ]
aliases = [ "/questions/73178" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [freaking mapnik! (error renderd, no datasource for type: 'postgis' )](/questions/73178/freaking-mapnik-error-renderd-no-datasource-for-type-postgis)

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
<span id="post-73178-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73178-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73178-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Recently I was assigned with a task of setting up a portable offline OSM tile server. So naturally I went there:</p>
<p><a href="https://switch2osm.org/serving-tiles/manually-building-a-tile-server-18-04-lts/"><code>https://switch2osm.org/serving-tiles/manually-building-a-tile-server-18-04-lts/</code></a></p>
<p>And tried to follow all the instructions on a virtual machine. (a VDI image with Ubuntu 19.10) And there I had soooooo much PAIN trying to install this freaking Mapnik thing! Literally I'm going to f*cking hate this name for god knows how long...but that's not the point. The point is that after I managed to install it using "pip", everything went smoothly until I tried to execute</p>
<pre><code>renderd -f -c /usr/local/etc/renderd.conf</code></pre>
<p>There I got in trouble once again as the following errors popped:</p>
<pre><code>renderd[15908]: An error occurred while loading the map layer &#39;ajt&#39;: Could not create datasource for type: &#39;postgis&#39; (no datasource plugin directories have been successfully registered)  encountered during parsing of layer &#39;landcover-low-zoom&#39; in Layer of &#39;/home/osboxes/src/openstreetmap-carto/mapnik.xml&#39;</code></pre>
<p>After some searching I found this topic:</p>
<pre><code>https://github.com/mapnik/node-mapnik/issues/311</code></pre>
<p>which hinted that I should</p>
<pre><code>`Try calling mapnik.register_default_input_plugins(); at the top of your script.`</code></pre>
<p>But where in the hell should I put this line I don't understand! I have no script. I suppose I have to launch python and somehow run it there but I haven't figured out how to do this. I could have gone and tried learning python to figure this out, sure, but this thing is taking too much time already and I don't think it should.</p>
<p>So I thought maybe somebody could help me out with this.</p>
<p>ALthough I anticipate a sh#tstorm coming my way about how incompetent I am and how I should go read the f<em>cking manual (which one, god damn it!). I definitely could have chosen words more carefully but f</em>ck this, I am so sick of this cr@p. This freaking mapnik! Why does it have to take so much attention on itself!</p>
<p>P.S. I had to install postgres 11 because my packet manager didn't see version 10. And when I was compiling a "mode_tile" module I commented out whe whole "gen_tile_test.cpp" because it failed to find guess what...A FREAKING <code>#include &lt;mapnik/box2d.hpp&gt;</code>!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Feb '20, 13:27</strong></p>
<img src="https://secure.gravatar.com/avatar/7d9dea8db6c9981b45d28f28bb29f49d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kartman1&#39;s gravatar image" />
<p><span>kartman1</span><br />
<span class="score" title="38 reputation points">38</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kartman1 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Feb '20, 13:31</strong> </span></p>
</div>
</div>
<div id="comments-container-73178" class="comments-container">
<span id="73179"></span>
<div id="comment-73179" class="comment">
<div id="post-73179-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>This forum is for questions which can be answered, not rants about your software installation experience. I note that you were installing on an entirely different version of the Operating System rather than 18.04 LTS: it is only to be expected that some things may have changed.</p>
</div>
<div id="comment-73179-info" class="comment-info">
<span class="comment-age">(21 Feb '20, 13:34)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="73180"></span>
<div id="comment-73180" class="comment">
<div id="post-73180-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ok, my bad, I ll go and try this with 18.04=( although it's strange that fundamentally most things worked as expected and yet they didn't</p>
</div>
<div id="comment-73180-info" class="comment-info">
<span class="comment-age">(21 Feb '20, 13:44)</span> <span class="comment-user userinfo">kartman1</span>
</div>
</div>
<span id="73181"></span>
<div id="comment-73181" class="comment">
<div id="post-73181-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>This is not strange at all. Your error message seems to point at Mapnik's PostGIS plugin not being found, likely because it has not been installed (sometimes, between distributions, packages are split up in several parts and where you only needed to install one in version A you now need to install three in version B) or because it resides in a different directory than anticipated. Your swearing is inappropriate, even more so as you already suspected, when writing your message, that you might be criticised for it!</p>
</div>
<div id="comment-73181-info" class="comment-info">
<span class="comment-age">(21 Feb '20, 14:13)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-73178" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73178-form-container" class="comment-form-container">
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

<span id="73182"></span>

<div id="answer-container-73182" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73182-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73182-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-73182-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="kartman1 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Perhaps this paragraph</p>
<pre><code>Note that these instructions are have been written and tested against a newly-installed Ubuntu 18.04 server. If you have got other versions of some software already installed (perhaps you upgraded from an earlier Ubuntu version, or you set up some PPAs to load from) then you may need to make some adjustments</code></pre>
<p>overdoes the "British reserve" somewhat (disclaimer - I wrote it). Maybe it should say "depending on where you are starting from, you may be in a whole world of pain".</p>
<p>It doesn't surprise me that you've had issues with Ubuntu 19. My experience with earlier Ubuntu interim releases haven't always been positive - I get the feeling that Ubuntu uses them to "throw functionality at the wall and see what sticks", which you probably don't want to be dealing with if you want a server to be around for more than a few months.</p>
<p>There's a new LTS version out this year, and I expect that we'll update the switch2osm guides once we've got something that works. Ubuntu 18.04 LTS is due to be receive regular support through <a href="https://ubuntu.com/about/release-cycle">2023</a> though, so there's no hurry.</p>
</div>
<div class="answer-controls post-controls">
<div class="community-wiki">
This answer is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Feb '20, 14:14</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Feb '20, 10:33</strong> </span></p>
</div>
</div>
<div id="comments-container-73182" class="comments-container">
<span id="73184"></span>
<div id="comment-73184" class="comment">
<div id="post-73184-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Yeah it worked on Ubuntu 18.04.3 Bionic Beaver (64bit). Although there was an error in a "sudo apt install npm nodejs" line: npm didn't want to install because one of its dependencies was broken. Luckly though there was a topic just on that matter (<a href="https://askubuntu.com/questions/1088662/npm-depends-node-gyp-0-10-9-but-it-is-not-going-to-be-installed)">https://askubuntu.com/questions/1088662/npm-depends-node-gyp-0-10-9-but-it-is-not-going-to-be-installed)</a> So I did "sudo apt-get install nodejs-dev node-gyp libssl1.0-dev" and it all worked. Although I had "default-libmysqlclient-dev libgdal-dev libmapnik-dev libmysqlclient-dev libssl-dev" removed in the process. I really hope that "libmapnik-dev" is not going to backfire... Thanks!</p>
</div>
<div id="comment-73184-info" class="comment-info">
<span class="comment-age">(21 Feb '20, 15:08)</span> <span class="comment-user userinfo">kartman1</span>
</div>
</div>
<span id="73185"></span>
<div id="comment-73185" class="comment">
<div id="post-73185-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You can test whether the lack of libmapnik-dev will cause a problem by building some other software that might need it locally (but not doing a "make install" or similar).</p>
<p>"node" changes every 5 mins - maybe we need to revisit that bit of the instructions. They're in github, so you can make a pull request there. There's one other postgres version oddity as an issue already, I think.</p>
</div>
<div id="comment-73185-info" class="comment-info">
<span class="comment-age">(21 Feb '20, 16:52)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-73182" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73182-form-container" class="comment-form-container">
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

