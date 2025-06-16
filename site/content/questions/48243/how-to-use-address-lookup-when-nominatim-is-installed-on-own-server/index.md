+++
type = "question"
title = "How to use address lookup when nominatim is installed on own server"
description = '''Hi! I&#x27;ve just managed to install Nominatim, using the description found here: https://wiki.openstreetmap.org/wiki/Nominatim/Installation_on_CentOS on a CentOS 7. It all works fine, I&#x27;ve already imported a pbf of Luxembourg for testing purposes, it seems that the search is working, but I can&#x27;t find th...'''
date = "2016-02-20T18:41:00Z"
lastmod = "2016-10-13T11:51:00Z"
weight = 48243
keywords = [ "nominatim", "lookup", "address" ]
aliases = [ "/questions/48243" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to use address lookup when nominatim is installed on own server](/questions/48243/how-to-use-address-lookup-when-nominatim-is-installed-on-own-server)

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
<span id="post-48243-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48243-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-48243-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi!</p>
<p>I've just managed to install Nominatim, using the description found here: <a href="https://wiki.openstreetmap.org/wiki/Nominatim/Installation_on_CentOS">https://wiki.openstreetmap.org/wiki/Nominatim/Installation_on_CentOS</a> on a CentOS 7. It all works fine, I've already imported a pbf of Luxembourg for testing purposes, it seems that the search is working, but I can't find the address lookup section of nominatim. The section, where I can enter node, way, or relation ids, to get information about them.</p>
<p>On the original Nominatim server, it can be found here: <a href="http://nominatim.openstreetmap.org/lookup">http://nominatim.openstreetmap.org/lookup</a></p>
<p>I've searched in /Nominatim/website/ directory, and I have no lookup file there, but when I check this git, they indeed have a lookup file in the website directory: <a href="https://github.com/twain47/Nominatim">https://github.com/twain47/Nominatim</a></p>
<p>Why am I missing the lookup file, I've followed the instalation instructions on the above url, to the letter, and downloaded the latest Nominatim version 2.4.0.</p>
<p>What could be the problem?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-lookup" rel="tag" title="see questions tagged &#39;lookup&#39;">lookup</span> <span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Feb '16, 18:41</strong></p>
<img src="https://secure.gravatar.com/avatar/8d611d043d7267073e41089a5283fbe1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Adam%20Baranyai&#39;s gravatar image" />
<p><span>Adam Baranyai</span><br />
<span class="score" title="61 reputation points">61</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Adam Baranyai has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-48243" class="comments-container">
&#10;</div>
<div id="comment-tools-48243" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48243-form-container" class="comment-form-container">
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

<span id="48245"></span>

<div id="answer-container-48245" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48245-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48245-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-48245-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Adam Baranyai has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Release 2.4.0 is dated 2015-05-07 but the "lookup" code was only added on 2015-06-16: <a href="https://github.com/twain47/Nominatim/commit/7c8c206818266f40d2447e9b4c1b059c1139b152">https://github.com/twain47/Nominatim/commit/7c8c206818266f40d2447e9b4c1b059c1139b152</a></p>
<p>Perhaps you can simply download the lookup.php from github and place it in the right directory (don't forget the symlink to webspace). Otherwise you'll have to install Nominatim "trunk" i.e. the newest, un-versioned code from github.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Feb '16, 22:09</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-48245" class="comments-container">
<span id="48257"></span>
<div id="comment-48257" class="comment">
<div id="post-48257-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>What are the drawbacks of using the unversioned code? Cause I tried downloading and symlinking lookup.php but it's not this easy unfortunatly:( As I can see, a bunch of other php codes were changed.</p>
</div>
<div id="comment-48257-info" class="comment-info">
<span class="comment-age">(21 Feb '16, 01:08)</span> <span class="comment-user userinfo">Adam Baranyai</span>
</div>
</div>
<span id="52526"></span>
<div id="comment-52526" class="comment">
<div id="post-52526-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi Adam,</p>
<p>Could you pls help me in the Nominatim installation as I have done each and every step in the link which you have shared. I even don't know the nominatim page as how it looks like.</p>
<p>Please help me in the installation</p>
</div>
<div id="comment-52526-info" class="comment-info">
<span class="comment-age">(13 Oct '16, 11:51)</span> <span class="comment-user userinfo">Ashok009</span>
</div>
</div>
</div>
<div id="comment-tools-48245" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48245-form-container" class="comment-form-container">
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

