+++
type = "question"
title = "tshark not displaying http traffic fully"
description = '''I am running tshark command as tshark -o &quot;ssl.desegment_ssl_records: TRUE&quot; -o &quot;ssl.desegment_ssl_application_data: TRUE&quot; -o &quot;ssl.keys_list:192.168.56.101,443,http,/etc/nginx/cert.key&quot; -o &quot;ssl.debug_file:/tmp/ssl.log&quot; tcp port 443 -R &quot;http.response or http.request&quot;  The output is something like this-...'''
date = "2014-10-22T15:07:00Z"
lastmod = "2014-10-22T15:07:00Z"
weight = 37296
keywords = [ "post", "capture-filter", "http", "postdissector", "display-filter" ]
aliases = [ "/questions/37296" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [tshark not displaying http traffic fully](/questions/37296/tshark-not-displaying-http-traffic-fully)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37296-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37296-score" class="post-score" title="current number of votes">0</div><span id="post-37296-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am running tshark command as</p><pre><code>tshark  -o &quot;ssl.desegment_ssl_records: TRUE&quot; -o &quot;ssl.desegment_ssl_application_data: TRUE&quot; -o &quot;ssl.keys_list:192.168.56.101,443,http,/etc/nginx/cert.key&quot; -o &quot;ssl.debug_file:/tmp/ssl.log&quot; tcp port 443  -R &quot;http.response or http.request&quot;</code></pre><p>The output is something like this-</p><pre><code>  6.183757 192.168.56.101 -&gt; 192.168.56.1 HTTP 1490 HTTP/1.1 200 OK  (application/x-javascript)
  6.329274 192.168.56.101 -&gt; 192.168.56.1 HTTP 960 HTTP/1.1 200 OK  (application/javascript)
  6.475231 192.168.56.101 -&gt; 192.168.56.1 HTTP 1349 HTTP/1.1 200 OK  (PNG)
  6.857929 192.168.56.101 -&gt; 192.168.56.1 HTTP 1444 HTTP/1.1 200 OK  (GIF89a)</code></pre><p>How do I go about displaying http form post data? I don't see a relevant field here- <a href="https://www.wireshark.org/docs/dfref/h/http.html">https://www.wireshark.org/docs/dfref/h/http.html</a></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-post" rel="tag" title="see questions tagged &#39;post&#39;">post</span> <span class="post-tag tag-link-capture-filter" rel="tag" title="see questions tagged &#39;capture-filter&#39;">capture-filter</span> <span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span> <span class="post-tag tag-link-postdissector" rel="tag" title="see questions tagged &#39;postdissector&#39;">postdissector</span> <span class="post-tag tag-link-display-filter" rel="tag" title="see questions tagged &#39;display-filter&#39;">display-filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Oct '14, 15:07</strong></p><img src="https://secure.gravatar.com/avatar/cc8c7b7305415e6eddfb4ba1fab236ba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gauravphoenix&#39;s gravatar image" /><p><span>gauravphoenix</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gauravphoenix has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>22 Oct '14, 15:21</strong> </span></p></div></div><div id="comments-container-37296" class="comments-container"></div><div id="comment-tools-37296" class="comment-tools"></div><div class="clear"></div><div id="comment-37296-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

