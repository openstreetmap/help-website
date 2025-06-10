+++
type = "question"
title = "Nominatim database connect"
description = '''Hi, I&#x27;ve got a server running nominatim with planet database.  As I wanted to update my data I&#x27;ve imported a new planet file into a second database on the same server.  How can I change the database which should be used?  Do I have to modify this line in the directory build/settings/settings.php?:  ...'''
date = "2019-06-17T14:55:00Z"
lastmod = "2019-06-18T09:33:00Z"
weight = 69641
keywords = [ "connection", "nominatim", "database" ]
aliases = [ "/questions/69641" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Nominatim database connect](/questions/69641/nominatim-database-connect)

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
<span id="post-69641-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69641-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-69641-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I've got a server running nominatim with planet database.</p>
<p>As I wanted to update my data I've imported a new planet file into a second database on the same server.</p>
<p>How can I change the database which should be used?</p>
<p>Do I have to modify this line in the directory build/settings/settings.php?: @define('CONST_Database_DSN', 'pgsql://@/nominatim'); // &lt;driver&gt;://&lt;username&gt;:&lt;password&gt;@&lt;host&gt;:&lt;port&gt;/&lt;database&gt;</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-connection" rel="tag" title="see questions tagged &#39;connection&#39;">connection</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-database" rel="tag" title="see questions tagged &#39;database&#39;">database</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Jun '19, 14:55</strong></p>
<img src="https://secure.gravatar.com/avatar/da2d9bb236eceb1795d2818fb69862e1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Maik28&#39;s gravatar image" />
<p><span>Maik28</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Maik28 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-69641" class="comments-container">
<span id="69644"></span>
<div id="comment-69644" class="comment">
<div id="post-69644-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>A Nominatim import is usually done with the <code>setup.php</code> script which loads its configuration from <code>settings.php</code>. If you have managed to import into a second database, then you will likely have made that modification already?</p>
</div>
<div id="comment-69644-info" class="comment-info">
<span class="comment-age">(17 Jun '19, 23:18)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="69645"></span>
<div id="comment-69645" class="comment">
<div id="post-69645-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I did the second import with osm2pgsql.</p>
<p>My plan was to test Nominatim with the new database and then switch over. (I hope it doesn't matter how the import was done especially because the database schema is different)</p>
</div>
<div id="comment-69645-info" class="comment-info">
<span class="comment-age">(18 Jun '19, 09:19)</span> <span class="comment-user userinfo">Maik28</span>
</div>
</div>
<span id="69648"></span>
<div id="comment-69648" class="comment">
<div id="post-69648-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If you have <em>not</em> used the exact same commandline flags that Nominatim uses during your second import (especially <code>-o gazetteer</code> but also others) then your second import is not usable for Nominatim at all. If you <em>have</em> used these flags then it can be used, but you need to run a series of steps, notably the indexing steps, before you can use it. Have a look at the source code of <code>setup.php</code> and all the steps it performs when you run it with <code>--all</code>; essentially you need to run all these minus the bare import. -- The easiest &amp; most foolproof way to re-import into a second database is to copy your whole Nominatim directory, change the <code>settings.php</code> connection string to point to a new database, and then run setup.php in that new directory.</p>
</div>
<div id="comment-69648-info" class="comment-info">
<span class="comment-age">(18 Jun '19, 09:33)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-69641" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69641-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

