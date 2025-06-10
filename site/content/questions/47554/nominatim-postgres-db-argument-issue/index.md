+++
type = "question"
title = "Nominatim - postgres DB argument issue"
description = '''Hi, I am using nominatim-2.3.1.  I set DB username &amp;amp; password @define(&#x27;CONST_Database_DSN&#x27;, &#x27;pgsql://nomi:nomi@localhost:5432/nominatim&#x27;); in settings.php, But received in osm2pgsql.c &amp;amp; postgresql.c as empty. So I cant connect DB to create DB &amp;amp; insert data. EDIT: The same Issue comes in ...'''
date = "2016-01-18T07:42:00Z"
lastmod = "2018-04-16T08:31:00Z"
weight = 47554
keywords = [ "username", "nominatim", "postgresql", "osm2pgsql", "settings" ]
aliases = [ "/questions/47554" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Nominatim - postgres DB argument issue](/questions/47554/nominatim-postgres-db-argument-issue)

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
<span id="post-47554-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47554-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-47554-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I am using <strong>nominatim-2.3.1</strong>.</p>
<p>I set DB username &amp; password <strong>@define('CONST_Database_DSN', 'pgsql://nomi:nomi@localhost:5432/nominatim');</strong> in settings.php, But received in osm2pgsql.c &amp; postgresql.c as empty.</p>
<p>So I cant connect DB to create DB &amp; insert data.</p>
<p>EDIT:</p>
<p>The same Issue comes in <strong>Nominatim-2.5.1</strong> too. So now i need to give username in osm2pgsql.c &amp; postgresql.c</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-username" rel="tag" title="see questions tagged &#39;username&#39;">username</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-settings" rel="tag" title="see questions tagged &#39;settings&#39;">settings</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Jan '16, 07:42</strong></p>
<img src="https://secure.gravatar.com/avatar/1ffa52ca3632b5a0cf02b51459b7529b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rajavelu_M&#39;s gravatar image" />
<p><span>Rajavelu_M</span><br />
<span class="score" title="253 reputation points">253</span><span title="45 badges"><span class="badge1">●</span><span class="badgecount">45</span></span><span title="48 badges"><span class="silver">●</span><span class="badgecount">48</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rajavelu_M has one accepted answer">33%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Apr '18, 08:47</strong> </span></p>
</div>
</div>
<div id="comments-container-47554" class="comments-container">
<span id="63010"></span>
<div id="comment-63010" class="comment">
<div id="post-63010-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Tried in Nominatim-3.1.0 too. Still, I can't get DB username. Also tried as given in local.php as follows, but not working. @define('CONST_Database_DSN', 'pgsql://nomi:nomi@:localhost:5432/nominatim');</p>
<p>Every time(for upgrade nomination versions) I need to change my username in the source before compilation.</p>
</div>
<div id="comment-63010-info" class="comment-info">
<span class="comment-age">(16 Apr '18, 08:31)</span> <span class="comment-user userinfo">Rajavelu_M</span>
</div>
</div>
</div>
<div id="comment-tools-47554" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47554-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

