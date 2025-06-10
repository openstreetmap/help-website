+++
type = "question"
title = "What is an easy way to test my OSM tile server?"
description = '''it has been several days of waiting, and it looks like my tile server is finally up and running, but I&#x27;m not seeing what I expected. what is the easiest way to view m maps now to really test and make sure the server is working correctly. I have some software that I built the OSM Server for, but that...'''
date = "2018-08-01T06:26:00Z"
lastmod = "2018-08-06T21:17:00Z"
weight = 65051
keywords = [ "rendering", "viewing", "tileserver" ]
aliases = [ "/questions/65051" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [What is an easy way to test my OSM tile server?](/questions/65051/what-is-an-easy-way-to-test-my-osm-tile-server)

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
<span id="post-65051-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65051-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65051-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>it has been several days of waiting, and it looks like my tile server is finally up and running, but I'm not seeing what I expected. what is the easiest way to view m maps now to really test and make sure the server is working correctly. I have some software that I built the OSM Server for, but that is not working right now and I want to be sure that the tile server is doing what it supposed to be doing. If I brows to <a href="http://192.168.1.24/hot/0/0/0.png,">http://192.168.1.24/hot/0/0/0.png,</a> I do get a plain White and blue map image of the world, but I have loaded north america, and was expecting to see something a bit more detailed. If I watch on the command line and monitor the rendering, I can change the z/x/y settings and see renderd and debug lines come up, but I'm still not getting a detailed map of anything. Is there an easy way to dump the tiles to a website to view the map?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-viewing" rel="tag" title="see questions tagged &#39;viewing&#39;">viewing</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Aug '18, 06:26</strong></p>
<img src="https://secure.gravatar.com/avatar/231ce5a82292640ac0faa68994879c84?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="KD7VEA&#39;s gravatar image" />
<p><span>KD7VEA</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="KD7VEA has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Aug '18, 10:30</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-65051" class="comments-container">
&#10;</div>
<div id="comment-tools-65051" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65051-form-container" class="comment-form-container">
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

<span id="65056"></span>

<div id="answer-container-65056" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-65056-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65056-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-65056-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Simply set up a small web page with OpenLayers or Leaflet (e.g. <a href="https://wiki.openstreetmap.org/wiki/OpenLayers_Simple_Example,">https://wiki.openstreetmap.org/wiki/OpenLayers_Simple_Example,</a> follow instructions under "Other tile sets" to add your own tiles). You could even BBBike's map compare service and add your own server as an extra layer (<a href="https://mc.bbbike.org/mc/">https://mc.bbbike.org/mc/</a> then follow "console" link in the footer to add your own tile URL). Needless to say, both depend on your tile server being accessible from wherever you run the browser.</p>
<p>A "white and blue world map but no details" usually means that your rendering toolchain works in principle, but the renderer cannot access the database right; either your database is empty, or you have configured the renderer to access a wrong one, or your data is in the wrong projection and therefore all appears at 0;0, something like that.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Aug '18, 09:15</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-65056" class="comments-container">
<span id="65085"></span>
<div id="comment-65085" class="comment">
<div id="post-65085-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ifollowed the instructions from <a href="https://switch2osm.org/manually-building-a-tile-server-18-04-lts/">https://switch2osm.org/manually-building-a-tile-server-18-04-lts/</a> , but I changed the username from renderaccount, and wonder if I missed a setting somewhere and left one of the usernames set as renderaccount instead of my new account. would you have a good starting point to see if it was missed somewhere. usually when I hit a roadblock like this, I will wipe the drive and reinstall, but now with all of the data that took days to render, I don't want to restart if I don't have to.</p>
</div>
<div id="comment-65085-info" class="comment-info">
<span class="comment-age">(02 Aug '18, 20:13)</span> <span class="comment-user userinfo">KD7VEA</span>
</div>
</div>
</div>
<div id="comment-tools-65056" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65056-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="65171"></span>

<div id="answer-container-65171" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-65171-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65171-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65171-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are a few other things that you can do. I'd start with these:</p>
<p>1) You can try and search for some data that should have been loaded, such as <a href="https://www.openstreetmap.org/node/151398920">this node</a> (a city in Nebraska):</p>
<pre><code>psql gis
gis=&gt; SELECT * FROM planet_osm_nodes WHERE (id = 151398920);</code></pre>
<p>It should come back and provide details and say "(1 row)".</p>
<p>2) You can look at what's happening in the syslog file and investigate any errors in there.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Aug '18, 21:17</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-65171" class="comments-container">
&#10;</div>
<div id="comment-tools-65171" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65171-form-container" class="comment-form-container">
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

