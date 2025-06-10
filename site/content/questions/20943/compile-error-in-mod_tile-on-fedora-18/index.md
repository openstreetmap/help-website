+++
type = "question"
title = "compile error in mod_tile on fedora 18"
description = '''I am going through the process of building a map server on fedora 18 (cos that is what I&#x27;ve got, so don&#x27;t ask) and got an error building mod_map : apxs:Error: Command failed with rc=65536 When I switched off the compiler warnings it showed this error from libtool: ./mod_tile.c:661:28: error: &#x27;conn_r...'''
date = "2013-03-23T23:24:00Z"
lastmod = "2013-03-26T22:01:00Z"
weight = 20943
keywords = [ "mod_map", "mod_tile.c", "mod_authnz_external" ]
aliases = [ "/questions/20943" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [compile error in mod_tile on fedora 18](/questions/20943/compile-error-in-mod_tile-on-fedora-18)

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
<span id="post-20943-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20943-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-20943-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am going through the process of building a map server on fedora 18 (cos that is what I've got, so don't ask) and got an error building mod_map : apxs:Error: Command failed with rc=65536</p>
<p>When I switched off the compiler warnings it showed this error from libtool: ./mod_tile.c:661:28: error: 'conn_rec' has no member named 'remote_ip'</p>
<p>This is a described in <a href="https://code.google.com/p/mod-auth-external/issues/detail?id=8">https://code.google.com/p/mod-auth-external/issues/detail?id=8</a> Where they helpfully write: "The remote_ip field in the conn_rec structure was removed in Apache 2.4.1 and replaced with client_ip and useragent_ip."</p>
<p>In mod_tile.c I replaced the 3 occurrences of remote_ip with client_ip and the mod compiled. great. But i dont know yet if it will run. Still, I thought I ought to tell someone... you probably know all this already I am sure, but if not could you pass this on to a developer? I don't know who that might be. I have only just started playing around with this stuff and don't know my way around. Oh, and I downloaded the code about 4 hours ago and I am writing this on Sat Mar 23 23:19:58 GMT 2013 so goodnight.</p>
<p>Panca Kanga</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-mod_map" rel="tag" title="see questions tagged &#39;mod_map&#39;">mod_map</span> <span class="post-tag tag-link-mod_tile.c" rel="tag" title="see questions tagged &#39;mod_tile.c&#39;">mod_tile.c</span> <span class="post-tag tag-link-mod_authnz_external" rel="tag" title="see questions tagged &#39;mod_authnz_external&#39;">mod_authnz_external</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Mar '13, 23:24</strong></p>
<img src="https://secure.gravatar.com/avatar/1bca123c0c1f7ff52cb5ac0972837cc7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Panca%20Kanga&#39;s gravatar image" />
<p><span>Panca Kanga</span><br />
<span class="score" title="30 reputation points">30</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Panca Kanga has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-20943" class="comments-container">
&#10;</div>
<div id="comment-tools-20943" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20943-form-container" class="comment-form-container">
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

<span id="20963"></span>

<div id="answer-container-20963" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-20963-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20963-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-20963-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>mod_tile should now compile with apache 2.4. If there are any additional fixes required to build mod_tile on Fedora 18, please let me know.</p>
<p>Thank you for reporting the issue.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Mar '13, 02:29</strong></p>
<img src="https://secure.gravatar.com/avatar/32c974c4ca8b246698c2b82c64924da5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="apmon&#39;s gravatar image" />
<p><span>apmon</span><br />
<span class="score" title="6527 reputation points"><span>6.5k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="44 badges"><span class="silver">●</span><span class="badgecount">44</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="apmon has 9 accepted answers">20%</span></p>
</div>
</div>
<div id="comments-container-20963" class="comments-container">
<span id="20974"></span>
<div id="comment-20974" class="comment">
<div id="post-20974-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for working on it so quickly. It compiled and installed under my fedora 18 system. I am just working through the steps at <a href="http://switch2osm.org/serving-tiles/manually-building-a-tile-server-12-04/">http://switch2osm.org/serving-tiles/manually-building-a-tile-server-12-04/</a> It seems very clearly written though I keep making silly mistakes. I should just follow the instructions and not mess about. I think I will download the UK tonight and wait and see how it goes with that map set installed. Currently renderd says it is writing mod_tile/default/0/0/0/0/0/0.meta but httpd cannot see it and when I look it is not there. Maybe because I have installed a too small dataset (of Nepal.) I am not writing expecting an `answer' BTW.</p>
</div>
<div id="comment-20974-info" class="comment-info">
<span class="comment-age">(25 Mar '13, 21:43)</span> <span class="comment-user userinfo">Panca Kanga</span>
</div>
</div>
<span id="21006"></span>
<div id="comment-21006" class="comment">
<div id="post-21006-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Sorry, there was another bug in renderd, that caused tiles to not be written out. This should be fixed now as well.</p>
</div>
<div id="comment-21006-info" class="comment-info">
<span class="comment-age">(26 Mar '13, 16:43)</span> <span class="comment-user userinfo">apmon</span>
</div>
</div>
<span id="21013"></span>
<div id="comment-21013" class="comment">
<div id="post-21013-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Oh, it was a little bug was it? I thought it was me. I had moved the install to another disk, and also I was switching selinux on and off trying various ways of setting <em>that</em>. The recompile with the V.29407 code does indeed get everything going. Yep, there is the world at 0/0/0. Excellent. I am only installing the map server at home for my own satisfaction and not expecting a 4-hour call-out on a bug report! However I am sure this speedy fix will help others with more serious needs. I am still grateful though. Thanx. Hmm ... But no sign of Nepal yet... I think I had better get England into the db and then see where I can find. I downloaded England last night and I will let it load in tonight. Panca Kanga.</p>
</div>
<div id="comment-21013-info" class="comment-info">
<span class="comment-age">(26 Mar '13, 22:01)</span> <span class="comment-user userinfo">Panca Kanga</span>
</div>
</div>
</div>
<div id="comment-tools-20963" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20963-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="20956"></span>

<div id="answer-container-20956" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-20956-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20956-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-20956-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I found this patch this afternoon: <a href="http://www.michael-joost.de/mod_tile_apache2.4.patch">http://www.michael-joost.de/mod_tile_apache2.4.patch</a></p>
<p>It is provided to meet the errors like I was having yesterday and also sorts out the renamed unixd_set_global_perms. On top of that it fixes the compiler warnings about getting long int instead of apr_uint64_t &amp;etc. Except unfortunately it does not apply correctly to my copy of mod_tile.c extracted from build 29393. (I assume it is intended to be applied with the gnu patch(1)). However not quite working does not matter 'cos looking at the patch shows you what needs doing. The main problems were the implicit declarations and it is obvious where to fix them once you know what to change them to. It seems all the funny ints can be left to get on with it.</p>
<p>Onwards and upwards..</p>
<p>BTW. The preview of this note looks funny all the _ have disappeared. What to do about it?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Mar '13, 22:13</strong></p>
<img src="https://secure.gravatar.com/avatar/1bca123c0c1f7ff52cb5ac0972837cc7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Panca%20Kanga&#39;s gravatar image" />
<p><span>Panca Kanga</span><br />
<span class="score" title="30 reputation points">30</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Panca Kanga has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-20956" class="comments-container">
&#10;</div>
<div id="comment-tools-20956" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20956-form-container" class="comment-form-container">
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

