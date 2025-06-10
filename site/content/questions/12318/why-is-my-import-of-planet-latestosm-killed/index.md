+++
type = "question"
title = "Why is my import of planet-latest.osm KILLED?"
description = '''Hey Guys! When trying to import the planet-latest.osm via osm2pgsql into PostGIS I receive the following problem. http://dpaste.org/ftsj8/ Can anybody guess, how to solve it? Greetings, Matze'''
date = "2012-04-24T11:06:00Z"
lastmod = "2012-04-25T10:57:00Z"
weight = 12318
keywords = [ "planet", "import", "postgresql", "osm2pgsql", "postgis" ]
aliases = [ "/questions/12318" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Why is my import of planet-latest.osm KILLED?](/questions/12318/why-is-my-import-of-planet-latestosm-killed)

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
<span id="post-12318-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12318-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-12318-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hey Guys!</p>
<p>When trying to import the planet-latest.osm via osm2pgsql into PostGIS I receive the following problem.</p>
<p><a href="http://dpaste.org/ftsj8/">http://dpaste.org/ftsj8/</a></p>
<p>Can anybody guess, how to solve it?</p>
<p>Greetings, Matze</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-planet" rel="tag" title="see questions tagged &#39;planet&#39;">planet</span> <span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Apr '12, 11:06</strong></p>
<img src="https://secure.gravatar.com/avatar/cc0198a02af3c41ad04b61e028c3b126?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MHein&#39;s gravatar image" />
<p><span>MHein</span><br />
<span class="score" title="141 reputation points">141</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MHein has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Aug '13, 11:40</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0c12497903c6f3b2dd9f4d87deb127de?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MagicFab&#39;s gravatar image" />
<p><span>MagicFab</span><br />
<span class="score" title="935 reputation points">935</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="22 badges"><span class="bronze">●</span><span class="badgecount">22</span></span></p>
</div>
</div>
<div id="comments-container-12318" class="comments-container">
<span id="12328"></span>
<div id="comment-12328" class="comment">
<div id="post-12328-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Not an answer but a question - just checking that you really do want to import the whole planet, i.e. you want to render a map of the world, not a small part of it?</p>
</div>
<div id="comment-12328-info" class="comment-info">
<span class="comment-age">(24 Apr '12, 13:14)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-12318" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12318-form-container" class="comment-form-container">
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

<span id="12332"></span>

<div id="answer-container-12332" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-12332-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12332-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-12332-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="MHein has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Please take <a href="http://switch2osm.org/serving-tiles/">http://switch2osm.org/serving-tiles/</a> "System Requirements" seriously.</p>
<p>Importing a full planet doesn't need an awful lot of resources in the grand scheme of things, but you will not be able to avoid allocating enough disk space (at least 300GB for the rendering database), and multiple GBs (as in more than 8) of memory.</p>
<p>Trying to skimp on this is a waste of your and other peoples time.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Apr '12, 13:49</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Apr '12, 14:00</strong> </span></p>
</div>
</div>
<div id="comments-container-12332" class="comments-container">
<span id="12350"></span>
<div id="comment-12350" class="comment">
<div id="post-12350-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>does anyone have more than 8GB of RAM in an normal PC?</p>
<p>IFAIK WinXP isn't able to cope with more than 2GB of RAM, is it?</p>
<p>Does this mean, that I won't be able to set up a Postgresql/PostGIS - database of the whole planet-file on my computer? Or is there a way to osm2pgsql it? A way that maybe takes much more time and maybe more disk space but doesn't need more RAM?</p>
</div>
<div id="comment-12350-info" class="comment-info">
<span class="comment-age">(25 Apr '12, 09:59)</span> <span class="comment-user userinfo">MHein</span>
</div>
</div>
<span id="12352"></span>
<div id="comment-12352" class="comment">
<div id="post-12352-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>The setup that you're using** (Windows XP VM host with 2Gb of RAM hosting a Linux VM with ~1Gb RAM and ~20Gb disk) is woefully inadequate for a full planet import.</p>
<p>However, it will allow you to become familiar with the tools involved - working out what you need to do to manage the database, using osm2pgsql to append rather than recreate (there are some list discussions on that that you can find with a web search).</p>
<p>** from the IRC discussion</p>
</div>
<div id="comment-12352-info" class="comment-info">
<span class="comment-age">(25 Apr '12, 10:57)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-12332" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12332-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="12321"></span>

<div id="answer-container-12321" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-12321-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12321-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-12321-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>osm2pgsql was likely killed due to being out of memory. Reduce the -C 12000 to a significantly lower number and try again.</p>
<p>dmesg will likely show if the process was killed by the OutOfMemory (OOM) killer.</p>
</div>
<div class="answer-controls post-controls">
<div class="community-wiki">
This answer is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Apr '12, 12:13</strong></p>
<img src="https://secure.gravatar.com/avatar/e79628d44a15e95c607f8c5007d0ccd2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Firefishy&#39;s gravatar image" />
<p><span>Firefishy ♦♦</span><br />
<span class="score" title="1296 reputation points"><span>1.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="36 badges"><span class="silver">●</span><span class="badgecount">36</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Firefishy has 14 accepted answers">29%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Apr '12, 13:40</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span></p>
</div>
</div>
<div id="comments-container-12321" class="comments-container">
<span id="12322"></span>
<div id="comment-12322" class="comment">
<div id="post-12322-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>In <a href="http://switch2osm.org/serving-tiles/building-a-tile-server-from-packages/">http://switch2osm.org/serving-tiles/building-a-tile-server-from-packages/</a> it says:</p>
<p>Depending on the size of the extract you are importing and the performance of the computer, this can take anywhere from a few minutes for small extracts up to several days for the full planet on slower hardware! If you are importing the full planet, it is strongly recommended to set -C 12000 (may increase as the OSM database grows).</p>
<p>Did I missunderstand it?</p>
</div>
<div id="comment-12322-info" class="comment-info">
<span class="comment-age">(24 Apr '12, 12:16)</span> <span class="comment-user userinfo">MHein</span>
</div>
</div>
<span id="12324"></span>
<div id="comment-12324" class="comment">
<div id="post-12324-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>No, you didn't misunderstand, but you still need enough memory or/and swap to cater for the 12 GB of node cache. If necessary add a swap file of appropriate size.</p>
</div>
<div id="comment-12324-info" class="comment-info">
<span class="comment-age">(24 Apr '12, 12:22)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="12327"></span>
<div id="comment-12327" class="comment">
<div id="post-12327-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>how can I add a swapfile of appropriate size?</p>
<p>How much memory on disk do I need for the Postgresql Database including the planet.osm-file?</p>
<p>And how is "dmesg" used?</p>
</div>
<div id="comment-12327-info" class="comment-info">
<span class="comment-age">(24 Apr '12, 12:46)</span> <span class="comment-user userinfo">MHein</span>
</div>
</div>
</div>
<div id="comment-tools-12321" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12321-form-container" class="comment-form-container">
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

