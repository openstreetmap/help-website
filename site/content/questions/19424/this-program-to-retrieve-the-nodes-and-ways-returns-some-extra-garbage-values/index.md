+++
type = "question"
title = "This program to retrieve the nodes and ways returns some extra garbage values..."
description = '''#include &amp;lt;iostream&amp;gt; #include &amp;lt;string&amp;gt; #include &amp;lt;vector&amp;gt; #include &amp;lt;cstdio&amp;gt; #include &amp;lt;stdlib.h&amp;gt; #include &amp;lt;winsock2.h&amp;gt; #define SIZE 10000  using namespace std;  const std::string host = &quot;81.19.81.199&quot;; // IP of overpass.osm.rambler.ru const int port = 80;  //(lower l...'''
date = "2013-01-30T06:35:00Z"
lastmod = "2013-01-30T09:20:00Z"
weight = 19424
keywords = [ "overpass", "request", "garbage" ]
aliases = [ "/questions/19424" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [This program to retrieve the nodes and ways returns some extra garbage values...](/questions/19424/this-program-to-retrieve-the-nodes-and-ways-returns-some-extra-garbage-values)

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
<span id="post-19424-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19424-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-19424-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<pre><code>#include &lt;iostream&gt;
#include &lt;string&gt;
#include &lt;vector&gt;
#include &lt;cstdio&gt;
#include &lt;stdlib.h&gt;
#include &lt;winsock2.h&gt;
#define SIZE 10000
&#10;using namespace std;
&#10;const std::string host  = &quot;81.19.81.199&quot;; // IP of overpass.osm.rambler.ru
const int port          = 80;
&#10;//(lower lat, usually lower lon, higher lat, usually higher lon).
const std::string query = &quot;GET /cgi/interpreter?data=[out:json];(node(18.51507,73.87276,18.53597,73.90142);way(18.51507,73.87276,18.53597,73.90142);node(w)-&gt;.x;);out; HTTP/1.1\r\n&quot;
                          &quot;Host: overpass.osm.rambler.ru\r\n&quot;
                          &quot;User-Agent: SteveC\r\n&quot;
                          &quot;Accept: */*\r\n&quot;
                          &quot;Connection: close\r\n&quot;
                          &quot;\r\n&quot;;
&#10;int main(int argc, char* argv[]) {
&#10;    FILE *fp = fopen (&quot;d://test.txt&quot;, &quot;r+&quot;);
&#10;    // Initialize Winsock.
    WSADATA wsadata;
    int iResult = WSAStartup (MAKEWORD(2,2), &amp;wsadata );
    if (iResult !=NO_ERROR )
        printf(&quot;\nmyERROR at WSAStartup()\n&quot;);
&#10;    int sock = socket(AF_INET, SOCK_STREAM, 0);
    if (sock == -1) {
        perror(&quot;error opening socket&quot;); return -1;
    }
&#10;    struct sockaddr_in sin;
    sin.sin_port = htons(port);
    sin.sin_addr.s_addr = inet_addr(host.c_str());
    sin.sin_family = AF_INET;
&#10;    if (connect(sock, (struct sockaddr *)&amp;sin, sizeof(sin)) == -1) {
        perror(&quot;error connecting to host&quot;); return -1;
    }
&#10;    const int query_len = query.length() + 1; // trailing &#39;\0&#39;
    if (send(sock, query.c_str(), query_len, 0) != query_len) {
        perror(&quot;error sending query&quot;); return -1;
    }
&#10;    const int buf_size = 1024 * 1024;
    while (true) {
        std::vector&lt;char&gt; buf(buf_size, &#39;\0&#39;);
        const int recv_len = recv(sock, &amp;buf[0], buf_size - 1, 0);
&#10;        if (recv_len == -1) {
            perror(&quot;error receiving response&quot;); return -1;
        } else if (recv_len == 0) {
            std::cout &lt;&lt; std::endl; break;
        } else {
            std::cout &lt;&lt; &amp;buf[0];
            fprintf(fp, &quot;%s&quot;, &amp;buf[0]);
        }
    }
&#10;    return 0;
}</code></pre>
<p>In this program some extra garbage values are inserted like :</p>
<pre><code>{
  &quot;type&quot;: &quot;node&quot;,
  &quot;id&quot;: 245647473,
  &quot;lat&quot;: 18.5289245,
  &quot;lon&quot;: 73.9019677,
  &quot;tags&quot;: {
    &quot;source&quot;: &quot;AND&quot;
  }
},
{
&#10;1000                         // garbage...
&#10;&quot;type&quot;: &quot;node&quot;,
  &quot;id&quot;: 245647482,
  &quot;lat&quot;: 18.5301753,
  &quot;lon&quot;: 73.8676588,
  &quot;tags&quot;: {
    &quot;source&quot;: &quot;AND&quot;
  }
},</code></pre>
<p>While executing the query in browser gives no problem. Earlier I thought there is some problem while writing to file, but the output by /<em>std::cout &lt;&lt; &amp;buf[0];</em>/ also gives the same result. Also the garbage value gets inserted in the same place every time I run the program. Why does it happen ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-request" rel="tag" title="see questions tagged &#39;request&#39;">request</span> <span class="post-tag tag-link-garbage" rel="tag" title="see questions tagged &#39;garbage&#39;">garbage</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Jan '13, 06:35</strong></p>
<img src="https://secure.gravatar.com/avatar/bd411afe7563961a31610b5f4d40dfd3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anubha&#39;s gravatar image" />
<p><span>Anubha</span><br />
<span class="score" title="31 reputation points">31</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anubha has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Jan '13, 06:41</strong> </span></p>
</div>
</div>
<div id="comments-container-19424" class="comments-container">
&#10;</div>
<div id="comment-tools-19424" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19424-form-container" class="comment-form-container">
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

<span id="19426"></span>

<div id="answer-container-19426" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-19426-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19426-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-19426-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Anubha has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Ah, that's my example code from <a href="/questions/18684/i-want-to-use-mainoverpass-api-for-retrieving-data-in-c-program">this question</a> with a little Winsock adjustments.</p>
<p>The number you see is not junk but the response is sent with <a href="https://en.wikipedia.org/wiki/Chunked_transfer_encoding">chunked transfer encoding</a> which you have to process first. This is just one of several possible transfer encodings which you SHOULD support in your program. As already explained in my answer to the other question you should better use a third-party library for HTTP traffic if you want a simple solution.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Jan '13, 06:43</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-19426" class="comments-container">
<span id="19428"></span>
<div id="comment-19428" class="comment">
<div id="post-19428-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you scai, its a real comfort to know those values are not junk, now that I know this I will support them in my parser happily. As for third-party library, for now JSON parser code I wrote works okay and renders pretty roads(with some nodes missing due to this encoding).In this month I coded the 3d car that is to travel these roads. Hope to complete the road stuff in feb. Your help so far is highly appreciated.</p>
</div>
<div id="comment-19428-info" class="comment-info">
<span class="comment-age">(30 Jan '13, 09:20)</span> <span class="comment-user userinfo">Anubha</span>
</div>
</div>
</div>
<div id="comment-tools-19426" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19426-form-container" class="comment-form-container">
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

