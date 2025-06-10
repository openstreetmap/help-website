+++
type = "question"
title = "Overpass API dispatcher daemon running for Nginx"
description = '''In:  https://wiki.openstreetmap.org/wiki/Overpass_API/Installation I can read:  Setting up the Web API only for apache Is it possible dispatcher daemon running for Nginx? can you help me with an example of nginx.conf?  nginx.conf worker_processes 1;  events {  worker_connections 1024; } http {  incl...'''
date = "2016-08-13T17:59:00Z"
lastmod = "2016-08-15T09:13:00Z"
weight = 51390
keywords = [ "overpass", "nginx" ]
aliases = [ "/questions/51390" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Overpass API dispatcher daemon running for Nginx](/questions/51390/overpass-api-dispatcher-daemon-running-for-nginx)

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
<span id="post-51390-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51390-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-51390-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>In: <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Installation">https://wiki.openstreetmap.org/wiki/Overpass_API/Installation</a> I can read: Setting up the Web API only for apache Is it possible dispatcher daemon running for Nginx?</p>
<p>can you help me with an example of nginx.conf?</p>
<h1 id="nginx.conf">nginx.conf</h1>
<pre><code>worker_processes  1;</code></pre>
<p>events { worker_connections 1024; }</p>
<p>http { include mime.types;</p>
<pre><code>default_type  application/octet-stream;
sendfile        on;
keepalive_timeout  65;
&#10;server {
    listen       8000;
location /api/ {
    alias /mnt/data/openstreetmap/osm-3s_v0.7.4/cgi-bin/;
}
#
location /cgi-bin/ {
            gzip off;
            root /mnt/data/openstreetmap/osm-3s_v0.7.4/;
            fastcgi_read_timeout 900;
            fastcgi_pass unix:/var/run/fcgiwrap.socket;
            include /opt/nginx/fastcgi_params;
            fastcgi_param SCRIPT_FILENAME  $document_root$fastcgi_script_name;
    }
&#10;    location / {
        root   /mnt/data/openstreetmap/osm-3s_v0.7.4/html;
        index  index.html index.htm;
    }
}</code></pre>
<p>}</p>
<p>wget --output-document=test.xml <a href="http://localhost:8000/api/interpreter?data=%3Cprint%20mode=%22body%22/%3E">http://localhost:8000/api/interpreter?data=%3Cprint%20mode=%22body%22/%3E</a> --2016-08-14 18:07:38-- <a href="http://localhost:8000/api/interpreter?data=%3Cprint%20mode=%22body%22/%3E">http://localhost:8000/api/interpreter?data=%3Cprint%20mode=%22body%22/%3E</a> Petición HTTP enviada, esperando respuesta... 200 OK Longitud: 1983984 (1,9M) [application/octet-stream] Grabando a: “test.xml”</p>
<p>test.xml 100%[======================================================================&gt;] 1,89M --.-KB/s in 0,004s</p>
<p>2016-08-14 18:07:38 (488 MB/s) - “test.xml” guardado [1983984/19839</p>
<p>however in browser (Google chrome) remote: <strong>405 Not Allowed</strong></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-nginx" rel="tag" title="see questions tagged &#39;nginx&#39;">nginx</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Aug '16, 17:59</strong></p>
<img src="https://secure.gravatar.com/avatar/304bf9b97689c5eb6191600403aaf65b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="arcadio%20ortega&#39;s gravatar image" />
<p><span>arcadio ortega</span><br />
<span class="score" title="41 reputation points">41</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="arcadio ortega has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Aug '16, 17:19</strong> </span></p>
</div>
</div>
<div id="comments-container-51390" class="comments-container">
<span id="51411"></span>
<div id="comment-51411" class="comment">
<div id="post-51411-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>cross-posted: <a href="https://stackoverflow.com/questions/38944826/overpass-api-with-nginx">https://stackoverflow.com/questions/38944826/overpass-api-with-nginx</a></p>
</div>
<div id="comment-51411-info" class="comment-info">
<span class="comment-age">(15 Aug '16, 07:28)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-51390" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51390-form-container" class="comment-form-container">
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

<span id="51412"></span>

<div id="answer-container-51412" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-51412-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51412-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-51412-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>write this</p>
<pre><code>rewrite ^/api/(.+)$ /cgi-bin/$1 last;</code></pre>
<p>instead of</p>
<pre><code>location /api/ {
    alias /mnt/data/openstreetmap/osm-3s_v0.7.4/cgi-bin/;
}</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Aug '16, 09:13</strong></p>
<img src="https://secure.gravatar.com/avatar/304bf9b97689c5eb6191600403aaf65b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="arcadio%20ortega&#39;s gravatar image" />
<p><span>arcadio ortega</span><br />
<span class="score" title="41 reputation points">41</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="arcadio ortega has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-51412" class="comments-container">
&#10;</div>
<div id="comment-tools-51412" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51412-form-container" class="comment-form-container">
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

