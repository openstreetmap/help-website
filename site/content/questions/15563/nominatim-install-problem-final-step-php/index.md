+++
type = "question"
title = "Nominatim Install Problem, Final Step. PHP?"
description = '''After completing the nominatim install, and map importing. we try to connect to the php site and recieve this error. the apache user has rwx on the nominatim folder, etc. cannot figure this out. even renamed postgres user www-data to apache. any thoughts? i can try to go into more detail if necessar...'''
date = "2012-08-27T18:32:00Z"
lastmod = "2012-09-11T21:44:00Z"
weight = 15563
keywords = [ "postgresql", "nominatim", "installation", "install", "php" ]
aliases = [ "/questions/15563" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Nominatim Install Problem, Final Step. PHP?](/questions/15563/nominatim-install-problem-final-step-php)

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
<span id="post-15563-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15563-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-15563-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>After completing the nominatim install, and map importing. we try to connect to the php site and recieve this error. the apache user has rwx on the nominatim folder, etc. cannot figure this out. even renamed postgres user www-data to apache. any thoughts? i can try to go into more detail if necessary.</p>
<pre><code>string(19) &quot;pgsql://@/nominatim&quot; object(DB_Error)#2 (8) { [&quot;error_message_prefix&quot;]=&gt; string(0) &quot;&quot; [&quot;mode&quot;]=&gt; int(1) [&quot;level&quot;]=&gt; int(1024) [&quot;code&quot;]=&gt; int(-24) [&quot;message&quot;]=&gt; string(24) &quot;DB Error: connect failed&quot; [&quot;userinfo&quot;]=&gt; string(239) &quot; [nativecode=pg_connect(): Unable to connect to PostgreSQL server: could not connect to server: Permission denied Is the server running locally and accepting connections on Unix domain socket &quot;/tmp/.s.PGSQL.5432&quot;?] ** pgsql://@/nominatim&quot; [&quot;backtrace&quot;]=&gt; array(7) { [0]=&gt; array(6) { [&quot;file&quot;]=&gt; string(22) &quot;/usr/share/pear/DB.php&quot; [&quot;line&quot;]=&gt; int(966) [&quot;function&quot;]=&gt; string(10) &quot;PEAR_Error&quot; [&quot;class&quot;]=&gt; string(10) &quot;PEAR_Error&quot; [&quot;type&quot;]=&gt; string(2) &quot;-&gt;&quot; [&quot;args&quot;]=&gt; array(5) { [0]=&gt; string(24) &quot;DB Error: connect failed&quot; [1]=&gt; int(-24) [2]=&gt; int(1) [3]=&gt; int(1024) [4]=&gt; string(216) &quot; [nativecode=pg_connect(): Unable to connect to PostgreSQL server: could not connect to server: Permission denied Is the server running locally and accepting connections on Unix domain socket &quot;/tmp/.s.PGSQL.5432&quot;?]&quot; } } [1]=&gt; array(7) { [&quot;file&quot;]=&gt; string(24) &quot;/usr/share/pear/PEAR.php&quot; [&quot;line&quot;]=&gt; int(531) [&quot;function&quot;]=&gt; string(8) &quot;DB_Error&quot; [&quot;class&quot;]=&gt; string(8) &quot;DB_Error&quot; [&quot;object&quot;]=&gt; *RECURSION* [&quot;type&quot;]=&gt; string(2) &quot;-&gt;&quot; [&quot;args&quot;]=&gt; array(4) { [0]=&gt; int(-24) [1]=&gt; int(1) [2]=&gt; int(1024) [3]=&gt; string(216) &quot; [nativecode=pg_connect(): Unable to connect to PostgreSQL server: could not connect to server: Permission denied Is the server running locally and accepting connections on Unix domain socket &quot;/tmp/.s.PGSQL.5432&quot;?]&quot; } } [2]=&gt; array(7) { [&quot;file&quot;]=&gt; string(29) &quot;/usr/share/pear/DB/common.php&quot; [&quot;line&quot;]=&gt; int(1903) [&quot;function&quot;]=&gt; string(10) &quot;raiseError&quot; [&quot;class&quot;]=&gt; string(4) &quot;PEAR&quot; [&quot;object&quot;]=&gt; object(DB_pgsql)#1 (28) { [&quot;phptype&quot;]=&gt; string(5) &quot;pgsql&quot; [&quot;dbsyntax&quot;]=&gt; string(5) &quot;pgsql&quot; [&quot;features&quot;]=&gt; array(7) { [&quot;limit&quot;]=&gt; string(5) &quot;alter&quot; [&quot;new_link&quot;]=&gt; string(5) &quot;4.3.0&quot; [&quot;numrows&quot;]=&gt; bool(true) [&quot;pconnect&quot;]=&gt; bool(true) [&quot;prepare&quot;]=&gt; bool(false) [&quot;ssl&quot;]=&gt; bool(true) [&quot;transactions&quot;]=&gt; bool(true) } [&quot;errorcode_map&quot;]=&gt; array(0) { } [&quot;connection&quot;]=&gt; bool(false) [&quot;dsn&quot;]=&gt; array(9) { [&quot;phptype&quot;]=&gt; string(5) &quot;pgsql&quot; [&quot;dbsyntax&quot;]=&gt; string(5) &quot;pgsql&quot; [&quot;username&quot;]=&gt; string(0) &quot;&quot; [&quot;password&quot;]=&gt; bool(false) [&quot;protocol&quot;]=&gt; string(3) &quot;tcp&quot; [&quot;hostspec&quot;]=&gt; string(0) &quot;&quot; [&quot;port&quot;]=&gt; bool(false) [&quot;socket&quot;]=&gt; bool(false) [&quot;database&quot;]=&gt; string(9) &quot;nominatim&quot; } [&quot;autocommit&quot;]=&gt; bool(true) [&quot;transaction_opcount&quot;]=&gt; int(0) [&quot;affected&quot;]=&gt; int(0) [&quot;row&quot;]=&gt; array(0) { } [&quot;_num_rows&quot;]=&gt; array(0) { } [&quot;fetchmode&quot;]=&gt; int(1) [&quot;fetchmode_object_class&quot;]=&gt; string(8) &quot;stdClass&quot; [&quot;was_connected&quot;]=&gt; NULL [&quot;last_query&quot;]=&gt; string(0) &quot;&quot; [&quot;options&quot;]=&gt; array(8) { [&quot;result_buffering&quot;]=&gt; int(500) [&quot;persistent&quot;]=&gt; bool(false) [&quot;ssl&quot;]=&gt; bool(false) [&quot;debug&quot;]=&gt; int(0) [&quot;seqname_format&quot;]=&gt; string(6) &quot;%s_seq&quot; [&quot;autofree&quot;]=&gt; bool(false) [&quot;portability&quot;]=&gt; int(0) [&quot;optimize&quot;]=&gt; string(11) &quot;performance&quot; } [&quot;last_parameters&quot;]=&gt; array(0) { } [&quot;prepare_tokens&quot;]=&gt; array(0) { } [&quot;prepare_types&quot;]=&gt; array(0) { } [&quot;prepared_queries&quot;]=&gt; array(0) { } [&quot;_last_query_manip&quot;]=&gt; bool(false) [&quot;_next_query_manip&quot;]=&gt; bool(false) [&quot;_debug&quot;]=&gt; bool(false) [&quot;_default_error_mode&quot;]=&gt; NULL [&quot;_default_error_options&quot;]=&gt; NULL [&quot;_default_error_handler&quot;]=&gt; string(0) &quot;&quot; [&quot;_error_class&quot;]=&gt; string(8) &quot;DB_Error&quot; [&quot;_expected_errors&quot;]=&gt; array(0) { } } [&quot;type&quot;]=&gt; string(2) &quot;-&gt;&quot; [&quot;args&quot;]=&gt; array(7) { [0]=&gt; NULL [1]=&gt; int(-24) [2]=&gt; NULL [3]=&gt; NULL [4]=&gt; string(216) &quot; [nativecode=pg_connect(): Unable to connect to PostgreSQL server: could not connect to server: Permission denied Is the server running locally and accepting connections on Unix domain socket &quot;/tmp/.s.PGSQL.5432&quot;?]&quot; [5]=&gt; string(8) &quot;DB_Error&quot; [6]=&gt; bool(true) } } [3]=&gt; array(7) { [&quot;file&quot;]=&gt; string(28) &quot;/usr/share/pear/DB/pgsql.php&quot; [&quot;line&quot;]=&gt; int(289) [&quot;function&quot;]=&gt; string(10) &quot;raiseError&quot; [&quot;class&quot;]=&gt; string(9) &quot;DB_common&quot; [&quot;object&quot;]=&gt; object(DB_pgsql)#1 (28) { [&quot;phptype&quot;]=&gt; string(5) &quot;pgsql&quot; [&quot;dbsyntax&quot;]=&gt; string(5) &quot;pgsql&quot; [&quot;features&quot;]=&gt; array(7) { [&quot;limit&quot;]=&gt; string(5) &quot;alter&quot; [&quot;new_link&quot;]=&gt; string(5) &quot;4.3.0&quot; [&quot;numrows&quot;]=&gt; bool(true) [&quot;pconnect&quot;]=&gt; bool(true) [&quot;prepare&quot;]=&gt; bool(false) [&quot;ssl&quot;]=&gt; bool(true) [&quot;transactions&quot;]=&gt; bool(true) } [&quot;errorcode_map&quot;]=&gt; array(0) { } [&quot;connection&quot;]=&gt; bool(false) [&quot;dsn&quot;]=&gt; array(9) { [&quot;phptype&quot;]=&gt; string(5) &quot;pgsql&quot; [&quot;dbsyntax&quot;]=&gt; string(5) &quot;pgsql&quot; [&quot;username&quot;]=&gt; string(0) &quot;&quot; [&quot;password&quot;]=&gt; bool(false) [&quot;protocol&quot;]=&gt; string(3) &quot;tcp&quot; [&quot;hostspec&quot;]=&gt; string(0) &quot;&quot; [&quot;port&quot;]=&gt; bool(false) [&quot;socket&quot;]=&gt; bool(false) [&quot;database&quot;]=&gt; string(9) &quot;nominatim&quot; } [&quot;autocommit&quot;]=&gt; bool(true) [&quot;transaction_opcount&quot;]=&gt; int(0) [&quot;affected&quot;]=&gt; int(0) [&quot;row&quot;]=&gt; array(0) { } [&quot;_num_rows&quot;]=&gt; array(0) { } [&quot;fetchmode&quot;]=&gt; int(1) [&quot;fetchmode_object_class&quot;]=&gt; string(8) &quot;stdClass&quot; [&quot;was_connected&quot;]=&gt; NULL [&quot;last_query&quot;]=&gt; string(0) &quot;&quot; [&quot;options&quot;]=&gt; array(8) { [&quot;result_buffering&quot;]=&gt; int(500) [&quot;persistent&quot;]=&gt; bool(false) [&quot;ssl&quot;]=&gt; bool(false) [&quot;debug&quot;]=&gt; int(0) [&quot;seqname_format&quot;]=&gt; string(6) &quot;%s_seq&quot; [&quot;autofree&quot;]=&gt; bool(false) [&quot;portability&quot;]=&gt; int(0) [&quot;optimize&quot;]=&gt; string(11) &quot;performance&quot; } [&quot;last_parameters&quot;]=&gt; array(0) { } [&quot;prepare_tokens&quot;]=&gt; array(0) { } [&quot;prepare_types&quot;]=&gt; array(0) { } [&quot;prepared_queries&quot;]=&gt; array(0) { } [&quot;_last_query_manip&quot;]=&gt; bool(false) [&quot;_next_query_manip&quot;]=&gt; bool(false) [&quot;_debug&quot;]=&gt; bool(false) [&quot;_default_error_mode&quot;]=&gt; NULL [&quot;_default_error_options&quot;]=&gt; NULL [&quot;_default_error_handler&quot;]=&gt; string(0) &quot;&quot; [&quot;_error_class&quot;]=&gt; string(8) &quot;DB_Error&quot; [&quot;_expected_errors&quot;]=&gt; array(0) { } } [&quot;type&quot;]=&gt; string(2) &quot;-&gt;&quot; [&quot;args&quot;]=&gt; array(5) { [0]=&gt; int(-24) [1]=&gt; NULL [2]=&gt; NULL [3]=&gt; NULL [4]=&gt; string(202) &quot;pg_connect(): Unable to connect to PostgreSQL server: could not connect to server: Permission denied Is the server running locally and accepting connections on Unix domain socket &quot;/tmp/.s.PGSQL.5432&quot;?&quot; } } [4]=&gt; array(7) { [&quot;file&quot;]=&gt; string(22) &quot;/usr/share/pear/DB.php&quot; [&quot;line&quot;]=&gt; int(556) [&quot;function&quot;]=&gt; string(7) &quot;connect&quot; [&quot;class&quot;]=&gt; string(8) &quot;DB_pgsql&quot; [&quot;object&quot;]=&gt; object(DB_pgsql)#1 (28) { [&quot;phptype&quot;]=&gt; string(5) &quot;pgsql&quot; [&quot;dbsyntax&quot;]=&gt; string(5) &quot;pgsql&quot; [&quot;features&quot;]=&gt; array(7) { [&quot;limit&quot;]=&gt; string(5) &quot;alter&quot; [&quot;new_link&quot;]=&gt; string(5) &quot;4.3.0&quot; [&quot;numrows&quot;]=&gt; bool(true) [&quot;pconnect&quot;]=&gt; bool(true) [&quot;prepare&quot;]=&gt; bool(false) [&quot;ssl&quot;]=&gt; bool(true) [&quot;transactions&quot;]=&gt; bool(true) } [&quot;errorcode_map&quot;]=&gt; array(0) { } [&quot;connection&quot;]=&gt; bool(false) [&quot;dsn&quot;]=&gt; array(9) { [&quot;phptype&quot;]=&gt; string(5) &quot;pgsql&quot; [&quot;dbsyntax&quot;]=&gt; string(5) &quot;pgsql&quot; [&quot;username&quot;]=&gt; string(0) &quot;&quot; [&quot;password&quot;]=&gt; bool(false) [&quot;protocol&quot;]=&gt; string(3) &quot;tcp&quot; [&quot;hostspec&quot;]=&gt; string(0) &quot;&quot; [&quot;port&quot;]=&gt; bool(false) [&quot;socket&quot;]=&gt; bool(false) [&quot;database&quot;]=&gt; string(9) &quot;nominatim&quot; } [&quot;autocommit&quot;]=&gt; bool(true) [&quot;transaction_opcount&quot;]=&gt; int(0) [&quot;affected&quot;]=&gt; int(0) [&quot;row&quot;]=&gt; array(0) { } [&quot;_num_rows&quot;]=&gt; array(0) { } [&quot;fetchmode&quot;]=&gt; int(1) [&quot;fetchmode_object_class&quot;]=&gt; string(8) &quot;stdClass&quot; [&quot;was_connected&quot;]=&gt; NULL [&quot;last_query&quot;]=&gt; string(0) &quot;&quot; [&quot;options&quot;]=&gt; array(8) { [&quot;result_buffering&quot;]=&gt; int(500) [&quot;persistent&quot;]=&gt; bool(false) [&quot;ssl&quot;]=&gt; bool(false) [&quot;debug&quot;]=&gt; int(0) [&quot;seqname_format&quot;]=&gt; string(6) &quot;%s_seq&quot; [&quot;autofree&quot;]=&gt; bool(false) [&quot;portability&quot;]=&gt; int(0) [&quot;optimize&quot;]=&gt; string(11) &quot;performance&quot; } [&quot;last_parameters&quot;]=&gt; array(0) { } [&quot;prepare_tokens&quot;]=&gt; array(0) { } [&quot;prepare_types&quot;]=&gt; array(0) { } [&quot;prepared_queries&quot;]=&gt; array(0) { } [&quot;_last_query_manip&quot;]=&gt; bool(false) [&quot;_next_query_manip&quot;]=&gt; bool(false) [&quot;_debug&quot;]=&gt; bool(false) [&quot;_default_error_mode&quot;]=&gt; NULL [&quot;_default_error_options&quot;]=&gt; NULL [&quot;_default_error_handler&quot;]=&gt; string(0) &quot;&quot; [&quot;_error_class&quot;]=&gt; string(8) &quot;DB_Error&quot; [&quot;_expected_errors&quot;]=&gt; array(0) { } } [&quot;type&quot;]=&gt; string(2) &quot;-&gt;&quot; [&quot;args&quot;]=&gt; array(2) { [0]=&gt; array(9) { [&quot;phptype&quot;]=&gt; string(5) &quot;pgsql&quot; [&quot;dbsyntax&quot;]=&gt; string(5) &quot;pgsql&quot; [&quot;username&quot;]=&gt; string(0) &quot;&quot; [&quot;password&quot;]=&gt; bool(false) [&quot;protocol&quot;]=&gt; string(3) &quot;tcp&quot; [&quot;hostspec&quot;]=&gt; string(0) &quot;&quot; [&quot;port&quot;]=&gt; bool(false) [&quot;socket&quot;]=&gt; bool(false) [&quot;database&quot;]=&gt; string(9) &quot;nominatim&quot; } [1]=&gt; bool(false) } } [5]=&gt; array(6) { [&quot;file&quot;]=&gt; string(29) &quot;/website/Nominatim/lib/db.php&quot; [&quot;line&quot;]=&gt; int(7) [&quot;function&quot;]=&gt; string(7) &quot;connect&quot; [&quot;class&quot;]=&gt; string(2) &quot;DB&quot; [&quot;type&quot;]=&gt; string(2) &quot;::&quot; [&quot;args&quot;]=&gt; array(2) { [0]=&gt; string(19) &quot;pgsql://@/nominatim&quot; [1]=&gt; bool(false) } } [6]=&gt; array(4) { [&quot;file&quot;]=&gt; string(37) &quot;/website/Nominatim/website/search.php&quot; [&quot;line&quot;]=&gt; int(6) [&quot;function&quot;]=&gt; string(5) &quot;getDB&quot; [&quot;args&quot;]=&gt; array(0) { } } } [&quot;callback&quot;]=&gt; NULL } DB Error: connect failed</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-installation" rel="tag" title="see questions tagged &#39;installation&#39;">installation</span> <span class="post-tag tag-link-install" rel="tag" title="see questions tagged &#39;install&#39;">install</span> <span class="post-tag tag-link-php" rel="tag" title="see questions tagged &#39;php&#39;">php</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Aug '12, 18:32</strong></p>
<img src="https://secure.gravatar.com/avatar/f606a0be81931b140017947c63373bba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmelo&#39;s gravatar image" />
<p><span>mmelo</span><br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mmelo has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Aug '12, 06:13</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-15563" class="comments-container">
&#10;</div>
<div id="comment-tools-15563" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15563-form-container" class="comment-form-container">
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

<span id="15593"></span>

<div id="answer-container-15593" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-15593-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15593-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-15593-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As the error message states, your apache does not have permission to access the socket file <code>/tmp/.s.PGSQL.5432</code> of your postgres server. Check that everybody has permission to read and write to this file. If not, change the settings for <code>unix_socket_permissions</code> in your psql config. Don't forget to check permissions for the directory as well.</p>
<p>Also check that your postgres is indeed using this socket (look for <code>unix_socket_directory</code> in your psql config) and running on port 5432 (see <code>port</code> in config). If it doesn't match something is wrong with your psql or php installation.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Aug '12, 20:07</strong></p>
<img src="https://secure.gravatar.com/avatar/d888b712d85dee0aa304297f2dc697c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lonvia&#39;s gravatar image" />
<p><span>lonvia</span><br />
<span class="score" title="6213 reputation points"><span>6.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lonvia has 43 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-15593" class="comments-container">
<span id="15982"></span>
<div id="comment-15982" class="comment">
<div id="post-15982-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>i figured it out, needed to disable selinux or open the 5432 port with semanage. thanks for pointing me in the right direction</p>
</div>
<div id="comment-15982-info" class="comment-info">
<span class="comment-age">(11 Sep '12, 21:44)</span> <span class="comment-user userinfo">mmelo</span>
</div>
</div>
</div>
<div id="comment-tools-15593" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15593-form-container" class="comment-form-container">
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

