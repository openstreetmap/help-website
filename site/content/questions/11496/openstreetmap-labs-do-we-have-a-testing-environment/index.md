+++
type = "question"
title = "Openstreetmap labs: Do we have a testing environment?"
description = '''Because I do not have the resources to set up my own local mapping server (basically lack of time and technical expertise) I am looking for a testing environment in order to learn more by &quot;hacking&quot;. I am the type of a man who is not able to install and set up complex software but is able to &quot;exploit...'''
date = "2012-03-25T21:27:00Z"
lastmod = "2012-03-28T09:01:00Z"
weight = 11496
keywords = [ "development", "test", "local", "mapnik", "server" ]
aliases = [ "/questions/11496" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Openstreetmap labs: Do we have a testing environment?](/questions/11496/openstreetmap-labs-do-we-have-a-testing-environment)

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
<span id="post-11496-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11496-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-11496-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Because I do not have the resources to set up my own local mapping server (basically lack of time and technical expertise) I am looking for a testing environment in order to learn more by "hacking". I am the type of a man who is not able to install and set up complex software but is able to "exploit" currently working system by altering various settings needed to get desired result (usualy small tweaks).</p>
<p>For instance I would like to learn how Mapnik stylesheets work with a sample set of OSM-like mapping data to be able to add rules for things that are new or still wait for their stylesheet rule. I found <a href="http://apis.dev.openstreetmap.org/">apis.dev.openstreetmap.org</a> page which looks like some testing sites. Can I use some of these for testing (import scripts, stylesheets etc.)? Do we have a kind of "labs" environment up? If not, are there any plans to have this?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-test" rel="tag" title="see questions tagged &#39;test&#39;">test</span> <span class="post-tag tag-link-local" rel="tag" title="see questions tagged &#39;local&#39;">local</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-server" rel="tag" title="see questions tagged &#39;server&#39;">server</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Mar '12, 21:27</strong></p>
<img src="https://secure.gravatar.com/avatar/7d327873d48d28e563c9ad7259853c35?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kozuch&#39;s gravatar image" />
<p><span>Kozuch</span><br />
<span class="score" title="1720 reputation points"><span>1.7k</span></span><span title="58 badges"><span class="badge1">●</span><span class="badgecount">58</span></span><span title="72 badges"><span class="silver">●</span><span class="badgecount">72</span></span><span title="85 badges"><span class="bronze">●</span><span class="badgecount">85</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kozuch has one accepted answer">8%</span></p>
</div>
</div>
<div id="comments-container-11496" class="comments-container">
&#10;</div>
<div id="comment-tools-11496" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11496-form-container" class="comment-form-container">
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

<span id="11497"></span>

<div id="answer-container-11497" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-11497-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11497-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-11497-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can use apis.dev.openstreetmap.org to run tests and experiments against the API, but there is no tile server connected to that so you won't see your changes on a map unless you make the map yourself! We don't have a ready-made Mapnik setup with database that you can use, but you can get an account on the "dev" server where the basic Mapnik software is already installed. You will still have to set up and populate your own database however, and install your own stylesheet. It is possible that another user of the dev server has already done that and that you can use their installation; a call-out on the "dev" mailing list might help.</p>
<p>Note however that a typical osm2pgsql database does not include all features so a database set up by someone else might not actually meet your requirements if you want to write rules for things that aren't on the map yet. You might really have to create your own database with osm2pgsql - but at least on the dev server all the tools are already installed.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Mar '12, 22:31</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-11497" class="comments-container">
<span id="11501"></span>
<div id="comment-11501" class="comment">
<div id="post-11501-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Sorry for being all talk and no action, but it'd be nice if there was a ready-made VM somewhere with the usual tools installed. If I ever come around to making one, I'll let people know :)</p>
</div>
<div id="comment-11501-info" class="comment-info">
<span class="comment-age">(26 Mar '12, 10:49)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
<span id="11543"></span>
<div id="comment-11543" class="comment">
<div id="post-11543-score" class="comment-score">
4
</div>
<div class="comment-text">
<p>There are Ubuntu packages for easy set up of the important tools. If your main operating system isn't Linux you can always install Ubuntu in a VM your self.</p>
<p>To play with the rendering style-sheet you will need to install a rendering tool-chain, which is best described at <a href="http://switch2osm.org/serving-tiles/building-a-tile-server-from-packages/">http://switch2osm.org/serving-tiles/building-a-tile-server-from-packages/</a></p>
<p>If you want to play with the Data-API e.g. to test import scripts, you can either use apis.dev.openstreetmap, or again use Ubuntu packages to set up the "rails_port" (The software running the website and API) wiki.osm.org/wiki/Rails_port</p>
</div>
<div id="comment-11543-info" class="comment-info">
<span class="comment-age">(28 Mar '12, 09:01)</span> <span class="comment-user userinfo">apmon</span>
</div>
</div>
</div>
<div id="comment-tools-11497" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11497-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="11498"></span>

<div id="answer-container-11498" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-11498-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11498-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-11498-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The OSMF does not have the funds to give any easy development environment to anyone. The dev.osm.org server is only for internal development.</p>
<p>You should try to test with smaler extracts or even shape files. I have a working instance of the tile rendering framework on my smal laptop, but only with an extract and with performance ok for one user.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Mar '12, 23:11</strong></p>
<img src="https://secure.gravatar.com/avatar/44a4438f0146dfd898e24c221fd28b58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gnonthgol&#39;s gravatar image" />
<p><span>Gnonthgol ♦</span><br />
<span class="score" title="13750 reputation points"><span>13.8k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="103 badges"><span class="silver">●</span><span class="badgecount">103</span></span><span title="198 badges"><span class="bronze">●</span><span class="badgecount">198</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gnonthgol has 57 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-11498" class="comments-container">
&#10;</div>
<div id="comment-tools-11498" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11498-form-container" class="comment-form-container">
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

