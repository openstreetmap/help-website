+++
type = "question"
title = "Nominatim website doesn/t work well"
description = '''Hello! I&#x27;ve instaled Nominatim on rhel 6.5,imported my map into, created website through httpd service, got any files in /var/www/html. But when I opened a link http://localhost I got many errors like:  string(19) &quot;pgsql://@/nominatim&quot; object(DB_Error)#2 (8) { [&quot;error_message_prefix&quot;]=&amp;gt; string(0)...'''
date = "2015-06-22T10:48:00Z"
lastmod = "2015-06-22T11:59:00Z"
weight = 43693
keywords = [ "nominatim" ]
aliases = [ "/questions/43693" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Nominatim website doesn/t work well](/questions/43693/nominatim-website-doesnt-work-well)

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
<span id="post-43693-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43693-score" class="post-score" title="current number of votes">
-2
</div>
<span id="post-43693-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello! I've instaled Nominatim on rhel 6.5,imported my map into, created website through httpd service, got any files in /var/www/html. But when I opened a link <a href="http://localhost">http://localhost</a> I got many errors like:</p>
<blockquote>
<p>string(19) "pgsql://@/nominatim" object(DB_Error)#2 (8) { ["error_message_prefix"]=&gt; string(0) "" ["mode"]=&gt; int(1) ["level"]=&gt; int(1024) ["code"]=&gt; int(-24) ["message"]=&gt; string(24) "DB Error: connect failed" ["userinfo"]=&gt; string(239) " [nativecode=pg_connect(): Unable to connect to PostgreSQL server: could not connect to server: Permission denied Is the server running locally and accepting connections on Unix domain socket "/tmp/.s.PGSQL.5432"?] <em><em>pgsql://@/nominatim" ["backtrace"]=&gt; array(7) { [0]=&gt; array(6) { ["file"]=&gt; string(22) "/usr/share/pear/DB.php" ["line"]=&gt; int(967) ["function"]=&gt; string(10) "PEAR_Error" ["class"]=&gt; string(10) "PEAR_Error" ["type"]=&gt; string(2) "-&gt;" ["args"]=&gt; array(5) { [0]=&gt; string(24) "DB Error: connect failed" [1]=&gt; int(-24) [2]=&gt; int(1) [3]=&gt; int(1024) [4]=&gt; string(216) " [nativecode=pg_connect(): Unable to connect to PostgreSQL server: could not connect to server: Permission denied Is the server running locally and accepting connections on Unix domain socket "/tmp/.s.PGSQL.5432"?]" } } [1]=&gt; array(7) { ["file"]=&gt; string(24) "/usr/share/pear/PEAR.php" ["line"]=&gt; int(531) ["function"]=&gt; string(8) "DB_Error" ["class"]=&gt; string(8) "DB_Error" ["object"]=&gt;</em> RECURSION</em> ["type"]=&gt; string(2) "-&gt;" ["args"]=&gt; array(4) { [0]=&gt; int(-24) [1]=&gt; int(1) [2]=&gt; int(1024) [3]=&gt; string(216) " [nativecode=pg_connect(): Unable to connect to PostgreSQL server: could not connect to server: Permission denied Is the server running locally and accepting connections on Unix domain socket "/tmp/.s.PGSQL.5432"?]" } } [2]=&gt; array(7) { ["file"]=&gt; string(29) "/usr/share/pear/DB/common.php" ["line"]=&gt; int(1907) ["function"]=&gt; string(10) "raiseError" ["class"]=&gt; string(4) "PEAR" ["object"]=&gt; object(DB_pgsql)#1 (28) { ["phptype"]=&gt; string(5) "pgsql" ["dbsyntax"]=&gt; string(5) "pgsql" ["features"]=&gt; array(7) { ["limit"]=&gt; string(5) "alter" ["new_link"]=&gt; string(5) "4.3.0" ["numrows"]=&gt; bool(true) ["pconnect"]=&gt; bool(true) ["prepare"]=&gt; bool(false) ["ssl"]=&gt; bool(true) ["transactions"]=&gt; bool(true) } ["errorcode_map"]=&gt; array(0) { } ["connection"]=&gt; bool(false) ["dsn"]=&gt; array(9) { ["phptype"]=&gt; string(5) "pgsql" ["dbsyntax"]=&gt; string(5) "pgsql" ["username"]=&gt; string(0) "" ["password"]=&gt; bool(false) ["protocol"]=&gt; string(3) "tcp" ["hostspec"]=&gt; string(0) "" ["port"]=&gt; bool(false) ["socket"]=&gt; bool(false) ["database"]=&gt; string(9) "nominatim" } ["autocommit"]=&gt; bool(true) ["transaction_opcount"]=&gt; int(0) ["affected"]=&gt; int(0) ["row"]=&gt; array(0) { } ["_num_rows"]=&gt; array(0) { } ["fetchmode"]=&gt; int(1) ["fetchmode_object_class"]=&gt; string(8) "stdClass" ["was_connected"]=&gt; NULL ["last_query"]=&gt; string(0) "" ["options"]=&gt; array(8) { ["result_buffering"]=&gt; int(500) ["persistent"]=&gt; bool(false) ["ssl"]=&gt; bool(false) ["debug"]=&gt; int(0) ["seqname_format"]=&gt; string(6) "%s_seq" ["autofree"]=&gt; bool(false) ["portability"]=&gt; int(0) ["optimize"]=&gt; string(11) "performance" } ["last_parameters"]=&gt; array(0) { } ["prepare_tokens"]=&gt; array(0) { } ["prepare_types"]=&gt; array(0) { } ["prepared_queries"]=&gt; array(0) { } ["_last_query_manip"]=&gt; bool(false) ["_next_query_manip"]=&gt; bool(false) ["_debug"]=&gt; bool(false) ["_default_error_mode"]=&gt; NULL ["_default_error_options"]=&gt; NULL ["_default_error_handler"]=&gt; string(0) "" ["_error_class"]=&gt; string(8) "DB_Error" ["_expected_errors"]=&gt; array(0) { } } ["type"]=&gt; string(2) "-&gt;" ["args"]=&gt; array(7) { [0]=&gt; NULL [1]=&gt; int(-24) [2]=&gt; NULL [3]=&gt; NULL [4]=&gt; string(216) " [nativecode=pg_connect(): Unable to connect to PostgreSQL server: could not connect to server: Permission denied Is the server running locally and accepting connections on Unix domain socket "/tmp/.s.PGSQL.5432"?]" [5]=&gt; string(8) "DB_Error" [6]=&gt; bool(true) } } [3]=&gt; array(7) { ["file"]=&gt; string(28) "/usr/share/pear/DB/pgsql.php" ["line"]=&gt; int(289) ["function"]=&gt; string(10) "raiseError" ["class"]=&gt; string(9) "DB_common" ["object"]=&gt; object(DB_pgsql)#1 (28) { ["phptype"]=&gt; string(5) "pgsql" ["dbsyntax"]=&gt; string(5) "pgsql" ["features"]=&gt; array(7) { ["limit"]=&gt; string(5) "alter" ["new_link"]=&gt; string(5) "4.3.0" ["numrows"]=&gt; bool(true) ["pconnect"]=&gt; bool(true) ["prepare"]=&gt; bool(false) ["ssl"]=&gt; bool(true) ["transactions"]=&gt; bool(true) } ["errorcode_map"]=&gt; array(0) { } ["connection"]=&gt; bool(false) ["dsn"]=&gt; array(9) { ["phptype"]=&gt; string(5) "pgsql" ["dbsyntax"]=&gt; string(5) "pgsql" ["username"]=&gt; string(0) "" ["password"]=&gt; bool(false) ["protocol"]=&gt; string(3) "tcp" ["hostspec"]=&gt; string(0) "" ["port"]=&gt; bool(false) ["socket"]=&gt; bool(false) ["database"]=&gt; string(9) "nominatim" } ["autocommit"]=&gt; bool(true) ["transaction_opcount"]=&gt; int(0) ["affected"]=&gt; int(0) ["row"]=&gt; array(0) { } ["_num_rows"]=&gt; array(0) { } ["fetchmode"]=&gt; int(1) ["fetchmode_object_class"]=&gt; string(8) "stdClass" ["was_connected"]=&gt; NULL ["last_query"]=&gt; string(0) "" ["options"]=&gt; array(8) { ["result_buffering"]=&gt; int(500) ["persistent"]=&gt; bool(false) ["ssl"]=&gt; bool(false) ["debug"]=&gt; int(0) ["seqname_format"]=&gt; string(6) "%s_seq" ["autofree"]=&gt; bool(false) ["portability"]=&gt; int(0) ["optimize"]=&gt; string(11) "performance" } ["last_parameters"]=&gt; array(0) { } ["prepare_tokens"]=&gt; array(0) { } ["prepare_types"]=&gt; array(0) { } ["prepared_queries"]=&gt; array(0) { } ["_last_query_manip"]=&gt; bool(false) ["_next_query_manip"]=&gt; bool(false) ["_debug"]=&gt; bool(false) ["_default_error_mode"]=&gt; NULL ["_default_error_options"]=&gt; NULL ["_default_error_handler"]=&gt; string(0) "" ["_error_class"]=&gt; string(8) "DB_Error" ["_expected_errors"]=&gt; array(0) { } } ["type"]=&gt; string(2) "-&gt;" ["args"]=&gt; array(5) { [0]=&gt; int(-24) [1]=&gt; NULL [2]=&gt; NULL [3]=&gt; NULL [4]=&gt; string(202) "pg_connect(): Unable to connect to PostgreSQL server: could not connect to server: Permission denied Is the server running locally and accepting connections on Unix domain socket "/tmp/.s.PGSQL.5432"?" } } [4]=&gt; array(7) { ["file"]=&gt; string(22) "/usr/share/pear/DB.php" ["line"]=&gt; int(557) ["function"]=&gt; string(7) "connect" ["class"]=&gt; string(8) "DB_pgsql" ["object"]=&gt; object(DB_pgsql)#1 (28) { ["phptype"]=&gt; string(5) "pgsql" ["dbsyntax"]=&gt; string(5) "pgsql" ["features"]=&gt; array(7) { ["limit"]=&gt; string(5) "alter" ["new_link"]=&gt; string(5) "4.3.0" ["numrows"]=&gt; bool(true) ["pconnect"]=&gt; bool(true) ["prepare"]=&gt; bool(false) ["ssl"]=&gt; bool(true) ["transactions"]=&gt; bool(true) } ["errorcode_map"]=&gt; array(0) { } ["connection"]=&gt; bool(false) ["dsn"]=&gt; array(9) { ["phptype"]=&gt; string(5) "pgsql" ["dbsyntax"]=&gt; string(5) "pgsql" ["username"]=&gt; string(0) "" ["password"]=&gt; bool(false) ["protocol"]=&gt; string(3) "tcp" ["hostspec"]=&gt; string(0) "" ["port"]=&gt; bool(false) ["socket"]=&gt; bool(false) ["database"]=&gt; string(9) "nominatim" } ["autocommit"]=&gt; bool(true) ["transaction_opcount"]=&gt; int(0) ["affected"]=&gt; int(0) ["row"]=&gt; array(0) { } ["_num_rows"]=&gt; array(0) { } ["fetchmode"]=&gt; int(1) ["fetchmode_object_class"]=&gt; string(8) "stdClass" ["was_connected"]=&gt; NULL ["last_query"]=&gt; string(0) "" ["options"]=&gt; array(8) { ["result_buffering"]=&gt; int(500) ["persistent"]=&gt; bool(false) ["ssl"]=&gt; bool(false) ["debug"]=&gt; int(0) ["seqname_format"]=&gt; string(6) "%s_seq" ["autofree"]=&gt; bool(false) ["portability"]=&gt; int(0) ["optimize"]=&gt; string(11) "performance" } ["last_parameters"]=&gt; array(0) { } ["prepare_tokens"]=&gt; array(0) { } ["prepare_types"]=&gt; array(0) { } ["prepared_queries"]=&gt; array(0) { } ["_last_query_manip"]=&gt; bool(false) ["_next_query_manip"]=&gt; bool(false) ["_debug"]=&gt; bool(false) ["_default_error_mode"]=&gt; NULL ["_default_error_options"]=&gt; NULL ["_default_error_handler"]=&gt; string(0) "" ["_error_class"]=&gt; string(8) "DB_Error" ["_expected_errors"]=&gt; array(0) { } } ["type"]=&gt; string(2) "-&gt;" ["args"]=&gt; array(2) { [0]=&gt; array(9) { ["phptype"]=&gt; string(5) "pgsql" ["dbsyntax"]=&gt; string(5) "pgsql" ["username"]=&gt; string(0) "" ["password"]=&gt; bool(false) ["protocol"]=&gt; string(3) "tcp" ["hostspec"]=&gt; string(0) "" ["port"]=&gt; bool(false) ["socket"]=&gt; bool(false) ["database"]=&gt; string(9) "nominatim" } [1]=&gt; bool(false) } } [5]=&gt; array(6) { ["file"]=&gt; string(25) "/opt/Nominatim/lib/db.php" ["line"]=&gt; int(7) ["function"]=&gt; string(7) "connect" ["class"]=&gt; string(2) "DB" ["type"]=&gt; string(2) "::" ["args"]=&gt; array(2) { [0]=&gt; string(19) "pgsql://@/nominatim" [1]=&gt; bool(false) } } [6]=&gt; array(4) { ["file"]=&gt; string(33) "/opt/Nominatim/website/search.php" ["line"]=&gt; int(10) ["function"]=&gt; string(5) "getDB" ["args"]=&gt; array(0) { } } } ["callback"]=&gt; NULL } DB Error: connect failed</p>
</blockquote>
<p>What's going wrong wit it?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Jun '15, 10:48</strong></p>
<img src="https://secure.gravatar.com/avatar/c14774eb4c4f7361a4e908fa59d9827d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Silentium&#39;s gravatar image" />
<p><span>Silentium</span><br />
<span class="score" title="9 reputation points">9</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Silentium has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-43693" class="comments-container">
&#10;</div>
<div id="comment-tools-43693" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43693-form-container" class="comment-form-container">
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

<span id="43695"></span>

<div id="answer-container-43695" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43695-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43695-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-43695-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The error message says:</p>
<blockquote>
<p>Unable to connect to PostgreSQL server: could not connect to server: Permission denied Is the server running locally and accepting connections on Unix domain socket</p>
</blockquote>
<p>It looks like the nominatim server cannot connect to the postgresql database. Is your database working OK?</p>
<p>There might be more help in this other answer: <a href="/questions/15563/nominatim-install-problem-final-step-php">https://help.openstreetmap.org/questions/15563/nominatim-install-problem-final-step-php</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Jun '15, 11:08</strong></p>
<img src="https://secure.gravatar.com/avatar/16e12e337f6edc3750681492656097ed?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rorym&#39;s gravatar image" />
<p><span>rorym</span><br />
<span class="score" title="5358 reputation points"><span>5.4k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="49 badges"><span class="silver">●</span><span class="badgecount">49</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rorym has 18 accepted answers">11%</span></p>
</div>
</div>
<div id="comments-container-43695" class="comments-container">
<span id="43697"></span>
<div id="comment-43697" class="comment">
<div id="post-43697-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanx for your link. Shutting down SELinux</p>
</div>
<div id="comment-43697-info" class="comment-info">
<span class="comment-age">(22 Jun '15, 11:59)</span> <span class="comment-user userinfo">Silentium</span>
</div>
</div>
</div>
<div id="comment-tools-43695" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43695-form-container" class="comment-form-container">
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

