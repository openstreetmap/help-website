+++
type = "question"
title = "Problem with local nominatim search"
description = '''Hello, i tried to install a local NOMINATIM server. Now I have the problem that i cannot access the nominatim/search.php. When i call a search i get an output like: 50) $iFinalLimit = 50; $iLimit = $iFinalLimit + min($iFinalLimit, 10); $iMinAddressRank = 0; $iMaxAddressRank = 30; $aAddressRankList =...'''
date = "2013-07-29T10:40:00Z"
lastmod = "2013-08-01T08:03:00Z"
weight = 24678
keywords = [ "http_403_forbidden", "nominatim", "php", "search", "localhost" ]
aliases = [ "/questions/24678" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Problem with local nominatim search](/questions/24678/problem-with-local-nominatim-search)

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
<span id="post-24678-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24678-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-24678-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>i tried to install a local NOMINATIM server. Now I have the problem that i cannot access the nominatim/search.php. When i call a search i get an output like:</p>
<p>50) $iFinalLimit = 50; $iLimit = $iFinalLimit + min($iFinalLimit, 10); $iMinAddressRank = 0; $iMaxAddressRank = 30; $aAddressRankList = array(); $sAllowedTypesSQLList = false; // Format for output if (isset($_GET['format']) &amp;&amp; ($_GET['format'] == 'html' || $_GET['format'] == 'xml' || $_GET['forma...</p>
<p>I suspect this might be a problem with the user rights as i get a 403 Forbidden when i try to acces <a href="http://localhost/nominatim">http://localhost/nominatim</a></p>
<p>Does anyone have a clue how i can fix this problem?</p>
<p>Greetings</p>
<p>Flo</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-http_403_forbidden" rel="tag" title="see questions tagged &#39;http_403_forbidden&#39;">http_403_forbidden</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-php" rel="tag" title="see questions tagged &#39;php&#39;">php</span> <span class="post-tag tag-link-search" rel="tag" title="see questions tagged &#39;search&#39;">search</span> <span class="post-tag tag-link-localhost" rel="tag" title="see questions tagged &#39;localhost&#39;">localhost</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Jul '13, 10:40</strong></p>
<img src="https://secure.gravatar.com/avatar/9abfb9db9a2b849922d2ebdfd3bbad50?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fajgiess&#39;s gravatar image" />
<p><span>fajgiess</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fajgiess has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Dec '18, 22:37</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-24678" class="comments-container">
&#10;</div>
<div id="comment-tools-24678" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24678-form-container" class="comment-form-container">
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

<span id="24681"></span>

<div id="answer-container-24681" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-24681-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24681-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-24681-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="fajgiess has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Does your server process the PHP? It looks like it doesn't. So probably you should check by creating a <code>phpinfo.php</code> file in your server webroot and writing <code>&lt; ?php phpinfo(); ?&gt;</code> in it.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Jul '13, 15:44</strong></p>
<img src="https://secure.gravatar.com/avatar/806d5a652505590a9eba797ad5bea8db?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gormo&#39;s gravatar image" />
<p><span>gormo</span><br />
<span class="score" title="2928 reputation points"><span>2.9k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="26 badges"><span class="silver">●</span><span class="badgecount">26</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gormo has 13 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-24681" class="comments-container">
<span id="24775"></span>
<div id="comment-24775" class="comment">
<div id="post-24775-score" class="comment-score">
4
</div>
<div class="comment-text">
<p>Thanks for the tip... The problem was that due to a typo i didn't install php5 ... now it works fine.</p>
</div>
<div id="comment-24775-info" class="comment-info">
<span class="comment-age">(01 Aug '13, 08:03)</span> <span class="comment-user userinfo">fajgiess</span>
</div>
</div>
</div>
<div id="comment-tools-24681" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24681-form-container" class="comment-form-container">
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

