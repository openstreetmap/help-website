+++
type = "question"
title = "How do you  change the served region of a tileserver?"
description = '''Hi folks, I have been running a tileserver, which has been setup using this switch2osm manual on my old machine at home. It serves custom-style tiles for Berlin and it runs OK. I would like to change the region served and updated by mod_tile /osmosis on my test server from Berlin to e.g. Paris or Ba...'''
date = "2015-03-24T16:04:00Z"
lastmod = "2015-04-07T21:59:00Z"
weight = 41876
keywords = [ "tileserver", "mod_tile", "osm2pgsql", "postgis", "expiry" ]
aliases = [ "/questions/41876" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How do you change the served region of a tileserver?](/questions/41876/how-do-you-change-the-served-region-of-a-tileserver)

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
<span id="post-41876-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41876-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-41876-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi folks,</p>
<p>I have been running a tileserver, which has been setup using <a href="https://switch2osm.org/serving-tiles/building-a-tile-server-from-packages/">this</a> switch2osm manual on my old machine at home. It serves custom-style tiles for Berlin and it runs OK. I would like to change the region served and updated by mod_tile /osmosis on my test server from Berlin to e.g. Paris or Bavaria in one go.</p>
<p>Hence, I would not like the automatic expiry process (sudo -u www-data /usr/bin/openstreetmap-tiles-update-expire) to expire and delete my tiles. Rather I would like to quickly delete all tiles in the default tile directory and reset the expiry mechanism once I have updated the gisdatabase using osm2pgsql. I reckon this saves my weak old machine some time.</p>
<p>Does anyone know how to do this or has anyone even done this so far?</p>
<p>To be honest, I have already tried to do so and ended up being unable to update my new tileset, i.e. I am mainly looking for a way to reset the update mechanism, so that I don´t have to reinstall everything...</p>
<p>Thanks in advance!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span> <span class="post-tag tag-link-mod_tile" rel="tag" title="see questions tagged &#39;mod_tile&#39;">mod_tile</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span> <span class="post-tag tag-link-expiry" rel="tag" title="see questions tagged &#39;expiry&#39;">expiry</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Mar '15, 16:04</strong></p>
<img src="https://secure.gravatar.com/avatar/a59933fbd400bfa55911387fb188cb6e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="V_T_&#39;s gravatar image" />
<p><span>V_T_</span><br />
<span class="score" title="56 reputation points">56</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="V_T_ has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-41876" class="comments-container">
&#10;</div>
<div id="comment-tools-41876" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41876-form-container" class="comment-form-container">
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

<span id="41877"></span>

<div id="answer-container-41877" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-41877-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41877-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-41877-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>rm -r of the directory with the tiles</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Mar '15, 16:19</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-41877" class="comments-container">
<span id="41882"></span>
<div id="comment-41882" class="comment">
<div id="post-41882-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you, Simon,</p>
<p>this removes all my tiles.</p>
<p>In fact, I had already done so, but it does not solve my problem.</p>
<p>Let me explain a bit more:</p>
<p>I cannot remember to have done so but I must have deleted the dirty_tiles-folder as well. Whenever I run the tiles-update-expire script again it throws an error telling me that removing /var/lib/mod_tile/dirty_tiles.4900 (or the like) failed because such a file or directory could not be found.</p>
<p>How can I reset the update mechanism ?</p>
</div>
<div id="comment-41882-info" class="comment-info">
<span class="comment-age">(24 Mar '15, 17:18)</span> <span class="comment-user userinfo">V_T_</span>
</div>
</div>
<span id="41885"></span>
<div id="comment-41885" class="comment">
<div id="post-41885-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>does /var/lib/mod_tile still exist?</p>
</div>
<div id="comment-41885-info" class="comment-info">
<span class="comment-age">(24 Mar '15, 18:03)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="41888"></span>
<div id="comment-41888" class="comment">
<div id="post-41888-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, it does.</p>
</div>
<div id="comment-41888-info" class="comment-info">
<span class="comment-age">(24 Mar '15, 18:55)</span> <span class="comment-user userinfo">V_T_</span>
</div>
</div>
<span id="41904"></span>
<div id="comment-41904" class="comment">
<div id="post-41904-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>IMHO there is no "dirty_tiles" folder so this sounds slightly mysterious, are you sure that the permissions for the directories are still ok (typically owned by www-data, but your setup might vary).</p>
</div>
<div id="comment-41904-info" class="comment-info">
<span class="comment-age">(25 Mar '15, 10:48)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="41909"></span>
<div id="comment-41909" class="comment">
<div id="post-41909-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Permissions shouldn´t have changed, but I´ll check this. If it falis, I will have a look at my backups. Ín case I have stored the tile directory I will try to restore it.</p>
</div>
<div id="comment-41909-info" class="comment-info">
<span class="comment-age">(25 Mar '15, 11:35)</span> <span class="comment-user userinfo">V_T_</span>
</div>
</div>
<span id="41927"></span>
<div id="comment-41927" class="comment not_top_scorer">
<div id="post-41927-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Well, it seems as if I haven`t kept any backups for /var/lib/ . That means I am stuck at this point. Has anyone had any ideas ?</p>
</div>
<div id="comment-41927-info" class="comment-info">
<span class="comment-age">(26 Mar '15, 15:39)</span> <span class="comment-user userinfo">V_T_</span>
</div>
</div>
</div>
<div id="comment-tools-41877" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-41877-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="42173"></span>

<div id="answer-container-42173" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-42173-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42173-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-42173-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The whole confusion about my broken update mechanism and a missing 'dirty tiles' directory had been kicked off by me disregarding one important point in the referenced switch2osm manual - and SimonPoole was running in the right direction by argueing about missing permissions: I should have run the postgis permissions script, e.g.</p>
<p><code>sudo /usr/bin/install-postgis-osm-user.sh gis www-data</code></p>
<p>, on the database...</p>
<p>After doing so, all spooky dirty-tiles messages vanished and I can now change the served region as I like, including a proper updates-and-expiry mechanism. See also <a href="http://gis.stackexchange.com/questions/139874/how-to-switch-the-region-of-an-osm-tile-server-properly-how-to-reset-update-me">here</a></p>
<p>Thanks anyway for your headaches.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Apr '15, 21:59</strong></p>
<img src="https://secure.gravatar.com/avatar/a59933fbd400bfa55911387fb188cb6e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="V_T_&#39;s gravatar image" />
<p><span>V_T_</span><br />
<span class="score" title="56 reputation points">56</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="V_T_ has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-42173" class="comments-container">
&#10;</div>
<div id="comment-tools-42173" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42173-form-container" class="comment-form-container">
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

