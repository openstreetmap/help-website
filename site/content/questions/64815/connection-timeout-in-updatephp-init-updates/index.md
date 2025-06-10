+++
type = "question"
title = "connection timeout in update.php --init-updates"
description = '''Hi,  Still I met connection timeout error while executing update.php --init-updates https://github.com/openstreetmap/Nominatim/issues/1083 Also tried after disabled ipv6, still met the same(https://stackoverflow.com/questions/4189973/file-get-contents-connection-timed-out ). Check my outputs:  php -...'''
date = "2018-07-20T12:55:00Z"
lastmod = "2018-07-22T11:20:00Z"
weight = 64815
keywords = [ "nominatim", "update", "php" ]
aliases = [ "/questions/64815" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [connection timeout in update.php --init-updates](/questions/64815/connection-timeout-in-updatephp-init-updates)

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
<span id="post-64815-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64815-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-64815-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>Still I met connection timeout error while executing <em>update.php --init-updates</em></p>
<p><a href="https://github.com/openstreetmap/Nominatim/issues/1083">https://github.com/openstreetmap/Nominatim/issues/1083</a></p>
<p>Also tried after disabled ipv6, still met the same(<a href="https://stackoverflow.com/questions/4189973/file-get-contents-connection-timed-out">https://stackoverflow.com/questions/4189973/file-get-contents-connection-timed-out</a> ).</p>
<p>Check my outputs:</p>
<blockquote>
<p><strong>php -r 'echo file_get_contents("https://download.geofabrik.de/europe/andorra-updates/state.txt");'</strong></p>
<p>Warning: file_get_contents(<a href="https://download.geofabrik.de/europe/andorra-updates/state.txt):">https://download.geofabrik.de/europe/andorra-updates/state.txt):</a> failed to open stream: Connection timed out in Command line code on line1</p>
<p><strong>curl "https://download.geofabrik.de/europe/andorra-updates/state.txt"</strong> original OSM minutely replication sequence number 3065501 timestamp=2018-07-19T20\:00\:02Z sequenceNumber=1948</p>
<p><strong>php -m</strong></p>
<p>[PHP Modules] Core ctype date dom ereg fileinfo filter hash iconv intl json libxml openssl pcre PDO pdo_pgsql pdo_sqlite pgsql Phar posix Reflection session SimpleXML SPL sqlite3 standard tokenizer xml xmlreader xmlwriter</p>
<p>[Zend Modules]</p>
</blockquote>
<p><a href="https://help.openstreetmap.org/users/150/mtmail">@mtmail</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-update" rel="tag" title="see questions tagged &#39;update&#39;">update</span> <span class="post-tag tag-link-php" rel="tag" title="see questions tagged &#39;php&#39;">php</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Jul '18, 12:55</strong></p>
<img src="https://secure.gravatar.com/avatar/1ffa52ca3632b5a0cf02b51459b7529b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rajavelu_M&#39;s gravatar image" />
<p><span>Rajavelu_M</span><br />
<span class="score" title="253 reputation points">253</span><span title="45 badges"><span class="badge1">●</span><span class="badgecount">45</span></span><span title="48 badges"><span class="silver">●</span><span class="badgecount">48</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rajavelu_M has one accepted answer">33%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Jul '18, 16:58</strong> </span></p>
</div>
</div>
<div id="comments-container-64815" class="comments-container">
<span id="64836"></span>
<div id="comment-64836" class="comment">
<div id="post-64836-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Does the connection timeout always occur or just sometimes? Are you familiar enough with wireshark or tcpdump to compare the failing php connection request against the succeeding curl connection request?</p>
</div>
<div id="comment-64836-info" class="comment-info">
<span class="comment-age">(21 Jul '18, 13:31)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="64851"></span>
<div id="comment-64851" class="comment">
<div id="post-64851-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/158/scai">@scai</a> : This connection timeout always occuring. Sorry i am not familiar with wireshark or tcpdump.</p>
</div>
<div id="comment-64851-info" class="comment-info">
<span class="comment-age">(22 Jul '18, 08:38)</span> <span class="comment-user userinfo">Rajavelu_M</span>
</div>
</div>
<span id="64855"></span>
<div id="comment-64855" class="comment">
<div id="post-64855-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Sounds like a problem caused by PHP. I guess you will find more help at StackOverflow. Specifically ask about the php command <code>file_get_contents()</code> from your question.</p>
</div>
<div id="comment-64855-info" class="comment-info">
<span class="comment-age">(22 Jul '18, 11:20)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-64815" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64815-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

