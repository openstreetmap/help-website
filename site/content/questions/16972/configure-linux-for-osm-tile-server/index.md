+++
type = "question"
title = "Configure Linux for OSM Tile Server"
description = '''Background: I am a Linux newbie. I have set up an OSM planet import and pre-rendered alot of the planet on a Windows machine. Now I want to take the next step and move to a Linux box so I can render tiles on the fly and use things like mod_tile to keep my database up to date via http://switch2osm.or...'''
date = "2012-10-17T19:39:00Z"
lastmod = "2014-06-27T16:10:00Z"
weight = 16972
keywords = [ "tileserver", "server", "linux" ]
aliases = [ "/questions/16972" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Configure Linux for OSM Tile Server](/questions/16972/configure-linux-for-osm-tile-server)

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
<span id="post-16972-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16972-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-16972-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Background: I am a Linux newbie. I have set up an OSM planet import and pre-rendered alot of the planet on a Windows machine. Now I want to take the next step and move to a Linux box so I can render tiles on the fly and use things like mod_tile to keep my database up to date via <a href="http://switch2osm.org/serving-tiles/manually-building-a-tile-server-12-04/">http://switch2osm.org/serving-tiles/manually-building-a-tile-server-12-04/</a> .</p>
<p>Questions:</p>
<ol>
<li>My company's IT is setting up a virtual Linux box for me to test/play on with 500 GB of space. They have asked me some questions about the Linux configuration that I need help on. What filesystem should I create in Linux? After some research I came up with either XFS or JFS using the FHS standard. XFS or JFS and not ext3 becuase something about the number of inodes available in ext3 could run out after millions of tiles causing my system to become logically out of space??? Does this make sense and does anyone have any suggestions on this?</li>
<li>They also asked me how I want my 500GB allocated to each volume inside the filesystem, mentioning terms like "UO1". I have no idea what this means or how to answer. Can someone help me?</li>
<li>My company only supports Redhat. Does anyone know if Redhat will impose any issues regarding the questions above or following the instructions at <a href="http://switch2osm.org/serving-tiles/manually-building-a-tile-server-12-04/">http://switch2osm.org/serving-tiles/manually-building-a-tile-server-12-04/</a> ?</li>
</ol>
<p>Thanks, Matt</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span> <span class="post-tag tag-link-server" rel="tag" title="see questions tagged &#39;server&#39;">server</span> <span class="post-tag tag-link-linux" rel="tag" title="see questions tagged &#39;linux&#39;">linux</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Oct '12, 19:39</strong></p>
<img src="https://secure.gravatar.com/avatar/fbb15843641ffaf1c2259cc7ebb4735c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maw269&#39;s gravatar image" />
<p><span>maw269</span><br />
<span class="score" title="115 reputation points">115</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maw269 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Nov '13, 14:49</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-16972" class="comments-container">
<span id="16974"></span>
<div id="comment-16974" class="comment">
<div id="post-16974-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'm not a filesystem expert but <em>ext4</em> with the <em>dir_index</em> option should suffice.</p>
</div>
<div id="comment-16974-info" class="comment-info">
<span class="comment-age">(17 Oct '12, 20:05)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="16991"></span>
<div id="comment-16991" class="comment">
<div id="post-16991-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Well Redhat uses a different package manager than Ubuntu so those two "apt-get" commands at the beginning aren't going to work. I haven't used Redhat in a while but I think it has a "yum" command that will install packages much like apt-get does. Package names and versions might not match up exactly either although I would imagine that they would be fairly close.</p>
</div>
<div id="comment-16991-info" class="comment-info">
<span class="comment-age">(18 Oct '12, 05:42)</span> <span class="comment-user userinfo">ToeBee</span>
</div>
</div>
<span id="34382"></span>
<div id="comment-34382" class="comment">
<div id="post-34382-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Were you able to implement this on Redhat? If yes, can you please share what challenges you faced, and the workaround you had to use? Thank you in advance.</p>
</div>
<div id="comment-34382-info" class="comment-info">
<span class="comment-age">(27 Jun '14, 16:10)</span> <span class="comment-user userinfo">dk2005</span>
</div>
</div>
</div>
<div id="comment-tools-16972" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16972-form-container" class="comment-form-container">
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

<span id="16994"></span>

<div id="answer-container-16994" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-16994-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16994-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-16994-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="maw269 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I suspect that it's not going to be straightforward. The <a href="http://switch2osm.org/serving-tiles/manually-building-a-tile-server-12-04/">switch2osm instructions</a> say "get XYZ from Ubuntu, build ABC from source". I'm guessing that you'd get two sorts of problems:</p>
<ul>
<li>Your Redhat version may have versions of packages to what are in Ubuntu 12.04, which work differently, or some may not be available.<br />
</li>
<li>There may filesystem differences for e.g. Apache which means that you need to play around with e.g. mod_tile to get it to work. If you don't have a local Ubuntu system to compare with resolving this may be tricky.</li>
</ul>
<p>I'd be tempted to progress to a "planet import and update in Redhat" in stages:</p>
<ol>
<li>First of all create a small VM somewhere (perhaps at home) and install Ubuntu in it, and then run through the switch2osm instructions, but using a very small country as the import data. Get rendering and updates to it working.</li>
<li>Do the same again, but with Redhat. You'll probably need to figure out where to get some packages and versions from, and probably build more from source. You'll also need to compare file locations between Ubuntu and Redhat, and edit config files and rebuild accordingly.</li>
<li>Once you've done that you should be able to scale up to a larger VM and be able to at least understand the questions your IT department (bless 'em) are asking.</li>
</ol>
<p>With regard to the specific questions:</p>
<ul>
<li>I believe that the way that rendered tiles are stored was changed a year or more ago, so I suspect running out of inodes on ext3 is unlikely to be an issue, at least in stage (2) above.</li>
<li>A poke around on the Internet suggests that "u01", "u02" etc. are Redhat's way of specifying "/usr" etc. When doing (2) if everything is on one partition no part will run out of space first and you can see where stuff goes, and modify install scripts accordingly if necessary.</li>
</ul>
<p>(I've not used a Redhat system for around 10 years, so take this answer with a large pinch of salt!)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Oct '12, 10:16</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Nov '13, 14:49</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-16994" class="comments-container">
<span id="16999"></span>
<div id="comment-16999" class="comment">
<div id="post-16999-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Excellent suggestions everyone. I will start with Ubuntu then transition to Redhat (fingers crossed). I will start small and not worry so much about disk allocation at this moment. Once I have everything up and running, I can get a feel for the actual space required for items that will not grow (applications) and also get a feel for the % of space required for items that will grow when moving to larger geographies (the DB and tilestore). I can then scale this space accordingly.</p>
<p>It also sounds like I will have to do some research to find Redhat eqivalents to Ubuntu commands. I hope I don't have to build too many things from source as that is out of my lane, but I have some developers at the office that can help me, I suppose.</p>
<p>I will get back to this forum if I get things working and maybe create a page somewhere with the Redhat eqivalent to <a href="http://switch2osm.org/serving-tiles/manually-building-a-tile-server-12-04/.">http://switch2osm.org/serving-tiles/manually-building-a-tile-server-12-04/.</a></p>
<p>If you come by this page in the future and don't find my final results, ping me because I probably forgot to update this page. Cheers</p>
</div>
<div id="comment-16999-info" class="comment-info">
<span class="comment-age">(18 Oct '12, 17:50)</span> <span class="comment-user userinfo">maw269</span>
</div>
</div>
<span id="20287"></span>
<div id="comment-20287" class="comment">
<div id="post-20287-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Well, I've gotten all the way to installing mapnik0.7.3 and creating a static image with generate_image.py. No luck so far with getting mod_tile to compile. Not looking good :-(</p>
</div>
<div id="comment-20287-info" class="comment-info">
<span class="comment-age">(25 Feb '13, 22:32)</span> <span class="comment-user userinfo">maw269</span>
</div>
</div>
</div>
<div id="comment-tools-16994" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16994-form-container" class="comment-form-container">
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

