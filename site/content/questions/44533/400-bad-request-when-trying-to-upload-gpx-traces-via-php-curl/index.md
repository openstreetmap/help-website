+++
type = "question"
title = "400 Bad Request when trying to upload GPX traces via PHP curl"
description = '''i am using PHP - Curl to Upload GPX traces. $fields_file = &#x27;2004062.gpx&#x27;; $fields_description = &#x27;Sample Description&#x27;; $fields_tags = &#x27;public&#x27;; $fields_visibility = &#x27;public&#x27;;  $FF[&#x27;file&#x27;] = $fields_file; $FF[&#x27;description&#x27;] = $fields_description; $FF[&#x27;tags&#x27;] = $fields_tags; $FF[&#x27;visibility&#x27;] = $fields...'''
date = "2015-07-30T08:20:00Z"
lastmod = "2015-07-30T08:40:00Z"
weight = 44533
keywords = [ "php", "gpx", "upload" ]
aliases = [ "/questions/44533" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [400 Bad Request when trying to upload GPX traces via PHP curl](/questions/44533/400-bad-request-when-trying-to-upload-gpx-traces-via-php-curl)

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
<span id="post-44533-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44533-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-44533-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>i am using PHP - Curl to Upload GPX traces.</p>
<pre><code>$fields_file          = &#39;2004062.gpx&#39;;
$fields_description   = &#39;Sample Description&#39;;
$fields_tags          = &#39;public&#39;;
$fields_visibility    = &#39;public&#39;;
&#10;$FF[&#39;file&#39;]         = $fields_file;
$FF[&#39;description&#39;]  = $fields_description;
$FF[&#39;tags&#39;]         = $fields_tags;
$FF[&#39;visibility&#39;]   = $fields_visibility;
&#10;http_build_query($FF);
&#10;$OSMuser = &#39;csrm.xxxxxxx@gmail.com&#39;;
$OSMpass = &#39;xxxxxxx*&#39;;
$host    = &#39;http://api.openstreetmap.org/api/0.6/gpx/create&#39;;
$agent   = &#39;Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.0.3705; .NET CLR 1.1.4322)&#39;;
$process = curl_init($host);
curl_setopt($process, CURLOPT_HTTPHEADER, array(&quot;Content-type: multipart/form-data&quot;));
curl_setopt($process, CURLOPT_HEADER, 1);
curl_setopt($process, CURLOPT_USERPWD, $OSMuser . &quot;:&quot; . $OSMpass);
curl_setopt($process, CURLOPT_TIMEOUT, 30);
curl_setopt($process, CURLOPT_POST, 1);
curl_setopt($process, CURLOPT_POSTFIELDS, http_build_query($FF));
curl_setopt($process, CURLOPT_RETURNTRANSFER, TRUE);
curl_setopt($process, CURLOPT_USERAGENT, $agent);
$return = curl_exec($process);
curl_close($process);</code></pre>
<p>Response:</p>
<pre><code>string(472) &quot;HTTP/1.1 400 Bad Request
Date: Thu, 30 Jul 2015 06:29:14 GMT
Server: Apache/2.4.7 (Ubuntu)
Cache-Control: no-cache
Vary: Accept-Language,Origin
X-XSS-Protection: 1; mode=block
Content-Language: en
X-Request-Id: VbnEOn8AAQEAAG2TtpMAAAAZ
X-Runtime: 0.012558
X-Frame-Options: SAMEORIGIN
X-Content-Type-Options: nosniff
X-Powered-By: Phusion Passenger 5.0.14
Status: 400 Bad Request
Content-Length: 0
Connection: close
Content-Type: text/html; charset=utf-8</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-php" rel="tag" title="see questions tagged &#39;php&#39;">php</span> <span class="post-tag tag-link-gpx" rel="tag" title="see questions tagged &#39;gpx&#39;">gpx</span> <span class="post-tag tag-link-upload" rel="tag" title="see questions tagged &#39;upload&#39;">upload</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Jul '15, 08:20</strong></p>
<img src="https://secure.gravatar.com/avatar/8bcde4e7b2fd222eaf9c9498a0e12590?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="CSRM%20Kozhikode&#39;s gravatar image" />
<p><span>CSRM Kozhikode</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="CSRM Kozhikode has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Jul '15, 08:38</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-44533" class="comments-container">
<span id="44534"></span>
<div id="comment-44534" class="comment">
<div id="post-44534-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I don't know the reason for the 400 status code but you should not send a wrong user agent.</p>
</div>
<div id="comment-44534-info" class="comment-info">
<span class="comment-age">(30 Jul '15, 08:40)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-44533" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44533-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

