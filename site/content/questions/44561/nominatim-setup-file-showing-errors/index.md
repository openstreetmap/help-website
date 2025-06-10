+++
type = "question"
title = "Nominatim setup file showing errors"
description = '''We are facing problem with the setup.php file. Can any one has any way to overcome this error ?  /public_html/Nominatim]# ./utils/setup.php --osm-file india-latest.osm.pbf --all [--osm2pgsql-cache 18000] 2&amp;gt;&amp;amp;1 | tee setup.log  Warning: require_once(DB.php): failed to open stream: No such file ...'''
date = "2015-07-31T08:06:00Z"
lastmod = "2015-07-31T09:16:00Z"
weight = 44561
keywords = [ "setup.php" ]
aliases = [ "/questions/44561" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Nominatim setup file showing errors](/questions/44561/nominatim-setup-file-showing-errors)

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
<span id="post-44561-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44561-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-44561-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>We are facing problem with the setup.php file. Can any one has any way to overcome this error ?</p>
<pre><code>    /public_html/Nominatim]# ./utils/setup.php --osm-file india-latest.osm.pbf --all [--osm2pgsql-cache 18000] 2&gt;&amp;1 | tee setup.log 
Warning: require_once(DB.php): failed to open stream: No such file or directory in /home/xxxxxxx/public_html/Nominatim/lib/db.php on line 2
&#10;Fatal error: require_once(): Failed opening required &#39;DB.php&#39; (include_path=&#39;.:/usr/lib/php:/usr/local/lib/php&#39;) in /home/xxxxxxx/public_html/Nominatim/lib/db.php on line 2</code></pre>
<p>--</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-setup.php" rel="tag" title="see questions tagged &#39;setup.php&#39;">setup.php</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 Jul '15, 08:06</strong></p>
<img src="https://secure.gravatar.com/avatar/2463811d231d70c616bd07bdc0067395?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="arj123&#39;s gravatar image" />
<p><span>arj123</span><br />
<span class="score" title="46 reputation points">46</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="arj123 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-44561" class="comments-container">
&#10;</div>
<div id="comment-tools-44561" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44561-form-container" class="comment-form-container">
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

<span id="44562"></span>

<div id="answer-container-44562" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-44562-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44562-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-44562-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="arj123 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It seems like you sure you are calling <code>setup.php</code> wrong.</p>
<p><code>--osm2pgsql-cache</code> is an optional parameter. Either remove it completely or leave it there but remove the square brackets <code>[]</code>. They are <em>not</em> part of the parameter but indicate only that this parameter is optional.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Jul '15, 08:12</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>31 Jul '15, 08:13</strong> </span></p>
</div>
</div>
<div id="comments-container-44562" class="comments-container">
<span id="44564"></span>
<div id="comment-44564" class="comment">
<div id="post-44564-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks <a href="http://help.openstreetmap.org/users/158/scai"></a><a href="http://help.openstreetmap.org/users/158/scai">@scai</a>, so instead of ./utils/setup.php --osm-file &lt;your data="" file=""&gt; --all [--osm2pgsql-cache 24000] 2&gt;&amp;1 | tee setup.log I have to use ./utils/setup.php --osm-file &lt;your data="" file=""&gt; --all --osm2pgsql-cache 24000 2&gt;&amp;1 | tee setup.log ?</p>
</div>
<div id="comment-44564-info" class="comment-info">
<span class="comment-age">(31 Jul '15, 08:19)</span> <span class="comment-user userinfo">arj123</span>
</div>
</div>
<span id="44565"></span>
<div id="comment-44565" class="comment">
<div id="post-44565-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, exactly :) Ideally you should adapt the size of the cache to your environment.</p>
</div>
<div id="comment-44565-info" class="comment-info">
<span class="comment-age">(31 Jul '15, 08:49)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="44566"></span>
<div id="comment-44566" class="comment">
<div id="post-44566-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>thank you.</p>
</div>
<div id="comment-44566-info" class="comment-info">
<span class="comment-age">(31 Jul '15, 09:16)</span> <span class="comment-user userinfo">arj123</span>
</div>
</div>
</div>
<div id="comment-tools-44562" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44562-form-container" class="comment-form-container">
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

